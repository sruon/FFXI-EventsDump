from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class WaitSchedulerTaskOpcode(SchedulerBase):

    opcode = 0x53
    name = "WAIT_SCHEDULER_TASK"

    def get_args(self):
        return [
            OpcodeArg("entity1", ArgType.ENTITY_ID, 4, "First entity ID"),
            OpcodeArg("entity2", ArgType.ENTITY_ID, 4, "Second entity ID"),
            OpcodeArg("action_id", ArgType.DWORD, 4, "Action ID to wait for"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        entity1_str = self.format_entity_id(args["entity1"], context=context)
        entity2_str = self.format_entity_id(args["entity2"], context=context)

        action_id_str = self.format_scheduler_id(args["action_id"])

        return f"{self.name}(entity1={entity1_str}, entity2={entity2_str}, action_id={action_id_str})"
