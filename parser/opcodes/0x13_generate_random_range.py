from .base import ArgType, BaseOpcode, OpcodeArg


class GenerateRandomRangeOpcode(BaseOpcode):

    opcode = 0x13
    name = "GENERATE_RANDOM_RANGE"

    def get_args(self):
        return [
            OpcodeArg("target", ArgType.WORD, 2, "Target work offset to store result"),
            OpcodeArg("max_value", ArgType.WORD, 2, "Maximum value for random generation"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        target_str = self.format_work_area_value(args["target"], context=context)
        max_str = self.format_work_area_value(args["max_value"], context=context)
        return f"{target_str} = rand() % {max_str}"
