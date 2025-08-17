# 16982260 - Prillaure

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 708 bytes                     |
| Total Events     | 2                             |
| References Count | 33                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [503](#event-503)     | 0x0001       |    550 |            121 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1256      |        4694 |
|       1 | 0x007E      |         126 |
|       2 | 0xFFFFFFFE  |  4294967294 |
|       3 | 0x0001      |           1 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x0004      |           4 |
|       7 | 0x0005      |           5 |
|       8 | 0x0006      |           6 |
|       9 | 0x1255      |        4693 |
|      10 | 0x007C      |         124 |
|      11 | 0x007A      |         122 |
|      12 | 0x0076      |         118 |
|      13 | 0x006E      |         110 |
|      14 | 0x005E      |          94 |
|      15 | 0x003E      |          62 |
|      16 | 0x1258      |        4696 |
|      17 | 0x0000      |           0 |
|      18 | 0x1259      |        4697 |
|      19 | 0x40000000  |  1073741824 |
|      20 | 0x125A      |        4698 |
|      21 | 0x0020      |          32 |
|      22 | 0x125B      |        4699 |
|      23 | 0x0040      |          64 |
|      24 | 0x125C      |        4700 |
|      25 | 0x0060      |          96 |
|      26 | 0x125D      |        4701 |
|      27 | 0x0080      |         128 |
|      28 | 0x125E      |        4702 |
|      29 | 0x00A0      |         160 |
|      30 | 0x00E9      |         233 |
|      31 | 0x00C8      |         200 |
|      32 | 0x003C      |          60 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 503

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 550 bytes |
| Instructions | 103       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    53 F8 FF FF 7F F8 FF  FF 7F 65 74 6F 6E 1E F0   S........eton..
0010: FF FF 7F 02 08 10 09 10  02 21 00 1D 00 80 23 21  .........!....#!
0020: 00 03 00 00 01 80 02 02  10 02 80 01 35 00 3D 00  ............5.=.
0030: 00 03 80 03 80 02 03 10  02 80 01 44 00 3D 00 00  ...........D.=..
0040: 04 80 03 80 02 04 10 02  80 01 53 00 3D 00 00 05  ..........S.=...
0050: 80 03 80 02 05 10 02 80  01 62 00 3D 00 00 06 80  .........b.=....
0060: 03 80 02 06 10 02 80 01  71 00 3D 00 00 07 80 03  ........q.=.....
0070: 80 02 07 10 02 80 01 80  00 3D 00 00 08 80 03 80  .........=......
0080: 02 00 00 01 80 00 8E 00  1D 00 80 23 21 00 1D 09  ...........#!...
0090: 80 23 02 00 00 0A 80 00  9D 00 01 E4 00 02 00 00  .#..............
00A0: 0B 80 00 A8 00 01 13 01  02 00 00 0C 80 00 B3 00  ................
00B0: 01 42 01 02 00 00 0D 80  00 BE 00 01 71 01 02 00  .B..........q...
00C0: 00 0E 80 00 C9 00 01 A0  01 02 00 00 0F 80 00 D4  ................
00D0: 00 01 CF 01 24 10 80 11  80 00 00 25 02 00 10 03  ....$......%....
00E0: 80 00 0B 01 24 12 80 11  80 02 10 25 02 00 10 11  ....$......%....
00F0: 80 00 FE 00 03 01 10 13  80 21 00 01 08 01 03 01  .........!......
0100: 10 11 80 0E 01 10 00 10  01 FD 01 02 00 10 04 80  ................
0110: 00 3A 01 24 14 80 11 80  03 10 25 02 00 10 11 80  .:.$......%.....
0120: 00 2D 01 03 01 10 13 80  21 00 01 37 01 03 01 10  .-......!..7....
0130: 15 80 0E 01 10 00 10 01  FD 01 02 00 10 05 80 00  ................
0140: 69 01 24 16 80 11 80 04  10 25 02 00 10 11 80 00  i.$......%......
0150: 5C 01 03 01 10 13 80 21  00 01 66 01 03 01 10 17  \......!..f.....
0160: 80 0E 01 10 00 10 01 FD  01 02 00 10 06 80 00 98  ................
0170: 01 24 18 80 11 80 05 10  25 02 00 10 11 80 00 8B  .$......%.......
0180: 01 03 01 10 13 80 21 00  01 95 01 03 01 10 19 80  ......!.........
0190: 0E 01 10 00 10 01 FD 01  02 00 10 07 80 00 C7 01  ................
01A0: 24 1A 80 11 80 06 10 25  02 00 10 11 80 00 BA 01  $......%........
01B0: 03 01 10 13 80 21 00 01  C4 01 03 01 10 1B 80 0E  .....!..........
01C0: 01 10 00 10 01 FD 01 02  00 10 08 80 00 F6 01 24  ...............$
01D0: 1C 80 11 80 07 10 25 02  00 10 11 80 00 E9 01 03  ......%.........
01E0: 01 10 13 80 21 00 01 F3  01 03 01 10 1D 80 0E 01  ....!...........
01F0: 10 00 10 01 FD 01 03 01  10 13 80 21 00 42 43 00  ...........!.BC.
0200: 43 01 02 02 10 11 80 00  10 02 48 1E 80 01 25 02  C.........H...%.
0210: 45 1F 80 F8 FF FF 7F F8  FF FF 7F 66 64 6F 31 11  E..........fdo1.
0220: 80 1C 20 80 30 21 00                              .. .0!.         
```

#### Opcodes

```
  0: 0x0001 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "eton" with entities [EventEntity, EventEntity]
  1: 0x000E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0013 [0x02] IF !(Work_Zone[8] <= Work_Zone[9]) GOTO 0x0021
  3: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=4694*)
    → "The minstrel of melodies is my name,\u0007For a mere 
