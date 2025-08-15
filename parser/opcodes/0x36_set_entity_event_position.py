from .base import ArgType, BaseOpcode, OpcodeArg


class SetEntityEventPositionOpcode(BaseOpcode):
    opcode = 0x36
    name = "SET_ENTITY_EVENT_POSITION"

    def get_args(self):
        return [
            OpcodeArg("x_position", ArgType.WORD, 2, ""),
            OpcodeArg("z_position", ArgType.WORD, 2, ""),
            OpcodeArg("y_position", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        x_str = self.format_coordinate_value(args["x_position"], context=context)
        z_str = self.format_coordinate_value(args["z_position"], context=context)
        y_str = self.format_coordinate_value(args["y_position"], context=context)

        return f"{self.name}(pos_x={x_str}, pos_z={z_str}, pos_y={y_str})"
