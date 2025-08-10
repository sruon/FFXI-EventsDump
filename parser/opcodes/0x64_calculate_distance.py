from .base import ArgType, BaseOpcode, OpcodeArg


class CalculateDistanceOpcode(BaseOpcode):

    opcode = 0x64
    name = "CALCULATE_DISTANCE"

    def get_args(self):
        return [
            OpcodeArg("dest_offset", ArgType.WORD, 2, "Destination work offset for result (offset 1)"),
            OpcodeArg("x1_offset", ArgType.WORD, 2, "First point X coordinate work offset (offset 3)"),
            OpcodeArg("z1_offset", ArgType.WORD, 2, "First point Z coordinate work offset (offset 5)"),
            OpcodeArg("x2_offset", ArgType.WORD, 2, "Second point X coordinate work offset (offset 7)"),
            OpcodeArg("z2_offset", ArgType.WORD, 2, "Second point Z coordinate work offset (offset 9)"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        dest = args["dest_offset"]
        x1 = args["x1_offset"]
        z1 = args["z1_offset"]
        x2 = args["x2_offset"]
        z2 = args["z2_offset"]

        dest_str = self.format_work_area_value(dest, context=context)
        x1_str = self.format_work_area_value(x1, context=context)
        z1_str = self.format_work_area_value(z1, context=context)
        x2_str = self.format_work_area_value(x2, context=context)
        z2_str = self.format_work_area_value(z2, context=context)

        return f"CALCULATE_DISTANCE: {dest_str} = distance between point1({x1_str}, {z1_str}) and point2({x2_str}, {z2_str})"
