# 16834573 - Large Apparatus

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Hall of Transference (ID: 14) |
| Block Size       | 520 bytes                     |
| Total Events     | 4                             |
| References Count | 15                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [126](#event-126)     | 0x0001       |    183 |             24 |
| [127](#event-127)     | 0x00B8       |      1 |              1 |
| [128](#event-128)     | 0x00B9       |    242 |             42 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0078      |         120 |
|       3 | 0x0013      |          19 |
|       4 | 0x005E      |          94 |
|       5 | 0x003C      |          60 |
|       6 | 0x00FA      |         250 |
|       7 | 0x04B0      |        1200 |
|       8 | 0x1C82      |        7298 |
|       9 | 0x1C83      |        7299 |
|      10 | 0x1C84      |        7300 |
|      11 | 0x0001      |           1 |
|      12 | 0x40000000  |  1073741824 |
|      13 | 0x1C85      |        7301 |
|      14 | 0x0384      |         900 |

## String References

- **7298**: By sealing off a portion of your memory, your destiny within this realm of Promyvion can be altered.
- **7299**: This will allow you to return to the entrance of the crag, having forgotten all events regarding this place.
- **7300**: Seal off your memories? [Yes./No.]
- **7301**: Are you sure? [Absolutely./No.]

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

### Event 126

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 183 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 46 01 45 00  80 F0 FF FF 7F F0 FF FF    .BF.E.........
0010: 7F 66 64 6F 31 01 80 1C  02 80 38 03 80 29 01 F0  .fdo1.....8..)..
0020: FF FF 7F 09 45 04 80 F8  FF FF 7F F8 FF FF 7F 7A  ....E..........z
0030: 31 34 61 01 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  14a..E..........
0040: 66 64 69 31 01 80 1C 05  80 2D F8 FF FF 7F F8 FF  fdi1.....-......
0050: FF 7F 32 73 77 31 1C 06  80 52 04 80 F8 FF FF 7F  ..2sw1...R......
0060: F8 FF FF 7F 7A 31 34 61  45 00 80 F0 FF FF 7F F0  ....z14aE.......
0070: FF FF 7F 6F 76 6C 31 01  80 45 04 80 F8 FF FF 7F  ...ovl1..E......
0080: F8 FF FF 7F 7A 31 34 62  01 80 1C 07 80 45 00 80  ....z14b.....E..
0090: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 05  ........fdo1....
00A0: 80 52 04 80 F8 FF FF 7F  F8 FF FF 7F 7A 31 34 62  .R..........z14b
00B0: 46 00 1C 05 80 30 21 00                           F....0!.        
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0017 [0x1C] WAIT(120* ticks)
  5: 0x001A [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x001D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
  7: 0x0024 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14a" with entities [EventEntity, EventEntity], work=[94*, 0*]
  8: 0x0035 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0046 [0x1C] WAIT(60* ticks)
 10: 0x0049 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2sw1" with entities [EventEntity, EventEntity]
 11: 0x0056 [0x1C] WAIT(250* ticks)
 12: 0x0059 [0x52] END_LOAD_SCHEDULER: End scheduler "z14a" with entities [EventEntity, EventEntity], work=94*
 13: 0x0068 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0079 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14b" with entities [EventEntity, EventEntity], work=[94*, 0*]
 15: 0x008A [0x1C] WAIT(1200* ticks)
 16: 0x008D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x009E [0x1C] WAIT(60* ticks)
 18: 0x00A1 [0x52] END_LOAD_SCHEDULER: End scheduler "z14b" with entities [EventEntity, EventEntity], work=94*
 19: 0x00B0 [0x46] CAMERA_CONTROL: Restore default settings
 20: 0x00B2 [0x1C] WAIT(60* ticks)
 21: 0x00B5 [0x30] SET_UCOFF_CONTINUE_ZERO()
 22: 0x00B6 [0x21] END_EVENT
 23: 0x00B7 [0x00] END_REQSTACK()
```

### Event 127

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          00                               .       
```

#### Opcodes

```
  0: 0x00B8 [0x00] END_REQSTACK()
```

### Event 128

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00B9    |
| Data Size    | 242 bytes |
| Instructions | 40        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             20 01 48 08 80 23 48            .H..#H
00C0: 09 80 23 24 0A 80 0B 80  01 80 25 02 00 10 0B 80  ..#$......%.....
00D0: 00 DD 00 03 01 10 0C 80  21 00 01 DD 00 24 0D 80  ........!....$..
00E0: 0B 80 01 80 25 02 00 10  0B 80 00 F7 00 03 01 10  ....%...........
00F0: 0C 80 21 00 01 F7 00 42  46 01 43 00 43 01 45 00  ..!....BF.C.C.E.
0100: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 1C  .........fdo1...
0110: 02 80 38 03 80 29 01 F0  FF FF 7F 09 45 04 80 F8  ..8..)......E...
0120: FF FF 7F F8 FF FF 7F 7A  31 34 61 01 80 45 00 80  .......z14a..E..
0130: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 01 80 1C 05  ........fdi1....
0140: 80 2D F8 FF FF 7F F8 FF  FF 7F 32 73 77 32 1C 06  .-........2sw2..
0150: 80 52 04 80 F8 FF FF 7F  F8 FF FF 7F 7A 31 34 61  .R..........z14a
0160: 45 00 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 01  E..........ovl1.
0170: 80 45 04 80 F8 FF FF 7F  F8 FF FF 7F 7A 31 34 62  .E..........z14b
0180: 01 80 1C 0E 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0190: 66 64 6F 31 01 80 1C 05  80 52 04 80 F8 FF FF 7F  fdo1.....R......
01A0: F8 FF FF 7F 7A 31 34 62  30 21 00                 ....z14b0!.     
```

#### Opcodes

```
  0: 0x00B9 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00BB [0x48] [System] [7298*]:
    → "By sealing off a portion of your memory, your destiny within this realm of Promyvion can be altered."
  2: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00BF [0x48] [System] [7299*]:
    → "This will allow you to return to the entrance of the crag, having forgotten all events regarding this place."
  4: 0x00C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00C3 [0x24] CREATE_DIALOG(message_id=7300*, default_option=1*, option_flags=0*)
    → "Seal off your memories? [Yes./No.]"
  6: 0x00CA [0x25] WAIT_DIALOG_SELECT()
  7: 0x00CB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00DD
  8: 0x00D3 [0x03] Work_Zone[1] = 1073741824*
  9: 0x00D8 [0x21] END_EVENT
 10: 0x00D9 [0x00] END_REQSTACK()

SUBROUTINE_00DD:
 11: 0x00DD [0x24] CREATE_DIALOG(message_id=7301*, default_option=1*, option_flags=0*)
    → "Are you sure? [Absolutely./No.]"
 12: 0x00E4 [0x25] WAIT_DIALOG_SELECT()
 13: 0x00E5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00F7
 14: 0x00ED [0x03] Work_Zone[1] = 1073741824*
 15: 0x00F2 [0x21] END_EVENT
 16: 0x00F3 [0x00] END_REQSTACK()

SUBROUTINE_00F7:
 17: 0x00F7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 18: 0x00F8 [0x46] CAMERA_CONTROL: Disable user control
 19: 0x00FA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 20: 0x00FC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 21: 0x00FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x010F [0x1C] WAIT(120* ticks)
 23: 0x0112 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 24: 0x0115 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
 25: 0x011C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14a" with entities [EventEntity, EventEntity], work=[94*, 0*]
 26: 0x012D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x013E [0x1C] WAIT(60* ticks)
 28: 0x0141 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2sw2" with entities [EventEntity, EventEntity]
 29: 0x014E [0x1C] WAIT(250* ticks)
 30: 0x0151 [0x52] END_LOAD_SCHEDULER: End scheduler "z14a" with entities [EventEntity, EventEntity], work=94*
 31: 0x0160 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x0171 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14b" with entities [EventEntity, EventEntity], work=[94*, 0*]
 33: 0x0182 [0x1C] WAIT(900* ticks)
 34: 0x0185 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 35: 0x0196 [0x1C] WAIT(60* ticks)
 36: 0x0199 [0x52] END_LOAD_SCHEDULER: End scheduler "z14b" with entities [EventEntity, EventEntity], work=94*
 37: 0x01A8 [0x30] SET_UCOFF_CONTINUE_ZERO()
 38: 0x01A9 [0x21] END_EVENT
 39: 0x01AA [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00DA [0x01] GOTO 0x00DD
# Dead code (unreachable instructions):
     0x00F4 [0x01] GOTO 0x00F7
```
