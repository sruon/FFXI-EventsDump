from .base import BaseOpcode


class OpenMoogleMenuOpcode(BaseOpcode):
    opcode = 0x85
    name = "OPEN_MOOGLE_MENU"

    def get_args(self):
        return []  # No arguments
