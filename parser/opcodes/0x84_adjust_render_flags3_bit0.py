from .base import BaseOpcode


class AdjustRenderFlags3Bit0Opcode(BaseOpcode):
    opcode = 0x84
    name = "ADJUST_RENDER_FLAGS3_BIT0"

    def get_args(self):
        return []  # No arguments, single byte opcode
