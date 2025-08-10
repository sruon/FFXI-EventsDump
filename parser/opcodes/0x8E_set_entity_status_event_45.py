from .base import BaseOpcode


class SetEntityStatusEvent45Opcode(BaseOpcode):
    """Sets the event entities event status to 45 if valid"""

    opcode = 0x8E
    name = "SET_ENTITY_STATUS_EVENT_45"

    def get_args(self):
        return []  # No arguments

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        """Generate a legible representation of the opcode."""
        return "EventEntity->StatusEvent = 45"
