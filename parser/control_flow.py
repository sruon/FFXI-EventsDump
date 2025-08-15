"""
Control Flow Analyzer for FFXI Event Code using networkx.
"""

from dataclasses import dataclass
from typing import Any

import networkx as nx

from parser.opcodes import get_opcode_registry


@dataclass
class BasicBlock:
    """A basic block in the control flow graph."""

    start_offset: int
    end_offset: int
    instructions: list[int]
    is_terminal: bool = False
    is_branch: bool = False


class ControlFlowAnalyzer:
    """Analyzes control flow using networkx directed graph."""

    def __init__(self):
        self.graph = nx.DiGraph()
        self.registry = get_opcode_registry()
        self.entry_offset = 0
        self.blocks_by_offset: dict[int, BasicBlock] = {}

    def analyze(self, event_data: bytes, entry_offset: int = 0) -> dict[str, Any]:
        """
        Analyze control flow in event bytecode.

        Returns dict with reachable_offsets, data_sections, jump_targets
        """
        self.entry_offset = entry_offset
        self.graph.clear()
        self.blocks_by_offset.clear()

        # Build CFG
        blocks = self._identify_basic_blocks(event_data)
        self._index_blocks(blocks)
        self._build_graph(event_data, blocks)

        # Get reachable offsets
        reachable_offsets = self._get_reachable_offsets(event_data)

        # Identify data sections
        data_sections = self._identify_data_sections(event_data, reachable_offsets)

        # Extract jump targets
        jump_targets = self._get_all_jump_targets(event_data)

        return {
            "reachable_offsets": reachable_offsets,
            "data_sections": data_sections,
            "jump_targets": jump_targets,
        }

    def _index_blocks(self, blocks: list[BasicBlock]):
        """Build index for O(1) block lookup."""
        self.blocks_by_offset.clear()
        for block in blocks:
            self.blocks_by_offset[block.start_offset] = block

    def _get_instruction_info(self, event_data: bytes, offset: int) -> tuple[Any | None, int, list[int]]:
        """Get opcode implementation, length, and jump targets for instruction at offset."""
        if offset >= len(event_data):
            return None, 1, []

        opcode = event_data[offset]
        opcode_impl = self.registry.get_opcode(opcode)

        if not opcode_impl:
            return None, 1, []

        length = opcode_impl.calculate_length(event_data, offset) or 1

        if offset + length > len(event_data):
            return opcode_impl, length, []

        # Get jump targets
        raw_bytes = event_data[offset : offset + length]
        args = opcode_impl.parse_args(raw_bytes)
        targets = opcode_impl.get_jump_targets(args)

        # Convert to data offsets
        result = []
        for target in targets:
            data_offset = target - self.entry_offset
            if 0 <= data_offset < len(event_data):
                result.append(data_offset)

        return opcode_impl, length, result

    def _identify_basic_blocks(self, event_data: bytes) -> list[BasicBlock]:
        block_starts = {0}

        offset = 0
        while offset < len(event_data):
            opcode_impl, length, targets = self._get_instruction_info(event_data, offset)

            block_starts.update(targets)

            if opcode_impl:
                if targets and not opcode_impl.is_terminal():
                    if offset + length < len(event_data):
                        block_starts.add(offset + length)

                elif opcode_impl.is_terminal() and offset + length < len(event_data):
                    block_starts.add(offset + length)

            offset += length

        sorted_starts = sorted(block_starts)
        blocks = []
        for i, start in enumerate(sorted_starts):
            end = sorted_starts[i + 1] if i + 1 < len(sorted_starts) else len(event_data)
            blocks.append(BasicBlock(start, end, list(range(start, end))))

        return blocks

    def _get_last_instruction_offset(self, event_data: bytes, block: BasicBlock) -> int | None:
        """Get offset of last instruction in block."""
        last_offset = None
        offset = block.start_offset

        while offset < block.end_offset and offset < len(event_data):
            opcode_impl, length, _ = self._get_instruction_info(event_data, offset)
            if opcode_impl:
                last_offset = offset
            offset += length

        return last_offset

    def _build_graph(self, event_data: bytes, blocks: list[BasicBlock]):
        """Build the control flow graph - simplified."""
        # Add all blocks as nodes
        for block in blocks:
            self.graph.add_node(block.start_offset, block=block)

        # Add edges based on control flow
        for block in blocks:
            last_offset = self._get_last_instruction_offset(event_data, block)
            if last_offset is None:
                continue

            opcode_impl, _, targets = self._get_instruction_info(event_data, last_offset)

            # Add edges to jump targets
            for target in targets:
                if target in self.blocks_by_offset:
                    self.graph.add_edge(block.start_offset, target)

            # Add fall-through edge if not terminal
            if not opcode_impl or not opcode_impl.is_terminal():
                if block.end_offset in self.blocks_by_offset:
                    self.graph.add_edge(block.start_offset, block.end_offset)
            else:
                # Special case: END_EVENT (0x21) can fall through to END_REQSTACK (0x00)
                if last_offset < len(event_data) and event_data[last_offset] == 0x21:
                    opcode_impl, length, _ = self._get_instruction_info(event_data, last_offset)
                    next_offset = last_offset + length
                    if next_offset < len(event_data) and event_data[next_offset] == 0x00:
                        if block.end_offset in self.blocks_by_offset:
                            self.graph.add_edge(block.start_offset, block.end_offset)

                block.is_terminal = True

    def _get_reachable_offsets(self, event_data: bytes) -> set[int]:
        """Get all reachable byte offsets - optimized."""
        if 0 not in self.graph:
            return set()

        # Get reachable blocks
        reachable_blocks = nx.descendants(self.graph, 0)
        reachable_blocks.add(0)

        # Collect all offsets from reachable blocks
        reachable = set()
        for block_start in reachable_blocks:
            if block_start in self.graph.nodes:
                block = self.graph.nodes[block_start]["block"]
                reachable.update(block.instructions)

        max_iterations = 100
        iteration = 0
        while iteration < max_iterations:
            iteration += 1
            initial_size = len(reachable)

            reachable_jump_targets = self._get_reachable_jump_targets(event_data, reachable)
            for target in reachable_jump_targets:
                if target in self.blocks_by_offset:
                    self._add_block_and_descendants(target, reachable, reachable_blocks)
                else:
                    self._trace_forward_from_offset(target, event_data, reachable)
            if len(reachable) == initial_size:
                break
        reachable_copy = list(reachable)
        for offset in reachable_copy:
            if offset < len(event_data):
                opcode = event_data[offset]
                if opcode in [0x21, 0x1B]:
                    _, length, _ = self._get_instruction_info(event_data, offset)
                    next_offset = offset + length
                    if next_offset < len(event_data) and event_data[next_offset] == 0x00:
                        reachable.add(next_offset)
                        for block_start in self.blocks_by_offset:
                            block = self.blocks_by_offset[block_start]
                            if block.start_offset <= next_offset < block.end_offset:
                                reachable.update(block.instructions)
                                break

        return reachable

    def _add_block_and_descendants(self, target, reachable, reachable_blocks):
        """Add a block and all its descendants to the reachable sets."""
        target_block = self.blocks_by_offset[target]
        reachable.update(target_block.instructions)
        reachable_blocks.add(target)

        if target in self.graph:
            for desc in nx.descendants(self.graph, target):
                if desc in self.blocks_by_offset:
                    desc_block = self.blocks_by_offset[desc]
                    reachable.update(desc_block.instructions)
                    reachable_blocks.add(desc)

    def _trace_forward_from_offset(self, start_offset, event_data, reachable):
        """Trace forward from an offset until a terminal instruction."""
        reachable.add(start_offset)
        offset = start_offset

        while offset < len(event_data):
            opcode_impl, length, _ = self._get_instruction_info(event_data, offset)
            if not opcode_impl:
                break

            reachable.update(range(offset, offset + length))
            if opcode_impl.is_terminal():
                break
            offset += length

    def _get_all_jump_targets(self, event_data: bytes) -> set[int]:
        """Get all jump targets in the bytecode."""
        return self._collect_jump_targets(event_data, filter_reachable=None)

    def _get_reachable_jump_targets(self, event_data: bytes, reachable_offsets: set[int]) -> set[int]:
        """Get jump targets only from reachable code."""
        return self._collect_jump_targets(event_data, filter_reachable=reachable_offsets)

    def _collect_jump_targets(self, event_data: bytes, filter_reachable=None) -> set[int]:
        """Collect jump targets with optional reachability filter."""
        targets = set()
        offset = 0

        while offset < len(event_data):
            if filter_reachable is None or offset in filter_reachable:
                _, length, jump_targets = self._get_instruction_info(event_data, offset)
                targets.update(jump_targets)
                offset += length
            else:
                offset += 1

        return targets

    def _identify_data_sections(self, event_data: bytes, reachable: set[int]) -> list[tuple[int, int]]:
        data_sections = set()
        offset = 0
        while offset < len(event_data):
            if offset not in reachable:
                offset += 1
                continue

            opcode = event_data[offset]
            if opcode == 0x9D and offset + 1 < len(event_data):
                subcase = event_data[offset + 1]

                if subcase == 0x00 and offset + 3 < len(event_data):
                    table_addr = int.from_bytes(event_data[offset + 2 : offset + 4], byteorder="little")
                    data_offset = table_addr - self.entry_offset
                    if 0 <= data_offset < len(event_data):
                        end_offset = data_offset + 2
                        while end_offset < len(event_data) and end_offset not in reachable:
                            end_offset += 2
                            if end_offset - data_offset > 256:
                                break
                        data_sections.add((data_offset, min(end_offset, len(event_data))))

                elif subcase == 0x01 and offset + 3 < len(event_data):
                    event_offset = int.from_bytes(event_data[offset + 2 : offset + 4], byteorder="little")
                    data_offset = event_offset - self.entry_offset
                    if 0 <= data_offset < len(event_data):
                        data_sections.add((data_offset, min(data_offset + 16, len(event_data))))

                elif subcase == 0x02 and offset + 3 < len(event_data):
                    event_offset = int.from_bytes(event_data[offset + 2 : offset + 4], byteorder="little")
                    data_offset = event_offset - self.entry_offset
                    if 0 <= data_offset < len(event_data):
                        end_offset = data_offset + 1
                        while end_offset < len(event_data) and end_offset not in reachable:
                            end_offset += 1
                        data_sections.add((data_offset, end_offset))

                elif subcase in [0x05, 0x06] and offset + 3 < len(event_data):
                    table_addr = int.from_bytes(event_data[offset + 2 : offset + 4], byteorder="little")
                    data_offset = table_addr - self.entry_offset
                    if 0 <= data_offset < len(event_data):
                        end_offset = data_offset + 2
                        while end_offset < len(event_data) and end_offset not in reachable:
                            end_offset += 2
                            if end_offset - data_offset > 256:
                                break
                        data_sections.add((data_offset, min(end_offset, len(event_data))))

                elif subcase == 0x07 and offset + 3 < len(event_data):
                    jump_table = int.from_bytes(event_data[offset + 2 : offset + 4], byteorder="little")
                    data_offset = jump_table - self.entry_offset
                    if 0 <= data_offset < len(event_data):
                        end_offset = data_offset + 2
                        while end_offset < len(event_data) and end_offset not in reachable:
                            end_offset += 2
                            if end_offset - data_offset > 256:
                                break
                        data_sections.add((data_offset, min(end_offset, len(event_data))))

            opcode_impl = self.registry.get_opcode(opcode)
            if opcode_impl:
                length = opcode_impl.calculate_length(event_data, offset) or 1
            else:
                length = 1
            offset += length

        sorted_sections = sorted(data_sections)
        merged = []
        for start, end in sorted_sections:
            if merged and start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))

        return merged
