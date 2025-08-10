from .binary_op_base import BinaryOpBase


class BitwiseOrOpcode(BinaryOpBase):
    opcode = 0x0E
    name = "BITWISE_OR"
    operator = "|="
