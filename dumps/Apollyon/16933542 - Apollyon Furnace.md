# 16933542 - Apollyon Furnace

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 708 bytes         |
| Total Events     | 4                 |
| References Count | 12                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [133](#event-133)     | 0x0001       |    169 |             31 |
| [135](#event-135)     | 0x00AA       |    293 |             48 |
| [137](#event-137)     | 0x01CF       |    162 |             31 |

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

## String References

- **7281**: Fusing your $0 with $1 Apollyon Units to create $2.
- **7282**: Proceed? [Yes./No.]
- **7286**: 
- **7288**: 

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
  1: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=7281*)
    → "Fusing your $0 with $1 Apollyon Units to create $2."
  2: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000F [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=0*, buffer1=0*, buffer2=0*, buffer3=0*)
  4: 0x0019 [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
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

### Event 135

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00AA    |
| Data Size    | 293 bytes |
| Instructions | 48        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                03 02 10 05 80 1D            ......
00B0: 06 80 23 D4 03 01 80 07  80 D4 03 03 80 08 80 03  ..#.............
00C0: 02 10 07 80 03 03 10 08  80 D4 02 09 80 0A 80 01  ................
00D0: 80 25 02 00 10 01 80 00  46 01 42 03 01 10 03 80  .%......F.B.....
00E0: 43 00 43 01 02 02 10 01  80 00 F4 00 03 01 10 01  C.C.............
00F0: 80 01 43 01 2C F8 FF FF  7F F8 FF FF 7F 69 64 73  ..C.,........ids
0100: 32 1C 04 80 2C F8 FF FF  7F F8 FF FF 7F 69 64 73  2...,........ids
0110: 33 1C 04 80 2C F8 FF FF  7F F8 FF FF 7F 69 64 73  3...,........ids
0120: 34 1C 04 80 2C F8 FF FF  7F F8 FF FF 7F 73 70 32  4...,........sp2
0130: 31 53 F8 FF FF 7F F8 FF  FF 7F 73 70 32 31 03 01  1S........sp21..
0140: 10 03 80 01 CA 01 02 00  10 03 80 00 BA 01 42 03  ..............B.
0150: 01 10 0A 80 43 00 43 01  02 02 10 01 80 00 68 01  ....C.C.......h.
0160: 03 01 10 01 80 01 B7 01  2C F8 FF FF 7F F8 FF FF  ........,.......
0170: 7F 69 64 73 32 1C 04 80  2C F8 FF FF 7F F8 FF FF  .ids2...,.......
0180: 7F 69 64 73 33 1C 04 80  2C F8 FF FF 7F F8 FF FF  .ids3...,.......
0190: 7F 69 64 73 34 1C 04 80  2C F8 FF FF 7F F8 FF FF  .ids4...,.......
01A0: 7F 73 70 32 31 53 F8 FF  FF 7F F8 FF FF 7F 73 70  .sp21S........sp
01B0: 32 31 03 01 10 03 80 01  CA 01 02 00 10 0A 80 00  21..............
01C0: CA 01 03 01 10 01 80 01  CA 01 2E 20 00 21 00     ........... .!. 
```

#### Opcodes

```
  0: 0x00AA [0x03] Work_Zone[2] = 10000*
  1: 0x00AF [0x1D] PRINT_EVENT_MESSAGE(message_id=7286*)
    → ""
  2: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B3 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 07 80 D4 03 03 80...])
  4: 0x00D1 [0x25] WAIT_DIALOG_SELECT()
  5: 0x00D2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0146
  6: 0x00DA [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x00DB [0x03] Work_Zone[1] = 1*
  8: 0x00E0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  9: 0x00E2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 10: 0x00E4 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00F4
 11: 0x00EC [0x03] Work_Zone[1] = 0*
 12: 0x00F1 [0x01] GOTO 0x0143
 13: 0x00F4 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 14: 0x0101 [0x1C] WAIT(60* ticks)
 15: 0x0104 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 16: 0x0111 [0x1C] WAIT(60* ticks)
 17: 0x0114 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 18: 0x0121 [0x1C] WAIT(60* ticks)
 19: 0x0124 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 20: 0x0131 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x013E [0x03] Work_Zone[1] = 1*

SUBROUTINE_0143:
 22: 0x0143 [0x01] GOTO 0x01CA
 23: 0x0146 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01BA
 24: 0x014E [0x42] SET_CLI_EVENT_CANCEL_DATA()
 25: 0x014F [0x03] Work_Zone[1] = 2*
 26: 0x0154 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 27: 0x0156 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 28: 0x0158 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0168
 29: 0x0160 [0x03] Work_Zone[1] = 0*
 30: 0x0165 [0x01] GOTO 0x01B7
 31: 0x0168 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 32: 0x0175 [0x1C] WAIT(60* ticks)
 33: 0x0178 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 34: 0x0185 [0x1C] WAIT(60* ticks)
 35: 0x0188 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 36: 0x0195 [0x1C] WAIT(60* ticks)
 37: 0x0198 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 38: 0x01A5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 39: 0x01B2 [0x03] Work_Zone[1] = 1*

SUBROUTINE_01B7:
 40: 0x01B7 [0x01] GOTO 0x01CA
 41: 0x01BA [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x01CA
 42: 0x01C2 [0x03] Work_Zone[1] = 0*
 43: 0x01C7 [0x01] GOTO 0x01CA

SUBROUTINE_01CA:
 44: 0x01CA [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 45: 0x01CB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 46: 0x01CD [0x21] END_EVENT
 47: 0x01CE [0x00] END_REQSTACK()
```

### Event 137

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01CF    |
| Data Size    | 162 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                               CC                 .
01D0: 01 02 10 03 10 04 10 05  10 1D 0B 80 23 93 01 80  ............#...
01E0: 24 02 80 03 80 01 80 25  02 00 10 01 80 00 5C 02  $......%......\.
01F0: 42 03 01 10 03 80 43 00  43 01 02 02 10 01 80 00  B.....C.C.......
0200: 0A 02 03 01 10 01 80 01  59 02 2C F8 FF FF 7F F8  ........Y.,.....
0210: FF FF 7F 69 64 73 32 1C  04 80 2C F8 FF FF 7F F8  ...ids2...,.....
0220: FF FF 7F 69 64 73 33 1C  04 80 2C F8 FF FF 7F F8  ...ids3...,.....
0230: FF FF 7F 69 64 73 34 1C  04 80 2C F8 FF FF 7F F8  ...ids4...,.....
0240: FF FF 7F 73 70 32 31 53  F8 FF FF 7F F8 FF FF 7F  ...sp21S........
0250: 73 70 32 31 03 01 10 03  80 01 6C 02 02 00 10 03  sp21......l.....
0260: 80 00 6C 02 03 01 10 01  80 01 6C 02 2E 20 00 21  ..l.......l.. .!
0270: 00                                                .               
```

#### Opcodes

```
  0: 0x01CF [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=Work_Zone[2], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x01D9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7288*)
    → ""
  2: 0x01DC [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01DD [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x01E0 [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  5: 0x01E7 [0x25] WAIT_DIALOG_SELECT()
  6: 0x01E8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x025C
  7: 0x01F0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x01F1 [0x03] Work_Zone[1] = 1*
  9: 0x01F6 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x01F8 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x01FA [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x020A
 12: 0x0202 [0x03] Work_Zone[1] = 0*
 13: 0x0207 [0x01] GOTO 0x0259
 14: 0x020A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x0217 [0x1C] WAIT(60* ticks)
 16: 0x021A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x0227 [0x1C] WAIT(60* ticks)
 18: 0x022A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x0237 [0x1C] WAIT(60* ticks)
 20: 0x023A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x0247 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x0254 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0259:
 23: 0x0259 [0x01] GOTO 0x026C
 24: 0x025C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x026C
 25: 0x0264 [0x03] Work_Zone[1] = 0*
 26: 0x0269 [0x01] GOTO 0x026C

SUBROUTINE_026C:
 27: 0x026C [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x026D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x026F [0x21] END_EVENT
 30: 0x0270 [0x00] END_REQSTACK()
```
