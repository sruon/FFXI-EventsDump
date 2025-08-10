from .base import ArgType, BaseOpcode, OpcodeArg


class SwapValuesOpcode(BaseOpcode):

    opcode = 0x19
    name = "SWAP_VALUES"

    def get_args(self):
        return [
            OpcodeArg("first_offset", ArgType.WORD, 2, "First work offset"),
            OpcodeArg("second_offset", ArgType.WORD, 2, "Second work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        first_str = self.format_work_area_value(args["first_offset"], context=context)
        second_str = self.format_work_area_value(args["second_offset"], context=context)
        return f"SWAP({first_str}, {second_str})"
