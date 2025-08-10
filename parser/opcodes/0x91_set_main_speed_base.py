from .base import ArgType, BaseOpcode, OpcodeArg


class SetMainSpeedBaseOpcode(BaseOpcode):
    opcode = 0x91
    name = "SET_MAIN_SPEED_BASE"

    def get_args(self):
        return [
            OpcodeArg("speed_value", ArgType.WORD, 2, "Main speed base value"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        speed_value = args["speed_value"]
        speed_str = self.format_work_area_value(speed_value, context=context)

        # The actual speed is multiplied by 10.0
        return f"ExtData[1]->MainSpeedBase = {speed_str} * 10.0"
