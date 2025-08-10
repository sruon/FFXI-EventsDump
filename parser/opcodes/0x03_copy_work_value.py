from .base import ArgType, BaseOpcode, OpcodeArg


class CopyWorkValueOpcode(BaseOpcode):
    opcode = 0x03
    name = "COPY_WORK_VALUE"

    def get_args(self):
        return [
            OpcodeArg("dest_offset", ArgType.WORD, 2, "Destination work offset to store to"),
            OpcodeArg("source_offset", ArgType.WORD, 2, "Source work offset to get from"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        source_str = self.format_work_area_value(args["source_offset"], context=context)
        dest_str = self.format_work_area_value(args["dest_offset"], context=context)
        return f"{dest_str} = {source_str}"
