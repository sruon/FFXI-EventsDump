from .base import ArgType, BaseOpcode, OpcodeArg


class PlayEmoteOpcode(BaseOpcode):

    opcode = 0x6E
    name = "PLAY_EMOTE"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
            OpcodeArg("emote_data", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        entity_id = args["entity_id"]
        emote_data = args["emote_data"]

        entity_str = self.format_entity_id(entity_id, context=context)
        emote_str = self.format_work_area_value(emote_data, context=context)

        return f"{entity_str} uses emote {emote_str}"
