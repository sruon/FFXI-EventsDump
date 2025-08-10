from .unary_op_base import UnaryOpBase


class SetZeroOpcode(UnaryOpBase):
    opcode = 0x06
    name = "SET_ZERO"
    assignment = "= 0"
