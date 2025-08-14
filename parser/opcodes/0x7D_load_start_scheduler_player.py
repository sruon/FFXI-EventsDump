from .base import ArgType, OpcodeArg
from .scheduler_base import SchedulerBase


class LoadStartSchedulerPlayerOpcode(SchedulerBase):
    opcode = 0x7D
    name = "LOAD_START_SCHEDULER_PLAYER"

    def get_args(self):
        return [
            OpcodeArg("animation_id", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        return f"{self.name}: Load scheduler with animation_id {args['animation_id']}"
