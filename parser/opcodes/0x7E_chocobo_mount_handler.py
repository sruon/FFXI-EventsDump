from .base import ArgType, BaseOpcode, OpcodeArg


class ChocoboMountHandlerOpcode(BaseOpcode):
    opcode = 0x7E
    name = "CHOCOBO_MOUNT_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on mode."""
        if offset + 2 > len(data):
            return 1  # Fallback

        mode = data[offset + 1]

        # Based on documentation:
        if mode == 3:
            return 16
        elif mode == 6:
            return 18
        elif mode == 7:
            return 8
        elif mode in [0, 1, 2, 4, 5, 8]:
            return 6
        else:
            return 6  # Default

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None) -> str:
        mode = args["mode"]

        if mode in [0, 5]:
            if len(raw_bytes) >= 6:
                import struct

                entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
                entity_str = self.format_entity_id(entity_id, context=context)
                return f"CHOCOBO_MOUNT: Dismount {entity_str} (status = 0)"
            return "CHOCOBO_MOUNT: Dismount (invalid data)"

        elif mode == 1:
            if len(raw_bytes) >= 6:
                import struct

                entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
                entity_str = self.format_entity_id(entity_id, context=context)
                return f"CHOCOBO_MOUNT: Mount chocobo on {entity_str} (status = 5)"
            return "CHOCOBO_MOUNT: Mount chocobo (invalid data)"

        elif mode == 2:
            if len(raw_bytes) >= 6:
                import struct

                entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
                entity_str = self.format_entity_id(entity_id, context=context)
                return f"CHOCOBO_MOUNT: Execute attachment function on {entity_str}"
            return "CHOCOBO_MOUNT: Execute attachment (invalid data)"

        elif mode == 3:
            if len(raw_bytes) >= 16:
                import struct

                entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
                entity_str = self.format_entity_id(entity_id, context=context)
                chocobo_data = struct.unpack_from("<HHH", raw_bytes, 6)[:3]
                chocobo_str = f"index={chocobo_data[0]}, color={chocobo_data[1]}, name_id={chocobo_data[2]}"
                return f"CHOCOBO_MOUNT: Mount custom chocobo on {entity_str} ({chocobo_str})"
            return "CHOCOBO_MOUNT: Mount custom chocobo (invalid data)"

        elif mode == 4:
            if len(raw_bytes) >= 6:
                import struct

                entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
                entity_str = self.format_entity_id(entity_id, context=context)
                return f"CHOCOBO_MOUNT: Mode 4 on {entity_str}"
            return "CHOCOBO_MOUNT: Mode 4 (invalid data)"

        elif mode == 6:
            if len(raw_bytes) >= 18:
                import struct

                entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
                entity_str = self.format_entity_id(entity_id, context=context)
                # extra_data = struct.unpack_from("<HHHHHH", raw_bytes, 6)  # Future use
                return f"CHOCOBO_MOUNT: Mode 6 (custom mount) on {entity_str}"
            return "CHOCOBO_MOUNT: Mode 6 (invalid data)"

        elif mode == 7:
            if len(raw_bytes) >= 8:
                import struct

                entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
                mount_id = struct.unpack_from("<H", raw_bytes, 6)[0]
                entity_str = self.format_entity_id(entity_id, context=context)
                mount_str = self.format_work_area_value(mount_id, context=context)
                return f"CHOCOBO_MOUNT: Mount {entity_str} on mount ID {mount_str} (status = 85)"
            return "CHOCOBO_MOUNT: Mount specific (invalid data)"

        elif mode == 8:
            if len(raw_bytes) >= 6:
                import struct

                entity_id = struct.unpack_from("<I", raw_bytes, 2)[0]
                entity_str = self.format_entity_id(entity_id, context=context)
                return f"CHOCOBO_MOUNT: Dismount {entity_str} from mount (status = 0, MountId = 0)"
            return "CHOCOBO_MOUNT: Dismount from mount (invalid data)"

        else:
            return f"CHOCOBO_MOUNT: Unknown mode {mode}"
