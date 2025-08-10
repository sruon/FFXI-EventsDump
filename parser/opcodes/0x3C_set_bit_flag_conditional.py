from .base import ArgType, BaseOpcode, OpcodeArg


class SetBitFlagConditionalOpcode(BaseOpcode):
    opcode = 0x3C
    name = "SET_BIT_FLAG_CONDITIONAL"

    def get_args(self):
        return [
            OpcodeArg("target_work_offset", ArgType.WORD, 2, ""),
            OpcodeArg("bit_index_work_offset", ArgType.WORD, 2, ""),
            OpcodeArg("condition_work_offset", ArgType.WORD, 2, ""),
        ]
