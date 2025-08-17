# 17335101 - Excenmille

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Beaucedine Glacier [S] (ID: 136) |
| Block Size       | 352 bytes                        |
| Total Events     | 19                               |
| References Count | 19                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [3](#event-3)              | 0x0001       |      1 |              1 |
| [4](#event-4)              | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     44 |              5 |
| [65535.2](#event-655352)   | 0x002F       |     14 |              4 |
| [65535.3](#event-655353)   | 0x003D       |     11 |              3 |
| [65535.4](#event-655354)   | 0x0048       |     10 |              2 |
| [65535.5](#event-655355)   | 0x0052       |     10 |              2 |
| [65535.6](#event-655356)   | 0x005C       |      1 |              1 |
| [65535.7](#event-655357)   | 0x005D       |     18 |              4 |
| [65535.8](#event-655358)   | 0x006F       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0079       |      9 |              3 |
| [65535.10](#event-6553510) | 0x0082       |      9 |              3 |
| [65535.11](#event-6553511) | 0x008B       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0095       |     11 |              3 |
| [2](#event-2)              | 0x00A0       |      1 |              1 |
| [65535.13](#event-6553513) | 0x00A1       |     11 |              3 |
| [6](#event-6)              | 0x00AC       |      1 |              1 |
| [65535.14](#event-6553514) | 0x00AD       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0515      |        1301 |
|       1 | 0x0032      |          50 |
|       2 | 0x05DC      |        1500 |
|       3 | 0x000C      |          12 |
|       4 | 0x1AD35     |      109877 |
|       5 | 0x1E8BA     |      125114 |
|       6 | 0xFFFFB2D8  |  4294947544 |
|       7 | 0x1AA7C     |      109180 |
|       8 | 0x1E4A7     |      124071 |
|       9 | 0xFFFFB32F  |  4294947631 |
|      10 | 0x0000      |           0 |
|      11 | 0x0001      |           1 |
|      12 | 0x0080      |         128 |
|      13 | 0x1886A     |      100458 |
|      14 | 0x209E8     |      133608 |
|      15 | 0xFFFFB0E7  |  4294947047 |
|      16 | 0x1DCA2     |      122018 |
|      17 | 0xFFFCC59C  |  4294755740 |
|      18 | 0xFFFFB358  |  4294947672 |

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

### Event 3

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

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 44 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 73 68     [..........sh
0010: 61 31 53 F8 FF FF 7F F8  FF FF 7F 73 68 61 31 59  a1S........sha1Y
0020: 01 F8 FF FF 7F 01 80 4B  F8 FF FF 7F 02 80 00     .......K....... 
```

#### Opcodes

```
  0: 0x0003 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=1301*
  1: 0x0012 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  2: 0x001F [0x59] UPDATE_ENTITY_DATA: Set EventEntity turn speed = 50*
  3: 0x0027 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=8.2°*)
  4: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 03 80 1F 00 04 80 05 80  06 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=109.877*, Z=125.114*, Y=-19.752*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         1F 00 07               ...
0040: 80 08 80 09 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=109.180*, Z=124.071*, Y=-19.665*
  1: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          6C F8 FF FF 7F 0A 80 0B          l.......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0048 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       6C F8 FF FF 7F 0C  80 0B 80 00                l.........    
```

#### Opcodes

```
  0: 0x0052 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      00                       .   
```

#### Opcodes

```
  0: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         22 00 2F               "./
0060: 00 F8 FF FF 7F 6C F8 FF  FF 7F 0A 80 0B 80 00     .....l......... 
```

#### Opcodes

```
  0: 0x005D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x005F [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0065 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               6C                 l
0070: F8 FF FF 7F 0C 80 0B 80  00                       .........       
```

#### Opcodes

```
  0: 0x006F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0079  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             22 00 2F 00 F8 FF FF           "./....
0080: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0079 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x007B [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0082  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       22 01 2F 01 F8 FF  FF 7F 00                   "./......     
```

#### Opcodes

```
  0: 0x0082 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0084 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   6C F8 FF FF 7F             l....
0090: 0A 80 0B 80 00                                    .....           
```

#### Opcodes

```
  0: 0x008B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 11 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                6C F8 FF  FF 7F 0C 80 0B 80 00 00       l..........
```

#### Opcodes

```
  0: 0x0095 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x009E [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x009F [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A0  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A1   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    1F 00 0D 80 0E 80 0F  80 1F 01 00               ...........    
```

#### Opcodes

```
  0: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=100.458*, Z=133.608*, Y=-20.249*
  1: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00AB [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         1F 00 10               ...
00B0: 80 11 80 12 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x00AD [0x1F] MOVE_ENTITY: EventEntity moves to X=122.018*, Z=-211.556*, Y=-19.624*
  1: 0x00B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00B7 [0x00] END_REQSTACK()
```
