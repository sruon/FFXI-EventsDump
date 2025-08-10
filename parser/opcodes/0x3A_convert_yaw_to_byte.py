from .base import ArgType, BaseOpcode, OpcodeArg


class ConvertYawToByteOpcode(BaseOpcode):
    opcode = 0x3A
    name = "CONVERT_YAW_TO_BYTE"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
            OpcodeArg("result_destination", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        entity_str = self.format_entity_id(args["entity_id"], context=context)
        result_str = self.format_work_area_value(args["result_destination"], context=context)

        return f"{self.name}(entity={entity_str}, result_destination={result_str})"
