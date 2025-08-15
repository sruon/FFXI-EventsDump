from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Any, NamedTuple, Optional


@dataclass
class OpcodeContext:
    """Context object that bundles all shared data for opcode processing."""

    imed_data: list | None = None
    zone_entities: object | None = None  # ZoneEntities object
    zone_strings: object | None = None  # ParsedStringDat object

    def __post_init__(self):
        # Ensure we have empty lists instead of None for safety
        if self.imed_data is None:
            self.imed_data = []


def decode_work_area_address(value: int, imed_data: list = None) -> str:
    """
    Decode a work area address value into a human-readable representation.

    Based on XiEvent::getworkofs function documentation.

    Args:
        value: The work area address value
        imed_data: Optional immediate data array for resolving reference values

    Returns:
        A human-readable string representation of the work area address
    """
    if 0x8000 <= value <= 0x8FFF:
        # val is considered a References entry index and returns: this->References[4 * (val & 0x7FFF)]
        ref_index = value & 0x7FFF  # This gives us 0-4095 range
        if imed_data and ref_index < len(imed_data):
            actual_value = imed_data[ref_index]
            return f"{actual_value}*"
        else:
            return f"References[{ref_index}]"
    elif value < 2048:
        if value >= 80:
            # val is considered invalid, 0 is returned
            return f"Invalid[{value:04X}]"
        else:
            # val is considered a WorkLocal index and returns: this->ExtData[1]->WorkLocal[val]
            return f"ExtData[1]->WorkLocal[{value}]"
    elif value < 4352:
        zone_index = value - 4096
        if 0 <= zone_index < 96:
            # val is considered a Work_Zone index and returns: Work_Zone[val - 4096]
            return f"Work_Zone[{zone_index}]"
        else:
            # val is considered invalid, 0 is returned
            return f"Invalid[{value:04X}]"
    elif value < 4608:
        mem_index = value - 4352
        if 0 <= mem_index < 96:
            # val is considered a Work_Zone_Memorize index and returns: Work_Zone[val - 4352]
            return f"Work_Zone_Memorize[{mem_index}]"
        else:
            # val is considered invalid, 0 is returned
            return f"Invalid[{value:04X}]"
    elif value < 6144:
        zone1700_index = value - 5888
        if 0 <= zone1700_index < 96:
            # val is considered a Work_Zone_1700 index and returns: Work_Zone_1700[val - 5888]
            return f"Work_Zone_1700[{zone1700_index}]"
        else:
            # val is considered invalid, 0 is returned
            return f"Invalid[{value:04X}]"
    elif value < 32640:
        # Handled as a switch case of val if this if is true - EntityTargetIndex[1] entity data
        entity_cases = {
            0x7F00: "ExtData[1]->EventPos[0] * 1000.0",
            0x7F01: "ExtData[1]->EventPos[1] * 1000.0",
            0x7F02: "ExtData[1]->EventPos[2] * 1000.0",
            0x7F03: "enDirCli(ExtData[1]->EventDir[1]) * 4096.0 * 0.15915963",
            0x7F06: "Entity->JobId (if LocalPlayer)",
            0x7F07: "Entity->Race",
            0x7F08: "Entity->JobLevel (if LocalPlayer)",
            0x7F0A: "Entity->ServerId",
            0x7F0B: "(Entity->Render.Flags01 >> 25) & 1",
        }
        # If it's a known entity case, return that, otherwise just return as hex
        if value in entity_cases:
            return entity_cases[value]
        else:
            # Unknown value in this range - just return as hex
            return f"0x{value:04X}"
    elif 0x9000 <= value <= 0xFFFF:
        # Values above reference range - just return as hex
        return f"0x{value:04X}"
    elif value >= 0x7FFF:
        # val is invalid, return is 0
        return f"Invalid[{value:04X}]"
    else:
        # Handled as a switch case of val for player entity data (0x7F80-0x7F8B)
        player_cases = {
            0x7F80: "LocalPlayer->LocalPosition.LocalX * 1000.0",
            0x7F81: "LocalPlayer->LocalPosition.LocalZ * 1000.0",
            0x7F82: "LocalPlayer->LocalPosition.LocalY * 1000.0",
            0x7F83: "enDirCli(LocalPlayer->LocalPosition.Unknown0000) * 4096.0 * 0.15915963",
            0x7F86: "LocalPlayer->JobId",
            0x7F87: "LocalPlayer->Race",
            0x7F88: "LocalPlayer->JobLevel",
            0x7F8A: "LocalPlayer->ServerId",
            0x7F8B: "(LocalPlayer->Render.Flags01 >> 25) & 1",
        }
        return player_cases.get(value, "0")


