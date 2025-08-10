from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags0Opcode(BaseOpcode):
    opcode = 0x2F
    name = "ADJUST_RENDER_FLAGS0"

    def get_args(self):
        return [
            OpcodeArg("flag", ArgType.BYTE, 1, ""),
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        flag = args["flag"]
        entity_id = args["entity_id"]

        entity_id_str = self.format_entity_id(entity_id, context=context)

        if flag & 0x01:
            operation = "|= 0x80000"
        else:
            operation = "&= ~0x80000"

        return f"{entity_id_str}->Render.Flags0 {operation} // Bit 19"
