from .base import ArgType, BaseOpcode, OpcodeArg


class ModuloOperationOpcode(BaseOpcode):
    opcode = 0x3F
    name = "MODULO_OPERATION"

    def get_args(self):
        return [
            OpcodeArg("target", ArgType.WORD, 2, ""),
            OpcodeArg("dividend", ArgType.WORD, 2, ""),
            OpcodeArg("divisor", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        target = self.format_work_area_value(args["target"], context=context)
        dividend = self.format_work_area_value(args["dividend"], context=context)
        divisor = self.format_work_area_value(args["divisor"], context=context)

        return f"{target} = {dividend} % {divisor}"
