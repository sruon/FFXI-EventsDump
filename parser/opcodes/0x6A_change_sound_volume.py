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
        volume_str = self.format_work_area_value(args["volume"], context=context)
        fade_time_str = self.format_work_area_value(args["fade_time"], context=context)
        
        # Resolve reference for sound_types to parse flags
        sound_types_val, was_ref = self.resolve_reference_value(args["sound_types"], context=context)
        
        # Parse sound type flags if we have a resolved value
        types = []
        if isinstance(sound_types_val, int) and sound_types_val < 0x8000:
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

        if types:
            types_str = "/".join(types)
            if was_ref:
                types_str = f"({types_str})*"
        else:
            types_str = self.format_work_area_value(args["sound_types"], context=context)

        return f"CHANGE_SOUND_VOLUME: Set {types_str} volume to {volume_str}, fade_time={fade_time_str}"