\u0006 gil I'd recall your past.\u0007But I find that you're lacking in cash or in fame,\u0007So until that time, my kind offer will last.\u007F1\u0000\u0007"
  4: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001F [0x21] END_EVENT
  6: 0x0020 [0x00] END_REQSTACK()
  7: 0x0021 [0x03] ExtData[1]->WorkLocal[0] = 126*
  8: 0x0026 [0x02] IF !(Work_Zone[2] == 4294967294*) GOTO 0x0035
  9: 0x002E [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=1*, condition_work_offset=1*)
 10: 0x0035 [0x02] IF !(Work_Zone[3] == 4294967294*) GOTO 0x0044
 11: 0x003D [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=2*, condition_work_offset=1*)
 12: 0x0044 [0x02] IF !(Work_Zone[4] == 4294967294*) GOTO 0x0053
 13: 0x004C [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=3*, condition_work_offset=1*)
 14: 0x0053 [0x02] IF !(Work_Zone[5] == 4294967294*) GOTO 0x0062
 15: 0x005B [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=4*, condition_work_offset=1*)
 16: 0x0062 [0x02] IF !(Work_Zone[6] == 4294967294*) GOTO 0x0071
 17: 0x006A [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=5*, condition_work_offset=1*)
 18: 0x0071 [0x02] IF !(Work_Zone[7] == 4294967294*) GOTO 0x0080
 19: 0x0079 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=6*, condition_work_offset=1*)
 20: 0x0080 [0x02] IF !(ExtData[1]->WorkLocal[0] == 126*) GOTO 0x008E
 21: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=4694*)
    → "The minstrel of melodies is my name,\u0007For a mere 
\u0006 gil I'd recall your past.\u0007But I find that you're lacking in cash or in fame,\u0007So until that time, my kind offer will last.\u007F1\u0000\u0007"
 22: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x008C [0x21] END_EVENT
 24: 0x008D [0x00] END_REQSTACK()
 25: 0x008E [0x1D] PRINT_EVENT_MESSAGE(message_id=4693*)
    → "The minstrel of melodies is my name,\u0007For a mere 
\u0006 gil I'll recall your past.\u0007Your stories of love, anger, triumph, and shame,\u0007The river of memories runs deep and vast.\u007F1\u0000\u0007"
 26: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0092 [0x02] IF !(ExtData[1]->WorkLocal[0] == 124*) GOTO 0x009D
 28: 0x009A [0x01] GOTO 0x00E4
 29: 0x009D [0x02] IF !(ExtData[1]->WorkLocal[0] == 122*) GOTO 0x00A8
 30: 0x00A5 [0x01] GOTO 0x0113
 31: 0x00A8 [0x02] IF !(ExtData[1]->WorkLocal[0] == 118*) GOTO 0x00B3
 32: 0x00B0 [0x01] GOTO 0x0142
 33: 0x00B3 [0x02] IF !(ExtData[1]->WorkLocal[0] == 110*) GOTO 0x00BE
 34: 0x00BB [0x01] GOTO 0x0171
 35: 0x00BE [0x02] IF !(ExtData[1]->WorkLocal[0] == 94*) GOTO 0x00C9
 36: 0x00C6 [0x01] GOTO 0x01A0
 37: 0x00C9 [0x02] IF !(ExtData[1]->WorkLocal[0] == 62*) GOTO 0x00D4
 38: 0x00D1 [0x01] GOTO 0x01CF
 39: 0x00D4 [0x24] CREATE_DIALOG(message_id=4696*, default_option=0*, option_flags=ExtData[1]->WorkLocal[0])
    → "Which memory will you have recalled?\u0007\u000BNothing.\u0007Aht Urhgan Missions.\u0007Aht Urhgan Quests 1.\u0007Aht Urhgan Quests 2.\u0007Aht Urhgan Quests 3.\u0007Aht Urhgan Quests 4.\u0007Other Quests.\u007F1\u0000\u0007"
 40: 0x00DB [0x25] WAIT_DIALOG_SELECT()
 41: 0x00DC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x010B

