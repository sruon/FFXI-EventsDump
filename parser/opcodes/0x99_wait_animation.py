from .base import ArgType, BaseOpcode, OpcodeArg


class WaitAnimationOpcode(BaseOpcode):

    opcode = 0x99
    name = "WAIT_ANIMATION"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        # Get entity ID representation
        entity_id = args["entity_id"]
        entity_repr = self.format_entity_id(entity_id, context=context)

        return f"Wait for {entity_repr} animation to complete"
