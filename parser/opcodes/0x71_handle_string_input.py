from .base import ArgType, BaseOpcode, OpcodeArg


class HandleStringInputOpcode(BaseOpcode):
    opcode = 0x71
    name = "HANDLE_STRING_INPUT"

    def get_args(self):
        return [
            OpcodeArg("input_type", ArgType.BYTE, 1, "Type of input operation"),
            # Additional args depend on input_type
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on input_type."""
        if offset + 2 > len(data):
            return 2  # Minimum length

        input_type = data[offset + 1]

        # Length mapping based on upstream documentation
        if input_type in [0x00, 0x01, 0x02, 0x21, 0x51, 0x53]:
            return 2  # 2 bytes total
        elif input_type in [0x03, 0x10, 0x11, 0x13, 0x30, 0x31, 0x40, 0x50, 0x52, 0x55]:
            return 4  # 4 bytes total
        elif input_type in [0x12, 0x32]:
            return 6  # 6 bytes total
        elif input_type == 0x41:
            return 8  # 8 bytes total
        elif input_type in [0x54]:
            return 10  # 10 bytes total
        elif input_type == 0x20:
            return 16  # 16 bytes total
        else:
            return 2  # Unknown input type, assume minimum

    def parse_args(self, raw_bytes: bytes):
        """Parse arguments based on the input type."""
        if len(raw_bytes) < 2:
            return {"input_type": 0}

        args = {"input_type": raw_bytes[1]}
        input_type = args["input_type"]

        # Parse specific fields based on input_type
        if input_type in [0x03, 0x10, 0x11, 0x13, 0x40, 0x50, 0x52, 0x55] and len(raw_bytes) >= 4:
            # 2-byte parameter
            args["work_offset"] = int.from_bytes(raw_bytes[2:4], "little")
        elif input_type in [0x12] and len(raw_bytes) >= 6:
            # 2 x 2-byte parameters
            args["work_offset1"] = int.from_bytes(raw_bytes[2:4], "little")
            args["work_offset2"] = int.from_bytes(raw_bytes[4:6], "little")
        elif input_type in [0x30, 0x31] and len(raw_bytes) >= 4:
            # 2-byte parameter
            args["param"] = int.from_bytes(raw_bytes[2:4], "little")
        elif input_type == 0x32 and len(raw_bytes) >= 6:
            # 2 x 2-byte parameters
            args["param1"] = int.from_bytes(raw_bytes[2:4], "little")
            args["param2"] = int.from_bytes(raw_bytes[4:6], "little")
        elif input_type == 0x41 and len(raw_bytes) >= 8:
            # 3 x 2-byte parameters
            args["param1"] = int.from_bytes(raw_bytes[2:4], "little")
            args["param2"] = int.from_bytes(raw_bytes[4:6], "little")
            args["param3"] = int.from_bytes(raw_bytes[6:8], "little")
        elif input_type == 0x54 and len(raw_bytes) >= 10:
            # 4 x 2-byte parameters
            args["param1"] = int.from_bytes(raw_bytes[2:4], "little")
            args["param2"] = int.from_bytes(raw_bytes[4:6], "little")
            args["param3"] = int.from_bytes(raw_bytes[6:8], "little")
            args["param4"] = int.from_bytes(raw_bytes[8:10], "little")
        elif input_type == 0x20 and len(raw_bytes) >= 16:
            # 7 x 2-byte parameters
            for i in range(7):
                args[f"param{i+1}"] = int.from_bytes(raw_bytes[2 + i * 2 : 4 + i * 2], "little")

        return args

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        input_type = args["input_type"]

        type_descriptions = {
            # String input modes
            0x00: "Open password input dialog (sends packet 0x60)",
            0x01: "Check if player has input or exited",
            0x02: "Check if server responded",
            0x03: "Check vulgar filter",
            # Numerical input modes
            0x10: "Open numerical input dialog",
            0x11: "Process numerical input A",
            0x12: "Open numerical input with params",
            0x13: "Process numerical input B",
            # Moblin Maze Mongers
            0x20: "Moblin Maze Mongers menu (sends packet 0x60)",
            0x21: "MMM menu check",
            # Other menu/dialog modes
            0x30: "Menu operation A",
            0x31: "Menu operation B",
            0x32: "Menu operation with params",
            # Linkshell Concierge
            0x40: "Linkshell Concierge window (sends packet 0x60)",
            0x41: "Linkshell Concierge with params (sends packet 0x60)",
            # Character/menu creation
            0x50: "Menu/character process A",
            0x51: "Menu/character check",
            0x52: "Menu/character process B",
            0x53: "Menu/character verify",
            0x54: "Menu/character complex",
            0x55: "Menu/character process C",
        }

        description = type_descriptions.get(input_type, f"Unknown mode 0x{input_type:02X}")
        params = []

        if "work_offset" in args:
            work_str = self.format_work_area_value(args["work_offset"], context=context)
            params.append(f"work={work_str}")

        if "work_offset1" in args and "work_offset2" in args:
            work1 = self.format_work_area_value(args["work_offset1"], context=context)
            work2 = self.format_work_area_value(args["work_offset2"], context=context)
            params.append(f"work=[{work1}, {work2}]")

        if "param" in args:
            params.append(f"param=0x{args['param']:04X}")

        if "param1" in args and "param2" in args and "param3" not in args:
            params.append(f"params=[0x{args['param1']:04X}, 0x{args['param2']:04X}]")
        elif "param1" in args and "param2" in args and "param3" in args:
            if "param4" in args:
                params.append(f"params=[0x{args['param1']:04X}, 0x{args['param2']:04X}, 0x{args['param3']:04X}, 0x{args['param4']:04X}]")
            else:
                params.append(f"params=[0x{args['param1']:04X}, 0x{args['param2']:04X}, 0x{args['param3']:04X}]")

        # Special case for mode 0x20 with 7 parameters
        if input_type == 0x20 and "param1" in args:
            param_list = []
            for i in range(1, 8):
                if f"param{i}" in args:
                    param_list.append(f"0x{args[f'param{i}']:04X}")
            if param_list:
                params = [f"params=[{', '.join(param_list)}]"]

        if params:
            return f"USER_INPUT_HANDLER: {description} ({', '.join(params)})"
        else:
            return f"USER_INPUT_HANDLER: {description}"
