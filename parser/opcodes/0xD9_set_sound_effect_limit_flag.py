from .base import ArgType, BaseOpcode, OpcodeArg


class SetSoundEffectLimitFlagOpcode(BaseOpcode):
    opcode = 0xD9
    name = "SET_SOUND_EFFECT_LIMIT_FLAG"

    def get_args(self):
        return [
            OpcodeArg("flag_value", ArgType.BYTE, 1, "Flag value for sound effect limits"),
        ]
