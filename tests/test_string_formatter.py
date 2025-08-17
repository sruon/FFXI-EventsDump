import pytest

from parser.string_formatter import format_string


class TestStringFormatter:
    """Test suite for FFXI string formatter using real game strings."""

    def test_basic_text(self):
        """Test plain text passes through unchanged."""
        # Real string from Avandale (7378)
        assert format_string("Oh, a new recruit, are you? That explains it!\x7f1\x00\x07") == "Oh, a new recruit, are you? That explains it!"
        # Real string from Nogelle (7461)
        assert format_string("Well that's too bad. If you find any, though, you know where to bring them!\x7f1\x00\x07") == "Well that's too bad. If you find any, though, you know where to bring them!"

    def test_line_breaks(self):
        """Test \x07 line break handling from real dialogue."""
        # Real string from Avandale (7372) - multiline cutscene text
        text = "\x02P\x00\x03T\x01On this particular day there comes a new\x07adventurer, ready to make a name for\x07\x7f\x05[himself/herself] in San d'Oria.\x7f4\t\x7f1\x00\x07"
        expected = "[Cutscene] On this particular day there comes a new adventurer, ready to make a name for [himself/herself] in San d'Oria."
        assert format_string(text) == expected

    def test_simple_numeric_parameters(self):
        """Test direct numeric parameters \x03-\x06."""
        # Real pattern from synergy messages  
        assert format_string("You need \x03 items") == "You need $3 items"
        assert format_string("Requires \x04 and \x05") == "Requires $4 and $5"
        assert format_string("Level \x06 required") == "Level $6 required"

    def test_numeric_parameter_with_index(self):
        """Test \x0A with index byte from real messages."""
        # Real pattern from synergy messages (string 27)
        assert format_string("\n\x00 \x7f\x12\x01[minute has/minutes have] elapsed.") == "$0 [minute has/minutes have] elapsed."
        # Real pattern from Nogelle (7458)
        assert format_string("You think you could bring \n\x01 chunks?") == "You think you could bring $1 chunks?"

    def test_player_name(self):
        """Test \x08 player name parameter."""
        # Standalone \x08 should be <Player>
        assert format_string("Hello \x08!") == "Hello <Player>!"
        # \x08 with index should be %N  
        assert format_string("You have signed up for \x08\x03.") == "You have signed up for %3."

    def test_entity_parameters(self):
        """Test entity/speaker parameters from real strings."""
        # Real pattern from synergy (strings 22-26) - party member with index
        assert format_string("The synergy furnace is currently in use by \x18\x01.\x7f1\x00\x07") == "The synergy furnace is currently in use by %1."
        assert format_string("The synergy furnace is currently in use by \x18\x03.\x7f1\x00\x07") == "The synergy furnace is currently in use by %3."
        # \x09) pattern for $0
        assert format_string("You obtain \x09)!") == "You obtain $0!"

    def test_selection_dialog(self):
        """Test \x0B selection dialog markers from real dialogue."""
        # Real string from Nogelle (7459)
        assert format_string('What do you say? \x07\x0bSure.\x07Not today.\x7f1\x00\x07') == 'What do you say? [Sure./Not today.]'
        # Real string from synergy (17)
        assert format_string('Claim usage of the furnace?\x07\x0bYes.\x07No.\x7f1\x00\x07') == 'Claim usage of the furnace? [Yes./No.]'
        # Real string from Avandale (7398) - multiple options
        text = "Something you'd like to know?\x07\x0bNothing, actually.\x07I'd like to get out of the city.\x07I'd like to do some shopping.\x07Tell me more about adventuring.\x7f1\x00\x07"
        expected = "Something you'd like to know? [Nothing, actually./I'd like to get out of the city./I'd like to do some shopping./Tell me more about adventuring.]"
        assert format_string(text) == expected

    def test_quotes(self):
        """Test quote markers \x07\x32 and \x07\x33 from real strings."""
        # Real strings from Bastok Markets (3-13) - Super Kupower messages
        assert format_string('\x072Thrifty Transit\x073!') == '"Thrifty Transit"!'
        assert format_string('\x072Martial Master\x073!') == '"Martial Master"!'
        assert format_string('\x072Blood of the Vampyr\x073!') == '"Blood of the Vampyr"!'
        
    def test_ordinals_not_quotes(self):
        """Test that ordinals like 2nd, 3rd are not converted to quotes"""
        assert format_string("1st: Bastok\x072nd: San d'Oria\x073rd: Windurst") == "1st: Bastok 2nd: San d'Oria 3rd: Windurst"

    def test_item_parameter(self):
        """Test \x19 item parameter with index."""
        assert format_string("You obtain \x19\x01!") == "You obtain %1!"
        assert format_string("Found \x19\x00") == "Found %0"

    def test_key_item_parameter(self):
        """Test \x1A key item parameter with index."""
        assert format_string("Obtained key item: \x1A\x02") == "Obtained key item: %2"

    def test_weather_parameter(self):
        """Test \x17 weather parameter."""
        assert format_string("Weather is \x17") == "Weather is %"

    def test_color_codes(self):
        """Test color code sequences are removed from real strings."""
        # Real strings from Bastok Markets (1) - colored text
        text = "\x1f!The complete set of mog tablets has been restored to Ru'Lude Gardens!\x07The ancient magic of King Kupofried permeates the air to instill adventurers in this area with its Super Kupowers!\x00\x07"
        expected = "The complete set of mog tablets has been restored to Ru'Lude Gardens! The ancient magic of King Kupofried permeates the air to instill adventurers in this area with its Super Kupowers!"
        assert format_string(text) == expected

    def test_gender_specific_text(self):
        """Test gender markers with bracketed text from real dialogue."""
        # Real string from Avandale (7372) - cutscene with gender markers
        text = "ready to make a name for\x07\x7f\x05[himself/herself] in San d'Oria."
        expected = "ready to make a name for [himself/herself] in San d'Oria."
        assert format_string(text) == expected
        # Real string from Avandale (7379)
        text = "chastise someone on \x7f\x05[his/her] first day."
        expected = "chastise someone on [his/her] first day."
        assert format_string(text) == expected

    def test_cutscene_marker(self):
        """Test cutscene marker at beginning from real strings."""
        # Real string from Avandale (7372)
        text = "\x02P\x00\x03T\x01On this particular day there comes a new\x07adventurer"
        expected = "[Cutscene] On this particular day there comes a new adventurer"
        assert format_string(text) == expected

    def test_complex_parameter_patterns(self):
        """Test \x01\x05[char]\x02 patterns from real game strings."""
        # Real string from Nogelle (7457, 7460, 7462) - item parameter
        # The % character before \x02 gets interpreted as $0 (index from the multi-byte sequence)
        text = "You know... Our beans really need some \x01\x05%\x02\x00\x00\x00. It's the secret"
        expected = "You know... Our beans really need some $0. It's the secret"
        assert format_string(text) == expected
        
        # Real string from synergy (19) - timer parameter
        # The \x7f\x00\x01\x01\x05[char]\x02\x00\x00\x00 pattern outputs just the character (icon/symbol)
        text = "\x7f\x00\x01\x01\x053\x02\x00\x00\x00 set. You now have claim"
        expected = "3 set. You now have claim"
        assert format_string(text) == expected
        
        # Real string from synergy (29, 37) - key item parameter
        text = "Possession of \x01\x056\x02\x00\x00\x00 is required"
        expected = "Possession of $6 is required"
        assert format_string(text) == expected

    def test_plural_markers(self):
        """Test plural markers from real synergy strings."""
        # Real string from synergy (19) - plural marker for minutes
        text = "within \n\x01 minute\x7f\x12\x01[/s].\x7f1\x00\x07"
        expected = "within $1 minute[/s]."
        assert format_string(text) == expected
        
        # Real string from synergy (27) - complex plural
        text = "\n\x00 \x7f\x12\x01[minute has/minutes have] elapsed."
        expected = "$0 [minute has/minutes have] elapsed."
        assert format_string(text) == expected

    def test_null_bytes(self):
        """Test null bytes are handled properly."""
        assert format_string("Hello\x00world") == "Hello world"
        assert format_string("Test\x00\x00message") == "Test message"

    def test_element_selection(self):
        """Test element selection from real synergy strings."""
        # Real string from synergy (41) - craft skill selection  
        # \x0c is not a recognized parameter byte, so it gets skipped
        text = "That recipe is impossible at your \x0c\x00[fishing/woodworking/smithing/goldsmithing/clothcraft/leathercraft/bonecraft/alchemy/cooking] skill level.\x7f1\x00\x07"
        expected = "That recipe is impossible at your [fishing/woodworking/smithing/goldsmithing/clothcraft/leathercraft/bonecraft/alchemy/cooking] skill level."
        assert format_string(text) == expected
        
    def test_complex_real_strings(self):
        """Test complex real-world examples from the game."""
        # Real string from synergy (38) - complex with multiple patterns
        # The \x7f\x00 pattern at start of parameter section and % character gets output as standalone %
        text = "Unable to proceed.\x07\x7f\x00\x01\x01\x05%\x02\x00\x00\x00 are not suitable for use as synergy ingredients.\x7f1\x00\x07"
        expected = "Unable to proceed. % are not suitable for use as synergy ingredients."
        assert format_string(text) == expected
        
        # Real string from Avandale (7406) - multiple selection dialog
        text = "What would you like to know? \x07\x0bHelping people.\x07Hunting monsters.\x07Making easy money.\x07Working for my country.\x7f1\x00\x07"
        expected = "What would you like to know? [Helping people./Hunting monsters./Making easy money./Working for my country.]"
        assert format_string(text) == expected

    def test_terminal_sequences(self):
        """Test terminal sequences from real strings."""
        # Most real strings end with \x7f1\x00\x07 or similar
        assert format_string("Test message.\x7f1\x00\x07") == "Test message."
        assert format_string("Another test.\x7f4\t\x7f1\x00\x07") == "Another test."
        assert format_string("Final test.\x00\x07") == "Final test."


if __name__ == "__main__":
    pytest.main([__file__, "-v"])