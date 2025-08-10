"""
https://github.com/atom0s/XiEvents/blob/main/Event%20DAT%20Files.md
"""

from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, Self

import yaml

from parser.stringdat import StringDatParser


@dataclass
class ZoneFiles:
    entities: str
    events: str
    strings_na: str
    strings_jp: str


@dataclass
class Zone:
    id: int
    name: str
    files: ZoneFiles

    _zones: ClassVar[dict[int, list[Self]]] = {}
    _zones_by_name: ClassVar[dict[str, Self]] = {}
    _loaded: ClassVar[bool] = False

    @classmethod
    def load_zones(cls) -> None:
        """Load all zones from YAML file."""
        if cls._loaded:
            return

        with open("data/zones.yaml", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        cls._zones.clear()
        cls._zones_by_name.clear()

        for zone_data in data["zones"]:
            zone_files = ZoneFiles(
                entities=zone_data["files"]["entities"],
                events=zone_data["files"]["events"],
                strings_na=zone_data["files"]["strings_na"],
                strings_jp=zone_data["files"]["strings_jp"],
            )

            zone = Zone(id=zone_data["id"], name=zone_data["name"], files=zone_files)

            # Handle multiple zones with the same ID
            if zone.id not in cls._zones:
                cls._zones[zone.id] = []
            cls._zones[zone.id].append(zone)

            if zone.name:
                cls._zones_by_name[zone.name.lower()] = zone

        cls._loaded = True

    @classmethod
    def get_all(cls) -> list[Self]:
        cls.load_zones()
        # Flatten the list of lists
        all_zones = []
        for zone_list in cls._zones.values():
            all_zones.extend(zone_list)
        return all_zones

    @classmethod
    def get_by_id(cls, zone_id: int) -> list[Self]:
        cls.load_zones()
        return cls._zones.get(zone_id, [])

    @classmethod
    def get_by_name(cls, zone_name: str) -> Self:
        cls.load_zones()
        return cls._zones_by_name.get(zone_name)

    def get_strings_na(self, ffxi_path: str = None):
        if ffxi_path is None:
            ffxi_path = "C:\\Program Files (x86)\\PlayOnline\\SquareEnix\\FINAL FANTASY XI\\"

        string_file_path = Path(ffxi_path) / self.files.strings_na
        return StringDatParser.parse_file_english(string_file_path)

    def get_strings_jp(self, ffxi_path: str = None):
        if ffxi_path is None:
            ffxi_path = "C:\\Program Files (x86)\\PlayOnline\\SquareEnix\\FINAL FANTASY XI\\"

        string_file_path = Path(ffxi_path) / self.files.strings_jp
        return StringDatParser.parse_file_japanese(string_file_path)
