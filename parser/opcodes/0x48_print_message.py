from .base import ArgType, BaseOpcode, OpcodeArg
from ..string_formatter import format_string


class PrintMessageOpcode(BaseOpcode):

    opcode = 0x48
    name = "PRINT_MESSAGE"

    def get_args(self):
        return [OpcodeArg("message_id", ArgType.MESSAGE_ID, 2, "Message ID to display")]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        message_id = args["message_id"]
        message_str = self.format_work_area_value(message_id, context=context)

        result = f"[System] [{message_str}]:"

        actual_message_id, was_ref = self.resolve_reference_value(message_id, context)

        if context and context.zone_strings and hasattr(context.zone_strings, "strings"):
            found_string = None
            for string_entry in context.zone_strings.strings:
                if string_entry.index == actual_message_id:
                    found_string = string_entry
                    break

            if found_string:
                escaped_text = format_string(found_string.text)
                result += f'\n    → "{escaped_text}"'

        return result
