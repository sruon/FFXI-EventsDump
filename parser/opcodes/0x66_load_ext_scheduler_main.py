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

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Fixed length - should be 15 bytes based on args specification."""
        return 15

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        unknown1 = args["unknown1"]
        entity1_id = args["entity1_id"]
        entity2_id = args["entity2_id"]
        action_id = args["action_id"]

        # Check if unknown1 is a reference (0x8000-0x8FFF range)
        if 0x8000 <= unknown1 <= 0x8FFF:
            ref_index = unknown1 & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                unknown1_str = f"{ref_value}*"
            else:
                unknown1_str = f"References[{ref_index}]"
        else:
            unknown1_str = f"0x{unknown1:04X}"

        # Format entity IDs
        entity1_str = self.format_entity_id(entity1_id, context=context)
        entity2_str = self.format_entity_id(entity2_id, context=context)

        # Format action_id using the scheduler ID formatter
        action_str = self.format_scheduler_id(action_id)

        return f"{self.name}(work_offset={unknown1_str}, entity1={entity1_str}, entity2={entity2_str}, action={action_str})"
