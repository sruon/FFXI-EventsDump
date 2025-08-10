from .base import ArgType, BaseOpcode, OpcodeArg


class SetCliEventUcFlagOpcode(BaseOpcode):
    opcode = 0x20
    name = "SET_CLI_EVENT_UC_FLAG"

    def get_args(self):
        return [
            OpcodeArg("flag_value", ArgType.BYTE, 1, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None) -> str:

        flag_value = args["flag_value"]

        if flag_value == 0x00:
            return "SET_CLI_EVENT_UC_FLAG: Unlock player control"
        elif flag_value == 0x01:
            return "SET_CLI_EVENT_UC_FLAG: Lock player control"
        else:
            return f"SET_CLI_EVENT_UC_FLAG: Unknown flag value 0x{flag_value:02X}"
