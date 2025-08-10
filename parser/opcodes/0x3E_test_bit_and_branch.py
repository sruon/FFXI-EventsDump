from .base import ArgType, BaseOpcode, OpcodeArg


class TestBitAndBranchOpcode(BaseOpcode):
    opcode = 0x3E
    name = "TEST_BIT_AND_BRANCH"

    def get_args(self):
        return [
            OpcodeArg("target_work_offset", ArgType.WORD, 2, ""),
            OpcodeArg("bit_index_work_offset", ArgType.WORD, 2, ""),
            OpcodeArg("jump_offset", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        target_str = self.format_work_area_value(args["target_work_offset"], context=context)
        bit_index_str = self.format_work_area_value(args["bit_index_work_offset"], context=context)
        return f"IF !({target_str} bit {bit_index_str}) GOTO 0x{args['jump_offset']:04X}"

    def get_jump_targets(self, args: dict, context=None) -> list:
        return [args["jump_offset"]]
