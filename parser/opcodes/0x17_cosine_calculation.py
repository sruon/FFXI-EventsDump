from .base import ArgType, BaseOpcode, OpcodeArg


class CosineCalculationOpcode(BaseOpcode):

    opcode = 0x17
    name = "COSINE_CALCULATION"

    def get_args(self):
        return [
            OpcodeArg("result", ArgType.WORD, 2, "Result work offset"),
            OpcodeArg("input", ArgType.WORD, 2, "Input work offset"),
            OpcodeArg("multiplier", ArgType.WORD, 2, "Multiplier work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        result_str = self.format_work_area_value(args["result"], context=context)
        input_str = self.format_work_area_value(args["input"], context=context)
        multiplier_str = self.format_work_area_value(args["multiplier"], context=context)
        return f"{result_str} = cos({input_str}) * {multiplier_str}"
