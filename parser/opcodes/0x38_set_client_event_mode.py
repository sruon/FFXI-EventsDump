from .base import ArgType, BaseOpcode, OpcodeArg


class SetClientEventModeOpcode(BaseOpcode):
    opcode = 0x38
    name = "SET_CLIENT_EVENT_MODE"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        mode_str = self.format_work_area_value(args["mode"], context=context)
        return f"{self.name}(mode={mode_str})"
