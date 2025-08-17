# 17105255 - Rongo-Nango

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 324 bytes                        |
| Total Events     | 2                                |
| References Count | 10                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [507](#event-507)     | 0x0001       |    256 |             67 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x2C24      |       11300 |
|       2 | 0x0000      |           0 |
|       3 | 0x2C27      |       11303 |
|       4 | 0x0002      |           2 |
|       5 | 0x2C26      |       11302 |
|       6 | 0x0003      |           3 |
|       7 | 0x2C25      |       11301 |
|       8 | 0x2C29      |       11305 |
|       9 | 0x2C28      |       11304 |

## String References

- **11300**: Please, don't come any closer! I was raised by beasts you see, and, well...it's the smell. I feel saturated by it. Iron, perfumes, spices... I can taste your stink and every time I do I feel I have somehow been infected by it.
- **11301**: Awww, you reek of parchmentaru... You must be from Windurst. Please, get away! My father told me never to trust a Windurstian.
- **11302**: Hm? Y-you want me to help you? I guess I could do that... But you have to promise me one thing. That you won't tease my friend, here. Got itaru?
- **11303**: Alright, let's get a move on, then. My friend is getting tired of being told to "stay."
- **11304**: Thank you... That should make my friend happy-wappy.
- **11305**: By the way, do you know the origin of this name, "Lungo-Nango"? It comes from the hero who carried Windurst to her greatest glory.

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

### Event 507

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 256 bytes |
| Instructions | 67        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 03 01 00 03  10 03 02 00 04 10 03 03    .B............
0010: 00 05 10 02 02 10 00 80  00 22 00 1D 01 80 23 01  ........."....#.
0020: FD 00 02 03 00 00 80 00  73 00 02 01 00 02 80 80  ........s.......
0030: 39 00 1D 01 80 23 01 70  00 02 01 00 00 80 80 4D  9....#.p.......M
0040: 00 03 02 10 02 80 1D 03  80 23 01 70 00 02 01 00  .........#.p....
0050: 04 80 80 61 00 03 02 10  00 80 1D 05 80 23 01 70  ...a.........#.p
0060: 00 02 01 00 06 80 80 70  00 1D 07 80 23 01 70 00  .......p....#.p.
0070: 01 FD 00 02 03 00 04 80  00 FD 00 02 01 00 02 80  ................
0080: 80 8A 00 1D 01 80 23 01  FD 00 02 01 00 00 80 80  ......#.........
0090: BC 00 02 02 00 00 80 00  A1 00 1D 08 80 23 01 B9  .............#..
00A0: 00 02 02 00 04 80 00 B5  00 03 02 10 02 80 1D 09  ................
00B0: 80 23 01 B9 00 1D 01 80  23 01 FD 00 02 01 00 04  .#......#.......
00C0: 80 80 EE 00 02 02 00 00  80 00 D3 00 1D 08 80 23  ...............#
00D0: 01 EB 00 02 02 00 04 80  00 E7 00 03 02 10 00 80  ................
00E0: 1D 09 80 23 01 EB 00 1D  01 80 23 01 FD 00 02 01  ...#......#.....
00F0: 00 06 80 80 FD 00 1D 07  80 23 01 FD 00 20 00 21  .........#... .!
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  3: 0x0009 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  4: 0x000E [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  5: 0x0013 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0022
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=11300*)
    → "Please, don't come any closer! I was raised by beasts you see, and, well...it's the smell. I feel saturated by it. Iron, perfumes, spices... I can taste your stink and every time I do I feel I have somehow been infected by it."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x01] GOTO 0x00FD
  9: 0x0022 [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x0073
 10: 0x002A [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0039
 11: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=11300*)
    → "Please, don't come any closer! I was raised by beasts you see, and, well...it's the smell. I feel saturated by it. Iron, perfumes, spices... I can taste your stink and every time I do I feel I have somehow been infected by it."
 12: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0036 [0x01] GOTO 0x0070
 14: 0x0039 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x004D
 15: 0x0041 [0x03] Work_Zone[2] = 0*
 16: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=11303*)
    → "Alright, let's get a move on, then. My friend is getting tired of being told to "stay.""
 17: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x004A [0x01] GOTO 0x0070
 19: 0x004D [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x0061
 20: 0x0055 [0x03] Work_Zone[2] = 1*
 21: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=11302*)
    → "Hm? Y-you want me to help you? I guess I could do that... But you have to promise me one thing. That you won't tease my friend, here. Got itaru?"
 22: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x005E [0x01] GOTO 0x0070
 24: 0x0061 [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x0070
 25: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=11301*)
    → "Awww, you reek of parchmentaru... You must be from Windurst. Please, get away! My father told me never to trust a Windurstian."
 26: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x006D [0x01] GOTO 0x0070

