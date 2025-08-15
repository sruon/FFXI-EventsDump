from .base import BaseOpcode


class DeprecatedOpcodeCB(BaseOpcode):
    opcode = 0xCB
    name = "DEPRECATED_OPCODE_CB"

    def calculate_length(self, data: bytes, offset: int) -> int:
        return 1
