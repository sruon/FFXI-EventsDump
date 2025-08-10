from .binary_op_base import BinaryOpBase


class BitwiseLeftShiftOpcode(BinaryOpBase):
    opcode = 0x10
    name = "BITWISE_LEFT_SHIFT"
    operator = "<<="
