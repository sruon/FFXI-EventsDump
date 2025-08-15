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
        def format_value(value):
            if 0x8000 <= value <= 0x8FFF:
                ref_index = value & 0x7FFF
                if context and context.imed_data and ref_index < len(context.imed_data):
                    return f"{context.imed_data[ref_index]}*"
                else:
                    return f"References[{ref_index}]"
            else:
                return str(value)

        start_bit_str = format_value(args["start_bit"])
        end_bit_str = format_value(args["end_bit"])
        source_str = self.format_work_area_value(args["source"], context=context)
        result_str = self.format_work_area_value(args["result"], context=context)

        return f"{result_str} = {source_str} (bits {start_bit_str}-{end_bit_str})"
