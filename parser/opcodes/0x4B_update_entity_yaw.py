from .base import ArgType, BaseOpcode, OpcodeArg


class UpdateEntityYawOpcode(BaseOpcode):

    opcode = 0x4B
    name = "UPDATE_ENTITY_YAW"

    def get_args(self):
        return [
            OpcodeArg("entity", ArgType.ENTITY_ID, 4, "Entity to rotate"),
            OpcodeArg("yaw", ArgType.WORD, 2, "Yaw rotation value"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        entity = args.get("entity", 0)
        yaw = args.get("yaw", 0)

        entity_str = self.format_entity_id(entity, context=context)
        yaw_str = self.format_yaw_value(yaw, context=context)

        return f"{self.name}(entity={entity_str}, yaw={yaw_str})"
