from .base import ArgType, BaseOpcode, OpcodeArg


class GetEntityPositionOpcode(BaseOpcode):
    opcode = 0x3B
    name = "GET_ENTITY_POSITION"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
            OpcodeArg("x_destination", ArgType.WORD, 2, ""),
            OpcodeArg("y_destination", ArgType.WORD, 2, ""),
            OpcodeArg("z_destination", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        entity_str = self.format_entity_id(args["entity_id"], context=context)
        x_str = self.format_work_area_value(args["x_destination"], context=context)
        y_str = self.format_work_area_value(args["y_destination"], context=context)
        z_str = self.format_work_area_value(args["z_destination"], context=context)

        return f"{self.name}(entity={entity_str}, x_destination={x_str}, y_destination={y_str}, z_destination={z_str})"
