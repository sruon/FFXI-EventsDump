from .base import BaseOpcode


class UnsetEventNpcOpcode(BaseOpcode):
    opcode = 0x96
    name = "UNSET_EVENT_NPC"

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        return "UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)"
