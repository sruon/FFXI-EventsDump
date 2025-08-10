from .base import ArgType, BaseOpcode, OpcodeArg


class GetAppFlagOpcode(BaseOpcode):

    opcode = 0xB1
    name = "GET_APP_FLAG"

    def get_args(self):
        return [
            OpcodeArg("flag_type", ArgType.BYTE, 1, ""),
            OpcodeArg("dest_offset", ArgType.WORD, 2, ""),
        ]
