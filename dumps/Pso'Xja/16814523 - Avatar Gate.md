# 16814523 - Avatar Gate

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Pso'Xja (ID: 9) |
| Block Size       | 172 bytes       |
| Total Events     | 7               |
| References Count | 7               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      2 |              2 |
| [65535.2](#event-655352) | 0x0004       |      2 |              2 |
| [11](#event-11)          | 0x0006       |     85 |             17 |
| [3](#event-3)            | 0x005B       |      1 |              1 |
| [65535.3](#event-655353) | 0x005C       |      6 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x01E0      |         480 |
|       1 | 0x01A4      |         420 |
|       2 | 0x00B4      |         180 |
|       3 | 0x00C8      |         200 |
|       4 | 0x0000      |           0 |
|       5 | 0x003C      |          60 |
|       6 | 0x012C      |         300 |

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

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 85 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   20 01  46 01 42 2D F8 FF FF 7F         .F.B-....
0010: F8 FF FF 7F 63 72 73 74  2D F8 FF FF 7F F8 FF FF  ....crst-.......
0020: 7F 73 31 31 39 1C 00 80  4C 1C 01 80 4D 1C 02 80  .s119...L...M...
0030: 45 03 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 04  E..........fdo1.
0040: 80 1C 05 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0050: 64 69 31 04 80 46 00 20  00 21 00                 di1..F. .!.     
```

#### Opcodes

```
  0: 0x0006 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0008 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x000A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x000B [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "crst" with entities [EventEntity, EventEntity]
  4: 0x0018 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s119" with entities [EventEntity, EventEntity]
  5: 0x0025 [0x1C] WAIT(480* ticks)
  6: 0x0028 [0x4C] EventEntity->StatusEvent = 8 // Open door
  7: 0x0029 [0x1C] WAIT(420* ticks)
  8: 0x002C [0x4D] EventEntity->StatusEvent = 9 // Close door
  9: 0x002D [0x1C] WAIT(180* ticks)
 10: 0x0030 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x0041 [0x1C] WAIT(60* ticks)
 12: 0x0044 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0055 [0x46] CAMERA_CONTROL: Restore default settings
 14: 0x0057 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 15: 0x0059 [0x21] END_EVENT
 16: 0x005A [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   00                         .    
```

#### Opcodes

```
  0: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      4C 1C 06 80              L...
0060: 4D 00                                             M.              
```

#### Opcodes

```
  0: 0x005C [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x005D [0x1C] WAIT(300* ticks)
  2: 0x0060 [0x4D] EventEntity->StatusEvent = 9 // Close door
  3: 0x0061 [0x00] END_REQSTACK()
```
