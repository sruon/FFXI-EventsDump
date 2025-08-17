# 16912899 - Crystalline Field

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al'Taieu (ID: 33) |
| Block Size       | 340 bytes         |
| Total Events     | 4                 |
| References Count | 10                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [163](#event-163)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      2 |              2 |
| [100](#event-100)        | 0x0004       |    264 |             38 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C9F      |        7327 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0013      |          19 |
|       6 | 0x00A0      |         160 |
|       7 | 0x00F0      |         240 |
|       8 | 0x0190      |         400 |
|       9 | 0x00B4      |         180 |

## String References

- **7327**: Pass through the gate? [Yes./No.]

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

### Event 163

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

### Event 100

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0004    |
| Data Size    | 264 bytes |
| Instructions | 38        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             20 01 24 00  80 01 80 02 80 25 02 00       .$......%..
0010: 10 02 80 00 F8 00 43 00  43 01 46 01 42 45 03 80  ......C.C.F.BE..
0020: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 02 80 1C 04  ........fdo1....
0030: 80 38 05 80 45 06 80 F0  FF FF 7F F0 FF FF 7F 67  .8..E..........g
0040: 61 74 30 02 80 29 01 F0  FF FF 7F 0D 45 03 80 F0  at0..)......E...
0050: FF FF 7F F0 FF FF 7F 66  64 69 31 02 80 1C 07 80  .......fdi1.....
0060: 45 03 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 02  E..........ovl1.
0070: 80 45 06 80 F0 FF FF 7F  F0 FF FF 7F 67 61 74 31  .E..........gat1
0080: 02 80 2D F8 FF FF 7F F8  FF FF 7F 6F 6F 66 66 1C  ..-........ooff.
0090: 08 80 4C 27 01 F0 FF FF  7F 0E 45 03 80 F0 FF FF  ..L'......E.....
00A0: 7F F0 FF FF 7F 6F 76 6C  31 02 80 45 06 80 F0 FF  .....ovl1..E....
00B0: FF 7F F0 FF FF 7F 67 61  74 32 02 80 1C 09 80 2D  ......gat2.....-
00C0: F8 FF FF 7F F8 FF FF 7F  6F 6E 6F 6E 54 F8 FF FF  ........ononT...
00D0: 7F F8 FF FF 7F 6F 6E 6F  6E 4D 45 03 80 F0 FF FF  .....ononME.....
00E0: 7F F0 FF FF 7F 66 64 6F  31 02 80 1C 04 80 03 01  .....fdo1.......
00F0: 10 01 80 46 00 01 08 01  02 00 10 01 80 00 08 01  ...F............
0100: 03 01 10 02 80 01 08 01  20 00 21 00              ........ .!.    
```

#### Opcodes

```
  0: 0x0004 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0006 [0x24] CREATE_DIALOG(message_id=7327*, default_option=1*, option_flags=0*)
    → "Pass through the gate? [Yes./No.]"
  2: 0x000D [0x25] WAIT_DIALOG_SELECT()
  3: 0x000E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F8
  4: 0x0016 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0018 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x001A [0x46] CAMERA_CONTROL: Disable user control
  7: 0x001C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x001D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x002E [0x1C] WAIT(60* ticks)
 10: 0x0031 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x0034 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "gat0" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 12: 0x0045 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0D)
 13: 0x004C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x005D [0x1C] WAIT(240* ticks)
 15: 0x0060 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0071 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "gat1" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 17: 0x0082 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "ooff" with entities [EventEntity, EventEntity]
 18: 0x008F [0x1C] WAIT(400* ticks)
 19: 0x0092 [0x4C] EventEntity->StatusEvent = 8 // Open door
 20: 0x0093 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x0E)
 21: 0x009A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x00AB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "gat2" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 23: 0x00BC [0x1C] WAIT(180* ticks)
 24: 0x00BF [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "onon" with entities [EventEntity, EventEntity]
 25: 0x00CC [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler "onon" with entities [EventEntity, EventEntity]
 26: 0x00D9 [0x4D] EventEntity->StatusEvent = 9 // Close door
 27: 0x00DA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x00EB [0x1C] WAIT(60* ticks)
 29: 0x00EE [0x03] Work_Zone[1] = 1*
 30: 0x00F3 [0x46] CAMERA_CONTROL: Restore default settings
 31: 0x00F5 [0x01] GOTO 0x0108
 32: 0x00F8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0108
 33: 0x0100 [0x03] Work_Zone[1] = 0*
 34: 0x0105 [0x01] GOTO 0x0108

SUBROUTINE_0108:
 35: 0x0108 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 36: 0x010A [0x21] END_EVENT
 37: 0x010B [0x00] END_REQSTACK()
```
