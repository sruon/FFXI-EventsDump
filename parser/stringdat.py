from pathlib import Path

from models.strings import ParsedStringDat


class StringDatParser:
    @staticmethod
    def parse_file(file_path: str | Path, encoding: str = "utf-8") -> ParsedStringDat:
        """Parse an FFXI Dialog Table file from disk."""
        try:
            with open(file_path, "rb") as f:
                data = f.read()
            return StringDatParser.parse_bytes(data, encoding)
        except FileNotFoundError:
            raise FileNotFoundError(f"Dialog Table file not found: {file_path}") from None
        except Exception as e:
            raise ValueError(f"Error parsing Dialog Table file {file_path}: {e}") from e

    @staticmethod
    def parse_bytes(data: bytes, encoding: str = "utf-8") -> ParsedStringDat:
        """Parse FFXI Dialog Table data from bytes."""
        try:
            return ParsedStringDat.from_raw_data(data, encoding)
        except Exception as e:
            raise ValueError(f"Invalid Dialog Table format: {e}") from e

    @staticmethod
    def parse_file_japanese(file_path: str | Path) -> ParsedStringDat:
        """Parse a Japanese string DAT file with Shift-JIS encoding."""
        return StringDatParser.parse_file(file_path, encoding="shift-jis")

    @staticmethod
    def parse_file_english(file_path: str | Path) -> ParsedStringDat:
        """Parse an English string DAT file with UTF-8 encoding."""
        return StringDatParser.parse_file(file_path, encoding="utf-8")

    @staticmethod
    def validate_file(file_path: str | Path, encoding: str = "utf-8") -> dict:
        """Validate an FFXI Dialog Table file and return metadata."""
        try:
            parsed = StringDatParser.parse_file(file_path, encoding)
            return {
                "valid": True,
                "entry_count": parsed.entry_count,
                "encoding": parsed.encoding,
                "file_size": parsed.file_size,
                "sample_strings": [s.text[:50] for s in parsed.strings[:5]],  # First 5 strings as samples
            }
        except Exception as e:
            return {
                "valid": False,
                "error": str(e),
                "file_size": Path(file_path).stat().st_size if Path(file_path).exists() else 0,
            }
