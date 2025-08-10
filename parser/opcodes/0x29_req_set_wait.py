from .base import ArgType, BaseOpcode, OpcodeArg


class ReqSetWaitOpcode(BaseOpcode):
    opcode = 0x29
    name = "REQ_SET_WAIT"

    def get_args(self):
        return [
            OpcodeArg("priority", ArgType.BYTE, 1, ""),
            OpcodeArg("server_id1", ArgType.WORD, 2, ""),
            OpcodeArg("server_id2", ArgType.WORD, 2, ""),
            OpcodeArg("tag_num", ArgType.BYTE, 1, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        priority = args["priority"]
        server_id1 = args["server_id1"]
        server_id2 = args["server_id2"]
        entity_id = (server_id2 << 16) | server_id1
        tag_num = args["tag_num"]

        entity_str = self.format_entity_id(entity_id, context=context)
        return f"{self.name}(priority=0x{priority:02X}, entity_id={entity_str}, tag_num=0x{tag_num:02X})"
