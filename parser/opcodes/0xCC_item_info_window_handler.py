from .base import ArgType, BaseOpcode, OpcodeArg


class ItemInfoWindowHandlerOpcode(BaseOpcode):
    opcode = 0xCC
    name = "ITEM_INFO_WINDOW_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("case_type", ArgType.BYTE, 1, "Case type for window handler"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate the length based on the case type."""
        if len(data) <= offset + 1:
            return 2  # Minimum length

        case_type = data[offset + 1]  # First byte after opcode

        # Length based on case type from specification
        if case_type in [0x00, 0x01, 0x03]:
            return 10  # 1 (opcode) + 1 (case) + 8 (4 words)
        elif case_type == 0x02:
            return 14  # 1 (opcode) + 1 (case) + 12 (6 words)
        elif case_type == 0x10:
            return 6  # 1 (opcode) + 1 (case) + 4 (2 words)
        elif case_type in [0x11, 0x20]:
            return 4  # 1 (opcode) + 1 (case) + 2 (1 word)
        else:
            return 4  # Unknown case, minimum length

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments based on case type."""
        if len(raw_bytes) < 2:
            return {"case_type": 0}

        case_type = raw_bytes[1]
        args = {"case_type": case_type}

        # Parse additional arguments based on case type
        if case_type in [0x00, 0x01, 0x03] and len(raw_bytes) >= 10:
            # 4 word parameters
            args.update(
                {
                    "param1": int.from_bytes(raw_bytes[2:4], "little"),
                    "param2": int.from_bytes(raw_bytes[4:6], "little"),
                    "param3": int.from_bytes(raw_bytes[6:8], "little"),
                    "param4": int.from_bytes(raw_bytes[8:10], "little"),
                }
            )
        elif case_type == 0x02 and len(raw_bytes) >= 14:
            # 6 word parameters
            args.update(
                {
                    "param1": int.from_bytes(raw_bytes[2:4], "little"),
                    "param2": int.from_bytes(raw_bytes[4:6], "little"),
                    "param3": int.from_bytes(raw_bytes[6:8], "little"),
                    "param4": int.from_bytes(raw_bytes[8:10], "little"),
                    "param5": int.from_bytes(raw_bytes[10:12], "little"),
                    "param6": int.from_bytes(raw_bytes[12:14], "little"),
                }
            )
        elif case_type == 0x10 and len(raw_bytes) >= 6:
            # 2 word parameters
            args.update(
                {
                    "param1": int.from_bytes(raw_bytes[2:4], "little"),
                    "param2": int.from_bytes(raw_bytes[4:6], "little"),
                }
            )
        elif case_type in [0x11, 0x20] and len(raw_bytes) >= 4:
            # 1 word parameter
            args.update(
                {
                    "param1": int.from_bytes(raw_bytes[2:4], "little"),
                }
            )

        return args

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        case_type = args["case_type"]

        # Case-specific descriptions
        case_descriptions = {
            0x00: "Open item info window (no chase)",
            0x01: "Open item info window (with chase)",
            0x02: "Open item info window (complex setup)",
            0x03: "Open item info window (conditional chase)",
            0x10: "Search menu zone interaction",
            0x11: "Check search menu condition",
            0x20: "Event item window create/destroy",
        }

        description = case_descriptions.get(case_type, f"Unknown case 0x{case_type:02X}")

        # Build parameter string based on case type
        params = []

        if case_type in [0x00, 0x01, 0x03]:
            if "param1" in args:
                p1 = self.format_work_area_value(args["param1"], context=context)
                p2 = self.format_work_area_value(args["param2"], context=context)
                p3 = self.format_work_area_value(args["param3"], context=context)
                p4 = self.format_work_area_value(args["param4"], context=context)
                params = [
                    f"check_value={p1}",
                    f"buffer1={p2}",
                    f"buffer2={p3}",
                    f"buffer3={p4}",
                ]
        elif case_type == 0x02:
            if "param1" in args:
                p1 = self.format_work_area_value(args["param1"], context=context)
                p2 = self.format_work_area_value(args["param2"], context=context)
                p3 = self.format_work_area_value(args["param3"], context=context)
                p4 = self.format_work_area_value(args["param4"], context=context)
                p5 = self.format_work_area_value(args["param5"], context=context)
                p6 = self.format_work_area_value(args["param6"], context=context)
                params = [
                    f"val1={p1}",
                    f"val2={p2}",
                    f"val3={p3}",
                    f"val4={p4}",
                    f"val5={p5}",
                    f"val6={p6}",
                ]
        elif case_type == 0x10:
            if "param1" in args:
                p1 = self.format_work_area_value(args["param1"], context=context)
                p2 = self.format_work_area_value(args["param2"], context=context)
                params = [f"zone_id={p1}", f"search_type={p2}"]
        elif case_type == 0x11:
            if "param1" in args:
                p1 = self.format_work_area_value(args["param1"], context=context)
                params = [f"flag_work_offset={p1}"]
        elif case_type == 0x20:
            if "param1" in args:
                p1 = self.format_work_area_value(args["param1"], context=context)
                params = [f"window_action={p1}"]

        param_str = ", ".join(params) if params else ""
        if param_str:
            return f"{self.name}(case=0x{case_type:02X} - {description}, {param_str})"
        else:
            return f"{self.name}(case=0x{case_type:02X} - {description})"
