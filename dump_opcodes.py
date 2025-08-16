import multiprocessing as mp
import os
import shutil
import urllib.parse
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from loguru import logger
from tabulate import tabulate

from models.zones import Zone
from parser.entitydat import EntityDatParser
from parser.eventcode import EventCodeParser
from parser.eventdat import EventDatParser
from parser.opcodes.base import OpcodeContext
from parser.subroutine import EventCode, Subroutine, Instruction, DataSection, DeadCode


class EventDumper:

    def __init__(self) -> None:
        self.env = Environment(loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True)
        self.opcode_parser = EventCodeParser(use_control_flow=True)
        self.ffxi_path = Path("C:\\Program Files (x86)\\PlayOnline\\SquareEnix\\FINAL FANTASY XI")

    def format_hex_dump(self, data: bytes, start_addr: int = 0) -> list[str]:
        """Format data as hex dump."""
        lines = []
        addr = (start_addr // 16) * 16
        skip = start_addr - addr
        pos = 0

        while pos < len(data):
            hex_parts = []
            ascii_parts = []

            if pos == 0 and skip > 0:
                hex_parts.extend(["  "] * skip)
                ascii_parts.extend([" "] * skip)

            bytes_in_line = 16 - (skip if pos == 0 else 0)
            end = min(pos + bytes_in_line, len(data))

            for i in range(pos, end):
                hex_parts.append(f"{data[i]:02X}")
                ascii_parts.append(chr(data[i]) if 32 <= data[i] <= 126 else ".")

            while len(hex_parts) < 16:
                hex_parts.append("  ")
                ascii_parts.append(" ")

            hex_str = " ".join(hex_parts[:8]) + "  " + " ".join(hex_parts[8:])
            ascii_str = "".join(ascii_parts)
            lines.append(f"{addr:04X}: {hex_str}  {ascii_str}")

            addr += 16
            pos = end
            skip = 0

        return lines

    def dump_zone(self, zone: Zone) -> None:
        """Dump all events for a zone."""
        logger.info(f"Processing zone {zone.name} (ID: {zone.id})")

        zone_path = Path("dumps") / zone.name
        
        # Clean up existing zone folder if it exists
        if zone_path.exists():
            logger.debug(f"Cleaning up existing folder for {zone.name}")
            shutil.rmtree(zone_path)
        
        zone_path.mkdir(parents=True, exist_ok=True)

        # Parse data files
        event_dat = self._parse_event_data(zone)
        if not event_dat:
            return

        zone_entities = self._parse_entity_data(zone)
        zone_strings = self._get_zone_strings(zone)

        actor_info = []

        for block_index, block in enumerate(event_dat.blocks):
            actor_data = self._process_actor(zone, block, block_index, event_dat, zone_entities, zone_strings, zone_path)
            if actor_data:
                actor_info.append(actor_data)

        # Write zone README
        self._write_zone_readme(zone, zone_path, actor_info)

        # Dump strings
        if zone_strings:
            self._dump_strings(zone, zone_path, zone_strings)

        logger.info(f"Completed zone {zone.name}")

    def _parse_event_data(self, zone: Zone):
        """Parse event data file."""
        try:
            if not zone.files or not zone.files.events:
                logger.warning(f"Zone {zone.name} has no event data file defined")
                return None
            path = self.ffxi_path / zone.files.events
            event_dat = EventDatParser.parse_file(path)
            logger.info(f"Zone {zone.name}: Found {event_dat.get_total_events()} events across {len(event_dat.blocks)} actors")
            return event_dat
        except Exception as e:
            logger.error(f"Failed to parse event data for zone {zone.name}: {e}")
            return None

    def _parse_entity_data(self, zone: Zone):
        """Parse entity data file."""
        try:
            if not zone.files or not zone.files.entities:
                logger.debug(f"Zone {zone.name} has no entity data file defined")
                return None
            path = self.ffxi_path / zone.files.entities
            entities = EntityDatParser.parse_file(path, zone.id, zone.name)
            logger.info(f"Zone {zone.name}: Found {len(entities.entities)} entities")
            return entities
        except Exception as e:
            logger.warning(f"Failed to parse entity data for zone {zone.name}: {e}")
            return None

    def _get_zone_strings(self, zone: Zone):
        """Get zone strings."""
        try:
            return zone.get_strings_na()
        except Exception as e:
            logger.warning(f"Failed to get strings for zone {zone.name}: {e}")
            return None

    def _get_actor_name(self, actor_number: int, zone_entities) -> tuple[str, str]:
        """Get actor folder name and display name."""
        if actor_number == 0x7FFFFFF0:
            return "Zone Events", "Zone Events"
        elif actor_number == 0x7FFFFFFF:
            return f"{actor_number} - Zone Player Events", "Zone/Player Events"

        folder_name = str(actor_number)
        display_name = "(unnamed)"

        if zone_entities:
            entity = zone_entities.get_entity_by_id(actor_number)
            if entity and entity.name:
                clean_name = "".join(c for c in entity.name if c.isalnum() or c in (" ", "-", "_")).strip()
                if clean_name:
                    folder_name = f"{actor_number} - {clean_name}"
                    display_name = clean_name

        return folder_name, display_name

    def _process_actor(self, zone, block, block_index, event_dat, zone_entities, zone_strings, zone_path):
        """Process a single actor block."""
        actor_number = block.actor_number
        folder_name, display_name = self._get_actor_name(actor_number, zone_entities)
        actor_path = zone_path / folder_name

        event_summaries = []
        event_id_counts = {}
        actor_has_events = False

        for event_index, (event_id, offset, event_data) in enumerate(block.get_all_events()):
            if len(event_data) < 1:
                continue

            try:
                # Parse and write event
                instructions, control_flow_data = self.opcode_parser.parse_event_data(event_data, offset)
                context = OpcodeContext(imed_data=block.imed_data, zone_entities=zone_entities, zone_strings=zone_strings)

                if event_id in event_id_counts:
                    event_id_counts[event_id] += 1
                    filename = f"{event_id}.{event_id_counts[event_id]}.md"
                    display_id = f"{event_id}.{event_id_counts[event_id]}"
                else:
                    event_id_counts[event_id] = 0
                    filename = f"{event_id}.md"
                    display_id = str(event_id)

                # Calculate size using the correct index
                if event_index + 1 < len(block.tag_offsets):
                    calculated_size = block.tag_offsets[event_index + 1] - offset
                else:
                    calculated_size = block.event_data_size - offset

                # Create actor dir if needed
                if not actor_has_events:
                    actor_path.mkdir(parents=True, exist_ok=True)
                    actor_has_events = True

                # Write event file
                self._write_event_file(
                    actor_path / filename,
                    event_id,
                    event_index,
                    block.tag_count,
                    offset,
                    event_data,
                    calculated_size,
                    instructions,
                    context,
                    control_flow_data,
                )

                event_summaries.append(
                    {
                        "display_id": display_id,
                        "filename": filename,
                        "offset": offset,
                        "size": len(event_data),
                        "instructions": len(instructions),
                    }
                )

            except Exception as e:
                logger.error(f"Failed to parse event {event_id} in zone {zone.name}, actor {actor_number}: {e}")
                raise

        # Write actor README if we have events
        if actor_has_events and event_summaries:
            self._write_actor_readme(actor_path, actor_number, display_name, zone, block, block_index, event_dat, event_summaries)

        if not event_summaries:
            return None

        return {
            "id": actor_number,
            "display_name": display_name,
            "folder": folder_name,
            "folder_encoded": urllib.parse.quote(folder_name),
            "event_count": len(event_summaries),
        }

    def _write_event_file(self, filepath, event_id, event_index, total_events, offset, event_data, calculated_size, instructions, context, control_flow_data):
        """Write a single event file."""
        # Build the EventCode structure
        event_code = self._build_event_code(
            event_id, event_index, total_events, offset, event_data, calculated_size, instructions, context, control_flow_data
        )
        
        # Build metadata table
        metadata_table = tabulate(
            [
                ["Event Index", f"{event_code.event_index + 1}/{event_code.total_events}"],
                ["Offset", f"0x{event_code.offset:04X}"],
                ["Data Size", f"{event_code.data_size} bytes"],
                ["Calculated Size", f"{event_code.calculated_size} bytes"],
                ["Instructions", str(event_code.total_instructions)],
            ],
            headers=["Field", "Value"],
            tablefmt="github",
        )

        # Render template with the cleaner structure
        template = self.env.get_template("event_simple.md.j2")
        content = template.render(
            event_id=event_code.event_id,
            metadata_table=metadata_table,
            hex_dump=self.format_hex_dump(event_data, offset),
            event_code=event_code,
        )

        filepath.write_text(content, encoding="utf-8")
    
    def _build_event_code(self, event_id, event_index, total_events, offset, event_data, calculated_size, instructions, context, control_flow_data):
        event_code = EventCode(
            event_id=event_id,
            event_index=event_index,
            total_events=total_events,
            offset=offset,
            data_size=len(event_data),
            calculated_size=calculated_size,
        )
        
        reachable = control_flow_data.get("reachable_offsets") if control_flow_data else None
        jump_targets = control_flow_data.get("jump_targets", set()) if control_flow_data else set()
        subroutine_starts = self._find_subroutine_starts(instructions, reachable, jump_targets, offset)
        
        current_offset = 0
        instruction_num = 0
        current_subroutine = None
        current_dead_code = None
        
        for i, inst in enumerate(instructions):
            is_data_section = inst.opcode == 0xFF and hasattr(inst.opcode_impl, "name") and inst.opcode_impl.name == "DATA_SECTION"
            is_reachable = reachable is None or current_offset in reachable
            
            if is_data_section:
                self._finalize_sections(event_code, current_subroutine, current_dead_code)
                current_subroutine = None
                current_dead_code = None
                event_code.data_sections.append(
                    DataSection(
                        offset=offset + current_offset,
                        size=len(inst.raw_bytes),
                        data=inst.raw_bytes,
                    )
                )
                
            elif is_reachable:
                desc = inst.get_legible_representation(context) if inst.opcode_impl else f"UNKNOWN_OPCODE_0x{inst.opcode:02X}"
                
                if current_offset in subroutine_starts:
                    if current_subroutine and current_subroutine.instructions:
                        current_subroutine.end_offset = offset + current_offset
                        event_code.subroutines.append(current_subroutine)
                    
                    if current_dead_code and current_dead_code.instructions:
                        event_code.dead_code_sections.append(current_dead_code)
                        current_dead_code = None
                    
                    current_subroutine = Subroutine(
                        start_offset=offset + current_offset,
                        end_offset=-1,
                        is_entry_point=(i == 0),
                    )
                
                if current_subroutine:
                    current_subroutine.instructions.append(
                        Instruction(
                            num=instruction_num,
                            offset=offset + current_offset,
                            opcode=inst.opcode,
                            description=desc,
                            raw_bytes=inst.raw_bytes,
                        )
                    )
                    instruction_num += 1
                    
            else:
                if current_subroutine and current_subroutine.instructions:
                    current_subroutine.end_offset = offset + current_offset
                    event_code.subroutines.append(current_subroutine)
                    current_subroutine = None
                
                if not current_dead_code:
                    current_dead_code = DeadCode()
                    
                desc = inst.get_legible_representation(context) if inst.opcode_impl else f"UNKNOWN_0x{inst.opcode:02X}"
                current_dead_code.instructions.append(
                    Instruction(
                        num=-1,
                        offset=offset + current_offset,
                        opcode=inst.opcode,
                        description=desc,
                        raw_bytes=inst.raw_bytes,
                    )
                )
            
            current_offset += len(inst.raw_bytes)
        
        self._finalize_sections(event_code, current_subroutine, current_dead_code, offset + current_offset)
        return event_code
    
    def _finalize_sections(self, event_code, current_subroutine, current_dead_code, end_offset=None):
        """Helper to finalize and append current sections."""
        if current_subroutine and current_subroutine.instructions:
            if end_offset:
                current_subroutine.end_offset = end_offset
            event_code.subroutines.append(current_subroutine)
            
        if current_dead_code and current_dead_code.instructions:
            event_code.dead_code_sections.append(current_dead_code)
    
    def _find_subroutine_starts(self, instructions, reachable, jump_targets, entry_offset=0):
        subroutine_starts = {0}
        
        if not jump_targets:
            return subroutine_starts
            
        goto_targets = set()
        call_targets = set()
        
        current_offset = 0
        for i, inst in enumerate(instructions):
            target = self._extract_jump_target(inst, entry_offset)
            if target is None:
                current_offset += len(inst.raw_bytes) if hasattr(inst, 'raw_bytes') else 1
                continue
                
            if 0 <= target < len(instructions) * 100:
                if inst.opcode == 0x1A:  # CALL
                    call_targets.add(target)
                    subroutine_starts.add(target)
                elif inst.opcode == 0x01:  # GOTO
                    goto_targets.add(target)
            
            current_offset += len(inst.raw_bytes)
        
        terminal_offsets = set()
        current_offset = 0
        for inst in instructions:
            if inst.opcode in [0x1B, 0x21, 0x01]:
                terminal_offsets.add(current_offset)
            current_offset += len(inst.raw_bytes)
        for target in goto_targets:
            if target in reachable:
                for term_offset in terminal_offsets:
                    if term_offset < target:
                        subroutine_starts.add(target)
                        break
                
        return subroutine_starts
    
    def _extract_jump_target(self, inst, entry_offset):
        """Extract jump target from instruction if it's a jump/call opcode."""
        if not (inst.opcode_impl and hasattr(inst, 'raw_bytes')):
            return None
            
        if inst.opcode not in [0x01, 0x1A]:  # GOTO, CALL
            return None
            
        args = inst.opcode_impl.parse_args(inst.raw_bytes)
        target = args.get('address', args.get('offset'))
        if target is not None:
            return target - entry_offset
        return None

    def _write_actor_readme(self, actor_path, actor_number, display_name, zone, block, block_index, event_dat, event_summaries):
        """Write actor README."""
        # Build actor title
        if actor_number == 0x7FFFFFF0:
            actor_title = "0x7FFFFFF0 - Zone Events"
        elif actor_number == 0x7FFFFFFF:
            actor_title = f"{actor_number} - Zone/Player Events"
        else:
            actor_title = f"{actor_number} - {display_name}" if display_name != "(unnamed)" else str(actor_number)

        # Build tables using tabulate
        common_data_table = tabulate(
            [
                ["Zone", f"{zone.name} (ID: {zone.id})"],
                ["Block Size", f"{event_dat.block_sizes[block_index]} bytes"],
                ["Total Events", str(block.tag_count)],
                ["References Count", str(block.imed_count)],
            ],
            headers=["Field", "Value"],
            tablefmt="github",
        )

        # Events table
        events_data = []
        for evt in event_summaries:
            event_link = f"[{evt['display_id']}](./{evt['filename']})"
            events_data.append([event_link, f"0x{evt['offset']:04X}", str(evt["size"]), str(evt["instructions"])])
        events_table = tabulate(events_data, headers=["Event ID", "Offset", "Size", "Instructions"], tablefmt="github")

        # References table if any
        references_table = None
        if block.imed_count > 0 and block.imed_data:
            refs_data = [[str(i), f"0x{val:04X}", str(val)] for i, val in enumerate(block.imed_data)]
            references_table = tabulate(refs_data, headers=["Index", "Hex Value", "Dec Value"], tablefmt="github")

        # Render template
        template = self.env.get_template("actor_simple.md.j2")
        content = template.render(
            actor_title=actor_title,
            common_data_table=common_data_table,
            events_table=events_table,
            references_table=references_table,
        )

        (actor_path / "README.md").write_text(content, encoding="utf-8")

    def _write_zone_readme(self, zone, zone_path, actor_info):
        """Write zone README."""
        # Zone info table
        zone_info_table = tabulate(
            [
                ["Zone ID", str(zone.id)],
                ["Total Actors", str(len(actor_info))],
                ["Total Events", str(sum(a["event_count"] for a in actor_info))],
            ],
            headers=["Field", "Value"],
            tablefmt="github",
        )

        # Source files table
        source_files = [["Events", zone.files.events]]
        if zone.files.strings_na:
            source_files.append(["Strings", zone.files.strings_na])
        if zone.files.entities:
            source_files.append(["Entities", zone.files.entities])
        source_files_table = tabulate(source_files, headers=["Type", "File Path"], tablefmt="github")

        # Actors table
        actors_data = []
        for actor in sorted(actor_info, key=lambda x: x["id"]):
            actor_id_hex = f"0x{actor['id']:08X}"
            actor_id_dec = str(actor["id"])
            name_with_link = f"[{actor['display_name']}](./{actor['folder_encoded']}/)"
            actors_data.append([actor_id_hex, actor_id_dec, name_with_link, str(actor["event_count"])])
        actors_table = tabulate(actors_data, headers=["Actor ID (Hex)", "Actor ID (Dec)", "Name", "Events"], tablefmt="github")

        # Render template
        template = self.env.get_template("zone_simple.md.j2")
        content = template.render(
            zone_name=zone.name,
            zone_info_table=zone_info_table,
            source_files_table=source_files_table,
            actors_table=actors_table,
        )

        (zone_path / "README.md").write_text(content, encoding="utf-8")

    def _dump_strings(self, zone, zone_path, zone_strings):
        """Dump zone strings."""
        try:
            with (zone_path / "strings.txt").open("w", encoding="utf-8") as f:
                f.write(f"# Strings for {zone.name}\n")
                f.write(f"# Total: {len(zone_strings.strings)} strings\n\n")
                for entry in zone_strings.strings:
                    text = entry.text.replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")
                    f.write(f"{entry.index:5d}: {text}\n")
        except Exception as e:
            logger.warning(f"Failed to dump strings for zone {zone.name}: {e}")


def _dump_zone_worker(zone):
    """Worker function for multiprocessing."""
    dumper = EventDumper()
    dumper.dump_zone(zone)


def dump_all_zones():
    """Dump all zones."""
    logger.info("Starting opcode dump for all zones...")
    zones = Zone.get_all()
    logger.info(f"Found {len(zones)} zones to process")

    Path("dumps").mkdir(parents=True, exist_ok=True)

    cpu_count = os.cpu_count() or 4
    logger.info(f"Using {cpu_count} worker processes")
    
    with mp.Pool(cpu_count) as pool:
        pool.map(_dump_zone_worker, zones)
    
    logger.info("Completed opcode dump for all zones!")


def dump_zone_by_id(zone_id: int):
    """Dump zones by ID."""
    zones = Zone.get_by_id(zone_id)
    if not zones:
        logger.error(f"Zone ID {zone_id} not found")
        return

    dumper = EventDumper()
    for zone in zones:
        logger.info(f"Processing zone variant: {zone.name}")
        dumper.dump_zone(zone)


def dump_zone_by_name(zone_name: str):
    """Dump zone by name."""
    zone = Zone.get_by_name(zone_name)
    if not zone:
        logger.error(f"Zone '{zone_name}' not found")
        return

    dumper = EventDumper()
    dumper.dump_zone(zone)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        try:
            dump_zone_by_id(int(arg))
        except ValueError:
            dump_zone_by_name(arg)
    else:
        dump_all_zones()
