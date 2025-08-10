from .base import ArgType, BaseOpcode, OpcodeArg


class SendEventUpdateOpcode(BaseOpcode):

    opcode = 0x43
    name = "SEND_EVENT_UPDATE"

    def get_args(self):
        return [
            OpcodeArg("update_flag", ArgType.BYTE, 1, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None) -> str:
        update_flag = args["update_flag"]

        if update_flag == 0x00:
            return "SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)"
        elif update_flag == 0x01:
            return "SEND_EVENT_UPDATE: Check pending flag (skip if not pending)"
        else:
            return f"SEND_EVENT_UPDATE: Update flag 0x{update_flag:02X}"
