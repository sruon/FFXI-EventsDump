from .base import ArgType, BaseOpcode, OpcodeArg


class ReqSetWithConditionsOpcode(BaseOpcode):
    opcode = 0x28
    name = "REQ_SET_WITH_CONDITIONS"

    def get_args(self):
        return [
            OpcodeArg("priority", ArgType.BYTE, 1, ""),
            OpcodeArg("entity_id", ArgType.ENTITY_ID, 4, "Target entity ID"),
            OpcodeArg("tag_num", ArgType.BYTE, 1, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        priority = args["priority"]
        entity_id = args["entity_id"]
        tag_num = args["tag_num"]

        entity_str = self.format_entity_id(entity_id, context=context)
        return f"{self.name}(priority=0x{priority:02X}, target_entity={entity_str}, tag_num=0x{tag_num:02X})"
