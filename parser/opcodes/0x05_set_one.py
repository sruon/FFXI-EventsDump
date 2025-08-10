from .unary_op_base import UnaryOpBase


class SetOneOpcode(UnaryOpBase):
    opcode = 0x05
    name = "SET_ONE"
    assignment = "= 1"
