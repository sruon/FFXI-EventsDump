from .base import ArgType, BaseOpcode, OpcodeArg


class LoadWaitOpcode(BaseOpcode):
    opcode = 0x80
    name = "LOAD_WAIT"

    def get_args(self):
        return [
            OpcodeArg("entity", ArgType.ENTITY_ID, 4, "Entity to check loading status for"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        entity_str = self.format_entity_id(args["entity"], context=context)
        return f"{self.name}(entity={entity_str})"
