from .base import ArgType, BaseOpcode, OpcodeArg


class DeprecatedOpcodeOpcode(BaseOpcode):

    opcode = 0x6D
    name = "DEPRECATED_OPCODE"

    def get_args(self):
        return [
            OpcodeArg("unused1", ArgType.WORD, 2, ""),
            OpcodeArg("unused2", ArgType.WORD, 2, ""),
            OpcodeArg("unused3", ArgType.WORD, 2, ""),
        ]
