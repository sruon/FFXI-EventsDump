from .base import ArgType, BaseOpcode, OpcodeArg


class SetupEventNpcOpcode(BaseOpcode):
    opcode = 0x95
    name = "SETUP_EVENT_NPC"

    def get_args(self):
        return [
            OpcodeArg("npc_param", ArgType.WORD, 2, "NPC parameter"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        npc_param = args["npc_param"]

        # Format the parameter using standard work area resolution
        param_str = self.format_work_area_value(npc_param, context=context)

        # According to docs, this modifies Render.Flags3 with the parameter value
        return f"SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = {param_str})"
