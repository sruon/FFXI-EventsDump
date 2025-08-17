# 17171008 - Rongo-Nango

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 372 bytes                       |
| Total Events     | 2                               |
| References Count | 10                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [501](#event-501)     | 0x0001       |    304 |             75 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1E15      |        7701 |
|       2 | 0x0000      |           0 |
|       3 | 0x1E17      |        7703 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x1E16      |        7702 |
|       7 | 0x1E19      |        7705 |
|       8 | 0x1E18      |        7704 |
|       9 | 0x001D      |          29 |

## String References

- **7701**: Huh!? Wha--!? Whe--!? I'm sorry, I haven't had a person speak to me in so long. You caughtaru me at unawares.
- **7702**: Awww, you reek of parchmentaru... You must be from Windurst. Please, get away! My father told me never to trust a Windurstian.
- **7703**: Hm? Y-you want me to help you? I guess I could do that... But you have to promise me one thing. That you won't tease my friend, here. Got itaru?
- **7704**: Thank you... That should make my friend happy-wappy.
- **7705**: By the way, do you know the origin of this name, "Lungo-Nango"? It comes from the hero who carried Windurst to her greatest glory.

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

### Event 501

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 304 bytes |
| Instructions | 75        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 03 01 00 03  10 03 02 00 04 10 03 03    .B............
0010: 00 05 10 02 02 10 00 80  00 22 00 1D 01 80 23 01  ........."....#.
0020: 2D 01 02 03 00 00 80 00  7F 00 02 01 00 02 80 80  -...............
0030: 45 00 6E F8 FF FF 7F 02  80 99 F8 FF FF 7F 1D 01  E.n.............
0040: 80 23 01 7C 00 02 01 00  00 80 80 59 00 03 02 10  .#.|.......Y....
0050: 02 80 1D 03 80 23 01 7C  00 02 01 00 04 80 80 6D  .....#.|.......m
0060: 00 03 02 10 00 80 1D 03  80 23 01 7C 00 02 01 00  .........#.|....
0070: 05 80 80 7C 00 1D 06 80  23 01 7C 00 01 2D 01 02  ...|....#.|..-..
0080: 03 00 04 80 00 2D 01 02  01 00 02 80 80 A2 00 6E  .....-.........n
0090: F8 FF FF 7F 02 80 99 F8  FF FF 7F 1D 01 80 23 01  ..............#.
00A0: 2D 01 02 01 00 00 80 80  E0 00 02 02 00 00 80 00  -...............
00B0: B9 00 1D 07 80 23 01 DD  00 02 02 00 04 80 00 CD  .....#..........
00C0: 00 03 02 10 02 80 1D 08  80 23 01 DD 00 6E F8 FF  .........#...n..
00D0: FF 7F 02 80 99 F8 FF FF  7F 1D 01 80 23 01 2D 01  ............#.-.
00E0: 02 01 00 04 80 80 1E 01  02 02 00 00 80 00 F7 00  ................
00F0: 1D 07 80 23 01 1B 01 02  02 00 04 80 00 0B 01 03  ...#............
0100: 02 10 00 80 1D 08 80 23  01 1B 01 6E F8 FF FF 7F  .......#...n....
0110: 09 80 99 F8 FF FF 7F 1D  01 80 23 01 2D 01 02 01  ..........#.-...
0120: 00 05 80 80 2D 01 1D 06  80 23 01 2D 01 20 00 21  ....-....#.-. .!
0130: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  3: 0x0009 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  4: 0x000E [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  5: 0x0013 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0022
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7701*)
    → "Huh!? Wha--!? Whe--!? I'm sorry, I haven't had a person speak to me in so long. You caughtaru me at unawares."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x01] GOTO 0x012D
  9: 0x0022 [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x007F
 10: 0x002A [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0045
 11: 0x0032 [0x6E] EventEntity uses emote 0*
 12: 0x0039 [0x99] Wait for EventEntity animation to complete
 13: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=7701*)
    → "Huh!? Wha--!? Whe--!? I'm sorry, I haven't had a person speak to me in so long. You caughtaru me at unawares."
 14: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0042 [0x01] GOTO 0x007C
 16: 0x0045 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0059
 17: 0x004D [0x03] Work_Zone[2] = 0*
 18: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=7703*)
    → "Hm? Y-you want me to help you? I guess I could do that... But you have to promise me one thing. That you won't tease my friend, here. Got itaru?"
 19: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0056 [0x01] GOTO 0x007C
 21: 0x0059 [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x006D
 22: 0x0061 [0x03] Work_Zone[2] = 1*
 23: 0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=7703*)
    → "Hm? Y-you want me to help you? I guess I could do that... But you have to promise me one thing. That you won't tease my friend, here. Got itaru?"
 24: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x006A [0x01] GOTO 0x007C
 26: 0x006D [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x007C
 27: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=7702*)
    → "Awww, you reek of parchmentaru... You must be from Windurst. Please, get away! My father told me never to trust a Windurstian."
 28: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0079 [0x01] GOTO 0x007C

