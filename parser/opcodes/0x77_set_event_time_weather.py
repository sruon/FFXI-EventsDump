from .base import ArgType, BaseOpcode, OpcodeArg


class SetEventTimeWeatherOpcode(BaseOpcode):
    opcode = 0x77
    name = "SET_EVENT_TIME_WEATHER"

    def get_args(self):
        return [
            OpcodeArg("hour", ArgType.WORD, 2, ""),
            OpcodeArg("weather", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        hour = args["hour"]
        weather = args["weather"]

        hour_str = self.format_work_area_value(hour, context=context)
        weather_str = self.format_work_area_value(weather, context=context)

        return f"{self.name}(hour={hour_str}, weather={weather_str})"
