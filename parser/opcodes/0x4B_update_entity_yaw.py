from .base import ArgType, BaseOpcode, OpcodeArg


class UpdateEntityYawOpcode(BaseOpcode):

    opcode = 0x4B
    name = "UPDATE_ENTITY_YAW"

    def get_args(self):
        return [
            OpcodeArg("entity", ArgType.ENTITY_ID, 4, "Entity to rotate"),
            OpcodeArg("yaw", ArgType.WORD, 2, "Yaw rotation value"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:

        entity = args.get("entity", 0)
        yaw = args.get("yaw", 0)

        # Format entity ID
        entity_str = self.format_entity_id(entity, context=context)

        # Format yaw (WORD value that could be reference)
        if 0x8000 <= yaw <= 0x8FFF:
            ref_index = yaw & 0x7FFF
            if context and context.imed_data and ref_index < len(context.imed_data):
                ref_value = context.imed_data[ref_index]
                rotation = (ref_value / 65536.0) * 360.0
                yaw_str = f"{rotation:.2f}°*"
            else:
                yaw_str = f"References[{ref_index}]"
        else:
            # Direct value - convert to rotation
            rotation = (yaw / 65536.0) * 360.0
            yaw_str = f"{rotation:.2f}°"

        return f"{self.name}(entity={entity_str}, yaw={yaw_str})"
