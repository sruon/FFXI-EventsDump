from .base import ArgType, BaseOpcode, OpcodeArg


class CreateDialogOpcode(BaseOpcode):
    opcode = 0x24
    name = "CREATE_DIALOG"

    def get_args(self):
        return [
            OpcodeArg("message_id", ArgType.WORD, 2, ""),
            OpcodeArg("default_option", ArgType.WORD, 2, ""),
            OpcodeArg("option_flags", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        message_id = args["message_id"]
        default_option = args["default_option"]
        option_flags = args["option_flags"]

        if 0x8000 <= message_id <= 0x8FFF:
            ref_index = message_id & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                message_id_str = f"{ref_value}*"
            else:
                message_id_str = f"References[{ref_index}]"
        else:
            message_id_str = f"0x{message_id:08X}"

        if 0x8000 <= default_option <= 0x8FFF:
            ref_index = default_option & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                default_option_str = f"{ref_value}*"
            else:
                default_option_str = f"References[{ref_index}]"
        else:
            default_option_str = f"0x{default_option:04X}"

        if 0x8000 <= option_flags <= 0x8FFF:
            ref_index = option_flags & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                option_flags_str = f"{ref_value}*"
            else:
                option_flags_str = f"References[{ref_index}]"
        else:
            option_flags_str = f"0x{option_flags:02X}"

        result = f"{self.name}(message_id={message_id_str}, default_option={default_option_str}, option_flags={option_flags_str})"

        if message_id_str.endswith("*") and context.zone_strings:
            string_id = int(message_id_str.rstrip("*"))
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
