"""Base class for scheduler-related opcodes."""

from .base import BaseOpcode


class SchedulerBase(BaseOpcode):
    """Base class for scheduler opcodes with common scheduler ID formatting."""

    def format_scheduler_id(self, scheduler_id: int) -> str:
        """Format a scheduler ID value, attempting ASCII decoding."""
        scheduler_bytes = scheduler_id.to_bytes(4, byteorder="little")
        try:
            scheduler_str = scheduler_bytes.decode("ascii").rstrip("\x00")
            if scheduler_str and all(32 <= ord(c) <= 126 for c in scheduler_str):
                return f'"{scheduler_str}"'
        except (UnicodeDecodeError, ValueError):
            pass
        return f"0x{scheduler_id:08X}"
