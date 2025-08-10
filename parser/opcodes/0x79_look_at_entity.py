from .base import ArgType, BaseOpcode, OpcodeArg


class LookAtEntityOpcode(BaseOpcode):
    opcode = 0x79
    name = "LOOK_AT_ENTITY"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, "Look at mode"),
            OpcodeArg("entity1_id", ArgType.DWORD, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.DWORD, 4, "Second entity ID or axis data"),
            # Variable third parameter based on mode
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        if offset + 1 >= len(data):
            return 10  # Default fallback

        mode = data[offset + 1]
        if mode == 1:
            return 12  # Mode 1: 12 bytes (includes work offset parameter)
        else:
            return 10  # Mode 0 or 2: 10 bytes

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments based on mode"""
        args = super().parse_args(raw_bytes)

        # Parse mode-specific third parameter
        if len(raw_bytes) >= 12 and args.get("mode") == 1:
            # Mode 1 has an extra work offset parameter for turn speed/method
            args["turn_param"] = int.from_bytes(raw_bytes[10:12], byteorder="little")

        return args

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        if "mode" in args and "entity1_id" in args and "entity2_id" in args:
            mode = args["mode"]
            entity1_str = self.format_entity_id(args["entity1_id"], context=context)
            entity2_str = self.format_entity_id(args["entity2_id"], context=context)

            mode_descriptions = {0: "Basic look", 1: "Extended look", 2: "Direct axis set"}

            mode_desc = mode_descriptions.get(mode, f"Unknown mode {mode}")

            result = f"{entity1_str} looks at {entity2_str} ({mode_desc})"

            # Add turn parameter for mode 1
            if mode == 1 and "turn_param" in args:
                turn_str = self.format_work_area_value(args["turn_param"], context=context)
                result += f" [turn_speed={turn_str}]"

            return result
        else:
            return super().get_legible_representation(raw_bytes, args, context)
