from .base import BaseOpcode


class BattlefieldServerResponseWaitOpcode(BaseOpcode):
    opcode = 0xA7
    name = "BATTLEFIELD_SERVER_RESPONSE_WAIT"

    def get_args(self):
        return []

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on pseudocode - 2 or 4 bytes."""
        if offset + 1 >= len(data):
            return 1  # Edge case: not enough data

        # Per pseudocode: if EventData[ExecPointer + 1] == 1, length is 4, otherwise 2
        mode = data[offset + 1]

        if mode == 0x01:
            return 4  # 1 opcode + 1 mode + 2 bytes parameter
        else:
            return 2  # 1 opcode + 1 mode byte

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments based on length."""
        if len(raw_bytes) < 2:
            return {}

        args = {"mode": raw_bytes[1]}

        # If mode == 1, there's a 2-byte parameter
        if args["mode"] == 0x01 and len(raw_bytes) >= 4:
            args["param"] = int.from_bytes(raw_bytes[2:4], "little")

        return args

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        mode = args["mode"]

        if mode == 0x01 and "param" in args:
            param = args["param"]
            param_str = self.format_work_area_value(param, context=context)
            return f"BATTLEFIELD_RESPONSE_WAIT: Wait for server response with parameter (Dynamis/MMM/Salvage), param={param_str}"
        else:
            return f"BATTLEFIELD_RESPONSE_WAIT: Wait for server response (Dynamis/MMM/Salvage), mode=0x{mode:02X}"
