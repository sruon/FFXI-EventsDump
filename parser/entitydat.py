"""
Parser for FFXI entity DAT files.
Based on Windower's MobListEntry format.
"""

from pathlib import Path

import construct
from construct import Adapter, Bytes, GreedyRange, Int32ul, Struct

from models.entities import Entity, ZoneEntities


# FFXI string adapter for decoding
class FFXIStringAdapter(Adapter):
    def _decode(self, data, context, path):
        """Decode FFXI string (simplified - mostly ASCII)."""
        # Find null terminator
        null_pos = data.find(b"\x00")
        if null_pos != -1:
            data = data[:null_pos]

        # Basic decode as latin-1 (preserves all byte values)
        try:
            return data.decode("latin-1").strip()
        except Exception:
            return data.decode("latin-1", errors="replace").strip()

    def _encode(self, data, context, path):
        """Encode string to FFXI format."""
        if isinstance(data, str):
            encoded = data.encode("latin-1", errors="replace")
        else:
            encoded = data
        # Pad to required length with null bytes
        return encoded.ljust(0x1C, b"\x00")[:0x1C]


# Entity entry structure
EntityEntry = Struct(
    "name" / FFXIStringAdapter(Bytes(0x1C)),  # 28 bytes for name
    "entity_id" / Int32ul,  # 4 bytes for entity ID
)

# Full entity DAT structure
EntityDat = GreedyRange(EntityEntry)


class EntityDatParser:
    """Parser for FFXI zone entity DAT files using construct."""

    @staticmethod
    def parse_file(file_path: str | Path, zone_id: int = 0, zone_name: str = "") -> ZoneEntities:
        """Parse an entity DAT file and return ZoneEntities."""
        try:
            with open(file_path, "rb") as f:
                data = f.read()
            return EntityDatParser.parse_bytes(data, zone_id, zone_name)
        except FileNotFoundError:
            raise FileNotFoundError(f"Entity DAT file not found: {file_path}") from None
        except Exception as e:
            raise ValueError(f"Error parsing entity DAT file {file_path}: {e}") from e

    @staticmethod
    def parse_bytes(data: bytes, zone_id: int = 0, zone_name: str = "") -> ZoneEntities:
        """Parse entity DAT bytes and return ZoneEntities."""
        try:
            parsed_entries = EntityDat.parse(data)
            entities = []

            for entry in parsed_entries:
                # Skip empty/invalid entries
                if entry.entity_id == 0:
                    continue

                # Validate entity ID format (from the C# code)
                if not EntityDatParser._is_valid_entity_id(entry.entity_id):
                    continue

                # Clean up name
                name = entry.name.strip() if entry.name else None
                if not name:
                    name = None

                entity = Entity(entity_id=entry.entity_id, name=name)
                entities.append(entity)

            return ZoneEntities(zone_id=zone_id, zone_name=zone_name, entities=entities)

        except construct.ConstructError as e:
            raise ValueError(f"Invalid entity DAT format: {e}") from e

    @staticmethod
    def _is_valid_entity_id(entity_id: int) -> bool:
        """Validate entity ID format based on Windower logic."""
        if entity_id == 0:
            return False

        # Check for valid prefixes: 0x010, 0x013, 0x011
        prefix = entity_id & 0xFFF00000
        return prefix in [0x01000000, 0x01300000, 0x01100000]
