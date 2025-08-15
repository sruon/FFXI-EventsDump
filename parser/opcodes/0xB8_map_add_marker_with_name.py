from .base import ArgType, BaseOpcode, OpcodeArg


class MapAddMarkerWithNameOpcode(BaseOpcode):
    opcode = 0xB8
    name = "MAP_ADD_MARKER_WITH_NAME"

    def get_args(self):
        return [
            OpcodeArg("zone", ArgType.WORD, 2, "Zone ID"),
            OpcodeArg("submap", ArgType.WORD, 2, "Submap ID"),
            OpcodeArg("marker_id", ArgType.WORD, 2, "Marker ID"),
            OpcodeArg("x_pos", ArgType.WORD, 2, "X position"),
            OpcodeArg("y_pos", ArgType.WORD, 2, "Y position"),
            OpcodeArg("marker_name", ArgType.STRING, 16, "Marker name (underscores replaced with spaces)"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        zone = args["zone"]
        submap = args["submap"]
        marker_id = args["marker_id"]
        x_pos = args["x_pos"]
        y_pos = args["y_pos"]
        marker_name = args["marker_name"]

        zone_str = self.format_work_area_value(zone, context=context)
        submap_str = self.format_work_area_value(submap, context=context)
        marker_id_str = self.format_work_area_value(marker_id, context=context)
        x_str = self.format_coordinate_value(x_pos, context=context)
        y_str = self.format_coordinate_value(y_pos, context=context)

        name_str = self.format_string_value(marker_name, replace_underscores=True)

        return f"{self.name}(zone={zone_str}, submap={submap_str}, marker_id={marker_id_str}, x_pos={x_str}, y_pos={y_str}, marker_name={name_str})"
