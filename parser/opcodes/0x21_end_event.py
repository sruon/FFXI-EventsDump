from .base import BaseOpcode


class EndEventOpcode(BaseOpcode):
    opcode = 0x21
    name = "END_EVENT"

    def get_args(self):
        return []  # No arguments

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        return "END_EVENT"

    def is_terminal(self) -> bool:
        return True
