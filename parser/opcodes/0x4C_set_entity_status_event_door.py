from .base import BaseOpcode


class SetEntityStatusEventDoorOpcode(BaseOpcode):
    """Sets entity status event to open door animation"""

    opcode = 0x4C
    name = "SET_ENTITY_STATUS_EVENT_DOOR"

    def get_args(self):
        return []  # No arguments

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        return "EventEntity->StatusEvent = 8 // Open door"
