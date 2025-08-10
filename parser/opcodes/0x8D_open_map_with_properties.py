from .base import ArgType, BaseOpcode, OpcodeArg


class OpenMapWithPropertiesOpcode(BaseOpcode):
    opcode = 0x8D
    name = "OPEN_MAP_WITH_PROPERTIES"

    def get_args(self):
        return [
            OpcodeArg("map_id", ArgType.WORD, 2, "Map ID to open"),
            OpcodeArg("properties", ArgType.WORD, 2, "Map properties"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        map_id = args["map_id"]
        properties = args["properties"]

        # Both parameters are work area offsets that need resolution
        map_str = self.format_work_area_value(map_id, context=context)
        props_str = self.format_work_area_value(properties, context=context)

        return f"{self.name}(map_id={map_str}, properties={props_str})"
