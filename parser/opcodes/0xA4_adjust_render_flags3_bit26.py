from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags3Bit26Opcode(BaseOpcode):
    opcode = 0xA4
    name = "ADJUST_RENDER_FLAGS3_BIT26"

    def get_args(self):
        return [
            OpcodeArg("flag_value", ArgType.BYTE, 1, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        value = args["flag_value"]

        # This sets bit 26 (unknown_3_2 field)
        # The operation: Flags3 ^= (Flags3 ^ (value << 26)) & 0x4000000
        # This effectively sets bit 26 to the LSB of value
        if value & 1:
            return "EventEntity->Flags3.unknown_3_2 = 1"
        else:
            return "EventEntity->Flags3.unknown_3_2 = 0"
