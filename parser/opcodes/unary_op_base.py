"""Base class for unary operation opcodes."""

from .base import ArgType, BaseOpcode, OpcodeArg


class UnaryOpBase(BaseOpcode):
    """Base for opcodes that operate on a single value."""

    suffix = None  # e.g., '++', '--'
    assignment = None  # e.g., '= 0', '= 1'

    def __init__(self):
        super().__init__()

    def get_args(self):
        return [
            OpcodeArg("target", ArgType.WORD, 2, "Target work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        target = self.format_work_area_value(args["target"], context=context)
        if self.suffix:
            return f"{target}{self.suffix}"
        elif self.assignment:
            return f"{target} {self.assignment}"
        raise ValueError(f"No operation defined for {self.__class__.__name__}")
