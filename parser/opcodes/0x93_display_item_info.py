from .base import ArgType, BaseOpcode, OpcodeArg


class DisplayItemInfoOpcode(BaseOpcode):
    opcode = 0x93
    name = "DISPLAY_ITEM_INFO"

    def get_args(self):
        return [
            OpcodeArg("item_id", ArgType.WORD, 2, "Item ID to display information for"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        item_id = args["item_id"]
        item_str = self.format_work_area_value(item_id, context=context)

        return f"{self.name}(item_id={item_str})"
