from .binary_op_base import BinaryOpBase


class BitwiseAndOpcode(BinaryOpBase):
    opcode = 0x0D
    name = "BITWISE_AND"
    operator = "&="
