import struct

from .base import ArgType, BaseOpcode, OpcodeArg


class UiWindowStringHandlerOpcode(BaseOpcode):
    opcode = 0xB4
    name = "UI_WINDOW_STRING_HANDLER"

    def get_args(self):
        # This is a variable-length opcode - args depend on case type
        return [
            OpcodeArg("case_type", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate the length based on the case type."""
        if len(data) <= offset + 1:
            return 2  # Minimum length

        case_type = data[offset + 1]  # First byte after opcode

        # Length based on case type from specification
        case_lengths = {
            0x00: 20,  # B4 00 + 16-byte string + 2-byte work offset
            0x01: 6,  # B4 01 + work offsets
            0x02: 6,  # B4 02 + work offsets
            0x03: 2,  # B4 03 only
            0x04: 6,  # B4 04 + work offsets
            0x05: 3,  # B4 05 + byte value
            0x06: 3,  # B4 06 + byte value
            0x07: 4,  # B4 07 + work offset
            0x08: 2,  # B4 08 only
            0x09: 4,  # B4 09 + work offset
            0x0A: 4,  # B4 0A + work offset
            0x0B: 2,  # B4 0B only
            0x0C: 4,  # B4 0C + work offset
            0x0D: 2,  # B4 0D only
            0x0E: 2,  # B4 0E only
            0x0F: 6,  # B4 0F + 2 work offsets
            0x10: 6,  # B4 10 + 2 work offsets
            0x11: 6,  # B4 11 + 2 work offsets
            0x12: 6,  # B4 12 + 2 work offsets
            0x13: 20,  # B4 13 + 16-byte string + 2-byte work offset
            0x14: 12,  # B4 14 + 5 work offsets
            0x15: 2,  # B4 15 only
        }

        return case_lengths.get(case_type, 2)

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments based on case type."""
        if len(raw_bytes) < 2:
            return {"case_type": 0}

        case_type = raw_bytes[1]
        args = {"case_type": case_type}

        # Parse additional arguments based on case type
        if case_type == 0x00 and len(raw_bytes) >= 20:
            # Case 0x00: Copy string from opcode data
            string_data = raw_bytes[4:20]  # 16 bytes of string data
            string_text = string_data.rstrip(b"\x00").decode("ascii", errors="replace")
            work_offset = struct.unpack("<H", raw_bytes[2:4])[0]
            args.update({"work_offset": work_offset, "string_data": string_text})
        elif case_type == 0x01 and len(raw_bytes) >= 6:
            # Case 0x01: Copy string from event strings table
            work_offset1 = struct.unpack("<H", raw_bytes[2:4])[0]
            work_offset2 = struct.unpack("<H", raw_bytes[4:6])[0]
            args.update({"work_offset": work_offset1, "string_index": work_offset2})
        elif case_type in [0x02, 0x04] and len(raw_bytes) >= 6:
            # Case 0x02: Update target window, Case 0x04: Copy string to buffers
            work_offset1 = struct.unpack("<H", raw_bytes[2:4])[0]
            work_offset2 = struct.unpack("<H", raw_bytes[4:6])[0]
            args.update({"work_offset1": work_offset1, "work_offset2": work_offset2})
        elif case_type in [0x05, 0x06] and len(raw_bytes) >= 3:
            # Case 0x05: Toggle event message flag, Case 0x06: Toggle query message flag
            flag_value = raw_bytes[2]
            args.update({"flag_value": flag_value})
        elif case_type in [0x07, 0x09, 0x0A, 0x0C] and len(raw_bytes) >= 4:
            # Various cases with single work offset
            work_offset = struct.unpack("<H", raw_bytes[2:4])[0]
            args.update({"work_offset": work_offset})
        elif case_type in [0x0F, 0x10, 0x11, 0x12] and len(raw_bytes) >= 6:
            # Chocobo racing cases with 2 work offsets
            work_offset1 = struct.unpack("<H", raw_bytes[2:4])[0]
            work_offset2 = struct.unpack("<H", raw_bytes[4:6])[0]
            args.update({"work_offset1": work_offset1, "work_offset2": work_offset2})
        elif case_type == 0x13 and len(raw_bytes) >= 20:
            # Case 0x13: Copy string and replace @ with space
            string_data = raw_bytes[4:20]  # 16 bytes of string data
            string_text = string_data.rstrip(b"\x00").decode("ascii", errors="replace")
            work_offset = struct.unpack("<H", raw_bytes[2:4])[0]
            args.update({"work_offset": work_offset, "string_data": string_text})
        elif case_type == 0x14 and len(raw_bytes) >= 12:
            # Case 0x14: Map window update with 5 work offsets
            offsets = []
            for i in range(5):
                offset_val = struct.unpack("<H", raw_bytes[2 + i * 2 : 4 + i * 2])[0]
                offsets.append(offset_val)
            args.update(
                {
                    "work_offset1": offsets[0],
                    "work_offset2": offsets[1],
                    "work_offset3": offsets[2],
                    "work_offset4": offsets[3],
                    "work_offset5": offsets[4],
                }
            )

        return args

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        case_type = args["case_type"]

        # Case-specific descriptions
        case_descriptions = {
            0x00: "Copy string from opcode",
            0x01: "Copy string from event strings table",
            0x02: "Update target window",
            0x03: "Destroy target window",
            0x04: "Copy string to shared buffers",
            0x05: "Toggle event message flag",
            0x06: "Toggle query message flag",
            0x07: "Open cast bar/time window",
            0x08: "Destroy cast bar/time window",
            0x09: "Get cast bar count value",
            0x0A: "Open event time window",
            0x0B: "Destroy event time window",
            0x0C: "Get event time count value",
            0x0D: "Set unknown flag to 1",
            0x0E: "Set unknown flag to 0",
            0x0F: "Open chocobo racing window",
            0x10: "Close chocobo racing window",
            0x11: "Open chocobo racing card window",
            0x12: "Close chocobo racing card window",
            0x13: "Copy string and replace @ with space",
            0x14: "Update map window values",
            0x15: "Test map window validity",
        }

        description = case_descriptions.get(case_type, f"Unknown case 0x{case_type:02X}")

        # Build parameter string based on case type
        params = []

        if case_type in [0x00, 0x13] and "string_data" in args:
            work_offset = args["work_offset"]
            work_str = self.format_work_area_value(work_offset, context=context)
            escaped_string = self.escape_unprintable_chars(args["string_data"])
            params = [f"work_offset={work_str}", f'string="{escaped_string}"']
        elif case_type == 0x01 and "string_index" in args:
            work_offset = args["work_offset"]
            string_index = args["string_index"]
            work_str = self.format_work_area_value(work_offset, context=context)
            index_str = self.format_work_area_value(string_index, context=context)
            params = [f"work_offset={work_str}", f"string_index={index_str}"]
        elif case_type in [0x02, 0x04] and "work_offset2" in args:
            work1 = self.format_work_area_value(args["work_offset1"], context=context)
            work2 = self.format_work_area_value(args["work_offset2"], context=context)
            params = [f"work_offset1={work1}", f"work_offset2={work2}"]
        elif case_type in [0x05, 0x06] and "flag_value" in args:
            params = [f"flag_value=0x{args['flag_value']:02X}"]
        elif case_type in [0x07, 0x09, 0x0A, 0x0C] and "work_offset" in args:
            work_str = self.format_work_area_value(args["work_offset"], context=context)
            params = [f"work_offset={work_str}"]
        elif case_type in [0x0F, 0x10, 0x11, 0x12] and "work_offset2" in args:
            work1 = self.format_work_area_value(args["work_offset1"], context=context)
            work2 = self.format_work_area_value(args["work_offset2"], context=context)
            params = [f"work_offset1={work1}", f"work_offset2={work2}"]
        elif case_type == 0x14 and "work_offset5" in args:
            work_params = []
            for i in range(1, 6):
                work_val = args.get(f"work_offset{i}", 0)
                work_str = self.format_work_area_value(work_val, context=context)
                work_params.append(f"work_offset{i}={work_str}")
            params = work_params

        param_str = ", ".join(params) if params else ""
        if param_str:
            return f"{self.name}(case=0x{case_type:02X} - {description}, {param_str})"
        else:
            return f"{self.name}(case=0x{case_type:02X} - {description})"
