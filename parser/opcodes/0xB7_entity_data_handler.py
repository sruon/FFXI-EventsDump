from .base import ArgType, BaseOpcode, OpcodeArg


class EntityDataHandlerOpcode(BaseOpcode):
    opcode = 0xB7
    name = "ENTITY_DATA_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("case_type", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on case type."""
        if offset + 2 > len(data):
            return 1  # Fallback

        case_type = data[offset + 1]
        if case_type == 0x01:
            # Case 1: Set entity name (10 bytes)
            return 10
        else:
            # All other cases (8 bytes)
            return 8

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        case_type = args["case_type"]

        # Parse additional parameters based on case
        if len(raw_bytes) >= 8:
            import struct

            entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
            entity_str = self.format_entity_id(entity_id, context=context)

            if case_type == 0x00:
                # Case 0: Store value into entity's event VM
                value = struct.unpack_from("<H", raw_bytes, 6)[0]
                value_str = self.format_work_area_value(value, context=context)
                return f"ENTITY_DATA_HANDLER: Store {value_str} into {entity_str} event VM"

            elif case_type == 0x01:
                # Case 1: Set entity name
                if len(raw_bytes) >= 10:
                    name_offset = struct.unpack_from("<H", raw_bytes, 6)[0]
                    name_str = self.format_work_area_value(name_offset, context=context)
                    name_id = struct.unpack_from("<H", raw_bytes, 8)[0]
                    name_id_str = self.format_work_area_value(name_id, context=context)
                    return f"ENTITY_DATA_HANDLER: Set {entity_str} name from {name_str} (monstrosity: {name_id_str})"
                else:
                    return "ENTITY_DATA_HANDLER: Set entity name (invalid data)"

            elif case_type == 0x02:
                # Case 2: Get entity server ID
                dest_offset = struct.unpack_from("<H", raw_bytes, 6)[0]
                dest_str = self.format_work_area_value(dest_offset, context=context)
                return f"ENTITY_DATA_HANDLER: {dest_str} = {entity_str} server ID"

            elif case_type == 0x03:
                # Case 3: Get entity index
                dest_offset = struct.unpack_from("<H", raw_bytes, 6)[0]
                dest_str = self.format_work_area_value(dest_offset, context=context)
                return f"ENTITY_DATA_HANDLER: {dest_str} = {entity_str} index"

            elif case_type == 0x04:
                # Case 4: Get entity index for user index array
                dest_offset = struct.unpack_from("<H", raw_bytes, 6)[0]
                dest_str = self.format_work_area_value(dest_offset, context=context)
                return f"ENTITY_DATA_HANDLER: {dest_str} = {entity_str} user index"

            else:
                # Unknown case type
                return f"ENTITY_DATA_HANDLER: Unknown case 0x{case_type:02X} for {entity_str}"
        else:
            return f"ENTITY_DATA_HANDLER: Case 0x{case_type:02X} (invalid data)"
