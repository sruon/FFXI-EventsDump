from .base import BaseOpcode


class WaitDialogSelectOpcode(BaseOpcode):
    opcode = 0x25
    name = "WAIT_DIALOG_SELECT"

    def get_args(self):
        return []
