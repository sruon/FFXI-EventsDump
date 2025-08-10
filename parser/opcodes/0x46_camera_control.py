from .base import ArgType, BaseOpcode, OpcodeArg


class CameraControlOpcode(BaseOpcode):

    opcode = 0x46
    name = "CAMERA_CONTROL"

    def get_args(self):
        return [
            OpcodeArg(
                "mode",
                ArgType.BYTE,
                1,
                "Camera mode (0=restore default, 1=disable control, 2=query status)",
            ),
        ]

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        mode = args["mode"]
        if mode == 0:
            return "CAMERA_CONTROL: Restore default settings"
        elif mode == 1:
            return "CAMERA_CONTROL: Disable user control"
        elif mode == 2:
            return "CAMERA_CONTROL: Query status"
        else:
            return f"CAMERA_CONTROL: Unknown mode {mode:#02x}"
