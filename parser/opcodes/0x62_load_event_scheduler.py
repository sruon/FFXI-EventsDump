from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class LoadEventSchedulerOpcode(SchedulerBase):
    opcode = 0x62
    name = "LOAD_EVENT_SCHEDULER"

    def get_args(self):
        # Same structure as 0x45 - 17 bytes total
        return [
            OpcodeArg("work_offset1", ArgType.WORD, 2, "First work area offset"),
            OpcodeArg("entity1", ArgType.ENTITY_ID, 4, "First entity ID"),
            OpcodeArg("entity2", ArgType.ENTITY_ID, 4, "Second entity ID"),
            OpcodeArg("scheduler_id", ArgType.DWORD, 4, "Scheduler ID (often ASCII string)"),
            OpcodeArg("work_offset2", ArgType.WORD, 2, "Second work area offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        work1 = args["work_offset1"]
        work1_str = self.format_work_area_value(work1, context=context)

        entity1_str = self.format_entity_id(args["entity1"], context=context)
        entity2_str = self.format_entity_id(args["entity2"], context=context)

        scheduler_id = args["scheduler_id"]
        scheduler_id_str = self.format_scheduler_id(scheduler_id)

        work2 = args["work_offset2"]
        work2_str = self.format_work_area_value(work2, context=context)

        return f"LOAD_EVENT_SCHEDULER (arg=5012): Load scheduler {scheduler_id_str} with entities [{entity1_str}, {entity2_str}], work=[{work1_str}, {work2_str}]"
