from .base import ArgType, BaseOpcode, OpcodeArg


class Calculate3dDistanceOpcode(BaseOpcode):
    opcode = 0x65
    name = "CALCULATE_3D_DISTANCE"

    def get_args(self):
        return [
            OpcodeArg("result", ArgType.WORD, 2, ""),
            OpcodeArg("entity1", ArgType.DWORD, 4, ""),
            OpcodeArg("entity2", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        result_work_str = self.format_work_area_value(args["result"], context=context)
        entity1_str = self.format_entity_id(args["entity1"], context=context)
        entity2_str = self.format_entity_id(args["entity2"], context=context)

        return f"{self.name}(result={result_work_str}, entity1={entity1_str}, entity2={entity2_str})"
