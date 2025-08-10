from .base import ArgType, BaseOpcode, OpcodeArg


class EntityLookAtOpcode(BaseOpcode):

    opcode = 0x4A
    name = "ENTITY_LOOK_AT"

    def get_args(self):
        return [
            OpcodeArg("entity1_id", ArgType.ENTITY_ID, 4, "Entity that will look"),
            OpcodeArg("entity2_id", ArgType.ENTITY_ID, 4, "Entity to look at"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        if context is None:
            from parser.opcodes.base import OpcodeContext

            context = OpcodeContext()

        if "entity1_id" in args and "entity2_id" in args:
            entity1_str = self.format_entity_id(args["entity1_id"], context=context)
            entity2_str = self.format_entity_id(args["entity2_id"], context=context)
            return f"{entity1_str} looks at {entity2_str}"
        else:
            return super().get_legible_representation(raw_bytes, args, context)
