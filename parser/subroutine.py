from dataclasses import dataclass, field


@dataclass
class Instruction:
    num: int
    offset: int
    opcode: int
    description: str
    raw_bytes: bytes = b""


@dataclass
class Subroutine:
    start_offset: int
    end_offset: int
    instructions: list[Instruction] = field(default_factory=list)
    is_entry_point: bool = False

    @property
    def label(self) -> str:
        if self.is_entry_point:
            return None
        return f"SUBROUTINE_{self.start_offset:04X}"


@dataclass
class DataSection:
    offset: int
    size: int
    data: bytes

    def format_hex_dump(self) -> list[str]:
        lines = [f"# Data Section: 0x{self.offset:04X} ({self.size} bytes)"]
        for i in range(0, len(self.data), 16):
            chunk = self.data[i : i + 16]
            hex_str = " ".join(f"{b:02X}" for b in chunk)
            lines.append(f"     0x{self.offset + i:04X}: {hex_str}")
        return lines


@dataclass
class DeadCode:
    instructions: list[Instruction] = field(default_factory=list)

    def format_lines(self) -> list[str]:
        lines = ["# Dead code (unreachable instructions):"]
        for inst in self.instructions:
            lines.append(f"     0x{inst.offset:04X} [0x{inst.opcode:02X}] {inst.description}")
        return lines


@dataclass
class EventCode:
    event_id: int | str
    event_index: int
    total_events: int
    offset: int
    data_size: int
    calculated_size: int

    subroutines: list[Subroutine] = field(default_factory=list)
    data_sections: list[DataSection] = field(default_factory=list)
    dead_code_sections: list[DeadCode] = field(default_factory=list)

    @property
    def total_instructions(self) -> int:
        return sum(len(sub.instructions) for sub in self.subroutines)
