# 17428911 - Granite Door

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 400 bytes                     |
| Total Events     | 4                             |
| References Count | 8                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [23](#event-23)       | 0x0001       |      1 |              1 |
| [25](#event-25)       | 0x0002       |    149 |             23 |
| [26](#event-26)       | 0x0097       |    183 |             32 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0012      |          18 |
|       4 | 0x003B      |          59 |
|       5 | 0x0078      |         120 |
|       6 | 0x1CE1      |        7393 |
|       7 | 0x0001      |           1 |

## String References

- **7393**: Leave this room? [Yes./No.]

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

### Event 23

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

### Event 25

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 149 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 46 01 45  00 80 F0 FF FF 7F F0 FF     .BF.E........
0010: FF 7F 66 64 6F 31 01 80  1C 02 80 38 03 80 29 0B  ..fdo1.....8..).
0020: F0 FF FF 7F 0A 29 0B F0  FF FF 7F 09 45 04 80 F8  .....)......E...
0030: FF FF 7F F8 FF FF 7F 73  30 33 34 01 80 45 00 80  .......s034..E..
0040: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 01 80 4C 1C  ........fdi1..L.
0050: 05 80 27 0B F0 FF FF 7F  0B 1C 05 80 45 00 80 F0  ..'.........E...
0060: FF FF 7F F0 FF FF 7F 66  64 6F 31 01 80 4D 1C 05  .......fdo1..M..
0070: 80 52 04 80 F8 FF FF 7F  F8 FF FF 7F 73 30 33 34  .R..........s034
0080: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
0090: 80 46 00 20 00 21 00                              .F. .!.         
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0007 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0018 [0x1C] WAIT(60* ticks)
  5: 0x001B [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
  6: 0x001E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0A)
  7: 0x0025 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x09)
  8: 0x002C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s034" with entities [EventEntity, EventEntity], work=[59*, 0*]
  9: 0x003D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x004E [0x4C] EventEntity->StatusEvent = 8 // Open door
 11: 0x004F [0x1C] WAIT(120* ticks)
 12: 0x0052 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0B)
 13: 0x0059 [0x1C] WAIT(120* ticks)
 14: 0x005C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x006D [0x4D] EventEntity->StatusEvent = 9 // Close door
 16: 0x006E [0x1C] WAIT(120* ticks)
 17: 0x0071 [0x52] END_LOAD_SCHEDULER: End scheduler "s034" with entities [EventEntity, EventEntity], work=59*
 18: 0x0080 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0091 [0x46] CAMERA_CONTROL: Restore default settings
 20: 0x0093 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 21: 0x0095 [0x21] END_EVENT
 22: 0x0096 [0x00] END_REQSTACK()
```

### Event 26

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0097    |
| Data Size    | 183 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      20  01 42 24 06 80 07 80 01          .B$.....
00A0: 80 25 02 00 10 01 80 00  AD 00 01 BC 00 02 00 10  .%..............
00B0: 07 80 00 BC 00 20 00 21  00 01 BC 00 46 01 45 00  ..... .!....F.E.
00C0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 1C  .........fdo1...
00D0: 02 80 38 03 80 29 0B F0  FF FF 7F 0D 29 0B F0 FF  ..8..)......)...
00E0: FF 7F 0C 45 04 80 F8 FF  FF 7F F8 FF FF 7F 73 30  ...E..........s0
00F0: 33 34 01 80 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  34..E..........f
0100: 64 69 31 01 80 4C 1C 05  80 27 0B F0 FF FF 7F 0E  di1..L...'......
0110: 1C 05 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0120: 6F 31 01 80 4D 1C 05 80  52 04 80 F8 FF FF 7F F8  o1..M...R.......
0130: FF FF 7F 73 30 33 34 45  00 80 F0 FF FF 7F F0 FF  ...s034E........
0140: FF 7F 66 64 69 31 01 80  46 00 20 00 21 00        ..fdi1..F. .!.  
```

#### Opcodes

```
  0: 0x0097 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0099 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x009A [0x24] CREATE_DIALOG(message_id=7393*, default_option=1*, option_flags=0*)
    → "Leave this room? [Yes./No.]"
  3: 0x00A1 [0x25] WAIT_DIALOG_SELECT()
  4: 0x00A2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00AD
  5: 0x00AA [0x01] GOTO 0x00BC
  6: 0x00AD [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00BC
  7: 0x00B5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00B7 [0x21] END_EVENT
  9: 0x00B8 [0x00] END_REQSTACK()

SUBROUTINE_00BC:
 10: 0x00BC [0x46] CAMERA_CONTROL: Disable user control
 11: 0x00BE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x00CF [0x1C] WAIT(60* ticks)
 13: 0x00D2 [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
 14: 0x00D5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0D)
 15: 0x00DC [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0C)
 16: 0x00E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s034" with entities [EventEntity, EventEntity], work=[59*, 0*]
 17: 0x00F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0105 [0x4C] EventEntity->StatusEvent = 8 // Open door
 19: 0x0106 [0x1C] WAIT(120* ticks)
 20: 0x0109 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0E)
 21: 0x0110 [0x1C] WAIT(120* ticks)
 22: 0x0113 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x0124 [0x4D] EventEntity->StatusEvent = 9 // Close door
 24: 0x0125 [0x1C] WAIT(120* ticks)
 25: 0x0128 [0x52] END_LOAD_SCHEDULER: End scheduler "s034" with entities [EventEntity, EventEntity], work=59*
 26: 0x0137 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x0148 [0x46] CAMERA_CONTROL: Restore default settings
 28: 0x014A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x014C [0x21] END_EVENT
 30: 0x014D [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00B9 [0x01] GOTO 0x00BC
```
