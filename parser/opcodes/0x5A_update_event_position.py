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

                if 0x8000 <= pos_x_raw <= 0x8FFF:
                    ref_index = pos_x_raw & 0x7FFF
                    if context and context.imed_data and ref_index < len(context.imed_data):
                        actual_x = context.imed_data[ref_index]
                        if actual_x > 0x80000000:
                            actual_x = struct.unpack("<i", struct.pack("<I", actual_x))[0]
                        pos_x_str = f"{actual_x * 0.001:.3f}*"
                    else:
                        pos_x_str = f"References[{ref_index}]"
                else:
                    pos_x_str = self.format_work_area_value(pos_x_raw, context=context)

                if 0x8000 <= pos_z_raw <= 0x8FFF:
                    ref_index = pos_z_raw & 0x7FFF
                    if context and context.imed_data and ref_index < len(context.imed_data):
                        actual_z = context.imed_data[ref_index]
                        if actual_z > 0x80000000:
                            actual_z = struct.unpack("<i", struct.pack("<I", actual_z))[0]
                        pos_z_str = f"{actual_z * 0.001:.3f}*"
                    else:
                        pos_z_str = f"References[{ref_index}]"
                else:
                    pos_z_str = self.format_work_area_value(pos_z_raw, context=context)

                if 0x8000 <= pos_y_raw <= 0x8FFF:
                    ref_index = pos_y_raw & 0x7FFF
                    if context and context.imed_data and ref_index < len(context.imed_data):
                        actual_y = context.imed_data[ref_index]
                        if actual_y > 0x80000000:
                            actual_y = struct.unpack("<i", struct.pack("<I", actual_y))[0]
                        pos_y_str = f"{actual_y * 0.001:.3f}*"
                    else:
                        pos_y_str = f"References[{ref_index}]"
                else:
                    pos_y_str = self.format_work_area_value(pos_y_raw, context=context)

                return f"UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X={pos_x_str}, Z={pos_z_str}, Y={pos_y_str}"
            else:
                return "UPDATE_EVENT_POSITION: Set MovePosition (invalid data)"
        else:
            return "UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition"
