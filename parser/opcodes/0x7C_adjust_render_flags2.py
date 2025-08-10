from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags2Opcode(BaseOpcode):
    opcode = 0x7C
    name = "ADJUST_RENDER_FLAGS2"

    def get_args(self):
        return [
            OpcodeArg("enable_flag", ArgType.BYTE, 1, ""),
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None) -> str:
        enable_flag = args["enable_flag"]
        entity_id = args["entity_id"]

        entity_str = self.format_entity_id(entity_id, context=context)
        if enable_flag & 0x80:
            # High bit set means XOR operation
            operation = "^="
            actual_flag = enable_flag & 0x7F
        else:
            # High bit clear means OR operation
            operation = "|="
            actual_flag = enable_flag

        return f"{entity_str}->Render.Flags2 {operation} 0x{actual_flag:02X}"
