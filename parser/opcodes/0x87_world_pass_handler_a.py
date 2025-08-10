from .base import ArgType, BaseOpcode, OpcodeArg


class WorldPassHandlerAOpcode(BaseOpcode):
    opcode = 0x87
    name = "WORLD_PASS_HANDLER_A"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, "World pass handler mode"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on mode."""
        if offset + 1 >= len(data):
            return 1  # Just opcode

        mode = data[offset + 1]
        if mode == 0x02:
            return 2  # Opcode + mode byte
        else:
            return 1  # Just opcode (default mode)

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments - optional mode byte."""
        if len(raw_bytes) >= 2:
            return {"mode": raw_bytes[1]}
        else:
            return {"mode": 0}  # Default mode

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        if args["mode"] == 0x02:
            return "WORLD_PASS_HANDLER_A: Send world pass packet 0x1B (Para=2)"
        else:
            return "WORLD_PASS_HANDLER_A: Send world pass packet 0x1B (Para=0)"
