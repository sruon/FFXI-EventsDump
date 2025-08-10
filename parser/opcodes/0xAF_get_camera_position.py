from .base import ArgType, BaseOpcode, OpcodeArg


class GetCameraPositionOpcode(BaseOpcode):
    opcode = 0xAF
    name = "GET_CAMERA_POSITION"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, ""),
            OpcodeArg("x", ArgType.WORD, 2, ""),
            OpcodeArg("z", ArgType.WORD, 2, ""),
            OpcodeArg("y", ArgType.WORD, 2, ""),
        ]
