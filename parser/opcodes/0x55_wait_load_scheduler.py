from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class WaitLoadSchedulerOpcode(SchedulerBase):

    opcode = 0x55
    name = "WAIT_LOAD_SCHEDULER"

    def get_args(self):
        return [
            OpcodeArg("scheduler_work_offset", ArgType.WORD, 2, "Work area offset"),
            OpcodeArg("entity1", ArgType.ENTITY_ID, 4, "First entity ID"),
            OpcodeArg("entity2", ArgType.ENTITY_ID, 4, "Second entity ID"),
            OpcodeArg("scheduler_id", ArgType.DWORD, 4, "Scheduler ID (ASCII string)"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        work_str = self.format_work_area_value(args["scheduler_work_offset"], context=context)
        entity1_str = self.format_entity_id(args["entity1"], context=context)
        entity2_str = self.format_entity_id(args["entity2"], context=context)
        scheduler_id_str = self.format_scheduler_id(args["scheduler_id"])

        return f"{self.name}: Wait for scheduler {scheduler_id_str} with entities [{entity1_str}, {entity2_str}], work={work_str}"
