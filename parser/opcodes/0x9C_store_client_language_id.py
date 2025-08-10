from .base import ArgType, BaseOpcode, OpcodeArg


class StoreClientLanguageIdOpcode(BaseOpcode):
    opcode = 0x9C
    name = "STORE_CLIENT_LANGUAGE_ID"

    def get_args(self):
        return [
            OpcodeArg("result", ArgType.WORD, 2, ""),
        ]
