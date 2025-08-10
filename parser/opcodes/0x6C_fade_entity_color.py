from .base import ArgType, BaseOpcode, OpcodeArg


class FadeEntityColorOpcode(BaseOpcode):

    opcode = 0x6C
    name = "FADE_ENTITY_COLOR"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
            OpcodeArg("end_alpha", ArgType.WORD, 2, ""),
            OpcodeArg("fade_time", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        entity_id_str = self.format_entity_id(args["entity_id"], context=context)

        end_alpha = args["end_alpha"]
        fade_time = args["fade_time"]

        # Check if end_alpha is a reference (0x8000-0x8FFF range)
        if 0x8000 <= end_alpha <= 0x8FFF:
            ref_index = end_alpha & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                end_alpha_str = f"{ref_value}*"
            else:
                end_alpha_str = f"References[{ref_index}]"
        else:
            end_alpha_str = f"0x{end_alpha:04X}"

        # Check if fade_time is a reference (0x8000-0x8FFF range)
        if 0x8000 <= fade_time <= 0x8FFF:
            ref_index = fade_time & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                fade_time_str = f"{ref_value}*"
            else:
                fade_time_str = f"References[{ref_index}]"
        else:
            fade_time_str = f"0x{fade_time:04X}"

        return f"{self.name}(entity_id={entity_id_str}, end_alpha={end_alpha_str}, fade_time={fade_time_str})"
