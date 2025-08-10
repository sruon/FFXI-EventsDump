"""Base class for wait-related opcodes."""

from .base import ArgType, BaseOpcode, OpcodeArg


class SimpleWaitBase(BaseOpcode):
    """Base for simple wait opcodes with a single work offset parameter."""

    wait_description = None  # Subclasses should define

    def get_args(self):
        return [
            OpcodeArg("wait_value", ArgType.WORD, 2, "Wait value work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        wait_str = self.format_work_area_value(args["wait_value"], context=context)
        if self.wait_description:
            return f"WAIT({wait_str} {self.wait_description})"
        return f"WAIT({wait_str})"