SUBROUTINE_0070:
 28: 0x0070 [0x01] GOTO 0x00FD
 29: 0x0073 [0x02] IF !(ExtData[1]->WorkLocal[3] == 2*) GOTO 0x00FD
 30: 0x007B [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x008A
 31: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=11300*)
    → "Please, don't come any closer! I was raised by beasts you see, and, well...it's the smell. I feel saturated by it. Iron, perfumes, spices... I can taste your stink and every time I do I feel I have somehow been infected by it."
 32: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0087 [0x01] GOTO 0x00FD
 34: 0x008A [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x00BC
 35: 0x0092 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00A1
 36: 0x009A [0x1D] PRINT_EVENT_MESSAGE(message_id=11305*)
    → "By the way, do you know the origin of this name, "Lungo-Nango"? It comes from the hero who carried Windurst to her greatest glory."
 37: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x009E [0x01] GOTO 0x00B9
 39: 0x00A1 [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x00B5
 40: 0x00A9 [0x03] Work_Zone[2] = 0*
 41: 0x00AE [0x1D] PRINT_EVENT_MESSAGE(message_id=11304*)
    → "Thank you... That should make my friend happy-wappy."
 42: 0x00B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x00B2 [0x01] GOTO 0x00B9
 44: 0x00B5 [0x1D] PRINT_EVENT_MESSAGE(message_id=11300*)
    → "Please, don't come any closer! I was raised by beasts you see, and, well...it's the smell. I feel saturated by it. Iron, perfumes, spices... I can taste your stink and every time I do I feel I have somehow been infected by it."
 45: 0x00B8 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00B9:
 46: 0x00B9 [0x01] GOTO 0x00FD
 47: 0x00BC [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x00EE
 48: 0x00C4 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00D3
 49: 0x00CC [0x1D] PRINT_EVENT_MESSAGE(message_id=11305*)
    → "By the way, do you know the origin of this name, "Lungo-Nango"? It comes from the hero who carried Windurst to her greatest glory."
 50: 0x00CF [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x00D0 [0x01] GOTO 0x00EB
 52: 0x00D3 [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x00E7
 53: 0x00DB [0x03] Work_Zone[2] = 1*
 54: 0x00E0 [0x1D] PRINT_EVENT_MESSAGE(message_id=11304*)
    → "Thank you... That should make my friend happy-wappy."
 55: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x00E4 [0x01] GOTO 0x00EB
 57: 0x00E7 [0x1D] PRINT_EVENT_MESSAGE(message_id=11300*)
    → "Please, don't come any closer! I was raised by beasts you see, and, well...it's the smell. I feel saturated by it. Iron, perfumes, spices... I can taste your stink and every time I do I feel I have somehow been infected by it."
 58: 0x00EA [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00EB:
 59: 0x00EB [0x01] GOTO 0x00FD
 60: 0x00EE [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x00FD
 61: 0x00F6 [0x1D] PRINT_EVENT_MESSAGE(message_id=11301*)
    → "Awww, you reek of parchmentaru... You must be from Windurst. Please, get away! My father told me never to trust a Windurstian."
 62: 0x00F9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x00FA [0x01] GOTO 0x00FD

SUBROUTINE_00FD:
 64: 0x00FD [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 65: 0x00FF [0x21] END_EVENT
 66: 0x0100 [0x00] END_REQSTACK()
```
