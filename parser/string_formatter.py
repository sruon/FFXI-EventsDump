import re


class FFXIStringFormatter:
    def __init__(self):
        self.in_selection = False
        self.result = []
        self.text = ""
        self.pos = 0

        self.direct_params = {
            0x03: "$3",
            0x04: "$4",
            0x05: "$5",
            0x06: "$6",
            0x17: "%",
        }

        self.indexed_params = {
            0x0A: "$",
            0x08: "%",
            0x09: "$",
            0x18: "%",
            0x19: "%",
            0x1A: "%",
            0x1C: "%",
            0x0C: "",
            0x0D: "$",
            0x0E: "$",
            0x0F: "$",
        }

        self.skip_bytes = {0x02, 0x1E, 0x1F}

    def format(self, text):
        self.text = text
        self.pos = 0
        self.result = []
        self.in_selection = False

        if text.startswith("\x02P\x00\x03T\x01"):
            self.result.append("[Cutscene] ")
            self.pos = 6

        while self.pos < len(text):
            byte = ord(text[self.pos])

            if byte in self.direct_params:
                self.result.append(self.direct_params[byte])
                self.pos += 1
            elif byte in self.indexed_params:
                self._handle_indexed_param(byte)
            elif byte == 0x07:
                self._handle_line_break()
            elif byte == 0x0B:
                self._handle_selection_start()
            elif byte == 0x01:
                self._handle_complex_param()
            elif byte == 0x7F:
                self._handle_special_marker()
            elif byte == 0x1E:
                self._handle_color_code()
            elif byte == 0x1F:
                self.pos += 2 if self.pos + 1 < len(text) else 1
            elif byte in self.skip_bytes:
                self.pos += 1
            elif byte == 0x00:
                self._handle_null_byte()
            elif byte < 0x20:
                self._handle_other_control(byte)
            elif 0x20 <= byte < 0x7F:
                self.result.append(text[self.pos])
                self.pos += 1
            else:
                self.pos += 1

        return self._cleanup_result()

    def _handle_indexed_param(self, byte):
        prefix = self.indexed_params[byte]
        
        # Handle special cases first
        special_handler = self._get_special_handler(byte)
        if special_handler:
            special_handler()
            return
            
        # Standard indexed parameter handling
        if self.pos + 1 < len(self.text):
            next_byte = ord(self.text[self.pos + 1])
            if next_byte < 0x20:
                self.result.append(f"{prefix}{next_byte}")
                self.pos += 2
            else:
                self.result.append("%" if byte in {0x08, 0x09} else prefix)
                self.pos += 1
        else:
            self.result.append("%" if byte in {0x08, 0x09} else prefix)
            self.pos += 1
    
    def _get_special_handler(self, byte):
        if byte == 0x08 and (self.pos + 1 >= len(self.text) or ord(self.text[self.pos + 1]) >= 0x20):
            return self._handle_player
        elif byte == 0x09 and self.pos + 1 < len(self.text) and self.text[self.pos + 1] == ")":
            return self._handle_speaker_zero
        elif byte == 0x0C:
            return self._handle_selection_param
        return None
    
    def _handle_player(self):
        self.result.append("<Player>")
        self.pos += 1
    
    def _handle_speaker_zero(self):
        self.result.append("$0")
        self.pos += 4 if self.pos + 3 < len(self.text) else 2
    
    def _handle_selection_param(self):
        if self.pos + 1 < len(self.text):
            next_char = self.text[self.pos + 1]
            skip = 2 if ord(next_char) < 0x20 or next_char == "!" else 1
            self.pos += skip
        else:
            self.pos += 1

    def _handle_line_break(self):
        if self.pos + 1 < len(self.text):
            next_byte = ord(self.text[self.pos + 1])
            if next_byte == 0x32 and not (self.pos + 3 < len(self.text) and self.text[self.pos + 2:self.pos + 4] == "nd"):
                self.result.append('"')
                self.pos += 2
            elif next_byte == 0x33 and not (self.pos + 3 < len(self.text) and self.text[self.pos + 2:self.pos + 4] == "rd"):
                self.result.append('"')
                self.pos += 2
            else:
                self.result.append("/" if self.in_selection else " ")
                self.pos += 1
        else:
            self.result.append("/" if self.in_selection else " ")
            self.pos += 1

    def _handle_selection_start(self):
        if self.result and self.result[-1] != " ":
            self.result.append(" ")
        self.result.append("[")
        self.in_selection = True
        self.pos += 1

    def _handle_complex_param(self):
        # Look for \x02 terminator within next 10 bytes
        search_end = min(self.pos + 10, len(self.text))
        search_start = self.pos + 3 if self.pos + 3 < len(self.text) else len(self.text)
        
        for j in range(search_start, search_end):
            if ord(self.text[j]) == 0x02:
                param = self._extract_param_at_terminator(j)
                if param:
                    self.result.append(param)
                    self.pos = j + 4
                    return
        
        # Simple \x01\xXX pattern
        if self.pos + 1 < len(self.text):
            next_byte = ord(self.text[self.pos + 1])
            if next_byte < 0x20:
                self.result.append(f"${next_byte}")
                self.pos += 2
                return
        
        self.pos += 1
    
    def _extract_param_at_terminator(self, term_pos):
        # Check character before \x02
        if term_pos > self.pos + 2 and self.text[term_pos - 1].isdigit():
            return f"${self.text[term_pos - 1]}"
        if term_pos > 0 and self.text[term_pos - 1] == ")":
            return "$0"
        # Multi-byte index after \x02
        if term_pos + 3 < len(self.text):
            idx = ord(self.text[term_pos + 1]) | (ord(self.text[term_pos + 2]) << 8) | (ord(self.text[term_pos + 3]) << 16)
            return f"${idx}"
        return None

    def _handle_special_marker(self):
        if self.pos + 1 < len(self.text):
            next_byte = ord(self.text[self.pos + 1])

            if (next_byte == 0x00 and self.pos + 9 < len(self.text) 
                and self.text[self.pos + 2:self.pos + 5] == "\x01\x01\x05"
                and self.text[self.pos + 6:self.pos + 10] == "\x02\x00\x00\x00"):
                self.result.append(self.text[self.pos + 5])
                self.pos += 10
            elif next_byte == 0x31:
                if self.in_selection:
                    self.result.append("]")
                    self.in_selection = False
                self.pos += 3 if self.pos + 2 < len(self.text) and ord(self.text[self.pos + 2]) != 0 else 2
            elif next_byte in {0x05, 0x12}:
                self.pos += 3 if next_byte == 0x12 else 2
            else:
                self.pos += min(3, len(self.text) - self.pos)
        else:
            self.pos += 1

    def _handle_color_code(self):
        if self.pos + 1 < len(self.text):
            next_byte = ord(self.text[self.pos + 1])
            if next_byte == 0x1F and self.pos + 2 < len(self.text):
                self.pos += 3
            else:
                self.pos += 2
        else:
            self.pos += 1

    def _handle_null_byte(self):
        if self.result and self.pos + 1 < len(self.text) and self.result[-1] not in [" ", "\n", "\t"]:
            self.result.append(" ")
        self.pos += 1

    def _handle_other_control(self, byte):
        if 0x10 <= byte <= 0x16:
            if self.pos + 1 < len(self.text) and ord(self.text[self.pos + 1]) < 0x20:
                self.result.append(f"${ord(self.text[self.pos + 1])}")
                self.pos += 2
            else:
                self.result.append(f"$P{byte:02X}")
                self.pos += 1
        else:
            self.pos += 1

    def _cleanup_result(self):
        result_str = "".join(self.result)
        result_str = re.sub(r"\s+", " ", result_str)
        return "".join(c for c in result_str if ord(c) >= 0x20 or c in ["\n", "\t"]).strip()


def format_string(text):
    formatter = FFXIStringFormatter()
    return formatter.format(text)
