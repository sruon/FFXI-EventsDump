from .base import ArgType, BaseOpcode, OpcodeArg


class DeliveryBoxHandlerOpcode(BaseOpcode):
    opcode = 0xB2
    name = "DELIVERY_BOX_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, ""),
        ]
