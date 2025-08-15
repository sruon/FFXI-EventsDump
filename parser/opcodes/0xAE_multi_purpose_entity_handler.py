from .base import ArgType, BaseOpcode, OpcodeArg


class MultiPurposeEntityHandlerOpcode(BaseOpcode):
    opcode = 0xAE
    name = "MULTI_PURPOSE_ENTITY_HANDLER"

    def get_args(self):
        return [
            OpcodeArg("case_type", ArgType.BYTE, 1, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        if offset >= len(data):
            return 1

        case_type = data[offset + 1] if offset + 1 < len(data) else 0

        case_lengths = {
            0x00: 6,  # Weather related
            0x01: 8,  # Entity name color
            0x02: 8,  # Same as 0x01
            0x03: 8,  # Mou4 value
            0x04: 8,  # Same as 0x03
            0x05: 10,  # ActorPointer link
            0x06: 6,  # Unset ActorPointer
            0x07: 10,  # EnvironmentAreaId
            0x08: 10,  # EnvironmentAreaId to 0
        }

        return case_lengths.get(case_type, 2)

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments based on case type."""
        args = {}
        if len(raw_bytes) < 2:
            return args

        args["case_type"] = raw_bytes[1]

        # Parse additional parameters based on case type
        case_type = args["case_type"]

        if case_type == 0x00 and len(raw_bytes) >= 6:
            # Weather related
            args["param1"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
            args["param2"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
        elif case_type in [0x01, 0x02, 0x03, 0x04] and len(raw_bytes) >= 8:
            # Entity operations (name color or Mou4)
            args["entity_id"] = int.from_bytes(raw_bytes[2:6], byteorder="little")
            args["value"] = int.from_bytes(raw_bytes[6:8], byteorder="little")
        elif case_type in [0x05, 0x07, 0x08] and len(raw_bytes) >= 10:
            # Two entity operations or EnvironmentAreaId
            args["entity1_id"] = int.from_bytes(raw_bytes[2:6], byteorder="little")
            args["entity2_id"] = int.from_bytes(raw_bytes[6:10], byteorder="little")
        elif case_type == 0x06 and len(raw_bytes) >= 6:
            # Unset ActorPointer
            args["entity_id"] = int.from_bytes(raw_bytes[2:6], byteorder="little")

        return args

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        case_type = args["case_type"]

        if case_type == 0x00:
            # Weather related
            param1_str = self.format_work_area_value(args["param1"], context=context)
            param2_str = self.format_work_area_value(args["param2"], context=context)
            return f"{self.name}(case_type=0x{case_type:02X} - Weather, param1={param1_str}, param2={param2_str})"
        elif case_type in [0x01, 0x02]:
            # Entity name color
            entity_str = self.format_entity_id(args["entity_id"], context=context)
            value_str = self.format_work_area_value(args["value"], context=context)
            return f"{self.name}(case_type=0x{case_type:02X} - Name color, entity={entity_str}, color={value_str})"
        elif case_type in [0x03, 0x04]:
            # Mou4 value
            entity_str = self.format_entity_id(args["entity_id"], context=context)
            value_str = self.format_work_area_value(args["value"], context=context)
            return f"{self.name}(case_type=0x{case_type:02X} - Mou4, entity={entity_str}, index={value_str})"
        elif case_type == 0x05:
            # ActorPointer link
            entity1_str = self.format_entity_id(args["entity1_id"], context=context)
            entity2_str = self.format_entity_id(args["entity2_id"], context=context)
            return f"{self.name}(case_type=0x{case_type:02X} - Link ActorPointer, entity1={entity1_str}, entity2={entity2_str})"
        elif case_type == 0x06:
            # Unset ActorPointer
            entity_str = self.format_entity_id(args["entity_id"], context=context)
            return f"{self.name}(case_type=0x{case_type:02X} - Unset ActorPointer, entity={entity_str})"
        elif case_type == 0x07:
            # EnvironmentAreaId
            entity_str = self.format_entity_id(args["entity1_id"], context=context)
            area_str = self.format_work_area_value(args["entity2_id"], context=context)
            return f"{self.name}(case_type=0x{case_type:02X} - Set EnvironmentAreaId, entity={entity_str}, area_id={area_str})"
        elif case_type == 0x08:
            # EnvironmentAreaId to 0
            entity_id = args["entity1_id"]
            entity_str = self.format_entity_id(entity_id, context)
            return f"{self.name}(case_type=0x{case_type:02X} - Clear EnvironmentAreaId, entity={entity_str})"
        else:
            return f"{self.name}(case_type=0x{case_type:02X})"
