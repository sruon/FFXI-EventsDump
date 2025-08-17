# 17768475 - DoorStarway Stairway

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 240 bytes               |
| Total Events     | 14                      |
| References Count | 5                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [95](#event-95)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      9 |              5 |
| [105](#event-105)        | 0x000B       |     63 |             15 |
| [106](#event-106)        | 0x004A       |     63 |             15 |
| [441](#event-441)        | 0x0089       |      1 |              1 |
| [448](#event-448)        | 0x008A       |      1 |              1 |
| [449](#event-449)        | 0x008B       |      1 |              1 |
| [454](#event-454)        | 0x008C       |      1 |              1 |
| [455](#event-455)        | 0x008D       |      1 |              1 |
| [460](#event-460)        | 0x008E       |      1 |              1 |
| [65535.2](#event-655352) | 0x008F       |      2 |              2 |
| [65535.3](#event-655353) | 0x0091       |      2 |              2 |
| [462](#event-462)        | 0x0093       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0168      |         360 |
|       1 | 0x0050      |          80 |
|       2 | 0x003C      |          60 |
|       3 | 0x00C8      |         200 |
|       4 | 0x0000      |           0 |

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

### Event 95

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
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4C 1C 00 80 4D 1C  01 80 00                   L...M....     
```

#### Opcodes

```
  0: 0x0002 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0003 [0x1C] WAIT(360* ticks)
  2: 0x0006 [0x4D] EventEntity->StatusEvent = 9 // Close door
  3: 0x0007 [0x1C] WAIT(80* ticks)
  4: 0x000A [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 63 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   46 01 42 20 01             F.B .
0010: 4C 1C 02 80 45 03 80 F8  FF FF 7F F8 FF FF 7F 66  L...E..........f
0020: 64 6F 31 04 80 1C 02 80  29 0B F0 FF FF 7F 26 4D  do1.....).....&M
0030: 1C 01 80 46 00 45 03 80  F8 FF FF 7F F8 FF FF 7F  ...F.E..........
0040: 66 64 69 31 04 80 20 00  21 00                    fdi1.. .!.      
```

#### Opcodes

```
  0: 0x000B [0x46] CAMERA_CONTROL: Disable user control
  1: 0x000D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x000E [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0010 [0x4C] EventEntity->StatusEvent = 8 // Open door
  4: 0x0011 [0x1C] WAIT(60* ticks)
  5: 0x0014 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  6: 0x0025 [0x1C] WAIT(60* ticks)
  7: 0x0028 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x26)
  8: 0x002F [0x4D] EventEntity->StatusEvent = 9 // Close door
  9: 0x0030 [0x1C] WAIT(80* ticks)
 10: 0x0033 [0x46] CAMERA_CONTROL: Restore default settings
 11: 0x0035 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 12: 0x0046 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0048 [0x21] END_EVENT
 14: 0x0049 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 63 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                46 01 42 20 01 4C            F.B .L
0050: 1C 02 80 45 03 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
0060: 6F 31 04 80 1C 02 80 29  0B F0 FF FF 7F 27 4D 1C  o1.....).....'M.
0070: 01 80 46 00 45 03 80 F8  FF FF 7F F8 FF FF 7F 66  ..F.E..........f
0080: 64 69 31 04 80 20 00 21  00                       di1.. .!.       
```

#### Opcodes

```
  0: 0x004A [0x46] CAMERA_CONTROL: Disable user control
  1: 0x004C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x004D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x004F [0x4C] EventEntity->StatusEvent = 8 // Open door
  4: 0x0050 [0x1C] WAIT(60* ticks)
  5: 0x0053 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  6: 0x0064 [0x1C] WAIT(60* ticks)
  7: 0x0067 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x27)
  8: 0x006E [0x4D] EventEntity->StatusEvent = 9 // Close door
  9: 0x006F [0x1C] WAIT(80* ticks)
 10: 0x0072 [0x46] CAMERA_CONTROL: Restore default settings
 11: 0x0074 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 12: 0x0085 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0087 [0x21] END_EVENT
 14: 0x0088 [0x00] END_REQSTACK()
```

### Event 441

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0089  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             00                             .      
```

#### Opcodes

```
  0: 0x0089 [0x00] END_REQSTACK()
```

### Event 448

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                00                           .     
```

#### Opcodes

```
  0: 0x008A [0x00] END_REQSTACK()
```

### Event 449

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   00                         .    
```

#### Opcodes

```
  0: 0x008B [0x00] END_REQSTACK()
```

### Event 454

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      00                       .   
```

#### Opcodes

```
  0: 0x008C [0x00] END_REQSTACK()
```

### Event 455

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         00                     .  
```

#### Opcodes

```
  0: 0x008D [0x00] END_REQSTACK()
```

### Event 460

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            00                   . 
```

#### Opcodes

```
  0: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008F  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               4C                 L
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x008F [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0091  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    4D 00                                           M.             
```

#### Opcodes

```
  0: 0x0091 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0092 [0x00] END_REQSTACK()
```

### Event 462

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0093  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          00                                          .            
```

#### Opcodes

```
  0: 0x0093 [0x00] END_REQSTACK()
```
