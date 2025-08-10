from .base import BaseOpcode


class SetEntityStatusEvent46Opcode(BaseOpcode):
    """Sets the event entities event status to 46 if valid"""

    opcode = 0x8F
    name = "SET_ENTITY_STATUS_EVENT_46"

    def get_args(self):
        return []  # No arguments
