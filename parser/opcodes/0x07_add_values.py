from .binary_op_base import BinaryOpBase


class AddValuesOpcode(BinaryOpBase):
    opcode = 0x07
    name = "ADD_VALUES"
    operator = "+="
