from .base import ArgType, BaseOpcode, OpcodeArg


class MultiHandlerComplexOpcode(BaseOpcode):

    opcode = 0x5F
    name = "MULTI_HANDLER_COMPLEX"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, "Handler mode (determines sub-operation)"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        if offset + 2 > len(data):
            return 1

        mode = data[offset + 1]
        if mode == 0 or mode == 1:
            return 2
        elif mode == 2:
            return 6
        elif mode == 3 or mode == 4:
            return 16
        elif mode == 5 or mode == 6:
            return 18
        elif mode == 7:
            return 14
        else:
            return 2

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        mode = args["mode"]

        mode_descriptions = {
            0: "Toggle Render.Flags0 bit 29",
            1: "Toggle Render.Flags0 bit 29",
            2: "Kill entity action (OpCode 0xC1)",
            3: "Load ext scheduler (OpCode 0x5B mode 0)",
            4: "Load ext scheduler (OpCode 0x5B mode 1)",
            5: "Load ext scheduler with flag (OpCode 0x5B mode 0, flag 1)",
            6: "Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1)",
            7: "Wait scheduler task (OpCode 0x53)",
        }

        description = mode_descriptions.get(mode, "Unknown")

        if mode in [3, 4] and len(raw_bytes) >= 16:
            ref_val = int.from_bytes(raw_bytes[2:4], byteorder="little")
            entity1_id = int.from_bytes(raw_bytes[4:8], byteorder="little")
            entity2_id = int.from_bytes(raw_bytes[8:12], byteorder="little")
            string_val = int.from_bytes(raw_bytes[12:16], byteorder="little")

            ref_str = self.format_work_area_value(ref_val, context) if 0x8000 <= ref_val <= 0x8FFF else f"0x{ref_val:04X}"

            entity1_str = self.format_entity_id(entity1_id, context=context)
            entity2_str = self.format_entity_id(entity2_id, context=context)

            try:
                string_bytes = string_val.to_bytes(4, byteorder="little")
                string_ascii = string_bytes.decode("ascii").rstrip("\x00")
                if string_ascii and all(32 <= ord(c) <= 126 for c in string_ascii):
                    string_display = f'"{string_ascii}"'
                else:
                    string_display = f"0x{string_val:08X}"
            except (UnicodeDecodeError, ValueError):
                string_display = f"0x{string_val:08X}"

            return f"{self.name}(mode=0x{mode:02X} - {description}, ref={ref_str}, entity1={entity1_str}, entity2={entity2_str}, string={string_display})"

        elif mode in [5, 6] and len(raw_bytes) >= 18:
            ref_val = int.from_bytes(raw_bytes[2:4], byteorder="little")
            entity1_id = int.from_bytes(raw_bytes[4:8], byteorder="little")
            entity2_id = int.from_bytes(raw_bytes[8:12], byteorder="little")
            string_val = int.from_bytes(raw_bytes[12:16], byteorder="little")
            extra_val = int.from_bytes(raw_bytes[16:18], byteorder="little")

            ref_str = self.format_work_area_value(ref_val, context) if 0x8000 <= ref_val <= 0x8FFF else f"0x{ref_val:04X}"

            entity1_str = self.format_entity_id(entity1_id, context=context)
            entity2_str = self.format_entity_id(entity2_id, context=context)

            try:
                string_bytes = string_val.to_bytes(4, byteorder="little")
                string_ascii = string_bytes.decode("ascii").rstrip("\x00")
                if string_ascii and all(32 <= ord(c) <= 126 for c in string_ascii):
                    string_display = f'"{string_ascii}"'
                else:
                    string_display = f"0x{string_val:08X}"
            except (UnicodeDecodeError, ValueError):
                string_display = f"0x{string_val:08X}"

            extra_str = self.format_work_area_value(extra_val, context) if 0x8000 <= extra_val <= 0x8FFF else f"0x{extra_val:04X}"

            return f"{self.name}(mode=0x{mode:02X} - {description}, ref={ref_str}, entity1={entity1_str}, entity2={entity2_str}, string={string_display}, extra={extra_str})"

        else:
            return f"{self.name}(mode=0x{mode:02X} - {description})"
