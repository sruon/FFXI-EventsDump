from .base import BaseOpcode


class WaitEntityRenderFlagOpcode(BaseOpcode):
    opcode = 0x70
    name = "WAIT_ENTITY_RENDER_FLAG"

    def get_args(self):
        return []  # No arguments

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        return "WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)"
