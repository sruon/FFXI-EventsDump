"""
FFXI Event Code Parser - New Implementation

Parses FFXI event bytecode using the new opcode class system.
"""

from typing import Any

from .control_flow import ControlFlowAnalyzer
from .opcodes import EventInstruction, get_opcode_registry


class DataSection:
    """Pseudo-opcode for representing unreachable data sections."""

    opcode = 0xFF
    name = "DATA_SECTION"

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        preview_len = min(32, len(raw_bytes))
        hex_preview = " ".join(f"{b:02x}" for b in raw_bytes[:preview_len])
        if len(raw_bytes) > preview_len:
            hex_preview += f" ... ({len(raw_bytes)} bytes total)"
        return f"DATA_SECTION: {hex_preview}"

    def parse_args(self, raw_bytes: bytes):
        return {}

    def calculate_length(self, data: bytes, offset: int):
        return len(data)


class EventCodeParser:
    """Parses FFXI event bytecode using the new opcode system."""

    def __init__(self, use_control_flow: bool = False) -> None:
        self.registry = get_opcode_registry()
        self.use_control_flow = use_control_flow
        self.control_flow_data: dict[str, Any] | None = None
        self._data_section_impl = DataSection()

    def parse_event_data(self, event_data: bytes, entry_offset: int = 0) -> list[EventInstruction]:
        """Parse event bytecode into instructions."""
        # Analyze control flow if enabled
        data_sections = []
        if self.use_control_flow:
            analyzer = ControlFlowAnalyzer()
            self.control_flow_data = analyzer.analyze(event_data, entry_offset)
            data_sections = self.control_flow_data["data_sections"]

        instructions = []
        offset = 0

        # Convert data sections to dict for O(1) lookup
        data_section_map = dict(data_sections)

        while offset < len(event_data):
            # Check if we're at the start of a data section
            if offset in data_section_map:
                end = data_section_map[offset]
                data_bytes = event_data[offset:end]
                instructions.append(EventInstruction(0xFF, data_bytes, self._data_section_impl))
                offset = end
                continue

            # Parse regular instruction
            instruction, bytes_consumed = self._parse_instruction(event_data, offset)
            if instruction:
                instructions.append(instruction)
                offset += bytes_consumed
            else:
                offset += 1  # Skip unknown byte

        return instructions

    def _parse_instruction(self, data: bytes, offset: int) -> tuple[EventInstruction | None, int]:
        """Parse a single instruction at the given offset."""
        if offset >= len(data):
            return None, 0

        opcode_value = data[offset]
        opcode_impl = self.registry.get_opcode(opcode_value)

        if opcode_impl:
            length = opcode_impl.calculate_length(data, offset)
            if offset + length <= len(data):
                raw_bytes = data[offset : offset + length]
                return EventInstruction(opcode_value, raw_bytes, opcode_impl), length
            return None, 0

        # Unknown opcode - create minimal instruction
        return EventInstruction(opcode_value, data[offset : offset + 1], None), 1


