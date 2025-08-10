from .base import ArgType, BaseOpcode, OpcodeArg


class CreateFrameDelayOpcode(BaseOpcode):

    opcode = 0x57
    name = "CREATE_FRAME_DELAY"

    def get_args(self):
        return [
            OpcodeArg(
                "delay_work_offset",
                ArgType.WORD,
                2,
                "Work area offset for value and result storage",
            ),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        delay_str = self.format_work_area_value(args["delay_work_offset"], context=context)

        return f"{self.name}(delay={delay_str})"