SUBROUTINE_00E4:
 42: 0x00E4 [0x24] CREATE_DIALOG(message_id=4697*, default_option=0*, option_flags=Work_Zone[2])
    → "Which memory will you have recalled?\u0007\u000BNothing.\u0007Immortal Sentries(pt.1).\u0007Immortal Sentries(pt.2).\u0007President Salaheem.\u0007Knight of Gold(pt.1).\u0007Knight of Gold(pt.2).\u0007Knight of Gold(pt.3).\u0007Knight of Gold(pt.4).\u0007Knight of Gold(pt.5).\u0007Knight of Gold(pt.6).\u0007Westerly Winds(pt.1).\u0007Westerly Winds(pt.2).\u0007Knight of Gold - Recollection(pt.1).\u0007Knight of Gold - Recollection(pt.2).\u0007Knight of Gold - Recollection(pt.3).\u0007Knight of Gold - Recollection(pt.4).\u0007Knight of Gold - Recollection(pt.5).\u0007Knight of Gold - Recollection(pt.6).\u0007Westerly Winds - Recollection(pt.1).\u0007Westerly Winds - Recollection(pt.2).\u0007Westerly Winds - Recollection(pt.3).\u0007Undersea Scouting.\u0007Imperial Schemes.\u0007Royal Puppeteer.\u0007The Black Coffin.\u0007Guests of the Empire(pt.1).\u0007Guests of the Empire(pt.2).\u0007Passing Glory.\u0007Sweets for the Soul.\u0007Teahouse Tumult.\u0007Shield of Diplomacy.\u0007Foiled Ambition.\u0007Playing the Part.\u007F1\u0000\u0007"
 43: 0x00EB [0x25] WAIT_DIALOG_SELECT()
 44: 0x00EC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00FE
 45: 0x00F4 [0x03] Work_Zone[1] = 1073741824*
 46: 0x00F9 [0x21] END_EVENT
 47: 0x00FA [0x00] END_REQSTACK()

SUBROUTINE_0108:
 48: 0x0108 [0x01] GOTO 0x01FD
 49: 0x010B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x013A

SUBROUTINE_0113:
 50: 0x0113 [0x24] CREATE_DIALOG(message_id=4698*, default_option=0*, option_flags=Work_Zone[3])
    → "Which memory will you have recalled?\u0007\u000BNothing.\u0007Arts and Crafts(pt.1).\u0007Arts and Crafts(pt.2).\u0007Got It All(pt.1).\u0007Got It All(pt.2).\u0007Got It All(pt.3).\u0007Got It All(pt.4).\u0007Got It All(pt.5).\u0007Got It All(pt.6).\u0007Got It All(pt.7).\u0007Get the Picture(pt.1).\u0007Get the Picture(pt.2).\u0007Get the Picture(pt.3).\u0007The Prankster(pt.1).\u0007The Prankster(pt.2).\u0007The Prankster(pt.3).\u0007Delivering the Goods(pt.1).\u0007Delivering the Goods(pt.2).\u0007Delivering the Goods(pt.3).\u0007Vanishing Act(pt.1).\u0007Vanishing Act(pt.2).\u0007Vanishing Act(pt.3).\u0007Vanishing Act(pt.4).\u0007Give Peace a Chance(pt.1).\u0007Give Peace a Chance(pt.2).\u0007Give Peace a Chance(pt.3).\u0007Luck of the Draw(pt.1).\u0007Luck of the Draw(pt.2).\u0007Luck of the Draw(pt.3).\u0007Finding Faults(pt.1).\u0007Finding Faults(pt.2).\u0007Finding Faults(pt.3).\u007F1\u0000\u0007"
 51: 0x011A [0x25] WAIT_DIALOG_SELECT()
 52: 0x011B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x012D
 53: 0x0123 [0x03] Work_Zone[1] = 1073741824*
 54: 0x0128 [0x21] END_EVENT
 55: 0x0129 [0x00] END_REQSTACK()

