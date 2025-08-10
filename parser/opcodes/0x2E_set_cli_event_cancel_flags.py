from .base import BaseOpcode


class SetCliEventCancelFlagsOpcode(BaseOpcode):
    opcode = 0x2E
    name = "SET_CLI_EVENT_CANCEL_FLAGS"

    def get_args(self):
        return []  # No arguments
