from .base import ArgType, BaseOpcode, OpcodeArg


class MapEditMarkerFromBufferOpcode(BaseOpcode):
    opcode = 0xB9
    name = "MAP_EDIT_MARKER_FROM_BUFFER"

    def get_args(self):
        return [
            OpcodeArg("map_flag", ArgType.BYTE, 1, "0=Open/close map, 1=Skip map open/close"),
            OpcodeArg("zone", ArgType.WORD, 2, "Zone ID"),
            OpcodeArg("submap", ArgType.WORD, 2, "Submap ID"),
            OpcodeArg("marker_id", ArgType.WORD, 2, "Marker ID"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        map_flag = args["map_flag"]
        zone = args["zone"]
        submap = args["submap"]
        marker_id = args["marker_id"]

        if map_flag == 0:
            flag_str = "0x00 (Open/close map)"
        elif map_flag == 1:
            flag_str = "0x01 (Skip map open/close)"
        else:
            flag_str = f"0x{map_flag:02X}"

        zone_str = self.format_work_area_value(zone, context=context)
        submap_str = self.format_work_area_value(submap, context=context)
        marker_id_str = self.format_work_area_value(marker_id, context=context)

        return f"{self.name}(map_flag={flag_str}, zone={zone_str}, submap={submap_str}, marker_id={marker_id_str})"
