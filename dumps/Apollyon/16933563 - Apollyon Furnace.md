# 16933563 - Apollyon Furnace

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 1844 bytes        |
| Total Events     | 8                 |
| References Count | 32                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [133](#event-133)     | 0x0001       |    155 |             31 |
| [135](#event-135)     | 0x009C       |    373 |             64 |
| [137](#event-137)     | 0x0211       |    162 |             31 |
| [139](#event-139)     | 0x02B3       |    155 |             31 |
| [141](#event-141)     | 0x034E       |    155 |             31 |
| [143](#event-143)     | 0x03E9       |    165 |             32 |
| [145](#event-145)     | 0x048E       |    499 |             89 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C71      |        7281 |
|       1 | 0x0000      |           0 |
|       2 | 0x1C72      |        7282 |
|       3 | 0x0001      |           1 |
|       4 | 0x003C      |          60 |
|       5 | 0x2710      |       10000 |
|       6 | 0x1C76      |        7286 |
|       7 | 0x667A      |       26234 |
|       8 | 0x66A4      |       26276 |
|       9 | 0x1C77      |        7287 |
|      10 | 0x0002      |           2 |
|      11 | 0x1C78      |        7288 |
|      12 | 0x1C83      |        7299 |
|      13 | 0x1C84      |        7300 |
|      14 | 0x1C86      |        7302 |
|      15 | 0x1C85      |        7301 |
|      16 | 0x1C87      |        7303 |
|      17 | 0x2716      |       10006 |
|      18 | 0x2717      |       10007 |
|      19 | 0x2718      |       10008 |
|      20 | 0x0003      |           3 |
|      21 | 0x2719      |       10009 |
|      22 | 0x0004      |           4 |
|      23 | 0x271A      |       10010 |
|      24 | 0x1C8B      |        7307 |
|      25 | 0x000F      |          15 |
|      26 | 0x0005      |           5 |
|      27 | 0x1C8C      |        7308 |
|      28 | 0x1C5F      |        7263 |
|      29 | 0x1C8D      |        7309 |
|      30 | 0x0010      |          16 |
|      31 | 0x001F      |          31 |

## String References

- **7263**: Enter 0 to cancel.
- **7281**: Fusing your $0 with $1 Apollyon Units to create $2.
- **7282**: Proceed? [Yes./No.]
- **7286**: $0 detected. Several equipment items can now be created.
- **7288**: Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Apollyon Units shall be expended in the process.
- **7299**: 
- **7300**: 
- **7301**: 
- **7302**: 
- **7303**: 
- **7308**: 
- **7309**: 

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
  1: 0x0004 [0x1D] PRINT_EVENT_MESSAGE(message_id=7281*)
    → "Fusing your $0 with $1 Apollyon Units to create $2."
  2: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0008 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x000B [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
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
  1: 0x00A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7286*)
    → "$0 detected. Several equipment items can now be created."
  2: 0x00A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00A5 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 07 80 D4 03 03 80...])
  4: 0x00C3 [0x25] WAIT_DIALOG_SELECT()
  5: 0x00C4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0160
  6: 0x00CC [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
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
 32: 0x0168 [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
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
  1: 0x021B [0x1D] PRINT_EVENT_MESSAGE(message_id=7288*)
    → "Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Apollyon Units shall be expended in the process."
  2: 0x021E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x021F [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x0222 [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
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
| Data Size    | 155 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:          93 05 10 1D 0C  80 23 93 01 80 24 0D 80     ......#...$..
02C0: 03 80 01 80 25 02 00 10  01 80 00 39 03 42 03 01  ....%......9.B..
02D0: 10 03 80 43 00 43 01 02  02 10 01 80 00 E7 02 03  ...C.C..........
02E0: 01 10 01 80 01 36 03 2C  F8 FF FF 7F F8 FF FF 7F  .....6.,........
02F0: 69 64 73 32 1C 04 80 2C  F8 FF FF 7F F8 FF FF 7F  ids2...,........
0300: 69 64 73 33 1C 04 80 2C  F8 FF FF 7F F8 FF FF 7F  ids3...,........
0310: 69 64 73 34 1C 04 80 2C  F8 FF FF 7F F8 FF FF 7F  ids4...,........
0320: 73 70 32 31 53 F8 FF FF  7F F8 FF FF 7F 73 70 32  sp21S........sp2
0330: 31 03 01 10 03 80 01 49  03 02 00 10 03 80 00 49  1......I.......I
0340: 03 03 01 10 01 80 01 49  03 2E 20 00 21 00        .......I.. .!.  
```

#### Opcodes

```
  0: 0x02B3 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[5])
  1: 0x02B6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7299*)
    → ""
  2: 0x02B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x02BA [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x02BD [0x24] CREATE_DIALOG(message_id=7300*, default_option=1*, option_flags=0*)
    → ""
  5: 0x02C4 [0x25] WAIT_DIALOG_SELECT()
  6: 0x02C5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0339
  7: 0x02CD [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x02CE [0x03] Work_Zone[1] = 1*
  9: 0x02D3 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x02D5 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x02D7 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x02E7
 12: 0x02DF [0x03] Work_Zone[1] = 0*
 13: 0x02E4 [0x01] GOTO 0x0336
 14: 0x02E7 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x02F4 [0x1C] WAIT(60* ticks)
 16: 0x02F7 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x0304 [0x1C] WAIT(60* ticks)
 18: 0x0307 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x0314 [0x1C] WAIT(60* ticks)
 20: 0x0317 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x0324 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x0331 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0336:
 23: 0x0336 [0x01] GOTO 0x0349
 24: 0x0339 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0349
 25: 0x0341 [0x03] Work_Zone[1] = 0*
 26: 0x0346 [0x01] GOTO 0x0349

SUBROUTINE_0349:
 27: 0x0349 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x034A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x034C [0x21] END_EVENT
 30: 0x034D [0x00] END_REQSTACK()
```

### Event 141

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x034E    |
| Data Size    | 155 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0340:                                            93 04                ..
0350: 10 1D 0E 80 23 93 01 80  24 0D 80 03 80 01 80 25  ....#...$......%
0360: 02 00 10 01 80 00 D4 03  42 03 01 10 03 80 43 00  ........B.....C.
0370: 43 01 02 02 10 01 80 00  82 03 03 01 10 01 80 01  C...............
0380: D1 03 2C F8 FF FF 7F F8  FF FF 7F 69 64 73 32 1C  ..,........ids2.
0390: 04 80 2C F8 FF FF 7F F8  FF FF 7F 69 64 73 33 1C  ..,........ids3.
03A0: 04 80 2C F8 FF FF 7F F8  FF FF 7F 69 64 73 34 1C  ..,........ids4.
03B0: 04 80 2C F8 FF FF 7F F8  FF FF 7F 73 70 32 31 53  ..,........sp21S
03C0: F8 FF FF 7F F8 FF FF 7F  73 70 32 31 03 01 10 03  ........sp21....
03D0: 80 01 E4 03 02 00 10 03  80 00 E4 03 03 01 10 01  ................
03E0: 80 01 E4 03 2E 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x034E [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[4])
  1: 0x0351 [0x1D] PRINT_EVENT_MESSAGE(message_id=7302*)
    → ""
  2: 0x0354 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0355 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x0358 [0x24] CREATE_DIALOG(message_id=7300*, default_option=1*, option_flags=0*)
    → ""
  5: 0x035F [0x25] WAIT_DIALOG_SELECT()
  6: 0x0360 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03D4
  7: 0x0368 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x0369 [0x03] Work_Zone[1] = 1*
  9: 0x036E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0370 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0372 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0382
 12: 0x037A [0x03] Work_Zone[1] = 0*
 13: 0x037F [0x01] GOTO 0x03D1
 14: 0x0382 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x038F [0x1C] WAIT(60* ticks)
 16: 0x0392 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x039F [0x1C] WAIT(60* ticks)
 18: 0x03A2 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x03AF [0x1C] WAIT(60* ticks)
 20: 0x03B2 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x03BF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x03CC [0x03] Work_Zone[1] = 1*

SUBROUTINE_03D1:
 23: 0x03D1 [0x01] GOTO 0x03E4
 24: 0x03D4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03E4
 25: 0x03DC [0x03] Work_Zone[1] = 0*
 26: 0x03E1 [0x01] GOTO 0x03E4

SUBROUTINE_03E4:
 27: 0x03E4 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x03E5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x03E7 [0x21] END_EVENT
 30: 0x03E8 [0x00] END_REQSTACK()
```

### Event 143

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x03E9    |
| Data Size    | 165 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:                             CC 03 06 10 03 10 04           .......
03F0: 10 05 10 1D 0F 80 23 48  10 80 93 01 80 24 02 80  ......#H.....$..
0400: 03 80 01 80 25 02 00 10  01 80 00 79 04 42 03 01  ....%......y.B..
0410: 10 03 80 43 00 43 01 02  02 10 01 80 00 27 04 03  ...C.C.......'..
0420: 01 10 01 80 01 76 04 2C  F8 FF FF 7F F8 FF FF 7F  .....v.,........
0430: 69 64 73 32 1C 04 80 2C  F8 FF FF 7F F8 FF FF 7F  ids2...,........
0440: 69 64 73 33 1C 04 80 2C  F8 FF FF 7F F8 FF FF 7F  ids3...,........
0450: 69 64 73 34 1C 04 80 2C  F8 FF FF 7F F8 FF FF 7F  ids4...,........
0460: 73 70 32 31 53 F8 FF FF  7F F8 FF FF 7F 73 70 32  sp21S........sp2
0470: 31 03 01 10 03 80 01 89  04 02 00 10 03 80 00 89  1...............
0480: 04 03 01 10 01 80 01 89  04 2E 20 00 21 00        .......... .!.  
```

#### Opcodes

```
  0: 0x03E9 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x03 - Open item info window (conditional chase), check_value=Work_Zone[6], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x03F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7301*)
    → ""
  2: 0x03F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x03F7 [0x48] [System] [7303*]:
    → ""
  4: 0x03FA [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  5: 0x03FD [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  6: 0x0404 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0405 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0479
  8: 0x040D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x040E [0x03] Work_Zone[1] = 1*
 10: 0x0413 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x0415 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x0417 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0427
 13: 0x041F [0x03] Work_Zone[1] = 0*
 14: 0x0424 [0x01] GOTO 0x0476
 15: 0x0427 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 16: 0x0434 [0x1C] WAIT(60* ticks)
 17: 0x0437 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 18: 0x0444 [0x1C] WAIT(60* ticks)
 19: 0x0447 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 20: 0x0454 [0x1C] WAIT(60* ticks)
 21: 0x0457 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x0464 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 23: 0x0471 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0476:
 24: 0x0476 [0x01] GOTO 0x0489
 25: 0x0479 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0489
 26: 0x0481 [0x03] Work_Zone[1] = 0*
 27: 0x0486 [0x01] GOTO 0x0489

SUBROUTINE_0489:
 28: 0x0489 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 29: 0x048A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x048C [0x21] END_EVENT
 31: 0x048D [0x00] END_REQSTACK()
```

### Event 145

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x048E    |
| Data Size    | 499 bytes |
| Instructions | 88        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0480:                                            03 00                ..
0490: 00 02 10 03 01 00 03 10  03 06 00 01 80 0C 04 10  ................
04A0: 3C 06 00 04 10 03 80 D4  03 01 80 11 80 D4 03 03  <...............
04B0: 80 12 80 D4 03 0A 80 13  80 D4 03 14 80 15 80 D4  ................
04C0: 03 16 80 17 80 03 02 10  11 80 03 03 10 12 80 03  ................
04D0: 04 10 13 80 03 05 10 15  80 03 06 10 17 80 03 07  ................
04E0: 10 00 00 03 08 10 01 00  03 01 10 01 80 D4 02 18  ................
04F0: 80 01 80 06 00 25 02 00  10 01 80 00 0F 05 40 01  .....%........@.
0500: 80 19 80 01 10 03 80 03  04 00 11 80 01 83 05 02  ................
0510: 00 10 03 80 00 28 05 40  01 80 19 80 01 10 0A 80  .....(.@........
0520: 03 04 00 12 80 01 83 05  02 00 10 0A 80 00 41 05  ..............A.
0530: 40 01 80 19 80 01 10 14  80 03 04 00 13 80 01 83  @...............
0540: 05 02 00 10 14 80 00 5A  05 40 01 80 19 80 01 10  .......Z.@......
0550: 16 80 03 04 00 15 80 01  83 05 02 00 10 16 80 00  ................
0560: 73 05 40 01 80 19 80 01  10 1A 80 03 04 00 17 80  s.@.............
0570: 01 83 05 02 00 10 1A 80  00 83 05 03 01 10 01 80  ................
0580: 01 83 05 02 01 10 01 80  00 8E 05 01 7C 06 03 02  ............|...
0590: 00 01 00 15 02 00 0A 80  03 02 10 02 00 1D 1B 80  ................
05A0: 23 48 1C 80 71 12 03 80  0A 80 71 13 02 10 02 02  #H..q.....q.....
05B0: 10 01 80 00 B9 05 01 7C  06 02 02 10 02 00 05 79  .......|.......y
05C0: 06 03 03 00 02 10 14 03  00 0A 80 03 05 00 02 10  ................
05D0: 03 02 10 00 00 03 03 10  03 00 03 04 10 04 00 03  ................
05E0: 05 10 05 00 1D 1D 80 23  24 0D 80 03 80 01 80 25  .......#$......%
05F0: 02 00 10 01 80 00 68 06  40 1E 80 1F 80 01 10 05  ......h.@.......
0600: 10 42 43 00 43 01 02 02  10 01 80 00 16 06 03 01  .BC.C...........
0610: 10 01 80 01 65 06 2C F8  FF FF 7F F8 FF FF 7F 69  ....e.,........i
0620: 64 73 32 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 69  ds2...,........i
0630: 64 73 33 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 69  ds3...,........i
0640: 64 73 34 1C 04 80 2C F8  FF FF 7F F8 FF FF 7F 73  ds4...,........s
0650: 70 32 31 53 F8 FF FF 7F  F8 FF FF 7F 73 70 32 31  p21S........sp21
0660: 03 01 10 03 80 01 76 06  02 00 10 03 80 00 76 06  ......v.......v.
0670: 01 C5 04 01 76 06 01 7C  06 01 C5 04 2E 20 00 21  ....v..|..... .!
0680: 00                                                .               
```

#### Opcodes

```
  0: 0x048E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0493 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x0498 [0x03] ExtData[1]->WorkLocal[6] = 0*
  3: 0x049D [0x0C] Work_Zone[4]--
  4: 0x04A0 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[6], bit_index_work_offset=Work_Zone[4], condition_work_offset=1*)
  5: 0x04A7 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 11 80 D4 03 03 80...])
  6: 0x04C5 [0x03] Work_Zone[2] = 10006*
  7: 0x04CA [0x03] Work_Zone[3] = 10007*
  8: 0x04CF [0x03] Work_Zone[4] = 10008*
  9: 0x04D4 [0x03] Work_Zone[5] = 10009*
 10: 0x04D9 [0x03] Work_Zone[6] = 10010*
 11: 0x04DE [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[0]
 12: 0x04E3 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[1]
 13: 0x04E8 [0x03] Work_Zone[1] = 0*
 14: 0x04ED [0xD4] MAP_QUERY_WINDOW: Test and open query window (flag=0x18, work=[0x0180, 0x0680, 0x2500])
 15: 0x04F6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x050F
 16: 0x04FE [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 17: 0x0507 [0x03] ExtData[1]->WorkLocal[4] = 10006*
 18: 0x050C [0x01] GOTO 0x0583
 19: 0x050F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0528
 20: 0x0517 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
 21: 0x0520 [0x03] ExtData[1]->WorkLocal[4] = 10007*
 22: 0x0525 [0x01] GOTO 0x0583
 23: 0x0528 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0541
 24: 0x0530 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=3*)
 25: 0x0539 [0x03] ExtData[1]->WorkLocal[4] = 10008*
 26: 0x053E [0x01] GOTO 0x0583
 27: 0x0541 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x055A
 28: 0x0549 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=4*)
 29: 0x0552 [0x03] ExtData[1]->WorkLocal[4] = 10009*
 30: 0x0557 [0x01] GOTO 0x0583
 31: 0x055A [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0573
 32: 0x0562 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=5*)
 33: 0x056B [0x03] ExtData[1]->WorkLocal[4] = 10010*
 34: 0x0570 [0x01] GOTO 0x0583
 35: 0x0573 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0583
 36: 0x057B [0x03] Work_Zone[1] = 0*
 37: 0x0580 [0x01] GOTO 0x0583

SUBROUTINE_0583:
 38: 0x0583 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x058E
 39: 0x058B [0x01] GOTO 0x067C
 40: 0x058E [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
 41: 0x0593 [0x15] ExtData[1]->WorkLocal[2] /= 2*
 42: 0x0598 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 43: 0x059D [0x1D] PRINT_EVENT_MESSAGE(message_id=7308*)
    → ""
 44: 0x05A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x05A1 [0x48] [System] [7263*]:
    → "Enter 0 to cancel."
 46: 0x05A4 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 47: 0x05AA [0x71] USER_INPUT_HANDLER: Process numerical input B (work=Work_Zone[2])
 48: 0x05AE [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x05B9
 49: 0x05B6 [0x01] GOTO 0x067C
 50: 0x05B9 [0x02] IF !(Work_Zone[2] > ExtData[1]->WorkLocal[2]) GOTO 0x0679
 51: 0x05C1 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[2]
 52: 0x05C6 [0x14] ExtData[1]->WorkLocal[3] *= 2*
 53: 0x05CB [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[2]
 54: 0x05D0 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 55: 0x05D5 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[3]
 56: 0x05DA [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[4]
 57: 0x05DF [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[5]
 58: 0x05E4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7309*)
    → ""
 59: 0x05E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x05E8 [0x24] CREATE_DIALOG(message_id=7300*, default_option=1*, option_flags=0*)
    → ""
 61: 0x05EF [0x25] WAIT_DIALOG_SELECT()
 62: 0x05F0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0668
 63: 0x05F8 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=Work_Zone[5])
 64: 0x0601 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 65: 0x0602 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 66: 0x0604 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 67: 0x0606 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0616
 68: 0x060E [0x03] Work_Zone[1] = 0*
 69: 0x0613 [0x01] GOTO 0x0665
 70: 0x0616 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 71: 0x0623 [0x1C] WAIT(60* ticks)
 72: 0x0626 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 73: 0x0633 [0x1C] WAIT(60* ticks)
 74: 0x0636 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 75: 0x0643 [0x1C] WAIT(60* ticks)
 76: 0x0646 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 77: 0x0653 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 78: 0x0660 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0665:
 79: 0x0665 [0x01] GOTO 0x0676
 80: 0x0668 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0676
 81: 0x0670 [0x01] GOTO 0x04C5

SUBROUTINE_0676:
 82: 0x0676 [0x01] GOTO 0x067C
 83: 0x0679 [0x01] GOTO 0x04C5

SUBROUTINE_067C:
 84: 0x067C [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 85: 0x067D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 86: 0x067F [0x21] END_EVENT
 87: 0x0680 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0673 [0x01] GOTO 0x0676
```
