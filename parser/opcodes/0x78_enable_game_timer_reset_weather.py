from .base import BaseOpcode


class EnableGameTimerResetWeatherOpcode(BaseOpcode):
    opcode = 0x78
    name = "ENABLE_GAME_TIMER_RESET_WEATHER"
