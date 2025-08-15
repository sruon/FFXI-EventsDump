from .base import BaseOpcode


class EnableGameTimerOpcode(BaseOpcode):
    opcode = 0xC9
    name = "ENABLE_GAME_TIMER"
