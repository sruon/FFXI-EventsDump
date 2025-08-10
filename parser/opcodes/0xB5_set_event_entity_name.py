from .base import ArgType, BaseOpcode, OpcodeArg


class SetEventEntityNameOpcode(BaseOpcode):
    opcode = 0xB5
    name = "SET_EVENT_ENTITY_NAME"

    def get_args(self):
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, ""),
            OpcodeArg("name_string", ArgType.WORD, 2, ""),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        # mode = args["mode"]  # Not used currently
        name_value = args["name_string"]

        # Format the name value using standard work area resolution
        name_str = self.format_work_area_value(name_value, context=context)

        # If it's a resolved reference (has asterisk), try to interpret the number as string
        if name_str.endswith("*") and name_str[:-1].isdigit():
            ref_val = int(name_str[:-1])
            # Try to convert the integer to a 4-byte string
            try:
                import struct

                # Pack as little-endian 32-bit int, then decode as ASCII
                bytes_val = struct.pack("<I", ref_val)
                # Filter out null bytes and non-printable chars
                string_val = "".join(chr(b) for b in bytes_val if 32 <= b < 127)
                if string_val:
                    name_str = f'"{string_val}"*'
            except Exception:
                pass  # Keep the numeric format

        return f"SET_EVENT_ENTITY_NAME: Change EventEntity name to {name_str}"
