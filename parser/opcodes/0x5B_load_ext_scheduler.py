from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class LoadExtSchedulerOpcode(SchedulerBase):

    opcode = 0x5B
    name = "LOAD_EXT_SCHEDULER"

    def get_args(self):
        return [
            OpcodeArg("scheduler_work_offset", ArgType.WORD, 2, "Work area offset"),
            OpcodeArg("entity1_id", ArgType.ENTITY_ID, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.ENTITY_ID, 4, "Second entity ID"),
            OpcodeArg("action_id", ArgType.DWORD, 4, "Scheduler action ID"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        work_str = self.format_work_area_value(args["scheduler_work_offset"], context=context)
        entity1_str = self.format_entity_id(args["entity1_id"], context=context)
        entity2_str = self.format_entity_id(args["entity2_id"], context=context)
        action_id_str = self.format_scheduler_id(args["action_id"])
        
        return f"{self.name}: Load scheduler {action_id_str} with entities [{entity1_str}, {entity2_str}], work={work_str}"
