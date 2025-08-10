from .base import ArgType, BaseOpcode, OpcodeArg


class CopyStringToArrayOpcode(BaseOpcode):
    opcode = 0xC3
    name = "COPY_STRING_TO_ARRAY"

    def get_args(self):
        return [
            OpcodeArg("array_index", ArgType.WORD, 2, "Array index for string destination"),
            OpcodeArg("string_value", ArgType.WORD, 2, "String value to copy"),
            OpcodeArg("additional_value", ArgType.WORD, 2, "Additional value parameter"),
        ]
