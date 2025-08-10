from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustRenderFlags3Bit11Opcode(BaseOpcode):
    opcode = 0xA5
    name = "ADJUST_RENDER_FLAGS3_BIT11"

    def get_args(self):
        return [
            OpcodeArg("flag_value", ArgType.BYTE, 1, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        value = args["flag_value"]

        # This sets bit 11 which is bit 3 of the BallistaTeam field (bits 8-15)
        # The operation: Flags3 ^= (Flags3 ^ (value << 11)) & 0x800
        # This effectively sets bit 11 to the LSB of value
        if value & 1:
            return "EventEntity->Flags3.BallistaTeam |= 0x08  // Set bit 3 of BallistaTeam"
        else:
            return "EventEntity->Flags3.BallistaTeam &= ~0x08  // Clear bit 3 of BallistaTeam"
