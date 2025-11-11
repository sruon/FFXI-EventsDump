# 17637620 - Abyssea Campaign

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 296 bytes         |
| Total Events     | 4                 |
| References Count | 17                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [172](#event-172)     | 0x0001       |    172 |             49 |
| [173](#event-173)     | 0x00AD       |     10 |              6 |
| [174](#event-174)     | 0x00B7       |     10 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x239F      |        9119 |
|       1 | 0x23A0      |        9120 |
|       2 | 0x23A1      |        9121 |
|       3 | 0x23A2      |        9122 |
|       4 | 0x0000      |           0 |
|       5 | 0x0078      |         120 |
|       6 | 0x23A3      |        9123 |
|       7 | 0x0001      |           1 |
|       8 | 0x05A0      |        1440 |
|       9 | 0x23A4      |        9124 |
|      10 | 0x0002      |           2 |
|      11 | 0x23A5      |        9125 |
|      12 | 0x0003      |           3 |
|      13 | 0x23A6      |        9126 |
|      14 | 0x0004      |           4 |
|      15 | 0x23A8      |        9128 |
|      16 | 0x23A9      |        9129 |

## String References

- **9119**: The Abyssea and Atma Axtravaganza is in full swing! Just open this chest to claim your prize.
- **9120**: You can claim it anytime you want during the campaign, but don't wait too long. You can't claim squat after the campaign ends.
- **9121**: Anyway, do you want your Abyssea and Atma Axtravaganza gifts or not?
- **9122**: Receive the gifts? [Of course!/No thanks.]
- **9123**: Gift 1: Eleven different types of atma. *Characters who already possess the specified atma will not receive all eleven.
- **9124**: Gift 2: One $3! *Characters who already possess all three will be given 100,000 cruor.
- **9125**: Gift 3: 100,000 cruor!
- **9126**: Gift 4: The ability to store 100 more traverser stones! *You may check your stock of stones by speaking with Joachim or other applicable Abyssean personages.
- **9128**: Now that you have all the gifts, it's time to put them to use in Abyssea!
- **9129**: You're able to claim these amazing Abyssean gifts, so go talk to Joachim in Port Jeuno (H-8) before it's too late.

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

### Event 172

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 172 bytes |
| Instructions | 49        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 1D 00  80 23 1D 01 80 23 1D 02   ........#...#..
0010: 80 23 24 03 80 04 80 04  80 25 02 00 10 04 80 00  .#$......%......
0020: AB 00 42 2C F8 FF FF 7F  F8 FF FF 7F 6F 70 65 6E  ..B,........open
0030: 1C 05 80 3E 00 00 04 80  3D 00 01 4A 00 1D 06 80  ...>....=..J....
0040: 23 03 01 10 07 80 43 00  43 01 3E 00 00 07 80 54  #.....C.C.>....T
0050: 00 01 66 00 03 02 10 08  80 1D 09 80 23 03 01 10  ..f.........#...
0060: 0A 80 43 00 43 01 3E 00  00 0A 80 70 00 01 7D 00  ..C.C.>....p..}.
0070: 1D 0B 80 23 03 01 10 0C  80 43 00 43 01 3E 00 00  ...#.....C.C.>..
0080: 0C 80 87 00 01 94 00 1D  0D 80 23 03 01 10 0E 80  ..........#.....
0090: 43 00 43 01 2C F8 FF FF  7F F8 FF FF 7F 63 6C 6F  C.C.,........clo
00A0: 73 1C 05 80 1D 0F 80 23  01 AB 00 21 00           s......#...!.   
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=9119*)
    → "The Abyssea and Atma Axtravaganza is in full swing! Just open this chest to claim your prize."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=9120*)
    → "You can claim it anytime you want during the campaign, but don't wait too long. You can't claim squat after the campaign ends."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=9121*)
    → "Anyway, do you want your Abyssea and Atma Axtravaganza gifts or not?"
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x24] CREATE_DIALOG(message_id=9122*, default_option=0*, option_flags=0*)
    → "Receive the gifts? [Of course!/No thanks.]"
  8: 0x0019 [0x25] WAIT_DIALOG_SELECT()
  9: 0x001A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00AB
 10: 0x0022 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 11: 0x0023 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "open" with entities [EventEntity, EventEntity]
 12: 0x0030 [0x1C] WAIT(120* ticks)
 13: 0x0033 [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 0*) GOTO 0x003D
 14: 0x003A [0x01] GOTO 0x004A
 15: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=9123*)
    → "Gift 1: Eleven different types of atma. *Characters who already possess the specified atma will not receive all eleven."
 16: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0041 [0x03] Work_Zone[1] = 1*
 18: 0x0046 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 19: 0x0048 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)

