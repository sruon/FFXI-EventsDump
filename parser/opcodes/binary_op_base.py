"""Base class for binary operation opcodes."""

from .base import ArgType, BaseOpcode, OpcodeArg


class BinaryOpBase(BaseOpcode):
    """Base for opcodes that perform dest op= source."""

    operator = None  # Subclasses must define

    def __init__(self):
        super().__init__()

    def get_args(self):
        return [
            OpcodeArg("dest_value", ArgType.WORD, 2, "Destination work offset"),
            OpcodeArg("source_value", ArgType.WORD, 2, "Source work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        if not self.operator:
            raise ValueError(f"Operator not defined for {self.__class__.__name__}")
        dest = self.format_work_area_value(args["dest_value"], context=context)
        source = self.format_work_area_value(args["source_value"], context=context)
        return f"{dest} {self.operator} {source}"
