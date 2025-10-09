# 16929565 - Temenos Furnace

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 1848 bytes       |
| Total Events     | 8                |
| References Count | 32               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1033](#event-1033)   | 0x0001       |    169 |             31 |
| [1034](#event-1034)   | 0x00AA       |    366 |             63 |
| [1035](#event-1035)   | 0x0218       |    162 |             31 |
| [1036](#event-1036)   | 0x02BA       |    155 |             31 |
| [1037](#event-1037)   | 0x0355       |    155 |             31 |
| [1038](#event-1038)   | 0x03F0       |    165 |             32 |
| [1039](#event-1039)   | 0x0495       |    499 |             89 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C69      |        7273 |
|       1 | 0x0000      |           0 |
|       2 | 0x1C6A      |        7274 |
|       3 | 0x0001      |           1 |
|       4 | 0x003C      |          60 |
|       5 | 0x270F      |        9999 |
|       6 | 0x1C6E      |        7278 |
|       7 | 0x6607      |       26119 |
|       8 | 0x66A3      |       26275 |
|       9 | 0x1C6F      |        7279 |
|      10 | 0x0002      |           2 |
|      11 | 0x1C70      |        7280 |
|      12 | 0x1C7B      |        7291 |
|      13 | 0x1C7C      |        7292 |
|      14 | 0x1C7E      |        7294 |
|      15 | 0x1C7D      |        7293 |
|      16 | 0x1C7F      |        7295 |
|      17 | 0x2716      |       10006 |
|      18 | 0x2717      |       10007 |
|      19 | 0x2718      |       10008 |
|      20 | 0x0003      |           3 |
|      21 | 0x2719      |       10009 |
|      22 | 0x0004      |           4 |
|      23 | 0x271A      |       10010 |
|      24 | 0x1C83      |        7299 |
|      25 | 0x000F      |          15 |
|      26 | 0x0005      |           5 |
|      27 | 0x1C84      |        7300 |
|      28 | 0x1C57      |        7255 |
|      29 | 0x1C85      |        7301 |
|      30 | 0x0010      |          16 |
|      31 | 0x001F      |          31 |

## String References

- **7255**: Enter 0 to cancel.
- **7273**: Fusing your $0 with $1 Apollyon Units to create $2.
- **7274**: Proceed? [Yes./No.]
- **7278**: $0 detected. Several equipment items can now be created.
- **7280**: Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Temenos Units shall be expended in the process.
- **7291**: 
- **7292**: 
- **7293**: 
- **7294**: 
- **7295**: 
- **7300**: 
- **7301**: 

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
  1: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=7273*)
    → "Fusing your $0 with $1 Apollyon Units to create $2."
  2: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000F [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=0*, buffer1=0*, buffer2=0*, buffer3=0*)
  4: 0x0019 [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
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
  1: 0x00AF [0x1D] PRINT_EVENT_MESSAGE(message_id=7278*)
    → "$0 detected. Several equipment items can now be created."
  2: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B3 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 07 80 D4 03 03 80...])
  4: 0x00D1 [0x25] WAIT_DIALOG_SELECT()
  5: 0x00D2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0169
  6: 0x00DA [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
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
 31: 0x0171 [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
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
  1: 0x0222 [0x1D] PRINT_EVENT_MESSAGE(message_id=7280*)
    → "Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Temenos Units shall be expended in the process."
  2: 0x0225 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0226 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x0229 [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
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
| Data Size    | 155 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                                93 05 10 1D 0C 80            ......
02C0: 23 93 01 80 24 0D 80 03  80 01 80 25 02 00 10 01  #...$......%....
02D0: 80 00 40 03 42 03 01 10  03 80 43 00 43 01 02 02  ..@.B.....C.C...
02E0: 10 01 80 00 EE 02 03 01  10 01 80 01 3D 03 2C F8  ............=.,.
02F0: FF FF 7F F8 FF FF 7F 69  64 73 32 1C 04 80 2C F8  .......ids2...,.
0300: FF FF 7F F8 FF FF 7F 69  64 73 33 1C 04 80 2C F8  .......ids3...,.
0310: FF FF 7F F8 FF FF 7F 69  64 73 34 1C 04 80 2C F8  .......ids4...,.
0320: FF FF 7F F8 FF FF 7F 73  70 32 31 53 F8 FF FF 7F  .......sp21S....
0330: F8 FF FF 7F 73 70 32 31  03 01 10 03 80 01 50 03  ....sp21......P.
0340: 02 00 10 03 80 00 50 03  03 01 10 01 80 01 50 03  ......P.......P.
0350: 2E 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x02BA [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[5])
  1: 0x02BD [0x1D] PRINT_EVENT_MESSAGE(message_id=7291*)
    → ""
  2: 0x02C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x02C1 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x02C4 [0x24] CREATE_DIALOG(message_id=7292*, default_option=1*, option_flags=0*)
    → ""
  5: 0x02CB [0x25] WAIT_DIALOG_SELECT()
  6: 0x02CC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0340
  7: 0x02D4 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x02D5 [0x03] Work_Zone[1] = 1*
  9: 0x02DA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x02DC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x02DE [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x02EE
 12: 0x02E6 [0x03] Work_Zone[1] = 0*
 13: 0x02EB [0x01] GOTO 0x033D
 14: 0x02EE [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x02FB [0x1C] WAIT(60* ticks)
 16: 0x02FE [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x030B [0x1C] WAIT(60* ticks)
 18: 0x030E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x031B [0x1C] WAIT(60* ticks)
 20: 0x031E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x032B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x0338 [0x03] Work_Zone[1] = 1*

SUBROUTINE_033D:
 23: 0x033D [0x01] GOTO 0x0350
 24: 0x0340 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0350
 25: 0x0348 [0x03] Work_Zone[1] = 0*
 26: 0x034D [0x01] GOTO 0x0350

SUBROUTINE_0350:
 27: 0x0350 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x0351 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x0353 [0x21] END_EVENT
 30: 0x0354 [0x00] END_REQSTACK()
```

### Event 1037

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0355    |
| Data Size    | 155 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0350:                93 04 10  1D 0E 80 23 93 01 80 24       ......#...$
0360: 0D 80 03 80 01 80 25 02  00 10 01 80 00 DB 03 42  ......%........B
0370: 03 01 10 03 80 43 00 43  01 02 02 10 01 80 00 89  .....C.C........
0380: 03 03 01 10 01 80 01 D8  03 2C F8 FF FF 7F F8 FF  .........,......
0390: FF 7F 69 64 73 32 1C 04  80 2C F8 FF FF 7F F8 FF  ..ids2...,......
03A0: FF 7F 69 64 73 33 1C 04  80 2C F8 FF FF 7F F8 FF  ..ids3...,......
03B0: FF 7F 69 64 73 34 1C 04  80 2C F8 FF FF 7F F8 FF  ..ids4...,......
03C0: FF 7F 73 70 32 31 53 F8  FF FF 7F F8 FF FF 7F 73  ..sp21S........s
03D0: 70 32 31 03 01 10 03 80  01 EB 03 02 00 10 03 80  p21.............
03E0: 00 EB 03 03 01 10 01 80  01 EB 03 2E 20 00 21 00  ............ .!.
```

#### Opcodes

```
  0: 0x0355 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[4])
  1: 0x0358 [0x1D] PRINT_EVENT_MESSAGE(message_id=7294*)
    → ""
  2: 0x035B [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x035C [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x035F [0x24] CREATE_DIALOG(message_id=7292*, default_option=1*, option_flags=0*)
    → ""
  5: 0x0366 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0367 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03DB
  7: 0x036F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x0370 [0x03] Work_Zone[1] = 1*
  9: 0x0375 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0377 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0379 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0389
 12: 0x0381 [0x03] Work_Zone[1] = 0*
 13: 0x0386 [0x01] GOTO 0x03D8
 14: 0x0389 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x0396 [0x1C] WAIT(60* ticks)
 16: 0x0399 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x03A6 [0x1C] WAIT(60* ticks)
 18: 0x03A9 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x03B6 [0x1C] WAIT(60* ticks)
 20: 0x03B9 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x03C6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x03D3 [0x03] Work_Zone[1] = 1*

SUBROUTINE_03D8:
 23: 0x03D8 [0x01] GOTO 0x03EB
 24: 0x03DB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03EB
 25: 0x03E3 [0x03] Work_Zone[1] = 0*
 26: 0x03E8 [0x01] GOTO 0x03EB

SUBROUTINE_03EB:
 27: 0x03EB [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x03EC [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x03EE [0x21] END_EVENT
 30: 0x03EF [0x00] END_REQSTACK()
```

### Event 1038

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x03F0    |
| Data Size    | 165 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03F0: CC 03 06 10 03 10 04 10  05 10 1D 0F 80 23 48 10  .............#H.
0400: 80 93 01 80 24 02 80 03  80 01 80 25 02 00 10 01  ....$......%....
0410: 80 00 80 04 42 03 01 10  03 80 43 00 43 01 02 02  ....B.....C.C...
0420: 10 01 80 00 2E 04 03 01  10 01 80 01 7D 04 2C F8  ............}.,.
0430: FF FF 7F F8 FF FF 7F 69  64 73 32 1C 04 80 2C F8  .......ids2...,.
0440: FF FF 7F F8 FF FF 7F 69  64 73 33 1C 04 80 2C F8  .......ids3...,.
0450: FF FF 7F F8 FF FF 7F 69  64 73 34 1C 04 80 2C F8  .......ids4...,.
0460: FF FF 7F F8 FF FF 7F 73  70 32 31 53 F8 FF FF 7F  .......sp21S....
0470: F8 FF FF 7F 73 70 32 31  03 01 10 03 80 01 90 04  ....sp21........
0480: 02 00 10 03 80 00 90 04  03 01 10 01 80 01 90 04  ................
0490: 2E 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x03F0 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x03 - Open item info window (conditional chase), check_value=Work_Zone[6], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x03FA [0x1D] PRINT_EVENT_MESSAGE(message_id=7293*)
    → ""
  2: 0x03FD [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x03FE [0x48] [System] [7295*]:
    → ""
  4: 0x0401 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  5: 0x0404 [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  6: 0x040B [0x25] WAIT_DIALOG_SELECT()
  7: 0x040C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0480
  8: 0x0414 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0415 [0x03] Work_Zone[1] = 1*
 10: 0x041A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x041C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x041E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x042E
 13: 0x0426 [0x03] Work_Zone[1] = 0*
 14: 0x042B [0x01] GOTO 0x047D
 15: 0x042E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 16: 0x043B [0x1C] WAIT(60* ticks)
 17: 0x043E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 18: 0x044B [0x1C] WAIT(60* ticks)
 19: 0x044E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 20: 0x045B [0x1C] WAIT(60* ticks)
 21: 0x045E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x046B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 23: 0x0478 [0x03] Work_Zone[1] = 1*

SUBROUTINE_047D:
 24: 0x047D [0x01] GOTO 0x0490
 25: 0x0480 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0490
 26: 0x0488 [0x03] Work_Zone[1] = 0*
 27: 0x048D [0x01] GOTO 0x0490

SUBROUTINE_0490:
 28: 0x0490 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 29: 0x0491 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x0493 [0x21] END_EVENT
 31: 0x0494 [0x00] END_REQSTACK()
```

### Event 1039

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0495    |
| Data Size    | 499 bytes |
| Instructions | 88        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0490:                03 01 00  02 10 03 02 00 03 10 03       ...........
04A0: 00 00 01 80 0C 04 10 3C  00 00 04 10 03 80 D4 03  .......<........
04B0: 01 80 11 80 D4 03 03 80  12 80 D4 03 0A 80 13 80  ................
04C0: D4 03 14 80 15 80 D4 03  16 80 17 80 03 02 10 11  ................
04D0: 80 03 03 10 12 80 03 04  10 13 80 03 05 10 15 80  ................
04E0: 03 06 10 17 80 03 07 10  01 00 03 08 10 02 00 03  ................
04F0: 01 10 01 80 D4 02 18 80  01 80 00 00 25 02 00 10  ............%...
0500: 01 80 00 16 05 40 01 80  19 80 01 10 03 80 03 05  .....@..........
0510: 00 11 80 01 8A 05 02 00  10 03 80 00 2F 05 40 01  ............/.@.
0520: 80 19 80 01 10 0A 80 03  05 00 12 80 01 8A 05 02  ................
0530: 00 10 0A 80 00 48 05 40  01 80 19 80 01 10 14 80  .....H.@........
0540: 03 05 00 13 80 01 8A 05  02 00 10 14 80 00 61 05  ..............a.
0550: 40 01 80 19 80 01 10 16  80 03 05 00 15 80 01 8A  @...............
0560: 05 02 00 10 16 80 00 7A  05 40 01 80 19 80 01 10  .......z.@......
0570: 1A 80 03 05 00 17 80 01  8A 05 02 00 10 1A 80 00  ................
0580: 8A 05 03 01 10 01 80 01  8A 05 02 01 10 01 80 00  ................
0590: 95 05 01 83 06 03 03 00  02 00 15 03 00 0A 80 03  ................
05A0: 02 10 03 00 1D 1B 80 23  48 1C 80 71 12 03 80 0A  .......#H..q....
05B0: 80 71 13 02 10 02 02 10  01 80 00 C0 05 01 83 06  .q..............
05C0: 02 02 10 03 00 05 80 06  03 04 00 02 10 14 04 00  ................
05D0: 0A 80 03 06 00 02 10 03  02 10 01 00 03 03 10 04  ................
05E0: 00 03 04 10 05 00 03 05  10 06 00 1D 1D 80 23 24  ..............#$
05F0: 0D 80 03 80 01 80 25 02  00 10 01 80 00 6F 06 40  ......%......o.@
0600: 1E 80 1F 80 01 10 05 10  42 43 00 43 01 02 02 10  ........BC.C....
0610: 01 80 00 1D 06 03 01 10  01 80 01 6C 06 2C F8 FF  ...........l.,..
0620: FF 7F F8 FF FF 7F 69 64  73 32 1C 04 80 2C F8 FF  ......ids2...,..
0630: FF 7F F8 FF FF 7F 69 64  73 33 1C 04 80 2C F8 FF  ......ids3...,..
0640: FF 7F F8 FF FF 7F 69 64  73 34 1C 04 80 2C F8 FF  ......ids4...,..
0650: FF 7F F8 FF FF 7F 73 70  32 31 53 F8 FF FF 7F F8  ......sp21S.....
0660: FF FF 7F 73 70 32 31 03  01 10 03 80 01 7D 06 02  ...sp21......}..
0670: 00 10 03 80 00 7D 06 01  CC 04 01 7D 06 01 83 06  .....}.....}....
0680: 01 CC 04 2E 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0495 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
  1: 0x049A [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[3]
  2: 0x049F [0x03] ExtData[1]->WorkLocal[0] = 0*
  3: 0x04A4 [0x0C] Work_Zone[4]--
  4: 0x04A7 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=Work_Zone[4], condition_work_offset=1*)
  5: 0x04AE [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 11 80 D4 03 03 80...])
  6: 0x04CC [0x03] Work_Zone[2] = 10006*
  7: 0x04D1 [0x03] Work_Zone[3] = 10007*
  8: 0x04D6 [0x03] Work_Zone[4] = 10008*
  9: 0x04DB [0x03] Work_Zone[5] = 10009*
 10: 0x04E0 [0x03] Work_Zone[6] = 10010*
 11: 0x04E5 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[1]
 12: 0x04EA [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[2]
 13: 0x04EF [0x03] Work_Zone[1] = 0*
 14: 0x04F4 [0xD4] MAP_QUERY_WINDOW: Test and open query window (flag=0x18, work=[0x0180, 0x80, 0x2500])
 15: 0x04FD [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0516
 16: 0x0505 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 17: 0x050E [0x03] ExtData[1]->WorkLocal[5] = 10006*
 18: 0x0513 [0x01] GOTO 0x058A
 19: 0x0516 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x052F
 20: 0x051E [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
 21: 0x0527 [0x03] ExtData[1]->WorkLocal[5] = 10007*
 22: 0x052C [0x01] GOTO 0x058A
 23: 0x052F [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0548
 24: 0x0537 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=3*)
 25: 0x0540 [0x03] ExtData[1]->WorkLocal[5] = 10008*
 26: 0x0545 [0x01] GOTO 0x058A
 27: 0x0548 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0561
 28: 0x0550 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=4*)
 29: 0x0559 [0x03] ExtData[1]->WorkLocal[5] = 10009*
 30: 0x055E [0x01] GOTO 0x058A
 31: 0x0561 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x057A
 32: 0x0569 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=5*)
 33: 0x0572 [0x03] ExtData[1]->WorkLocal[5] = 10010*
 34: 0x0577 [0x01] GOTO 0x058A
 35: 0x057A [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x058A
 36: 0x0582 [0x03] Work_Zone[1] = 0*
 37: 0x0587 [0x01] GOTO 0x058A

SUBROUTINE_058A:
 38: 0x058A [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0595
 39: 0x0592 [0x01] GOTO 0x0683
 40: 0x0595 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[2]
 41: 0x059A [0x15] ExtData[1]->WorkLocal[3] /= 2*
 42: 0x059F [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[3]
 43: 0x05A4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7300*)
    → ""
 44: 0x05A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x05A8 [0x48] [System] [7255*]:
    → "Enter 0 to cancel."
 46: 0x05AB [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 47: 0x05B1 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=Work_Zone[2])
 48: 0x05B5 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x05C0
 49: 0x05BD [0x01] GOTO 0x0683
 50: 0x05C0 [0x02] IF !(Work_Zone[2] > ExtData[1]->WorkLocal[3]) GOTO 0x0680
 51: 0x05C8 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[2]
 52: 0x05CD [0x14] ExtData[1]->WorkLocal[4] *= 2*
 53: 0x05D2 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[2]
 54: 0x05D7 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 55: 0x05DC [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[4]
 56: 0x05E1 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[5]
 57: 0x05E6 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[6]
 58: 0x05EB [0x1D] PRINT_EVENT_MESSAGE(message_id=7301*)
    → ""
 59: 0x05EE [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x05EF [0x24] CREATE_DIALOG(message_id=7292*, default_option=1*, option_flags=0*)
    → ""
 61: 0x05F6 [0x25] WAIT_DIALOG_SELECT()
 62: 0x05F7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x066F
 63: 0x05FF [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=Work_Zone[5])
 64: 0x0608 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 65: 0x0609 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 66: 0x060B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 67: 0x060D [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x061D
 68: 0x0615 [0x03] Work_Zone[1] = 0*
 69: 0x061A [0x01] GOTO 0x066C
 70: 0x061D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 71: 0x062A [0x1C] WAIT(60* ticks)
 72: 0x062D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 73: 0x063A [0x1C] WAIT(60* ticks)
 74: 0x063D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 75: 0x064A [0x1C] WAIT(60* ticks)
 76: 0x064D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 77: 0x065A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 78: 0x0667 [0x03] Work_Zone[1] = 1*

SUBROUTINE_066C:
 79: 0x066C [0x01] GOTO 0x067D
 80: 0x066F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x067D
 81: 0x0677 [0x01] GOTO 0x04CC

SUBROUTINE_067D:
 82: 0x067D [0x01] GOTO 0x0683
 83: 0x0680 [0x01] GOTO 0x04CC

SUBROUTINE_0683:
 84: 0x0683 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 85: 0x0684 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 86: 0x0686 [0x21] END_EVENT
 87: 0x0687 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x067A [0x01] GOTO 0x067D
```
