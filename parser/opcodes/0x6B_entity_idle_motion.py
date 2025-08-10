from .base import ArgType, BaseOpcode, OpcodeArg


class EntityIdleMotionOpcode(BaseOpcode):

    opcode = 0x6B
    name = "ENTITY_IDLE_MOTION"

    def get_args(self):
        return [
            OpcodeArg("animation_id", ArgType.DWORD, 4, "Animation ID to set"),
            OpcodeArg("entity_id", ArgType.DWORD, 4, "Entity to reset to idle"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args: dict = None, context=None) -> str:
        animation_id = args["animation_id"]
        entity_id = args["entity_id"]

        entity_str = self.format_entity_id(entity_id, context=context)
        animation_str = None
        try:
            # Convert DWORD to 4 bytes and try to decode as ASCII
            ascii_bytes = []
            temp = animation_id
            for _ in range(4):
                ascii_bytes.append(temp & 0xFF)
                temp >>= 8

            # Try to decode as ASCII string
            ascii_str = bytes(ascii_bytes).decode("ascii", errors="ignore").rstrip("\x00")
            if ascii_str.isprintable() and len(ascii_str.strip()) > 0:
                animation_str = f'"{ascii_str}"'
        except Exception:
            pass

        # Fallback to hex representation if not a valid string
        if not animation_str:
            animation_str = f"0x{animation_id:08X}"

        return f"STOP_AND_IDLE: {entity_str} stops current action and resets to idle (animation={animation_str})"
