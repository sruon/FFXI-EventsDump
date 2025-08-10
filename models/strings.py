from dataclasses import dataclass

from construct import Bytes, Int32ul, Struct

DialogTableDat = Struct(
    "file_size_marker" / Int32ul,  # Should be 0x10000000 + (file_size - 4)
    "raw_data" / Bytes("remaining"),  # Rest of file for manual processing
)


@dataclass
class ParsedString:
    index: int
    offset: int
    text: str
    encoding: str = "utf-8"

    def __str__(self) -> str:
        return f"String[{self.index}]: {self.text[:50]}{'...' if len(self.text) > 50 else ''}"


@dataclass
class ParsedStringDat:

    entry_count: int
    strings: list[ParsedString]
    encoding: str = "utf-8"
    file_size: int = 0

    @classmethod
    def from_raw_data(cls, raw_data: bytes, encoding: str = "utf-8") -> "ParsedStringDat":
        """Create from raw file data following FFXI Dialog Table format."""
        if len(raw_data) < 8:
            raise ValueError("File too small to be a valid Dialog Table")

        # Read file size marker
        file_size_marker = int.from_bytes(raw_data[0:4], "little")
        expected_marker = 0x10000000 + len(raw_data) - 4

        if file_size_marker != expected_marker:
            raise ValueError(f"Invalid file size marker: {file_size_marker:08X}, expected {expected_marker:08X}")

        # Read first text position (XOR'd with 0x80808080)
        first_text_pos = int.from_bytes(raw_data[4:8], "little") ^ 0x80808080

        if first_text_pos % 4 != 0 or first_text_pos > len(raw_data) or first_text_pos < 8:
            raise ValueError(f"Invalid first text position: {first_text_pos}")

        # Calculate entry count
        entry_count = first_text_pos // 4

        # Read all offset entries
        offsets = [first_text_pos]
        for i in range(1, entry_count):
            offset_pos = 4 + (i * 4)
            if offset_pos + 4 > len(raw_data):
                break
            offset = int.from_bytes(raw_data[offset_pos : offset_pos + 4], "little") ^ 0x80808080
            offsets.append(offset)

        # Add end-of-file as final offset
        offsets.append(len(raw_data) - 4)
        offsets.sort()

        # Extract strings
        strings = []
        for i in range(entry_count):
            # Check bounds - offsets should be relative to start of file (after size marker)
            if offsets[i] < 4 * entry_count or offsets[i] >= len(raw_data) - 4:
                continue

            # Offsets are relative to the position after the file size marker (position 4)
            start_pos = offsets[i] + 4
            end_pos = (offsets[i + 1] + 4) if i + 1 < len(offsets) else len(raw_data)

            # Ensure we don't read past end of file
            if start_pos >= len(raw_data) or end_pos > len(raw_data):
                continue

            try:
                string_bytes = raw_data[start_pos:end_pos]

                # FFXI strings are encoded by adding 0x80 to each byte - decode them
                decoded_bytes = bytes(b - 0x80 if b >= 0x80 else b for b in string_bytes)

                # Remove null terminators
                decoded_bytes = decoded_bytes.rstrip(b"\x00")

                text = decoded_bytes.decode(encoding, errors="replace")
                strings.append(ParsedString(index=i, offset=offsets[i], text=text, encoding=encoding))
            except Exception:
                # If decoding fails, store as hex representation
                hex_text = string_bytes.hex() if "string_bytes" in locals() else ""
                strings.append(
                    ParsedString(
                        index=i,
                        offset=offsets[i] if i < len(offsets) else 0,
                        text=f"<DECODE_ERROR:{hex_text}>",
                        encoding=encoding,
                    )
                )

        return cls(
            entry_count=entry_count,
            strings=strings,
            encoding=encoding,
            file_size=len(raw_data),
        )

    def get_string_by_index(self, index: int) -> ParsedString | None:
        """Get string by index."""
        if 0 <= index < len(self.strings):
            return self.strings[index]
        return None

    def get_string_text(self, index: int) -> str | None:
        """Get string text by index."""
        string_obj = self.get_string_by_index(index)
        return string_obj.text if string_obj else None

    def search_strings(self, query: str, case_sensitive: bool = False) -> list[ParsedString]:
        """Search for strings containing the query."""
        results = []
        query_lower = query.lower() if not case_sensitive else query

        for string_obj in self.strings:
            text_to_search = string_obj.text.lower() if not case_sensitive else string_obj.text
            if query_lower in text_to_search:
                results.append(string_obj)

        return results

    def __str__(self) -> str:
        return f"ParsedStringDat(entries={self.entry_count}, encoding={self.encoding}, size={self.file_size})"
