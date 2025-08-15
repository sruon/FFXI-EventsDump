from .base import ArgType, BaseOpcode, OpcodeArg


class SetEntityDirectionOpcode(BaseOpcode):
    opcode = 0x39
    name = "SET_ENTITY_DIRECTION"

    def get_args(self):
        return [
            OpcodeArg("direction", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        direction_str = self.format_yaw_value(args["direction"], context=context)
        return f"{self.name}(direction={direction_str})"
