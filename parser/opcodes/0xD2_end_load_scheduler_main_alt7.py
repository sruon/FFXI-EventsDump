from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class EndLoadSchedulerMainAlt7Opcode(SchedulerBase):
    opcode = 0xD2
    name = "END_LOAD_SCHEDULER_MAIN_ALT7"

    def get_args(self):
        return [
            OpcodeArg("unknown1", ArgType.BYTE, 1, "Unknown parameter 1"),
            OpcodeArg("unknown2", ArgType.BYTE, 1, "Unknown parameter 2"),
            OpcodeArg("entity1_id", ArgType.DWORD, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.DWORD, 4, "Second entity ID"),
            OpcodeArg("scheduler_param", ArgType.WORD, 2, "Scheduler parameter"),
            OpcodeArg("unknown3", ArgType.BYTE, 1, "Unknown parameter 3"),
            OpcodeArg("work_offset", ArgType.BYTE, 1, "Work offset parameter"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        entity1_str = self.format_entity_id(args["entity1_id"], context=context)
        entity2_str = self.format_entity_id(args["entity2_id"], context=context)
        scheduler_param_str = self.format_scheduler_id(args["scheduler_param"])
        work_str = self.format_work_area_value(args["work_offset"], context=context)
        
        return f"{self.name}: End scheduler {scheduler_param_str} with entities [{entity1_str}, {entity2_str}], work={work_str}"
