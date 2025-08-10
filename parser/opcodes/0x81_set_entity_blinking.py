from .base import ArgType, BaseOpcode, OpcodeArg


class SetEntityBlinkingOpcode(BaseOpcode):
    opcode = 0x81
    name = "SET_ENTITY_BLINKING"

    def get_args(self):
        return [
            OpcodeArg("blink_flag", ArgType.BYTE, 1, "Whether entity should blink"),
            OpcodeArg("entity", ArgType.ENTITY_ID, 4, "Entity to set blinking status for"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        entity_str = self.format_entity_id(args["entity"], context=context)
        return f"{self.name}(blink_flag=0x{args['blink_flag']:02X}, entity={entity_str})"
