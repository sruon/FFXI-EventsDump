from .base import ArgType, BaseOpcode, OpcodeArg


class SetMainSpeedOpcode(BaseOpcode):
    opcode = 0x32
    name = "SET_MAIN_SPEED"

    def get_args(self):
        return [
            OpcodeArg("speed", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        speed = args["speed"]
        speed_str = self.format_work_area_value(speed, context=context)
        return f"ExtData[1]->MainSpeed = {speed_str} * 0.1"
