from .base import ArgType, BaseOpcode, OpcodeArg


class SetEntityEventDirOpcode(BaseOpcode):
    opcode = 0xD8
    name = "SET_ENTITY_EVENT_DIR"

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate length based on mode byte"""
        if offset + 1 >= len(data):
            return 6  # Default length

        mode = data[offset + 1]
        if mode == 0x00:
            return 6  # Copy LastPosition case
        elif mode in [0x01, 0x02, 0x03]:
            return 8  # Single direction value case
        elif mode == 0x04:
            return 12  # Three direction values case
        else:
            return 6  # Default case

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, "Operation mode (0=copy LastPosition, 1-3=set single dir, 4=set all dirs)"),
            OpcodeArg("entity_server_id", ArgType.DWORD, 4, "Entity server ID"),
            OpcodeArg("direction1", ArgType.WORD, 2, "Direction value 1 (modes 1-4)"),
            OpcodeArg("direction2", ArgType.WORD, 2, "Direction value 2 (mode 4 only)"),
            OpcodeArg("direction3", ArgType.WORD, 2, "Direction value 3 (mode 4 only)"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        if not args:
            args = self.parse_args(raw_bytes)

        mode = args.get("mode", 0)
        entity_id = args.get("entity_server_id", 0)

        # Format entity ID
        entity_str = self.format_entity_id(entity_id, context=context)

        if mode == 0x00:
            return f"SET_ENTITY_EVENT_DIR: Copy {entity_str} LastPosition to EventDir"
        elif mode == 0x01:
            dir_val = args.get("direction1", 0)
            dir_str = self.format_work_area_value(dir_val, context=context)
            return f"SET_ENTITY_EVENT_DIR: Set {entity_str} EventDir[0] = {dir_str}"
        elif mode == 0x02:
            dir_val = args.get("direction1", 0)
            dir_str = self.format_work_area_value(dir_val, context=context)
            return f"SET_ENTITY_EVENT_DIR: Set {entity_str} EventDir[1] = {dir_str}"
        elif mode == 0x03:
            dir_val = args.get("direction1", 0)
            dir_str = self.format_work_area_value(dir_val, context=context)
            return f"SET_ENTITY_EVENT_DIR: Set {entity_str} EventDir[2] = {dir_str}"
        elif mode == 0x04:
            dir1_str = self.format_work_area_value(args.get("direction1", 0), context=context)
            dir2_str = self.format_work_area_value(args.get("direction2", 0), context=context)
            dir3_str = self.format_work_area_value(args.get("direction3", 0), context=context)
            return f"SET_ENTITY_EVENT_DIR: Set {entity_str} EventDir[0]={dir1_str}, EventDir[1]={dir2_str}, EventDir[2]={dir3_str}"
        else:
            return f"SET_ENTITY_EVENT_DIR: Unknown mode 0x{mode:02X} for {entity_str}"
