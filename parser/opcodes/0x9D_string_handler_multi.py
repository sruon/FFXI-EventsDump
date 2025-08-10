from .base import ArgType, BaseOpcode, OpcodeArg


class StringHandlerMultiOpcode(BaseOpcode):
    opcode = 0x9D
    name = "OPCODE_9D"

    def get_args(self):
        # Variable arguments based on subcase
        return [
            OpcodeArg("subcase", ArgType.BYTE, 1, "Subcase (0-16)"),
            # Additional args depend on subcase - parsed dynamically
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        """Calculate variable length based on subcase."""
        if offset + 1 > len(data):
            return 1

        subcase = data[offset + 1]

        # Length based on Atomos documentation (ExecPointer increments)
        length_map = {
            0x00: 8,  # Conditional table lookup
            0x01: 8,  # Copy 16-byte string from event data
            0x02: 6,  # Store event data and reference pointers
            0x03: 8,  # Context switch and value read
            0x04: 8,  # Read string from work zone pointer
            0x05: 8,  # Set value at calculated offset
            0x06: 8,  # Store string at calculated position
            0x07: 6,  # Jump table call
            0x08: 23,  # String compare with literal
            0x09: 9,  # String compare with variable
            0x0A: 10,  # Conditional value retrieval
            0x0B: 10,  # Conditional string retrieval
            0x0C: 8,  # Store EventData and References pointers (duplicate of 0x02?)
            0x0D: 10,  # Context switch and value storage
            0x0E: 10,  # Read string from work zone pointer
            0x0F: 10,  # Set value at calculated offset
            0x10: 10,  # Store string at calculated position
        }

        return length_map.get(subcase, 2)  # Default to 2 if unknown

    def parse_args(self, raw_bytes: bytes):
        """Parse arguments based on subcase."""
        if len(raw_bytes) < 2:
            return {"subcase": 0}

        args = {"subcase": raw_bytes[1]}
        subcase = args["subcase"]

        if subcase == 0x00:  # Conditional table lookup
            if len(raw_bytes) >= 8:
                args["table_addr"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["dest_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["val1_offset"] = int.from_bytes(raw_bytes[6:8], byteorder="little")

        elif subcase == 0x01:  # Copy 16-byte string from event data
            if len(raw_bytes) >= 8:
                # getworkstrofs_(this, 6), eventgetcode(this, 2), getworkofs_(this, 4)
                args["event_offset"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["index_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["dest_offset"] = int.from_bytes(raw_bytes[6:8], byteorder="little")
        elif subcase == 0x02:  # Store event data and reference pointers
            if len(raw_bytes) >= 6:
                # setworkofs_(this, 2, EventData), setworkofs_(this, 4, References)
                args["eventdata_offset"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["references_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")

        elif subcase == 0x03:  # Context switch and value read
            if len(raw_bytes) >= 8:
                args["zone_index"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["condition"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["work_offset"] = int.from_bytes(raw_bytes[6:8], byteorder="little")

        elif subcase == 0x04:  # Read string from work zone pointer
            if len(raw_bytes) >= 8:
                args["zone_index"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["string_index"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["dest_offset"] = int.from_bytes(raw_bytes[6:8], byteorder="little")

        elif subcase == 0x05:  # Set value at calculated offset
            if len(raw_bytes) >= 8:
                # getworkofs_(this, 6), getworkofs_(this, 4), eventgetcode(this, 2)
                # setworkofs_(this, 2 * val1, val2)
                args["table_addr"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["value_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["index_offset"] = int.from_bytes(raw_bytes[6:8], byteorder="little")

        elif subcase == 0x06:  # Store string at calculated position
            if len(raw_bytes) >= 8:
                # getworkstrofs_(this, 4), getworkofs_(this, 6), eventgetcode(this, 2)
                args["table_addr"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["string_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["index_offset"] = int.from_bytes(raw_bytes[6:8], byteorder="little")

        elif subcase == 0x07:  # Jump table call
            if len(raw_bytes) >= 6:
                # getworkofs_(this, 4), eventgetcode(this, 2)
                args["jump_table"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["index_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")

        elif subcase == 0x08:  # String compare with literal
            if len(raw_bytes) >= 23:
                # Complex string comparison with branching
                args["str1_offset"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["str2_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["literal_string"] = raw_bytes[6:22]  # 16 bytes
                args["jump_offset"] = raw_bytes[22]

        elif subcase == 0x09:  # String compare with variable
            if len(raw_bytes) >= 9:
                # String comparison with work area strings
                args["str1_offset"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["str2_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["flags_offset"] = int.from_bytes(raw_bytes[6:8], byteorder="little")
                args["jump_offset"] = raw_bytes[8]

        elif subcase in [0x0A, 0x0B]:  # Conditional value/string retrieval
            if len(raw_bytes) >= 10:
                args["condition"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["source_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["dest_offset"] = int.from_bytes(raw_bytes[6:8], byteorder="little")
                args["extra"] = int.from_bytes(raw_bytes[8:10], byteorder="little")

        elif subcase == 0x0C:  # Store EventData and References (like 0x02)
            if len(raw_bytes) >= 8:
                args["eventdata_offset"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["references_offset"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["extra"] = int.from_bytes(raw_bytes[6:8], byteorder="little")

        elif subcase in [0x0D, 0x0E, 0x0F, 0x10]:  # Various operations
            if len(raw_bytes) >= 10:
                args["param1"] = int.from_bytes(raw_bytes[2:4], byteorder="little")
                args["param2"] = int.from_bytes(raw_bytes[4:6], byteorder="little")
                args["param3"] = int.from_bytes(raw_bytes[6:8], byteorder="little")
                args["param4"] = int.from_bytes(raw_bytes[8:10], byteorder="little")

        else:
            # Capture raw parameters for unimplemented subcases
            if len(raw_bytes) > 2:
                args["raw_params"] = raw_bytes[2:]

        return args

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):
        subcase = args["subcase"]

        if subcase == 0x00:
            # Conditional table lookup operation
            table = args.get("table_addr", 0)
            dest = args.get("dest_offset", 0)
            val1 = args.get("val1_offset", 0)

            dest_str = self.format_work_area_value(dest, context=context)
            val1_str = self.format_work_area_value(val1, context=context)

            # Show as: dest = table[index] format, reading WORD values
            return f"{dest_str} = 0x{table:04X}[{val1_str}] // Read WORD"

        elif subcase == 0x01:
            # Copy 16-byte string from event data
            event_off = args.get("event_offset", 0)
            index = args.get("index_offset", 0)
            dest = args.get("dest_offset", 0)

            index_str = self.format_work_area_value(index, context=context)
            dest_str = self.format_work_area_value(dest, context=context)

            return f"{dest_str} = EventData[0x{event_off:04X} + {index_str}] // Copy 16-byte string"
        elif subcase == 0x02:
            # Remap VM variable space pointers
            # Sets Work_Zone and References to point to different memory
            event_pos = args.get("eventdata_offset", 0)
            zone_idx = args.get("references_offset", 0)

            # Special handling for 0x8000 which resolves to "0*"
            if zone_idx == 0x8000 and context and context.imed_data and len(context.imed_data) > 0:
                if context.imed_data[0] == 0:
                    zone_str = "0"  # Just show 0, not 0*
                else:
                    zone_str = self.format_work_area_value(zone_idx, context=context)
            else:
                zone_str = self.format_work_area_value(zone_idx, context=context)

            # Remaps the VM's variable space at this index
            return f"Remap Work_Zone[{zone_str}] -> EventData[0x{event_pos:04X}]"

        elif subcase == 0x03:
            # Read using remapped variable space
            zone = args.get("zone_index", 0)
            cond = args.get("condition", 0)
            work = args.get("work_offset", 0)

            # Special handling for 0x8000 which resolves to "0*"
            if zone == 0x8000 and context and context.imed_data and len(context.imed_data) > 0:
                if context.imed_data[0] == 0:
                    zone_str = "0"  # Just show 0, not 0*
                else:
                    zone_str = self.format_work_area_value(zone, context=context)
            else:
                zone_str = self.format_work_area_value(zone, context=context)

            cond_str = self.format_work_area_value(cond, context=context)
            work_str = self.format_work_area_value(work, context=context)

            # Uses the remapped address space to read a value
            return f"{work_str} = Work_Zone[{zone_str}][{cond_str}] // Via remapped space"

        elif subcase == 0x04:
            # Read string from work zone pointer
            zone = args.get("zone_index", 0)
            str_idx = args.get("string_index", 0)
            dest = args.get("dest_offset", 0)

            zone_str = self.format_work_area_value(zone, context=context)
            idx_str = self.format_work_area_value(str_idx, context=context)
            dest_str = self.format_work_area_value(dest, context=context)

            return f"{dest_str} = WorkZone[{zone_str}]->String[{idx_str}]"

        elif subcase == 0x05:
            # Set value at calculated offset
            table = args.get("table_addr", 0)
            value = args.get("value_offset", 0)
            index = args.get("index_offset", 0)

            value_str = self.format_work_area_value(value, context=context)
            index_str = self.format_work_area_value(index, context=context)

            # Writing WORD value to table
            return f"0x{table:04X}[{index_str} * 2] = {value_str} // Write WORD"

        elif subcase == 0x06:
            # Store string at calculated position
            table = args.get("table_addr", 0)
            string = args.get("string_offset", 0)
            index = args.get("index_offset", 0)

            string_str = self.format_work_area_value(string, context=context)
            index_str = self.format_work_area_value(index, context=context)

            # Writing 16-byte string to table
            return f"0x{table:04X}[{index_str} * 2] = {string_str} // Write STRING"

        elif subcase == 0x07:
            # Jump table call
            table = args.get("jump_table", 0)
            index = args.get("index_offset", 0)

            index_str = self.format_work_area_value(index, context=context)

            return f"CALL 0x{table:04X}[{index_str}] // Jump table"

        elif subcase == 0x08:
            # String compare with literal, conditional jump
            str1 = args.get("str1_offset", 0)
            str2 = args.get("str2_offset", 0)
            literal = args.get("literal_string", b"")
            jump = args.get("jump_offset", 0)

            str1_str = self.format_work_area_value(str1, context=context)
            str2_str = self.format_work_area_value(str2, context=context)

            # Try to decode literal string
            try:
                literal_str = literal.rstrip(b"\x00").decode("ascii")
                if all(c.isprintable() for c in literal_str):
                    literal_display = f'"{literal_str}"'
                else:
                    literal_display = literal.hex()
            except Exception:
                literal_display = literal.hex()

            return f"IF (strcmp({str1_str}, {literal_display}) != 0) GOTO 0x{jump:02X} // Also sets {str2_str}"

        elif subcase == 0x09:
            # String compare with variable, conditional jump
            str1 = args.get("str1_offset", 0)
            str2 = args.get("str2_offset", 0)
            flags = args.get("flags_offset", 0)
            jump = args.get("jump_offset", 0)

            str1_str = self.format_work_area_value(str1, context=context)
            str2_str = self.format_work_area_value(str2, context=context)
            flags_str = self.format_work_area_value(flags, context=context)

            return f"IF (strcmp({str1_str}, {str2_str}) with flags {flags_str}) GOTO 0x{jump:02X}"

        elif subcase == 0x0A:
            # Conditional value retrieval
            cond = args.get("condition", 0)
            src = args.get("source_offset", 0)
            dest = args.get("dest_offset", 0)
            extra = args.get("extra", 0)

            cond_str = self.format_work_area_value(cond, context=context)
            src_str = self.format_work_area_value(src, context=context)
            dest_str = self.format_work_area_value(dest, context=context)

            return f"IF ({cond_str}) {dest_str} = {src_str} // extra=0x{extra:04X}"

        elif subcase == 0x0B:
            # Conditional string retrieval
            cond = args.get("condition", 0)
            src = args.get("source_offset", 0)
            dest = args.get("dest_offset", 0)
            extra = args.get("extra", 0)

            cond_str = self.format_work_area_value(cond, context=context)
            src_str = self.format_work_area_value(src, context=context)
            dest_str = self.format_work_area_value(dest, context=context)

            return f"IF ({cond_str}) {dest_str} = String[{src_str}] // extra=0x{extra:04X}"

        elif subcase == 0x0C:
            # Remap VM variable space (extended version)
            event_pos = args.get("eventdata_offset", 0)
            zone_idx = args.get("references_offset", 0)
            extra = args.get("extra", 0)

            zone_str = self.format_work_area_value(zone_idx, context=context)
            extra_str = self.format_work_area_value(extra, context=context)

            return f"Remap Work_Zone[{zone_str}] -> EventData[0x{event_pos:04X}] // Extra={extra_str}"

        elif subcase == 0x0D:
            # Context switch and value storage
            p1 = args.get("param1", 0)
            p2 = args.get("param2", 0)
            p3 = args.get("param3", 0)
            p4 = args.get("param4", 0)

            p1_str = self.format_work_area_value(p1, context=context)
            p2_str = self.format_work_area_value(p2, context=context)
            p3_str = self.format_work_area_value(p3, context=context)

            return f"Context switch then {p3_str} = value // p1={p1_str}, p2={p2_str}, p4=0x{p4:04X}"

        elif subcase == 0x0E:
            # Read string from work zone pointer
            p1 = args.get("param1", 0)
            p2 = args.get("param2", 0)
            p3 = args.get("param3", 0)
            p4 = args.get("param4", 0)

            p1_str = self.format_work_area_value(p1, context=context)
            p2_str = self.format_work_area_value(p2, context=context)
            p3_str = self.format_work_area_value(p3, context=context)

            return f"{p3_str} = String from zone // p1={p1_str}, p2={p2_str}, p4=0x{p4:04X}"

        elif subcase == 0x0F:
            # Set value at calculated offset
            p1 = args.get("param1", 0)
            p2 = args.get("param2", 0)
            p3 = args.get("param3", 0)
            p4 = args.get("param4", 0)

            p1_str = self.format_work_area_value(p1, context=context)
            p2_str = self.format_work_area_value(p2, context=context)
            p3_str = self.format_work_area_value(p3, context=context)

            return f"Table[{p1_str}] = {p2_str} // p3={p3_str}, p4=0x{p4:04X}"

        elif subcase == 0x10:
            # Store string at calculated position
            p1 = args.get("param1", 0)
            p2 = args.get("param2", 0)
            p3 = args.get("param3", 0)
            p4 = args.get("param4", 0)

            p1_str = self.format_work_area_value(p1, context=context)
            p2_str = self.format_work_area_value(p2, context=context)
            p3_str = self.format_work_area_value(p3, context=context)

            return f"Table[{p1_str}] = String[{p2_str}] // p3={p3_str}, p4=0x{p4:04X}"

        else:
            # Unknown subcase
            params = args.get("raw_params", b"")
            if params:
                data_hex = " ".join(f"{b:02X}" for b in params[:6])
                return f"OPCODE_9D[0x{subcase:02X}]: Unknown (params: {data_hex}...)"
            else:
                return f"OPCODE_9D[0x{subcase:02X}]: Unknown"

    def get_jump_targets(self, args: dict, context=None) -> list:
        """Return jump targets for subcases that have them."""
        subcase = args.get("subcase", 0)

        if subcase == 0x07:
            # CALL - but this is more like a computed jump
            # The actual target is computed from jump table
            return []  # Can't determine statically
        elif subcase == 0x08:
            # String compare with jump
            if "jump_offset" in args:
                return [args["jump_offset"]]
        elif subcase == 0x09:
            # String compare with jump
            if "jump_offset" in args:
                return [args["jump_offset"]]

        return []
