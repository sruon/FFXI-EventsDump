from .base import BaseOpcode


class ReturnFromJumpOpcode(BaseOpcode):
    opcode = 0x1B
    name = "RETURN_FROM_JUMP"

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        return "RETURN"

    def is_terminal(self) -> bool:
        return True
