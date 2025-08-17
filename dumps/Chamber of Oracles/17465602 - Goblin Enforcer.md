# 17465602 - Goblin Enforcer

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Chamber of Oracles (ID: 168) |
| Block Size       | 492 bytes                    |
| Total Events     | 19                           |
| References Count | 25                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     15 |              4 |
| [65535.2](#event-655352)   | 0x0010       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001A       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0024       |      8 |              3 |
| [5](#event-5)              | 0x002C       |      1 |              1 |
| [65535.5](#event-655355)   | 0x002D       |     24 |              6 |
| [65535.6](#event-655356)   | 0x0045       |     34 |              4 |
| [65535.7](#event-655357)   | 0x0067       |     19 |              3 |
| [65535.8](#event-655358)   | 0x007A       |     19 |              3 |
| [65535.9](#event-655359)   | 0x008D       |     16 |              2 |
| [65535.10](#event-6553510) | 0x009D       |     19 |              3 |
| [6](#event-6)              | 0x00B0       |      1 |              1 |
| [65535.11](#event-6553511) | 0x00B1       |     13 |              3 |
| [65535.12](#event-6553512) | 0x00BE       |     34 |              8 |
| [65535.13](#event-6553513) | 0x00E0       |     19 |              3 |
| [65535.14](#event-6553514) | 0x00F3       |     16 |              2 |
| [65535.15](#event-6553515) | 0x0103       |     19 |              3 |
| [65535.16](#event-6553516) | 0x0116       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0080      |         128 |
|       2 | 0x0442      |        1090 |
|       3 | 0x0001      |           1 |
|       4 | 0x0011      |          17 |
|       5 | 0x098E      |        2446 |
|       6 | 0xFFFFF8FC  |  4294965500 |
|       7 | 0x0338      |         824 |
|       8 | 0x00D8      |         216 |
|       9 | 0x0064      |         100 |
|      10 | 0x0866      |        2150 |
|      11 | 0x0050      |          80 |
|      12 | 0x001E      |          30 |
|      13 | 0x00D7      |         215 |
|      14 | 0x0048      |          72 |
|      15 | 0x002D      |          45 |
|      16 | 0x0694      |        1684 |
|      17 | 0x087C      |        2172 |
|      18 | 0xFFFFF736  |  4294965046 |
|      19 | 0xFFFFC562  |  4294952290 |
|      20 | 0x023E      |         574 |
|      21 | 0xFFFF0212  |  4294902290 |
|      22 | 0x004A      |          74 |
|      23 | 0x00DA      |         218 |
|      24 | 0x003C      |          60 |

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
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 92 01 F8 FF FF  7F 94 01 F8 FF FF 7F 00   "..............
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0009 [0x94] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 6C F8 FF FF 7F 00 80 00  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                6C F8 FF FF 7F 01            l.....
0020: 80 00 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             B6 00 02 80  C0 03 80 00                  ........    
```

#### Opcodes

```
  0: 0x0024 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1090*)
  1: 0x0028 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x002B [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      00                       .   
```

#### Opcodes

```
  0: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 04 80               2..
0030: 1F 00 05 80 06 80 07 80  1F 01 6F 4A F8 FF FF 7F  ..........oJ....
0040: FD 80 0A 01 00                                    .....           
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 17* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.446*, Z=-1.796*, Y=0.824*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003B [0x4A] EventEntity looks at Moogle (ID: 17465597/0x010A80FD)
  5: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                5B 08 80  F8 FF FF 7F F8 FF FF 7F       [..........
0050: 66 6E 64 30 1C 09 80 5B  08 80 F8 FF FF 7F F8 FF  fnd0...[........
0060: FF 7F 66 6E 64 31 00                              ..fnd1.         
```

#### Opcodes

```
  0: 0x0045 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fnd0" with entities [EventEntity, EventEntity], work=216*
  1: 0x0054 [0x1C] WAIT(100* ticks)
  2: 0x0057 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fnd1" with entities [EventEntity, EventEntity], work=216*
  3: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      5B  0A 80 F8 FF FF 7F F8 FF         [........
0070: FF 7F 74 6C 33 30 1C 0B  80 00                    ..tl30....      
```

#### Opcodes

```
  0: 0x0067 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl30" with entities [EventEntity, EventEntity], work=2150*
  1: 0x0076 [0x1C] WAIT(80* ticks)
  2: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                5B 0A 80 F8 FF FF            [.....
0080: 7F F8 FF FF 7F 74 6C 33  31 1C 0C 80 00           .....tl31....   
```

#### Opcodes

```
  0: 0x007A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl31" with entities [EventEntity, EventEntity], work=2150*
  1: 0x0089 [0x1C] WAIT(30* ticks)
  2: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         5B 0D 80               [..
0090: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 00           ........tlk0.   
```

#### Opcodes

```
  0: 0x008D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=215*
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         5B 0D 80               [..
00A0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 65 1C 0C 80 00  ........tlke....
```

#### Opcodes

```
  0: 0x009D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [EventEntity, EventEntity], work=215*
  1: 0x00AC [0x1C] WAIT(30* ticks)
  2: 0x00AF [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B0  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    1C 0E 80 4A F8 FF FF  7F FF 80 0A 01 00         ...J.........  
```

#### Opcodes

```
  0: 0x00B1 [0x1C] WAIT(72* ticks)
  1: 0x00B4 [0x4A] EventEntity looks at Nanaa Mihgo (ID: 17465599/0x010A80FF)
  2: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            32 0F                2.
00C0: 80 1F 00 10 80 11 80 12  80 1F 01 1F 00 00 80 13  ................
00D0: 80 14 80 1F 01 5A 00 00  80 15 80 14 80 5A 01 00  .....Z.......Z..
```

#### Opcodes

```
  0: 0x00BE [0x32] ExtData[1]->MainSpeed = 45* * 0.1
  1: 0x00C1 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.684*, Z=2.172*, Y=-2.250*
  2: 0x00C9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00CB [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=-15.006*, Y=0.574*
  4: 0x00D3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00D5 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=0.000*, Z=-65.006*, Y=0.574*
  6: 0x00DD [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x00DF [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 5B 0A 80 F8 FF FF 7F F8  FF FF 7F 6F 64 6F 30 1C  [..........odo0.
00F0: 16 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00E0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "odo0" with entities [EventEntity, EventEntity], work=2150*
  1: 0x00EF [0x1C] WAIT(74* ticks)
  2: 0x00F2 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          5B 0A 80 F8 FF  FF 7F F8 FF FF 7F 6F 64     [..........od
0100: 6F 31 00                                          o1.             
```

#### Opcodes

```
  0: 0x00F3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "odo1" with entities [EventEntity, EventEntity], work=2150*
  1: 0x0102 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0103   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          5B 17 80 F8 FF  FF 7F F8 FF FF 7F 77 65     [..........we
0110: 74 63 1C 0C 80 00                                 tc....          
```

#### Opcodes

```
  0: 0x0103 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wetc" with entities [EventEntity, EventEntity], work=218*
  1: 0x0112 [0x1C] WAIT(30* ticks)
  2: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   5B 0D  80 F8 FF FF 7F F8 FF FF        [.........
0120: 7F 74 6C 6B 65 1C 18 80  00                       .tlke....       
```

#### Opcodes

```
  0: 0x0116 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [EventEntity, EventEntity], work=215*
  1: 0x0125 [0x1C] WAIT(60* ticks)
  2: 0x0128 [0x00] END_REQSTACK()
```
