from pathlib import Path

import construct

from models.events import EventDat, ParsedEventDat


class EventDatParser:
    @staticmethod
    def parse_file(file_path: str | Path) -> ParsedEventDat:
        try:
            with open(file_path, "rb") as f:
                data = f.read()
            return EventDatParser.parse_bytes(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Event DAT file not found: {file_path}") from None
        except Exception as e:
            raise ValueError(f"Error parsing event DAT file {file_path}: {e}") from e

    @staticmethod
    def parse_bytes(data: bytes) -> ParsedEventDat:
        try:
            parsed = EventDat.parse(data)
            return ParsedEventDat.from_construct(parsed)
        except construct.ConstructError as e:
            raise ValueError(f"Invalid event DAT format: {e}") from e
