from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class EndMapSchedulerOpcode(SchedulerBase):

    opcode = 0x51
    name = "END_MAP_SCHEDULER"

    def get_args(self):
        return [
            OpcodeArg("entity1_id", ArgType.ENTITY_ID, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.ENTITY_ID, 4, "Second entity ID"),
            OpcodeArg("scheduler_id", ArgType.DWORD, 4, "Scheduler ID"),
        ]
    
    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        entity1_str = self.format_entity_id(args["entity1_id"], context=context)
        entity2_str = self.format_entity_id(args["entity2_id"], context=context)
        scheduler_display = self.format_scheduler_id(args["scheduler_id"])
        return f"{self.name}: End scheduler {scheduler_display} for entities [{entity1_str}, {entity2_str}]"
