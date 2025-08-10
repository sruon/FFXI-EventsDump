from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags1MultiOpcode(BaseOpcode):
    opcode = 0x60
    name = "ADJUST_RENDER_FLAGS1_MULTI"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on mode parameter."""
        if offset + 2 > len(data):
            return 1  # Fallback

        mode = data[offset + 1]
        if mode <= 1:  # Modes 0-1: 4 bytes total
            return 4  # 1 + 1 + 2
        elif mode == 2:  # Mode 2: 6 bytes total
            return 6  # 1 + 1 + 4
        else:  # Other modes: 2 bytes total (deprecated/skip)
            return 2  # 1 + 1

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        mode = args["mode"]

        if mode <= 1:
            # Modes 0-1: Adjust Render.Flags1
            if len(raw_bytes) >= 4:
                import struct

                flags_value = struct.unpack_from("<H", raw_bytes, 2)[0]
                flags_str = self.format_work_area_value(flags_value, context=context)

                if mode == 0:
                    # Mode 0: Clear bit 0x80 and OR with flags_value
                    return f"EventEntity->Render.Flags1 = (Flags1 & ~0x80) | {flags_str}"
                else:
                    # Mode 1: Set bit 0x80 and OR with flags_value
                    return f"EventEntity->Render.Flags1 = (Flags1 | 0x80) | {flags_str}"
            else:
                return f"ADJUST_RENDER_FLAGS1_MULTI: Invalid data for mode {mode}"

        elif mode == 2:
            # Mode 2: Zone action call
            if len(raw_bytes) >= 6:
                import struct

                param = struct.unpack_from("<I", raw_bytes, 2)[0]
                param_str = self.format_work_area_value(param, context=context)
                return f"ZONE_SET_ACTION: Set zone action with param {param_str}"
            else:
                return "ADJUST_RENDER_FLAGS1_MULTI: Invalid data for mode 2"
        else:
            # Deprecated/unknown modes
            return f"ADJUST_RENDER_FLAGS1_MULTI: Deprecated mode {mode:#02x} (no operation)"
