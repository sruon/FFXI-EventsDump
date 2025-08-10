from .base import ArgType, BaseOpcode, OpcodeArg


class ChangeSoundVolumeOpcode(BaseOpcode):
    """Changes sound volume for specified sound types (effect/system/zone/master)"""

    opcode = 0x6A
    name = "CHANGE_SOUND_VOLUME"

    def get_args(self):
        return [
            OpcodeArg("volume", ArgType.WORD, 2, ""),
            OpcodeArg("fade_time", ArgType.WORD, 2, ""),
            OpcodeArg("sound_types", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        volume = args["volume"]
        fade_time = args["fade_time"]
        sound_types = args["sound_types"]

        volume_str = self.format_work_area_value(volume, context=context)
        fade_time_str = self.format_work_area_value(fade_time, context=context)
        if 0x8000 <= sound_types <= 0x8FFF:
            ref_index = sound_types & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                sound_types_val = context.imed_data[ref_index]
            else:
                sound_types_val = sound_types
        else:
            sound_types_val = sound_types

        # Parse sound type flags
        types = []
        if isinstance(sound_types_val, int):
            if sound_types_val & 0x01:
                types.append("Effects")
            if sound_types_val & 0x02:
                types.append("System")
            if sound_types_val & 0x04:
                types.append("Zone")
            if sound_types_val & 0x08:
                types.append("Master")
            if sound_types_val & 0x10:
                types.append("SpecialChat")

        types_str = "/".join(types) if types else self.format_work_area_value(sound_types, context=context)

        return f"CHANGE_SOUND_VOLUME: Set {types_str} volume to {volume_str}, fade_time={fade_time_str}"
