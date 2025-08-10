from .binary_op_base import BinaryOpBase


class MultiplyValuesOpcode(BinaryOpBase):
    opcode = 0x14
    name = "MULTIPLY_VALUES"
    operator = "*="
