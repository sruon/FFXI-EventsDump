from .base import ArgType, BaseOpcode, OpcodeArg


class SetClientEventModeOpcode(BaseOpcode):
    opcode = 0x38
    name = "SET_CLIENT_EVENT_MODE"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        mode = args["mode"]

        if 0x8000 <= mode <= 0x8FFF:
            ref_index = mode & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                mode_str = f"{ref_value}*"
            else:
                mode_str = f"References[{ref_index}]"
        else:
            mode_str = self.format_work_area_value(mode)

        return f"{self.name}(mode={mode_str})"
