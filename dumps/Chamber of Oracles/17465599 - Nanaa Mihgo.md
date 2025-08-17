# 17465599 - Nanaa Mihgo

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Chamber of Oracles (ID: 168) |
| Block Size       | 460 bytes                    |
| Total Events     | 16                           |
| References Count | 24                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     21 |              6 |
| [65535.2](#event-655352)   | 0x0016       |     12 |              4 |
| [65535.3](#event-655353)   | 0x0022       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0032       |     16 |              2 |
| [5](#event-5)              | 0x0042       |      1 |              1 |
| [65535.5](#event-655355)   | 0x0043       |     10 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     10 |              2 |
| [65535.7](#event-655357)   | 0x0057       |     18 |              2 |
| [65535.8](#event-655358)   | 0x0069       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0078       |     46 |              8 |
| [65535.10](#event-6553510) | 0x00A6       |     20 |              5 |
| [6](#event-6)              | 0x00BA       |      1 |              1 |
| [65535.11](#event-6553511) | 0x00BB       |     34 |              8 |
| [65535.12](#event-6553512) | 0x00DD       |     31 |              5 |
| [65535.13](#event-6553513) | 0x00FC       |     31 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FA      |         250 |
|       1 | 0x31909     |      203017 |
|       2 | 0x9B5D      |       39773 |
|       3 | 0xFFFFF736  |  4294965046 |
|       4 | 0x0039      |          57 |
|       5 | 0x0000      |           0 |
|       6 | 0x0080      |         128 |
|       7 | 0x0002      |           2 |
|       8 | 0x000D      |          13 |
|       9 | 0x032C      |         812 |
|      10 | 0xFFFFF8DE  |  4294965470 |
|      11 | 0x0338      |         824 |
|      12 | 0x000F      |          15 |
|      13 | 0x0AC4      |        2756 |
|      14 | 0x001E      |          30 |
|      15 | 0x000A      |          10 |
|      16 | 0x24BE      |        9406 |
|      17 | 0x155C      |        5468 |
|      18 | 0x0694      |        1684 |
|      19 | 0x087C      |        2172 |
|      20 | 0xFFFFC562  |  4294952290 |
|      21 | 0x023E      |         574 |
|      22 | 0xFFFF0212  |  4294902290 |
|      23 | 0x0100      |         256 |

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
| Data Size    | 21 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    A4 01 B6 00 00 80 22  00 92 01 F8 FF FF 7F 94   ......"........
0010: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0001 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=250*)
  2: 0x0007 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0009 [0x92] EventEntity->Render.Flags3 ^= 0x01
  4: 0x000F [0x94] EventEntity->Render.Flags3 ^= 0x01
  5: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   1F 00  01 80 02 80 03 80 1F 01        ..........
0020: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0016 [0x1F] MOVE_ENTITY: EventEntity moves to X=203.017*, Z=39.773*, Y=-2.250*
  1: 0x001E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0020 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       66 04 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B    f..........tlk
0030: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0022 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=57*
  1: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       66 04 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B    f..........tlk
0040: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0032 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=57*
  1: 0x0041 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0042  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       00                                            .             
```

#### Opcodes

```
  0: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          6C F8 FF FF 7F  05 80 05 80 00              l.........   
```

#### Opcodes

```
  0: 0x0043 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         6C F8 FF               l..
0050: FF 7F 06 80 05 80 00                              .......         
```

#### Opcodes

```
  0: 0x004D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  1: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      62  07 80 F8 FF FF 7F F8 FF         b........
0060: FF 7F 6D 61 69 6E 05 80  00                       ..main...       
```

#### Opcodes

```
  0: 0x0057 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[2*, 0*]
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             32 08 80 1F 00 09 80           2......
0070: 0A 80 0B 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0069 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=0.812*, Z=-1.826*, Y=0.824*
  2: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 46 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          81 00 F8 FF FF 7F 7C 00          ......|.
0080: F8 FF FF 7F 1C 0C 80 5B  0D 80 F8 FF FF 7F F8 FF  .......[........
0090: FF 7F 79 65 73 30 1C 0E  80 81 01 F8 FF FF 7F 7C  ..yes0.........|
00A0: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0078 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x007E [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x0084 [0x1C] WAIT(15* ticks)
  3: 0x0087 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes0" with entities [EventEntity, EventEntity], work=2756*
  4: 0x0096 [0x1C] WAIT(30* ticks)
  5: 0x0099 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  6: 0x009F [0x7C] EventEntity->Render.Flags2 |= 0x01
  7: 0x00A5 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A6   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   59 04  F8 FF FF 7F 0F 80 1F 00        Y.........
00B0: 10 80 11 80 04 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x00A6 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 10* * 0.1
  1: 0x00AE [0x1F] MOVE_ENTITY: EventEntity moves to X=9.406*, Z=5.468*, Y=0.057*
  2: 0x00B6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B9 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                00                           .     
```

#### Opcodes

```
  0: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   32 0C 80 1F 00             2....
00C0: 12 80 13 80 03 80 1F 01  1F 00 05 80 14 80 15 80  ................
00D0: 1F 01 5A 00 05 80 16 80  15 80 5A 01 00           ..Z.......Z..   
```

#### Opcodes

```
  0: 0x00BB [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x00BE [0x1F] MOVE_ENTITY: EventEntity moves to X=1.684*, Z=2.172*, Y=-2.250*
  2: 0x00C6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C8 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=-15.006*, Y=0.574*
  4: 0x00D0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00D2 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=0.000*, Z=-65.006*, Y=0.574*
  6: 0x00DA [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 31 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         81 00 F8               ...
00E0: FF FF 7F 7C 00 F8 FF FF  7F 1C 0C 80 5B 0D 80 F8  ...|........[...
00F0: FF FF 7F F8 FF FF 7F 69  74 61 30 00              .......ita0.    
```

#### Opcodes

```
  0: 0x00DD [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x00E3 [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x00E9 [0x1C] WAIT(15* ticks)
  3: 0x00EC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ita0" with entities [EventEntity, EventEntity], work=2756*
  4: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FC   |
| Data Size    | 31 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      81 00 F8 FF              ....
0100: FF 7F 7C 00 F8 FF FF 7F  5B 0D 80 F8 FF FF 7F F8  ..|.....[.......
0110: FF FF 7F 69 74 61 31 1C  17 80 00                 ...ita1....     
```

#### Opcodes

```
  0: 0x00FC [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0102 [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x0108 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ita1" with entities [EventEntity, EventEntity], work=2756*
  3: 0x0117 [0x1C] WAIT(256* ticks)
  4: 0x011A [0x00] END_REQSTACK()
```
