from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags3Opcode(BaseOpcode):
    opcode = 0x86
    name = "ADJUST_RENDER_FLAGS3"

    def get_args(self):
        return [
            OpcodeArg("flag_value", ArgType.BYTE, 1, "Flag value to apply"),
            OpcodeArg("entity_id", ArgType.DWORD, 4, "Entity ID"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        entity_str = self.format_entity_id(args["entity_id"], context=context)
        if args["flag_value"] & 1:
            return f"{entity_str}->Render.Flags3 ^= 0x{args['flag_value']:02X}"
        else:
            return f"{entity_str}->Render.Flags3 = Flags3  // No change (flag=0)"
