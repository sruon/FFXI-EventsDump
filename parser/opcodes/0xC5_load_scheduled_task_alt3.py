from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class LoadScheduledTaskAlt3Opcode(SchedulerBase):
    opcode = 0xC5
    name = "LOAD_SCHEDULED_TASK_ALT3"

    def get_args(self):
        return [
            OpcodeArg("work_offset", ArgType.WORD, 2, "Work area offset"),
            OpcodeArg("entity1_id", ArgType.DWORD, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.DWORD, 4, "Second entity ID"),
            OpcodeArg("task_param", ArgType.WORD, 2, "Task parameter"),
            OpcodeArg("scheduler_id", ArgType.DWORD, 4, "Scheduler ID"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        entity1_str = self.format_entity_id(args["entity1_id"], context=context)
        entity2_str = self.format_entity_id(args["entity2_id"], context=context)
        scheduler_display = self.format_scheduler_id(args["scheduler_id"])
        work_str = self.format_work_area_value(args["work_offset"], context=context)
        return f"{self.name}: Load scheduler {scheduler_display} for entities [{entity1_str}, {entity2_str}], work={work_str}, param={args['task_param']}"
