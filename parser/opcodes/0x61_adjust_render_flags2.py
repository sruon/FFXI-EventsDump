from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags2Opcode(BaseOpcode):
    opcode = 0x61
    name = "ADJUST_RENDER_FLAGS2"

    def get_args(self):
        return [
            OpcodeArg("flag_value", ArgType.BYTE, 1, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        flag_value = args["flag_value"]

        # Based on docs: Sets bit 0 of Render.Flags2 based on LSB of flag_value
        if flag_value & 1:
            return "EventEntity->Render.Flags2 |= 0x00000001"
        else:
            return "EventEntity->Render.Flags2 &= ~0x00000001"
