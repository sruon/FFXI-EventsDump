from .base import ArgType, BaseOpcode, OpcodeArg


class SetMusicVolumeOpcode(BaseOpcode):

    opcode = 0x5D
    name = "SET_MUSIC_VOLUME"

    def get_args(self):
        return [
            OpcodeArg("volume", ArgType.WORD, 2, "Target volume level"),
            OpcodeArg("fade_time", ArgType.WORD, 2, "Fade transition time"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        volume = args["volume"]
        fade_time = args["fade_time"]

        volume_str = self.format_work_area_value(volume, context=context)
        fade_time_str = self.format_work_area_value(fade_time, context=context)

        return f"{self.name}(volume={volume_str}, fade_time={fade_time_str})"
