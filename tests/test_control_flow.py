"""
Tests for control flow analysis in FFXI event bytecode.
"""

import pytest
from parser.control_flow import ControlFlowAnalyzer
from parser.eventcode import EventCodeParser
from parser.opcodes.base import OpcodeContext
from dump_opcodes import EventDumper


class TestControlFlow:
    """Test control flow analysis."""
    
    def build_event_code(self, event_data, event_id="test", entry_offset=0x0000):
        """Helper to build event code from bytecode."""
        analyzer = ControlFlowAnalyzer()
        result = analyzer.analyze(event_data, entry_offset=entry_offset)
        
        parser = EventCodeParser(use_control_flow=False)
        instructions, _ = parser.parse_event_data(event_data, entry_offset=entry_offset)
        
        dumper = EventDumper()
        context = OpcodeContext(imed_data=[])
        return dumper._build_event_code(
            event_id=event_id,
            event_index=0,
            total_events=1,
            offset=entry_offset,
            event_data=event_data,
            calculated_size=len(event_data),
            instructions=instructions,
            context=context,
            control_flow_data=result
        ), result
    
    def test_simple_conditional_with_goto(self):
        """Test basic control flow with IF and GOTO."""
        event_data = bytes.fromhex(
            "03 00 00 01 10"  # Work[0] = Work[1]
            "02 00 00 01 00 01 15 00"  # IF !(Work[0] == 1) GOTO 0x15
            "03 00 00 02 00"  # Work[0] = 2
            "01 1A 00"  # GOTO 0x1A
            "03 00 00 03 00"  # Work[0] = 3
            "21"  # END_EVENT
            "00"  # END_REQSTACK
        )
        
        _, result = self.build_event_code(event_data)
        reachable = result['reachable_offsets']
        assert 0x00 in reachable  # Entry point
        assert 0x15 in reachable  # IF jump target
        assert 0x1A in reachable  # GOTO target
        
        assert result['jump_targets'] == {0x15, 0x1A}
        
    def test_subroutine_detection(self):
        """Test that subroutines are detected correctly."""
        event_data = bytes.fromhex(
            "48 01 80 23"  # MESSAGE
            "02 00 10 00 80 00 10 00"  # IF !(Work[0] == 0) GOTO 0x10
            "48 02 80 23"  # MESSAGE  
            "1B"  # RETURN
            "48 03 80 23"  # MESSAGE (unreachable)
            "21"  # END_EVENT
            "00"  # END_REQSTACK
        )
        
        event_code, result = self.build_event_code(event_data)
        reachable = result['reachable_offsets']
        assert 0x00 in reachable  # Entry point
        assert 0x10 in reachable  # RETURN
        assert 0x11 not in reachable  # After RETURN - unreachable
        
        assert len(event_code.subroutines) == 1
        assert event_code.subroutines[0].is_entry_point
        assert len(event_code.dead_code_sections) > 0
        
    def test_goto_creates_subroutine(self):
        """Test that GOTO target creates a new subroutine."""
        event_data = bytes.fromhex(
            "01 08 00"  # GOTO 0x08
            "48 01 80 23"  # MESSAGE (unreachable)
            "21"  # END_EVENT (unreachable)
            "48 02 80 23"  # MESSAGE (jump target)
            "00"  # END_REQSTACK
        )
        
        event_code, result = self.build_event_code(event_data)
        assert result['jump_targets'] == {0x08}
        
        assert len(event_code.subroutines) == 2
        assert event_code.subroutines[0].is_entry_point
        assert event_code.subroutines[0].start_offset == 0x00
        assert event_code.subroutines[1].start_offset == 0x08
        
    def test_end_event_end_reqstack(self):
        """Test that END_EVENT followed by END_REQSTACK is handled correctly."""
        event_data = bytes.fromhex(
            "48 01 80 23"  # MESSAGE
            "21"  # END_EVENT
            "00"  # END_REQSTACK
        )
        
        _, result = self.build_event_code(event_data)
        
        reachable = result['reachable_offsets']
        assert 0x00 in reachable
        assert 0x04 in reachable  # END_EVENT
        assert 0x05 in reachable  # END_REQSTACK
        
    def test_return_ends_subroutine(self):
        """Test that RETURN properly ends a subroutine."""
        event_data = bytes.fromhex(
            "1A 0C 00"  # CALL 0x0C
            "48 01 80 23"  # MESSAGE
            "21"  # END_EVENT
            "00"  # END_REQSTACK
            "FF FF FF"  # data section marker
            "48 02 80 23"  # MESSAGE (subroutine)
            "1B"  # RETURN
        )
        
        _, result = self.build_event_code(event_data)
        
        reachable = result['reachable_offsets']
        assert 0x00 in reachable  # CALL
        assert 0x0C in reachable  # Subroutine start (MESSAGE)
        assert 0x10 in reachable  # RETURN
        
    def test_only_calls_create_subroutines(self):
        """Test that only CALL targets create subroutines, not conditional jumps."""
        event_data = bytes.fromhex(
            "02 00 00 01 00 01 10 00"  # IF !(Work[0] == 1) GOTO 0x10
            "48 01 80 23"  # MESSAGE
            "01 14 00"  # GOTO 0x14
            "00"  # padding
            "48 02 80 23"  # MESSAGE (IF target)
            "21"  # END_EVENT (GOTO target)
            "00"  # END_REQSTACK
        )
        
        event_code, result = self.build_event_code(event_data)
        
        subroutine_starts = {sub.start_offset for sub in event_code.subroutines}
        assert 0x00 in subroutine_starts  # Entry
        assert 0x10 not in subroutine_starts  # IF target - not a subroutine
        assert 20 in subroutine_starts  # GOTO target after terminal (0x14 = 20 decimal)


class TestProblematicFiles:
    """Test cases for specific problematic files that were discovered."""
    
    def build_event_code(self, event_data, event_id="test", entry_offset=0x0000):
        """Helper to build event code from bytecode."""
        analyzer = ControlFlowAnalyzer()
        result = analyzer.analyze(event_data, entry_offset=entry_offset)
        
        parser = EventCodeParser(use_control_flow=False)
        instructions, _ = parser.parse_event_data(event_data, entry_offset=entry_offset)
        
        dumper = EventDumper()
        context = OpcodeContext(imed_data=[])
        return dumper._build_event_code(
            event_id=event_id,
            event_index=0,
            total_events=1,
            offset=entry_offset,
            event_data=event_data,
            calculated_size=len(event_data),
            instructions=instructions,
            context=context,
            control_flow_data=result
        ), result
    
    def test_file_65535_10(self):
        """Test the specific issue in 65535.10.md"""
        event_data = bytes.fromhex(
            "03 01 00 00 00"  # Work[1] = Work[0]
            "02 01 00 06 80 05 AE 00"  # IF !(Work[1] > 5) GOTO 0xAE
            "08 01 00 01 80"  # Work[1] -= 1
            "01 B3 00"  # GOTO 0xB3
            "08 01 00 07 80"  # Work[1] -= 2
            "14 01 00 08 80"  # Work[1] *= 10
            "07 01 00 09 80"  # Work[1] += 9
            "1B"  # RETURN
        )
        
        event_code, result = self.build_event_code(event_data, event_id="65535", entry_offset=0x99)
        
        subroutine_starts = {sub.start_offset: sub.label for sub in event_code.subroutines}
        
        assert 0x99 in subroutine_starts  # Entry point
        assert 0xAE not in subroutine_starts  # Conditional jump target
        # 0xB3 may or may not be a subroutine depending on if it's after a terminal