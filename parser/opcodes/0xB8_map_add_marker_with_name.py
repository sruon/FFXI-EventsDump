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
            # Note: We'll handle the 16 bytes manually in parse_args
        ]

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments including the 16-byte marker name."""
        # Parse the normal arguments first
        args = super().parse_args(raw_bytes)

        # Add the marker name (16 bytes starting at offset 11)
        if len(raw_bytes) >= 27:  # 1 (opcode) + 10 (5 words) + 16 (marker name)
            args["marker_name"] = raw_bytes[11:27]
        else:
            args["marker_name"] = b""

        return args

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        zone = args["zone"]
        submap = args["submap"]
        marker_id = args["marker_id"]
        x_pos = args["x_pos"]
        y_pos = args["y_pos"]
        marker_name = args.get("marker_name", b"")

        # Format values using work area formatting where appropriate
        zone_str = self.format_work_area_value(zone, context=context)
        submap_str = self.format_work_area_value(submap, context=context)
        marker_id_str = self.format_work_area_value(marker_id, context=context)

        # X and Y positions are work offsets or actual coordinates (16-bit values)
        # Check if they're work references first
        if 0x8000 <= x_pos <= 0x8FFF:
            ref_index = x_pos & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                x_float = self.convert_coordinate_to_float(ref_value)
                x_str = f"{x_float:.3f}*"
            else:
                x_str = f"References[{ref_index}]"
        else:
            # Direct coordinate value
            x_float = self.convert_coordinate_to_float(x_pos)
            x_str = f"{x_float:.3f}"

        if 0x8000 <= y_pos <= 0x8FFF:
            ref_index = y_pos & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                y_float = self.convert_coordinate_to_float(ref_value)
                y_str = f"{y_float:.3f}*"
            else:
                y_str = f"References[{ref_index}]"
        else:
            # Direct coordinate value
            y_float = self.convert_coordinate_to_float(y_pos)
            y_str = f"{y_float:.3f}"

        # Try to interpret marker name as ASCII string, replacing underscores with spaces
        try:
            if isinstance(marker_name, bytes):
                ascii_str = marker_name.rstrip(b"\x00").decode("ascii")
                # Replace underscores with spaces as per the documentation
                ascii_str = ascii_str.replace("_", " ")
                if ascii_str and all(32 <= ord(c) <= 126 or c == " " for c in ascii_str):
                    name_str = f'"{ascii_str}"'
                else:
                    name_str = f"0x{marker_name.hex()}"
            else:
                name_str = f"0x{marker_name:032X}"
        except (UnicodeDecodeError, ValueError):
            if isinstance(marker_name, bytes):
                name_str = f"0x{marker_name.hex()}"
            else:
                name_str = f"0x{marker_name:032X}"

        return f"{self.name}(zone={zone_str}, submap={submap_str}, marker_id={marker_id_str}, x_pos={x_str}, y_pos={y_str}, marker_name={name_str})"
