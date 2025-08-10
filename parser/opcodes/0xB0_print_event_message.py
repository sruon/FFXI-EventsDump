from .base import ArgType, BaseOpcode, OpcodeArg


class PrintEventMessageOpcode(BaseOpcode):
    opcode = 0xB0
    name = "PRINT_EVENT_MESSAGE"

    def get_args(self):
        return [
            OpcodeArg("unknown1", ArgType.BYTE, 1, ""),
            OpcodeArg("speaker_id", ArgType.DWORD, 4, ""),
            OpcodeArg("listener_id", ArgType.DWORD, 4, ""),
            OpcodeArg("message_offset", ArgType.WORD, 2, ""),
        ]