SUBROUTINE_007C:
 30: 0x007C [0x01] GOTO 0x012D
 31: 0x007F [0x02] IF !(ExtData[1]->WorkLocal[3] == 2*) GOTO 0x012D
 32: 0x0087 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00A2
 33: 0x008F [0x6E] EventEntity uses emote 0*
 34: 0x0096 [0x99] Wait for EventEntity animation to complete
 35: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=7701*)
    → "Huh!? Wha--!? Whe--!? I'm sorry, I haven't had a person speak to me in so long. You caughtaru me at unawares."
 36: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x009F [0x01] GOTO 0x012D
 38: 0x00A2 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x00E0
 39: 0x00AA [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00B9
 40: 0x00B2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7705*)
    → "By the way, do you know the origin of this name, "Lungo-Nango"? It comes from the hero who carried Windurst to her greatest glory."
 41: 0x00B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x00B6 [0x01] GOTO 0x00DD
 43: 0x00B9 [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x00CD
 44: 0x00C1 [0x03] Work_Zone[2] = 0*
 45: 0x00C6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7704*)
    → "Thank you... That should make my friend happy-wappy."
 46: 0x00C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x00CA [0x01] GOTO 0x00DD
 48: 0x00CD [0x6E] EventEntity uses emote 0*
 49: 0x00D4 [0x99] Wait for EventEntity animation to complete
 50: 0x00D9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7701*)
    → "Huh!? Wha--!? Whe--!? I'm sorry, I haven't had a person speak to me in so long. You caughtaru me at unawares."
 51: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00DD:
 52: 0x00DD [0x01] GOTO 0x012D
 53: 0x00E0 [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x011E
 54: 0x00E8 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00F7
 55: 0x00F0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7705*)
    → "By the way, do you know the origin of this name, "Lungo-Nango"? It comes from the hero who carried Windurst to her greatest glory."
 56: 0x00F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x00F4 [0x01] GOTO 0x011B
 58: 0x00F7 [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x010B
 59: 0x00FF [0x03] Work_Zone[2] = 1*
 60: 0x0104 [0x1D] PRINT_EVENT_MESSAGE(message_id=7704*)
    → "Thank you... That should make my friend happy-wappy."
 61: 0x0107 [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x0108 [0x01] GOTO 0x011B
 63: 0x010B [0x6E] EventEntity uses emote 29*
 64: 0x0112 [0x99] Wait for EventEntity animation to complete
 65: 0x0117 [0x1D] PRINT_EVENT_MESSAGE(message_id=7701*)
    → "Huh!? Wha--!? Whe--!? I'm sorry, I haven't had a person speak to me in so long. You caughtaru me at unawares."
 66: 0x011A [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_011B:
 67: 0x011B [0x01] GOTO 0x012D
 68: 0x011E [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x012D
 69: 0x0126 [0x1D] PRINT_EVENT_MESSAGE(message_id=7702*)
    → "Awww, you reek of parchmentaru... You must be from Windurst. Please, get away! My father told me never to trust a Windurstian."
 70: 0x0129 [0x23] WAIT_FOR_DIALOG_INTERACTION
 71: 0x012A [0x01] GOTO 0x012D

SUBROUTINE_012D:
 72: 0x012D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 73: 0x012F [0x21] END_EVENT
 74: 0x0130 [0x00] END_REQSTACK()
```