SUBROUTINE_0137:
 56: 0x0137 [0x01] GOTO 0x01FD
 57: 0x013A [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0169

SUBROUTINE_0142:
 58: 0x0142 [0x24] CREATE_DIALOG(message_id=4699*, default_option=0*, option_flags=Work_Zone[4])
    → "Which memory will you have recalled?\u0007\u000BNothing.\u0007An Empty Vessel(pt.1).\u0007An Empty Vessel(pt.2).\u0007An Empty Vessel(pt.3).\u0007An Empty Vessel(pt.4).\u0007A Taste of Honey(pt.1).\u0007A Taste of Honey(pt.2).\u0007Promotion: Private First Class(pt.1).\u0007Promotion: Private First Class(pt.2).\u0007Promotion: Superior Private(pt.1).\u0007Promotion: Superior Private(pt.2).\u0007Promotion: Superior Private(pt.3).\u0007No Strings Attached(pt.1).\u0007No Strings Attached(pt.2).\u0007No Strings Attached(pt.3).\u0007No Strings Attached(pt.4).\u0007No Strings Attached(pt.5).\u0007The Die Is Cast(pt.1).\u0007The Die Is Cast(pt.2).\u0007The Die Is Cast(pt.3).\u0007Two Horn the Savage(pt.1).\u0007Two Horn the Savage(pt.2).\u0007Two Horn the Savage(pt.3).\u0007Keeping Notes(pt.1).\u0007Keeping Notes(pt.2).\u007F1\u0000\u0007"
 59: 0x0149 [0x25] WAIT_DIALOG_SELECT()
 60: 0x014A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x015C
 61: 0x0152 [0x03] Work_Zone[1] = 1073741824*
 62: 0x0157 [0x21] END_EVENT
 63: 0x0158 [0x00] END_REQSTACK()

SUBROUTINE_0166:
 64: 0x0166 [0x01] GOTO 0x01FD
 65: 0x0169 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0198

SUBROUTINE_0171:
 66: 0x0171 [0x24] CREATE_DIALOG(message_id=4700*, default_option=0*, option_flags=Work_Zone[5])
    → "Which memory will you have recalled?\u0007\u000BNothing.\u0007Olduum(pt.1).\u0007Olduum(pt.2).\u0007Equipped for All Occasions.\u0007Striking a Balance(pt.1).\u0007Striking a Balance(pt.2).\u0007Striking a Balance(pt.3).\u0007Striking a Balance(pt.4).\u0007Striking a Balance(pt.5).\u0007Striking a Balance(pt.6).\u0007Striking a Balance(pt.7).\u0007Beginnings(pt.1).\u0007Beginnings(pt.2).\u0007Omens(pt.1).\u0007Omens(pt.2).\u0007Omens(pt.3).\u0007Omens(pt.4).\u0007Transformations.\u0007The Beast Within(pt.1).\u0007The Beast Within(pt.2).\u0007Promotion: Lance Corporal(pt.1).\u0007Promotion: Lance Corporal(pt.2).\u0007Promotion: Lance Corporal(pt.3).\u0007Promotion: Lance Corporal(pt.4).\u0007Promotion: Lance Corporal(pt.5).\u0007Against All Odds.\u0007Promotion: Corporal(pt.1).\u0007Promotion: Corporal(pt.2).\u0007The Art of War(pt.1).\u0007The Art of War(pt.2).\u0007The Art of War(pt.3).\u007F1\u0000\u0007"
 67: 0x0178 [0x25] WAIT_DIALOG_SELECT()
 68: 0x0179 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x018B
 69: 0x0181 [0x03] Work_Zone[1] = 1073741824*
 70: 0x0186 [0x21] END_EVENT
 71: 0x0187 [0x00] END_REQSTACK()

SUBROUTINE_0195:
 72: 0x0195 [0x01] GOTO 0x01FD
 73: 0x0198 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x01C7

SUBROUTINE_01A0:
 74: 0x01A0 [0x24] CREATE_DIALOG(message_id=4701*, default_option=0*, option_flags=Work_Zone[6])
    → "Which memory will you have recalled?\u0007\u000BNothing.\u0007The Wayward Automaton(pt.1).\u0007The Wayward Automaton(pt.2).\u0007Operation Teatime(pt.1).\u0007Operation Teatime(pt.2).\u0007Puppetmaster Blues(pt.1).\u0007Puppetmaster Blues(pt.2).\u0007Puppetmaster Blues(pt.3).\u0007Moment of Truth(pt.1).\u0007Moment of Truth(pt.2).\u0007Moment of Truth(pt.3).\u0007Moment of Truth(pt.4).\u0007Promotion: Sergeant(pt.1).\u0007Promotion: Sergeant(pt.2).\u0007Promotion: Sergeant(pt.3).\u0007Promotion: Sergeant Major(pt.1).\u0007Promotion: Sergeant Major(pt.2).\u0007Promotion: Sergeant Major(pt.3).\u0007Promotion: Sergeant Major(pt.4).\u0007Led Astray(pt.1).\u0007Led Astray(pt.2).\u0007Led Astray(pt.3).\u0007Led Astray(pt.4).\u0007Led Astray(pt.5).\u0007Led Astray(pt.6).\u0007Saga of the Skyserpent(pt.1).\u0007Saga of the Skyserpent(pt.2).\u007F1\u0000\u0007"
 75: 0x01A7 [0x25] WAIT_DIALOG_SELECT()
 76: 0x01A8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01BA
 77: 0x01B0 [0x03] Work_Zone[1] = 1073741824*
 78: 0x01B5 [0x21] END_EVENT
 79: 0x01B6 [0x00] END_REQSTACK()

SUBROUTINE_01C4:
 80: 0x01C4 [0x01] GOTO 0x01FD
 81: 0x01C7 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x01F6

SUBROUTINE_01CF:
 82: 0x01CF [0x24] CREATE_DIALOG(message_id=4702*, default_option=0*, option_flags=Work_Zone[7])
    → "Which memory will you have recalled?\u0007\u000BNothing.\u0007Nashmeira PR.\u0007Razfahd PR.\u0007Naja PR.\u0007Blue Mage Trailer.\u0007Naja Trailer.\u0007Gordius Trailer.\u0007Volcano Trailer.\u0007Wildcat Reward(pt.1).\u0007Wildcat Reward(pt.2).\u0007Choosing an automaton frame.\u0007The Valoredge X-900.\u0007The Sharpshot Z-500.\u0007The Stormwaker Y-700.\u0007Assault Tutorial.\u0007Magus Attire(pt.1).\u0007Magus Attire(pt.2).\u0007Magus Attire(pt.3).\u0007Magus Attire(pt.4).\u0007Magus Attire(pt.5).\u0007Magus Attire(pt.6).\u0007Puppetry Attire(pt.1).\u0007Puppetry Attire(pt.2).\u0007Salvage.\u0007Wyrmseeker of Areuhat.\u007F1\u0000\u0007"
 83: 0x01D6 [0x25] WAIT_DIALOG_SELECT()
 84: 0x01D7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01E9
 85: 0x01DF [0x03] Work_Zone[1] = 1073741824*
 86: 0x01E4 [0x21] END_EVENT
 87: 0x01E5 [0x00] END_REQSTACK()

SUBROUTINE_01F3:
 88: 0x01F3 [0x01] GOTO 0x01FD
 89: 0x01F6 [0x03] Work_Zone[1] = 1073741824*
 90: 0x01FB [0x21] END_EVENT
 91: 0x01FC [0x00] END_REQSTACK()

SUBROUTINE_01FD:
 92: 0x01FD [0x42] SET_CLI_EVENT_CANCEL_DATA()
 93: 0x01FE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 94: 0x0200 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 95: 0x0202 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0210
 96: 0x020A [0x48] [System] [233*]:
    → "You do not have enough gil.\u007F1\u0000\u0007"
 97: 0x020D [0x01] GOTO 0x0225
 98: 0x0210 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 99: 0x0221 [0x1C] WAIT(60* ticks)
100: 0x0224 [0x30] SET_UCOFF_CONTINUE_ZERO()

SUBROUTINE_0225:
101: 0x0225 [0x21] END_EVENT
102: 0x0226 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00FB [0x01] GOTO 0x0108
# Dead code (unreachable instructions):
     0x012A [0x01] GOTO 0x0137
# Dead code (unreachable instructions):
     0x0159 [0x01] GOTO 0x0166
# Dead code (unreachable instructions):
     0x0188 [0x01] GOTO 0x0195
# Dead code (unreachable instructions):
     0x01B7 [0x01] GOTO 0x01C4
# Dead code (unreachable instructions):
     0x01E6 [0x01] GOTO 0x01F3
```
