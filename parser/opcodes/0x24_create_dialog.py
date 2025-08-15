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

        message_id_str = self.format_work_area_value(message_id, context=context)
        default_option_str = self.format_work_area_value(default_option, context=context)
        option_flags_str = self.format_work_area_value(option_flags, context=context)

        result = f"{self.name}(message_id={message_id_str}, default_option={default_option_str}, option_flags={option_flags_str})"

        resolved_id, was_ref = self.resolve_reference_value(message_id, context)
        if was_ref and context.zone_strings:
            found_string = None
            for parsed_string in context.zone_strings.strings:
                if parsed_string.index == resolved_id:
                    found_string = parsed_string
                    break

            if found_string:
                escaped_text = self.escape_unprintable_chars(found_string.text)
                result += f'\n    → "{escaped_text}"'
            else:
                result += f"\n    → [String ID {resolved_id} not found]"

        return result
