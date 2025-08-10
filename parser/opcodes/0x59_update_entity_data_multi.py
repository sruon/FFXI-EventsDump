from .base import ArgType, BaseOpcode, OpcodeArg


class UpdateEntityDataMultiOpcode(BaseOpcode):

    opcode = 0x59
    name = "UPDATE_ENTITY_DATA_MULTI"

    def get_args(self):
        return [
            OpcodeArg(
                "mode",
                ArgType.BYTE,
                1,
                "Update mode (determines additional parameters)",
            ),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        if offset + 2 > len(data):
            return 1

        mode = data[offset + 1]
        if mode == 0 or mode == 2 or mode == 7:
            return 4
        elif mode == 6:
            return 6
        elif mode == 5:
            return 7
        elif mode == 1 or mode == 3 or mode == 4 or mode == 8:
            return 8
        else:
            return 4

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        mode = args["mode"]

        if mode == 0 and len(raw_bytes) >= 4:
            import struct

            speed = struct.unpack_from("<H", raw_bytes, 2)[0]
            speed_str = self.format_work_area_value(speed, context=context)
            return f"UPDATE_ENTITY_DATA: Set EventEntity target turn speed = {speed_str}"

        elif mode == 1 and len(raw_bytes) >= 8:
            import struct

            entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
            speed = struct.unpack_from("<H", raw_bytes, 6)[0]
            entity_str = self.format_entity_id(entity_id, context=context)
            speed_str = self.format_work_area_value(speed, context=context)
            return f"UPDATE_ENTITY_DATA: Set {entity_str} turn speed = {speed_str}"

        elif mode == 2 and len(raw_bytes) >= 4:
            import struct

            speed = struct.unpack_from("<H", raw_bytes, 2)[0]
            speed_str = self.format_work_area_value(speed, context=context)
            return f"UPDATE_ENTITY_DATA: Set EventEntity target turn speed head = {speed_str}"

        elif mode == 3 and len(raw_bytes) >= 8:
            import struct

            entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
            speed = struct.unpack_from("<H", raw_bytes, 6)[0]
            entity_str = self.format_entity_id(entity_id, context=context)
            speed_str = self.format_work_area_value(speed, context=context)
            return f"UPDATE_ENTITY_DATA: Set {entity_str} turn speed head = {speed_str}"

        elif mode == 4 and len(raw_bytes) >= 8:
            import struct

            entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
            speed = struct.unpack_from("<H", raw_bytes, 6)[0]
            entity_str = self.format_entity_id(entity_id, context=context)
            speed_str = self.format_work_area_value(speed, context=context)
            return f"UPDATE_ENTITY_DATA: Set {entity_str} main speed = {speed_str} * 0.1"

        elif mode == 5 and len(raw_bytes) >= 7:
            import struct

            entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
            flag_byte = raw_bytes[6] if len(raw_bytes) > 6 else 0
            entity_str = self.format_entity_id(entity_id, context=context)
            if flag_byte & 1:
                return f"UPDATE_ENTITY_DATA: {entity_str}->Render.Flags0 |= 0x200000"
            else:
                return f"UPDATE_ENTITY_DATA: {entity_str}->Render.Flags0 &= ~0x200000"

        elif mode == 6 and len(raw_bytes) >= 6:
            import struct

            entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
            entity_str = self.format_entity_id(entity_id, context=context)
            return f"UPDATE_ENTITY_DATA: Check if {entity_str} is performing moving action"

        elif mode == 7 and len(raw_bytes) >= 4:
            import struct

            flag = struct.unpack_from("<H", raw_bytes, 2)[0]
            flag_str = self.format_work_area_value(flag, context=context)
            return f"UPDATE_ENTITY_DATA: Set EventEntity target movement flag = {flag_str}"

        elif mode == 8 and len(raw_bytes) >= 8:
            import struct

            entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
            flag = struct.unpack_from("<H", raw_bytes, 6)[0]
            entity_str = self.format_entity_id(entity_id, context=context)
            flag_str = self.format_work_area_value(flag, context=context)
            return f"UPDATE_ENTITY_DATA: Set {entity_str} movement flag = {flag_str}"

        else:
            return f"UPDATE_ENTITY_DATA: Unknown mode {mode}"
