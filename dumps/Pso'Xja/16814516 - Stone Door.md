# 16814516 - Stone Door

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Pso'Xja (ID: 9) |
| Block Size       | 5516 bytes      |
| Total Events     | 13              |
| References Count | 25              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      2 |              2 |
| [65535.2](#event-655352) | 0x0004       |      2 |              2 |
| [106](#event-106)        | 0x0006       |    533 |             70 |
| [107](#event-107)        | 0x021B       |    533 |             70 |
| [108](#event-108)        | 0x0430       |    533 |             70 |
| [109](#event-109)        | 0x0645       |    802 |            104 |
| [110](#event-110)        | 0x0967       |    802 |            104 |
| [111](#event-111)        | 0x0C89       |    802 |            104 |
| [112](#event-112)        | 0x0FAB       |   1071 |            138 |
| [50](#event-50)          | 0x13DA       |    264 |             36 |
| [2](#event-2)            | 0x14E2       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1BA8      |        7080 |
|       1 | 0x0002      |           2 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x0078      |         120 |
|       5 | 0x0013      |          19 |
|       6 | 0x00A0      |         160 |
|       7 | 0x012C      |         300 |
|       8 | 0x005A      |          90 |
|       9 | 0x00C9      |         201 |
|      10 | 0x00B4      |         180 |
|      11 | 0x003C      |          60 |
|      12 | 0x0001      |           1 |
|      13 | 0x1BAF      |        7087 |
|      14 | 0x1BA9      |        7081 |
|      15 | 0x1BB0      |        7088 |
|      16 | 0x1BAA      |        7082 |
|      17 | 0x1BB1      |        7089 |
|      18 | 0x1BAB      |        7083 |
|      19 | 0x0003      |           3 |
|      20 | 0x1BAC      |        7084 |
|      21 | 0x1BAD      |        7085 |
|      22 | 0x1BAE      |        7086 |
|      23 | 0x0004      |           4 |
|      24 | 0x1BA2      |        7074 |

## String References

- **7074**: Proceed onward? [Yes./No.]
- **7080**: Proceed onward? [Yes./Warp to the Propagator./Turn back.]
- **7081**: Proceed onward? [Yes./Warp to the Solicitor./Turn back.]
- **7082**: Proceed onward? [Yes./Warp to the Ponderer./Turn back.]
- **7083**: Proceed onward? [Yes./Warp to the Propagator./Warp to the Solicitor./Turn back.]
- **7084**: Proceed onward? [Yes./Warp to the Propagator./Warp to the Ponderer./Turn back.]
- **7085**: Proceed onward? [Yes./Warp to the Solicitor./Warp to the Ponderer./Turn back.]
- **7086**: Proceed onward? [Yes./Warp to the Propagator./Warp to the Solicitor./Warp to the Ponderer./Turn back.]
- **7087**: Really warp to the Propagator? [Yes./No.]
- **7088**: Really warp to the Solicitor? [Yes./No.]
- **7089**: Really warp to the Ponderer? [Yes./No.]

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

### Event 0

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
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4C 00                                         L.            
```

#### Opcodes

```
  0: 0x0002 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             4D 00                                     M.          
```

#### Opcodes

```
  0: 0x0004 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0006    |
| Data Size    | 533 bytes |
| Instructions | 70        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   20 01  24 00 80 01 80 02 80 25         .$......%
0010: 02 00 10 02 80 00 FA 00  43 00 43 01 42 46 01 45  ........C.C.BF.E
0020: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 02 80  ..........fdo1..
0030: 1C 04 80 38 05 80 29 01  F0 FF FF 7F 29 45 06 80  ...8..).....)E..
0040: F8 FF FF 7F F8 FF FF 7F  7A 30 39 66 02 80 45 03  ........z09f..E.
0050: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 02 80 1C  .........fdi1...
0060: 07 80 52 06 80 F8 FF FF  7F F8 FF FF 7F 7A 30 39  ..R..........z09
0070: 66 4C 1C 08 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  fL...E..........
0080: 6F 76 6C 31 02 80 45 03  80 F0 FF FF 7F F0 FF FF  ovl1..E.........
0090: 7F 62 6C 6F 6E 02 80 45  09 80 F0 FF FF 7F F0 FF  .blon..E........
00A0: FF 7F 62 6C 6F 6E 02 80  45 06 80 F8 FF FF 7F F8  ..blon..E.......
00B0: FF FF 7F 7A 30 39 67 02  80 1C 0A 80 45 03 80 F0  ...z09g.....E...
00C0: FF FF 7F F0 FF FF 7F 66  64 6F 31 02 80 1C 0B 80  .......fdo1.....
00D0: 52 06 80 F8 FF FF 7F F8  FF FF 7F 7A 30 39 67 45  R..........z09gE
00E0: 03 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 66 02 80  ..........blof..
00F0: 03 01 10 0C 80 46 00 01  17 02 02 00 10 0C 80 00  .....F..........
0100: 07 02 24 0D 80 0C 80 02  80 25 02 00 10 02 80 00  ..$......%......
0110: F4 01 43 00 43 01 42 46  01 45 03 80 F0 FF FF 7F  ..C.C.BF.E......
0120: F0 FF FF 7F 66 64 6F 31  02 80 1C 04 80 38 05 80  ....fdo1.....8..
0130: 29 01 F0 FF FF 7F 29 45  06 80 F8 FF FF 7F F8 FF  ).....)E........
0140: FF 7F 7A 30 39 66 02 80  45 03 80 F0 FF FF 7F F0  ..z09f..E.......
0150: FF FF 7F 66 64 69 31 02  80 1C 07 80 52 06 80 F8  ...fdi1.....R...
0160: FF FF 7F F8 FF FF 7F 7A  30 39 66 4C 1C 08 80 45  .......z09fL...E
0170: 03 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 02 80  ..........ovl1..
0180: 45 03 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 02  E..........blon.
0190: 80 45 09 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
01A0: 02 80 45 06 80 F8 FF FF  7F F8 FF FF 7F 7A 30 39  ..E..........z09
01B0: 67 02 80 1C 0A 80 45 03  80 F0 FF FF 7F F0 FF FF  g.....E.........
01C0: 7F 66 64 6F 31 02 80 1C  0B 80 52 06 80 F8 FF FF  .fdo1.....R.....
01D0: 7F F8 FF FF 7F 7A 30 39  67 45 03 80 F0 FF FF 7F  .....z09gE......
01E0: F0 FF FF 7F 62 6C 6F 66  02 80 03 01 10 01 80 46  ....blof.......F
01F0: 00 01 04 02 02 00 10 0C  80 00 04 02 03 01 10 02  ................
0200: 80 01 04 02 01 17 02 02  00 10 01 80 00 17 02 03  ................
0210: 01 10 02 80 01 17 02 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x0006 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0008 [0x24] CREATE_DIALOG(message_id=7080*, default_option=2*, option_flags=0*)
    → "Proceed onward? [Yes./Warp to the Propagator./Turn back.]"
  2: 0x000F [0x25] WAIT_DIALOG_SELECT()
  3: 0x0010 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00FA
  4: 0x0018 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x001A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x001C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x001D [0x46] CAMERA_CONTROL: Disable user control
  8: 0x001F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0030 [0x1C] WAIT(120* ticks)
 10: 0x0033 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x0036 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 12: 0x003D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 13: 0x004E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x005F [0x1C] WAIT(300* ticks)
 15: 0x0062 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 16: 0x0071 [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x0072 [0x1C] WAIT(90* ticks)
 18: 0x0075 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0086 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0097 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x00A8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 22: 0x00B9 [0x1C] WAIT(180* ticks)
 23: 0x00BC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x00CD [0x1C] WAIT(60* ticks)
 25: 0x00D0 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 26: 0x00DF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x00F0 [0x03] Work_Zone[1] = 1*
 28: 0x00F5 [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x00F7 [0x01] GOTO 0x0217
 30: 0x00FA [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0207
 31: 0x0102 [0x24] CREATE_DIALOG(message_id=7087*, default_option=1*, option_flags=0*)
    → "Really warp to the Propagator? [Yes./No.]"
 32: 0x0109 [0x25] WAIT_DIALOG_SELECT()
 33: 0x010A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01F4
 34: 0x0112 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x0114 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x0116 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 37: 0x0117 [0x46] CAMERA_CONTROL: Disable user control
 38: 0x0119 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x012A [0x1C] WAIT(120* ticks)
 40: 0x012D [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 41: 0x0130 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 42: 0x0137 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 43: 0x0148 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 44: 0x0159 [0x1C] WAIT(300* ticks)
 45: 0x015C [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 46: 0x016B [0x4C] EventEntity->StatusEvent = 8 // Open door
 47: 0x016C [0x1C] WAIT(90* ticks)
 48: 0x016F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x0180 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x0191 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 51: 0x01A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 52: 0x01B3 [0x1C] WAIT(180* ticks)
 53: 0x01B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 54: 0x01C7 [0x1C] WAIT(60* ticks)
 55: 0x01CA [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 56: 0x01D9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x01EA [0x03] Work_Zone[1] = 2*
 58: 0x01EF [0x46] CAMERA_CONTROL: Restore default settings
 59: 0x01F1 [0x01] GOTO 0x0204
 60: 0x01F4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0204
 61: 0x01FC [0x03] Work_Zone[1] = 0*
 62: 0x0201 [0x01] GOTO 0x0204

SUBROUTINE_0204:
 63: 0x0204 [0x01] GOTO 0x0217
 64: 0x0207 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0217
 65: 0x020F [0x03] Work_Zone[1] = 0*
 66: 0x0214 [0x01] GOTO 0x0217

SUBROUTINE_0217:
 67: 0x0217 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 68: 0x0219 [0x21] END_EVENT
 69: 0x021A [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x021B    |
| Data Size    | 533 bytes |
| Instructions | 70        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                                   20 01 24 0E 80              .$..
0220: 01 80 02 80 25 02 00 10  02 80 00 0F 03 43 00 43  ....%........C.C
0230: 01 42 46 01 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  .BF.E..........f
0240: 64 6F 31 02 80 1C 04 80  38 05 80 29 01 F0 FF FF  do1.....8..)....
0250: 7F 29 45 06 80 F8 FF FF  7F F8 FF FF 7F 7A 30 39  .)E..........z09
0260: 66 02 80 45 03 80 F0 FF  FF 7F F0 FF FF 7F 66 64  f..E..........fd
0270: 69 31 02 80 1C 07 80 52  06 80 F8 FF FF 7F F8 FF  i1.....R........
0280: FF 7F 7A 30 39 66 4C 1C  08 80 45 03 80 F0 FF FF  ..z09fL...E.....
0290: 7F F0 FF FF 7F 6F 76 6C  31 02 80 45 03 80 F0 FF  .....ovl1..E....
02A0: FF 7F F0 FF FF 7F 62 6C  6F 6E 02 80 45 09 80 F0  ......blon..E...
02B0: FF FF 7F F0 FF FF 7F 62  6C 6F 6E 02 80 45 06 80  .......blon..E..
02C0: F8 FF FF 7F F8 FF FF 7F  7A 30 39 67 02 80 1C 0A  ........z09g....
02D0: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
02E0: 02 80 1C 0B 80 52 06 80  F8 FF FF 7F F8 FF FF 7F  .....R..........
02F0: 7A 30 39 67 45 03 80 F0  FF FF 7F F0 FF FF 7F 62  z09gE..........b
0300: 6C 6F 66 02 80 03 01 10  0C 80 46 00 01 2C 04 02  lof.......F..,..
0310: 00 10 0C 80 00 1C 04 24  0F 80 0C 80 02 80 25 02  .......$......%.
0320: 00 10 02 80 00 09 04 43  00 43 01 42 46 01 45 03  .......C.C.BF.E.
0330: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 02 80 1C  .........fdo1...
0340: 04 80 38 05 80 29 01 F0  FF FF 7F 29 45 06 80 F8  ..8..).....)E...
0350: FF FF 7F F8 FF FF 7F 7A  30 39 66 02 80 45 03 80  .......z09f..E..
0360: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 02 80 1C 07  ........fdi1....
0370: 80 52 06 80 F8 FF FF 7F  F8 FF FF 7F 7A 30 39 66  .R..........z09f
0380: 4C 1C 08 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 6F  L...E..........o
0390: 76 6C 31 02 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  vl1..E..........
03A0: 62 6C 6F 6E 02 80 45 09  80 F0 FF FF 7F F0 FF FF  blon..E.........
03B0: 7F 62 6C 6F 6E 02 80 45  06 80 F8 FF FF 7F F8 FF  .blon..E........
03C0: FF 7F 7A 30 39 67 02 80  1C 0A 80 45 03 80 F0 FF  ..z09g.....E....
03D0: FF 7F F0 FF FF 7F 66 64  6F 31 02 80 1C 0B 80 52  ......fdo1.....R
03E0: 06 80 F8 FF FF 7F F8 FF  FF 7F 7A 30 39 67 45 03  ..........z09gE.
03F0: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 66 02 80 03  .........blof...
0400: 01 10 01 80 46 00 01 19  04 02 00 10 0C 80 00 19  ....F...........
0410: 04 03 01 10 02 80 01 19  04 01 2C 04 02 00 10 01  ..........,.....
0420: 80 00 2C 04 03 01 10 02  80 01 2C 04 20 00 21 00  ..,.......,. .!.
```

#### Opcodes

```
  0: 0x021B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x021D [0x24] CREATE_DIALOG(message_id=7081*, default_option=2*, option_flags=0*)
    → "Proceed onward? [Yes./Warp to the Solicitor./Turn back.]"
  2: 0x0224 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0225 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x030F
  4: 0x022D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x022F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0231 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0232 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0234 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0245 [0x1C] WAIT(120* ticks)
 10: 0x0248 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x024B [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 12: 0x0252 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 13: 0x0263 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0274 [0x1C] WAIT(300* ticks)
 15: 0x0277 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 16: 0x0286 [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x0287 [0x1C] WAIT(90* ticks)
 18: 0x028A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x029B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x02AC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x02BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 22: 0x02CE [0x1C] WAIT(180* ticks)
 23: 0x02D1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x02E2 [0x1C] WAIT(60* ticks)
 25: 0x02E5 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 26: 0x02F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x0305 [0x03] Work_Zone[1] = 1*
 28: 0x030A [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x030C [0x01] GOTO 0x042C
 30: 0x030F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x041C
 31: 0x0317 [0x24] CREATE_DIALOG(message_id=7088*, default_option=1*, option_flags=0*)
    → "Really warp to the Solicitor? [Yes./No.]"
 32: 0x031E [0x25] WAIT_DIALOG_SELECT()
 33: 0x031F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0409
 34: 0x0327 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x0329 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x032B [0x42] SET_CLI_EVENT_CANCEL_DATA()
 37: 0x032C [0x46] CAMERA_CONTROL: Disable user control
 38: 0x032E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x033F [0x1C] WAIT(120* ticks)
 40: 0x0342 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 41: 0x0345 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 42: 0x034C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 43: 0x035D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 44: 0x036E [0x1C] WAIT(300* ticks)
 45: 0x0371 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 46: 0x0380 [0x4C] EventEntity->StatusEvent = 8 // Open door
 47: 0x0381 [0x1C] WAIT(90* ticks)
 48: 0x0384 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x0395 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x03A6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 51: 0x03B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 52: 0x03C8 [0x1C] WAIT(180* ticks)
 53: 0x03CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 54: 0x03DC [0x1C] WAIT(60* ticks)
 55: 0x03DF [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 56: 0x03EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x03FF [0x03] Work_Zone[1] = 2*
 58: 0x0404 [0x46] CAMERA_CONTROL: Restore default settings
 59: 0x0406 [0x01] GOTO 0x0419
 60: 0x0409 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0419
 61: 0x0411 [0x03] Work_Zone[1] = 0*
 62: 0x0416 [0x01] GOTO 0x0419

SUBROUTINE_0419:
 63: 0x0419 [0x01] GOTO 0x042C
 64: 0x041C [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x042C
 65: 0x0424 [0x03] Work_Zone[1] = 0*
 66: 0x0429 [0x01] GOTO 0x042C

SUBROUTINE_042C:
 67: 0x042C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 68: 0x042E [0x21] END_EVENT
 69: 0x042F [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0430    |
| Data Size    | 533 bytes |
| Instructions | 70        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0430: 20 01 24 10 80 01 80 02  80 25 02 00 10 02 80 00   .$......%......
0440: 24 05 43 00 43 01 42 46  01 45 03 80 F0 FF FF 7F  $.C.C.BF.E......
0450: F0 FF FF 7F 66 64 6F 31  02 80 1C 04 80 38 05 80  ....fdo1.....8..
0460: 29 01 F0 FF FF 7F 29 45  06 80 F8 FF FF 7F F8 FF  ).....)E........
0470: FF 7F 7A 30 39 66 02 80  45 03 80 F0 FF FF 7F F0  ..z09f..E.......
0480: FF FF 7F 66 64 69 31 02  80 1C 07 80 52 06 80 F8  ...fdi1.....R...
0490: FF FF 7F F8 FF FF 7F 7A  30 39 66 4C 1C 08 80 45  .......z09fL...E
04A0: 03 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 02 80  ..........ovl1..
04B0: 45 03 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 02  E..........blon.
04C0: 80 45 09 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
04D0: 02 80 45 06 80 F8 FF FF  7F F8 FF FF 7F 7A 30 39  ..E..........z09
04E0: 67 02 80 1C 0A 80 45 03  80 F0 FF FF 7F F0 FF FF  g.....E.........
04F0: 7F 66 64 6F 31 02 80 1C  0B 80 52 06 80 F8 FF FF  .fdo1.....R.....
0500: 7F F8 FF FF 7F 7A 30 39  67 45 03 80 F0 FF FF 7F  .....z09gE......
0510: F0 FF FF 7F 62 6C 6F 66  02 80 03 01 10 0C 80 46  ....blof.......F
0520: 00 01 41 06 02 00 10 0C  80 00 31 06 24 11 80 0C  ..A.......1.$...
0530: 80 02 80 25 02 00 10 02  80 00 1E 06 43 00 43 01  ...%........C.C.
0540: 42 46 01 45 03 80 F0 FF  FF 7F F0 FF FF 7F 66 64  BF.E..........fd
0550: 6F 31 02 80 1C 04 80 38  05 80 29 01 F0 FF FF 7F  o1.....8..).....
0560: 29 45 06 80 F8 FF FF 7F  F8 FF FF 7F 7A 30 39 66  )E..........z09f
0570: 02 80 45 03 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
0580: 31 02 80 1C 07 80 52 06  80 F8 FF FF 7F F8 FF FF  1.....R.........
0590: 7F 7A 30 39 66 4C 1C 08  80 45 03 80 F0 FF FF 7F  .z09fL...E......
05A0: F0 FF FF 7F 6F 76 6C 31  02 80 45 03 80 F0 FF FF  ....ovl1..E.....
05B0: 7F F0 FF FF 7F 62 6C 6F  6E 02 80 45 09 80 F0 FF  .....blon..E....
05C0: FF 7F F0 FF FF 7F 62 6C  6F 6E 02 80 45 06 80 F8  ......blon..E...
05D0: FF FF 7F F8 FF FF 7F 7A  30 39 67 02 80 1C 0A 80  .......z09g.....
05E0: 45 03 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 02  E..........fdo1.
05F0: 80 1C 0B 80 52 06 80 F8  FF FF 7F F8 FF FF 7F 7A  ....R..........z
0600: 30 39 67 45 03 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  09gE..........bl
0610: 6F 66 02 80 03 01 10 01  80 46 00 01 2E 06 02 00  of.......F......
0620: 10 0C 80 00 2E 06 03 01  10 02 80 01 2E 06 01 41  ...............A
0630: 06 02 00 10 01 80 00 41  06 03 01 10 02 80 01 41  .......A.......A
0640: 06 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0430 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0432 [0x24] CREATE_DIALOG(message_id=7082*, default_option=2*, option_flags=0*)
    → "Proceed onward? [Yes./Warp to the Ponderer./Turn back.]"
  2: 0x0439 [0x25] WAIT_DIALOG_SELECT()
  3: 0x043A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0524
  4: 0x0442 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0444 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0446 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0447 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0449 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x045A [0x1C] WAIT(120* ticks)
 10: 0x045D [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x0460 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 12: 0x0467 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 13: 0x0478 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0489 [0x1C] WAIT(300* ticks)
 15: 0x048C [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 16: 0x049B [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x049C [0x1C] WAIT(90* ticks)
 18: 0x049F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x04B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x04C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x04D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 22: 0x04E3 [0x1C] WAIT(180* ticks)
 23: 0x04E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x04F7 [0x1C] WAIT(60* ticks)
 25: 0x04FA [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 26: 0x0509 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x051A [0x03] Work_Zone[1] = 1*
 28: 0x051F [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x0521 [0x01] GOTO 0x0641
 30: 0x0524 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0631
 31: 0x052C [0x24] CREATE_DIALOG(message_id=7089*, default_option=1*, option_flags=0*)
    → "Really warp to the Ponderer? [Yes./No.]"
 32: 0x0533 [0x25] WAIT_DIALOG_SELECT()
 33: 0x0534 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x061E
 34: 0x053C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x053E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x0540 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 37: 0x0541 [0x46] CAMERA_CONTROL: Disable user control
 38: 0x0543 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x0554 [0x1C] WAIT(120* ticks)
 40: 0x0557 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 41: 0x055A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 42: 0x0561 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 43: 0x0572 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 44: 0x0583 [0x1C] WAIT(300* ticks)
 45: 0x0586 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 46: 0x0595 [0x4C] EventEntity->StatusEvent = 8 // Open door
 47: 0x0596 [0x1C] WAIT(90* ticks)
 48: 0x0599 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x05AA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x05BB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 51: 0x05CC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 52: 0x05DD [0x1C] WAIT(180* ticks)
 53: 0x05E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 54: 0x05F1 [0x1C] WAIT(60* ticks)
 55: 0x05F4 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 56: 0x0603 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x0614 [0x03] Work_Zone[1] = 2*
 58: 0x0619 [0x46] CAMERA_CONTROL: Restore default settings
 59: 0x061B [0x01] GOTO 0x062E
 60: 0x061E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x062E
 61: 0x0626 [0x03] Work_Zone[1] = 0*
 62: 0x062B [0x01] GOTO 0x062E

SUBROUTINE_062E:
 63: 0x062E [0x01] GOTO 0x0641
 64: 0x0631 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0641
 65: 0x0639 [0x03] Work_Zone[1] = 0*
 66: 0x063E [0x01] GOTO 0x0641

SUBROUTINE_0641:
 67: 0x0641 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 68: 0x0643 [0x21] END_EVENT
 69: 0x0644 [0x00] END_REQSTACK()
```

### Event 109

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0645    |
| Data Size    | 802 bytes |
| Instructions | 104       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0640:                20 01 24  12 80 13 80 02 80 25 02        .$......%.
0650: 00 10 02 80 00 39 07 43  00 43 01 42 46 01 45 03  .....9.C.C.BF.E.
0660: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 02 80 1C  .........fdo1...
0670: 04 80 38 05 80 29 01 F0  FF FF 7F 29 45 06 80 F8  ..8..).....)E...
0680: FF FF 7F F8 FF FF 7F 7A  30 39 66 02 80 45 03 80  .......z09f..E..
0690: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 02 80 1C 07  ........fdi1....
06A0: 80 52 06 80 F8 FF FF 7F  F8 FF FF 7F 7A 30 39 66  .R..........z09f
06B0: 4C 1C 08 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 6F  L...E..........o
06C0: 76 6C 31 02 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  vl1..E..........
06D0: 62 6C 6F 6E 02 80 45 09  80 F0 FF FF 7F F0 FF FF  blon..E.........
06E0: 7F 62 6C 6F 6E 02 80 45  06 80 F8 FF FF 7F F8 FF  .blon..E........
06F0: FF 7F 7A 30 39 67 02 80  1C 0A 80 45 03 80 F0 FF  ..z09g.....E....
0700: FF 7F F0 FF FF 7F 66 64  6F 31 02 80 1C 0B 80 52  ......fdo1.....R
0710: 06 80 F8 FF FF 7F F8 FF  FF 7F 7A 30 39 67 45 03  ..........z09gE.
0720: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 66 02 80 03  .........blof...
0730: 01 10 0C 80 46 00 01 63  09 02 00 10 0C 80 00 46  ....F..c.......F
0740: 08 24 0D 80 0C 80 02 80  25 02 00 10 02 80 00 33  .$......%......3
0750: 08 43 00 43 01 42 46 01  45 03 80 F0 FF FF 7F F0  .C.C.BF.E.......
0760: FF FF 7F 66 64 6F 31 02  80 1C 04 80 38 05 80 29  ...fdo1.....8..)
0770: 01 F0 FF FF 7F 29 45 06  80 F8 FF FF 7F F8 FF FF  .....)E.........
0780: 7F 7A 30 39 66 02 80 45  03 80 F0 FF FF 7F F0 FF  .z09f..E........
0790: FF 7F 66 64 69 31 02 80  1C 07 80 52 06 80 F8 FF  ..fdi1.....R....
07A0: FF 7F F8 FF FF 7F 7A 30  39 66 4C 1C 08 80 45 03  ......z09fL...E.
07B0: 80 F0 FF FF 7F F0 FF FF  7F 6F 76 6C 31 02 80 45  .........ovl1..E
07C0: 03 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 02 80  ..........blon..
07D0: 45 09 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 02  E..........blon.
07E0: 80 45 06 80 F8 FF FF 7F  F8 FF FF 7F 7A 30 39 67  .E..........z09g
07F0: 02 80 1C 0A 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0800: 66 64 6F 31 02 80 1C 0B  80 52 06 80 F8 FF FF 7F  fdo1.....R......
0810: F8 FF FF 7F 7A 30 39 67  45 03 80 F0 FF FF 7F F0  ....z09gE.......
0820: FF FF 7F 62 6C 6F 66 02  80 03 01 10 01 80 46 00  ...blof.......F.
0830: 01 43 08 02 00 10 0C 80  00 43 08 03 01 10 02 80  .C.......C......
0840: 01 43 08 01 63 09 02 00  10 01 80 00 53 09 24 0F  .C..c.......S.$.
0850: 80 0C 80 02 80 25 02 00  10 02 80 00 40 09 43 00  .....%......@.C.
0860: 43 01 42 46 01 45 03 80  F0 FF FF 7F F0 FF FF 7F  C.BF.E..........
0870: 66 64 6F 31 02 80 1C 04  80 38 05 80 29 01 F0 FF  fdo1.....8..)...
0880: FF 7F 29 45 06 80 F8 FF  FF 7F F8 FF FF 7F 7A 30  ..)E..........z0
0890: 39 66 02 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  9f..E..........f
08A0: 64 69 31 02 80 1C 07 80  52 06 80 F8 FF FF 7F F8  di1.....R.......
08B0: FF FF 7F 7A 30 39 66 4C  1C 08 80 45 03 80 F0 FF  ...z09fL...E....
08C0: FF 7F F0 FF FF 7F 6F 76  6C 31 02 80 45 03 80 F0  ......ovl1..E...
08D0: FF FF 7F F0 FF FF 7F 62  6C 6F 6E 02 80 45 09 80  .......blon..E..
08E0: F0 FF FF 7F F0 FF FF 7F  62 6C 6F 6E 02 80 45 06  ........blon..E.
08F0: 80 F8 FF FF 7F F8 FF FF  7F 7A 30 39 67 02 80 1C  .........z09g...
0900: 0A 80 45 03 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0910: 31 02 80 1C 0B 80 52 06  80 F8 FF FF 7F F8 FF FF  1.....R.........
0920: 7F 7A 30 39 67 45 03 80  F0 FF FF 7F F0 FF FF 7F  .z09gE..........
0930: 62 6C 6F 66 02 80 03 01  10 13 80 46 00 01 50 09  blof.......F..P.
0940: 02 00 10 0C 80 00 50 09  03 01 10 02 80 01 50 09  ......P.......P.
0950: 01 63 09 02 00 10 13 80  00 63 09 03 01 10 02 80  .c.......c......
0960: 01 63 09 20 00 21 00                              .c. .!.         
```

#### Opcodes

```
  0: 0x0645 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0647 [0x24] CREATE_DIALOG(message_id=7083*, default_option=3*, option_flags=0*)
    → "Proceed onward? [Yes./Warp to the Propagator./Warp to the Solicitor./Turn back.]"
  2: 0x064E [0x25] WAIT_DIALOG_SELECT()
  3: 0x064F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0739
  4: 0x0657 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0659 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x065B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x065C [0x46] CAMERA_CONTROL: Disable user control
  8: 0x065E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x066F [0x1C] WAIT(120* ticks)
 10: 0x0672 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x0675 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 12: 0x067C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 13: 0x068D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x069E [0x1C] WAIT(300* ticks)
 15: 0x06A1 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 16: 0x06B0 [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x06B1 [0x1C] WAIT(90* ticks)
 18: 0x06B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x06C5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x06D6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x06E7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 22: 0x06F8 [0x1C] WAIT(180* ticks)
 23: 0x06FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x070C [0x1C] WAIT(60* ticks)
 25: 0x070F [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 26: 0x071E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x072F [0x03] Work_Zone[1] = 1*
 28: 0x0734 [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x0736 [0x01] GOTO 0x0963
 30: 0x0739 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0846
 31: 0x0741 [0x24] CREATE_DIALOG(message_id=7087*, default_option=1*, option_flags=0*)
    → "Really warp to the Propagator? [Yes./No.]"
 32: 0x0748 [0x25] WAIT_DIALOG_SELECT()
 33: 0x0749 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0833
 34: 0x0751 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x0753 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x0755 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 37: 0x0756 [0x46] CAMERA_CONTROL: Disable user control
 38: 0x0758 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x0769 [0x1C] WAIT(120* ticks)
 40: 0x076C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 41: 0x076F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 42: 0x0776 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 43: 0x0787 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 44: 0x0798 [0x1C] WAIT(300* ticks)
 45: 0x079B [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 46: 0x07AA [0x4C] EventEntity->StatusEvent = 8 // Open door
 47: 0x07AB [0x1C] WAIT(90* ticks)
 48: 0x07AE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x07BF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x07D0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 51: 0x07E1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 52: 0x07F2 [0x1C] WAIT(180* ticks)
 53: 0x07F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 54: 0x0806 [0x1C] WAIT(60* ticks)
 55: 0x0809 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 56: 0x0818 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x0829 [0x03] Work_Zone[1] = 2*
 58: 0x082E [0x46] CAMERA_CONTROL: Restore default settings
 59: 0x0830 [0x01] GOTO 0x0843
 60: 0x0833 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0843
 61: 0x083B [0x03] Work_Zone[1] = 0*
 62: 0x0840 [0x01] GOTO 0x0843

SUBROUTINE_0843:
 63: 0x0843 [0x01] GOTO 0x0963
 64: 0x0846 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0953
 65: 0x084E [0x24] CREATE_DIALOG(message_id=7088*, default_option=1*, option_flags=0*)
    → "Really warp to the Solicitor? [Yes./No.]"
 66: 0x0855 [0x25] WAIT_DIALOG_SELECT()
 67: 0x0856 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0940
 68: 0x085E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 69: 0x0860 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 70: 0x0862 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 71: 0x0863 [0x46] CAMERA_CONTROL: Disable user control
 72: 0x0865 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 73: 0x0876 [0x1C] WAIT(120* ticks)
 74: 0x0879 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 75: 0x087C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 76: 0x0883 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 77: 0x0894 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 78: 0x08A5 [0x1C] WAIT(300* ticks)
 79: 0x08A8 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 80: 0x08B7 [0x4C] EventEntity->StatusEvent = 8 // Open door
 81: 0x08B8 [0x1C] WAIT(90* ticks)
 82: 0x08BB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 83: 0x08CC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 84: 0x08DD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 85: 0x08EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 86: 0x08FF [0x1C] WAIT(180* ticks)
 87: 0x0902 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 88: 0x0913 [0x1C] WAIT(60* ticks)
 89: 0x0916 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 90: 0x0925 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 91: 0x0936 [0x03] Work_Zone[1] = 3*
 92: 0x093B [0x46] CAMERA_CONTROL: Restore default settings
 93: 0x093D [0x01] GOTO 0x0950
 94: 0x0940 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0950
 95: 0x0948 [0x03] Work_Zone[1] = 0*
 96: 0x094D [0x01] GOTO 0x0950

SUBROUTINE_0950:
 97: 0x0950 [0x01] GOTO 0x0963
 98: 0x0953 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0963
 99: 0x095B [0x03] Work_Zone[1] = 0*
100: 0x0960 [0x01] GOTO 0x0963

SUBROUTINE_0963:
101: 0x0963 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
102: 0x0965 [0x21] END_EVENT
103: 0x0966 [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0967    |
| Data Size    | 802 bytes |
| Instructions | 104       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0960:                      20  01 24 14 80 13 80 02 80          .$......
0970: 25 02 00 10 02 80 00 5B  0A 43 00 43 01 42 46 01  %......[.C.C.BF.
0980: 45 03 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 02  E..........fdo1.
0990: 80 1C 04 80 38 05 80 29  01 F0 FF FF 7F 29 45 06  ....8..).....)E.
09A0: 80 F8 FF FF 7F F8 FF FF  7F 7A 30 39 66 02 80 45  .........z09f..E
09B0: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 02 80  ..........fdi1..
09C0: 1C 07 80 52 06 80 F8 FF  FF 7F F8 FF FF 7F 7A 30  ...R..........z0
09D0: 39 66 4C 1C 08 80 45 03  80 F0 FF FF 7F F0 FF FF  9fL...E.........
09E0: 7F 6F 76 6C 31 02 80 45  03 80 F0 FF FF 7F F0 FF  .ovl1..E........
09F0: FF 7F 62 6C 6F 6E 02 80  45 09 80 F0 FF FF 7F F0  ..blon..E.......
0A00: FF FF 7F 62 6C 6F 6E 02  80 45 06 80 F8 FF FF 7F  ...blon..E......
0A10: F8 FF FF 7F 7A 30 39 67  02 80 1C 0A 80 45 03 80  ....z09g.....E..
0A20: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 02 80 1C 0B  ........fdo1....
0A30: 80 52 06 80 F8 FF FF 7F  F8 FF FF 7F 7A 30 39 67  .R..........z09g
0A40: 45 03 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 66 02  E..........blof.
0A50: 80 03 01 10 0C 80 46 00  01 85 0C 02 00 10 0C 80  ......F.........
0A60: 00 68 0B 24 0D 80 0C 80  02 80 25 02 00 10 02 80  .h.$......%.....
0A70: 00 55 0B 43 00 43 01 42  46 01 45 03 80 F0 FF FF  .U.C.C.BF.E.....
0A80: 7F F0 FF FF 7F 66 64 6F  31 02 80 1C 04 80 38 05  .....fdo1.....8.
0A90: 80 29 01 F0 FF FF 7F 29  45 06 80 F8 FF FF 7F F8  .).....)E.......
0AA0: FF FF 7F 7A 30 39 66 02  80 45 03 80 F0 FF FF 7F  ...z09f..E......
0AB0: F0 FF FF 7F 66 64 69 31  02 80 1C 07 80 52 06 80  ....fdi1.....R..
0AC0: F8 FF FF 7F F8 FF FF 7F  7A 30 39 66 4C 1C 08 80  ........z09fL...
0AD0: 45 03 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 02  E..........ovl1.
0AE0: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
0AF0: 02 80 45 09 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
0B00: 6E 02 80 45 06 80 F8 FF  FF 7F F8 FF FF 7F 7A 30  n..E..........z0
0B10: 39 67 02 80 1C 0A 80 45  03 80 F0 FF FF 7F F0 FF  9g.....E........
0B20: FF 7F 66 64 6F 31 02 80  1C 0B 80 52 06 80 F8 FF  ..fdo1.....R....
0B30: FF 7F F8 FF FF 7F 7A 30  39 67 45 03 80 F0 FF FF  ......z09gE.....
0B40: 7F F0 FF FF 7F 62 6C 6F  66 02 80 03 01 10 01 80  .....blof.......
0B50: 46 00 01 65 0B 02 00 10  0C 80 00 65 0B 03 01 10  F..e.......e....
0B60: 02 80 01 65 0B 01 85 0C  02 00 10 01 80 00 75 0C  ...e..........u.
0B70: 24 11 80 0C 80 02 80 25  02 00 10 02 80 00 62 0C  $......%......b.
0B80: 43 00 43 01 42 46 01 45  03 80 F0 FF FF 7F F0 FF  C.C.BF.E........
0B90: FF 7F 66 64 6F 31 02 80  1C 04 80 38 05 80 29 01  ..fdo1.....8..).
0BA0: F0 FF FF 7F 29 45 06 80  F8 FF FF 7F F8 FF FF 7F  ....)E..........
0BB0: 7A 30 39 66 02 80 45 03  80 F0 FF FF 7F F0 FF FF  z09f..E.........
0BC0: 7F 66 64 69 31 02 80 1C  07 80 52 06 80 F8 FF FF  .fdi1.....R.....
0BD0: 7F F8 FF FF 7F 7A 30 39  66 4C 1C 08 80 45 03 80  .....z09fL...E..
0BE0: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 02 80 45 03  ........ovl1..E.
0BF0: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 02 80 45  .........blon..E
0C00: 09 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 02 80  ..........blon..
0C10: 45 06 80 F8 FF FF 7F F8  FF FF 7F 7A 30 39 67 02  E..........z09g.
0C20: 80 1C 0A 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0C30: 64 6F 31 02 80 1C 0B 80  52 06 80 F8 FF FF 7F F8  do1.....R.......
0C40: FF FF 7F 7A 30 39 67 45  03 80 F0 FF FF 7F F0 FF  ...z09gE........
0C50: FF 7F 62 6C 6F 66 02 80  03 01 10 13 80 46 00 01  ..blof.......F..
0C60: 72 0C 02 00 10 0C 80 00  72 0C 03 01 10 02 80 01  r.......r.......
0C70: 72 0C 01 85 0C 02 00 10  13 80 00 85 0C 03 01 10  r...............
0C80: 02 80 01 85 0C 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x0967 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0969 [0x24] CREATE_DIALOG(message_id=7084*, default_option=3*, option_flags=0*)
    → "Proceed onward? [Yes./Warp to the Propagator./Warp to the Ponderer./Turn back.]"
  2: 0x0970 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0971 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0A5B
  4: 0x0979 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x097B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x097D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x097E [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0980 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0991 [0x1C] WAIT(120* ticks)
 10: 0x0994 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x0997 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 12: 0x099E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 13: 0x09AF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x09C0 [0x1C] WAIT(300* ticks)
 15: 0x09C3 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 16: 0x09D2 [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x09D3 [0x1C] WAIT(90* ticks)
 18: 0x09D6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x09E7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x09F8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0A09 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 22: 0x0A1A [0x1C] WAIT(180* ticks)
 23: 0x0A1D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x0A2E [0x1C] WAIT(60* ticks)
 25: 0x0A31 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 26: 0x0A40 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x0A51 [0x03] Work_Zone[1] = 1*
 28: 0x0A56 [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x0A58 [0x01] GOTO 0x0C85
 30: 0x0A5B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0B68
 31: 0x0A63 [0x24] CREATE_DIALOG(message_id=7087*, default_option=1*, option_flags=0*)
    → "Really warp to the Propagator? [Yes./No.]"
 32: 0x0A6A [0x25] WAIT_DIALOG_SELECT()
 33: 0x0A6B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0B55
 34: 0x0A73 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x0A75 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x0A77 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 37: 0x0A78 [0x46] CAMERA_CONTROL: Disable user control
 38: 0x0A7A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x0A8B [0x1C] WAIT(120* ticks)
 40: 0x0A8E [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 41: 0x0A91 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 42: 0x0A98 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 43: 0x0AA9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 44: 0x0ABA [0x1C] WAIT(300* ticks)
 45: 0x0ABD [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 46: 0x0ACC [0x4C] EventEntity->StatusEvent = 8 // Open door
 47: 0x0ACD [0x1C] WAIT(90* ticks)
 48: 0x0AD0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x0AE1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x0AF2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 51: 0x0B03 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 52: 0x0B14 [0x1C] WAIT(180* ticks)
 53: 0x0B17 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 54: 0x0B28 [0x1C] WAIT(60* ticks)
 55: 0x0B2B [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 56: 0x0B3A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x0B4B [0x03] Work_Zone[1] = 2*
 58: 0x0B50 [0x46] CAMERA_CONTROL: Restore default settings
 59: 0x0B52 [0x01] GOTO 0x0B65
 60: 0x0B55 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0B65
 61: 0x0B5D [0x03] Work_Zone[1] = 0*
 62: 0x0B62 [0x01] GOTO 0x0B65

SUBROUTINE_0B65:
 63: 0x0B65 [0x01] GOTO 0x0C85
 64: 0x0B68 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0C75
 65: 0x0B70 [0x24] CREATE_DIALOG(message_id=7089*, default_option=1*, option_flags=0*)
    → "Really warp to the Ponderer? [Yes./No.]"
 66: 0x0B77 [0x25] WAIT_DIALOG_SELECT()
 67: 0x0B78 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0C62
 68: 0x0B80 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 69: 0x0B82 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 70: 0x0B84 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 71: 0x0B85 [0x46] CAMERA_CONTROL: Disable user control
 72: 0x0B87 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 73: 0x0B98 [0x1C] WAIT(120* ticks)
 74: 0x0B9B [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 75: 0x0B9E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 76: 0x0BA5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 77: 0x0BB6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 78: 0x0BC7 [0x1C] WAIT(300* ticks)
 79: 0x0BCA [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 80: 0x0BD9 [0x4C] EventEntity->StatusEvent = 8 // Open door
 81: 0x0BDA [0x1C] WAIT(90* ticks)
 82: 0x0BDD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 83: 0x0BEE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 84: 0x0BFF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 85: 0x0C10 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 86: 0x0C21 [0x1C] WAIT(180* ticks)
 87: 0x0C24 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 88: 0x0C35 [0x1C] WAIT(60* ticks)
 89: 0x0C38 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 90: 0x0C47 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 91: 0x0C58 [0x03] Work_Zone[1] = 3*
 92: 0x0C5D [0x46] CAMERA_CONTROL: Restore default settings
 93: 0x0C5F [0x01] GOTO 0x0C72
 94: 0x0C62 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0C72
 95: 0x0C6A [0x03] Work_Zone[1] = 0*
 96: 0x0C6F [0x01] GOTO 0x0C72

SUBROUTINE_0C72:
 97: 0x0C72 [0x01] GOTO 0x0C85
 98: 0x0C75 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0C85
 99: 0x0C7D [0x03] Work_Zone[1] = 0*
100: 0x0C82 [0x01] GOTO 0x0C85

SUBROUTINE_0C85:
101: 0x0C85 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
102: 0x0C87 [0x21] END_EVENT
103: 0x0C88 [0x00] END_REQSTACK()
```

### Event 111

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0C89    |
| Data Size    | 802 bytes |
| Instructions | 104       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0C80:                             20 01 24 15 80 13 80            .$....
0C90: 02 80 25 02 00 10 02 80  00 7D 0D 43 00 43 01 42  ..%......}.C.C.B
0CA0: 46 01 45 03 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  F.E..........fdo
0CB0: 31 02 80 1C 04 80 38 05  80 29 01 F0 FF FF 7F 29  1.....8..).....)
0CC0: 45 06 80 F8 FF FF 7F F8  FF FF 7F 7A 30 39 66 02  E..........z09f.
0CD0: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
0CE0: 02 80 1C 07 80 52 06 80  F8 FF FF 7F F8 FF FF 7F  .....R..........
0CF0: 7A 30 39 66 4C 1C 08 80  45 03 80 F0 FF FF 7F F0  z09fL...E.......
0D00: FF FF 7F 6F 76 6C 31 02  80 45 03 80 F0 FF FF 7F  ...ovl1..E......
0D10: F0 FF FF 7F 62 6C 6F 6E  02 80 45 09 80 F0 FF FF  ....blon..E.....
0D20: 7F F0 FF FF 7F 62 6C 6F  6E 02 80 45 06 80 F8 FF  .....blon..E....
0D30: FF 7F F8 FF FF 7F 7A 30  39 67 02 80 1C 0A 80 45  ......z09g.....E
0D40: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 02 80  ..........fdo1..
0D50: 1C 0B 80 52 06 80 F8 FF  FF 7F F8 FF FF 7F 7A 30  ...R..........z0
0D60: 39 67 45 03 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  9gE..........blo
0D70: 66 02 80 03 01 10 0C 80  46 00 01 A7 0F 02 00 10  f.......F.......
0D80: 0C 80 00 8A 0E 24 0F 80  0C 80 02 80 25 02 00 10  .....$......%...
0D90: 02 80 00 77 0E 43 00 43  01 42 46 01 45 03 80 F0  ...w.C.C.BF.E...
0DA0: FF FF 7F F0 FF FF 7F 66  64 6F 31 02 80 1C 04 80  .......fdo1.....
0DB0: 38 05 80 29 01 F0 FF FF  7F 29 45 06 80 F8 FF FF  8..).....)E.....
0DC0: 7F F8 FF FF 7F 7A 30 39  66 02 80 45 03 80 F0 FF  .....z09f..E....
0DD0: FF 7F F0 FF FF 7F 66 64  69 31 02 80 1C 07 80 52  ......fdi1.....R
0DE0: 06 80 F8 FF FF 7F F8 FF  FF 7F 7A 30 39 66 4C 1C  ..........z09fL.
0DF0: 08 80 45 03 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  ..E..........ovl
0E00: 31 02 80 45 03 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  1..E..........bl
0E10: 6F 6E 02 80 45 09 80 F0  FF FF 7F F0 FF FF 7F 62  on..E..........b
0E20: 6C 6F 6E 02 80 45 06 80  F8 FF FF 7F F8 FF FF 7F  lon..E..........
0E30: 7A 30 39 67 02 80 1C 0A  80 45 03 80 F0 FF FF 7F  z09g.....E......
0E40: F0 FF FF 7F 66 64 6F 31  02 80 1C 0B 80 52 06 80  ....fdo1.....R..
0E50: F8 FF FF 7F F8 FF FF 7F  7A 30 39 67 45 03 80 F0  ........z09gE...
0E60: FF FF 7F F0 FF FF 7F 62  6C 6F 66 02 80 03 01 10  .......blof.....
0E70: 01 80 46 00 01 87 0E 02  00 10 0C 80 00 87 0E 03  ..F.............
0E80: 01 10 02 80 01 87 0E 01  A7 0F 02 00 10 01 80 00  ................
0E90: 97 0F 24 11 80 0C 80 02  80 25 02 00 10 02 80 00  ..$......%......
0EA0: 84 0F 43 00 43 01 42 46  01 45 03 80 F0 FF FF 7F  ..C.C.BF.E......
0EB0: F0 FF FF 7F 66 64 6F 31  02 80 1C 04 80 38 05 80  ....fdo1.....8..
0EC0: 29 01 F0 FF FF 7F 29 45  06 80 F8 FF FF 7F F8 FF  ).....)E........
0ED0: FF 7F 7A 30 39 66 02 80  45 03 80 F0 FF FF 7F F0  ..z09f..E.......
0EE0: FF FF 7F 66 64 69 31 02  80 1C 07 80 52 06 80 F8  ...fdi1.....R...
0EF0: FF FF 7F F8 FF FF 7F 7A  30 39 66 4C 1C 08 80 45  .......z09fL...E
0F00: 03 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 02 80  ..........ovl1..
0F10: 45 03 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 02  E..........blon.
0F20: 80 45 09 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
0F30: 02 80 45 06 80 F8 FF FF  7F F8 FF FF 7F 7A 30 39  ..E..........z09
0F40: 67 02 80 1C 0A 80 45 03  80 F0 FF FF 7F F0 FF FF  g.....E.........
0F50: 7F 66 64 6F 31 02 80 1C  0B 80 52 06 80 F8 FF FF  .fdo1.....R.....
0F60: 7F F8 FF FF 7F 7A 30 39  67 45 03 80 F0 FF FF 7F  .....z09gE......
0F70: F0 FF FF 7F 62 6C 6F 66  02 80 03 01 10 13 80 46  ....blof.......F
0F80: 00 01 94 0F 02 00 10 0C  80 00 94 0F 03 01 10 02  ................
0F90: 80 01 94 0F 01 A7 0F 02  00 10 13 80 00 A7 0F 03  ................
0FA0: 01 10 02 80 01 A7 0F 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x0C89 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0C8B [0x24] CREATE_DIALOG(message_id=7085*, default_option=3*, option_flags=0*)
    → "Proceed onward? [Yes./Warp to the Solicitor./Warp to the Ponderer./Turn back.]"
  2: 0x0C92 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0C93 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0D7D
  4: 0x0C9B [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0C9D [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0C9F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0CA0 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0CA2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0CB3 [0x1C] WAIT(120* ticks)
 10: 0x0CB6 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x0CB9 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 12: 0x0CC0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 13: 0x0CD1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0CE2 [0x1C] WAIT(300* ticks)
 15: 0x0CE5 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 16: 0x0CF4 [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x0CF5 [0x1C] WAIT(90* ticks)
 18: 0x0CF8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0D09 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0D1A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0D2B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 22: 0x0D3C [0x1C] WAIT(180* ticks)
 23: 0x0D3F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x0D50 [0x1C] WAIT(60* ticks)
 25: 0x0D53 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 26: 0x0D62 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x0D73 [0x03] Work_Zone[1] = 1*
 28: 0x0D78 [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x0D7A [0x01] GOTO 0x0FA7
 30: 0x0D7D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0E8A
 31: 0x0D85 [0x24] CREATE_DIALOG(message_id=7088*, default_option=1*, option_flags=0*)
    → "Really warp to the Solicitor? [Yes./No.]"
 32: 0x0D8C [0x25] WAIT_DIALOG_SELECT()
 33: 0x0D8D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0E77
 34: 0x0D95 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x0D97 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x0D99 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 37: 0x0D9A [0x46] CAMERA_CONTROL: Disable user control
 38: 0x0D9C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x0DAD [0x1C] WAIT(120* ticks)
 40: 0x0DB0 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 41: 0x0DB3 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 42: 0x0DBA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 43: 0x0DCB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 44: 0x0DDC [0x1C] WAIT(300* ticks)
 45: 0x0DDF [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 46: 0x0DEE [0x4C] EventEntity->StatusEvent = 8 // Open door
 47: 0x0DEF [0x1C] WAIT(90* ticks)
 48: 0x0DF2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x0E03 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x0E14 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 51: 0x0E25 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 52: 0x0E36 [0x1C] WAIT(180* ticks)
 53: 0x0E39 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 54: 0x0E4A [0x1C] WAIT(60* ticks)
 55: 0x0E4D [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 56: 0x0E5C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x0E6D [0x03] Work_Zone[1] = 2*
 58: 0x0E72 [0x46] CAMERA_CONTROL: Restore default settings
 59: 0x0E74 [0x01] GOTO 0x0E87
 60: 0x0E77 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0E87
 61: 0x0E7F [0x03] Work_Zone[1] = 0*
 62: 0x0E84 [0x01] GOTO 0x0E87

SUBROUTINE_0E87:
 63: 0x0E87 [0x01] GOTO 0x0FA7
 64: 0x0E8A [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0F97
 65: 0x0E92 [0x24] CREATE_DIALOG(message_id=7089*, default_option=1*, option_flags=0*)
    → "Really warp to the Ponderer? [Yes./No.]"
 66: 0x0E99 [0x25] WAIT_DIALOG_SELECT()
 67: 0x0E9A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0F84
 68: 0x0EA2 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 69: 0x0EA4 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 70: 0x0EA6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 71: 0x0EA7 [0x46] CAMERA_CONTROL: Disable user control
 72: 0x0EA9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 73: 0x0EBA [0x1C] WAIT(120* ticks)
 74: 0x0EBD [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 75: 0x0EC0 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 76: 0x0EC7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 77: 0x0ED8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 78: 0x0EE9 [0x1C] WAIT(300* ticks)
 79: 0x0EEC [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 80: 0x0EFB [0x4C] EventEntity->StatusEvent = 8 // Open door
 81: 0x0EFC [0x1C] WAIT(90* ticks)
 82: 0x0EFF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 83: 0x0F10 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 84: 0x0F21 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 85: 0x0F32 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 86: 0x0F43 [0x1C] WAIT(180* ticks)
 87: 0x0F46 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 88: 0x0F57 [0x1C] WAIT(60* ticks)
 89: 0x0F5A [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 90: 0x0F69 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 91: 0x0F7A [0x03] Work_Zone[1] = 3*
 92: 0x0F7F [0x46] CAMERA_CONTROL: Restore default settings
 93: 0x0F81 [0x01] GOTO 0x0F94
 94: 0x0F84 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0F94
 95: 0x0F8C [0x03] Work_Zone[1] = 0*
 96: 0x0F91 [0x01] GOTO 0x0F94

SUBROUTINE_0F94:
 97: 0x0F94 [0x01] GOTO 0x0FA7
 98: 0x0F97 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0FA7
 99: 0x0F9F [0x03] Work_Zone[1] = 0*
100: 0x0FA4 [0x01] GOTO 0x0FA7

SUBROUTINE_0FA7:
101: 0x0FA7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
102: 0x0FA9 [0x21] END_EVENT
103: 0x0FAA [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0FAB     |
| Data Size    | 1071 bytes |
| Instructions | 138        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0FA0:                                   20 01 24 16 80              .$..
0FB0: 17 80 02 80 25 02 00 10  02 80 00 9F 10 43 00 43  ....%........C.C
0FC0: 01 42 46 01 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  .BF.E..........f
0FD0: 64 6F 31 02 80 1C 04 80  38 05 80 29 01 F0 FF FF  do1.....8..)....
0FE0: 7F 29 45 06 80 F8 FF FF  7F F8 FF FF 7F 7A 30 39  .)E..........z09
0FF0: 66 02 80 45 03 80 F0 FF  FF 7F F0 FF FF 7F 66 64  f..E..........fd
1000: 69 31 02 80 1C 07 80 52  06 80 F8 FF FF 7F F8 FF  i1.....R........
1010: FF 7F 7A 30 39 66 4C 1C  08 80 45 03 80 F0 FF FF  ..z09fL...E.....
1020: 7F F0 FF FF 7F 6F 76 6C  31 02 80 45 03 80 F0 FF  .....ovl1..E....
1030: FF 7F F0 FF FF 7F 62 6C  6F 6E 02 80 45 09 80 F0  ......blon..E...
1040: FF FF 7F F0 FF FF 7F 62  6C 6F 6E 02 80 45 06 80  .......blon..E..
1050: F8 FF FF 7F F8 FF FF 7F  7A 30 39 67 02 80 1C 0A  ........z09g....
1060: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
1070: 02 80 1C 0B 80 52 06 80  F8 FF FF 7F F8 FF FF 7F  .....R..........
1080: 7A 30 39 67 45 03 80 F0  FF FF 7F F0 FF FF 7F 62  z09gE..........b
1090: 6C 6F 66 02 80 03 01 10  0C 80 46 00 01 D6 13 02  lof.......F.....
10A0: 00 10 0C 80 00 AC 11 24  0D 80 0C 80 02 80 25 02  .......$......%.
10B0: 00 10 02 80 00 99 11 43  00 43 01 42 46 01 45 03  .......C.C.BF.E.
10C0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 02 80 1C  .........fdo1...
10D0: 04 80 38 05 80 29 01 F0  FF FF 7F 29 45 06 80 F8  ..8..).....)E...
10E0: FF FF 7F F8 FF FF 7F 7A  30 39 66 02 80 45 03 80  .......z09f..E..
10F0: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 02 80 1C 07  ........fdi1....
1100: 80 52 06 80 F8 FF FF 7F  F8 FF FF 7F 7A 30 39 66  .R..........z09f
1110: 4C 1C 08 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 6F  L...E..........o
1120: 76 6C 31 02 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  vl1..E..........
1130: 62 6C 6F 6E 02 80 45 09  80 F0 FF FF 7F F0 FF FF  blon..E.........
1140: 7F 62 6C 6F 6E 02 80 45  06 80 F8 FF FF 7F F8 FF  .blon..E........
1150: FF 7F 7A 30 39 67 02 80  1C 0A 80 45 03 80 F0 FF  ..z09g.....E....
1160: FF 7F F0 FF FF 7F 66 64  6F 31 02 80 1C 0B 80 52  ......fdo1.....R
1170: 06 80 F8 FF FF 7F F8 FF  FF 7F 7A 30 39 67 45 03  ..........z09gE.
1180: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 66 02 80 03  .........blof...
1190: 01 10 01 80 46 00 01 A9  11 02 00 10 0C 80 00 A9  ....F...........
11A0: 11 03 01 10 02 80 01 A9  11 01 D6 13 02 00 10 01  ................
11B0: 80 00 B9 12 24 0F 80 0C  80 02 80 25 02 00 10 02  ....$......%....
11C0: 80 00 A6 12 43 00 43 01  42 46 01 45 03 80 F0 FF  ....C.C.BF.E....
11D0: FF 7F F0 FF FF 7F 66 64  6F 31 02 80 1C 04 80 38  ......fdo1.....8
11E0: 05 80 29 01 F0 FF FF 7F  29 45 06 80 F8 FF FF 7F  ..).....)E......
11F0: F8 FF FF 7F 7A 30 39 66  02 80 45 03 80 F0 FF FF  ....z09f..E.....
1200: 7F F0 FF FF 7F 66 64 69  31 02 80 1C 07 80 52 06  .....fdi1.....R.
1210: 80 F8 FF FF 7F F8 FF FF  7F 7A 30 39 66 4C 1C 08  .........z09fL..
1220: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  .E..........ovl1
1230: 02 80 45 03 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
1240: 6E 02 80 45 09 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  n..E..........bl
1250: 6F 6E 02 80 45 06 80 F8  FF FF 7F F8 FF FF 7F 7A  on..E..........z
1260: 30 39 67 02 80 1C 0A 80  45 03 80 F0 FF FF 7F F0  09g.....E.......
1270: FF FF 7F 66 64 6F 31 02  80 1C 0B 80 52 06 80 F8  ...fdo1.....R...
1280: FF FF 7F F8 FF FF 7F 7A  30 39 67 45 03 80 F0 FF  .......z09gE....
1290: FF 7F F0 FF FF 7F 62 6C  6F 66 02 80 03 01 10 13  ......blof......
12A0: 80 46 00 01 B6 12 02 00  10 0C 80 00 B6 12 03 01  .F..............
12B0: 10 02 80 01 B6 12 01 D6  13 02 00 10 13 80 00 C6  ................
12C0: 13 24 11 80 0C 80 02 80  25 02 00 10 02 80 00 B3  .$......%.......
12D0: 13 43 00 43 01 42 46 01  45 03 80 F0 FF FF 7F F0  .C.C.BF.E.......
12E0: FF FF 7F 66 64 6F 31 02  80 1C 04 80 38 05 80 29  ...fdo1.....8..)
12F0: 01 F0 FF FF 7F 29 45 06  80 F8 FF FF 7F F8 FF FF  .....)E.........
1300: 7F 7A 30 39 66 02 80 45  03 80 F0 FF FF 7F F0 FF  .z09f..E........
1310: FF 7F 66 64 69 31 02 80  1C 07 80 52 06 80 F8 FF  ..fdi1.....R....
1320: FF 7F F8 FF FF 7F 7A 30  39 66 4C 1C 08 80 45 03  ......z09fL...E.
1330: 80 F0 FF FF 7F F0 FF FF  7F 6F 76 6C 31 02 80 45  .........ovl1..E
1340: 03 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 02 80  ..........blon..
1350: 45 09 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 02  E..........blon.
1360: 80 45 06 80 F8 FF FF 7F  F8 FF FF 7F 7A 30 39 67  .E..........z09g
1370: 02 80 1C 0A 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
1380: 66 64 6F 31 02 80 1C 0B  80 52 06 80 F8 FF FF 7F  fdo1.....R......
1390: F8 FF FF 7F 7A 30 39 67  45 03 80 F0 FF FF 7F F0  ....z09gE.......
13A0: FF FF 7F 62 6C 6F 66 02  80 03 01 10 17 80 46 00  ...blof.......F.
13B0: 01 C3 13 02 00 10 0C 80  00 C3 13 03 01 10 02 80  ................
13C0: 01 C3 13 01 D6 13 02 00  10 17 80 00 D6 13 03 01  ................
13D0: 10 02 80 01 D6 13 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x0FAB [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0FAD [0x24] CREATE_DIALOG(message_id=7086*, default_option=4*, option_flags=0*)
    → "Proceed onward? [Yes./Warp to the Propagator./Warp to the Solicitor./Warp to the Ponderer./Turn back.]"
  2: 0x0FB4 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0FB5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x109F
  4: 0x0FBD [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0FBF [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0FC1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0FC2 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0FC4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0FD5 [0x1C] WAIT(120* ticks)
 10: 0x0FD8 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x0FDB [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 12: 0x0FE2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 13: 0x0FF3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x1004 [0x1C] WAIT(300* ticks)
 15: 0x1007 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 16: 0x1016 [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x1017 [0x1C] WAIT(90* ticks)
 18: 0x101A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x102B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x103C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x104D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 22: 0x105E [0x1C] WAIT(180* ticks)
 23: 0x1061 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x1072 [0x1C] WAIT(60* ticks)
 25: 0x1075 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 26: 0x1084 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x1095 [0x03] Work_Zone[1] = 1*
 28: 0x109A [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x109C [0x01] GOTO 0x13D6
 30: 0x109F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x11AC
 31: 0x10A7 [0x24] CREATE_DIALOG(message_id=7087*, default_option=1*, option_flags=0*)
    → "Really warp to the Propagator? [Yes./No.]"
 32: 0x10AE [0x25] WAIT_DIALOG_SELECT()
 33: 0x10AF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x1199
 34: 0x10B7 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x10B9 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x10BB [0x42] SET_CLI_EVENT_CANCEL_DATA()
 37: 0x10BC [0x46] CAMERA_CONTROL: Disable user control
 38: 0x10BE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x10CF [0x1C] WAIT(120* ticks)
 40: 0x10D2 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 41: 0x10D5 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 42: 0x10DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 43: 0x10ED [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 44: 0x10FE [0x1C] WAIT(300* ticks)
 45: 0x1101 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 46: 0x1110 [0x4C] EventEntity->StatusEvent = 8 // Open door
 47: 0x1111 [0x1C] WAIT(90* ticks)
 48: 0x1114 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x1125 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x1136 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 51: 0x1147 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 52: 0x1158 [0x1C] WAIT(180* ticks)
 53: 0x115B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 54: 0x116C [0x1C] WAIT(60* ticks)
 55: 0x116F [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 56: 0x117E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x118F [0x03] Work_Zone[1] = 2*
 58: 0x1194 [0x46] CAMERA_CONTROL: Restore default settings
 59: 0x1196 [0x01] GOTO 0x11A9
 60: 0x1199 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x11A9
 61: 0x11A1 [0x03] Work_Zone[1] = 0*
 62: 0x11A6 [0x01] GOTO 0x11A9

SUBROUTINE_11A9:
 63: 0x11A9 [0x01] GOTO 0x13D6
 64: 0x11AC [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x12B9
 65: 0x11B4 [0x24] CREATE_DIALOG(message_id=7088*, default_option=1*, option_flags=0*)
    → "Really warp to the Solicitor? [Yes./No.]"
 66: 0x11BB [0x25] WAIT_DIALOG_SELECT()
 67: 0x11BC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x12A6
 68: 0x11C4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 69: 0x11C6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 70: 0x11C8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 71: 0x11C9 [0x46] CAMERA_CONTROL: Disable user control
 72: 0x11CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 73: 0x11DC [0x1C] WAIT(120* ticks)
 74: 0x11DF [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 75: 0x11E2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 76: 0x11E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 77: 0x11FA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 78: 0x120B [0x1C] WAIT(300* ticks)
 79: 0x120E [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 80: 0x121D [0x4C] EventEntity->StatusEvent = 8 // Open door
 81: 0x121E [0x1C] WAIT(90* ticks)
 82: 0x1221 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 83: 0x1232 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 84: 0x1243 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 85: 0x1254 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 86: 0x1265 [0x1C] WAIT(180* ticks)
 87: 0x1268 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 88: 0x1279 [0x1C] WAIT(60* ticks)
 89: 0x127C [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 90: 0x128B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 91: 0x129C [0x03] Work_Zone[1] = 3*
 92: 0x12A1 [0x46] CAMERA_CONTROL: Restore default settings
 93: 0x12A3 [0x01] GOTO 0x12B6
 94: 0x12A6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x12B6
 95: 0x12AE [0x03] Work_Zone[1] = 0*
 96: 0x12B3 [0x01] GOTO 0x12B6

SUBROUTINE_12B6:
 97: 0x12B6 [0x01] GOTO 0x13D6
 98: 0x12B9 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x13C6
 99: 0x12C1 [0x24] CREATE_DIALOG(message_id=7089*, default_option=1*, option_flags=0*)
    → "Really warp to the Ponderer? [Yes./No.]"
100: 0x12C8 [0x25] WAIT_DIALOG_SELECT()
101: 0x12C9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x13B3
102: 0x12D1 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
103: 0x12D3 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
104: 0x12D5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
105: 0x12D6 [0x46] CAMERA_CONTROL: Disable user control
106: 0x12D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
107: 0x12E9 [0x1C] WAIT(120* ticks)
108: 0x12EC [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
109: 0x12EF [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
110: 0x12F6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
111: 0x1307 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
112: 0x1318 [0x1C] WAIT(300* ticks)
113: 0x131B [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
114: 0x132A [0x4C] EventEntity->StatusEvent = 8 // Open door
115: 0x132B [0x1C] WAIT(90* ticks)
116: 0x132E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
117: 0x133F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
118: 0x1350 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
119: 0x1361 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
120: 0x1372 [0x1C] WAIT(180* ticks)
121: 0x1375 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
122: 0x1386 [0x1C] WAIT(60* ticks)
123: 0x1389 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
124: 0x1398 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
125: 0x13A9 [0x03] Work_Zone[1] = 4*
126: 0x13AE [0x46] CAMERA_CONTROL: Restore default settings
127: 0x13B0 [0x01] GOTO 0x13C3
128: 0x13B3 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x13C3
129: 0x13BB [0x03] Work_Zone[1] = 0*
130: 0x13C0 [0x01] GOTO 0x13C3

SUBROUTINE_13C3:
131: 0x13C3 [0x01] GOTO 0x13D6
132: 0x13C6 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x13D6
133: 0x13CE [0x03] Work_Zone[1] = 0*
134: 0x13D3 [0x01] GOTO 0x13D6

SUBROUTINE_13D6:
135: 0x13D6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
136: 0x13D8 [0x21] END_EVENT
137: 0x13D9 [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x13DA    |
| Data Size    | 264 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
13D0:                                20 01 24 18 80 0C             .$...
13E0: 80 02 80 25 02 00 10 02  80 00 CE 14 43 00 43 01  ...%........C.C.
13F0: 42 46 01 45 03 80 F0 FF  FF 7F F0 FF FF 7F 66 64  BF.E..........fd
1400: 6F 31 02 80 1C 04 80 38  05 80 29 01 F0 FF FF 7F  o1.....8..).....
1410: 29 45 06 80 F8 FF FF 7F  F8 FF FF 7F 7A 30 39 66  )E..........z09f
1420: 02 80 45 03 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
1430: 31 02 80 1C 07 80 52 06  80 F8 FF FF 7F F8 FF FF  1.....R.........
1440: 7F 7A 30 39 66 4C 1C 08  80 45 03 80 F0 FF FF 7F  .z09fL...E......
1450: F0 FF FF 7F 6F 76 6C 31  02 80 45 03 80 F0 FF FF  ....ovl1..E.....
1460: 7F F0 FF FF 7F 62 6C 6F  6E 02 80 45 09 80 F0 FF  .....blon..E....
1470: FF 7F F0 FF FF 7F 62 6C  6F 6E 02 80 45 06 80 F8  ......blon..E...
1480: FF FF 7F F8 FF FF 7F 7A  30 39 67 02 80 1C 0A 80  .......z09g.....
1490: 45 03 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 02  E..........fdo1.
14A0: 80 1C 0B 80 52 06 80 F8  FF FF 7F F8 FF FF 7F 7A  ....R..........z
14B0: 30 39 67 45 03 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  09gE..........bl
14C0: 6F 66 02 80 03 01 10 0C  80 46 00 01 DE 14 02 00  of.......F......
14D0: 10 0C 80 00 DE 14 03 01  10 02 80 01 DE 14 20 00  .............. .
14E0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x13DA [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x13DC [0x24] CREATE_DIALOG(message_id=7074*, default_option=1*, option_flags=0*)
    → "Proceed onward? [Yes./No.]"
  2: 0x13E3 [0x25] WAIT_DIALOG_SELECT()
  3: 0x13E4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x14CE
  4: 0x13EC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x13EE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x13F0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x13F1 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x13F3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x1404 [0x1C] WAIT(120* ticks)
 10: 0x1407 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x140A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x29)
 12: 0x1411 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 13: 0x1422 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x1433 [0x1C] WAIT(300* ticks)
 15: 0x1436 [0x52] END_LOAD_SCHEDULER: End scheduler "z09f" with entities [EventEntity, EventEntity], work=160*
 16: 0x1445 [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x1446 [0x1C] WAIT(90* ticks)
 18: 0x1449 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x145A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x146B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x147C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z09g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 22: 0x148D [0x1C] WAIT(180* ticks)
 23: 0x1490 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x14A1 [0x1C] WAIT(60* ticks)
 25: 0x14A4 [0x52] END_LOAD_SCHEDULER: End scheduler "z09g" with entities [EventEntity, EventEntity], work=160*
 26: 0x14B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x14C4 [0x03] Work_Zone[1] = 1*
 28: 0x14C9 [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x14CB [0x01] GOTO 0x14DE
 30: 0x14CE [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x14DE
 31: 0x14D6 [0x03] Work_Zone[1] = 0*
 32: 0x14DB [0x01] GOTO 0x14DE

SUBROUTINE_14DE:
 33: 0x14DE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 34: 0x14E0 [0x21] END_EVENT
 35: 0x14E1 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x14E2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
14E0:       00                                            .             
```

#### Opcodes

```
  0: 0x14E2 [0x00] END_REQSTACK()
```
