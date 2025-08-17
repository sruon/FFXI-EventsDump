# 17105259 - Duskraven

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 384 bytes                        |
| Total Events     | 2                                |
| References Count | 9                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [511](#event-511)     | 0x0001       |    322 |             85 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x2BEF      |       11247 |
|       2 | 0x0000      |           0 |
|       3 | 0x2BF0      |       11248 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x2BF3      |       11251 |
|       7 | 0x2BF1      |       11249 |
|       8 | 0x2BF2      |       11250 |

## String References

- **11247**: I sense something...otherworldly about you, traveler. But appearances can oft be misleading, nay?
- **11248**: It may hap the secrets I seek lie with [the Crimson Lion/the Republic/the Federation]...
- **11249**: Ah, so your nation requests my services... I shall consider your proposal...
- **11250**: I lack the patience to deal with those who do not kneel to the raven...
- **11251**: I have heard rumor that the lord of the beastmen sits upon an hoary throne in the frozen north. Do you believe he would entertain a raven?

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

### Event 511

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 322 bytes |
| Instructions | 85        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 20 01 42 1E  F0 FF FF 7F 03 01 00 03    .B .B.........
0010: 10 03 02 00 04 10 03 03  00 05 10 02 02 10 00 80  ................
0020: 00 2A 00 1D 01 80 23 01  3F 01 02 03 00 02 80 80  .*....#.?.......
0030: 39 00 1D 01 80 23 01 3F  01 02 03 00 00 80 80 BC  9....#.?........
0040: 00 02 01 00 02 80 80 50  00 1D 01 80 23 01 B9 00  .......P....#...
0050: 02 01 00 00 80 80 73 00  02 02 00 00 80 00 6C 00  ......s.......l.
0060: 03 02 10 02 80 1D 03 80  23 01 70 00 1D 01 80 23  ........#.p....#
0070: 01 B9 00 02 01 00 04 80  80 96 00 02 02 00 04 80  ................
0080: 00 8F 00 03 02 10 00 80  1D 03 80 23 01 93 00 1D  ...........#....
0090: 01 80 23 01 B9 00 02 01  00 05 80 80 B9 00 02 02  ..#.............
00A0: 00 05 80 00 B2 00 03 02  10 04 80 1D 03 80 23 01  ..............#.
00B0: B6 00 1D 01 80 23 01 B9  00 01 3F 01 02 03 00 04  .....#....?.....
00C0: 80 80 3F 01 02 01 00 02  80 80 D3 00 1D 01 80 23  ..?............#
00D0: 01 3C 01 02 01 00 00 80  80 F6 00 02 02 00 00 80  .<..............
00E0: 00 EF 00 03 02 10 02 80  1D 06 80 23 01 F3 00 1D  ...........#....
00F0: 07 80 23 01 3C 01 02 01  00 04 80 80 19 01 02 02  ..#.<...........
0100: 00 04 80 00 12 01 03 02  10 00 80 1D 06 80 23 01  ..............#.
0110: 16 01 1D 08 80 23 01 3C  01 02 01 00 05 80 80 3C  .....#.<.......<
0120: 01 02 02 00 05 80 00 35  01 03 02 10 04 80 1D 06  .......5........
0130: 80 23 01 39 01 1D 07 80  23 01 3C 01 01 3F 01 20  .#.9....#.<..?. 
0140: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0006 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0007 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x000C [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  6: 0x0011 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  7: 0x0016 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  8: 0x001B [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x002A
  9: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=11247*)
    → "I sense something...otherworldly about you, traveler. But appearances can oft be misleading, nay?"
 10: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0027 [0x01] GOTO 0x013F
 12: 0x002A [0x02] IF !(ExtData[1]->WorkLocal[3] == 0*) GOTO 0x0039
 13: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=11247*)
    → "I sense something...otherworldly about you, traveler. But appearances can oft be misleading, nay?"
 14: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0036 [0x01] GOTO 0x013F
 16: 0x0039 [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x00BC
 17: 0x0041 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0050
 18: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=11247*)
    → "I sense something...otherworldly about you, traveler. But appearances can oft be misleading, nay?"
 19: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x004D [0x01] GOTO 0x00B9
 21: 0x0050 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0073
 22: 0x0058 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x006C
 23: 0x0060 [0x03] Work_Zone[2] = 0*
 24: 0x0065 [0x1D] PRINT_EVENT_MESSAGE(message_id=11248*)
    → "It may hap the secrets I seek lie with [the Crimson Lion/the Republic/the Federation]..."
 25: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0069 [0x01] GOTO 0x0070
 27: 0x006C [0x1D] PRINT_EVENT_MESSAGE(message_id=11247*)
    → "I sense something...otherworldly about you, traveler. But appearances can oft be misleading, nay?"
 28: 0x006F [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0070:
 29: 0x0070 [0x01] GOTO 0x00B9
 30: 0x0073 [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x0096
 31: 0x007B [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x008F
 32: 0x0083 [0x03] Work_Zone[2] = 1*
 33: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=11248*)
    → "It may hap the secrets I seek lie with [the Crimson Lion/the Republic/the Federation]..."
 34: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x008C [0x01] GOTO 0x0093
 36: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=11247*)
    → "I sense something...otherworldly about you, traveler. But appearances can oft be misleading, nay?"
 37: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0093:
 38: 0x0093 [0x01] GOTO 0x00B9
 39: 0x0096 [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x00B9
 40: 0x009E [0x02] IF !(ExtData[1]->WorkLocal[2] == 3*) GOTO 0x00B2
 41: 0x00A6 [0x03] Work_Zone[2] = 2*
 42: 0x00AB [0x1D] PRINT_EVENT_MESSAGE(message_id=11248*)
    → "It may hap the secrets I seek lie with [the Crimson Lion/the Republic/the Federation]..."
 43: 0x00AE [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x00AF [0x01] GOTO 0x00B6
 45: 0x00B2 [0x1D] PRINT_EVENT_MESSAGE(message_id=11247*)
    → "I sense something...otherworldly about you, traveler. But appearances can oft be misleading, nay?"
 46: 0x00B5 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00B6:
 47: 0x00B6 [0x01] GOTO 0x00B9

SUBROUTINE_00B9:
 48: 0x00B9 [0x01] GOTO 0x013F
 49: 0x00BC [0x02] IF !(ExtData[1]->WorkLocal[3] == 2*) GOTO 0x013F
 50: 0x00C4 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00D3
 51: 0x00CC [0x1D] PRINT_EVENT_MESSAGE(message_id=11247*)
    → "I sense something...otherworldly about you, traveler. But appearances can oft be misleading, nay?"
 52: 0x00CF [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x00D0 [0x01] GOTO 0x013C
 54: 0x00D3 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x00F6
 55: 0x00DB [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00EF
 56: 0x00E3 [0x03] Work_Zone[2] = 0*
 57: 0x00E8 [0x1D] PRINT_EVENT_MESSAGE(message_id=11251*)
    → "I have heard rumor that the lord of the beastmen sits upon an hoary throne in the frozen north. Do you believe he would entertain a raven?"
 58: 0x00EB [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x00EC [0x01] GOTO 0x00F3
 60: 0x00EF [0x1D] PRINT_EVENT_MESSAGE(message_id=11249*)
    → "Ah, so your nation requests my services... I shall consider your proposal..."
 61: 0x00F2 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00F3:
 62: 0x00F3 [0x01] GOTO 0x013C
 63: 0x00F6 [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x0119
 64: 0x00FE [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x0112
 65: 0x0106 [0x03] Work_Zone[2] = 1*
 66: 0x010B [0x1D] PRINT_EVENT_MESSAGE(message_id=11251*)
    → "I have heard rumor that the lord of the beastmen sits upon an hoary throne in the frozen north. Do you believe he would entertain a raven?"
 67: 0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
 68: 0x010F [0x01] GOTO 0x0116
 69: 0x0112 [0x1D] PRINT_EVENT_MESSAGE(message_id=11250*)
    → "I lack the patience to deal with those who do not kneel to the raven..."
 70: 0x0115 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0116:
 71: 0x0116 [0x01] GOTO 0x013C
 72: 0x0119 [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x013C
 73: 0x0121 [0x02] IF !(ExtData[1]->WorkLocal[2] == 3*) GOTO 0x0135
 74: 0x0129 [0x03] Work_Zone[2] = 2*
 75: 0x012E [0x1D] PRINT_EVENT_MESSAGE(message_id=11251*)
    → "I have heard rumor that the lord of the beastmen sits upon an hoary throne in the frozen north. Do you believe he would entertain a raven?"
 76: 0x0131 [0x23] WAIT_FOR_DIALOG_INTERACTION
 77: 0x0132 [0x01] GOTO 0x0139
 78: 0x0135 [0x1D] PRINT_EVENT_MESSAGE(message_id=11249*)
    → "Ah, so your nation requests my services... I shall consider your proposal..."
 79: 0x0138 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0139:
 80: 0x0139 [0x01] GOTO 0x013C

SUBROUTINE_013C:
 81: 0x013C [0x01] GOTO 0x013F

SUBROUTINE_013F:
 82: 0x013F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 83: 0x0141 [0x21] END_EVENT
 84: 0x0142 [0x00] END_REQSTACK()
```
