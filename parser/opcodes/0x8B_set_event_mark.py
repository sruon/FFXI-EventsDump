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

        # Format coordinates (scale by 0.001 for map coordinates)
        if 0x8000 <= pos_x <= 0x8FFF:
            ref_index = pos_x & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                actual_x = context.imed_data[ref_index]
                # For large values, interpret as signed int32
                import struct

                if actual_x > 0x80000000:
                    actual_x = struct.unpack("<i", struct.pack("<I", actual_x))[0]
                x_str = f"{actual_x * 0.001:.1f}*"
            else:
                x_str = f"References[{ref_index}]"
        else:
            # Scale the coordinate value
            x_str = f"{pos_x * 0.001:.1f}"

        if 0x8000 <= pos_y <= 0x8FFF:
            ref_index = pos_y & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                actual_y = context.imed_data[ref_index]
                # For large values, interpret as signed int32
                import struct

                if actual_y > 0x80000000:
                    actual_y = struct.unpack("<i", struct.pack("<I", actual_y))[0]
                y_str = f"{actual_y * 0.001:.1f}*"
            else:
                y_str = f"References[{ref_index}]"
        else:
            # Scale the coordinate value
            y_str = f"{pos_y * 0.001:.1f}"

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
