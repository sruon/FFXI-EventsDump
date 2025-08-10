from .base import ArgType, BaseOpcode, OpcodeArg


class RequestEventMapNumberOpcode(BaseOpcode):
    opcode = 0xA6
    name = "REQUEST_EVENT_MAP_NUMBER"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on mode."""
        if offset + 1 >= len(data):
            return 2

        mode = data[offset + 1]
        if mode == 2:
            # Mode 2 has additional work offset parameter
            return 4
        else:
            # Default/Mode 1
            return 2

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None) -> str:
        mode = args["mode"]

        if mode == 2:
            # Mode 2: Store current SubMapNum to work area
            if len(raw_bytes) >= 4:
                import struct

                work_offset = struct.unpack_from("<H", raw_bytes, 2)[0]
                work_str = self.format_work_area_value(work_offset, context=context)
                return f"REQUEST_EVENT_MAP_NUMBER: {work_str} = CurrentSubMapNum (mode 2)"
            else:
                return "REQUEST_EVENT_MAP_NUMBER: Store SubMapNum (invalid data)"
        else:
            # Mode 1 or default: Just request the map number
            return f"REQUEST_EVENT_MAP_NUMBER: Request map info from server (mode {mode}) (0x00EB packet)"
