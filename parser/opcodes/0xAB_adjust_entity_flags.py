from .base import ArgType, BaseOpcode, OpcodeArg


class AdjustEntityFlagsOpcode(BaseOpcode):
    opcode = 0xAB
    name = "ADJUST_ENTITY_FLAGS"

    def get_args(self):
        return [
            OpcodeArg("sub_case", ArgType.BYTE, 1, ""),
        ]

    def parse_args(self, data: bytes) -> dict:
        """Parse arguments based on sub-case value."""
        if len(data) < 2:
            return {"sub_case": 0}

        sub_case = data[1]
        result = {"sub_case": sub_case}

        # Parse additional parameters based on sub-case
        if sub_case == 0x11 or (0x14 <= sub_case <= 0x18):
            # 2-byte parameter
            if len(data) >= 4:
                param = int.from_bytes(data[2:4], byteorder="little")
                result["parameter"] = param
        elif sub_case == 0x1B or sub_case == 0x1C:
            # 4-byte parameter (entity ID)
            if len(data) >= 6:
                entity_id = int.from_bytes(data[2:6], byteorder="little")
                result["entity_id"] = entity_id

        return result

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        sub_case = args["sub_case"]

        # Build specific representations for each sub-case
        if sub_case == 0x01:
            return "EventEntity->Render.Flags0 |= 0x10000 // Set bit 16"
        elif sub_case == 0x02:
            return "EventEntity->Render.Flags0 &= ~0x10000 // Clear bit 16"
        elif sub_case == 0x03:
            return "EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17"
        elif sub_case == 0x04:
            return "EventEntity->Render.Flags0 |= 0x40000 // Set bit 18"
        elif sub_case == 0x05:
            return "EventEntity->Render.Flags0 &= ~0x40000 // Clear bit 18"
        elif sub_case == 0x06:
            return "EventEntity->Render.Flags0 ^= (Flags0 ^ 0x200000) & 0x200000 // Manipulate bit 21"
        elif sub_case == 0x07:
            return "EventEntity->Render.Flags2 |= 0x01 // Set bit 0"
        elif sub_case == 0x08:
            return "EventEntity->Render.Flags2 |= 0x02 // Set bit 1"
        elif sub_case == 0x09:
            return "EventEntity->UnknownFlag = 1 // Enable unknown flag"
        elif sub_case == 0x0A:
            return "EventEntity->UnknownFlag = 0 // Disable unknown flag"
        elif sub_case == 0x0B:
            return "EventEntity->Render.Flags0 ^= 0x100000 // Toggle bit 20"
        elif sub_case == 0x0C:
            return "EventEntity->Render.Flags0 ^= 0x400000 // Toggle bit 22"
        elif sub_case == 0x0D:
            return "EventEntity->Render.Flags4 |= 0x01 // Set bit 0"
        elif sub_case == 0x0E:
            return "EventEntity->Render.Flags4 |= 0x02 // Set bit 1"
        elif sub_case == 0x0F:
            return "EventEntity->CalibrationFlag = 1 // Set calibration flag"
        elif sub_case == 0x10:
            return "EventEntity->CalibrationFlag = 0 // Clear calibration flag"
        elif sub_case == 0x11:
            param_str = self.format_work_area_value(args["parameter"], context=context)
            return f"EventEntity->DespawnValue = {param_str} // Set despawn value"
        elif sub_case == 0x12:
            return "EventEntity->Render.Flags2 |= 0x04 // Set bit 2"
        elif sub_case == 0x13:
            return "EventEntity->Render.Flags2 &= ~0x04 // Clear bit 2"
        elif 0x14 <= sub_case <= 0x18:
            param_str = self.format_work_area_value(args["parameter"], context=context)
            helper_num = sub_case - 0x13
            return f"CallHelperFunction{helper_num}({param_str}) // Helper function {helper_num}"
        elif sub_case == 0x19:
            return "EventEntity->Render.Flags7 |= 0x0C // Set bits 2 and 3"
        elif sub_case == 0x1A:
            return "EventEntity->Render.Flags7 &= ~0x0C // Clear bits 2 and 3"
        elif sub_case == 0x1B:
            entity_id = args["entity_id"]
            entity_str = self.format_entity_id(entity_id, context=context)
            return f"{entity_str}->Render.Flags7 |= 0x0C // OR bits 2 and 3"
        elif sub_case == 0x1C:
            entity_id = args["entity_id"]
            entity_str = self.format_entity_id(entity_id, context=context)
            return f"{entity_str}->Render.Flags7 &= ~0x0C // AND NOT bits 2 and 3"
        else:
            # Fallback for unknown sub-cases
            return f"ADJUST_ENTITY_FLAGS: Unknown sub_case 0x{sub_case:02X}"

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on sub-case."""
        if offset + 2 > len(data):
            return 1  # Fallback

        sub_case = data[offset + 1]

        # Exact byte counts from Atomos spec for EVERY sub-case:
        length_map = {
            0x00: 2,  # Step forward (deprecated?)
            0x01: 2,  # Set Render.Flags0 bit
            0x02: 2,  # Clear Render.Flags0 bit
            0x03: 2,  # Toggle Render.Flags0 bit
            0x04: 2,  # Set Render.Flags0 bit (alt)
            0x05: 2,  # Clear Render.Flags0 bit (alt)
            0x06: 2,  # Manipulate Render.Flags0
            0x07: 2,  # Adjust Render.Flags2
            0x08: 2,  # Adjust Render.Flags2 (alt)
            0x09: 2,  # Enable unknown flag
            0x0A: 2,  # Disable unknown flag
            0x0B: 2,  # Toggle Render.Flags0 bit
            0x0C: 2,  # Toggle Render.Flags0 bit (alt)
            0x0D: 2,  # Modify Render.Flags4
            0x0E: 2,  # Modify Render.Flags4 (alt)
            0x0F: 2,  # Set calibration flag
            0x10: 2,  # Clear calibration flag
            0x11: 4,  # Set despawn value (has 2-byte parameter)
            0x12: 2,  # Set Render.Flags2 bit
            0x13: 2,  # Clear Render.Flags2 bit
            0x14: 4,  # Call helper function 1 (has 2-byte parameter)
            0x15: 4,  # Call helper function 2 (has 2-byte parameter)
            0x16: 4,  # Call helper function 3 (has 2-byte parameter)
            0x17: 4,  # Call helper function 4 (has 2-byte parameter)
            0x18: 4,  # Call helper function 5 (has 2-byte parameter)
            0x19: 2,  # Set Render.Flags7 bits
            0x1A: 2,  # Clear Render.Flags7 bits
            0x1B: 6,  # OR Render.Flags7 (has 4-byte entity parameter)
            0x1C: 6,  # AND Render.Flags7 (has 4-byte entity parameter)
        }

        # Return the exact length for known sub-cases, or 2 for unknown
        return length_map.get(sub_case, 2)
