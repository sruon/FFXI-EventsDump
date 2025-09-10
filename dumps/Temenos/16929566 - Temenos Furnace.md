# 16929566 - Temenos Furnace

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 1300 bytes       |
| Total Events     | 7                |
| References Count | 17               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1033](#event-1033)   | 0x0001       |    169 |             31 |
| [1034](#event-1034)   | 0x00AA       |    381 |             68 |
| [1035](#event-1035)   | 0x0227       |    162 |             31 |
| [1036](#event-1036)   | 0x02C9       |    155 |             31 |
| [1037](#event-1037)   | 0x0364       |    155 |             31 |
| [1038](#event-1038)   | 0x03FF       |    165 |             32 |

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

## String References

- **7273**: Fusing your $0 with $1 Apollyon Units to create $2.
- **7274**: Proceed? [Yes./No.]
- **7278**: $0 detected. Several equipment items can now be created.
- **7280**: Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Temenos Units shall be expended in the process.
- **7291**: 
- **7292**: 
- **7293**: 
- **7294**: 
- **7295**: 

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
| Data Size    | 381 bytes |
| Instructions | 68        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                03 02 10 05 80 1D            ......
00B0: 06 80 23 D4 03 01 80 07  80 D4 03 03 80 08 80 03  ..#.............
00C0: 02 10 07 80 03 03 10 08  80 D4 02 09 80 0A 80 01  ................
00D0: 80 25 02 00 10 01 80 00  72 01 93 02 10 24 02 80  .%......r....$..
00E0: 03 80 01 80 25 02 00 10  01 80 00 5C 01 93 01 80  ....%......\....
00F0: 42 03 01 10 03 80 43 00  43 01 02 02 10 01 80 00  B.....C.C.......
0100: 0A 01 03 01 10 01 80 01  59 01 2C F8 FF FF 7F F8  ........Y.,.....
0110: FF FF 7F 69 64 73 32 1C  04 80 2C F8 FF FF 7F F8  ...ids2...,.....
0120: FF FF 7F 69 64 73 33 1C  04 80 2C F8 FF FF 7F F8  ...ids3...,.....
0130: FF FF 7F 69 64 73 34 1C  04 80 2C F8 FF FF 7F F8  ...ids4...,.....
0140: FF FF 7F 73 70 32 31 53  F8 FF FF 7F F8 FF FF 7F  ...sp21S........
0150: 73 70 32 31 03 01 10 03  80 01 6F 01 02 00 10 03  sp21......o.....
0160: 80 00 6F 01 93 01 80 03  01 10 01 80 01 6F 01 01  ..o..........o..
0170: 22 02 02 00 10 03 80 00  12 02 93 03 10 24 02 80  "............$..
0180: 03 80 01 80 25 02 00 10  01 80 00 FC 01 93 01 80  ....%...........
0190: 42 03 01 10 0A 80 43 00  43 01 02 02 10 01 80 00  B.....C.C.......
01A0: AA 01 03 01 10 01 80 01  F9 01 2C F8 FF FF 7F F8  ..........,.....
01B0: FF FF 7F 69 64 73 32 1C  04 80 2C F8 FF FF 7F F8  ...ids2...,.....
01C0: FF FF 7F 69 64 73 33 1C  04 80 2C F8 FF FF 7F F8  ...ids3...,.....
01D0: FF FF 7F 69 64 73 34 1C  04 80 2C F8 FF FF 7F F8  ...ids4...,.....
01E0: FF FF 7F 73 70 32 31 53  F8 FF FF 7F F8 FF FF 7F  ...sp21S........
01F0: 73 70 32 31 03 01 10 03  80 01 0F 02 02 00 10 03  sp21............
0200: 80 00 0F 02 93 01 80 03  01 10 01 80 01 0F 02 01  ................
0210: 22 02 02 00 10 0A 80 00  22 02 03 01 10 01 80 01  ".......".......
0220: 22 02 2E 20 00 21 00                              ".. .!.         
```

#### Opcodes

```
  0: 0x00AA [0x03] Work_Zone[2] = 9999*
  1: 0x00AF [0x1D] PRINT_EVENT_MESSAGE(message_id=7278*)
    → "$0 detected. Several equipment items can now be created."
  2: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B3 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 07 80 D4 03 03 80...])
  4: 0x00D1 [0x25] WAIT_DIALOG_SELECT()
  5: 0x00D2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0172
  6: 0x00DA [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[2])
  7: 0x00DD [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  8: 0x00E4 [0x25] WAIT_DIALOG_SELECT()
  9: 0x00E5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x015C
 10: 0x00ED [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 11: 0x00F0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x00F1 [0x03] Work_Zone[1] = 1*
 13: 0x00F6 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 14: 0x00F8 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 15: 0x00FA [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x010A
 16: 0x0102 [0x03] Work_Zone[1] = 0*
 17: 0x0107 [0x01] GOTO 0x0159
 18: 0x010A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 19: 0x0117 [0x1C] WAIT(60* ticks)
 20: 0x011A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 21: 0x0127 [0x1C] WAIT(60* ticks)
 22: 0x012A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 23: 0x0137 [0x1C] WAIT(60* ticks)
 24: 0x013A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 25: 0x0147 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 26: 0x0154 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0159:
 27: 0x0159 [0x01] GOTO 0x016F
 28: 0x015C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x016F
 29: 0x0164 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 30: 0x0167 [0x03] Work_Zone[1] = 0*
 31: 0x016C [0x01] GOTO 0x016F

SUBROUTINE_016F:
 32: 0x016F [0x01] GOTO 0x0222
 33: 0x0172 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0212
 34: 0x017A [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[3])
 35: 0x017D [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
 36: 0x0184 [0x25] WAIT_DIALOG_SELECT()
 37: 0x0185 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01FC
 38: 0x018D [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 39: 0x0190 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 40: 0x0191 [0x03] Work_Zone[1] = 2*
 41: 0x0196 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 42: 0x0198 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 43: 0x019A [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x01AA
 44: 0x01A2 [0x03] Work_Zone[1] = 0*
 45: 0x01A7 [0x01] GOTO 0x01F9
 46: 0x01AA [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 47: 0x01B7 [0x1C] WAIT(60* ticks)
 48: 0x01BA [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 49: 0x01C7 [0x1C] WAIT(60* ticks)
 50: 0x01CA [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 51: 0x01D7 [0x1C] WAIT(60* ticks)
 52: 0x01DA [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 53: 0x01E7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 54: 0x01F4 [0x03] Work_Zone[1] = 1*

SUBROUTINE_01F9:
 55: 0x01F9 [0x01] GOTO 0x020F
 56: 0x01FC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x020F
 57: 0x0204 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 58: 0x0207 [0x03] Work_Zone[1] = 0*
 59: 0x020C [0x01] GOTO 0x020F

SUBROUTINE_020F:
 60: 0x020F [0x01] GOTO 0x0222
 61: 0x0212 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0222
 62: 0x021A [0x03] Work_Zone[1] = 0*
 63: 0x021F [0x01] GOTO 0x0222

SUBROUTINE_0222:
 64: 0x0222 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 65: 0x0223 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 66: 0x0225 [0x21] END_EVENT
 67: 0x0226 [0x00] END_REQSTACK()
```

### Event 1035

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0227    |
| Data Size    | 162 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                      CC  01 02 10 03 10 04 10 05         .........
0230: 10 1D 0B 80 23 93 01 80  24 02 80 03 80 01 80 25  ....#...$......%
0240: 02 00 10 01 80 00 B4 02  42 03 01 10 03 80 43 00  ........B.....C.
0250: 43 01 02 02 10 01 80 00  62 02 03 01 10 01 80 01  C.......b.......
0260: B1 02 2C F8 FF FF 7F F8  FF FF 7F 69 64 73 32 1C  ..,........ids2.
0270: 04 80 2C F8 FF FF 7F F8  FF FF 7F 69 64 73 33 1C  ..,........ids3.
0280: 04 80 2C F8 FF FF 7F F8  FF FF 7F 69 64 73 34 1C  ..,........ids4.
0290: 04 80 2C F8 FF FF 7F F8  FF FF 7F 73 70 32 31 53  ..,........sp21S
02A0: F8 FF FF 7F F8 FF FF 7F  73 70 32 31 03 01 10 03  ........sp21....
02B0: 80 01 C4 02 02 00 10 03  80 00 C4 02 03 01 10 01  ................
02C0: 80 01 C4 02 2E 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x0227 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=Work_Zone[2], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x0231 [0x1D] PRINT_EVENT_MESSAGE(message_id=7280*)
    → "Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Temenos Units shall be expended in the process."
  2: 0x0234 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0235 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x0238 [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  5: 0x023F [0x25] WAIT_DIALOG_SELECT()
  6: 0x0240 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02B4
  7: 0x0248 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x0249 [0x03] Work_Zone[1] = 1*
  9: 0x024E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0250 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0252 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0262
 12: 0x025A [0x03] Work_Zone[1] = 0*
 13: 0x025F [0x01] GOTO 0x02B1
 14: 0x0262 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x026F [0x1C] WAIT(60* ticks)
 16: 0x0272 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x027F [0x1C] WAIT(60* ticks)
 18: 0x0282 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x028F [0x1C] WAIT(60* ticks)
 20: 0x0292 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x029F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x02AC [0x03] Work_Zone[1] = 1*

SUBROUTINE_02B1:
 23: 0x02B1 [0x01] GOTO 0x02C4
 24: 0x02B4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02C4
 25: 0x02BC [0x03] Work_Zone[1] = 0*
 26: 0x02C1 [0x01] GOTO 0x02C4

SUBROUTINE_02C4:
 27: 0x02C4 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x02C5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x02C7 [0x21] END_EVENT
 30: 0x02C8 [0x00] END_REQSTACK()
```

### Event 1036

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02C9    |
| Data Size    | 155 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:                             93 05 10 1D 0C 80 23           ......#
02D0: 93 01 80 24 0D 80 03 80  01 80 25 02 00 10 01 80  ...$......%.....
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
  0: 0x02C9 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[5])
  1: 0x02CC [0x1D] PRINT_EVENT_MESSAGE(message_id=7291*)
    → ""
  2: 0x02CF [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x02D0 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x02D3 [0x24] CREATE_DIALOG(message_id=7292*, default_option=1*, option_flags=0*)
    → ""
  5: 0x02DA [0x25] WAIT_DIALOG_SELECT()
  6: 0x02DB [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x034F
  7: 0x02E3 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x02E4 [0x03] Work_Zone[1] = 1*
  9: 0x02E9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x02EB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x02ED [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x02FD
 12: 0x02F5 [0x03] Work_Zone[1] = 0*
 13: 0x02FA [0x01] GOTO 0x034C
 14: 0x02FD [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x030A [0x1C] WAIT(60* ticks)
 16: 0x030D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x031A [0x1C] WAIT(60* ticks)
 18: 0x031D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x032A [0x1C] WAIT(60* ticks)
 20: 0x032D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x033A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x0347 [0x03] Work_Zone[1] = 1*

SUBROUTINE_034C:
 23: 0x034C [0x01] GOTO 0x035F
 24: 0x034F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x035F
 25: 0x0357 [0x03] Work_Zone[1] = 0*
 26: 0x035C [0x01] GOTO 0x035F

SUBROUTINE_035F:
 27: 0x035F [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x0360 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x0362 [0x21] END_EVENT
 30: 0x0363 [0x00] END_REQSTACK()
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
0360:             93 04 10 1D  0E 80 23 93 01 80 24 0D      ......#...$.
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
  1: 0x0367 [0x1D] PRINT_EVENT_MESSAGE(message_id=7294*)
    → ""
  2: 0x036A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x036B [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x036E [0x24] CREATE_DIALOG(message_id=7292*, default_option=1*, option_flags=0*)
    → ""
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
0400: 01 06 10 03 10 04 10 05  10 1D 0F 80 23 48 10 80  ............#H..
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
  0: 0x03FF [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=Work_Zone[6], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x0409 [0x1D] PRINT_EVENT_MESSAGE(message_id=7293*)
    → ""
  2: 0x040C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x040D [0x48] [System] [7295*]:
    → ""
  4: 0x0410 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  5: 0x0413 [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
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
