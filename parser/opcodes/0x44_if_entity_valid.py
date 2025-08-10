from .base import ArgType, BaseOpcode, OpcodeArg


class IfEntityValidOpcode(BaseOpcode):

    opcode = 0x44
    name = "IF_ENTITY_VALID"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.WORD, 2, "Entity ID to test"),
            OpcodeArg("else_offset", ArgType.WORD, 2, "Jump offset if entity is invalid"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        entity_str = self.format_entity_id(args["entity_id"], context=context)
        return f"{self.name}({entity_str} valid ? continue : jump_to=0x{args['else_offset']:04X})"

    def get_jump_targets(self, args: dict, context=None) -> list:
        return [args["else_offset"]]
