from .base import ArgType, BaseOpcode, OpcodeArg


class MapMarkerControlOpcode(BaseOpcode):

    opcode = 0xA8
    name = "MAP_MARKER_CONTROL"

    def get_args(self):
        return [
            OpcodeArg("map_flag", ArgType.BYTE, 1, "Map open flag (0=no map, 1=open map)"),
            OpcodeArg("zone_offset", ArgType.WORD, 2, "Zone ID or work offset"),
            OpcodeArg("marker_offset", ArgType.WORD, 2, "Marker ID or work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        map_flag = args["map_flag"]
        zone_offset = args["zone_offset"]
        marker_offset = args["marker_offset"]

        # Format work offsets
        zone_str = self.format_work_area_value(zone_offset, context=context)
        marker_str = self.format_work_area_value(marker_offset, context=context)

        # Build description based on flag
        if map_flag == 0:
            action = "Reset/unlock markers (no map display)"
        elif map_flag == 1:
            action = "Open map and reset/unlock markers"
        else:
            action = f"Control markers (flag=0x{map_flag:02X})"

        return f"MAP_MARKER_CONTROL: {action}, zone={zone_str}, marker={marker_str}"
