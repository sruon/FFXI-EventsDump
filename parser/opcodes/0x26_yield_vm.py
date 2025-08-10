from .base import BaseOpcode


class YieldVmOpcode(BaseOpcode):
    opcode = 0x26
    name = "YIELD_VM"

    def get_args(self):
        return []  # No arguments

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        return "DEPRECATED_YIELD"

    def is_terminal(self) -> bool:
        return True
