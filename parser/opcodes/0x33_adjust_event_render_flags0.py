from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustEventRenderFlags0Opcode(BaseOpcode):
    opcode = 0x33
    name = "ADJUST_EVENT_RENDER_FLAGS0"

    def get_args(self):
        return [
            OpcodeArg("flag", ArgType.BYTE, 1, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None) -> str:

        flag = args["flag"]

        if flag & 0x80:
            operation = "^="
        elif flag & 0x01:
            operation = "|="
        else:
            operation = "&= ~"

        return f"EventEntity->Render.Flags0 {operation} 0x200000 // Bit 21 (flag=0x{flag:02X})"
