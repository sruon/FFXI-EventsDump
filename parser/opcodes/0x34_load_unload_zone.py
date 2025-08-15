from .base import ArgType, BaseOpcode, OpcodeArg


class LoadUnloadZoneOpcode(BaseOpcode):
    opcode = 0x34
    name = "LOAD_UNLOAD_ZONE"

    def get_args(self):
        return [
            OpcodeArg("zone_id", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        zone_id = args["zone_id"]
        zone_id_str = self.format_work_area_value(zone_id, context=context)

        return f"{self.name}(zone_id={zone_id_str})"
