from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class LoadScheduledTaskOpcode(SchedulerBase):

    opcode = 0x45
    name = "LOAD_SCHEDULED_TASK"

    def get_args(self):
        return [
            OpcodeArg("first_work_offset", ArgType.WORD, 2, "First work area offset"),
            OpcodeArg("entity1", ArgType.ENTITY_ID, 4, "First entity ID"),
            OpcodeArg("entity2", ArgType.ENTITY_ID, 4, "Second entity ID"),
            OpcodeArg("scheduler_id", ArgType.DWORD, 4, "Scheduler ID (often ASCII string)"),
            OpcodeArg("second_work_offset", ArgType.WORD, 2, "Second work area offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        work1_str = self.format_work_area_value(args["first_work_offset"], context=context)
        entity1_str = self.format_entity_id(args["entity1"], context=context)
        entity2_str = self.format_entity_id(args["entity2"], context=context)

        scheduler_id = args["scheduler_id"]
        scheduler_id_str = self.format_scheduler_id(scheduler_id)

        work2_str = self.format_work_area_value(args["second_work_offset"], context=context)

        return f"{self.name}(work_offset1={work1_str}, entity1={entity1_str}, entity2={entity2_str}, scheduler_id={scheduler_id_str}, work_offset2={work2_str})"
