from .base import ArgType, BaseOpcode, OpcodeArg


class PartyStateCheckOpcode(BaseOpcode):
    opcode = 0xC2
    name = "PARTY_STATE_CHECK"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, "Mode for party state check"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on mode."""
        if offset + 2 > len(data):
            return 1  # Fallback

        mode = data[offset + 1]
        if mode == 1:
            # Mode 1: Build mask of visitable party members (4 bytes)
            return 4
        elif mode == 2:
            # Mode 2: Check if party member house is valid/open (6 bytes)
            return 6
        else:
            # Other modes: 2 bytes
            return 2

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        mode = args["mode"]

        if mode == 1:
            # Mode 1: Build mask of valid party members that can be visited
            if len(raw_bytes) >= 4:
                import struct

                dest_offset = struct.unpack_from("<H", raw_bytes, 2)[0]
                dest_str = self.format_work_area_value(dest_offset, context=context)
                return f"PARTY_STATE_CHECK: {dest_str} = mask of visitable party members"
            else:
                return "PARTY_STATE_CHECK: Build visitable party mask (invalid data)"

        elif mode == 2:
            # Mode 2: Check if selected party member's house is valid/open
            if len(raw_bytes) >= 6:
                import struct

                mask_offset = struct.unpack_from("<H", raw_bytes, 2)[0]
                result_offset = struct.unpack_from("<H", raw_bytes, 4)[0]
                mask_str = self.format_work_area_value(mask_offset, context=context)
                result_str = self.format_work_area_value(result_offset, context=context)
                return f"PARTY_STATE_CHECK: {result_str} = check if party member (from {mask_str}) house is open"
            else:
                return "PARTY_STATE_CHECK: Check party house validity (invalid data)"
        else:
            return f"PARTY_STATE_CHECK: Unknown mode {mode:#02x}"