SUBROUTINE_004A:
 20: 0x004A [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 1*) GOTO 0x0054
 21: 0x0051 [0x01] GOTO 0x0066
 22: 0x0054 [0x03] Work_Zone[2] = 1440*
 23: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=9124*)
    → "Gift 2: One $3! *Characters who already possess all three will be given 100,000 cruor."
 24: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x005D [0x03] Work_Zone[1] = 2*
 26: 0x0062 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 27: 0x0064 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)

SUBROUTINE_0066:
 28: 0x0066 [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 2*) GOTO 0x0070
 29: 0x006D [0x01] GOTO 0x007D
 30: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=9125*)
    → "Gift 3: 100,000 cruor!"
 31: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0074 [0x03] Work_Zone[1] = 3*
 33: 0x0079 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 34: 0x007B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)

SUBROUTINE_007D:
 35: 0x007D [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 3*) GOTO 0x0087
 36: 0x0084 [0x01] GOTO 0x0094
 37: 0x0087 [0x1D] PRINT_EVENT_MESSAGE(message_id=9126*)
    → "Gift 4: The ability to store 100 more traverser stones! *You may check your stock of stones by speaking with Joachim or other applicable Abyssean personages."
 38: 0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x008B [0x03] Work_Zone[1] = 4*
 40: 0x0090 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 41: 0x0092 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)

SUBROUTINE_0094:
 42: 0x0094 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "clos" with entities [EventEntity, EventEntity]
 43: 0x00A1 [0x1C] WAIT(120* ticks)
 44: 0x00A4 [0x1D] PRINT_EVENT_MESSAGE(message_id=9128*)
    → "Now that you have all the gifts, it's time to put them to use in Abyssea!"
 45: 0x00A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x00A8 [0x01] GOTO 0x00AB

SUBROUTINE_00AB:
 47: 0x00AB [0x21] END_EVENT
 48: 0x00AC [0x00] END_REQSTACK()
```

### Event 173

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 10 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         1D 00 80               ...
00B0: 23 1D 0F 80 23 21 00                              #...#!.         
```

#### Opcodes

```
  0: 0x00AD [0x1D] PRINT_EVENT_MESSAGE(message_id=9119*)
    → "The Abyssea and Atma Axtravaganza is in full swing! Just open this chest to claim your prize."
  1: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00B1 [0x1D] PRINT_EVENT_MESSAGE(message_id=9128*)
    → "Now that you have all the gifts, it's time to put them to use in Abyssea!"
  3: 0x00B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00B5 [0x21] END_EVENT
  5: 0x00B6 [0x00] END_REQSTACK()
```

### Event 174

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 10 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      1D  00 80 23 1D 10 80 23 21         ...#...#!
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=9119*)
    → "The Abyssea and Atma Axtravaganza is in full swing! Just open this chest to claim your prize."
  1: 0x00BA [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00BB [0x1D] PRINT_EVENT_MESSAGE(message_id=9129*)
    → "You're able to claim these amazing Abyssean gifts, so go talk to Joachim in Port Jeuno (H-8) before it's too late."
  3: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00BF [0x21] END_EVENT
  5: 0x00C0 [0x00] END_REQSTACK()
```
