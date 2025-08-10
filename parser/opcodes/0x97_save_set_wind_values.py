from .base import ArgType, BaseOpcode, OpcodeArg


class SaveSetWindValuesOpcode(BaseOpcode):
    opcode = 0x97
    name = "SAVE_SET_WIND_VALUES"

    def get_args(self):
        return [
            OpcodeArg("wind_base", ArgType.WORD, 2, ""),
            OpcodeArg("wind_width", ArgType.WORD, 2, ""),
        ]
