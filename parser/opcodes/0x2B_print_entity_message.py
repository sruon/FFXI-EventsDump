from .base import ArgType, BaseOpcode, OpcodeArg
from ..string_formatter import format_string


class PrintEntityMessageOpcode(BaseOpcode):
    opcode = 0x2B
    name = "PRINT_ENTITY_MESSAGE"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
            OpcodeArg("message", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        entity_id = args["entity_id"]
        message = args["message"]

        entity_str = self.format_entity_id(entity_id, context=context)
        message_str = self.format_work_area_value(message, context=context)

        result = f"{entity_str} [{message_str}]:"

        if message_str.endswith("*") and context and context.zone_strings:
            string_id = int(message_str.rstrip("*"))
            found_string = None
            for parsed_string in context.zone_strings.strings:
                if parsed_string.index == string_id:
                    found_string = parsed_string
                    break

            if found_string:
                escaped_text = format_string(found_string.text)
                result += f'\n    → "{escaped_text}"'
            else:
                nearby_strings = []
                if context.zone_strings and context.zone_strings.strings:
                    for parsed_string in context.zone_strings.strings:
                        if abs(parsed_string.index - string_id) <= 5:
                            nearby_strings.append(f"{parsed_string.index}")

                if nearby_strings:
                    result += f"\n    → [String ID {string_id} not found, nearby: {', '.join(nearby_strings)}]"
                else:
                    result += f"\n    → [String ID {string_id} not found]"

        return result
