from .base import ArgType, BaseOpcode, OpcodeArg


class GetActorIndexDeprecatedOpcode(BaseOpcode):

    opcode = 0x56
    name = "GET_ACTOR_INDEX_DEPRECATED"

    def get_args(self):
        return [
            OpcodeArg("entity", ArgType.WORD, 2, "Entity work area address"),
            OpcodeArg("unused_data", ArgType.WORD, 2, "Unused parameter"),
        ]
