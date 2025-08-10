from .base import BaseOpcode


class YieldEventVmOpcode(BaseOpcode):

    opcode = 0x58
    name = "YIELD_EVENT_VM"

    def get_args(self):
        return []
