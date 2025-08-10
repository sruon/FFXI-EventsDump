from .base import ArgType, BaseOpcode, OpcodeArg


class ClearEntityMotionQueueOpcode(BaseOpcode):
    opcode = 0xD3
    name = "CLEAR_ENTITY_MOTION_QUEUE"

    def get_args(self):
        return [
            OpcodeArg(
                "condition_flag",
                ArgType.BYTE,
                1,
                "Condition flag (must be 0 to execute)",
            ),
            OpcodeArg("entity_server_id", ArgType.DWORD, 4, "Entity server ID"),
        ]
