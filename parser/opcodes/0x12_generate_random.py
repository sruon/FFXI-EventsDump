from .base import ArgType, BaseOpcode, OpcodeArg


class GenerateRandomOpcode(BaseOpcode):
    opcode = 0x12
    name = "GENERATE_RANDOM"

    def get_args(self):
        return [
            OpcodeArg("target", ArgType.WORD, 2, "Target work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        target = self.format_work_area_value(args["target"], context=context)
        return f"{target} = rand()"
