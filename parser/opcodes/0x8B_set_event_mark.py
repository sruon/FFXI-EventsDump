from .base import ArgType, BaseOpcode, OpcodeArg


class SetEventMarkOpcode(BaseOpcode):

    opcode = 0x8B
    name = "SET_EVENT_MARK"

    def get_args(self):
        return [
            OpcodeArg("map_id", ArgType.WORD, 2, "Map ID"),
            OpcodeArg("point_index", ArgType.WORD, 2, "Map point index"),
            OpcodeArg("pos_x", ArgType.WORD, 2, "Map position X"),
            OpcodeArg("pos_y", ArgType.WORD, 2, "Map position Y"),
            # Note: We'll handle the 16 bytes manually in parse_args
        ]

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments including the 16-byte marker name."""
        # Parse the normal arguments first
        args = super().parse_args(raw_bytes)

        # Add the marker name (16 bytes starting at offset 9)
        if len(raw_bytes) >= 25:  # 1 (opcode) + 8 (4 words) + 16 (marker name)
            args["marker_name"] = raw_bytes[9:25]
        else:
            args["marker_name"] = b""

        return args

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        map_id = args["map_id"]
        point_index = args["point_index"]
        pos_x = args["pos_x"]
        pos_y = args["pos_y"]
        marker_name = args.get("marker_name", b"")

        # Format map ID
        map_id_str = self.format_work_area_value(map_id, context=context)

        # Format point index
        point_index_str = self.format_work_area_value(point_index, context=context)

        # Format coordinates using base class method
        x_str = self.format_coordinate_value(pos_x, context=context)
        y_str = self.format_coordinate_value(pos_y, context=context)

        # Try to interpret marker name as ASCII string
        try:
            if isinstance(marker_name, bytes) and len(marker_name) > 0:
                # Decode as ASCII, replacing underscores with spaces per documentation
                ascii_str = marker_name.rstrip(b"\x00").decode("ascii").replace("_", " ")
                if ascii_str and all(32 <= ord(c) <= 126 for c in ascii_str):
                    name_str = f'"{ascii_str}"'
                else:
                    # Show as hex if not printable or empty
                    hex_val = marker_name.hex()
                    if hex_val == "00" * 16 or hex_val == "":
                        name_str = "(no name)"
                    else:
                        name_str = f"0x{hex_val}"
            else:
                name_str = "(no name)"
        except (UnicodeDecodeError, ValueError):
            if isinstance(marker_name, bytes) and len(marker_name) > 0:
                name_str = f"0x{marker_name.hex()}"
            else:
                name_str = "(no name)"

        return f"SET_EVENT_MARK: Add/update map marker on map {map_id_str} at ({x_str}, {y_str}), index={point_index_str}, name={name_str}"
