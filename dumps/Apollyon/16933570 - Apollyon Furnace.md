# 16933570 - Apollyon Furnace

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 1884 bytes        |
| Total Events     | 8                 |
| References Count | 34                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [133](#event-133)     | 0x0001       |    155 |             31 |
| [135](#event-135)     | 0x009C       |    373 |             64 |
| [137](#event-137)     | 0x0211       |    162 |             31 |
| [139](#event-139)     | 0x02B3       |    170 |             35 |
| [141](#event-141)     | 0x035D       |    155 |             31 |
| [143](#event-143)     | 0x03F8       |    165 |             32 |
| [145](#event-145)     | 0x049D       |    517 |             92 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C76      |        7286 |
|       1 | 0x0000      |           0 |
|       2 | 0x1C77      |        7287 |
|       3 | 0x0001      |           1 |
|       4 | 0x003C      |          60 |
|       5 | 0x2710      |       10000 |
|       6 | 0x1C7B      |        7291 |
|       7 | 0x667A      |       26234 |
|       8 | 0x66A4      |       26276 |
|       9 | 0x1C7C      |        7292 |
|      10 | 0x0002      |           2 |
|      11 | 0x1C7D      |        7293 |
|      12 | 0x1C89      |        7305 |
|      13 | 0x1CA7      |        7335 |
|      14 | 0x1C8A      |        7306 |
|      15 | 0x1C8B      |        7307 |
|      16 | 0x1C8C      |        7308 |
|      17 | 0x1C8D      |        7309 |
|      18 | 0x2716      |       10006 |
|      19 | 0x2717      |       10007 |
|      20 | 0x2718      |       10008 |
|      21 | 0x0003      |           3 |
|      22 | 0x2719      |       10009 |
|      23 | 0x0004      |           4 |
|      24 | 0x271A      |       10010 |
|      25 | 0x1C91      |        7313 |
|      26 | 0x000F      |          15 |
|      27 | 0x0005      |           5 |
|      28 | 0x0063      |          99 |
|      29 | 0x1C92      |        7314 |
|      30 | 0x1C64      |        7268 |
|      31 | 0x1C93      |        7315 |
|      32 | 0x0010      |          16 |
|      33 | 0x001F      |          31 |

## String References

- **7268**: Enter 0 to cancel.
- **7286**: Fusing your $0 with $1 Apollyon Units to create $2.
- **7287**: Proceed? [Yes./No.]
- **7291**: # detected. Several equipment items can now be created.
- **7293**: Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Apollyon Units shall be expended in the process.
- **7305**: Confirming $0, $1, and $2. Able to create $3.
- **7306**: What will you do? [Create./Do not create.]
- **7307**: Confirming $0 and $1. Able to create $2.
- **7308**: Carrying over attributes from the $0 to the $4.
- **7309**: Your $0 will be consumed.
- **7314**: Able to change up to $0.
- **7315**: Changing $1 $0 into $3 $0 .
- **7335**: #, $1, and all five types of shards confirmed. Able to create $3.

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

### Event 133

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 155 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    93 04 10 1D 00 80 23  93 01 80 24 02 80 03 80   ......#...$....
0010: 01 80 25 02 00 10 01 80  00 87 00 42 03 01 10 03  ..%........B....
0020: 80 43 00 43 01 02 02 10  01 80 00 35 00 03 01 10  .C.C.......5....
0030: 01 80 01 84 00 2C F8 FF  FF 7F F8 FF FF 7F 69 64  .....,........id
0040: 73 32 1C 04 80 2C F8 FF  FF 7F F8 FF FF 7F 69 64  s2...,........id
0050: 73 33 1C 04 80 2C F8 FF  FF 7F F8 FF FF 7F 69 64  s3...,........id
0060: 73 34 1C 04 80 2C F8 FF  FF 7F F8 FF FF 7F 73 70  s4...,........sp
0070: 32 31 53 F8 FF FF 7F F8  FF FF 7F 73 70 32 31 03  21S........sp21.
0080: 01 10 03 80 01 97 00 02  00 10 03 80 00 97 00 03  ................
0090: 01 10 01 80 01 97 00 2E  20 00 21 00              ........ .!.    
```

#### Opcodes

```
  0: 0x0001 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[4])
  1: 0x0004 [0x1D] PRINT_EVENT_MESSAGE(message_id=7286*)
    → "Fusing your $0 with $1 Apollyon Units to create $2."
  2: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0008 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x000B [0x24] CREATE_DIALOG(message_id=7287*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  5: 0x0012 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0013 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0087
  7: 0x001B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x001C [0x03] Work_Zone[1] = 1*
  9: 0x0021 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0023 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0025 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0035
 12: 0x002D [0x03] Work_Zone[1] = 0*
 13: 0x0032 [0x01] GOTO 0x0084
 14: 0x0035 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x0042 [0x1C] WAIT(60* ticks)
 16: 0x0045 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x0052 [0x1C] WAIT(60* ticks)
 18: 0x0055 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x0062 [0x1C] WAIT(60* ticks)
 20: 0x0065 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x007F [0x03] Work_Zone[1] = 1*

SUBROUTINE_0084:
 23: 0x0084 [0x01] GOTO 0x0097
 24: 0x0087 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0097
 25: 0x008F [0x03] Work_Zone[1] = 0*
 26: 0x0094 [0x01] GOTO 0x0097

SUBROUTINE_0097:
 27: 0x0097 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x0098 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x009A [0x21] END_EVENT
 30: 0x009B [0x00] END_REQSTACK()
```

### Event 135

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x009C    |
| Data Size    | 373 bytes |
| Instructions | 64        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      03 02 10 05              ....
00A0: 80 1D 06 80 23 D4 03 01  80 07 80 D4 03 03 80 08  ....#...........
00B0: 80 03 02 10 07 80 03 03  10 08 80 D4 02 09 80 0A  ................
00C0: 80 01 80 25 02 00 10 01  80 00 60 01 24 02 80 03  ...%......`.$...
00D0: 80 01 80 25 02 00 10 01  80 00 4D 01 42 03 01 10  ...%......M.B...
00E0: 03 80 43 00 43 01 02 02  10 01 80 00 F6 00 03 01  ..C.C...........
00F0: 10 01 80 01 4A 01 2C F8  FF FF 7F F8 FF FF 7F 69  ....J.,........i
0100: 64 73 32 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 69  ds2...,........i
0110: 64 73 33 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 69  ds3...,........i
0120: 64 73 34 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 73  ds4...,........s
0130: 70 32 31 53 F8 FF FF 7F  F8 FF FF 7F 73 70 32 31  p21S........sp21
0140: 03 01 10 03 80 03 02 10  07 80 01 5D 01 02 00 10  ...........]....
0150: 03 80 00 5D 01 03 01 10  01 80 01 5D 01 01 0C 02  ...].......]....
0160: 02 00 10 03 80 00 FC 01  24 02 80 03 80 01 80 25  ........$......%
0170: 02 00 10 01 80 00 E9 01  42 03 01 10 0A 80 43 00  ........B.....C.
0180: 43 01 02 02 10 01 80 00  92 01 03 01 10 01 80 01  C...............
0190: E6 01 2C F8 FF FF 7F F8  FF FF 7F 69 64 73 32 1C  ..,........ids2.
01A0: 04 80 2C F8 FF FF 7F F8  FF FF 7F 69 64 73 33 1C  ..,........ids3.
01B0: 04 80 2C F8 FF FF 7F F8  FF FF 7F 69 64 73 34 1C  ..,........ids4.
01C0: 04 80 2C F8 FF FF 7F F8  FF FF 7F 73 70 32 31 53  ..,........sp21S
01D0: F8 FF FF 7F F8 FF FF 7F  73 70 32 31 03 01 10 03  ........sp21....
01E0: 80 03 02 10 08 80 01 F9  01 02 00 10 03 80 00 F9  ................
01F0: 01 03 01 10 01 80 01 F9  01 01 0C 02 02 00 10 0A  ................
0200: 80 00 0C 02 03 01 10 01  80 01 0C 02 2E 20 00 21  ............. .!
0210: 00                                                .               
```

#### Opcodes

```
  0: 0x009C [0x03] Work_Zone[2] = 10000*
  1: 0x00A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7291*)
    → "# detected. Several equipment items can now be created."
  2: 0x00A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00A5 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 07 80 D4 03 03 80...])
  4: 0x00C3 [0x25] WAIT_DIALOG_SELECT()
  5: 0x00C4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0160
  6: 0x00CC [0x24] CREATE_DIALOG(message_id=7287*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  7: 0x00D3 [0x25] WAIT_DIALOG_SELECT()
  8: 0x00D4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x014D
  9: 0x00DC [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x00DD [0x03] Work_Zone[1] = 1*
 11: 0x00E2 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x00E4 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x00E6 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00F6
 14: 0x00EE [0x03] Work_Zone[1] = 0*
 15: 0x00F3 [0x01] GOTO 0x014A
 16: 0x00F6 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 17: 0x0103 [0x1C] WAIT(60* ticks)
 18: 0x0106 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 19: 0x0113 [0x1C] WAIT(60* ticks)
 20: 0x0116 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 21: 0x0123 [0x1C] WAIT(60* ticks)
 22: 0x0126 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 23: 0x0133 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 24: 0x0140 [0x03] Work_Zone[1] = 1*
 25: 0x0145 [0x03] Work_Zone[2] = 26234*

SUBROUTINE_014A:
 26: 0x014A [0x01] GOTO 0x015D
 27: 0x014D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x015D
 28: 0x0155 [0x03] Work_Zone[1] = 0*
 29: 0x015A [0x01] GOTO 0x015D

SUBROUTINE_015D:
 30: 0x015D [0x01] GOTO 0x020C
 31: 0x0160 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01FC
 32: 0x0168 [0x24] CREATE_DIALOG(message_id=7287*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
 33: 0x016F [0x25] WAIT_DIALOG_SELECT()
 34: 0x0170 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01E9
 35: 0x0178 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 36: 0x0179 [0x03] Work_Zone[1] = 2*
 37: 0x017E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 38: 0x0180 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 39: 0x0182 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0192
 40: 0x018A [0x03] Work_Zone[1] = 0*
 41: 0x018F [0x01] GOTO 0x01E6
 42: 0x0192 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 43: 0x019F [0x1C] WAIT(60* ticks)
 44: 0x01A2 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 45: 0x01AF [0x1C] WAIT(60* ticks)
 46: 0x01B2 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 47: 0x01BF [0x1C] WAIT(60* ticks)
 48: 0x01C2 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 49: 0x01CF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 50: 0x01DC [0x03] Work_Zone[1] = 1*
 51: 0x01E1 [0x03] Work_Zone[2] = 26276*

SUBROUTINE_01E6:
 52: 0x01E6 [0x01] GOTO 0x01F9
 53: 0x01E9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01F9
 54: 0x01F1 [0x03] Work_Zone[1] = 0*
 55: 0x01F6 [0x01] GOTO 0x01F9

SUBROUTINE_01F9:
 56: 0x01F9 [0x01] GOTO 0x020C
 57: 0x01FC [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x020C
 58: 0x0204 [0x03] Work_Zone[1] = 0*
 59: 0x0209 [0x01] GOTO 0x020C

SUBROUTINE_020C:
 60: 0x020C [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 61: 0x020D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 62: 0x020F [0x21] END_EVENT
 63: 0x0210 [0x00] END_REQSTACK()
```

### Event 137

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0211    |
| Data Size    | 162 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:    CC 03 02 10 03 10 04  10 05 10 1D 0B 80 23 93   .............#.
0220: 01 80 24 02 80 03 80 01  80 25 02 00 10 01 80 00  ..$......%......
0230: 9E 02 42 03 01 10 03 80  43 00 43 01 02 02 10 01  ..B.....C.C.....
0240: 80 00 4C 02 03 01 10 01  80 01 9B 02 2C F8 FF FF  ..L.........,...
0250: 7F F8 FF FF 7F 69 64 73  32 1C 04 80 2C F8 FF FF  .....ids2...,...
0260: 7F F8 FF FF 7F 69 64 73  33 1C 04 80 2C F8 FF FF  .....ids3...,...
0270: 7F F8 FF FF 7F 69 64 73  34 1C 04 80 2C F8 FF FF  .....ids4...,...
0280: 7F F8 FF FF 7F 73 70 32  31 53 F8 FF FF 7F F8 FF  .....sp21S......
0290: FF 7F 73 70 32 31 03 01  10 03 80 01 AE 02 02 00  ..sp21..........
02A0: 10 03 80 00 AE 02 03 01  10 01 80 01 AE 02 2E 20  ............... 
02B0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0211 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x03 - Open item info window (conditional chase), check_value=Work_Zone[2], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x021B [0x1D] PRINT_EVENT_MESSAGE(message_id=7293*)
    → "Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Apollyon Units shall be expended in the process."
  2: 0x021E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x021F [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x0222 [0x24] CREATE_DIALOG(message_id=7287*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  5: 0x0229 [0x25] WAIT_DIALOG_SELECT()
  6: 0x022A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x029E
  7: 0x0232 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x0233 [0x03] Work_Zone[1] = 1*
  9: 0x0238 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x023A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x023C [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x024C
 12: 0x0244 [0x03] Work_Zone[1] = 0*
 13: 0x0249 [0x01] GOTO 0x029B
 14: 0x024C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x0259 [0x1C] WAIT(60* ticks)
 16: 0x025C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x0269 [0x1C] WAIT(60* ticks)
 18: 0x026C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x0279 [0x1C] WAIT(60* ticks)
 20: 0x027C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x0289 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x0296 [0x03] Work_Zone[1] = 1*

SUBROUTINE_029B:
 23: 0x029B [0x01] GOTO 0x02AE
 24: 0x029E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02AE
 25: 0x02A6 [0x03] Work_Zone[1] = 0*
 26: 0x02AB [0x01] GOTO 0x02AE

SUBROUTINE_02AE:
 27: 0x02AE [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x02AF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x02B1 [0x21] END_EVENT
 30: 0x02B2 [0x00] END_REQSTACK()
```

### Event 139

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02B3    |
| Data Size    | 170 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:          93 05 10 02 06  10 01 80 00 C5 02 1D 0C     .............
02C0: 80 23 01 C9 02 1D 0D 80  23 93 01 80 24 0E 80 03  .#......#...$...
02D0: 80 01 80 25 02 00 10 01  80 00 48 03 42 03 01 10  ...%......H.B...
02E0: 03 80 43 00 43 01 02 02  10 01 80 00 F6 02 03 01  ..C.C...........
02F0: 10 01 80 01 45 03 2C F8  FF FF 7F F8 FF FF 7F 69  ....E.,........i
0300: 64 73 32 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 69  ds2...,........i
0310: 64 73 33 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 69  ds3...,........i
0320: 64 73 34 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 73  ds4...,........s
0330: 70 32 31 53 F8 FF FF 7F  F8 FF FF 7F 73 70 32 31  p21S........sp21
0340: 03 01 10 03 80 01 58 03  02 00 10 03 80 00 58 03  ......X.......X.
0350: 03 01 10 01 80 01 58 03  2E 20 00 21 00           ......X.. .!.   
```

#### Opcodes

```
  0: 0x02B3 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[5])
  1: 0x02B6 [0x02] IF !(Work_Zone[6] == 0*) GOTO 0x02C5
  2: 0x02BE [0x1D] PRINT_EVENT_MESSAGE(message_id=7305*)
    → "Confirming $0, $1, and $2. Able to create $3."
  3: 0x02C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x02C2 [0x01] GOTO 0x02C9
  5: 0x02C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7335*)
    → "#, $1, and all five types of shards confirmed. Able to create $3."
  6: 0x02C8 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_02C9:
  7: 0x02C9 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  8: 0x02CC [0x24] CREATE_DIALOG(message_id=7306*, default_option=1*, option_flags=0*)
    → "What will you do? [Create./Do not create.]"
  9: 0x02D3 [0x25] WAIT_DIALOG_SELECT()
 10: 0x02D4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0348
 11: 0x02DC [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x02DD [0x03] Work_Zone[1] = 1*
 13: 0x02E2 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 14: 0x02E4 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 15: 0x02E6 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x02F6
 16: 0x02EE [0x03] Work_Zone[1] = 0*
 17: 0x02F3 [0x01] GOTO 0x0345
 18: 0x02F6 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 19: 0x0303 [0x1C] WAIT(60* ticks)
 20: 0x0306 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 21: 0x0313 [0x1C] WAIT(60* ticks)
 22: 0x0316 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 23: 0x0323 [0x1C] WAIT(60* ticks)
 24: 0x0326 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 25: 0x0333 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 26: 0x0340 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0345:
 27: 0x0345 [0x01] GOTO 0x0358
 28: 0x0348 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0358
 29: 0x0350 [0x03] Work_Zone[1] = 0*
 30: 0x0355 [0x01] GOTO 0x0358

SUBROUTINE_0358:
 31: 0x0358 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 32: 0x0359 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x035B [0x21] END_EVENT
 34: 0x035C [0x00] END_REQSTACK()
```

### Event 141

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x035D    |
| Data Size    | 155 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0350:                                         93 04 10               ...
0360: 1D 0F 80 23 93 01 80 24  0E 80 03 80 01 80 25 02  ...#...$......%.
0370: 00 10 01 80 00 E3 03 42  03 01 10 03 80 43 00 43  .......B.....C.C
0380: 01 02 02 10 01 80 00 91  03 03 01 10 01 80 01 E0  ................
0390: 03 2C F8 FF FF 7F F8 FF  FF 7F 69 64 73 32 1C 04  .,........ids2..
03A0: 80 2C F8 FF FF 7F F8 FF  FF 7F 69 64 73 33 1C 04  .,........ids3..
03B0: 80 2C F8 FF FF 7F F8 FF  FF 7F 69 64 73 34 1C 04  .,........ids4..
03C0: 80 2C F8 FF FF 7F F8 FF  FF 7F 73 70 32 31 53 F8  .,........sp21S.
03D0: FF FF 7F F8 FF FF 7F 73  70 32 31 03 01 10 03 80  .......sp21.....
03E0: 01 F3 03 02 00 10 03 80  00 F3 03 03 01 10 01 80  ................
03F0: 01 F3 03 2E 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x035D [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[4])
  1: 0x0360 [0x1D] PRINT_EVENT_MESSAGE(message_id=7307*)
    → "Confirming $0 and $1. Able to create $2."
  2: 0x0363 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0364 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x0367 [0x24] CREATE_DIALOG(message_id=7306*, default_option=1*, option_flags=0*)
    → "What will you do? [Create./Do not create.]"
  5: 0x036E [0x25] WAIT_DIALOG_SELECT()
  6: 0x036F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03E3
  7: 0x0377 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x0378 [0x03] Work_Zone[1] = 1*
  9: 0x037D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x037F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0381 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0391
 12: 0x0389 [0x03] Work_Zone[1] = 0*
 13: 0x038E [0x01] GOTO 0x03E0
 14: 0x0391 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x039E [0x1C] WAIT(60* ticks)
 16: 0x03A1 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x03AE [0x1C] WAIT(60* ticks)
 18: 0x03B1 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x03BE [0x1C] WAIT(60* ticks)
 20: 0x03C1 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x03CE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x03DB [0x03] Work_Zone[1] = 1*

SUBROUTINE_03E0:
 23: 0x03E0 [0x01] GOTO 0x03F3
 24: 0x03E3 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03F3
 25: 0x03EB [0x03] Work_Zone[1] = 0*
 26: 0x03F0 [0x01] GOTO 0x03F3

SUBROUTINE_03F3:
 27: 0x03F3 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x03F4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x03F6 [0x21] END_EVENT
 30: 0x03F7 [0x00] END_REQSTACK()
```

### Event 143

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x03F8    |
| Data Size    | 165 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03F0:                          CC 03 06 10 03 10 04 10          ........
0400: 05 10 1D 10 80 23 48 11  80 93 01 80 24 02 80 03  .....#H.....$...
0410: 80 01 80 25 02 00 10 01  80 00 88 04 42 03 01 10  ...%........B...
0420: 03 80 43 00 43 01 02 02  10 01 80 00 36 04 03 01  ..C.C.......6...
0430: 10 01 80 01 85 04 2C F8  FF FF 7F F8 FF FF 7F 69  ......,........i
0440: 64 73 32 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 69  ds2...,........i
0450: 64 73 33 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 69  ds3...,........i
0460: 64 73 34 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 73  ds4...,........s
0470: 70 32 31 53 F8 FF FF 7F  F8 FF FF 7F 73 70 32 31  p21S........sp21
0480: 03 01 10 03 80 01 98 04  02 00 10 03 80 00 98 04  ................
0490: 03 01 10 01 80 01 98 04  2E 20 00 21 00           ......... .!.   
```

#### Opcodes

```
  0: 0x03F8 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x03 - Open item info window (conditional chase), check_value=Work_Zone[6], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x0402 [0x1D] PRINT_EVENT_MESSAGE(message_id=7308*)
    → "Carrying over attributes from the $0 to the $4."
  2: 0x0405 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0406 [0x48] [System] [7309*]:
    → "Your $0 will be consumed."
  4: 0x0409 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  5: 0x040C [0x24] CREATE_DIALOG(message_id=7287*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  6: 0x0413 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0414 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0488
  8: 0x041C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x041D [0x03] Work_Zone[1] = 1*
 10: 0x0422 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x0424 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x0426 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0436
 13: 0x042E [0x03] Work_Zone[1] = 0*
 14: 0x0433 [0x01] GOTO 0x0485
 15: 0x0436 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 16: 0x0443 [0x1C] WAIT(60* ticks)
 17: 0x0446 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 18: 0x0453 [0x1C] WAIT(60* ticks)
 19: 0x0456 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 20: 0x0463 [0x1C] WAIT(60* ticks)
 21: 0x0466 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x0473 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 23: 0x0480 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0485:
 24: 0x0485 [0x01] GOTO 0x0498
 25: 0x0488 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0498
 26: 0x0490 [0x03] Work_Zone[1] = 0*
 27: 0x0495 [0x01] GOTO 0x0498

SUBROUTINE_0498:
 28: 0x0498 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 29: 0x0499 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x049B [0x21] END_EVENT
 31: 0x049C [0x00] END_REQSTACK()
```

### Event 145

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x049D    |
| Data Size    | 517 bytes |
| Instructions | 91        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0490:                                         03 00 00               ...
04A0: 02 10 03 01 00 03 10 03  06 00 01 80 0C 04 10 3C  ...............<
04B0: 06 00 04 10 03 80 D4 03  01 80 12 80 D4 03 03 80  ................
04C0: 13 80 D4 03 0A 80 14 80  D4 03 15 80 16 80 D4 03  ................
04D0: 17 80 18 80 03 02 10 12  80 03 03 10 13 80 03 04  ................
04E0: 10 14 80 03 05 10 16 80  03 06 10 18 80 03 07 10  ................
04F0: 00 00 03 08 10 01 00 03  01 10 01 80 D4 02 19 80  ................
0500: 01 80 06 00 25 02 00 10  01 80 00 1E 05 40 01 80  ....%........@..
0510: 1A 80 01 10 03 80 03 04  00 12 80 01 92 05 02 00  ................
0520: 10 03 80 00 37 05 40 01  80 1A 80 01 10 0A 80 03  ....7.@.........
0530: 04 00 13 80 01 92 05 02  00 10 0A 80 00 50 05 40  .............P.@
0540: 01 80 1A 80 01 10 15 80  03 04 00 14 80 01 92 05  ................
0550: 02 00 10 15 80 00 69 05  40 01 80 1A 80 01 10 17  ......i.@.......
0560: 80 03 04 00 16 80 01 92  05 02 00 10 17 80 00 82  ................
0570: 05 40 01 80 1A 80 01 10  1B 80 03 04 00 18 80 01  .@..............
0580: 92 05 02 00 10 1B 80 00  92 05 03 01 10 01 80 01  ................
0590: 92 05 02 01 10 01 80 00  9D 05 01 9D 06 03 02 00  ................
05A0: 01 00 15 02 00 0A 80 02  02 00 1C 80 04 B4 05 03  ................
05B0: 02 00 1C 80 03 02 10 02  00 1D 1D 80 23 48 1E 80  ............#H..
05C0: 71 12 03 80 0A 80 71 13  02 10 02 02 10 01 80 00  q.....q.........
05D0: DA 05 03 01 10 01 80 01  9D 06 02 02 10 02 00 05  ................
05E0: 9A 06 03 03 00 02 10 14  03 00 0A 80 03 05 00 02  ................
05F0: 10 03 02 10 00 00 03 03  10 03 00 03 04 10 04 00  ................
0600: 03 05 10 05 00 1D 1F 80  23 24 0E 80 03 80 01 80  ........#$......
0610: 25 02 00 10 01 80 00 89  06 40 20 80 21 80 01 10  %........@ .!...
0620: 05 10 42 43 00 43 01 02  02 10 01 80 00 37 06 03  ..BC.C.......7..
0630: 01 10 01 80 01 86 06 2C  F8 FF FF 7F F8 FF FF 7F  .......,........
0640: 69 64 73 32 1C 04 80 2C  F8 FF FF 7F F8 FF FF 7F  ids2...,........
0650: 69 64 73 33 1C 04 80 2C  F8 FF FF 7F F8 FF FF 7F  ids3...,........
0660: 69 64 73 34 1C 04 80 2C  F8 FF FF 7F F8 FF FF 7F  ids4...,........
0670: 73 70 32 31 53 F8 FF FF  7F F8 FF FF 7F 73 70 32  sp21S........sp2
0680: 31 03 01 10 03 80 01 97  06 02 00 10 03 80 00 97  1...............
0690: 06 01 D4 04 01 97 06 01  9D 06 01 D4 04 2E 20 00  .............. .
06A0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x049D [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x04A2 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x04A7 [0x03] ExtData[1]->WorkLocal[6] = 0*
  3: 0x04AC [0x0C] Work_Zone[4]--
  4: 0x04AF [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[6], bit_index_work_offset=Work_Zone[4], condition_work_offset=1*)
  5: 0x04B6 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 12 80 D4 03 03 80...])
  6: 0x04D4 [0x03] Work_Zone[2] = 10006*
  7: 0x04D9 [0x03] Work_Zone[3] = 10007*
  8: 0x04DE [0x03] Work_Zone[4] = 10008*
  9: 0x04E3 [0x03] Work_Zone[5] = 10009*
 10: 0x04E8 [0x03] Work_Zone[6] = 10010*
 11: 0x04ED [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[0]
 12: 0x04F2 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[1]
 13: 0x04F7 [0x03] Work_Zone[1] = 0*
 14: 0x04FC [0xD4] MAP_QUERY_WINDOW: Test and open query window (flag=0x19, work=[0x0180, 0x0680, 0x2500])
 15: 0x0505 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x051E
 16: 0x050D [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 17: 0x0516 [0x03] ExtData[1]->WorkLocal[4] = 10006*
 18: 0x051B [0x01] GOTO 0x0592
 19: 0x051E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0537
 20: 0x0526 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
 21: 0x052F [0x03] ExtData[1]->WorkLocal[4] = 10007*
 22: 0x0534 [0x01] GOTO 0x0592
 23: 0x0537 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0550
 24: 0x053F [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=3*)
 25: 0x0548 [0x03] ExtData[1]->WorkLocal[4] = 10008*
 26: 0x054D [0x01] GOTO 0x0592
 27: 0x0550 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0569
 28: 0x0558 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=4*)
 29: 0x0561 [0x03] ExtData[1]->WorkLocal[4] = 10009*
 30: 0x0566 [0x01] GOTO 0x0592
 31: 0x0569 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0582
 32: 0x0571 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=5*)
 33: 0x057A [0x03] ExtData[1]->WorkLocal[4] = 10010*
 34: 0x057F [0x01] GOTO 0x0592
 35: 0x0582 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0592
 36: 0x058A [0x03] Work_Zone[1] = 0*
 37: 0x058F [0x01] GOTO 0x0592

SUBROUTINE_0592:
 38: 0x0592 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x059D
 39: 0x059A [0x01] GOTO 0x069D
 40: 0x059D [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
 41: 0x05A2 [0x15] ExtData[1]->WorkLocal[2] /= 2*
 42: 0x05A7 [0x02] IF !(ExtData[1]->WorkLocal[2] < 99*) GOTO 0x05B4
 43: 0x05AF [0x03] ExtData[1]->WorkLocal[2] = 99*
 44: 0x05B4 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 45: 0x05B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7314*)
    → "Able to change up to $0."
 46: 0x05BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x05BD [0x48] [System] [7268*]:
    → "Enter 0 to cancel."
 48: 0x05C0 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 49: 0x05C6 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=Work_Zone[2])
 50: 0x05CA [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x05DA
 51: 0x05D2 [0x03] Work_Zone[1] = 0*
 52: 0x05D7 [0x01] GOTO 0x069D
 53: 0x05DA [0x02] IF !(Work_Zone[2] > ExtData[1]->WorkLocal[2]) GOTO 0x069A
 54: 0x05E2 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[2]
 55: 0x05E7 [0x14] ExtData[1]->WorkLocal[3] *= 2*
 56: 0x05EC [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[2]
 57: 0x05F1 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 58: 0x05F6 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[3]
 59: 0x05FB [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[4]
 60: 0x0600 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[5]
 61: 0x0605 [0x1D] PRINT_EVENT_MESSAGE(message_id=7315*)
    → "Changing $1 $0 into $3 $0 ."
 62: 0x0608 [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x0609 [0x24] CREATE_DIALOG(message_id=7306*, default_option=1*, option_flags=0*)
    → "What will you do? [Create./Do not create.]"
 64: 0x0610 [0x25] WAIT_DIALOG_SELECT()
 65: 0x0611 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0689
 66: 0x0619 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=Work_Zone[5])
 67: 0x0622 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 68: 0x0623 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 69: 0x0625 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 70: 0x0627 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0637
 71: 0x062F [0x03] Work_Zone[1] = 0*
 72: 0x0634 [0x01] GOTO 0x0686
 73: 0x0637 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 74: 0x0644 [0x1C] WAIT(60* ticks)
 75: 0x0647 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 76: 0x0654 [0x1C] WAIT(60* ticks)
 77: 0x0657 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 78: 0x0664 [0x1C] WAIT(60* ticks)
 79: 0x0667 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 80: 0x0674 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 81: 0x0681 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0686:
 82: 0x0686 [0x01] GOTO 0x0697
 83: 0x0689 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0697
 84: 0x0691 [0x01] GOTO 0x04D4

SUBROUTINE_0697:
 85: 0x0697 [0x01] GOTO 0x069D
 86: 0x069A [0x01] GOTO 0x04D4

SUBROUTINE_069D:
 87: 0x069D [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 88: 0x069E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 89: 0x06A0 [0x21] END_EVENT
 90: 0x06A1 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0694 [0x01] GOTO 0x0697
```
