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
