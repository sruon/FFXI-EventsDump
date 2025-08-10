"""
FFXI Event Opcodes Package

This package contains all FFXI event opcode implementations organized
by opcode value. Each opcode is implemented as a separate class inheriting
from BaseOpcode.

Usage:
    from parser.opcodes import get_opcode_registry

    registry = get_opcode_registry()
    opcode_impl = registry.get_opcode(0x01)  # Get GOTO opcode
"""

from .base import ArgType, BaseOpcode, EventInstruction, OpcodeArg
from .registry import OpcodeRegistry, get_opcode_registry

__all__ = [
    "BaseOpcode",
    "OpcodeArg",
    "ArgType",
    "EventInstruction",
    "OpcodeRegistry",
    "get_opcode_registry",
]
