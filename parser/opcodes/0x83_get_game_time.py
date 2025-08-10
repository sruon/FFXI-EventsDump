from .base import ArgType, BaseOpcode, OpcodeArg


class GetGameTimeOpcode(BaseOpcode):
    opcode = 0x83
    name = "GET_GAME_TIME"

    def get_args(self):
        return [
            OpcodeArg("target", ArgType.WORD, 2, "Work memory offset to store game time"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        work_str = self.format_work_area_value(args["target"], context=context)
        return f"{work_str} = GetGameTime()"
