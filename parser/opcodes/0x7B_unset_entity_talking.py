from .base import ArgType, BaseOpcode, OpcodeArg


class UnsetEntityTalkingOpcode(BaseOpcode):
    opcode = 0x7B
    name = "UNSET_ENTITY_TALKING"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        entity_id = args["entity_id"]
        entity_str = self.format_entity_id(entity_id, context=context)

        return f"{entity_str} stops talking"
