# 16867731 - Memory Flux

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Promyvion - Vahzl (ID: 22) |
| Block Size       | 240 bytes                  |
| Total Events     | 3                          |
| References Count | 6                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [53](#event-53)       | 0x0001       |      1 |              1 |
| [12](#event-12)       | 0x0002       |    184 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x00B4      |         180 |
|       4 | 0x012C      |         300 |
|       5 | 0x1C3F      |        7231 |

## String References

- **7231**: DEBUG:$3{$3^$3$2p$317F$P10i]\\7B

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

### Event 53

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

### Event 12

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 184 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 46 01 42 45  00 80 F0 FF FF 7F F0 FF     .F.BE........
0010: FF 7F 66 64 6F 31 01 80  1C 02 80 45 00 80 F0 FF  ..fdo1.....E....
0020: FF 7F F0 FF FF 7F 66 64  69 31 01 80 1C 02 80 2D  ......fdi1.....-
0030: F8 FF FF 7F F8 FF FF 7F  73 31 34 31 2D F8 FF FF  ........s141-...
0040: 7F F8 FF FF 7F 73 74 61  31 1C 03 80 2D F8 FF FF  .....sta1...-...
0050: 7F F8 FF FF 7F 73 74 61  32 1C 04 80 2D F8 FF FF  .....sta2...-...
0060: 7F F8 FF FF 7F 73 74 61  33 54 F8 FF FF 7F F8 FF  .....sta3T......
0070: FF 7F 73 74 61 33 4C 1D  05 80 23 45 00 80 F0 FF  ..sta3L...#E....
0080: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 1C 03 80 4D  ......fdo1.....M
0090: 2D F8 FF FF 7F F8 FF FF  7F 73 74 61 34 1C 02 80  -........sta4...
00A0: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
00B0: 80 1C 02 80 46 00 20 00  21 00                    ....F. .!.      
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0006 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0007 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0018 [0x1C] WAIT(60* ticks)
  5: 0x001B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x002C [0x1C] WAIT(60* ticks)
  7: 0x002F [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s141" with entities [EventEntity, EventEntity]
  8: 0x003C [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "sta1" with entities [EventEntity, EventEntity]
  9: 0x0049 [0x1C] WAIT(180* ticks)
 10: 0x004C [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "sta2" with entities [EventEntity, EventEntity]
 11: 0x0059 [0x1C] WAIT(300* ticks)
 12: 0x005C [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "sta3" with entities [EventEntity, EventEntity]
 13: 0x0069 [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler "sta3" with entities [EventEntity, EventEntity]
 14: 0x0076 [0x4C] EventEntity->StatusEvent = 8 // Open door
 15: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=7231*)
    → "DEBUG:$3{$3^$3$2p$317F$P10i]\7B"
 16: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x007B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x008C [0x1C] WAIT(180* ticks)
 19: 0x008F [0x4D] EventEntity->StatusEvent = 9 // Close door
 20: 0x0090 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "sta4" with entities [EventEntity, EventEntity]
 21: 0x009D [0x1C] WAIT(60* ticks)
 22: 0x00A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x00B1 [0x1C] WAIT(60* ticks)
 24: 0x00B4 [0x46] CAMERA_CONTROL: Restore default settings
 25: 0x00B6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 26: 0x00B8 [0x21] END_EVENT
 27: 0x00B9 [0x00] END_REQSTACK()
```
