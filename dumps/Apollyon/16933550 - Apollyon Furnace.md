# 16933550 - Apollyon Furnace

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 804 bytes         |
| Total Events     | 4                 |
| References Count | 12                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [132](#event-132)     | 0x0001       |    169 |             31 |
| [134](#event-134)     | 0x00AA       |    391 |             70 |
| [136](#event-136)     | 0x0231       |    162 |             31 |

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
- **7286**: $0 detected. Several equipment items can now be created.
- **7288**: Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Apollyon Units shall be expended in the process.

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

### Event 132

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

### Event 134

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00AA    |
| Data Size    | 391 bytes |
| Instructions | 70        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                03 02 10 05 80 1D            ......
00B0: 06 80 23 D4 03 01 80 07  80 D4 03 03 80 08 80 03  ..#.............
00C0: 02 10 07 80 03 03 10 08  80 D4 02 09 80 0A 80 01  ................
00D0: 80 25 02 00 10 01 80 00  77 01 93 02 10 24 02 80  .%......w....$..
00E0: 03 80 01 80 25 02 00 10  01 80 00 61 01 93 01 80  ....%......a....
00F0: 42 03 01 10 03 80 43 00  43 01 02 02 10 01 80 00  B.....C.C.......
0100: 0A 01 03 01 10 01 80 01  5E 01 2C F8 FF FF 7F F8  ........^.,.....
0110: FF FF 7F 69 64 73 32 1C  04 80 2C F8 FF FF 7F F8  ...ids2...,.....
0120: FF FF 7F 69 64 73 33 1C  04 80 2C F8 FF FF 7F F8  ...ids3...,.....
0130: FF FF 7F 69 64 73 34 1C  04 80 2C F8 FF FF 7F F8  ...ids4...,.....
0140: FF FF 7F 73 70 32 31 53  F8 FF FF 7F F8 FF FF 7F  ...sp21S........
0150: 73 70 32 31 03 01 10 03  80 03 02 10 07 80 01 74  sp21...........t
0160: 01 02 00 10 03 80 00 74  01 93 01 80 03 01 10 01  .......t........
0170: 80 01 74 01 01 2C 02 02  00 10 03 80 00 1C 02 93  ..t..,..........
0180: 03 10 24 02 80 03 80 01  80 25 02 00 10 01 80 00  ..$......%......
0190: 06 02 93 01 80 42 03 01  10 0A 80 43 00 43 01 02  .....B.....C.C..
01A0: 02 10 01 80 00 AF 01 03  01 10 01 80 01 03 02 2C  ...............,
01B0: F8 FF FF 7F F8 FF FF 7F  69 64 73 32 1C 04 80 2C  ........ids2...,
01C0: F8 FF FF 7F F8 FF FF 7F  69 64 73 33 1C 04 80 2C  ........ids3...,
01D0: F8 FF FF 7F F8 FF FF 7F  69 64 73 34 1C 04 80 2C  ........ids4...,
01E0: F8 FF FF 7F F8 FF FF 7F  73 70 32 31 53 F8 FF FF  ........sp21S...
01F0: 7F F8 FF FF 7F 73 70 32  31 03 01 10 03 80 03 02  .....sp21.......
0200: 10 08 80 01 19 02 02 00  10 03 80 00 19 02 93 01  ................
0210: 80 03 01 10 01 80 01 19  02 01 2C 02 02 00 10 0A  ..........,.....
0220: 80 00 2C 02 03 01 10 01  80 01 2C 02 2E 20 00 21  ..,.......,.. .!
0230: 00                                                .               
```

#### Opcodes

```
  0: 0x00AA [0x03] Work_Zone[2] = 10000*
  1: 0x00AF [0x1D] PRINT_EVENT_MESSAGE(message_id=7286*)
    → "$0 detected. Several equipment items can now be created."
  2: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B3 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[01 80 07 80 D4 03 03 80...])
  4: 0x00D1 [0x25] WAIT_DIALOG_SELECT()
  5: 0x00D2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0177
  6: 0x00DA [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[2])
  7: 0x00DD [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  8: 0x00E4 [0x25] WAIT_DIALOG_SELECT()
  9: 0x00E5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0161
 10: 0x00ED [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 11: 0x00F0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x00F1 [0x03] Work_Zone[1] = 1*
 13: 0x00F6 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 14: 0x00F8 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 15: 0x00FA [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x010A
 16: 0x0102 [0x03] Work_Zone[1] = 0*
 17: 0x0107 [0x01] GOTO 0x015E
 18: 0x010A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 19: 0x0117 [0x1C] WAIT(60* ticks)
 20: 0x011A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 21: 0x0127 [0x1C] WAIT(60* ticks)
 22: 0x012A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 23: 0x0137 [0x1C] WAIT(60* ticks)
 24: 0x013A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 25: 0x0147 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 26: 0x0154 [0x03] Work_Zone[1] = 1*
 27: 0x0159 [0x03] Work_Zone[2] = 26234*

SUBROUTINE_015E:
 28: 0x015E [0x01] GOTO 0x0174
 29: 0x0161 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0174
 30: 0x0169 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 31: 0x016C [0x03] Work_Zone[1] = 0*
 32: 0x0171 [0x01] GOTO 0x0174

SUBROUTINE_0174:
 33: 0x0174 [0x01] GOTO 0x022C
 34: 0x0177 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x021C
 35: 0x017F [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone[3])
 36: 0x0182 [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
 37: 0x0189 [0x25] WAIT_DIALOG_SELECT()
 38: 0x018A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0206
 39: 0x0192 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 40: 0x0195 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 41: 0x0196 [0x03] Work_Zone[1] = 2*
 42: 0x019B [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 43: 0x019D [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 44: 0x019F [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x01AF
 45: 0x01A7 [0x03] Work_Zone[1] = 0*
 46: 0x01AC [0x01] GOTO 0x0203
 47: 0x01AF [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 48: 0x01BC [0x1C] WAIT(60* ticks)
 49: 0x01BF [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 50: 0x01CC [0x1C] WAIT(60* ticks)
 51: 0x01CF [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 52: 0x01DC [0x1C] WAIT(60* ticks)
 53: 0x01DF [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 54: 0x01EC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 55: 0x01F9 [0x03] Work_Zone[1] = 1*
 56: 0x01FE [0x03] Work_Zone[2] = 26276*

SUBROUTINE_0203:
 57: 0x0203 [0x01] GOTO 0x0219
 58: 0x0206 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0219
 59: 0x020E [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 60: 0x0211 [0x03] Work_Zone[1] = 0*
 61: 0x0216 [0x01] GOTO 0x0219

SUBROUTINE_0219:
 62: 0x0219 [0x01] GOTO 0x022C
 63: 0x021C [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x022C
 64: 0x0224 [0x03] Work_Zone[1] = 0*
 65: 0x0229 [0x01] GOTO 0x022C

SUBROUTINE_022C:
 66: 0x022C [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 67: 0x022D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 68: 0x022F [0x21] END_EVENT
 69: 0x0230 [0x00] END_REQSTACK()
```

### Event 136

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0231    |
| Data Size    | 162 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:    CC 01 02 10 03 10 04  10 05 10 1D 0B 80 23 93   .............#.
0240: 01 80 24 02 80 03 80 01  80 25 02 00 10 01 80 00  ..$......%......
0250: BE 02 42 03 01 10 03 80  43 00 43 01 02 02 10 01  ..B.....C.C.....
0260: 80 00 6C 02 03 01 10 01  80 01 BB 02 2C F8 FF FF  ..l.........,...
0270: 7F F8 FF FF 7F 69 64 73  32 1C 04 80 2C F8 FF FF  .....ids2...,...
0280: 7F F8 FF FF 7F 69 64 73  33 1C 04 80 2C F8 FF FF  .....ids3...,...
0290: 7F F8 FF FF 7F 69 64 73  34 1C 04 80 2C F8 FF FF  .....ids4...,...
02A0: 7F F8 FF FF 7F 73 70 32  31 53 F8 FF FF 7F F8 FF  .....sp21S......
02B0: FF 7F 73 70 32 31 03 01  10 03 80 01 CE 02 02 00  ..sp21..........
02C0: 10 03 80 00 CE 02 03 01  10 01 80 01 CE 02 2E 20  ............... 
02D0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0231 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=Work_Zone[2], buffer1=Work_Zone[3], buffer2=Work_Zone[4], buffer3=Work_Zone[5])
  1: 0x023B [0x1D] PRINT_EVENT_MESSAGE(message_id=7288*)
    → "Commencing enhancement of $0. To proceed, $6 units of $5 are required. $4 Apollyon Units shall be expended in the process."
  2: 0x023E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x023F [0x93] DISPLAY_ITEM_INFO(item_id=0*)
  4: 0x0242 [0x24] CREATE_DIALOG(message_id=7282*, default_option=1*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  5: 0x0249 [0x25] WAIT_DIALOG_SELECT()
  6: 0x024A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02BE
  7: 0x0252 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x0253 [0x03] Work_Zone[1] = 1*
  9: 0x0258 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x025A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x025C [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x026C
 12: 0x0264 [0x03] Work_Zone[1] = 0*
 13: 0x0269 [0x01] GOTO 0x02BB
 14: 0x026C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids2" with entities [EventEntity, EventEntity]
 15: 0x0279 [0x1C] WAIT(60* ticks)
 16: 0x027C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids3" with entities [EventEntity, EventEntity]
 17: 0x0289 [0x1C] WAIT(60* ticks)
 18: 0x028C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ids4" with entities [EventEntity, EventEntity]
 19: 0x0299 [0x1C] WAIT(60* ticks)
 20: 0x029C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp21" with entities [EventEntity, EventEntity]
 21: 0x02A9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp21" with entities [EventEntity, EventEntity]
 22: 0x02B6 [0x03] Work_Zone[1] = 1*

SUBROUTINE_02BB:
 23: 0x02BB [0x01] GOTO 0x02CE
 24: 0x02BE [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02CE
 25: 0x02C6 [0x03] Work_Zone[1] = 0*
 26: 0x02CB [0x01] GOTO 0x02CE

SUBROUTINE_02CE:
 27: 0x02CE [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 28: 0x02CF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x02D1 [0x21] END_EVENT
 30: 0x02D2 [0x00] END_REQSTACK()
```
