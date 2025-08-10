from .wait_base import SimpleWaitBase


class WaitTimeOpcode(SimpleWaitBase):
    opcode = 0x1C
    name = "WAIT_TIME"
    wait_description = "ticks"
