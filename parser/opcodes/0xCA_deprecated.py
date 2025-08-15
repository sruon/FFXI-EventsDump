from .base import BaseOpcode


class DeprecatedOpcodeCA(BaseOpcode):
    opcode = 0xCA
    name = "DEPRECATED_OPCODE_CA"

    def calculate_length(self, data: bytes, offset: int) -> int:
        return 1
