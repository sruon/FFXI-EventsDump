from .base import ArgType, BaseOpcode, OpcodeArg


class LoadZoneNoCloseOpcode(BaseOpcode):
    opcode = 0x35
    name = "LOAD_ZONE_NO_CLOSE"

    def get_args(self):
        return [
            OpcodeArg("zone_id", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        zone_id = args["zone_id"]

        if 0x8000 <= zone_id <= 0x8FFF:
            ref_index = zone_id & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                zone_id_str = f"{ref_value}*"
            else:
                zone_id_str = f"References[{ref_index}]"
        else:
            zone_id_str = str(zone_id)

        return f"{self.name}(zone_id={zone_id_str})"
