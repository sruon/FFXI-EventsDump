from .base import ArgType, BaseOpcode, OpcodeArg


class ClearBitFlagConditionalOpcode(BaseOpcode):
    opcode = 0x3D
    name = "CLEAR_BIT_FLAG_CONDITIONAL"

    def get_args(self):
        return [
            OpcodeArg("target_work_offset", ArgType.WORD, 2, ""),
            OpcodeArg("bit_index_work_offset", ArgType.WORD, 2, ""),
            OpcodeArg("condition_work_offset", ArgType.WORD, 2, ""),
        ]
