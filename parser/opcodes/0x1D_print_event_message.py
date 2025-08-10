from .base import ArgType, BaseOpcode, OpcodeArg


class PrintEventMessageOpcode(BaseOpcode):
    opcode = 0x1D
    name = "PRINT_EVENT_MESSAGE"

    def get_args(self):
        return [
            OpcodeArg("message_id", ArgType.WORD, 2, "Message ID work offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        message_id = args["message_id"]

        if 0x8000 <= message_id <= 0x8FFF:
            ref_index = message_id & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                message_str = f"{ref_value}*"
            else:
                message_str = f"References[{ref_index}]"
        else:
            message_str = f"0x{message_id:04X}"

        result = f"{self.name}(message_id={message_str})"

        if message_str.endswith("*") and context.zone_strings:
            string_id = int(message_str.rstrip("*"))
            found_string = None
            for parsed_string in context.zone_strings.strings:
                if parsed_string.index == string_id:
                    found_string = parsed_string
                    break

            if found_string:
                escaped_text = self.escape_unprintable_chars(found_string.text)
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
