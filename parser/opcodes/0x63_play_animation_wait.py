from .base import ArgType, BaseOpcode, OpcodeArg


class PlayAnimationWaitOpcode(BaseOpcode):
    """Sets the event entity to play an animation then waits for it to complete"""

    opcode = 0x63
    name = "PLAY_ANIMATION_WAIT"

    def get_args(self):
        return [
            OpcodeArg("animation_id", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        anim_id = args["animation_id"]

        return f"{self.name}(animation={anim_id})"
