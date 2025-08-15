from .base import BaseOpcode


class EndReqStackOpcode(BaseOpcode):
    opcode = 0x00
    name = "END_REQSTACK"

    def is_terminal(self) -> bool:
        return True
