from .base import BaseOpcode


class WaitDialogSelectAltOpcode(BaseOpcode):
    opcode = 0x7F
    name = "WAIT_DIALOG_SELECT_ALT"

    def get_args(self):
        return []  # No arguments
