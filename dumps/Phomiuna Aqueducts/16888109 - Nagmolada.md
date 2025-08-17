# 16888109 - Nagmolada

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Phomiuna Aqueducts (ID: 27) |
| Block Size       | 464 bytes                   |
| Total Events     | 22                          |
| References Count | 17                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x005B       |     16 |              2 |
| [65535.8](#event-655358)   | 0x006B       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0079       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0089       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0097       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00A7       |     14 |              2 |
| [36](#event-36)            | 0x00B5       |      7 |              2 |
| [65535.13](#event-6553513) | 0x00BC       |     10 |              2 |
| [65535.14](#event-6553514) | 0x00C6       |     15 |              5 |
| [65535.15](#event-6553515) | 0x00D5       |     15 |              5 |
| [35](#event-35)            | 0x00E4       |      7 |              2 |
| [65535.16](#event-6553516) | 0x00EB       |     10 |              2 |
| [65535.17](#event-6553517) | 0x00F5       |     15 |              5 |
| [65535.18](#event-6553518) | 0x0104       |     15 |              5 |
| [65535.19](#event-6553519) | 0x0113       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x01D1      |         465 |
|       1 | 0xFFFE5A20  |  4294859296 |
|       2 | 0xEA60      |       60000 |
|       3 | 0xFFFFA240  |  4294943296 |
|       4 | 0x07E8      |        2024 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFE65D8  |  4294862296 |
|       7 | 0xFFFE6DA8  |  4294864296 |
|       8 | 0xFFFDCAC5  |  4294822597 |
|       9 | 0xE901      |       59649 |
|      10 | 0x0000      |           0 |
|      11 | 0x08AE      |        2222 |
|      12 | 0xFFFDB674  |  4294817396 |
|      13 | 0xE86C      |       59500 |
|      14 | 0xFFFFFC19  |  4294966297 |
|      15 | 0xFFFDA42C  |  4294812716 |
|      16 | 0xFFFD9C5C  |  4294810716 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 61 30   [..........tla0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=465*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 61 30 00      S........tla0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tla0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               5B                 [
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 61 31 00     ..........tla1. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=465*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 61 31 00           ........tla1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tla1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         5B 00 80               [..
0040: F8 FF FF 7F F8 FF FF 7F  74 68 61 30 00           ........tha0.   
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tha0" with entities [EventEntity, EventEntity], work=465*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         53 F8 FF               S..
0050: FF 7F F8 FF FF 7F 74 68  61 30 00                 ......tha0.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tha0" with entities [EventEntity, EventEntity]
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   5B 00 80 F8 FF             [....
0060: FF 7F F8 FF FF 7F 74 68  61 31 00                 ......tha1.     
```

#### Opcodes

```
  0: 0x005B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tha1" with entities [EventEntity, EventEntity], work=465*
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   53 F8 FF FF 7F             S....
0070: F8 FF FF 7F 74 68 61 31  00                       ....tha1.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tha1" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             5B 00 80 F8 FF FF 7F           [......
0080: F8 FF FF 7F 74 68 62 30  00                       ....thb0.       
```

#### Opcodes

```
  0: 0x0079 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb0" with entities [EventEntity, EventEntity], work=465*
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             53 F8 FF FF 7F F8 FF           S......
0090: FF 7F 74 68 62 30 00                              ..thb0.         
```

#### Opcodes

```
  0: 0x0089 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thb0" with entities [EventEntity, EventEntity]
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      5B  00 80 F8 FF FF 7F F8 FF         [........
00A0: FF 7F 74 68 62 31 00                              ..thb1.         
```

#### Opcodes

```
  0: 0x0097 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb1" with entities [EventEntity, EventEntity], work=465*
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00B0: 74 68 62 31 00                                    thb1.           
```

#### Opcodes

```
  0: 0x00A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thb1" with entities [EventEntity, EventEntity]
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 36

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B5  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x00B5 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      37 01 80 02              7...
00C0: 80 03 80 04 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00BC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-108.000*, z=60.000*, y=-24.000*, direction=177.9°*
  1: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   32 05  80 1F 00 06 80 02 80 03        2.........
00D0: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x00C6 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00C9 [0x1F] MOVE_ENTITY: EventEntity moves to X=-105.000*, Z=60.000*, Y=-24.000*
  2: 0x00D1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                32 05 80  1F 00 07 80 02 80 03 80       2..........
00E0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x00D5 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00D8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-103.000*, Z=60.000*, Y=-24.000*
  2: 0x00E0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00E3 [0x00] END_REQSTACK()
```

### Event 35

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E4  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x00E4 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00EA [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EB   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                   37 08 80 09 80             7....
00F0: 0A 80 0B 80 00                                    .....           
```

#### Opcodes

```
  0: 0x00EB [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-144.699*, z=59.649*, y=0.000*, direction=195.3°*
  1: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                32 05 80  1F 00 0C 80 0D 80 0E 80       2..........
0100: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x00F5 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00F8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-149.900*, Z=59.500*, Y=-0.999*
  2: 0x0100 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0102 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0103 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0104   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             32 05 80 1F  00 0F 80 0D 80 0E 80 1F      2...........
0110: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0104 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0107 [0x1F] MOVE_ENTITY: EventEntity moves to X=-154.580*, Z=59.500*, Y=-0.999*
  2: 0x010F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0111 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0112 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0113   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          32 05 80 1F 00  10 80 0D 80 0E 80 1F 01     2............
0120: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0113 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0116 [0x1F] MOVE_ENTITY: EventEntity moves to X=-156.580*, Z=59.500*, Y=-0.999*
  2: 0x011E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0120 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0121 [0x00] END_REQSTACK()
```
