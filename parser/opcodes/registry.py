"""
Opcode Registry - Central registry for all FFXI event opcodes.

This module handles loading and managing all opcode implementations.
"""

import importlib
from pathlib import Path

from .base import BaseOpcode


class OpcodeRegistry:
    """Central registry for all opcode implementations."""

    def __init__(self):
        self._opcodes: dict[int, BaseOpcode] = {}
        self._load_all_opcodes()

    def _load_all_opcodes(self):
        """Automatically load all opcode implementations from the opcodes directory."""
        opcodes_dir = Path(__file__).parent

        # Find all 0xXX_*.py files
        for file_path in opcodes_dir.glob("0x*.py"):
            filename = file_path.name
            try:
                # Import the module
                module_name = filename[:-3]  # Remove .py extension
                module = importlib.import_module(f".{module_name}", package=__package__)

                # Find the opcode class in the module
                opcode_class = self._find_opcode_class(module)
                if opcode_class:
                    opcode_instance = opcode_class()
                    # Use the opcode value from the class itself, not the filename
                    self._opcodes[opcode_instance.opcode] = opcode_instance

            except (ImportError, AttributeError) as e:
                print(f"Failed to load opcode from {filename}: {e}")
                continue

    def _find_opcode_class(self, module) -> type[BaseOpcode] | None:
        """Find the BaseOpcode subclass in a module."""
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            # Skip base classes and only get concrete implementations
            if (
                isinstance(attr, type)
                and issubclass(attr, BaseOpcode)
                and attr != BaseOpcode
                and hasattr(attr, "opcode")
                and attr.opcode is not None
            ):
                return attr
        return None

    def get_opcode(self, opcode_value: int) -> BaseOpcode | None:
        """Get an opcode implementation by its value."""
        return self._opcodes.get(opcode_value)

    def has_opcode(self, opcode_value: int) -> bool:
        """Check if an opcode is registered."""
        return opcode_value in self._opcodes

    def get_all_opcodes(self) -> dict[int, BaseOpcode]:
        """Get all registered opcodes."""
        return self._opcodes.copy()

    def register_opcode(self, opcode: BaseOpcode):
        """Manually register an opcode (for testing or custom opcodes)."""
        self._opcodes[opcode.opcode] = opcode


# Global registry instance
_registry = None


def get_opcode_registry() -> OpcodeRegistry:
    """Get the global opcode registry instance."""
    global _registry
    if _registry is None:
        _registry = OpcodeRegistry()
    return _registry
