# 17924210 - Garden Strongbox

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Mog Garden (ID: 280) |
| Block Size       | 740 bytes            |
| Total Events     | 7                    |
| References Count | 25                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      3 |              2 |
| [65535.2](#event-655352) | 0x0005       |      3 |              2 |
| [65535.3](#event-655353) | 0x0008       |      5 |              2 |
| [1074](#event-1074)      | 0x000D       |    136 |             32 |
| [1073](#event-1073)      | 0x0095       |    446 |            103 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x03C9      |         969 |
|       1 | 0x1D64      |        7524 |
|       2 | 0x0000      |           0 |
|       3 | 0x3B9ACA00  |  1000000000 |
|       4 | 0x1D66      |        7526 |
|       5 | 0x001F      |          31 |
|       6 | 0x0001      |           1 |
|       7 | 0x001E      |          30 |
|       8 | 0x1D65      |        7525 |
|       9 | 0x989680    |    10000000 |
|      10 | 0x03C0      |         960 |
|      11 | 0x18FE      |        6398 |
|      12 | 0x1D5C      |        7516 |
|      13 | 0x1D5D      |        7517 |
|      14 | 0x1D5E      |        7518 |
|      15 | 0x1D5F      |        7519 |
|      16 | 0x1D60      |        7520 |
|      17 | 0x1D63      |        7523 |
|      18 | 0x0009      |           9 |
|      19 | 0x0002      |           2 |
|      20 | 0x1D68      |        7528 |
|      21 | 0x1D69      |        7529 |
|      22 | 0x1D67      |        7527 |
|      23 | 0x1D6A      |        7530 |
|      24 | 0x0003      |           3 |

## String References

- **6398**: You do not have enough gil.
- **7516**: A repository rests before you, likely containing $0 gil.
- **7517**: What shall you do? [Check its contents./Deposit gil./Withdraw gil./Nothing.]
- **7518**: You peer through the opening to see how high your treasures are piled.
- **7519**: It turns out that you have $0 gil stored safely inside.
- **7520**: You can deposit $1 more gil until the repository can hold no more.
- **7523**: How much gil will you deposit?
- **7524**: Truly deposit $2 gil? [Yes./No.]
- **7525**: The satisfying clink of money finding a snug nook within its safehouse soothes your soul.
- **7526**: You cannot add any more gil!
- **7527**: You cannot hold any more gil!
- **7528**: How much gil will you withdraw?
- **7529**: Truly withdraw $2 gil? [Yes./No.]
- **7530**: Not a single gil rests inside the repository anymore.

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

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 00                                      "..           
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                22 01 00                                "..        
```

#### Opcodes

```
  0: 0x0005 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          B6 00 00 80 00                   .....   
```

#### Opcodes

```
  0: 0x0008 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=969*)
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 1074

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000D    |
| Data Size    | 136 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         03 01 00               ...
0010: 03 10 03 04 10 02 10 24  01 80 02 80 02 80 25 02  .......$......%.
0020: 00 10 02 80 00 88 00 42  03 03 00 01 00 07 03 00  .......B........
0030: 04 10 02 03 00 03 80 02  41 00 48 04 80 23 01 85  ........A.H..#..
0040: 00 06 01 10 40 05 80 05  80 01 10 06 80 40 02 80  ....@........@..
0050: 07 80 01 10 04 10 43 00  43 01 02 02 10 06 80 00  ......C.C.......
0060: 79 00 48 08 80 23 02 03  00 09 80 04 75 00 B6 00  y.H..#......u...
0070: 00 80 01 79 00 B6 00 0A  80 02 02 10 02 80 00 85  ...y............
0080: 00 48 0B 80 23 01 93 00  02 00 10 06 80 00 93 00  .H..#...........
0090: 01 93 00 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x000D [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  1: 0x0012 [0x03] Work_Zone[4] = Work_Zone[2]
  2: 0x0017 [0x24] CREATE_DIALOG(message_id=7524*, default_option=0*, option_flags=0*)
    → "Truly deposit $2 gil? [Yes./No.]"
  3: 0x001E [0x25] WAIT_DIALOG_SELECT()
  4: 0x001F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0088
  5: 0x0027 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x0028 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[1]
  7: 0x002D [0x07] ExtData[1]->WorkLocal[3] += Work_Zone[4]
  8: 0x0032 [0x02] IF !(ExtData[1]->WorkLocal[3] <= 1000000000*) GOTO 0x0041
  9: 0x003A [0x48] [System] [7526*]:
    → "You cannot add any more gil!"
 10: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x003E [0x01] GOTO 0x0085
 12: 0x0041 [0x06] Work_Zone[1] = 0
 13: 0x0044 [0x40] SET_BIT_WORK_RANGE(start_bit=31*, end_bit=31*, target=Work_Zone[1], source=1*)
 14: 0x004D [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=30*, target=Work_Zone[1], source=Work_Zone[4])
 15: 0x0056 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 16: 0x0058 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 17: 0x005A [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0079
 18: 0x0062 [0x48] [System] [7525*]:
    → "The satisfying clink of money finding a snug nook within its safehouse soothes your soul."
 19: 0x0065 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0066 [0x02] IF !(ExtData[1]->WorkLocal[3] < 10000000*) GOTO 0x0075
 21: 0x006E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=969*)
 22: 0x0072 [0x01] GOTO 0x0079
 23: 0x0075 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=960*)

SUBROUTINE_0079:
 24: 0x0079 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0085
 25: 0x0081 [0x48] [System] [6398*]:
    → "You do not have enough gil."
 26: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0085:
 27: 0x0085 [0x01] GOTO 0x0093
 28: 0x0088 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0093
 29: 0x0090 [0x01] GOTO 0x0093

SUBROUTINE_0093:
 30: 0x0093 [0x21] END_EVENT
 31: 0x0094 [0x00] END_REQSTACK()
```

### Event 1073

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0095    |
| Data Size    | 446 bytes |
| Instructions | 103       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                03 01 00  02 10 48 0C 80 23 03 00       .....H..#..
00A0: 00 06 80 02 00 00 02 80  02 51 02 24 0D 80 02 80  .........Q.$....
00B0: 02 80 25 02 00 10 02 80  00 D9 00 03 02 00 03 80  ..%.............
00C0: 48 0E 80 23 48 0F 80 23  08 02 00 01 00 03 03 10  H..#H..#........
00D0: 02 00 48 10 80 23 01 4E  02 02 00 10 06 80 00 7E  ..H..#.N.......~
00E0: 01 48 11 80 23 71 12 06  80 12 80 71 13 04 10 02  .H..#q.....q....
00F0: 04 10 02 80 05 FA 00 01  70 01 24 01 80 02 80 02  ........p.$.....
0100: 80 25 02 00 10 02 80 00  7B 01 42 03 03 00 01 00  .%......{.B.....
0110: 07 03 00 04 10 02 03 00  03 80 02 24 01 48 04 80  ...........$.H..
0120: 23 01 6D 01 06 01 10 40  05 80 05 80 01 10 06 80  #.m....@........
0130: 40 02 80 07 80 01 10 04  10 43 00 43 01 02 02 10  @........C.C....
0140: 06 80 00 5C 01 48 08 80  23 02 03 00 09 80 04 58  ...\.H..#......X
0150: 01 B6 00 00 80 01 5C 01  B6 00 0A 80 02 02 10 02  ......\.........
0160: 80 00 68 01 48 0B 80 23  03 00 00 02 80 01 70 01  ..h.H..#......p.
0170: 02 00 10 06 80 00 7B 01  01 7B 01 01 4E 02 02 00  ......{..{..N...
0180: 10 13 80 00 3E 02 48 14  80 23 71 12 06 80 12 80  ....>.H..#q.....
0190: 71 13 04 10 02 04 10 02  80 05 9F 01 01 30 02 24  q............0.$
01A0: 15 80 02 80 02 80 25 02  00 10 02 80 00 3B 02 42  ......%......;.B
01B0: 03 03 00 01 00 08 03 00  04 10 02 03 00 02 80 03  ................
01C0: C9 01 48 0B 80 23 01 2D  02 06 01 10 40 05 80 05  ..H..#.-....@...
01D0: 80 01 10 02 80 40 02 80  07 80 01 10 04 10 43 00  .....@........C.
01E0: 43 01 02 02 10 02 80 00  EE 01 48 16 80 23 02 02  C.........H..#..
01F0: 10 06 80 00 09 02 02 03  00 09 80 04 05 02 B6 00  ................
0200: 00 80 01 09 02 B6 00 0A  80 02 02 10 13 80 00 28  ...............(
0210: 02 48 17 80 23 02 03 00  09 80 04 24 02 B6 00 00  .H..#......$....
0220: 80 01 28 02 B6 00 0A 80  03 00 00 02 80 01 30 02  ..(...........0.
0230: 02 00 10 06 80 00 3B 02  01 3B 02 01 4E 02 02 00  ......;..;..N...
0240: 10 18 80 00 4E 02 03 00  00 02 80 01 4E 02 01 A3  ....N.......N...
0250: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0095 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
  1: 0x009A [0x48] [System] [7516*]:
    → "A repository rests before you, likely containing $0 gil."
  2: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x009E [0x03] ExtData[1]->WorkLocal[0] = 1*
  4: 0x00A3 [0x02] IF !(ExtData[1]->WorkLocal[0] <= 0*) GOTO 0x0251
  5: 0x00AB [0x24] CREATE_DIALOG(message_id=7517*, default_option=0*, option_flags=0*)
    → "What shall you do? [Check its contents./Deposit gil./Withdraw gil./Nothing.]"
  6: 0x00B2 [0x25] WAIT_DIALOG_SELECT()
  7: 0x00B3 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00D9
  8: 0x00BB [0x03] ExtData[1]->WorkLocal[2] = 1000000000*
  9: 0x00C0 [0x48] [System] [7518*]:
    → "You peer through the opening to see how high your treasures are piled."
 10: 0x00C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00C4 [0x48] [System] [7519*]:
    → "It turns out that you have $0 gil stored safely inside."
 12: 0x00C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00C8 [0x08] ExtData[1]->WorkLocal[2] -= ExtData[1]->WorkLocal[1]
 14: 0x00CD [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
 15: 0x00D2 [0x48] [System] [7520*]:
    → "You can deposit $1 more gil until the repository can hold no more."
 16: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00D6 [0x01] GOTO 0x024E
 18: 0x00D9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x017E
 19: 0x00E1 [0x48] [System] [7523*]:
    → "How much gil will you deposit?"
 20: 0x00E4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x00E5 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 9*])
 22: 0x00EB [0x71] USER_INPUT_HANDLER: Process numerical input B (work=Work_Zone[4])
 23: 0x00EF [0x02] IF !(Work_Zone[4] > 0*) GOTO 0x00FA
 24: 0x00F7 [0x01] GOTO 0x0170
 25: 0x00FA [0x24] CREATE_DIALOG(message_id=7524*, default_option=0*, option_flags=0*)
    → "Truly deposit $2 gil? [Yes./No.]"
 26: 0x0101 [0x25] WAIT_DIALOG_SELECT()
 27: 0x0102 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x017B
 28: 0x010A [0x42] SET_CLI_EVENT_CANCEL_DATA()
 29: 0x010B [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[1]
 30: 0x0110 [0x07] ExtData[1]->WorkLocal[3] += Work_Zone[4]
 31: 0x0115 [0x02] IF !(ExtData[1]->WorkLocal[3] <= 1000000000*) GOTO 0x0124
 32: 0x011D [0x48] [System] [7526*]:
    → "You cannot add any more gil!"
 33: 0x0120 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0121 [0x01] GOTO 0x016D
 35: 0x0124 [0x06] Work_Zone[1] = 0
 36: 0x0127 [0x40] SET_BIT_WORK_RANGE(start_bit=31*, end_bit=31*, target=Work_Zone[1], source=1*)
 37: 0x0130 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=30*, target=Work_Zone[1], source=Work_Zone[4])
 38: 0x0139 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 39: 0x013B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 40: 0x013D [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x015C
 41: 0x0145 [0x48] [System] [7525*]:
    → "The satisfying clink of money finding a snug nook within its safehouse soothes your soul."
 42: 0x0148 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x0149 [0x02] IF !(ExtData[1]->WorkLocal[3] < 10000000*) GOTO 0x0158
 44: 0x0151 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=969*)
 45: 0x0155 [0x01] GOTO 0x015C
 46: 0x0158 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=960*)

SUBROUTINE_015C:
 47: 0x015C [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0168
 48: 0x0164 [0x48] [System] [6398*]:
    → "You do not have enough gil."
 49: 0x0167 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x0168 [0x03] ExtData[1]->WorkLocal[0] = 0*

SUBROUTINE_016D:
 51: 0x016D [0x01] GOTO 0x0170

SUBROUTINE_0170:
 52: 0x0170 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x017B
 53: 0x0178 [0x01] GOTO 0x017B

SUBROUTINE_017B:
 54: 0x017B [0x01] GOTO 0x024E
 55: 0x017E [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x023E
 56: 0x0186 [0x48] [System] [7528*]:
    → "How much gil will you withdraw?"
 57: 0x0189 [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x018A [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 9*])
 59: 0x0190 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=Work_Zone[4])
 60: 0x0194 [0x02] IF !(Work_Zone[4] > 0*) GOTO 0x019F
 61: 0x019C [0x01] GOTO 0x0230
 62: 0x019F [0x24] CREATE_DIALOG(message_id=7529*, default_option=0*, option_flags=0*)
    → "Truly withdraw $2 gil? [Yes./No.]"
 63: 0x01A6 [0x25] WAIT_DIALOG_SELECT()
 64: 0x01A7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x023B
 65: 0x01AF [0x42] SET_CLI_EVENT_CANCEL_DATA()
 66: 0x01B0 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[1]
 67: 0x01B5 [0x08] ExtData[1]->WorkLocal[3] -= Work_Zone[4]
 68: 0x01BA [0x02] IF !(ExtData[1]->WorkLocal[3] >= 0*) GOTO 0x01C9
 69: 0x01C2 [0x48] [System] [6398*]:
    → "You do not have enough gil."
 70: 0x01C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 71: 0x01C6 [0x01] GOTO 0x022D
 72: 0x01C9 [0x06] Work_Zone[1] = 0
 73: 0x01CC [0x40] SET_BIT_WORK_RANGE(start_bit=31*, end_bit=31*, target=Work_Zone[1], source=0*)
 74: 0x01D5 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=30*, target=Work_Zone[1], source=Work_Zone[4])
 75: 0x01DE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 76: 0x01E0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 77: 0x01E2 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x01EE
 78: 0x01EA [0x48] [System] [7527*]:
    → "You cannot hold any more gil!"
 79: 0x01ED [0x23] WAIT_FOR_DIALOG_INTERACTION
 80: 0x01EE [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0209
 81: 0x01F6 [0x02] IF !(ExtData[1]->WorkLocal[3] < 10000000*) GOTO 0x0205
 82: 0x01FE [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=969*)
 83: 0x0202 [0x01] GOTO 0x0209
 84: 0x0205 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=960*)

SUBROUTINE_0209:
 85: 0x0209 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0228
 86: 0x0211 [0x48] [System] [7530*]:
    → "Not a single gil rests inside the repository anymore."
 87: 0x0214 [0x23] WAIT_FOR_DIALOG_INTERACTION
 88: 0x0215 [0x02] IF !(ExtData[1]->WorkLocal[3] < 10000000*) GOTO 0x0224
 89: 0x021D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=969*)
 90: 0x0221 [0x01] GOTO 0x0228
 91: 0x0224 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=960*)

SUBROUTINE_0228:
 92: 0x0228 [0x03] ExtData[1]->WorkLocal[0] = 0*

SUBROUTINE_022D:
 93: 0x022D [0x01] GOTO 0x0230

SUBROUTINE_0230:
 94: 0x0230 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x023B
 95: 0x0238 [0x01] GOTO 0x023B

SUBROUTINE_023B:
 96: 0x023B [0x01] GOTO 0x024E
 97: 0x023E [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x024E
 98: 0x0246 [0x03] ExtData[1]->WorkLocal[0] = 0*
 99: 0x024B [0x01] GOTO 0x024E

SUBROUTINE_024E:
100: 0x024E [0x01] GOTO 0x00A3
101: 0x0251 [0x21] END_EVENT
102: 0x0252 [0x00] END_REQSTACK()
```
