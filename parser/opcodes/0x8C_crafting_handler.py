from .base import ArgType, BaseOpcode, OpcodeArg


class CraftingHandlerOpcode(BaseOpcode):

    opcode = 0x8C
    name = "CRAFTING_HANDLER"

    def get_args(self):
        # Base argument - additional arguments parsed dynamically
        return [
            OpcodeArg("mode", ArgType.BYTE, 1, "Crafting handler mode"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on mode."""
        if offset + 1 >= len(data):
            return 2  # Default if we can't read mode

        mode = data[offset + 1]

        # Based on upstream pseudocode
        if mode == 0:
            return 8  # Mode 0: 8 bytes
        elif mode == 1:
            return 2  # Mode 1: 2 bytes
        elif mode == 2:
            return 12  # Mode 2: 12 bytes
        elif mode == 3:
            return 10  # Mode 3: 10 bytes
        elif mode == 4:
            return 10  # Mode 4: 10 bytes
        elif mode == 5:
            return 14  # Mode 5: 14 bytes
        else:
            return 2  # Unknown mode - default to minimum

    def parse_args(self, raw_bytes: bytes) -> dict:
        """Parse arguments based on mode."""
        if len(raw_bytes) < 2:
            return {"mode": 0}

        mode = raw_bytes[1]
        result = {"mode": mode}

        # Parse additional arguments based on mode
        if mode == 0 and len(raw_bytes) >= 8:
            # Mode 0: 8 bytes total - Additional data for mode 0
            result["data"] = raw_bytes[2:8]
        elif mode == 2 and len(raw_bytes) >= 12:
            # Mode 2: 12 bytes total - Additional data for mode 2
            result["data"] = raw_bytes[2:12]
        elif mode == 3 and len(raw_bytes) >= 10:
            # Mode 3: 10 bytes total - Additional data for mode 3
            result["data"] = raw_bytes[2:10]
        elif mode == 4 and len(raw_bytes) >= 10:
            # Mode 4: 10 bytes total - Additional data for mode 4
            result["data"] = raw_bytes[2:10]
        elif mode == 5 and len(raw_bytes) >= 14:
            # Mode 5: 14 bytes total - Additional data for mode 5
            result["data"] = raw_bytes[2:14]

        return result

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        mode = args["mode"]

        mode_names = {
            0: "Initialize crafting session",
            1: "End crafting session",
            2: "Set recipe data",
            3: "Get synthesis recipe",
            4: "Get crystal recipe",
            5: "Set extended recipe data",
        }

        mode_desc = mode_names.get(mode, f"Unknown mode {mode}")

        return f"{self.name}(mode=0x{mode:02X}) // {mode_desc}"
