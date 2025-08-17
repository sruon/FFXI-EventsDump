# 16916890 - Cermet Portal

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Grand Palace of Hu'Xzoi (ID: 34) |
| Block Size       | 260 bytes                        |
| Total Events     | 6                                |
| References Count | 8                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [59](#event-59)          | 0x0002       |    181 |             30 |
| [0](#event-0)            | 0x00B7       |      1 |              1 |
| [65535.1](#event-655351) | 0x00B8       |      2 |              2 |
| [65535.2](#event-655352) | 0x00BA       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0013      |          19 |
|       4 | 0x0078      |         120 |
|       5 | 0x00F0      |         240 |
|       6 | 0x0064      |         100 |
|       7 | 0x00C9      |         201 |

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

### Event 65534

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

### Event 59

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 181 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 43 00 43 01  46 01 42 45 00 80 F0 FF     .C.C.F.BE....
0010: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 1C 02 80 38  ......fdo1.....8
0020: 03 80 29 01 F0 FF FF 7F  08 45 00 80 F0 FF FF 7F  ..)......E......
0030: F0 FF FF 7F 66 64 69 31  01 80 1C 04 80 2D F8 FF  ....fdi1.....-..
0040: FF 7F F8 FF FF 7F 73 31  34 39 2D F8 FF FF 7F F8  ......s149-.....
0050: FF FF 7F 68 69 6B 61 54  F8 FF FF 7F F8 FF FF 7F  ...hikaT........
0060: 68 69 6B 61 1C 02 80 4C  1C 04 80 27 01 F0 FF FF  hika...L...'....
0070: 7F 09 1C 05 80 4D 1C 06  80 45 00 80 F0 FF FF 7F  .....M...E......
0080: F0 FF FF 7F 66 64 6F 31  01 80 1C 02 80 45 07 80  ....fdo1.....E..
0090: F0 FF FF 7F F0 FF FF 7F  77 68 69 31 01 80 46 00  ........whi1..F.
00A0: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
00B0: 80 46 00 20 00 21 00                              .F. .!.         
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x0006 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x0008 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x000A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x000B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x001C [0x1C] WAIT(60* ticks)
  7: 0x001F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0022 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x08)
  9: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x003A [0x1C] WAIT(120* ticks)
 11: 0x003D [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s149" with entities [EventEntity, EventEntity]
 12: 0x004A [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "hika" with entities [EventEntity, EventEntity]
 13: 0x0057 [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler "hika" with entities [EventEntity, EventEntity]
 14: 0x0064 [0x1C] WAIT(60* ticks)
 15: 0x0067 [0x4C] EventEntity->StatusEvent = 8 // Open door
 16: 0x0068 [0x1C] WAIT(120* ticks)
 17: 0x006B [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
 18: 0x0072 [0x1C] WAIT(240* ticks)
 19: 0x0075 [0x4D] EventEntity->StatusEvent = 9 // Close door
 20: 0x0076 [0x1C] WAIT(100* ticks)
 21: 0x0079 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x008A [0x1C] WAIT(60* ticks)
 23: 0x008D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 24: 0x009E [0x46] CAMERA_CONTROL: Restore default settings
 25: 0x00A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x00B1 [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x00B3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 28: 0x00B5 [0x21] END_EVENT
 29: 0x00B6 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      00                                  .        
```

#### Opcodes

```
  0: 0x00B7 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B8  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          4C 00                            L.      
```

#### Opcodes

```
  0: 0x00B8 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x00B9 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BA  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                4D 00                        M.    
```

#### Opcodes

```
  0: 0x00BA [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x00BB [0x00] END_REQSTACK()
```
