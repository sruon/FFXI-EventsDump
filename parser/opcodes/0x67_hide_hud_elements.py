from .base import ArgType, BaseOpcode, OpcodeArg


class HideHudElementsOpcode(BaseOpcode):

    opcode = 0x67
    name = "HIDE_HUD_ELEMENTS"

    def get_args(self):
        return [
            OpcodeArg("param1", ArgType.WORD, 2, ""),
            OpcodeArg("param2", ArgType.WORD, 2, ""),
        ]
