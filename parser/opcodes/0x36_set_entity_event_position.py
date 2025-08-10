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
        def format_position(value):
            if 0x8000 <= value <= 0x8FFF:
                ref_index = value & 0x7FFF
                if context and context.imed_data and ref_index < len(context.imed_data):
                    ref_value = context.imed_data[ref_index]
                    float_value = self.convert_coordinate_to_float(ref_value)
                    return f"{float_value:.3f}*"
                else:
                    return f"References[{ref_index}]"
            else:
                return self.format_work_area_value(value, context=context)

        x_str = format_position(args["x_position"])
        z_str = format_position(args["z_position"])
        y_str = format_position(args["y_position"])

        return f"{self.name}(pos_x={x_str}, pos_z={z_str}, pos_y={y_str})"
