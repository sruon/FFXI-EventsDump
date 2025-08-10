from .base import ArgType, BaseOpcode, OpcodeArg


class EntityHideFlagOpcode(BaseOpcode):
    opcode = 0x22
    name = "ENTITY_HIDE_FLAG"

    def get_args(self):
        return [
            OpcodeArg("enabled", ArgType.BYTE, 1, ""),
        ]
