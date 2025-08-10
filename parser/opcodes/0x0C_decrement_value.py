from .unary_op_base import UnaryOpBase


class DecrementValueOpcode(UnaryOpBase):
    opcode = 0x0C
    name = "DECREMENT_VALUE"
    suffix = "--"
