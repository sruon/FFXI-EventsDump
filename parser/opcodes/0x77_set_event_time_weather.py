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

        # Check if hour is a reference (0x8000-0x8FFF range)
        if 0x8000 <= hour <= 0x8FFF:
            ref_index = hour & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                hour_str = f"{ref_value}*"
            else:
                hour_str = f"References[{ref_index}]"
        else:
            hour_str = str(hour)

        # Check if weather is a reference (0x8000-0x8FFF range)
        if 0x8000 <= weather <= 0x8FFF:
            ref_index = weather & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                weather_str = f"{ref_value}*"
            else:
                weather_str = f"References[{ref_index}]"
        else:
            weather_str = str(weather)

        return f"{self.name}(hour={hour_str}, weather={weather_str})"
