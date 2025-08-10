from .base import ArgType, BaseOpcode, OpcodeArg


class VmControlOpcode(BaseOpcode):
    opcode = 0x7A
    name = "VM_CONTROL"

    def get_args(self):
        return [
            OpcodeArg("operation", ArgType.BYTE, 1, ""),
            OpcodeArg("entity_id", ArgType.DWORD, 4, ""),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on operation parameter."""
        if offset + 2 > len(data):
            return 1  # Fallback

        operation = data[offset + 1]
        if operation == 0:  # Case 0: Reset entity VM - 6 bytes total
            return 6
        elif operation == 1:  # Case 1: Reset ReqStack - 7 bytes total
            return 7
        elif operation == 2:  # Case 2: Copy/share ExtData - 6 bytes total
            return 6
        elif operation == 3:  # Case 3: Uncopy ExtData - 2 bytes total
            return 2
        elif operation == 4:  # Case 4: Make copies - 8 bytes total
            return 8
        elif operation == 5:  # Case 5: Reset state from case 4 - 6 bytes total
            return 6
        else:
            # Unknown operation - assume minimum 2 bytes
            return 2

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments based on operation mode."""
        if len(raw_bytes) < 2:
            return {}

        args = {"operation": raw_bytes[1]}
        operation = args["operation"]

        # Parse entity_id for operations that need it (0, 1, 2, 4, 5)
        if operation in [0, 2] and len(raw_bytes) >= 6:
            args["entity_id"] = int.from_bytes(raw_bytes[2:6], byteorder="little")
        elif operation == 1 and len(raw_bytes) >= 7:
            args["entity_id"] = int.from_bytes(raw_bytes[2:6], byteorder="little")
            args["tag_num"] = raw_bytes[6]
        elif operation == 4 and len(raw_bytes) >= 8:
            args["entity_id"] = int.from_bytes(raw_bytes[2:6], byteorder="little")
            args["param1"] = raw_bytes[6]
            args["param2"] = raw_bytes[7]
        elif operation == 5 and len(raw_bytes) >= 6:
            args["entity_id"] = int.from_bytes(raw_bytes[2:6], byteorder="little")

        return args

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        operation = args["operation"]

        operation_descriptions = {
            0: "Reset VM",
            1: "Reset ReqStack",
            2: "Share ExtData",
            3: "Unshare ExtData",
            4: "Copy data",
            5: "Reset copy state",
        }

        op_desc = operation_descriptions.get(operation, f"Unknown operation {operation}")

        if operation == 0:
            if "entity_id" in args:
                entity_str = self.format_entity_id(args["entity_id"], context=context)
                return f"VM_CONTROL: Reset VM for {entity_str}"
            return f"VM_CONTROL: {op_desc}"

        elif operation == 1:
            if "entity_id" in args and "tag_num" in args:
                entity_str = self.format_entity_id(args["entity_id"], context=context)
                return f"VM_CONTROL: Reset ReqStack[tag={args['tag_num']}] for {entity_str}"
            return f"VM_CONTROL: {op_desc}"

        elif operation == 2:
            if "entity_id" in args:
                entity_str = self.format_entity_id(args["entity_id"], context=context)
                return f"VM_CONTROL: Share ExtData with {entity_str}"
            return f"VM_CONTROL: {op_desc}"

        elif operation == 3:
            return "VM_CONTROL: Unshare ExtData (restore original)"

        elif operation == 4:
            if "entity_id" in args:
                entity_str = self.format_entity_id(args["entity_id"], context=context)
                param1 = args["param1"]
                param2 = args["param2"]
                return f"VM_CONTROL: Copy data from {entity_str} (params={param1}, {param2})"
            return f"VM_CONTROL: {op_desc}"

        elif operation == 5:
            if "entity_id" in args:
                entity_str = self.format_entity_id(args["entity_id"], context=context)
                return f"VM_CONTROL: Reset copy state for {entity_str}"
            return f"VM_CONTROL: {op_desc}"

        else:
            return f"VM_CONTROL(operation={operation})"
