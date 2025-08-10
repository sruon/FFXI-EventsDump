from .base import ArgType, BaseOpcode, OpcodeArg


class SetBitWorkRangeOpcode(BaseOpcode):
    opcode = 0x40
    name = "SET_BIT_WORK_RANGE"

    def get_args(self):
        return [
            OpcodeArg("start_bit", ArgType.WORD, 2, ""),
            OpcodeArg("end_bit", ArgType.WORD, 2, ""),
            OpcodeArg("target", ArgType.WORD, 2, ""),
            OpcodeArg("source", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        start_bit_str = self.format_work_area_value(args["start_bit"], context=context)
        end_bit_str = self.format_work_area_value(args["end_bit"], context=context)
        target_str = self.format_work_area_value(args["target"], context=context)
        source_str = self.format_work_area_value(args["source"], context=context)

        return f"{self.name}(start_bit={start_bit_str}, end_bit={end_bit_str}, target={target_str}, source={source_str})"
