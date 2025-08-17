from .base import ArgType, BaseOpcode, OpcodeArg
from ..string_formatter import format_string


class PrintEventMessageOpcode(BaseOpcode):
    opcode = 0x1D
    name = "PRINT_EVENT_MESSAGE"

    def get_args(self):
        return [
            OpcodeArg("message_id", ArgType.WORD, 2, "Message ID work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        message_id = args["message_id"]
        message_str = self.format_work_area_value(message_id, context=context)

        result = f"{self.name}(message_id={message_str})"

        resolved_id, was_ref = self.resolve_reference_value(message_id, context)
        if was_ref and context.zone_strings:
            found_string = None
            for parsed_string in context.zone_strings.strings:
                if parsed_string.index == resolved_id:
                    found_string = parsed_string
                    break

            if found_string:
                formatted_text = format_string(found_string.text)
                result += f'\n    → "{formatted_text}"'
            else:
                result += f"\n    → [String ID {resolved_id} not found]"

        return result
