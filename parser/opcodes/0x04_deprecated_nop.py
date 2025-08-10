from .base import ArgType, BaseOpcode, OpcodeArg


class DeprecatedNopOpcode(BaseOpcode):
    opcode = 0x04
    name = "DEPRECATED_NOP"

    def get_args(self):
        return [
            OpcodeArg("unused", ArgType.WORD, 2, "Unused parameter"),
        ]
