from .base import ArgType, BaseOpcode, OpcodeArg


class EntityAppearanceHandlerOpcode(BaseOpcode):
    opcode = 0xB6
    name = "ENTITY_APPEARANCE_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("case_type", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate the length based on the case type."""
        if offset >= len(data):
            return 1

        case_type = data[offset + 1] if offset + 1 < len(data) else 0

        # Based on Atomos documentation
        case_lengths = {
            0x00: 4,  # Hair style
            0x01: 4,  # Race
            0x02: 4,  # Hair (Look)
            0x03: 4,  # Head
            0x04: 4,  # Body
            0x05: 4,  # Hands
            0x06: 4,  # Legs
            0x07: 4,  # Feet
            0x08: 4,  # Main
            0x09: 4,  # Sub
            0x0A: 4,  # Ranged
            0x0B: 20,  # Full entity look (Race + 9 equipment slots)
            0x0C: 6,  # Type, Hair, Unknown
            0x0D: 14,  # Look with Render flags
            0x0E: 14,  # Look with Render flags
            0x0F: 4,  # Model size
            0x10: 2,  # Test validity
            0x11: 2,  # Unknown call
            0x12: 2,  # Render.Flags2
            0x13: 2,  # Render.Flags2
            0x14: 2,  # Render.Flags2
            0x15: 2,  # Render.Flags2
        }

        return case_lengths.get(case_type, 2)  # Default to 2 bytes if unknown case type

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments based on case type."""
        args = {}
        if len(raw_bytes) < 2:
            return args

        args["case_type"] = raw_bytes[1]
        case_type = args["case_type"]

        # Parse value for single-item cases (0x00-0x0A, 0x0F)
        if case_type in range(0x00, 0x0B) or case_type == 0x0F:
            if len(raw_bytes) >= 4:
                args["value"] = int.from_bytes(raw_bytes[2:4], byteorder="little")

        # For case 0x0B, parse all the equipment slots
        elif case_type == 0x0B and len(raw_bytes) >= 20:
            args["race"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
            args["hair"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
            args["head"] = int.from_bytes(raw_bytes[6:8], byteorder="little")
            args["body"] = int.from_bytes(raw_bytes[8:10], byteorder="little")
            args["hands"] = int.from_bytes(raw_bytes[10:12], byteorder="little")
            args["legs"] = int.from_bytes(raw_bytes[12:14], byteorder="little")
            args["feet"] = int.from_bytes(raw_bytes[14:16], byteorder="little")
            args["main"] = int.from_bytes(raw_bytes[16:18], byteorder="little")
            args["sub"] = int.from_bytes(raw_bytes[18:20], byteorder="little")

        # For case 0x0C (Type/Hair/Unknown)
        elif case_type == 0x0C and len(raw_bytes) >= 6:
            args["type"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
            args["hair"] = raw_bytes[4]
            args["unknown"] = raw_bytes[5]

        # For cases 0x0D and 0x0E (Look with Render flags)
        elif case_type in [0x0D, 0x0E] and len(raw_bytes) >= 14:
            args["race"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
            args["face"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
            args["head"] = int.from_bytes(raw_bytes[6:8], byteorder="little")
            args["body"] = int.from_bytes(raw_bytes[8:10], byteorder="little")
            args["hands"] = int.from_bytes(raw_bytes[10:12], byteorder="little")
            args["render_flags"] = int.from_bytes(raw_bytes[12:14], byteorder="little")

        return args

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        case_type = args["case_type"]

        # Case type descriptions
        case_descriptions = {
            0x00: "Hair style",
            0x01: "Race",
            0x02: "Hair (Look)",
            0x03: "Head",
            0x04: "Body",
            0x05: "Hands",
            0x06: "Legs",
            0x07: "Feet",
            0x08: "Main",
            0x09: "Sub",
            0x0A: "Ranged",
            0x0B: "Full entity look",
            0x0C: "Type/Hair/Unknown",
            0x0D: "Look with Render flags",
            0x0E: "Look with Render flags",
            0x0F: "Model size",
            0x10: "Test validity",
            0x11: "Unknown call",
            0x12: "Render.Flags2",
            0x13: "Render.Flags2",
            0x14: "Render.Flags2",
            0x15: "Render.Flags2",
        }

        case_desc = case_descriptions.get(case_type, f"Unknown 0x{case_type:02X}")

        # Handle different case types
        if case_type in range(0x00, 0x0B) or case_type == 0x0F:
            # Single value cases
            if "value" in args:
                return f"{self.name}(case={case_desc}, value={self.format_work_area_value(args['value'], context=context)})"
            else:
                return f"{self.name}(case={case_desc})"

        elif case_type == 0x0B:
            # Full entity look
            return (
                f"{self.name}(case={case_desc}, "
                f"race={self.format_work_area_value(args['race'], context=context)}, "
                f"hair={self.format_work_area_value(args['hair'], context=context)}, "
                f"head={self.format_work_area_value(args['head'], context=context)}, "
                f"body={self.format_work_area_value(args['body'], context=context)}, "
                f"hands={self.format_work_area_value(args['hands'], context=context)}, "
                f"legs={self.format_work_area_value(args['legs'], context=context)}, "
                f"feet={self.format_work_area_value(args['feet'], context=context)}, "
                f"main={self.format_work_area_value(args['main'], context=context)}, "
                f"sub={self.format_work_area_value(args['sub'], context=context)})"
            )

        elif case_type == 0x0C:
            # Type/Hair/Unknown
            if "type" in args:
                return f"{self.name}(case={case_desc}, type={self.format_work_area_value(args['type'], context=context)}, hair={args['hair']}, unknown={args['unknown']})"
            else:
                return f"{self.name}(case={case_desc})"

        elif case_type in [0x0D, 0x0E]:
            # Look with Render flags
            if "race" in args:
                return (
                    f"{self.name}(case={case_desc}, "
                    f"race={self.format_work_area_value(args['race'], context=context)}, "
                    f"face={self.format_work_area_value(args['face'], context=context)}, "
                    f"head={self.format_work_area_value(args['head'], context=context)}, "
                    f"body={self.format_work_area_value(args['body'], context=context)}, "
                    f"hands={self.format_work_area_value(args['hands'], context=context)}, "
                    f"render_flags=0x{args['render_flags']:04X})"
                )
            else:
                return f"{self.name}(case={case_desc})"

        else:
            return f"{self.name}(case={case_desc})"
