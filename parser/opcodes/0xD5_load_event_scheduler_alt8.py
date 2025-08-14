from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class LoadEventSchedulerAlt8Opcode(SchedulerBase):
    opcode = 0xD5
    name = "LOAD_EVENT_SCHEDULER_ALT8"

    def get_args(self):
        return [
            OpcodeArg("unknown1", ArgType.BYTE, 1, "Unknown parameter 1"),
            OpcodeArg("unknown2", ArgType.BYTE, 1, "Unknown parameter 2"),
            OpcodeArg("entity1_id", ArgType.DWORD, 4, "First entity ID"),
            OpcodeArg("entity2_id", ArgType.DWORD, 4, "Second entity ID"),
            OpcodeArg("task_param", ArgType.WORD, 2, "Task parameter"),
            OpcodeArg("unknown3", ArgType.BYTE, 1, "Unknown parameter 3"),
            OpcodeArg("unknown4", ArgType.BYTE, 1, "Unknown parameter 4"),
            OpcodeArg("work_offset", ArgType.BYTE, 1, "Work offset parameter"),
            OpcodeArg("unknown5", ArgType.BYTE, 1, "Unknown parameter 5"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        entity1_str = self.format_entity_id(args["entity1_id"], context=context)
        entity2_str = self.format_entity_id(args["entity2_id"], context=context)
        task_param_str = self.format_scheduler_id(args["task_param"])
        work_str = self.format_work_area_value(args["work_offset"], context=context)
        
        return f"{self.name}: Load scheduler {task_param_str} with entities [{entity1_str}, {entity2_str}], work={work_str}"
