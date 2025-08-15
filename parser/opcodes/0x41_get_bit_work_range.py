from .base import ArgType, BaseOpcode, OpcodeArg


class GetBitWorkRangeOpcode(BaseOpcode):
    opcode = 0x41
    name = "GET_BIT_WORK_RANGE"

    def get_args(self):
        return [
            OpcodeArg("start_bit", ArgType.WORD, 2, ""),
            OpcodeArg("end_bit", ArgType.WORD, 2, ""),
            OpcodeArg("source", ArgType.WORD, 2, ""),
            OpcodeArg("result", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        start_bit_str = self.format_work_area_value(args["start_bit"], context=context)
        end_bit_str = self.format_work_area_value(args["end_bit"], context=context)
        source_str = self.format_work_area_value(args["source"], context=context)
        result_str = self.format_work_area_value(args["result"], context=context)

        return f"{result_str} = {source_str} (bits {start_bit_str}-{end_bit_str})"
