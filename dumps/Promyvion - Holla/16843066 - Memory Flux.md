# 16843066 - Memory Flux

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Promyvion - Holla (ID: 16) |
| Block Size       | 240 bytes                  |
| Total Events     | 2                          |
| References Count | 7                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [11](#event-11)       | 0x0001       |    187 |             29 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x00B4      |         180 |
|       4 | 0x012C      |         300 |
|       5 | 0x0258      |         600 |
|       6 | 0x1C43      |        7235 |

## String References

- **7235**: DEBUG:$3{$3^$3$2p$317F$P10i]\\7B

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

### Event 11

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 187 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 46 01 42 45 00  80 F0 FF FF 7F F0 FF FF    .F.BE.........
0010: 7F 66 64 6F 31 01 80 1C  02 80 45 00 80 F0 FF FF  .fdo1.....E.....
0020: 7F F0 FF FF 7F 66 64 69  31 01 80 1C 02 80 2D F8  .....fdi1.....-.
0030: FF FF 7F F8 FF FF 7F 73  31 34 31 2D F8 FF FF 7F  .......s141-....
0040: F8 FF FF 7F 73 74 62 31  1C 03 80 2D F8 FF FF 7F  ....stb1...-....
0050: F8 FF FF 7F 73 74 62 32  1C 04 80 2D F8 FF FF 7F  ....stb2...-....
0060: F8 FF FF 7F 73 74 62 33  54 F8 FF FF 7F F8 FF FF  ....stb3T.......
0070: 7F 73 74 62 33 1C 05 80  4C 1D 06 80 23 45 00 80  .stb3...L...#E..
0080: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 03  ........fdo1....
0090: 80 4D 2D F8 FF FF 7F F8  FF FF 7F 73 74 62 34 1C  .M-........stb4.
00A0: 02 80 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
00B0: 31 01 80 1C 02 80 46 00  20 00 21 00              1.....F. .!.    
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0005 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0017 [0x1C] WAIT(60* ticks)
  5: 0x001A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x002B [0x1C] WAIT(60* ticks)
  7: 0x002E [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s141" with entities [EventEntity, EventEntity]
  8: 0x003B [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "stb1" with entities [EventEntity, EventEntity]
  9: 0x0048 [0x1C] WAIT(180* ticks)
 10: 0x004B [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "stb2" with entities [EventEntity, EventEntity]
 11: 0x0058 [0x1C] WAIT(300* ticks)
 12: 0x005B [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "stb3" with entities [EventEntity, EventEntity]
 13: 0x0068 [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler "stb3" with entities [EventEntity, EventEntity]
 14: 0x0075 [0x1C] WAIT(600* ticks)
 15: 0x0078 [0x4C] EventEntity->StatusEvent = 8 // Open door
 16: 0x0079 [0x1D] PRINT_EVENT_MESSAGE(message_id=7235*)
    → "DEBUG:$3{$3^$3$2p$317F$P10i]\7B"
 17: 0x007C [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x007D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x008E [0x1C] WAIT(180* ticks)
 20: 0x0091 [0x4D] EventEntity->StatusEvent = 9 // Close door
 21: 0x0092 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "stb4" with entities [EventEntity, EventEntity]
 22: 0x009F [0x1C] WAIT(60* ticks)
 23: 0x00A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x00B3 [0x1C] WAIT(60* ticks)
 25: 0x00B6 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x00B8 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 27: 0x00BA [0x21] END_EVENT
 28: 0x00BB [0x00] END_REQSTACK()
```
