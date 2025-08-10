from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class WaitLoadSchedulerAlt5Opcode(SchedulerBase):
    """Waits for load scheduler with alternate configuration (helper call 70691)"""

    opcode = 0xD1
    name = "WAIT_LOAD_SCHEDULER_ALT5"

    def get_args(self):
        # Same parameters as opcode 0x55
        return [
            OpcodeArg("work_offset", ArgType.WORD, 2, "Work area offset"),
            OpcodeArg("entity1", ArgType.ENTITY_ID, 4, "First entity ID"),
            OpcodeArg("entity2", ArgType.ENTITY_ID, 4, "Second entity ID"),
            OpcodeArg("scheduler_id", ArgType.DWORD, 4, "Scheduler ID (often ASCII string)"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        # Format work offset (handles references internally)
        work_str = self.format_work_area_value(args["work_offset"], context=context)

        entity1_str = self.format_entity_id(args["entity1"], context=context)
        entity2_str = self.format_entity_id(args["entity2"], context=context)

        # Format scheduler_id using the base class method
        scheduler_id = args["scheduler_id"]
        scheduler_id_str = self.format_scheduler_id(scheduler_id)

        return f"WAIT_LOAD_SCHEDULER_ALT5: Wait for scheduler {scheduler_id_str} with entities [{entity1_str}, {entity2_str}], work={work_str}"
