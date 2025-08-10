from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags1Opcode(BaseOpcode):
    opcode = 0x74
    name = "ADJUST_RENDER_FLAGS1"

    def get_args(self):
        return [
            OpcodeArg("flag", ArgType.BYTE, 1, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None) -> str:
        flag = args["flag"]

        # Determine the operation based on the flag value
        if flag & 0x80:
            # High bit set means XOR operation
            operation = "^="
            actual_flag = flag & 0x7F
        else:
            # High bit clear means OR operation
            operation = "|="
            actual_flag = flag

        return f"EventEntity->Render.Flags1 {operation} 0x{actual_flag:02X}"
