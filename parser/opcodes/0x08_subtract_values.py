from .binary_op_base import BinaryOpBase


class SubtractValuesOpcode(BinaryOpBase):
    opcode = 0x08
    name = "SUBTRACT_VALUES"
    operator = "-="
