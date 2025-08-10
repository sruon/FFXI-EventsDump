from .base import ArgType, BaseOpcode, OpcodeArg


class SetBitFlagOpcode(BaseOpcode):
    opcode = 0x09
    name = "SET_BIT_FLAG"

    def get_args(self):
        return [
            OpcodeArg("target", ArgType.WORD, 2, "Target work offset"),
            OpcodeArg("bit_position", ArgType.WORD, 2, "Bit position work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        target_str = self.format_work_area_value(args["target"], context=context)
        bit_position_str = self.format_work_area_value(args["bit_position"], context=context)
        return f"{target_str} |= (1 << {bit_position_str})"
