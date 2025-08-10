from .base import BaseOpcode


class SetEntityStatusEventCloseDoorOpcode(BaseOpcode):
    """Sets entity status event to close door animation"""

    opcode = 0x4D
    name = "SET_ENTITY_STATUS_EVENT_CLOSE_DOOR"

    def get_args(self):
        return []  # No arguments

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        return "EventEntity->StatusEvent = 9 // Close door"
