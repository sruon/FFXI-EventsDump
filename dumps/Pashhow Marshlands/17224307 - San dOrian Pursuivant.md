# 17224307 - San dOrian Pursuivant

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Pashhow Marshlands (ID: 109) |
| Block Size       | 304 bytes                    |
| Total Events     | 2                            |
| References Count | 15                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      6 |              2 |
| [19](#event-19)       | 0x0006       |    211 |             55 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0002      |           2 |
|       2 | 0x1D8B      |        7563 |
|       3 | 0x01F4      |         500 |
|       4 | 0x1D8E      |        7566 |
|       5 | 0x1D8F      |        7567 |
|       6 | 0x0001      |           1 |
|       7 | 0x1D90      |        7568 |
|       8 | 0x1D91      |        7569 |
|       9 | 0x1D92      |        7570 |
|      10 | 0x1D93      |        7571 |
|      11 | 0x1D94      |        7572 |
|      12 | 0x1D95      |        7573 |
|      13 | 0x1D8C      |        7564 |
|      14 | 0x1D8D      |        7565 |

## String References

- **7563**: This is our force's camp. Returning to the camp after falling in battle will allow for a quicker return to the battlefield. It can also help you escape an enemy that may be waiting for your recovery.
- **7564**: This is the camp of the [San d'Orian/Bastokan/Windurstian] forces. There is no rule preventing members of the opposition from entering this area. However, such actions may reflect on the sportsmanship of the adventurers that do so.
- **7565**: I am the assigned Pursuivant of the [San d'Orian/Bastokan/Windurstian] forces. It is my duty to remain at this camp and aid players when necessary.
- **7566**: If the rules still seem a bit difficult, I could provide you with $6. This will give you useful advice while participating, as well as provide you with information on upcoming matches.
- **7567**: Would you like one? [Yes./No.]
- **7568**: This device works like a linkshell and will allow you to hear my advice during the course of the match. All you have to do is follow what I say, and you'll have no problems.
- **7569**: Well, if you ever change your mind, please let me know.
- **7570**: Are you still using the $3? If not, I ask that you return it. There are many novice adventurers that could use one, and we are in short supply.
- **7571**: Would you like to return it? [Yes./No.]
- **7572**: Ha ha! Now that you think you've got what it takes, get out there on the battlefield and create some havoc!
- **7573**: I see. Well, I can't force you to return it... Good luck, citizen!

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 03 01 00 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0000 [0x03] ExtData[1]->WorkLocal[1] = 0*
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0006    |
| Data Size    | 211 bytes |
| Instructions | 55        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   06 01  10 03 00 00 02 10 03 03        ..........
0010: 00 05 10 02 03 10 01 00  00 D8 00 1E F0 FF FF 7F  ................
0020: 6F 70 08 00 00 01 80 02  00 00 01 00 00 A4 00 1D  op..............
0030: 02 80 23 03 02 10 03 80  02 03 00 00 80 00 72 00  ..#...........r.
0040: 1D 04 80 23 24 05 80 06  80 00 80 25 02 00 10 00  ...#$......%....
0050: 80 00 60 00 1D 07 80 23  03 01 10 06 80 01 6F 00  ..`....#......o.
0060: 02 00 10 06 80 00 6F 00  1D 08 80 23 01 6F 00 01  ......o....#.o..
0070: A1 00 1D 09 80 23 24 0A  80 06 80 00 80 25 02 00  .....#$......%..
0080: 10 00 80 00 92 00 1D 0B  80 23 03 01 10 01 80 01  .........#......
0090: A1 00 02 00 10 06 80 00  A1 00 1D 0C 80 23 01 A1  .............#..
00A0: 00 01 D7 00 06 02 00 02  00 00 00 80 04 BA 00 02  ................
00B0: 00 00 01 80 05 BA 00 05  02 00 02 02 00 06 80 00  ................
00C0: CE 00 03 02 10 01 00 1D  0D 80 23 01 D7 00 03 02  ..........#.....
00D0: 10 01 00 1D 0E 80 23 21  00                       ......#!.       
```

#### Opcodes

```
  0: 0x0006 [0x06] Work_Zone[1] = 0
  1: 0x0009 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  2: 0x000E [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  3: 0x0013 [0x02] IF !(Work_Zone[3] == ExtData[1]->WorkLocal[1]) GOTO 0x00D8
  4: 0x001B [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0020 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0021 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0022 [0x08] ExtData[1]->WorkLocal[0] -= 2*
  8: 0x0027 [0x02] IF !(ExtData[1]->WorkLocal[0] == ExtData[1]->WorkLocal[1]) GOTO 0x00A4
  9: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=7563*)
    → "This is our force's camp. Returning to the camp after falling in battle will allow for a quicker return to the battlefield. It can also help you escape an enemy that may be waiting for your recovery."
 10: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0033 [0x03] Work_Zone[2] = 500*
 12: 0x0038 [0x02] IF !(ExtData[1]->WorkLocal[3] == 0*) GOTO 0x0072
 13: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=7566*)
    → "If the rules still seem a bit difficult, I could provide you with $6. This will give you useful advice while participating, as well as provide you with information on upcoming matches."
 14: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0044 [0x24] CREATE_DIALOG(message_id=7567*, default_option=1*, option_flags=0*)
    → "Would you like one? [Yes./No.]"
 16: 0x004B [0x25] WAIT_DIALOG_SELECT()
 17: 0x004C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0060
 18: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=7568*)
    → "This device works like a linkshell and will allow you to hear my advice during the course of the match. All you have to do is follow what I say, and you'll have no problems."
 19: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0058 [0x03] Work_Zone[1] = 1*
 21: 0x005D [0x01] GOTO 0x006F
 22: 0x0060 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x006F
 23: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=7569*)
    → "Well, if you ever change your mind, please let me know."
 24: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x006C [0x01] GOTO 0x006F

SUBROUTINE_006F:
 26: 0x006F [0x01] GOTO 0x00A1
 27: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=7570*)
    → "Are you still using the $3? If not, I ask that you return it. There are many novice adventurers that could use one, and we are in short supply."
 28: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0076 [0x24] CREATE_DIALOG(message_id=7571*, default_option=1*, option_flags=0*)
    → "Would you like to return it? [Yes./No.]"
 30: 0x007D [0x25] WAIT_DIALOG_SELECT()
 31: 0x007E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0092
 32: 0x0086 [0x1D] PRINT_EVENT_MESSAGE(message_id=7572*)
    → "Ha ha! Now that you think you've got what it takes, get out there on the battlefield and create some havoc!"
 33: 0x0089 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x008A [0x03] Work_Zone[1] = 2*
 35: 0x008F [0x01] GOTO 0x00A1
 36: 0x0092 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A1
 37: 0x009A [0x1D] PRINT_EVENT_MESSAGE(message_id=7573*)
    → "I see. Well, I can't force you to return it... Good luck, citizen!"
 38: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x009E [0x01] GOTO 0x00A1

SUBROUTINE_00A1:
 40: 0x00A1 [0x01] GOTO 0x00D7
 41: 0x00A4 [0x06] ExtData[1]->WorkLocal[2] = 0
 42: 0x00A7 [0x02] IF !(ExtData[1]->WorkLocal[0] < 0*) GOTO 0x00BA
 43: 0x00AF [0x02] IF !(ExtData[1]->WorkLocal[0] > 2*) GOTO 0x00BA
 44: 0x00B7 [0x05] ExtData[1]->WorkLocal[2] = 1
 45: 0x00BA [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00CE
 46: 0x00C2 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 47: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7564*)
    → "This is the camp of the [San d'Orian/Bastokan/Windurstian] forces. There is no rule preventing members of the opposition from entering this area. However, such actions may reflect on the sportsmanship of the adventurers that do so."
 48: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x00CB [0x01] GOTO 0x00D7
 50: 0x00CE [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 51: 0x00D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7565*)
    → "I am the assigned Pursuivant of the [San d'Orian/Bastokan/Windurstian] forces. It is my duty to remain at this camp and aid players when necessary."
 52: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00D7:
 53: 0x00D7 [0x21] END_EVENT
 54: 0x00D8 [0x00] END_REQSTACK()
```
