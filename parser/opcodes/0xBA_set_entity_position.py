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
        if entity_id == 0x7FFFFFF0:
            entity_repr = "LocalPlayer"
        elif entity_id == 0x7FFFFFF8:
            entity_repr = "EventEntity"
        elif entity_id & 0x8000:
            # Reference
            ref_index = entity_id - 0x8000
            if context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                # Try to get entity name if available
                if context.zone_entities:
                    entity_name = context.zone_entities.get_entity_display_name(ref_value)
                    if not entity_name.startswith("Unknown NPC"):
                        entity_repr = f"{entity_name}*"
                    else:
                        entity_repr = f"{ref_value}/0x{ref_value:08X}*"
                else:
                    entity_repr = f"{ref_value}/0x{ref_value:08X}*"
            else:
                entity_repr = f"References[{ref_index}]"
        else:
            # Try to get entity name if available
            if context.zone_entities:
                entity_name = context.zone_entities.get_entity_display_name(entity_id)
                entity_repr = entity_name
            else:
                entity_repr = f"0x{entity_id:08X}"

        # Handle position coordinates using standardized methods
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
