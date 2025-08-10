from .base import ArgType, BaseOpcode, OpcodeArg


class KillEntityActionOpcode(BaseOpcode):
    opcode = 0xC1
    name = "KILL_ENTITY_ACTION"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.DWORD, 4, "Entity ID to kill action for"),
        ]
