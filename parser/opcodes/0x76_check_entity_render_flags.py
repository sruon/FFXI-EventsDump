from .base import ArgType, BaseOpcode, OpcodeArg


class CheckEntityRenderFlagsOpcode(BaseOpcode):
    opcode = 0x76
    name = "CHECK_ENTITY_RENDER_FLAGS"

    def get_args(self):
        return [
            OpcodeArg("entity", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        entity = args["entity"]

        entity_str = self.format_entity_id(entity, context=context)

        return f"CHECK_ENTITY_RENDER_FLAGS: Wait until {entity_str} Render.Flags0 and Render.Flags3 conditions are met"
