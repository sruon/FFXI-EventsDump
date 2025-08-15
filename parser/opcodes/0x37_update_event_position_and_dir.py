from .base import ArgType, BaseOpcode, OpcodeArg


class UpdateEventPositionAndDirOpcode(BaseOpcode):
    opcode = 0x37
    name = "UPDATE_EVENT_POSITION_AND_DIR"

    def get_args(self):
        return [
            OpcodeArg("x", ArgType.WORD, 2, ""),
            OpcodeArg("z", ArgType.WORD, 2, ""),
            OpcodeArg("y", ArgType.WORD, 2, ""),
            OpcodeArg("dir", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        x_str = self.format_coordinate_value(args["x"], context=context)
        z_str = self.format_coordinate_value(args["z"], context=context)
        y_str = self.format_coordinate_value(args["y"], context=context)
        dir_str = self.format_direction_value(args["dir"], context=context)

        return f"UPDATE_EVENT_POSITION_AND_DIR: x={x_str}, z={z_str}, y={y_str}, direction={dir_str}"
