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
