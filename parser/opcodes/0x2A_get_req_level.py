from .base import ArgType, BaseOpcode, OpcodeArg


class GetReqLevelOpcode(BaseOpcode):
    opcode = 0x2A
    name = "GET_REQ_LEVEL"

    def get_args(self):
        return [
            OpcodeArg("level", ArgType.BYTE, 1, ""),
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        level = args["level"]
        entity_id = args["entity_id"]
        entity_str = self.format_entity_id(entity_id, context=context)
        return f"{self.name}(level={level}, entity_id={entity_str})"
