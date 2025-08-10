from .base import ArgType, BaseOpcode, OpcodeArg


class OpenMapWindowOpcode(BaseOpcode):
    opcode = 0xC8
    name = "OPEN_MAP_WINDOW"

    def get_args(self):
        return [
            OpcodeArg("zone", ArgType.WORD, 2, "Zone ID for map"),
            OpcodeArg("submap", ArgType.WORD, 2, "Submap ID"),
            OpcodeArg("flag", ArgType.WORD, 2, "Flag parameter"),
        ]
