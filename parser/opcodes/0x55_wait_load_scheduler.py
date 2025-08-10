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

        work = args["scheduler_work_offset"]
        if 0x8000 <= work <= 0x8FFF:
            ref_index = work & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                work_str = f"{context.imed_data[ref_index]}*"
            else:
                work_str = f"References[{ref_index}]"
        else:
            work_str = self.format_work_area_value(work)

        entity1_str = self.format_entity_id(args["entity1"], context=context)
        entity2_str = self.format_entity_id(args["entity2"], context=context)

        scheduler_id = args["scheduler_id"]
        scheduler_id_str = self.format_scheduler_id(scheduler_id)

        return f"{self.name}(work_offset={work_str}, entity1={entity1_str}, entity2={entity2_str}, scheduler_id={scheduler_id_str})"
