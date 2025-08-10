from .base import ArgType, BaseOpcode, OpcodeArg


class SetSoundVolumeOpcode(BaseOpcode):

    opcode = 0x69
    name = "SET_SOUND_VOLUME"

    def get_args(self):
        return [
            OpcodeArg("mute_flag", ArgType.BYTE, 1, ""),
            OpcodeArg("sound_types", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None) -> str:
        mute_flag = args["mute_flag"]
        sound_types = args["sound_types"]

        sound_types_str = self.format_work_area_value(sound_types, context=context)
        types = []
        if isinstance(sound_types, int):
            if sound_types & 0x01:
                types.append("Effects")
            if sound_types & 0x02:
                types.append("System")
            if sound_types & 0x04:
                types.append("Zone")
            if sound_types & 0x08:
                types.append("Master")
            if sound_types & 0x10:
                types.append("SpecialChat")

        types_str = "/".join(types) if types else f"flags={sound_types_str}"

        if mute_flag:
            return f"SET_SOUND_VOLUME: Mute {types_str}"
        else:
            return f"SET_SOUND_VOLUME: Unmute {types_str}"
