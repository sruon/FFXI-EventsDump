# 17776869 - Goblin Enforcer

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 416 bytes             |
| Total Events     | 21                    |
| References Count | 17                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     15 |              4 |
| [65535.2](#event-655352)   | 0x0010       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001A       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0024       |      5 |              2 |
| [10180](#event-10180)      | 0x0029       |      1 |              1 |
| [65535.5](#event-655355)   | 0x002A       |     18 |              2 |
| [10182](#event-10182)      | 0x003C       |      1 |              1 |
| [65535.6](#event-655356)   | 0x003D       |     13 |              3 |
| [65535.7](#event-655357)   | 0x004A       |      8 |              3 |
| [65535.8](#event-655358)   | 0x0052       |     18 |              3 |
| [65535.9](#event-655359)   | 0x0064       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0074       |     16 |              2 |
| [65535.11](#event-6553511) | 0x0084       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0094       |     16 |              2 |
| [10184](#event-10184)      | 0x00A4       |      1 |              1 |
| [65535.13](#event-6553513) | 0x00A5       |      8 |              3 |
| [65535.14](#event-6553514) | 0x00AD       |     27 |              7 |
| [65535.15](#event-6553515) | 0x00C8       |     15 |              5 |
| [65535.16](#event-6553516) | 0x00D7       |     16 |              2 |
| [65535.17](#event-6553517) | 0x00E7       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0080      |         128 |
|       1 | 0x0000      |           0 |
|       2 | 0x0034      |          52 |
|       3 | 0x007C      |         124 |
|       4 | 0x00B4      |         180 |
|       5 | 0x093C      |        2364 |
|       6 | 0x0001      |           1 |
|       7 | 0x0A50      |        2640 |
|       8 | 0x0442      |        1090 |
|       9 | 0x000E      |          14 |
|      10 | 0xFFFEB127  |  4294881575 |
|      11 | 0x1294F     |       76111 |
|      12 | 0xFFFFFB50  |  4294966096 |
|      13 | 0x000F      |          15 |
|      14 | 0xFFFEBB20  |  4294884128 |
|      15 | 0x1176F     |       71535 |
|      16 | 0x00D7      |         215 |

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
0010: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
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
0020: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             B6 00 02 80  00                           .....       
```

#### Opcodes

```
  0: 0x0024 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 10180

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                C5 03 80 F8 FF FF            ......
0030: 7F F8 FF FF 7F 6D 61 69  6E 01 80 00              .....main...    
```

#### Opcodes

```
  0: 0x002A [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80016E69 for entities [EventEntity, EventEntity], work=124*, param=24941
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 10182

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      00                       .   
```

#### Opcodes

```
  0: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         1C 04 80               ...
0040: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x003D [0x1C] WAIT(180* ticks)
  1: 0x0040 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  2: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                B6 00 05 80 C0 06            ......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x004A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2364*)
  1: 0x004E [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 18 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       22 00 5B 07 80 F8  FF FF 7F F8 FF FF 7F 62    ".[..........b
0060: 6B 61 30 00                                       ka0.            
```

#### Opcodes

```
  0: 0x0052 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0054 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bka0" with entities [EventEntity, EventEntity], work=2640*
  2: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             5B 07 80 F8  FF FF 7F F8 FF FF 7F 62      [..........b
0070: 6B 61 6C 00                                       kal.            
```

#### Opcodes

```
  0: 0x0064 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bkal" with entities [EventEntity, EventEntity], work=2640*
  1: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             5B 07 80 F8  FF FF 7F F8 FF FF 7F 62      [..........b
0080: 6B 61 31 00                                       ka1.            
```

#### Opcodes

```
  0: 0x0074 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bka1" with entities [EventEntity, EventEntity], work=2640*
  1: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             5B 07 80 F8  FF FF 7F F8 FF FF 7F 62      [..........b
0090: 6B 6C 30 00                                       kl0.            
```

#### Opcodes

```
  0: 0x0084 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bkl0" with entities [EventEntity, EventEntity], work=2640*
  1: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             5B 07 80 F8  FF FF 7F F8 FF FF 7F 62      [..........b
00A0: 6B 6C 31 00                                       kl1.            
```

#### Opcodes

```
  0: 0x0094 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bkl1" with entities [EventEntity, EventEntity], work=2640*
  1: 0x00A3 [0x00] END_REQSTACK()
```

### Event 10184

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             00                                        .           
```

#### Opcodes

```
  0: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A5  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                B6 00 08  80 C0 06 80 00                ........   
```

#### Opcodes

```
  0: 0x00A5 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1090*)
  1: 0x00A9 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         32 09 80               2..
00B0: 1F 00 0A 80 0B 80 0C 80  1F 01 6F 1C 0D 80 4A F8  ..........o...J.
00C0: FF FF 7F E0 40 0F 01 00                           ....@...        
```

#### Opcodes

```
  0: 0x00AD [0x32] ExtData[1]->MainSpeed = 14* * 0.1
  1: 0x00B0 [0x1F] MOVE_ENTITY: EventEntity moves to X=-85.721*, Z=76.111*, Y=-1.200*
  2: 0x00B8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00BB [0x1C] WAIT(15* ticks)
  5: 0x00BE [0x4A] EventEntity looks at Moogle (ID: 17776864/0x010F40E0)
  6: 0x00C7 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C8   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          32 09 80 1F 00 0E 80 0F          2.......
00D0: 80 0C 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x00C8 [0x32] ExtData[1]->MainSpeed = 14* * 0.1
  1: 0x00CB [0x1F] MOVE_ENTITY: EventEntity moves to X=-83.168*, Z=71.535*, Y=-1.200*
  2: 0x00D3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00D6 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      5B  10 80 F8 FF FF 7F F8 FF         [........
00E0: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x00D7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=215*
  1: 0x00E6 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                      5B  10 80 F8 FF FF 7F F8 FF         [........
00F0: FF 7F 74 6C 6B 65 00                              ..tlke.         
```

#### Opcodes

```
  0: 0x00E7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [EventEntity, EventEntity], work=215*
  1: 0x00F6 [0x00] END_REQSTACK()
```