def decode_entity_id(entity_id: int) -> str:
    """
    Decode entity ID values into human-readable representations.

    Based on XiEvent::GetActorIndex function documentation.

    Args:
        entity_id: The entity ID value

    Returns:
        A human-readable string representation of the entity ID
    """
    if entity_id == 0x7FFFFFC0 or entity_id == 0x7FFFFFF0:
        return "LocalPlayer"
    elif 0x7FFFFFC1 <= entity_id <= 0x7FFFFFC5:
        party_member = entity_id - 0x7FFFFFC0  # 1-5
        return f"PartyMember{party_member}"
    elif 0x7FFFFFC6 <= entity_id <= 0x7FFFFFCB:
        alliance_member = entity_id - 0x7FFFFFC5  # 1-6
        return f"AllianceMember{alliance_member}"
    elif 0x7FFFFFCC <= entity_id <= 0x7FFFFFD1:
        alliance_member = entity_id - 0x7FFFFFCB + 6  # 7-12
        return f"AllianceMember{alliance_member}"
    elif 0x7FFFFFF1 <= entity_id <= 0x7FFFFFF5:
        party_ref = entity_id - 0x7FFFFFF0  # 1-5
        return f"PartyRef{party_ref}"
    elif entity_id == 0x7FFFFFF8:
        return "EventEntity"
    elif entity_id == 0x7FFFFFF9:
        return "LocalPlayer"
    else:
        return f"0x{entity_id:08X}"


class ArgType(Enum):
    """Argument types for opcodes."""

    BYTE = "byte"
    WORD = "word"
    DWORD = "dword"
    STRING = "string"  # Fixed-size string (size specified in OpcodeArg)
    ENTITY_ID = "entity_id"
    MESSAGE_ID = "message_id"
    TASK_ID = "task_id"
    UNKNOWN = "unknown"


class OpcodeArg:
    """Definition of an opcode argument."""

    def __init__(self, name: str, arg_type: ArgType, size: int, description: str = ""):
        self.name = name
        self.arg_type = arg_type
        self.size = size
        self.description = description

    def __repr__(self):
        return f"OpcodeArg(name='{self.name}', type={self.arg_type}, size={self.size})"


