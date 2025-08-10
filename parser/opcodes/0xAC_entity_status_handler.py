from .base import ArgType, BaseOpcode, OpcodeArg


class EntityStatusHandlerOpcode(BaseOpcode):
    opcode = 0xAC
    name = "ENTITY_STATUS_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("case_type", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate the length based on the case type."""
        if offset >= len(data):
            return 1

        case_type = data[offset + 1] if offset + 1 < len(data) else 0

        # Based on Atomos documentation
        if case_type == 0x00 or case_type == 0x01:
            return 4  # 1 + 1 + 2 (case + word value)
        elif case_type == 0x02 or case_type == 0x03:
            return 6  # 1 + 1 + 4 (case + entity)
        elif case_type == 0x04:
            return 8  # 1 + 1 + 4 + 2 (case + entity + value)
        else:
            return 4  # Default to minimum

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        case_type = args["case_type"]

        # Only handle documented cases 0x00-0x04
        if case_type == 0x00 and len(raw_bytes) >= 4:
            # Case 0: Set StatusServer
            value = int.from_bytes(raw_bytes[2:4], byteorder="little")
            value_str = self.format_work_area_value(value, context=context)
            return f"EventEntity->StatusServer = {value_str}"

        elif case_type == 0x01 and len(raw_bytes) >= 4:
            # Case 1: Set StatusEvent
            value = int.from_bytes(raw_bytes[2:4], byteorder="little")
            value_str = self.format_work_area_value(value, context=context)
            return f"EventEntity->StatusEvent = {value_str}"

        elif case_type == 0x02 and len(raw_bytes) >= 6:
            # Case 2: Set entity Render.Flags6
            entity_id = int.from_bytes(raw_bytes[2:6], byteorder="little")
            entity_str = self.format_entity_id(entity_id, context=context)
            return f"{entity_str}->Render.Flags6 |= 0x02 // Set bit 1"

        elif case_type == 0x03 and len(raw_bytes) >= 6:
            # Case 3: Set entity Render.Flags6 (same as case 2)
            entity_id = int.from_bytes(raw_bytes[2:6], byteorder="little")
            entity_str = self.format_entity_id(entity_id, context=context)
            return f"{entity_str}->Render.Flags6 |= 0x02 // Set bit 1"

        elif case_type == 0x04 and len(raw_bytes) >= 8:
            # Case 4: Set entity Render.Flags7 with value
            entity_id = int.from_bytes(raw_bytes[2:6], byteorder="little")
            flags_value = int.from_bytes(raw_bytes[6:8], byteorder="little")
            entity_str = self.format_entity_id(entity_id, context=context)
            flags_str = self.format_work_area_value(flags_value, context=context)
            return f"{entity_str}->Render.Flags7 = {flags_str}"

        else:
            # Unknown/invalid case - likely from bad parse
            return f"ENTITY_STATUS_HANDLER: Invalid case 0x{case_type:02X} (bad parse?)"
