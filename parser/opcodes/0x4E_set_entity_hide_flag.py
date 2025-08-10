from .base import ArgType, BaseOpcode, OpcodeArg


class SetEntityHideFlagOpcode(BaseOpcode):
    """Sets entity visibility state through render flags"""

    opcode = 0x4E
    name = "SET_ENTITY_HIDE_FLAG"

    def get_args(self):
        return [
            OpcodeArg("flag", ArgType.BYTE, 1, "Hide flag (0=show, 1=hide)"),
            OpcodeArg("entity_id", ArgType.ENTITY_ID, 4, "Entity to show/hide"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        flag = args.get("flag", 0)
        entity_id = args.get("entity_id", 0)

        entity_id_str = self.format_entity_id(entity_id, context=context)

        if flag == 0:
            return f"SET_ENTITY_HIDE_FLAG: Show {entity_id_str}"
        else:
            return f"SET_ENTITY_HIDE_FLAG: Hide {entity_id_str}"
