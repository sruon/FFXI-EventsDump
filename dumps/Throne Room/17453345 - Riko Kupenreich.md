# 17453345 - Riko Kupenreich

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Throne Room (ID: 165) |
| Block Size       | 644 bytes             |
| Total Events     | 26                    |
| References Count | 24                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     19 |              5 |
| [65535.2](#event-655352)   | 0x0014       |     12 |              3 |
| [65535.3](#event-655353)   | 0x0020       |     12 |              3 |
| [4](#event-4)              | 0x002C       |      1 |              1 |
| [65535.4](#event-655354)   | 0x002D       |     16 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     37 |              5 |
| [65535.6](#event-655356)   | 0x0062       |     19 |              3 |
| [65535.7](#event-655357)   | 0x0075       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0085       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0095       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00A5       |     19 |              3 |
| [65535.11](#event-6553511) | 0x00B8       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00C8       |     19 |              3 |
| [65535.13](#event-6553513) | 0x00DB       |     21 |              3 |
| [65535.14](#event-6553514) | 0x00F0       |     18 |              2 |
| [5](#event-5)              | 0x0102       |      1 |              1 |
| [65535.15](#event-6553515) | 0x0103       |     16 |              2 |
| [65535.16](#event-6553516) | 0x0113       |     19 |              3 |
| [65535.17](#event-6553517) | 0x0126       |     19 |              3 |
| [65535.18](#event-6553518) | 0x0139       |     22 |              4 |
| [65535.19](#event-6553519) | 0x014F       |     18 |              2 |
| [65535.20](#event-6553520) | 0x0161       |     16 |              2 |
| [65535.21](#event-6553521) | 0x0171       |     19 |              3 |
| [65535.22](#event-6553522) | 0x0184       |     19 |              3 |
| [65535.23](#event-6553523) | 0x0197       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0937      |        2359 |
|       1 | 0x0000      |           0 |
|       2 | 0x0080      |         128 |
|       3 | 0x0A48      |        2632 |
|       4 | 0x0AC3      |        2755 |
|       5 | 0x0078      |         120 |
|       6 | 0x0028      |          40 |
|       7 | 0x0A52      |        2642 |
|       8 | 0x0050      |          80 |
|       9 | 0x0A55      |        2645 |
|      10 | 0x0140      |         320 |
|      11 | 0x01E0      |         480 |
|      12 | 0x0089      |         137 |
|      13 | 0x0320      |         800 |
|      14 | 0x00A0      |         160 |
|      15 | 0x0A58      |        2648 |
|      16 | 0x0194      |         404 |
|      17 | 0x003C      |          60 |
|      18 | 0x00F0      |         240 |
|      19 | 0x008D      |         141 |
|      20 | 0x0AC5      |        2757 |
|      21 | 0x0120      |         288 |
|      22 | 0x0098      |         152 |
|      23 | 0x0068      |         104 |

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
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 B6 00 00 80 92  01 F8 FF FF 7F 94 01 F8   "..............
0010: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2359*)
  2: 0x0007 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000D [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             A4 00 6C F8  FF FF 7F 01 80 01 80 00      ..l.........
```

#### Opcodes

```
  0: 0x0014 [0xA4] EventEntity->Flags3.unknown_3_2 = 0
  1: 0x0016 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  2: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: A4 01 6C F8 FF FF 7F 02  80 01 80 00              ..l.........    
```

#### Opcodes

```
  0: 0x0020 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0022 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  2: 0x002B [0x00] END_REQSTACK()
```

### Event 4

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

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         5B 03 80               [..
0030: F8 FF FF 7F F8 FF FF 7F  6D 64 77 30 00           ........mdw0.   
```

#### Opcodes

```
  0: 0x002D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mdw0" with entities [EventEntity, EventEntity], work=2632*
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         5B 04 80               [..
0040: F8 FF FF 7F F8 FF FF 7F  70 6E 62 30 1C 05 80 5B  ........pnb0...[
0050: 04 80 F8 FF FF 7F F8 FF  FF 7F 70 6E 62 31 1C 06  ..........pnb1..
0060: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnb0" with entities [EventEntity, EventEntity], work=2755*
  1: 0x004C [0x1C] WAIT(120* ticks)
  2: 0x004F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnb1" with entities [EventEntity, EventEntity], work=2755*
  3: 0x005E [0x1C] WAIT(40* ticks)
  4: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       5B 07 80 F8 FF FF  7F F8 FF FF 7F 6C 64 77    [..........ldw
0070: 30 1C 08 80 00                                    0....           
```

#### Opcodes

```
  0: 0x0062 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ldw0" with entities [EventEntity, EventEntity], work=2642*
  1: 0x0071 [0x1C] WAIT(80* ticks)
  2: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                5B 09 80  F8 FF FF 7F F8 FF FF 7F       [..........
0080: 72 63 73 64 00                                    rcsd.           
```

#### Opcodes

```
  0: 0x0075 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rcsd" with entities [EventEntity, EventEntity], work=2645*
  1: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                5B 09 80  F8 FF FF 7F F8 FF FF 7F       [..........
0090: 72 73 74 64 00                                    rstd.           
```

#### Opcodes

```
  0: 0x0085 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rstd" with entities [EventEntity, EventEntity], work=2645*
  1: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                5B 09 80  F8 FF FF 7F F8 FF FF 7F       [..........
00A0: 6E 73 74 64 00                                    nstd.           
```

#### Opcodes

```
  0: 0x0095 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nstd" with entities [EventEntity, EventEntity], work=2645*
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                5B 09 80  F8 FF FF 7F F8 FF FF 7F       [..........
00B0: 72 77 72 30 1C 0A 80 00                           rwr0....        
```

#### Opcodes

```
  0: 0x00A5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rwr0" with entities [EventEntity, EventEntity], work=2645*
  1: 0x00B4 [0x1C] WAIT(320* ticks)
  2: 0x00B7 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B8   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          5B 09 80 F8 FF FF 7F F8          [.......
00C0: FF FF 7F 72 64 77 30 00                           ...rdw0.        
```

#### Opcodes

```
  0: 0x00B8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rdw0" with entities [EventEntity, EventEntity], work=2645*
  1: 0x00C7 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C8   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          5B 09 80 F8 FF FF 7F F8          [.......
00D0: FF FF 7F 72 64 77 31 1C  0B 80 00                 ...rdw1....     
```

#### Opcodes

```
  0: 0x00C8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rdw1" with entities [EventEntity, EventEntity], work=2645*
  1: 0x00D7 [0x1C] WAIT(480* ticks)
  2: 0x00DA [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DB   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   C5 0C 80 F8 FF             .....
00E0: FF 7F F8 FF FF 7F 73 30  30 30 01 80 1C 0D 80 00  ......s000......
```

#### Opcodes

```
  0: 0x00DB [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80013030 for entities [EventEntity, EventEntity], work=137*, param=12403
  1: 0x00EC [0x1C] WAIT(800* ticks)
  2: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: C5 0C 80 F8 FF FF 7F F8  FF FF 7F 6B 69 6C 30 01  ...........kil0.
0100: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00F0 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8001306C for entities [EventEntity, EventEntity], work=137*, param=26987
  1: 0x0101 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0102  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       00                                            .             
```

#### Opcodes

```
  0: 0x0102 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0103   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          5B 07 80 F8 FF  FF 7F F8 FF FF 7F 6B 79     [..........ky
0110: 6F 30 00                                          o0.             
```

#### Opcodes

```
  0: 0x0103 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kyo0" with entities [EventEntity, EventEntity], work=2642*
  1: 0x0112 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0113   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          5B 07 80 F8 FF  FF 7F F8 FF FF 7F 6F 6A     [..........oj
0120: 69 30 1C 0E 80 00                                 i0....          
```

#### Opcodes

```
  0: 0x0113 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "oji0" with entities [EventEntity, EventEntity], work=2642*
  1: 0x0122 [0x1C] WAIT(160* ticks)
  2: 0x0125 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0126   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                   5B 0F  80 F8 FF FF 7F F8 FF FF        [.........
0130: 7F 6D 73 72 30 1C 10 80  00                       .msr0....       
```

#### Opcodes

```
  0: 0x0126 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "msr0" with entities [EventEntity, EventEntity], work=2648*
  1: 0x0135 [0x1C] WAIT(404* ticks)
  2: 0x0138 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0139   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             1C 11 80 5B 0F 80 F8           ...[...
0140: FF FF 7F F8 FF FF 7F 6D  6D 7A 30 1C 12 80 00     .......mmz0.... 
```

#### Opcodes

```
  0: 0x0139 [0x1C] WAIT(60* ticks)
  1: 0x013C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mmz0" with entities [EventEntity, EventEntity], work=2648*
  2: 0x014B [0x1C] WAIT(240* ticks)
  3: 0x014E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014F   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                               C5                 .
0150: 13 80 F8 FF FF 7F F8 FF  FF 7F 73 30 30 30 01 80  ..........s000..
0160: 00                                                .               
```

#### Opcodes

```
  0: 0x014F [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80013030 for entities [EventEntity, EventEntity], work=141*, param=12403
  1: 0x0160 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0161   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:    5B 14 80 F8 FF FF 7F  F8 FF FF 7F 77 68 74 30   [..........wht0
0170: 00                                                .               
```

#### Opcodes

```
  0: 0x0161 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht0" with entities [EventEntity, EventEntity], work=2757*
  1: 0x0170 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0171   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:    5B 14 80 F8 FF FF 7F  F8 FF FF 7F 77 68 74 31   [..........wht1
0180: 1C 15 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0171 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht1" with entities [EventEntity, EventEntity], work=2757*
  1: 0x0180 [0x1C] WAIT(288* ticks)
  2: 0x0183 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0184   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:             5B 14 80 F8  FF FF 7F F8 FF FF 7F 77      [..........w
0190: 68 74 32 1C 16 80 00                              ht2....         
```

#### Opcodes

```
  0: 0x0184 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht2" with entities [EventEntity, EventEntity], work=2757*
  1: 0x0193 [0x1C] WAIT(152* ticks)
  2: 0x0196 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0197   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                      5B  14 80 F8 FF FF 7F F8 FF         [........
01A0: FF 7F 77 68 74 33 1C 17  80 00                    ..wht3....      
```

#### Opcodes

```
  0: 0x0197 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht3" with entities [EventEntity, EventEntity], work=2757*
  1: 0x01A6 [0x1C] WAIT(104* ticks)
  2: 0x01A9 [0x00] END_REQSTACK()
```
