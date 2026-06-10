# 16929577 - Temenos Furnace

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 1892 bytes       |
| Total Events     | 8                |
| References Count | 34               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1033](#event-1033)   | 0x0001       |    169 |             31 |
| [1034](#event-1034)   | 0x00AA       |    366 |             63 |
| [1035](#event-1035)   | 0x0218       |    162 |             31 |
| [1036](#event-1036)   | 0x02BA       |    170 |             35 |
| [1037](#event-1037)   | 0x0364       |    155 |             31 |
| [1038](#event-1038)   | 0x03FF       |    165 |             32 |
| [1039](#event-1039)   | 0x04A4       |    517 |             92 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C6D      |        7277 |
|       1 | 0x0000      |           0 |
|       2 | 0x1C6E      |        7278 |
|       3 | 0x0001      |           1 |
|       4 | 0x003C      |          60 |
|       5 | 0x270F      |        9999 |
|       6 | 0x1C72      |        7282 |
|       7 | 0x6607      |       26119 |
|       8 | 0x66A3      |       26275 |
|       9 | 0x1C73      |        7283 |
|      10 | 0x0002      |           2 |
|      11 | 0x1C74      |        7284 |
|      12 | 0x1C80      |        7296 |
|      13 | 0x1C9E      |        7326 |
|      14 | 0x1C81      |        7297 |
|      15 | 0x1C82      |        7298 |
|      16 | 0x1C83      |        7299 |
|      17 | 0x1C84      |        7300 |
|      18 | 0x2716      |       10006 |
|      19 | 0x2717      |       10007 |
|      20 | 0x2718      |       10008 |
|      21 | 0x0003      |           3 |
|      22 | 0x2719      |       10009 |
|      23 | 0x0004      |           4 |
|      24 | 0x271A      |       10010 |
|      25 | 0x1C88      |        7304 |
|      26 | 0x000F      |          15 |
|      27 | 0x0005      |           5 |
|      28 | 0x0063      |          99 |
|      29 | 0x1C89      |        7305 |
|      30 | 0x1C5B      |        7259 |
|      31 | 0x1C8A      |        7306 |
|      32 | 0x0010      |          16 |
|      33 | 0x001F      |          31 |

## String References

- **7259**: Enter 0 to cancel.
- **7277**: Fusing your $0 with $1 Temenos Units to create $2.
- **7278**: Proceed? [Yes./No.]
- **7282**: # detected. Several equipment items can now be created.
- **7284**: Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Temenos Units shall be expended in the process.
- **7296**: Confirming $0, $1, and $2. Able to create $3.
- **7297**: What will you do? [Create./Do not create.]
- **7298**: Confirming $0, $1... Able to create $2.
- **7299**: Carrying over attributes from the $0 to the $4.
- **7300**: Your $0 will be consumed.
- **7305**: Able to change up to $0.
- **7306**: Changing $1 $0 into $3 $0 .
- **7326**: #, $1, and all five types of shards confirmed. Able to create $3.

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

### Event 1033

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 169 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    CC 01 04 10 05 10 06  10 07 10 1D 00 80 23 CC   .............#.
0010: 01 01 80 01 80 01 80 01  80 24 02 80 03 80 01 80  .........$......
0020: 25 02 00 10 01 80 00 95  00 42 03 01 10 03 80 43  %........B.....C
0030: 00 43 01 02 02 10 01 80  00 43 00 03 01 10 01 80  .C.......C......
0040: 01 92 00 2C F8 FF FF 7F  F8 FF FF 7F 69 64 73 32  ...,........ids2
0050: 1C 04 80 2C F8 FF FF 7F  F8 FF FF 7F 69 64 73 33  ...,........ids3
0060: 1C 04 80 2C F8 FF FF 7F  F8 FF FF 7F 69 64 73 34  ...,........ids4
0070: 1C 04 80 2C F8 FF FF 7F  F8 FF FF 7F 73 70 32 31  ...,........sp21
0080: 53 F8 FF FF 7F F8 FF FF  7F 73 70 32 31 03 01 10  S........sp21...
0090: 03 80 01 A5 00 02 00 10  03 80 00 A5 00 03 01 10  ................
00A0: 01 80 01 A5 00 2E 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x0001 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=Work_Zone[4], buffer1=Work_Zone[5], buffer2=Work_Zone[6], buffer3=Work_Zone[7])
  1: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=7277*)
    → "Fusing your $0 with $1 Temenos Units to create $2."
  2: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000F [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=0*, buffer1=0*, buffer2=0*, buffer3=0*)
  4: 0x0019 [0x24] CREATE_DIALOG(message_id=7278*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  5: 0x0020 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0021 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0095
  7: 0x0029 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x002A [0x03] Work_Zone[1] = 1*
  9: 0x002F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0031 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0033 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0043
 12: 0x003B [0x03] Work_Zone[1] = 0*
 13: 0x0040 [0x01] GOTO 0x0092
 14: 0x0043 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x0050 [0x1C] WAIT(60* ticks)
 16: 0x0053 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x0060 [0x1C] WAIT(60* ticks)
 18: 0x0063 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x0070 [0x1C] WAIT(60* ticks)
 20: 0x0073 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x0080 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x008D [0x03] Work_Zone[1] = 1*

SUBROUTINE_0092:
 23: 0x0092 [0x01] GOTO 0x00A5
 24: 0x0095 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A5
 25: 0x009D [0x03] Work_Zone[1] = 0*
 26: 0x00A2 [0x01] GOTO 0x00A5

SUBROUTINE_00A5:
 27: 0x00A5 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x00A6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x00A8 [0x21] END_EVENT
 30: 0x00A9 [0x00] END_REQSTACK()
```

### Event 1034

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00AA    |
| Data Size    | 366 bytes |
| Instructions | 63        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                03 02 10 05 80 1D            ......
00B0: 06 80 23 D4 03 01 80 07  80 D4 03 03 80 08 80 03  ..#.............
00C0: 02 10 07 80 03 03 10 08  80 D4 02 09 80 0A 80 01  ................
00D0: 80 25 02 00 10 01 80 00  69 01 24 02 80 03 80 01  .%......i.$.....
00E0: 80 25 02 00 10 01 80 00  56 01 42 03 01 10 03 80  .%......V.B.....
00F0: 43 00 43 01 02 02 10 01  80 00 04 01 03 01 10 01  C.C.............
0100: 80 01 53 01 2C F8 FF FF  7F F8 FF FF 7F 69 64 73  ..S.,........ids
0110: 32 1C 04 80 2C F8 FF FF  7F F8 FF FF 7F 69 64 73  2...,........ids
0120: 33 1C 04 80 2C F8 FF FF  7F F8 FF FF 7F 69 64 73  3...,........ids
0130: 34 1C 04 80 2C F8 FF FF  7F F8 FF FF 7F 73 70 32  4...,........sp2
0140: 31 53 F8 FF FF 7F F8 FF  FF 7F 73 70 32 31 03 01  1S........sp21..
0150: 10 03 80 01 66 01 02 00  10 03 80 00 66 01 03 01  ....f.......f...
0160: 10 01 80 01 66 01 01 13  02 02 00 10 03 80 00 03  ....f...........
0170: 02 24 02 80 03 80 01 80  25 02 00 10 01 80 00 ED  .$......%.......
0180: 01 42 03 01 10 0A 80 43  00 43 01 02 02 10 01 80  .B.....C.C......
0190: 00 9B 01 03 01 10 01 80  01 EA 01 2C F8 FF FF 7F  ...........,....
01A0: F8 FF FF 7F 69 64 73 32  1C 04 80 2C F8 FF FF 7F  ....ids2...,....
01B0: F8 FF FF 7F 69 64 73 33  1C 04 80 2C F8 FF FF 7F  ....ids3...,....
01C0: F8 FF FF 7F 69 64 73 34  1C 04 80 2C F8 FF FF 7F  ....ids4...,....
01D0: F8 FF FF 7F 73 70 32 31  53 F8 FF FF 7F F8 FF FF  ....sp21S.......
01E0: 7F 73 70 32 31 03 01 10  03 80 01 00 02 02 00 10  .sp21...........
01F0: 03 80 00 00 02 93 01 80  03 01 10 01 80 01 00 02  ................
0200: 01 13 02 02 00 10 0A 80  00 13 02 03 01 10 01 80  ................
0210: 01 13 02 2E 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x00AA [0x03] Work_Zone[2] = 9999*
  1: 0x00AF [0x1D] PRINT_EVENT_MESSAGE(message_id=7282*)
    → "# detected. Several equipment items can now be created."
  2: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B3 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 07 80 D4 03 03 80...])
  4: 0x00D1 [0x25] WAIT_DIALOG_SELECT()
  5: 0x00D2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0169
  6: 0x00DA [0x24] CREATE_DIALOG(message_id=7278*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  7: 0x00E1 [0x25] WAIT_DIALOG_SELECT()
  8: 0x00E2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0156
  9: 0x00EA [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x00EB [0x03] Work_Zone[1] = 1*
 11: 0x00F0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x00F2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x00F4 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0104
 14: 0x00FC [0x03] Work_Zone[1] = 0*
 15: 0x0101 [0x01] GOTO 0x0153
 16: 0x0104 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 17: 0x0111 [0x1C] WAIT(60* ticks)
 18: 0x0114 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 19: 0x0121 [0x1C] WAIT(60* ticks)
 20: 0x0124 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 21: 0x0131 [0x1C] WAIT(60* ticks)
 22: 0x0134 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 23: 0x0141 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 24: 0x014E [0x03] Work_Zone[1] = 1*

SUBROUTINE_0153:
 25: 0x0153 [0x01] GOTO 0x0166
 26: 0x0156 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0166
 27: 0x015E [0x03] Work_Zone[1] = 0*
 28: 0x0163 [0x01] GOTO 0x0166

SUBROUTINE_0166:
 29: 0x0166 [0x01] GOTO 0x0213
 30: 0x0169 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0203
 31: 0x0171 [0x24] CREATE_DIALOG(message_id=7278*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
 32: 0x0178 [0x25] WAIT_DIALOG_SELECT()
 33: 0x0179 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01ED
 34: 0x0181 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 35: 0x0182 [0x03] Work_Zone[1] = 2*
 36: 0x0187 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 37: 0x0189 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 38: 0x018B [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x019B
 39: 0x0193 [0x03] Work_Zone[1] = 0*
 40: 0x0198 [0x01] GOTO 0x01EA
 41: 0x019B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 42: 0x01A8 [0x1C] WAIT(60* ticks)
 43: 0x01AB [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 44: 0x01B8 [0x1C] WAIT(60* ticks)
 45: 0x01BB [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 46: 0x01C8 [0x1C] WAIT(60* ticks)
 47: 0x01CB [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 48: 0x01D8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 49: 0x01E5 [0x03] Work_Zone[1] = 1*

SUBROUTINE_01EA:
 50: 0x01EA [0x01] GOTO 0x0200
 51: 0x01ED [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0200
 52: 0x01F5 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 53: 0x01F8 [0x03] Work_Zone[1] = 0*
 54: 0x01FD [0x01] GOTO 0x0200

SUBROUTINE_0200:
 55: 0x0200 [0x01] GOTO 0x0213
 56: 0x0203 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0213
 57: 0x020B [0x03] Work_Zone[1] = 0*
 58: 0x0210 [0x01] GOTO 0x0213

SUBROUTINE_0213:
 59: 0x0213 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 60: 0x0214 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 61: 0x0216 [0x21] END_EVENT
 62: 0x0217 [0x00] END_REQSTACK()
```

### Event 1035

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0218    |
| Data Size    | 162 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                          CC 03 02 10 03 10 04 10          ........
0220: 05 10 1D 0B 80 23 93 01  80 24 02 80 03 80 01 80  .....#...$......
0230: 25 02 00 10 01 80 00 A5  02 42 03 01 10 03 80 43  %........B.....C
0240: 00 43 01 02 02 10 01 80  00 53 02 03 01 10 01 80  .C.......S......
0250: 01 A2 02 2C F8 FF FF 7F  F8 FF FF 7F 69 64 73 32  ...,........ids2
0260: 1C 04 80 2C F8 FF FF 7F  F8 FF FF 7F 69 64 73 33  ...,........ids3
0270: 1C 04 80 2C F8 FF FF 7F  F8 FF FF 7F 69 64 73 34  ...,........ids4
0280: 1C 04 80 2C F8 FF FF 7F  F8 FF FF 7F 73 70 32 31  ...,........sp21
0290: 53 F8 FF FF 7F F8 FF FF  7F 73 70 32 31 03 01 10  S........sp21...
02A0: 03 80 01 B5 02 02 00 10  03 80 00 B5 02 03 01 10  ................
02B0: 01 80 01 B5 02 2E 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x0218 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x03 - Open item info window (conditional chase), check_value=Work_Zone[2], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x0222 [0x1D] PRINT_EVENT_MESSAGE(message_id=7284*)
    → "Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Temenos Units shall be expended in the process."
  2: 0x0225 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0226 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x0229 [0x24] CREATE_DIALOG(message_id=7278*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  5: 0x0230 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0231 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02A5
  7: 0x0239 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x023A [0x03] Work_Zone[1] = 1*
  9: 0x023F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0241 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0243 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0253
 12: 0x024B [0x03] Work_Zone[1] = 0*
 13: 0x0250 [0x01] GOTO 0x02A2
 14: 0x0253 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x0260 [0x1C] WAIT(60* ticks)
 16: 0x0263 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x0270 [0x1C] WAIT(60* ticks)
 18: 0x0273 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x0280 [0x1C] WAIT(60* ticks)
 20: 0x0283 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x0290 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x029D [0x03] Work_Zone[1] = 1*

SUBROUTINE_02A2:
 23: 0x02A2 [0x01] GOTO 0x02B5
 24: 0x02A5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02B5
 25: 0x02AD [0x03] Work_Zone[1] = 0*
 26: 0x02B2 [0x01] GOTO 0x02B5

SUBROUTINE_02B5:
 27: 0x02B5 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x02B6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x02B8 [0x21] END_EVENT
 30: 0x02B9 [0x00] END_REQSTACK()
```

### Event 1036

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02BA    |
| Data Size    | 170 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                                93 05 10 02 06 10            ......
02C0: 01 80 00 CC 02 1D 0C 80  23 01 D0 02 1D 0D 80 23  ........#......#
02D0: 93 01 80 24 0E 80 03 80  01 80 25 02 00 10 01 80  ...$......%.....
02E0: 00 4F 03 42 03 01 10 03  80 43 00 43 01 02 02 10  .O.B.....C.C....
02F0: 01 80 00 FD 02 03 01 10  01 80 01 4C 03 2C F8 FF  ...........L.,..
0300: FF 7F F8 FF FF 7F 69 64  73 32 1C 04 80 2C F8 FF  ......ids2...,..
0310: FF 7F F8 FF FF 7F 69 64  73 33 1C 04 80 2C F8 FF  ......ids3...,..
0320: FF 7F F8 FF FF 7F 69 64  73 34 1C 04 80 2C F8 FF  ......ids4...,..
0330: FF 7F F8 FF FF 7F 73 70  32 31 53 F8 FF FF 7F F8  ......sp21S.....
0340: FF FF 7F 73 70 32 31 03  01 10 03 80 01 5F 03 02  ...sp21......_..
0350: 00 10 03 80 00 5F 03 03  01 10 01 80 01 5F 03 2E  ....._......._..
0360: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x02BA [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[5])
  1: 0x02BD [0x02] IF !(Work_Zone[6] == 0*) GOTO 0x02CC
  2: 0x02C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7296*)
    → "Confirming $0, $1, and $2. Able to create $3."
  3: 0x02C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x02C9 [0x01] GOTO 0x02D0
  5: 0x02CC [0x1D] PRINT_EVENT_MESSAGE(message_id=7326*)
    → "#, $1, and all five types of shards confirmed. Able to create $3."
  6: 0x02CF [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_02D0:
  7: 0x02D0 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  8: 0x02D3 [0x24] CREATE_DIALOG(message_id=7297*, default_option=1*, option_flags=0*)
    → "What will you do? [Create./Do not create.]"
  9: 0x02DA [0x25] WAIT_DIALOG_SELECT()
 10: 0x02DB [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x034F
 11: 0x02E3 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x02E4 [0x03] Work_Zone[1] = 1*
 13: 0x02E9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 14: 0x02EB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 15: 0x02ED [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x02FD
 16: 0x02F5 [0x03] Work_Zone[1] = 0*
 17: 0x02FA [0x01] GOTO 0x034C
 18: 0x02FD [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 19: 0x030A [0x1C] WAIT(60* ticks)
 20: 0x030D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 21: 0x031A [0x1C] WAIT(60* ticks)
 22: 0x031D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 23: 0x032A [0x1C] WAIT(60* ticks)
 24: 0x032D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 25: 0x033A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 26: 0x0347 [0x03] Work_Zone[1] = 1*

SUBROUTINE_034C:
 27: 0x034C [0x01] GOTO 0x035F
 28: 0x034F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x035F
 29: 0x0357 [0x03] Work_Zone[1] = 0*
 30: 0x035C [0x01] GOTO 0x035F

SUBROUTINE_035F:
 31: 0x035F [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 32: 0x0360 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x0362 [0x21] END_EVENT
 34: 0x0363 [0x00] END_REQSTACK()
```

### Event 1037

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0364    |
| Data Size    | 155 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0360:             93 04 10 1D  0F 80 23 93 01 80 24 0E      ......#...$.
0370: 80 03 80 01 80 25 02 00  10 01 80 00 EA 03 42 03  .....%........B.
0380: 01 10 03 80 43 00 43 01  02 02 10 01 80 00 98 03  ....C.C.........
0390: 03 01 10 01 80 01 E7 03  2C F8 FF FF 7F F8 FF FF  ........,.......
03A0: 7F 69 64 73 32 1C 04 80  2C F8 FF FF 7F F8 FF FF  .ids2...,.......
03B0: 7F 69 64 73 33 1C 04 80  2C F8 FF FF 7F F8 FF FF  .ids3...,.......
03C0: 7F 69 64 73 34 1C 04 80  2C F8 FF FF 7F F8 FF FF  .ids4...,.......
03D0: 7F 73 70 32 31 53 F8 FF  FF 7F F8 FF FF 7F 73 70  .sp21S........sp
03E0: 32 31 03 01 10 03 80 01  FA 03 02 00 10 03 80 00  21..............
03F0: FA 03 03 01 10 01 80 01  FA 03 2E 20 00 21 00     ........... .!. 
```

#### Opcodes

```
  0: 0x0364 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[4])
  1: 0x0367 [0x1D] PRINT_EVENT_MESSAGE(message_id=7298*)
    → "Confirming $0, $1... Able to create $2."
  2: 0x036A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x036B [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x036E [0x24] CREATE_DIALOG(message_id=7297*, default_option=1*, option_flags=0*)
    → "What will you do? [Create./Do not create.]"
  5: 0x0375 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0376 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03EA
  7: 0x037E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x037F [0x03] Work_Zone[1] = 1*
  9: 0x0384 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0386 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0388 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0398
 12: 0x0390 [0x03] Work_Zone[1] = 0*
 13: 0x0395 [0x01] GOTO 0x03E7
 14: 0x0398 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x03A5 [0x1C] WAIT(60* ticks)
 16: 0x03A8 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x03B5 [0x1C] WAIT(60* ticks)
 18: 0x03B8 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x03C5 [0x1C] WAIT(60* ticks)
 20: 0x03C8 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x03D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x03E2 [0x03] Work_Zone[1] = 1*

SUBROUTINE_03E7:
 23: 0x03E7 [0x01] GOTO 0x03FA
 24: 0x03EA [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03FA
 25: 0x03F2 [0x03] Work_Zone[1] = 0*
 26: 0x03F7 [0x01] GOTO 0x03FA

SUBROUTINE_03FA:
 27: 0x03FA [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x03FB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x03FD [0x21] END_EVENT
 30: 0x03FE [0x00] END_REQSTACK()
```

### Event 1038

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x03FF    |
| Data Size    | 165 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03F0:                                               CC                 .
0400: 03 06 10 03 10 04 10 05  10 1D 10 80 23 48 11 80  ............#H..
0410: 93 01 80 24 02 80 03 80  01 80 25 02 00 10 01 80  ...$......%.....
0420: 00 8F 04 42 03 01 10 03  80 43 00 43 01 02 02 10  ...B.....C.C....
0430: 01 80 00 3D 04 03 01 10  01 80 01 8C 04 2C F8 FF  ...=.........,..
0440: FF 7F F8 FF FF 7F 69 64  73 32 1C 04 80 2C F8 FF  ......ids2...,..
0450: FF 7F F8 FF FF 7F 69 64  73 33 1C 04 80 2C F8 FF  ......ids3...,..
0460: FF 7F F8 FF FF 7F 69 64  73 34 1C 04 80 2C F8 FF  ......ids4...,..
0470: FF 7F F8 FF FF 7F 73 70  32 31 53 F8 FF FF 7F F8  ......sp21S.....
0480: FF FF 7F 73 70 32 31 03  01 10 03 80 01 9F 04 02  ...sp21.........
0490: 00 10 03 80 00 9F 04 03  01 10 01 80 01 9F 04 2E  ................
04A0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x03FF [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x03 - Open item info window (conditional chase), check_value=Work_Zone[6], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x0409 [0x1D] PRINT_EVENT_MESSAGE(message_id=7299*)
    → "Carrying over attributes from the $0 to the $4."
  2: 0x040C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x040D [0x48] [System] [7300*]:
    → "Your $0 will be consumed."
  4: 0x0410 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  5: 0x0413 [0x24] CREATE_DIALOG(message_id=7278*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  6: 0x041A [0x25] WAIT_DIALOG_SELECT()
  7: 0x041B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x048F
  8: 0x0423 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0424 [0x03] Work_Zone[1] = 1*
 10: 0x0429 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x042B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x042D [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x043D
 13: 0x0435 [0x03] Work_Zone[1] = 0*
 14: 0x043A [0x01] GOTO 0x048C
 15: 0x043D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 16: 0x044A [0x1C] WAIT(60* ticks)
 17: 0x044D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 18: 0x045A [0x1C] WAIT(60* ticks)
 19: 0x045D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 20: 0x046A [0x1C] WAIT(60* ticks)
 21: 0x046D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x047A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 23: 0x0487 [0x03] Work_Zone[1] = 1*

SUBROUTINE_048C:
 24: 0x048C [0x01] GOTO 0x049F
 25: 0x048F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x049F
 26: 0x0497 [0x03] Work_Zone[1] = 0*
 27: 0x049C [0x01] GOTO 0x049F

SUBROUTINE_049F:
 28: 0x049F [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 29: 0x04A0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x04A2 [0x21] END_EVENT
 31: 0x04A3 [0x00] END_REQSTACK()
```

### Event 1039

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x04A4    |
| Data Size    | 517 bytes |
| Instructions | 91        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04A0:             03 01 00 02  10 03 02 00 03 10 03 00      ............
04B0: 00 01 80 0C 04 10 3C 00  00 04 10 03 80 D4 03 01  ......<.........
04C0: 80 12 80 D4 03 03 80 13  80 D4 03 0A 80 14 80 D4  ................
04D0: 03 15 80 16 80 D4 03 17  80 18 80 03 02 10 12 80  ................
04E0: 03 03 10 13 80 03 04 10  14 80 03 05 10 16 80 03  ................
04F0: 06 10 18 80 03 07 10 01  00 03 08 10 02 00 03 01  ................
0500: 10 01 80 D4 02 19 80 01  80 00 00 25 02 00 10 01  ...........%....
0510: 80 00 25 05 40 01 80 1A  80 01 10 03 80 03 05 00  ..%.@...........
0520: 12 80 01 99 05 02 00 10  03 80 00 3E 05 40 01 80  ...........>.@..
0530: 1A 80 01 10 0A 80 03 05  00 13 80 01 99 05 02 00  ................
0540: 10 0A 80 00 57 05 40 01  80 1A 80 01 10 15 80 03  ....W.@.........
0550: 05 00 14 80 01 99 05 02  00 10 15 80 00 70 05 40  .............p.@
0560: 01 80 1A 80 01 10 17 80  03 05 00 16 80 01 99 05  ................
0570: 02 00 10 17 80 00 89 05  40 01 80 1A 80 01 10 1B  ........@.......
0580: 80 03 05 00 18 80 01 99  05 02 00 10 1B 80 00 99  ................
0590: 05 03 01 10 01 80 01 99  05 02 01 10 01 80 00 A4  ................
05A0: 05 01 A4 06 03 03 00 02  00 15 03 00 0A 80 02 03  ................
05B0: 00 1C 80 04 BB 05 03 03  00 1C 80 03 02 10 03 00  ................
05C0: 1D 1D 80 23 48 1E 80 71  12 03 80 0A 80 71 13 02  ...#H..q.....q..
05D0: 10 02 02 10 01 80 00 E1  05 03 01 10 01 80 01 A4  ................
05E0: 06 02 02 10 03 00 05 A1  06 03 04 00 02 10 14 04  ................
05F0: 00 0A 80 03 06 00 02 10  03 02 10 01 00 03 03 10  ................
0600: 04 00 03 04 10 05 00 03  05 10 06 00 1D 1F 80 23  ...............#
0610: 24 0E 80 03 80 01 80 25  02 00 10 01 80 00 90 06  $......%........
0620: 40 20 80 21 80 01 10 05  10 42 43 00 43 01 02 02  @ .!.....BC.C...
0630: 10 01 80 00 3E 06 03 01  10 01 80 01 8D 06 2C F8  ....>.........,.
0640: FF FF 7F F8 FF FF 7F 69  64 73 32 1C 04 80 2C F8  .......ids2...,.
0650: FF FF 7F F8 FF FF 7F 69  64 73 33 1C 04 80 2C F8  .......ids3...,.
0660: FF FF 7F F8 FF FF 7F 69  64 73 34 1C 04 80 2C F8  .......ids4...,.
0670: FF FF 7F F8 FF FF 7F 73  70 32 31 53 F8 FF FF 7F  .......sp21S....
0680: F8 FF FF 7F 73 70 32 31  03 01 10 03 80 01 9E 06  ....sp21........
0690: 02 00 10 03 80 00 9E 06  01 DB 04 01 9E 06 01 A4  ................
06A0: 06 01 DB 04 2E 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x04A4 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
  1: 0x04A9 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[3]
  2: 0x04AE [0x03] ExtData[1]->WorkLocal[0] = 0*
  3: 0x04B3 [0x0C] Work_Zone[4]--
  4: 0x04B6 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=Work_Zone[4], condition_work_offset=1*)
  5: 0x04BD [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 12 80 D4 03 03 80...])
  6: 0x04DB [0x03] Work_Zone[2] = 10006*
  7: 0x04E0 [0x03] Work_Zone[3] = 10007*
  8: 0x04E5 [0x03] Work_Zone[4] = 10008*
  9: 0x04EA [0x03] Work_Zone[5] = 10009*
 10: 0x04EF [0x03] Work_Zone[6] = 10010*
 11: 0x04F4 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[1]
 12: 0x04F9 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[2]
 13: 0x04FE [0x03] Work_Zone[1] = 0*
 14: 0x0503 [0xD4] MAP_QUERY_WINDOW: Test and open query window (flag=0x19, work=[0x0180, 0x80, 0x2500])
 15: 0x050C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0525
 16: 0x0514 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 17: 0x051D [0x03] ExtData[1]->WorkLocal[5] = 10006*
 18: 0x0522 [0x01] GOTO 0x0599
 19: 0x0525 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x053E
 20: 0x052D [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
 21: 0x0536 [0x03] ExtData[1]->WorkLocal[5] = 10007*
 22: 0x053B [0x01] GOTO 0x0599
 23: 0x053E [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0557
 24: 0x0546 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=3*)
 25: 0x054F [0x03] ExtData[1]->WorkLocal[5] = 10008*
 26: 0x0554 [0x01] GOTO 0x0599
 27: 0x0557 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0570
 28: 0x055F [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=4*)
 29: 0x0568 [0x03] ExtData[1]->WorkLocal[5] = 10009*
 30: 0x056D [0x01] GOTO 0x0599
 31: 0x0570 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0589
 32: 0x0578 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=5*)
 33: 0x0581 [0x03] ExtData[1]->WorkLocal[5] = 10010*
 34: 0x0586 [0x01] GOTO 0x0599
 35: 0x0589 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0599
 36: 0x0591 [0x03] Work_Zone[1] = 0*
 37: 0x0596 [0x01] GOTO 0x0599

SUBROUTINE_0599:
 38: 0x0599 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x05A4
 39: 0x05A1 [0x01] GOTO 0x06A4
 40: 0x05A4 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[2]
 41: 0x05A9 [0x15] ExtData[1]->WorkLocal[3] /= 2*
 42: 0x05AE [0x02] IF !(ExtData[1]->WorkLocal[3] < 99*) GOTO 0x05BB
 43: 0x05B6 [0x03] ExtData[1]->WorkLocal[3] = 99*
 44: 0x05BB [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[3]
 45: 0x05C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7305*)
    → "Able to change up to $0."
 46: 0x05C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x05C4 [0x48] [System] [7259*]:
    → "Enter 0 to cancel."
 48: 0x05C7 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 49: 0x05CD [0x71] USER_INPUT_HANDLER: Process numerical input B (work=Work_Zone[2])
 50: 0x05D1 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x05E1
 51: 0x05D9 [0x03] Work_Zone[1] = 0*
 52: 0x05DE [0x01] GOTO 0x06A4
 53: 0x05E1 [0x02] IF !(Work_Zone[2] > ExtData[1]->WorkLocal[3]) GOTO 0x06A1
 54: 0x05E9 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[2]
 55: 0x05EE [0x14] ExtData[1]->WorkLocal[4] *= 2*
 56: 0x05F3 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[2]
 57: 0x05F8 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 58: 0x05FD [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[4]
 59: 0x0602 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[5]
 60: 0x0607 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[6]
 61: 0x060C [0x1D] PRINT_EVENT_MESSAGE(message_id=7306*)
    → "Changing $1 $0 into $3 $0 ."
 62: 0x060F [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x0610 [0x24] CREATE_DIALOG(message_id=7297*, default_option=1*, option_flags=0*)
    → "What will you do? [Create./Do not create.]"
 64: 0x0617 [0x25] WAIT_DIALOG_SELECT()
 65: 0x0618 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0690
 66: 0x0620 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=Work_Zone[5])
 67: 0x0629 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 68: 0x062A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 69: 0x062C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 70: 0x062E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x063E
 71: 0x0636 [0x03] Work_Zone[1] = 0*
 72: 0x063B [0x01] GOTO 0x068D
 73: 0x063E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 74: 0x064B [0x1C] WAIT(60* ticks)
 75: 0x064E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 76: 0x065B [0x1C] WAIT(60* ticks)
 77: 0x065E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 78: 0x066B [0x1C] WAIT(60* ticks)
 79: 0x066E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 80: 0x067B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 81: 0x0688 [0x03] Work_Zone[1] = 1*

SUBROUTINE_068D:
 82: 0x068D [0x01] GOTO 0x069E
 83: 0x0690 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x069E
 84: 0x0698 [0x01] GOTO 0x04DB

SUBROUTINE_069E:
 85: 0x069E [0x01] GOTO 0x06A4
 86: 0x06A1 [0x01] GOTO 0x04DB

SUBROUTINE_06A4:
 87: 0x06A4 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 88: 0x06A5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 89: 0x06A7 [0x21] END_EVENT
 90: 0x06A8 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x069B [0x01] GOTO 0x069E
```
