from .base import ArgType, BaseOpcode, OpcodeArg


class SetEntityPositionOpcode(BaseOpcode):
    opcode = 0xBA
    name = "SET_ENTITY_POSITION"

    def get_args(self):
        return [
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
            OpcodeArg("pos_x", ArgType.WORD, 2, ""),
            OpcodeArg("pos_z", ArgType.WORD, 2, ""),
            OpcodeArg("pos_y", ArgType.WORD, 2, ""),
            OpcodeArg("direction", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        entity_id = args["entity_id"]
        entity_repr = self.format_entity_id(entity_id, context=context)

        position_reprs = {
            "pos_x": self.format_coordinate_value(args["pos_x"], context),
            "pos_z": self.format_coordinate_value(args["pos_z"], context),
            "pos_y": self.format_coordinate_value(args["pos_y"], context),
            "direction": self.format_direction_value(args["direction"], context),
        }

        return (
            f"{self.name}("
            f"entity_id={entity_repr}, "
            f"pos_x={position_reprs['pos_x']}, "
            f"pos_z={position_reprs['pos_z']}, "
            f"pos_y={position_reprs['pos_y']}, "
            f"direction={position_reprs['direction']})"
        )
