from .base import ArgType, BaseOpcode, OpcodeArg


class RankingsBoardHandlerOpcode(BaseOpcode):
    opcode = 0xB3
    name = "RANKINGS_BOARD_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("case_type", ArgType.BYTE, 1, ""),
        ]
