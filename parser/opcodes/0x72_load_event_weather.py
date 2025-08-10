from .base import ArgType, BaseOpcode, OpcodeArg


class LoadEventWeatherOpcode(BaseOpcode):
    opcode = 0x72
    name = "LOAD_EVENT_WEATHER"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, ""),
            OpcodeArg("weather_id", ArgType.WORD, 2, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on mode."""
        if offset + 2 > len(data):
            return 1  # Fallback

        mode = data[offset + 1]

        # Based on documentation:
        # Mode 0: 10 bytes (request weather file, includes additional parameters)
        # Mode 1: 6 bytes (process loaded weather data)
        # Other: 4 bytes (basic format)
        if mode == 0:
            return 10
        elif mode == 1:
            return 6
        else:
            return 4  # Default for unknown modes or basic format

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        mode = args["mode"]
        weather_id = args["weather_id"]
        weather_str = self.format_work_area_value(weather_id, context=context)
        extra_params = []
        if len(raw_bytes) >= 6:
            import struct

            param1 = struct.unpack_from("<H", raw_bytes, 4)[0]
            param1_str = self.format_work_area_value(param1, context=context)
            extra_params.append(f"param1={param1_str}")

        if len(raw_bytes) >= 10:
            param2 = struct.unpack_from("<I", raw_bytes, 6)[0]
            # Could be entity ID or other value
            param2_str = (
                self.format_entity_id(param2, context=context) if param2 > 0x1000000 else self.format_work_area_value(param2, context=context)
            )
            extra_params.append(f"param2={param2_str}")

        params_str = ", " + ", ".join(extra_params) if extra_params else ""

        if mode == 0:
            return f"LOAD_EVENT_WEATHER: Request weather file 7033, weather_id={weather_str}{params_str}"
        elif mode == 1:
            return f"LOAD_EVENT_WEATHER: Process loaded weather data, weather_id={weather_str}{params_str}"
        else:
            return f"LOAD_EVENT_WEATHER: Unknown mode {mode}, weather_id={weather_str}{params_str}"
