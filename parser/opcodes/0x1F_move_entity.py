from .base import ArgType, BaseOpcode, OpcodeArg


class MoveEntityOpcode(BaseOpcode):
    opcode = 0x1F
    name = "MOVE_ENTITY"

    def get_args(self):
        return [
            OpcodeArg(
                "mode",
                ArgType.BYTE,
                1,
                "Mode: 0=Initial movement setup, 1=Update position",
            ),
        ]

    def parse_args(self, data: bytes) -> dict:
        if len(data) < 2:
            return {"mode": 0}

        mode = data[1]
        result = {"mode": mode}

        if mode == 0 and len(data) >= 8:
            x_raw = int.from_bytes(data[2:4], byteorder="little")
            z_raw = int.from_bytes(data[4:6], byteorder="little")
            y_raw = int.from_bytes(data[6:8], byteorder="little")

            result.update(
                {
                    "x_coord": x_raw,
                    "z_coord": z_raw,
                    "y_coord": y_raw,
                }
            )

        return result

    def calculate_length(self, data: bytes, offset: int) -> int:
        if offset + 2 > len(data):
            return 1

        mode = data[offset + 1]
        if mode == 0:
            return 8
        else:
            return 2

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        mode = args["mode"]

        if mode == 0:
            x_raw = args["x_coord"]
            z_raw = args["z_coord"]
            y_raw = args["y_coord"]

            coord_reprs = {}
            for name, raw_value in [
                ("x_coord", x_raw),
                ("z_coord", z_raw),
                ("y_coord", y_raw),
            ]:
                if 0x8000 <= raw_value <= 0x8FFF:
                    ref_index = raw_value & 0x7FFF
                    if context and context.imed_data and ref_index < len(context.imed_data):
                        ref_value = context.imed_data[ref_index]
                        float_val = self.convert_coordinate_to_float(ref_value)
                        coord_reprs[name] = f"{float_val:.3f}*"
                    else:
                        coord_reprs[name] = f"References[{ref_index}]"
                else:
                    float_val = self.convert_coordinate_to_float(raw_value)
                    coord_reprs[name] = f"{float_val:.3f}"

            return f"MOVE_ENTITY: EventEntity moves to X={coord_reprs['x_coord']}, Z={coord_reprs['z_coord']}, Y={coord_reprs['y_coord']}"
        else:
            return f"MOVE_ENTITY: Update entity position (mode={mode})"
