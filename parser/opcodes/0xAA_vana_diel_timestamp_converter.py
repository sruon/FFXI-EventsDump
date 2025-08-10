from .base import ArgType, BaseOpcode, OpcodeArg


class VanaDielTimestampConverterOpcode(BaseOpcode):
    opcode = 0xAA
    name = "VANA_DIEL_TIMESTAMP_CONVERTER"

    def get_args(self):
        return [
            OpcodeArg("timestamp", ArgType.WORD, 2, ""),
            OpcodeArg("year", ArgType.WORD, 2, ""),
            OpcodeArg("month", ArgType.WORD, 2, ""),
            OpcodeArg("day", ArgType.WORD, 2, ""),
            OpcodeArg("weekday", ArgType.WORD, 2, ""),
            OpcodeArg("hour", ArgType.WORD, 2, ""),
            OpcodeArg("minute", ArgType.WORD, 2, ""),
            OpcodeArg("moon", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        # Format all work offsets
        timestamp_str = self.format_work_area_value(args["timestamp"], context=context)
        year_str = self.format_work_area_value(args["year"], context=context)
        month_str = self.format_work_area_value(args["month"], context=context)
        day_str = self.format_work_area_value(args["day"], context=context)
        weekday_str = self.format_work_area_value(args["weekday"], context=context)
        hour_str = self.format_work_area_value(args["hour"], context=context)
        minute_str = self.format_work_area_value(args["minute"], context=context)
        moon_str = self.format_work_area_value(args["moon"], context=context)

        return (
            f"{self.name}(timestamp={timestamp_str}, year={year_str}, "
            f"month={month_str}, day={day_str}, weekday={weekday_str}, "
            f"hour={hour_str}, minute={minute_str}, moon={moon_str})"
        )
