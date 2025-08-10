from .base import BaseOpcode


class EndReqStackOpcode(BaseOpcode):
    opcode = 0x00
    name = "END_REQSTACK"

    def get_args(self):
        return []  # No arguments

    def is_terminal(self) -> bool:
        return True
