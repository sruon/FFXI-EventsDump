from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class LoadEventSchedulerAltOpcode(SchedulerBase):
    opcode = 0xBB
    name = "LOAD_EVENT_SCHEDULER_ALT"

    def get_args(self):
        return [
            OpcodeArg("work_offset1", ArgType.WORD, 2, "First work area offset"),
            OpcodeArg("entity1_id", ArgType.DWORD, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.DWORD, 4, "Second entity ID"),
            OpcodeArg("scheduler_id", ArgType.DWORD, 4, "Scheduler ID (often ASCII string)"),
            OpcodeArg("work_offset2", ArgType.WORD, 2, "Second work area offset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None) -> str:
        # Format work offsets
        work1 = args["work_offset1"]
        work1_str = self.format_work_area_value(work1, context=context)

        # Format entity IDs
        entity1_str = self.format_entity_id(args["entity1_id"], context=context)
        entity2_str = self.format_entity_id(args["entity2_id"], context=context)

        # Format scheduler_id using the base class method
        scheduler_id = args["scheduler_id"]
        scheduler_id_str = self.format_scheduler_id(scheduler_id)

        work2 = args["work_offset2"]
        work2_str = self.format_work_area_value(work2, context=context)

        return f"LOAD_EVENT_SCHEDULER_ALT: Load scheduler {scheduler_id_str} with entities [{entity1_str}, {entity2_str}], work=[{work1_str}, {work2_str}]"
