from .binary_op_base import BinaryOpBase


class DivideValuesOpcode(BinaryOpBase):
    opcode = 0x15
    name = "DIVIDE_VALUES"
    operator = "/="
