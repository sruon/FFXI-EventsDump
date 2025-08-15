from .base import ArgType, BaseOpcode, OpcodeArg


class ScheduleMagicCastingOpcode(BaseOpcode):
    opcode = 0x73
    name = "SCHEDULE_MAGIC_CASTING"

    def get_args(self):
        return [
            OpcodeArg("magic_id", ArgType.WORD, 2, ""),
            OpcodeArg("caster_entity", ArgType.DWORD, 4, ""),
            OpcodeArg("target_entity", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        magic_id = args["magic_id"]
        caster_entity = args["caster_entity"]
        target_entity = args["target_entity"]

        magic_id_str = self.format_work_area_value(magic_id, context=context)
        caster_entity_str = self.format_entity_id(caster_entity, context=context)
        target_entity_str = self.format_entity_id(target_entity, context=context)

        return f"{caster_entity_str} casts magic {magic_id_str} on {target_entity_str}"
