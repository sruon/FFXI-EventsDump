from .base import ArgType, BaseOpcode, OpcodeArg


class MapEditMarkerFromBufferOpcode(BaseOpcode):
    opcode = 0xB9
    name = "MAP_EDIT_MARKER_FROM_BUFFER"

    def get_args(self):
        return [
            OpcodeArg("map_flag", ArgType.BYTE, 1, ""),
            OpcodeArg("zone", ArgType.WORD, 2, ""),
            OpcodeArg("submap", ArgType.WORD, 2, ""),
            OpcodeArg("marker_id", ArgType.WORD, 2, ""),
        ]
