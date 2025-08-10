from .binary_op_base import BinaryOpBase


class BitwiseRightShiftOpcode(BinaryOpBase):
    opcode = 0x11
    name = "BITWISE_RIGHT_SHIFT"
    operator = ">>="
