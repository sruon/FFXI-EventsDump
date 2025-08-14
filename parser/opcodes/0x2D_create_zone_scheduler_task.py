from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class CreateZoneSchedulerTaskOpcode(SchedulerBase):
    opcode = 0x2D
    name = "CREATE_ZONE_SCHEDULER_TASK"

    def get_args(self):
        return [
            OpcodeArg("entity1", ArgType.DWORD, 4, ""),
            OpcodeArg("entity2", ArgType.DWORD, 4, ""),
            OpcodeArg("zone_action", ArgType.DWORD, 4, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        entity1 = args["entity1"]
        entity2 = args["entity2"]
        zone_action = args["zone_action"]

        entity1_str = self.format_entity_id(entity1, context=context)
        entity2_str = self.format_entity_id(entity2, context=context)

        zone_action_display = self.format_scheduler_id(zone_action)

        return f"{self.name}: Create scheduler {zone_action_display} with entities [{entity1_str}, {entity2_str}]"
