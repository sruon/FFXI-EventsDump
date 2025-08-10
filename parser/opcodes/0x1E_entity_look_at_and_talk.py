from .base import ArgType, BaseOpcode, OpcodeArg


class EntityLookAtAndTalkOpcode(BaseOpcode):
    opcode = 0x1E
    name = "ENTITY_LOOK_AT_AND_TALK"

    def get_args(self):
        return [
            OpcodeArg("target_entity", ArgType.ENTITY_ID, 4, "Target entity (4 bytes)"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        target_entity = args["target_entity"]

        target_str = self.format_entity_id(target_entity, context=context)

        return f"EventEntity looks at {target_str} and starts talking"
