from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class LoadExtSchedulerMainOpcode(SchedulerBase):
    opcode = 0x66
    name = "LOAD_EXT_SCHEDULER_MAIN"

    def get_args(self):
        return [
            OpcodeArg("unknown1", ArgType.WORD, 2, ""),
            OpcodeArg("entity1_id", ArgType.DWORD, 4, ""),
            OpcodeArg("entity2_id", ArgType.DWORD, 4, ""),
            OpcodeArg("action_id", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        work_str = self.format_work_area_value(args["unknown1"], context=context)
        entity1_str = self.format_entity_id(args["entity1_id"], context=context)
        entity2_str = self.format_entity_id(args["entity2_id"], context=context)
        action_str = self.format_scheduler_id(args["action_id"])

        return f"{self.name}: Load scheduler {action_str} with entities [{entity1_str}, {entity2_str}], work={work_str}"
