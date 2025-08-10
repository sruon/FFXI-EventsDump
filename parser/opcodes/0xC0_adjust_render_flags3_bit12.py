from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags3Bit12Opcode(BaseOpcode):
    opcode = 0xC0
    name = "ADJUST_RENDER_FLAGS3_BIT12"

    def get_args(self):
        return [
            OpcodeArg("flag_value", ArgType.WORD, 2, "Flag value for bit 12 manipulation"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        flag_value = args["flag_value"]

        # Resolve reference if needed
        resolved_value, was_reference = self.resolve_reference_value(flag_value, context)

        # Format the display string
        flag_str = self.format_work_area_value(flag_value, context=context)

        # If we successfully resolved the value, check its LSB
        if was_reference and resolved_value != flag_value:
            if resolved_value & 1:
                return f"EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from {flag_str})"
            else:
                return f"EventEntity->Render.Flags3 &= ~0x1000 // Clear bit 12 (from {flag_str})"
        elif not was_reference:
            # Direct value - check the LSB
            if flag_value & 1:
                return "EventEntity->Render.Flags3 |= 0x1000 // Set bit 12"
            else:
                return "EventEntity->Render.Flags3 &= ~0x1000 // Clear bit 12"
        else:
            # Reference that couldn't be resolved
            return f"EventEntity->Render.Flags3: Set bit 12 based on LSB of {flag_str}"