class BaseOpcode(ABC):
    """Base class for all FFXI event opcodes."""

    def __init__(self):
        # Use class attributes if available
        self._opcode = self.opcode if hasattr(self, "opcode") else None
        self._name = self.name if hasattr(self, "name") else None
        self._args = self.get_args() if hasattr(self, "get_args") else []

    def get_args(self) -> list[OpcodeArg]:
        """Return the list of arguments this opcode takes."""
        return []

    def calculate_length(self, data: bytes, offset: int) -> int:
        """
        Calculate the length of this opcode instruction in bytes.

        For most opcodes, this is 1 (opcode) + sum of argument sizes.
        Variable-length opcodes should override this method.

        Args:
            data: The full event data bytes
            offset: The offset where this opcode starts

        Returns:
            The total length of this instruction in bytes
        """
        if not self._args:
            return 1  # Just the opcode byte

        return 1 + sum(arg.size for arg in self._args)

    def parse_args(self, raw_bytes: bytes) -> dict[str, Any]:
        """
        Parse raw argument bytes according to opcode definition.

        Args:
            raw_bytes: The raw instruction bytes including opcode

        Returns:
            Dictionary mapping argument names to their parsed values
        """
        if not self._args or len(raw_bytes) <= 1:
            return {}

        args = {}
        offset = 1  # Skip opcode byte

        for arg_def in self._args:
            if offset + arg_def.size > len(raw_bytes):
                break

            raw_value = raw_bytes[offset : offset + arg_def.size]

            if arg_def.arg_type == ArgType.STRING:
                value = raw_value
            elif arg_def.size == 1:
                value = raw_value[0]
            elif arg_def.size == 2:
                value = int.from_bytes(raw_value, "little")
            elif arg_def.size == 4:
                value = int.from_bytes(raw_value, "little")
            else:
                value = raw_value

            args[arg_def.name] = value
            offset += arg_def.size

        return args

    def convert_coordinate_to_float(self, value: int) -> float:
        """
        Convert FFXI coordinate value to float using standard scaling.
        Per upstream documentation, coordinates use * 0.001 scaling.

        Args:
            value: Raw coordinate value (as unsigned int)

        Returns:
            Float coordinate value
        """
        import struct

        # Check if this is a negative value (sign bit set in 32-bit unsigned)
        if value > 0x7FFFFFFF:  # If greater than max signed 32-bit int
            # Convert to signed 32-bit integer
            signed_value = struct.unpack("<i", struct.pack("<I", value))[0]
        else:
            signed_value = value

        # FFXI coordinates use * 0.001 scaling per upstream documentation
        return signed_value * 0.001

    def convert_direction_to_degrees(self, value: int) -> float:
        """
        Convert FFXI direction value to degrees.
        Per upstream documentation: * 6.283 * 0.00024414062 converts to radians.

        Args:
            value: Raw direction value

        Returns:
            Direction in degrees
        """
        # Convert to radians using the documented formula
        radians = value * 6.283 * 0.00024414062
        # Convert radians to degrees for display
        degrees = radians * (180.0 / 3.14159265359)
        return degrees

    def format_entity_id(self, entity_id: int, arg_name: str = None, context: "OpcodeContext" = None) -> str:
        """
        Format an entity ID value.

        Args:
            entity_id: The entity ID to format
            arg_name: Optional argument name for context
            context: Context object containing zone_entities

        Returns:
            Formatted string representation
        """
        if context is None:
            context = OpcodeContext()

        # Special entity IDs first
        if entity_id == 0x7FFFFFF0:
            return "LocalPlayer"
        elif entity_id == 0x7FFFFFF8:
            return "EventEntity"

        # Try to get entity name if available
        if context.zone_entities:
            return context.zone_entities.get_entity_display_name(entity_id)

        # Fall back to standard decoding
        decoded = decode_entity_id(entity_id)
        if decoded.startswith("0x"):
            return f"{entity_id}/0x{entity_id:08X}"  # Both decimal and hex
        else:
            return f"{decoded} ({entity_id}/0x{entity_id:08X})"

    def resolve_reference_value(self, value: int, context: "OpcodeContext" = None) -> tuple[int, bool]:
        """
        Resolve a reference value if it's in the 0x8000-0x8FFF range.

        Args:
            value: The value to check and potentially resolve
            context: Context object containing imed_data

        Returns:
            Tuple of (resolved_value, was_reference)
            If not a reference or can't be resolved, returns (value, False)
        """
        if context is None:
            context = OpcodeContext()

        if 0x8000 <= value <= 0x8FFF:
            ref_index = value & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                return (context.imed_data[ref_index], True)
            # Reference but can't resolve
            return (value, False)
        # Not a reference
        return (value, False)

    def format_string_value(self, value: bytes, replace_underscores: bool = False) -> str:
        """
        Format a bytes value as a string for display.

        Args:
            value: The bytes value to format
            replace_underscores: Whether to replace underscores with spaces

        Returns:
            Formatted string representation
        """
        if not value or value == b"\x00" * len(value):
            return '""'

        try:
            # Try to decode as ASCII, strip null bytes
            ascii_str = value.rstrip(b"\x00").decode("ascii")
            if replace_underscores:
                ascii_str = ascii_str.replace("_", " ")
            # Check if it's printable
            if ascii_str and all(32 <= ord(c) <= 126 or c == " " for c in ascii_str):
                return f'"{ascii_str}"'
            else:
                return f"0x{value.hex()}"
        except (UnicodeDecodeError, ValueError):
            return f"0x{value.hex()}"

    def format_work_area_value(self, value: int, arg_name: str = None, context: "OpcodeContext" = None) -> str:
        """
        Format a value that might be a work area address.

        Args:
            value: The value to format
            arg_name: Optional argument name for context
            context: Context object containing imed_data

        Returns:
            Formatted string representation
        """
        if context is None:
            context = OpcodeContext()
        # This method is specifically for work area values, so DO the work area detection
        work_desc = decode_work_area_address(value, context.imed_data)

        # If it's a reference that resolved to a value, it already has the * marker
        if "*" in work_desc:
            return work_desc
        # If it's a valid work area description, just return the description without hex
        elif not work_desc.startswith("Invalid[") and not work_desc.startswith("0x"):
            return work_desc
        else:
            # Fall back to hex formatting
            if value < 256:
                return f"0x{value:02X}"
            elif value < 65536:
                return f"0x{value:04X}"
            else:
                return f"0x{value:08X}"

    def format_coordinate_value(self, value: int, context: "OpcodeContext" = None) -> str:
        """
        Format a coordinate value, handling references and converting to float.

        Args:
            value: The raw coordinate value (WORD)
            context: Context object containing imed_data

        Returns:
            Formatted coordinate string with float conversion
        """
        if context is None:
            context = OpcodeContext()

        # Check if this is a reference (0x8000-0x8FFF range)
        if 0x8000 <= value <= 0x8FFF:
            ref_index = value & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                actual_value = context.imed_data[ref_index]
                # Convert to float using the standard method
                float_value = self.convert_coordinate_to_float(actual_value)
                return f"{float_value:.3f}*"
            else:
                return f"References[{ref_index}]"
        else:
            # Direct work area value - use standard formatting
            work_desc = decode_work_area_address(value, context.imed_data)
            # If it's a valid work area description, return it
            if not work_desc.startswith("Invalid[") and not work_desc.startswith("0x"):
                return work_desc
            else:
                # Not a work area value, might be a small immediate coordinate
                # Values under 0x8000 are typically work area references, not coordinates
                return f"0x{value:04X}"

    def format_direction_value(self, value: int, context: "OpcodeContext" = None) -> str:
        """
        Format a direction value, handling references and converting to degrees.

        Args:
            value: The raw direction value (WORD)
            context: Context object containing imed_data

        Returns:
            Formatted direction string in degrees
        """
        if context is None:
            context = OpcodeContext()

        # Check if this is a reference (0x8000-0x8FFF range)
        if 0x8000 <= value <= 0x8FFF:
            ref_index = value & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                actual_value = context.imed_data[ref_index]
                # Convert to degrees using the standard method
                degrees = self.convert_direction_to_degrees(actual_value)
                return f"{degrees:.1f}°*"
            else:
                return f"References[{ref_index}]"
        else:
            # Direct work area value - use standard formatting
            work_desc = decode_work_area_address(value, context.imed_data)
            # If it's a valid work area description, return it
            if not work_desc.startswith("Invalid[") and not work_desc.startswith("0x"):
                return work_desc
            else:
                # Not a work area value, might be a small immediate direction
                return f"0x{value:04X}"

    def format_yaw_value(self, value: int, context: "OpcodeContext" = None) -> str:
        """
        Format a yaw value using simpler scaling (/ 65536.0 * 360.0).
        Used by some opcodes like UPDATE_PLAYER_LOCATION.

        Args:
            value: The raw yaw value (WORD)
            context: Context object containing imed_data

        Returns:
            Formatted yaw string in degrees
        """
        if context is None:
            context = OpcodeContext()

        # Check if this is a reference (0x8000-0x8FFF range)
        if 0x8000 <= value <= 0x8FFF:
            ref_index = value & 0x7FFF
            if context.imed_data and ref_index < len(context.imed_data):
                actual_value = context.imed_data[ref_index]
                # Yaw uses simple scaling: / 65536.0 * 360.0
                degrees = (actual_value / 65536.0) * 360.0
                return f"{degrees:.1f}°*"
            else:
                return f"References[{ref_index}]"
        else:
            # Direct work area value - use standard formatting
            work_desc = decode_work_area_address(value, context.imed_data)
            # If it's a valid work area description, return it
            if not work_desc.startswith("Invalid[") and not work_desc.startswith("0x"):
                return work_desc
            else:
                # Not a work area value, might be a small immediate yaw
                return f"0x{value:04X}"

    def escape_unprintable_chars(self, text: str) -> str:
        """
        Escape unprintable characters in a string using \\u0000 format.

        Args:
            text: The input text string

        Returns:
            String with unprintable characters escaped as \\u0000 format
        """
        if not text:
            return text

        result = []
        for char in text:
            # Check if character is printable (ASCII 32-126) or common whitespace
            if ord(char) >= 32 and ord(char) <= 126:
                result.append(char)
            elif char in ("\n", "\t", "\r"):
                # Keep common whitespace characters as-is
                result.append(char)
            else:
                # Escape as \u0000 format
                result.append(f"\\u{ord(char):04X}")

        return "".join(result)

    def _is_entity_value(self, name: str, value: int) -> bool:
        """Check if a parameter is likely an entity ID."""
        name_lower = name.lower()
        return (
            "entity" in name_lower
            or "actor" in name_lower
            or name_lower.endswith("_id")
            or (0x7FFFFFC0 <= value <= 0x7FFFFFFA)  # Special entity IDs
            or (0x01000000 <= value <= 0x01FFFFFF)  # Regular entity IDs
        )

    def _is_special_entity(self, decoded: str) -> bool:
        """Check if an entity should not show its ID."""
        return (
            decoded in ["EventEntity", "LocalPlayer"]
            or decoded.startswith("PartyMember")
            or decoded.startswith("AllianceMember")
            or decoded.startswith("PartyRef")
        )

    def get_legible_representation(self, raw_bytes: bytes, args: dict[str, Any] = None, context: OpcodeContext = None) -> str:
        """
        Return a human-readable representation of this opcode instruction.

        This method can be overridden to provide custom formatting for specific opcodes.

        Args:
            raw_bytes: The raw instruction bytes
            args: Parsed arguments (will be calculated if not provided)
            context: Context object containing imed_data, zone_entities, zone_strings

        Returns:
            A legible string representation of the instruction
        """
        if args is None:
            args = self.parse_args(raw_bytes)

        if args:
            formatted_args = []
            for arg_def in self._args:
                name = arg_def.name
                if name not in args:
                    continue

                value = args[name]

                # Auto-detect entity IDs based on name patterns or value ranges
                if isinstance(value, int) and self._is_entity_value(name, value):
                    decoded = decode_entity_id(value)
                    if not decoded.startswith("0x"):
                        if self._is_special_entity(decoded):
                            formatted_args.append(f"{name}={decoded}")
                        else:
                            formatted_args.append(f"{name}={decoded} (0x{value:08X})")
                    else:
                        formatted_args.append(f"{name}={decoded}")
                elif isinstance(value, int):
                    # Default formatting for other integers
                    if value < 256:
                        formatted_args.append(f"{name}=0x{value:02X}")
                    elif value < 65536:
                        formatted_args.append(f"{name}=0x{value:04X}")
                    else:
                        formatted_args.append(f"{name}=0x{value:08X}")
                elif isinstance(value, bytes):
                    formatted_args.append(f"{name}={value.hex()}")
                else:
                    formatted_args.append(f"{name}={value}")

            return f"{self._name}({', '.join(formatted_args)})"
        else:
            return f"{self._name}()"

    def __str__(self) -> str:
        return f"<Opcode 0x{self._opcode:02X} {self._name}>"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(0x{self._opcode:02X})>"

    def get_jump_targets(self, args: dict, context=None) -> list[int]:
        return []

    def is_terminal(self) -> bool:
        return False


