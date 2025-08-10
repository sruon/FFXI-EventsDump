from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class LoadScheduledTaskAltOpcode(SchedulerBase):
    opcode = 0x9F
    name = "LOAD_SCHEDULED_TASK_ALT"

    def get_args(self):
        return [
            OpcodeArg("work_offset1", ArgType.WORD, 2, "First work area offset"),
            OpcodeArg("entity1_id", ArgType.DWORD, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.DWORD, 4, "Second entity ID"),
            OpcodeArg("scheduler_id", ArgType.DWORD, 4, "Scheduler ID (often ASCII string)"),
            OpcodeArg("work_offset2", ArgType.WORD, 2, "Second work area offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        work1 = args["work_offset1"]
        entity1_id = args["entity1_id"]
        entity2_id = args["entity2_id"]
        scheduler_id = args["scheduler_id"]
        work2 = args["work_offset2"]

        # Format work offsets
        work1_str = self.format_work_area_value(work1, context=context)
        work2_str = self.format_work_area_value(work2, context=context)

        # Format entity IDs
        entity1_str = self.format_entity_id(entity1_id, context=context)
        entity2_str = self.format_entity_id(entity2_id, context=context)

        # Format scheduler_id using the base class method
        scheduler_id_str = self.format_scheduler_id(scheduler_id)

        return f"LOAD_SCHEDULED_TASK_ALT: Load scheduler {scheduler_id_str} with entities [{entity1_str}, {entity2_str}], work=[{work1_str}, {work2_str}]"
