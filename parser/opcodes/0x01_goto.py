from .base import ArgType, BaseOpcode, OpcodeArg


class GotoOpcode(BaseOpcode):
    opcode = 0x01
    name = "GOTO"

    def get_args(self):
        return [OpcodeArg("offset", ArgType.WORD, 2, "Target offset to jump to")]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        return f"GOTO 0x{args['offset']:04X}"

    def get_jump_targets(self, args: dict, context=None) -> list:
        return [args["offset"]]

    def is_terminal(self) -> bool:
        return True
