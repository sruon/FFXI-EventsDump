from .base import ArgType, BaseOpcode, OpcodeArg


class SetRectEventSendFlagOpcode(BaseOpcode):
    opcode = 0x9E
    name = "SET_RECT_EVENT_SEND_FLAG"

    def get_args(self):
        return [
            OpcodeArg(
                "flag_value",
                ArgType.BYTE,
                1,
                "Flag value (0 sets flag to true, non-zero sets to false)",
            ),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        flag_value = args["flag_value"]

        if flag_value == 0:
            return "SET_RECT_EVENT_SEND_FLAG: Notify client of area visual look change"
        else:
            return "SET_RECT_EVENT_SEND_FLAG: Notify client of area movement"
