from .base import ArgType, BaseOpcode, OpcodeArg


class MapQueryWindowHandlerOpcode(BaseOpcode):
    """Handles map query window operations with multiple sub-cases"""

    opcode = 0xD4
    name = "MAP_QUERY_WINDOW_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("sub_case", ArgType.BYTE, 1, "Sub-case for map query window handler"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate the length based on the sub-case."""
        if len(data) <= offset + 1:
            return 2  # Minimum length

        sub_case = data[offset + 1]  # First byte after opcode

        # Length based on sub-case from documentation
        if sub_case == 0x00:
            return 9  # 1 + 1 + 7 (case + 7 bytes)
        elif sub_case == 0x01:
            return 32  # 1 + 1 + 30 (case + 30 bytes)
        elif sub_case == 0x02:
            return 9  # 1 + 1 + 7 (case + 7 bytes)
        elif sub_case in [0x03, 0x04, 0x05]:
            return 30  # 1 + 1 + 28 (case + 28 bytes)
        else:
            return 2  # Unknown case, minimum length

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments based on sub-case."""
        if len(raw_bytes) < 2:
            return {"sub_case": 0}

        sub_case = raw_bytes[1]
        args = {"sub_case": sub_case}

        # Parse additional arguments based on sub-case
        if sub_case in [0x00, 0x02] and len(raw_bytes) >= 9:
            # Case 0x00/0x02: 7 additional bytes
            args["flag"] = raw_bytes[2] if len(raw_bytes) > 2 else 0
            args["work_offset1"] = int.from_bytes(raw_bytes[3:5], "little") if len(raw_bytes) > 4 else 0
            args["work_offset2"] = int.from_bytes(raw_bytes[5:7], "little") if len(raw_bytes) > 6 else 0
            args["work_offset3"] = int.from_bytes(raw_bytes[7:9], "little") if len(raw_bytes) > 8 else 0
        elif sub_case == 0x01 and len(raw_bytes) >= 32:
            # Case 0x01: 30 bytes - appears to be a buffer/data block
            args["buffer_data"] = raw_bytes[2:32] if len(raw_bytes) >= 32 else raw_bytes[2:]
        elif sub_case in [0x03, 0x04, 0x05] and len(raw_bytes) >= 30:
            # Case 0x03/0x04/0x05: 28 bytes - appears to be a buffer/data block
            args["buffer_data"] = raw_bytes[2:30] if len(raw_bytes) >= 30 else raw_bytes[2:]

        return args

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        sub_case = args["sub_case"]

        # Case descriptions based on documentation
        case_descriptions = {
            0x00: "Test and open map window",
            0x01: "Prepare buffer and copy to TalkpQW object",
            0x02: "Test and open query window",
            0x03: "Prepare buffer configuration A",
            0x04: "Prepare buffer configuration B",
            0x05: "Prepare buffer configuration B",
        }

        description = case_descriptions.get(sub_case, f"Unknown case 0x{sub_case:02X}")

        # Build parameter string based on sub-case
        if sub_case in [0x00, 0x02]:
            flag = args["flag"]
            work1 = args["work_offset1"]
            work2 = args["work_offset2"]
            work3 = args["work_offset3"]

            work1_str = self.format_work_area_value(work1, context=context)
            work2_str = self.format_work_area_value(work2, context=context)
            work3_str = self.format_work_area_value(work3, context=context)

            return f"MAP_QUERY_WINDOW: {description} (flag=0x{flag:02X}, work=[{work1_str}, {work2_str}, {work3_str}])"
        elif sub_case in [0x01, 0x03, 0x04, 0x05]:
            buffer_data = args.get("buffer_data", b"")
            # Display first few bytes of buffer as hex
            if buffer_data:
                hex_preview = " ".join(f"{b:02X}" for b in buffer_data[:8])
                if len(buffer_data) > 8:
                    hex_preview += "..."
                return f"MAP_QUERY_WINDOW: {description} (buffer=[{hex_preview}])"
            else:
                return f"MAP_QUERY_WINDOW: {description}"
        else:
            return f"MAP_QUERY_WINDOW: {description}"
