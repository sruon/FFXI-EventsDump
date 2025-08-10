from .base import ArgType, BaseOpcode, OpcodeArg


class Atan2CalculationOpcode(BaseOpcode):

    opcode = 0x18
    name = "ATAN2_CALCULATION"

    def get_args(self):
        return [
            OpcodeArg("result", ArgType.WORD, 2, "Result work offset"),
            OpcodeArg("y_input", ArgType.WORD, 2, "Y coordinate work offset"),
            OpcodeArg("x_input", ArgType.WORD, 2, "X coordinate work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        result_str = self.format_work_area_value(args["result"], context=context)
        y_str = self.format_work_area_value(args["y_input"], context=context)
        x_str = self.format_work_area_value(args["x_input"], context=context)
        return f"{result_str} = atan2({y_str}, {x_str})"
