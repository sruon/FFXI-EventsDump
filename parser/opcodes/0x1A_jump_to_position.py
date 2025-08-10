from .base import ArgType, BaseOpcode, OpcodeArg


class JumpToPositionOpcode(BaseOpcode):
    opcode = 0x1A
    name = "JUMP_TO_POSITION"

    def get_args(self):
        return [
            OpcodeArg("offset", ArgType.WORD, 2, "Jump destination offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        return f"CALL_SUBROUTINE(address=0x{args['offset']:04X})"

    def get_jump_targets(self, args: dict, context=None) -> list:
        return [args["offset"]]
