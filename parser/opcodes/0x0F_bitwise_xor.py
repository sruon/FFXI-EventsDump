from .binary_op_base import BinaryOpBase


class BitwiseXorOpcode(BinaryOpBase):
    opcode = 0x0F
    name = "BITWISE_XOR"
    operator = "^="
