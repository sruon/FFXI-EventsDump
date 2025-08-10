from .base import ArgType, BaseOpcode, OpcodeArg


class StoreReqWhoServerIdOpcode(BaseOpcode):
    opcode = 0xBE
    name = "STORE_REQ_WHO_SERVER_ID"

    def get_args(self):
        return [
            OpcodeArg("work_offset", ArgType.WORD, 2, ""),
        ]
