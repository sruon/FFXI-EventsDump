from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags3Opcode(BaseOpcode):
    opcode = 0x92
    name = "ADJUST_RENDER_FLAGS3"

    def get_args(self):
        return [
            OpcodeArg("flag", ArgType.BYTE, 1, "Flag value to apply"),
            OpcodeArg("entity_id", ArgType.ENTITY_ID, 4, "Entity ID to adjust flags for"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        flag = args["flag"]
        entity_id = args["entity_id"]

        entity_id_str = self.format_entity_id(entity_id, context=context)

        # Similar to 0x86, XORs Render.Flags3 with the flag value
        if flag:
            return f"{entity_id_str}->Render.Flags3 ^= 0x{flag:02X}"
        else:
            return f"{entity_id_str}->Render.Flags3 = Flags3  // No change (flag=0)"
