from .unary_op_base import UnaryOpBase


class IncrementValueOpcode(UnaryOpBase):
    opcode = 0x0B
    name = "INCREMENT_VALUE"
    suffix = "++"