class EventInstruction:
    """Represents a single parsed event instruction."""

    def __init__(self, opcode_value: int, raw_bytes: bytes, opcode_impl: BaseOpcode | None = None):
        self.opcode = opcode_value
        self.raw_bytes = raw_bytes
        self.opcode_impl = opcode_impl
        self.args = opcode_impl.parse_args(raw_bytes) if opcode_impl else {}

    @property
    def definition(self) -> Optional["OpcodeDefinition"]:
        """Legacy compatibility - return None if no opcode implementation."""
        return None if not self.opcode_impl else self

    @property
    def name(self) -> str:
        """Get the opcode name."""
        return self.opcode_impl.get_name() if self.opcode_impl else f"UNKNOWN_0x{self.opcode:02X}"

    def get_legible_representation(self, context: OpcodeContext = None) -> str:
        """Get a human-readable representation of this instruction."""
        if context is None:
            context = OpcodeContext()

        if self.opcode_impl:
            return self.opcode_impl.get_legible_representation(self.raw_bytes, self.args, context)
        else:
            hex_args = " ".join(f"{b:02X}" for b in self.raw_bytes[1:])
            return f"OPCODE_0x{self.opcode:02X}({hex_args})" if len(self.raw_bytes) > 1 else f"OPCODE_0x{self.opcode:02X}()"

    def __str__(self) -> str:
        return self.get_legible_representation()
