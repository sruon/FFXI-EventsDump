from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class WaitMapSchedulerOpcode(SchedulerBase):

    opcode = 0x54
    name = "WAIT_MAP_SCHEDULER"

    def get_args(self):
        return [
            OpcodeArg("entity1_id", ArgType.ENTITY_ID, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.ENTITY_ID, 4, "Second entity ID"),
            OpcodeArg("action_id", ArgType.DWORD, 4, "Action ID to wait for"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        entity1_str = self.format_entity_id(args["entity1_id"], context=context)
        entity2_str = self.format_entity_id(args["entity2_id"], context=context)
        action_id_str = self.format_scheduler_id(args["action_id"])

        return f"{self.name}: Wait for scheduler {action_id_str} with entities [{entity1_str}, {entity2_str}]"
