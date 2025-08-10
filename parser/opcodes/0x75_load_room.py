from .base import ArgType, BaseOpcode, OpcodeArg


class LoadRoomOpcode(BaseOpcode):

    opcode = 0x75
    name = "LOAD_ROOM"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        if offset + 1 >= len(data):
            return 2  # Default fallback

        mode = data[offset + 1]
        if mode == 1:
            return 2  # Mode 1: 2 bytes total
        else:
            return 4  # Mode 0 or 2: 4 bytes total

    def parse_args(self, raw_bytes: bytes) -> dict:
        args = super().parse_args(raw_bytes)

        # Parse room_id for modes 0 and 2
        if len(raw_bytes) >= 4 and args.get("mode") != 1:
            args["room_id"] = int.from_bytes(raw_bytes[2:4], byteorder="little")

        return args

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        mode = args["mode"]

        mode_descriptions = {0: "Load indoor room", 1: "No action", 2: "Change sub-map"}

        mode_desc = mode_descriptions.get(mode, f"Unknown mode {mode}")

        if mode == 1:
            # Mode 1 doesn't have a room parameter
            return f"{self.name}({mode_desc})"
        elif "room_id" in args:
            # Modes 0 and 2 have a room/map ID parameter
            room_str = self.format_work_area_value(args["room_id"], context=context)
            return f"{self.name}({mode_desc}, room={room_str})"
        else:
            return f"{self.name}(mode={mode})"
