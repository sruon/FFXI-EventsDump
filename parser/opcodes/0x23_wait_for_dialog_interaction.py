from .base import BaseOpcode


class WaitForDialogInteractionOpcode(BaseOpcode):
    opcode = 0x23
    name = "WAIT_FOR_DIALOG_INTERACTION"

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        return "WAIT_FOR_DIALOG_INTERACTION"
