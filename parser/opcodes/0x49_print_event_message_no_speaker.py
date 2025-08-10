from .base import ArgType, BaseOpcode, OpcodeArg


class PrintEventMessageNoSpeakerOpcode(BaseOpcode):

    opcode = 0x49
    name = "PRINT_EVENT_MESSAGE_NO_SPEAKER"

    def get_args(self):
        return [
            OpcodeArg("target_entity", ArgType.DWORD, 4, "Target entity ID"),
            OpcodeArg("message_id", ArgType.WORD, 2, "Message ID to display"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        entity_str = self.format_entity_id(args["target_entity"], context=context)
        message_str = self.format_work_area_value(args["message_id"], context=context)

        return f"{entity_str} (No speaker name) [{message_str}]:"
