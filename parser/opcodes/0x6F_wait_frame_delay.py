from .base import BaseOpcode


class WaitFrameDelayOpcode(BaseOpcode):

    opcode = 0x6F
    name = "WAIT_FRAME_DELAY"

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        return "WAIT_FRAME_DELAY: Yield until WaitTime reaches zero"
