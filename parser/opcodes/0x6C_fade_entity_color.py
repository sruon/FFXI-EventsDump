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

        end_alpha_str = self.format_work_area_value(end_alpha, context=context)
        fade_time_str = self.format_work_area_value(fade_time, context=context)

        return f"{self.name}(entity_id={entity_id_str}, end_alpha={end_alpha_str}, fade_time={fade_time_str})"
