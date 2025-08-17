from .base import ArgType, BaseOpcode, OpcodeArg


class ClearBitFlagConditionalOpcode(BaseOpcode):
    opcode = 0x3D
    name = "CLEAR_BIT_FLAG_CONDITIONAL"

    def get_args(self):
        return [
            OpcodeArg("target_work_offset", ArgType.WORD, 2, ""),
            OpcodeArg("bit_index_work_offset", ArgType.WORD, 2, ""),
            OpcodeArg("condition_work_offset", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        target = self.format_work_area_value(args["target_work_offset"], context=context)
        bit_index = self.format_work_area_value(args["bit_index_work_offset"], context=context)
        condition = self.format_work_area_value(args["condition_work_offset"], context=context)

        return f"{self.name}(target_work_offset={target}, bit_index_work_offset={bit_index}, condition_work_offset={condition})"
