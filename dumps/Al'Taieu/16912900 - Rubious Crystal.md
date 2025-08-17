# 16912900 - Rubious Crystal

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al'Taieu (ID: 33) |
| Block Size       | 220 bytes         |
| Total Events     | 4                 |
| References Count | 9                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [163](#event-163)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      2 |              2 |
| [101](#event-101)        | 0x0004       |    145 |             26 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0013      |          19 |
|       4 | 0x00A0      |         160 |
|       5 | 0x0078      |         120 |
|       6 | 0x0172      |         370 |
|       7 | 0x0514      |        1300 |
|       8 | 0x00B4      |         180 |

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

### Event 101

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0004    |
| Data Size    | 145 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             20 01 43 00  43 01 46 01 42 45 00 80       .C.C.F.BE..
0010: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 02  ........fdo1....
0020: 80 38 03 80 45 04 80 F0  FF FF 7F F0 FF FF 7F 73  .8..E..........s
0030: 74 77 31 01 80 29 01 F0  FF FF 7F 0F 45 00 80 F0  tw1..)......E...
0040: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 1C 05 80  .......fdi1.....
0050: 2D F8 FF FF 7F F8 FF FF  7F 31 74 6F 77 1C 06 80  -........1tow...
0060: 4C 1C 07 80 4D 1C 08 80  45 00 80 F0 FF FF 7F F0  L...M...E.......
0070: FF FF 7F 66 64 6F 31 01  80 1C 02 80 46 00 45 00  ...fdo1.....F.E.
0080: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 01 80 46  .........fdi1..F
0090: 00 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0004 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0006 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x0008 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x000A [0x46] CAMERA_CONTROL: Disable user control
  4: 0x000C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x000D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x001E [0x1C] WAIT(60* ticks)
  7: 0x0021 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0024 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "stw1" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
  9: 0x0035 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0F)
 10: 0x003C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x004D [0x1C] WAIT(120* ticks)
 12: 0x0050 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1tow" with entities [EventEntity, EventEntity]
 13: 0x005D [0x1C] WAIT(370* ticks)
 14: 0x0060 [0x4C] EventEntity->StatusEvent = 8 // Open door
 15: 0x0061 [0x1C] WAIT(1300* ticks)
 16: 0x0064 [0x4D] EventEntity->StatusEvent = 9 // Close door
 17: 0x0065 [0x1C] WAIT(180* ticks)
 18: 0x0068 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0079 [0x1C] WAIT(60* ticks)
 20: 0x007C [0x46] CAMERA_CONTROL: Restore default settings
 21: 0x007E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x008F [0x46] CAMERA_CONTROL: Restore default settings
 23: 0x0091 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 24: 0x0093 [0x21] END_EVENT
 25: 0x0094 [0x00] END_REQSTACK()
```
