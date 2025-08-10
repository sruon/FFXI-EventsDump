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
        def format_coord_value(value, is_direction=False):
            if 0x8000 <= value <= 0x8FFF:
                ref_index = value & 0x7FFF
                if context and context.imed_data and ref_index < len(context.imed_data):
                    ref_value = context.imed_data[ref_index]
                    if is_direction:
                        degrees = self.convert_direction_to_degrees(ref_value)
                        return f"{degrees:.1f}°*"
                    else:
                        float_val = self.convert_coordinate_to_float(ref_value)
                        return f"{float_val:.3f}*"
                else:
                    return f"References[{ref_index}]"
            else:
                return self.format_work_area_value(value, context=context)

        x_str = format_coord_value(args["x"])
        z_str = format_coord_value(args["z"])
        y_str = format_coord_value(args["y"])
        dir_str = format_coord_value(args["dir"], is_direction=True)

        return f"UPDATE_EVENT_POSITION_AND_DIR: x={x_str}, z={z_str}, y={y_str}, direction={dir_str}"
