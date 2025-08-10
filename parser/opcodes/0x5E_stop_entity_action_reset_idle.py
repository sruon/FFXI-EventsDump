from .base import ArgType, BaseOpcode, OpcodeArg


class StopEntityActionResetIdleOpcode(BaseOpcode):

    opcode = 0x5E
    name = "STOP_ENTITY_ACTION_RESET_IDLE"

    def get_args(self):
        return [
            OpcodeArg("animation_id", ArgType.DWORD, 4, "Animation ID to stop/reset"),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        animation_id = args["animation_id"]

        try:
            ascii_bytes = []
            temp = animation_id
            for _ in range(4):
                ascii_bytes.append(temp & 0xFF)
                temp >>= 8

            ascii_str = bytes(ascii_bytes).decode("ascii", errors="ignore").rstrip("\x00")
            if ascii_str.isprintable() and len(ascii_str.strip()) > 0:
                return f'EventEntity goes idle (kills current action) (animation: "{ascii_str}")'
        except Exception:
            pass

        return f"EventEntity goes idle (kills current action) (animation: 0x{animation_id:08X})"
