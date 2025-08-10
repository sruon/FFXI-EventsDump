from .base import ArgType, BaseOpcode, OpcodeArg


class SetEntityDirectionOpcode(BaseOpcode):
    opcode = 0x39
    name = "SET_ENTITY_DIRECTION"

    def get_args(self):
        return [
            OpcodeArg("direction", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        direction = args["direction"]

        if 0x8000 <= direction <= 0x8FFF:
            ref_index = direction & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                degrees = (ref_value / 65536.0) * 360.0
                direction_str = f"{degrees:.1f}°*"
            else:
                direction_str = f"References[{ref_index}]"
        else:
            degrees = (direction / 65536.0) * 360.0
            direction_str = f"{degrees:.1f}°"

        return f"{self.name}(direction={direction_str})"
