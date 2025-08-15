from .base import BaseOpcode


class AdjustEntityRenderFlags0Flags1Opcode(BaseOpcode):
    opcode = 0x90
    name = "ADJUST_ENTITY_RENDER_FLAGS0_FLAGS1"

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        """Generate a legible representation of the opcode."""
        return "EventEntity->Render.Flags0 |= 0x04; EventEntity->Render.Flags1 |= 0x08"
