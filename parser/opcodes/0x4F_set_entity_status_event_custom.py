from .base import ArgType, BaseOpcode, OpcodeArg


class SetEntityStatusEventCustomOpcode(BaseOpcode):
    """Sets entity status event to custom value based on render flags"""

    opcode = 0x4F
    name = "SET_ENTITY_STATUS_EVENT_CUSTOM"

    def get_args(self):
        return [
            OpcodeArg("status", ArgType.WORD, 2, "Custom status event value"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        status = args.get("status", 0)
        status_str = self.format_work_area_value(status, context=context)

        return f"EventEntity->StatusEvent = {status_str} // Custom event value"
