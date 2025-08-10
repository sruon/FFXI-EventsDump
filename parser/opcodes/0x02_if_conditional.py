from .base import ArgType, BaseOpcode, OpcodeArg


class IfConditionalOpcode(BaseOpcode):
    opcode = 0x02
    name = "IF_CONDITIONAL"

    def get_args(self):
        return [
            OpcodeArg("val1", ArgType.WORD, 2, "First comparison value (work offset)"),
            OpcodeArg("val2", ArgType.WORD, 2, "Second comparison value (work offset)"),
            OpcodeArg("condition_type", ArgType.BYTE, 1, "Condition type (0-10)"),
            OpcodeArg("else_offset", ArgType.WORD, 2, "Jump offset if condition fails"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        actual_condition = args["condition_type"] & 0x0F

        condition_names = {
            0: "==",
            1: "==",
            2: "<=",
            3: ">=",
            4: "<",
            5: ">",
            6: "&",
            7: "==",
            8: "|",
            9: "&",
            10: "^",
        }
        cond_name = condition_names.get(actual_condition, f"UNKNOWN_COND_{actual_condition}")

        val1_str = self.format_work_area_value(args["val1"], context=context)
        val2_str = self.format_work_area_value(args["val2"], context=context)

        return f"IF !({val1_str} {cond_name} {val2_str}) GOTO 0x{args['else_offset']:04X}"

    def get_jump_targets(self, args: dict, context=None) -> list:
        return [args["else_offset"]]
