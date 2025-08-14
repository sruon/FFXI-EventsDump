from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class DualEntitySchedulerHandlerOpcode(SchedulerBase):
    opcode = 0xAD
    name = "DUAL_ENTITY_SCHEDULER_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("sub_case", ArgType.BYTE, 1, "Sub-case value (0-9)"),
            OpcodeArg("param", ArgType.WORD, 2, "Parameter/work offset"),
            OpcodeArg("entity1", ArgType.DWORD, 4, "First entity ID"),
            OpcodeArg("entity2", ArgType.DWORD, 4, "Second entity ID"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        sub_case = args["sub_case"]
        param = args["param"]
        entity1 = args["entity1"]
        entity2 = args["entity2"]

        # Format parameter (could be work area reference)
        param_str = self.format_work_area_value(param, context=context)

        # Format entity IDs
        entity1_str = self.format_entity_id(entity1, context=context)
        entity2_str = self.format_entity_id(entity2, context=context)

        # Sub-case descriptions (based on lower 4 bits according to docs)
        sub_case_val = sub_case & 0x0F

        return f"{self.name}: Execute sub-case {sub_case_val} with entities [{entity1_str}, {entity2_str}], work={param_str}"
