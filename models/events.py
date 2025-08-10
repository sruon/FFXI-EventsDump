from dataclasses import dataclass

from construct import Aligned, Array, Bytes, Int16ul, Int32ul, Struct, this

EventHeader = Struct(
    "block_count" / Int32ul,
    "block_sizes" / Array(this.block_count, Int32ul),
)

EventBlock = Struct(
    "actor_number" / Int32ul,  # Entity Server Id
    "tag_count" / Int32ul,  # Event count
    "tag_offsets" / Array(this.tag_count, Int16ul),  # Event offset table
    "event_exec_nums" / Array(this.tag_count, Int16ul),  # Event id table
    "imed_count" / Int32ul,  # Event immediate data count
    "imed_data" / Array(this.imed_count, Int32ul),  # Event immediate data table
    "event_data_size" / Int32ul,  # Event data size
    "event_data" / Aligned(4, Bytes(this.event_data_size)),  # Event data (4-byte aligned)
)

EventDat = Struct(
    "header" / EventHeader,
    "blocks" / Array(this.header.block_count, EventBlock),
)


@dataclass
class ParsedEventBlock:
    actor_number: int
    tag_count: int
    tag_offsets: list[int]
    event_exec_nums: list[int]
    imed_count: int
    imed_data: list[int]
    event_data_size: int
    event_data: bytes

    @classmethod
    def from_construct(cls, block_data) -> "ParsedEventBlock":
        return cls(
            actor_number=block_data.actor_number,
            tag_count=block_data.tag_count,
            tag_offsets=list(block_data.tag_offsets),
            event_exec_nums=list(block_data.event_exec_nums),
            imed_count=block_data.imed_count,
            imed_data=list(block_data.imed_data),
            event_data_size=block_data.event_data_size,
            event_data=block_data.event_data,
        )

    def get_event_by_id(self, event_id: int) -> tuple[int, bytes]:
        try:
            index = self.event_exec_nums.index(event_id)
            offset = self.tag_offsets[index]
            return (offset, self.event_data[offset:])
        except (ValueError, IndexError):
            return None

    def get_all_events(self) -> list[tuple[int, int, bytes]]:
        events = []
        for i, event_id in enumerate(self.event_exec_nums):
            offset = self.tag_offsets[i]
            # Calculate data length (to next offset or end)
            if i + 1 < len(self.tag_offsets):
                next_offset = self.tag_offsets[i + 1]
                data = self.event_data[offset:next_offset]
            else:
                data = self.event_data[offset:]
            events.append((event_id, offset, data))
        return events

    def __str__(self) -> str:
        return (
            f"ParsedEventBlock(actor={self.actor_number}, events={self.tag_count}, "
            f"imed_count={self.imed_count}, data_size={self.event_data_size})"
        )


@dataclass
class ParsedEventDat:

    block_count: int
    block_sizes: list[int]
    blocks: list[ParsedEventBlock]

    @classmethod
    def from_construct(cls, parsed_data) -> "ParsedEventDat":
        blocks = [ParsedEventBlock.from_construct(block) for block in parsed_data.blocks]
        return cls(
            block_count=parsed_data.header.block_count,
            block_sizes=list(parsed_data.header.block_sizes),
            blocks=blocks,
        )

    def get_block_by_actor(self, actor_number: int) -> ParsedEventBlock | None:
        for block in self.blocks:
            if block.actor_number == actor_number:
                return block
        return None

    def get_all_actors(self) -> list[int]:
        return [block.actor_number for block in self.blocks]

    def get_total_events(self) -> int:
        return sum(block.tag_count for block in self.blocks)

    def __str__(self) -> str:
        total_size = sum(block.event_data_size for block in self.blocks)
        return f"ParsedEventDat(blocks={self.block_count}, total_events={self.get_total_events()}, total_size={total_size} bytes)"
