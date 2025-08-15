from .base import ArgType, BaseOpcode, OpcodeArg


class UpdateEventPositionOpcode(BaseOpcode):

    opcode = 0x5A
    name = "UPDATE_EVENT_POSITION"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, "Position update mode"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        if offset + 2 > len(data):
            return 1

        mode = data[offset + 1]
        if mode == 0:
            return 8
        else:
            return 2

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        mode = args["mode"]

        if mode == 0:
            if len(raw_bytes) >= 8:
                import struct
                pos_x_raw = struct.unpack_from("<H", raw_bytes, 2)[0]
                pos_z_raw = struct.unpack_from("<H", raw_bytes, 4)[0]
                pos_y_raw = struct.unpack_from("<H", raw_bytes, 6)[0]

                pos_x_str = self.format_coordinate_value(pos_x_raw, context=context)
                pos_z_str = self.format_coordinate_value(pos_z_raw, context=context)
                pos_y_str = self.format_coordinate_value(pos_y_raw, context=context)

                return f"UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X={pos_x_str}, Z={pos_z_str}, Y={pos_y_str}"
            else:
                return "UPDATE_EVENT_POSITION: Set MovePosition (invalid data)"
        else:
            return "UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition"
