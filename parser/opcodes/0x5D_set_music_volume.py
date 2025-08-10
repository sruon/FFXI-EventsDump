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

        if 0x8000 <= volume <= 0x8FFF:
            ref_index = volume & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                volume_str = f"{ref_value}*"
            else:
                volume_str = f"References[{ref_index}]"
        else:
            volume_str = str(volume)

        if 0x8000 <= fade_time <= 0x8FFF:
            ref_index = fade_time & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                fade_time_str = f"{ref_value}*"
            else:
                fade_time_str = f"References[{ref_index}]"
        else:
            fade_time_str = str(fade_time)

        return f"{self.name}(volume={volume_str}, fade_time={fade_time_str})"
