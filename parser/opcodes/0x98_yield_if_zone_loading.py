from .base import BaseOpcode


class YieldIfZoneLoadingOpcode(BaseOpcode):
    opcode = 0x98
    name = "YIELD_IF_ZONE_LOADING"
