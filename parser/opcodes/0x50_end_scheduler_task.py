from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class EndSchedulerTaskOpcode(SchedulerBase):

    opcode = 0x50
    name = "END_SCHEDULER_TASK"

    def get_args(self):
        return [
            OpcodeArg("first_entity", ArgType.WORD, 2, "First entity work area address"),
            OpcodeArg("first_param", ArgType.WORD, 2, "Unknown parameter 1"),
            OpcodeArg("second_entity", ArgType.WORD, 2, "Second entity work area address"),
            OpcodeArg("second_param", ArgType.WORD, 2, "Unknown parameter 2"),
            OpcodeArg("action_id", ArgType.WORD, 2, "Action/task ID to end"),
            OpcodeArg("third_param", ArgType.WORD, 2, "Unknown parameter 3"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        first_entity_str = self.format_work_area_value(args["first_entity"], context=context)
        second_entity_str = self.format_work_area_value(args["second_entity"], context=context)
        action_id_str = self.format_scheduler_id(args["action_id"])
        
        return f"{self.name}(first_entity={first_entity_str}, first_param={args['first_param']}, second_entity={second_entity_str}, second_param={args['second_param']}, action_id={action_id_str}, third_param={args['third_param']})"
