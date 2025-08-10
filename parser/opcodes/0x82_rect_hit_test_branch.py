from .base import ArgType, BaseOpcode, OpcodeArg


class RectHitTestBranchOpcode(BaseOpcode):
    opcode = 0x82
    name = "RECT_HIT_TEST_BRANCH"

    def get_args(self):
        return [
            OpcodeArg("rect_id", ArgType.DWORD, 4, "Rectangle ID to test"),
            OpcodeArg("jump_offset", ArgType.WORD, 2, "Offset to jump to if hit test fails"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Fixed length opcode."""
        return 7  # 1 + 4 + 2

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        rect_str = self.format_work_area_value(args["rect_id"], context=context)
        return f"RECT_HIT_TEST_BRANCH: If EventEntity is NOT in rectangle {rect_str}, GOTO 0x{args['jump_offset']:04X}"

    def get_jump_targets(self, args: dict, context=None) -> list:
        return [args["jump_offset"]]
