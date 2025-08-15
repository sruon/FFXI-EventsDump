from .base import BaseOpcode


class WaitEntityAnimationOpcode(BaseOpcode):
    opcode = 0x9B
    name = "WAIT_ENTITY_ANIMATION"

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        """Return descriptive text for waiting on animation."""
        return "Wait for EventEntity animation to complete"
