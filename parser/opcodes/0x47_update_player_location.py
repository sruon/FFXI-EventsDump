import struct

from .base import ArgType, BaseOpcode, OpcodeArg


class UpdatePlayerLocationOpcode(BaseOpcode):
    opcode = 0x47
    name = "UPDATE_PLAYER_LOCATION"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, "Update mode"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        if offset + 2 > len(data):
            return 1
        return 10 if data[offset + 1] == 0 else 2

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        mode = args["mode"]

        if mode == 0 and len(raw_bytes) >= 10:
            pos_x = self.format_coordinate_value(struct.unpack_from("<H", raw_bytes, 2)[0], context)
            pos_z = self.format_coordinate_value(struct.unpack_from("<H", raw_bytes, 4)[0], context)
            pos_y = self.format_coordinate_value(struct.unpack_from("<H", raw_bytes, 6)[0], context)
            yaw_raw = struct.unpack_from("<H", raw_bytes, 8)[0]

            if yaw_raw == 0x0F11:
                yaw = "ExtData[1]->EventDir[1] * 360.0 / 65536.0"
            else:
                yaw = self.format_direction_value(yaw_raw, context)

            return f"UPDATE_PLAYER_POS({pos_x}, {pos_z}, {pos_y}, yaw={yaw})"

        return "WAIT_PLAYER_POS_UPDATE" if mode != 0 else "UPDATE_PLAYER_POS()"
