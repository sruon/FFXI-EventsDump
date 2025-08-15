from .base import ArgType, BaseOpcode, OpcodeArg


class HelperCallAltOpcode(BaseOpcode):

    opcode = 0xC4
    name = "HELPER_CALL_ALT"

    def get_args(self):
        # Same parameters as opcode 0x73 with an additional mode byte
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, "Mode selector (1=arg17, 2=arg18, else=arg16)"),
            OpcodeArg("magic_id", ArgType.WORD, 2, "Magic ID"),
            OpcodeArg("caster_entity", ArgType.DWORD, 4, "Caster entity ID"),
            OpcodeArg("target_entity", ArgType.DWORD, 4, "Target entity ID"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        mode = args["mode"]
        magic_id = args["magic_id"]
        caster_entity = args["caster_entity"]
        target_entity = args["target_entity"]

        # Determine which helper argument is used based on mode
        if mode == 1:
            helper_arg = 17
        elif mode == 2:
            helper_arg = 18
        else:
            helper_arg = 16  # Default

        magic_id_str = self.format_work_area_value(magic_id, context=context)
        caster_entity_str = self.format_entity_id(caster_entity, context=context)
        target_entity_str = self.format_entity_id(target_entity, context=context)

        return f"SCHEDULE_MAGIC_CASTING_ALT (arg={helper_arg}): {caster_entity_str} casts magic {magic_id_str} on {target_entity_str}"
