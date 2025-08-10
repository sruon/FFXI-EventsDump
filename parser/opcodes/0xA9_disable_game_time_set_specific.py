from .base import ArgType, BaseOpcode, OpcodeArg


class DisableGameTimeSetSpecificOpcode(BaseOpcode):
    opcode = 0xA9
    name = "DISABLE_GAME_TIME_SET_SPECIFIC"

    def get_args(self):
        return [
            OpcodeArg("time_offset", ArgType.WORD, 2, ""),
        ]
