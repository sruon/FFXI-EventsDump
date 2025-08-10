from .base import ArgType, BaseOpcode, OpcodeArg


class ChocoboRacingParameterGetterOpcode(BaseOpcode):
    opcode = 0xBF
    name = "CHOCOBO_RACING_PARAMETER_GETTER"

    def get_args(self):
        return [
            OpcodeArg("param_type", ArgType.BYTE, 1, ""),
        ]
