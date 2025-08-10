from .base import ArgType, BaseOpcode, OpcodeArg


class OpenMapOpcode(BaseOpcode):

    opcode = 0x89
    name = "OPEN_MAP"

    def get_args(self):
        return [
            OpcodeArg("map_id", ArgType.WORD, 2, "Map ID to open"),
        ]
