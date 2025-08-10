from .base import BaseOpcode


class CloseMapOpcode(BaseOpcode):

    opcode = 0x8A
    name = "CLOSE_MAP"

    def get_args(self):
        return []  # No arguments
