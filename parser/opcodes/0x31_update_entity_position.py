from .base import ArgType, BaseOpcode, OpcodeArg


class UpdateEntityPositionOpcode(BaseOpcode):
    opcode = 0x31
    name = "UPDATE_ENTITY_POSITION"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on mode parameter."""
        if offset + 2 > len(data):
            return 1  # Fallback

        mode = data[offset + 1]
        if mode == 0:  # Mode 0: set goal position (10 bytes total)
            return 10  # 1 + 1 + 8 (4x WORD for pos_x, pos_z, pos_y, move_time)
        elif mode == 0x01:  # Mode 1: update movement (2 bytes total)
            return 2  # 1 + 1
        else:
            # Unknown mode - assume it might have position data
            return 10

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        mode = args["mode"]

        if mode == 0:
            # Mode 0: Set goal position - parse additional parameters
            if len(raw_bytes) >= 10:
                import struct

                pos_x_raw = struct.unpack_from("<H", raw_bytes, 2)[0]
                pos_z_raw = struct.unpack_from("<H", raw_bytes, 4)[0]
                pos_y_raw = struct.unpack_from("<H", raw_bytes, 6)[0]
                move_time_raw = struct.unpack_from("<H", raw_bytes, 8)[0]

                # Use the standardized coordinate formatting methods
                pos_x_str = self.format_coordinate_value(pos_x_raw, context)
                pos_z_str = self.format_coordinate_value(pos_z_raw, context)
                pos_y_str = self.format_coordinate_value(pos_y_raw, context)

                # Move time - just resolve work area
                move_time_str = self.format_work_area_value(move_time_raw, context=context)

                return f"UPDATE_ENTITY_POSITION: Set EventEntity goal position to X={pos_x_str}, Z={pos_z_str}, Y={pos_y_str}, Time={move_time_str}"
            else:
                return "UPDATE_ENTITY_POSITION: Set goal position (invalid data)"
        elif mode == 0x01:
            # Mode 1: Update movement towards goal
            return "UPDATE_ENTITY_POSITION: Move EventEntity towards goal position"
        else:
            # Unknown mode - try to parse as position data if length allows
            if len(raw_bytes) >= 10:
                import struct

                pos_x_raw = struct.unpack_from("<H", raw_bytes, 2)[0]
                pos_z_raw = struct.unpack_from("<H", raw_bytes, 4)[0]
                pos_y_raw = struct.unpack_from("<H", raw_bytes, 6)[0]
                move_time_raw = struct.unpack_from("<H", raw_bytes, 8)[0]

                # Use the standardized coordinate formatting methods
                pos_x_str = self.format_coordinate_value(pos_x_raw, context)
                pos_z_str = self.format_coordinate_value(pos_z_raw, context)
                pos_y_str = self.format_coordinate_value(pos_y_raw, context)

                # Move time - just resolve work area
                move_time_str = self.format_work_area_value(move_time_raw, context=context)

                return f"UPDATE_ENTITY_POSITION: Set EventEntity goal position to X={pos_x_str}, Z={pos_z_str}, Y={pos_y_str}, Time={move_time_str} (mode 0x{mode:02X})"
            else:
                return f"UPDATE_ENTITY_POSITION: Unknown mode 0x{mode:02X}"
