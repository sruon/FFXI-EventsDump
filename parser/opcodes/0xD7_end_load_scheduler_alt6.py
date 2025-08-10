from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class EndLoadSchedulerAlt6Opcode(SchedulerBase):
    opcode = 0xD7
    name = "END_LOAD_SCHEDULER_ALT6"

    def get_args(self):
        return [
            OpcodeArg("work_offset", ArgType.WORD, 2, "Work area offset"),
            OpcodeArg("entity1_id", ArgType.ENTITY_ID, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.ENTITY_ID, 4, "Second entity ID"),
            OpcodeArg("scheduler_id", ArgType.DWORD, 4, "Scheduler ID"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        work_str = self.format_work_area_value(args["work_offset"], context=context)
        entity1_str = self.format_entity_id(args["entity1_id"], context=context)
        entity2_str = self.format_entity_id(args["entity2_id"], context=context)
        scheduler_display = self.format_scheduler_id(args["scheduler_id"])
        return f"{self.name}: End scheduler {scheduler_display} with entities [{entity1_str}, {entity2_str}], work={work_str}"
