# 17465600 - Goblin Repossessor

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Chamber of Oracles (ID: 168) |
| Block Size       | 820 bytes                    |
| Total Events     | 36                           |
| References Count | 25                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     15 |              4 |
| [65535.2](#event-655352)   | 0x0010       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001A       |     12 |              3 |
| [65535.4](#event-655354)   | 0x0026       |      8 |              3 |
| [65535.5](#event-655355)   | 0x002E       |     34 |              8 |
| [5](#event-5)              | 0x0050       |      1 |              1 |
| [6](#event-6)              | 0x0051       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0052       |     13 |              3 |
| [65535.7](#event-655357)   | 0x005F       |     19 |              3 |
| [65535.8](#event-655358)   | 0x0072       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0082       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0092       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00A2       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00B2       |      2 |              2 |
| [65535.13](#event-6553513) | 0x00B4       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00C4       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00D4       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00E4       |     16 |              2 |
| [65535.17](#event-6553517) | 0x00F4       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0104       |     16 |              2 |
| [65535.19](#event-6553519) | 0x0114       |     16 |              2 |
| [65535.20](#event-6553520) | 0x0124       |     16 |              2 |
| [65535.21](#event-6553521) | 0x0134       |     16 |              2 |
| [65535.22](#event-6553522) | 0x0144       |     16 |              2 |
| [65535.23](#event-6553523) | 0x0154       |     16 |              2 |
| [65535.24](#event-6553524) | 0x0164       |     16 |              2 |
| [65535.25](#event-6553525) | 0x0174       |     16 |              2 |
| [65535.26](#event-6553526) | 0x0184       |     16 |              2 |
| [65535.27](#event-6553527) | 0x0194       |     34 |              4 |
| [65535.28](#event-6553528) | 0x01B6       |     19 |              3 |
| [65535.29](#event-6553529) | 0x01C9       |     19 |              3 |
| [65535.30](#event-6553530) | 0x01DC       |     19 |              3 |
| [65535.31](#event-6553531) | 0x01EF       |     24 |              6 |
| [65535.32](#event-6553532) | 0x0207       |     19 |              3 |
| [65535.33](#event-6553533) | 0x021A       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0080      |         128 |
|       2 | 0x01F9      |         505 |
|       3 | 0x0001      |           1 |
|       4 | 0x002D      |          45 |
|       5 | 0x0694      |        1684 |
|       6 | 0x087C      |        2172 |
|       7 | 0xFFFFF736  |  4294965046 |
|       8 | 0xFFFFC562  |  4294952290 |
|       9 | 0x023E      |         574 |
|      10 | 0xFFFF0212  |  4294902290 |
|      11 | 0x005A      |          90 |
|      12 | 0x0866      |        2150 |
|      13 | 0x004A      |          74 |
|      14 | 0x00D7      |         215 |
|      15 | 0x00D8      |         216 |
|      16 | 0x0078      |         120 |
|      17 | 0x00BC      |         188 |
|      18 | 0x00DA      |         218 |
|      19 | 0x001E      |          30 |
|      20 | 0x0011      |          17 |
|      21 | 0x0244      |         580 |
|      22 | 0xFFFFFE88  |  4294966920 |
|      23 | 0x0338      |         824 |
|      24 | 0x0050      |          80 |

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
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                A4 01 6C F8 FF FF            ..l...
0020: 7F 01 80 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x001A [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x001C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  2: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   B6 00  02 80 C0 03 80 00              ........  
```

#### Opcodes

```
  0: 0x0026 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=505*)
  1: 0x002A [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            32 04                2.
0030: 80 1F 00 05 80 06 80 07  80 1F 01 1F 00 00 80 08  ................
0040: 80 09 80 1F 01 5A 00 00  80 0A 80 09 80 5A 01 00  .....Z.......Z..
```

#### Opcodes

```
  0: 0x002E [0x32] ExtData[1]->MainSpeed = 45* * 0.1
  1: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.684*, Z=2.172*, Y=-2.250*
  2: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=-15.006*, Y=0.574*
  4: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0045 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=0.000*, Z=-65.006*, Y=0.574*
  6: 0x004D [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x004F [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0050  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0050 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    00                                              .              
```

#### Opcodes

```
  0: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       1C 0B 80 4A F8 FF  FF 7F FF 80 0A 01 00       ...J......... 
```

#### Opcodes

```
  0: 0x0052 [0x1C] WAIT(90* ticks)
  1: 0x0055 [0x4A] EventEntity looks at Nanaa Mihgo (ID: 17465599/0x010A80FF)
  2: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               5B                 [
0060: 0C 80 F8 FF FF 7F F8 FF  FF 7F 6F 64 6F 30 1C 0D  ..........odo0..
0070: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x005F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "odo0" with entities [EventEntity, EventEntity], work=2150*
  1: 0x006E [0x1C] WAIT(74* ticks)
  2: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       5B 0C 80 F8 FF FF  7F F8 FF FF 7F 6F 64 6F    [..........odo
0080: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0072 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "odo1" with entities [EventEntity, EventEntity], work=2150*
  1: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       5B 0E 80 00 81 0A  01 00 81 0A 01 74 6C 6B    [..........tlk
0090: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0082 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=215*
  1: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       5B 0E 80 00 81 0A  01 00 81 0A 01 70 61 73    [..........pas
00A0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0092 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=215*
  1: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       5B 0E 80 F8 FF FF  7F F8 FF FF 7F 63 6F 72    [..........cor
00B0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x00A2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "cor0" with entities [EventEntity, EventEntity], work=215*
  1: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B2  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       84 00                                         ..            
```

#### Opcodes

```
  0: 0x00B2 [0x84] ADJUST_RENDER_FLAGS3_BIT0()
  1: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             5B 0E 80 00  81 0A 01 00 81 0A 01 74      [..........t
00C0: 6C 6B 32 00                                       lk2.            
```

#### Opcodes

```
  0: 0x00B4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=215*
  1: 0x00C3 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:             5B 0E 80 00  81 0A 01 00 81 0A 01 74      [..........t
00D0: 69 64 30 00                                       id0.            
```

#### Opcodes

```
  0: 0x00C4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tid0" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=215*
  1: 0x00D3 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             5B 0E 80 00  81 0A 01 00 81 0A 01 74      [..........t
00E0: 61 6F 30 00                                       ao0.            
```

#### Opcodes

```
  0: 0x00D4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tao0" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=215*
  1: 0x00E3 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             5B 0F 80 00  81 0A 01 00 81 0A 01 61      [..........a
00F0: 6E 67 30 00                                       ng0.            
```

#### Opcodes

```
  0: 0x00E4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x00F3 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:             5B 0F 80 00  81 0A 01 00 81 0A 01 61      [..........a
0100: 6E 67 31 00                                       ng1.            
```

#### Opcodes

```
  0: 0x00F4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang1" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0103 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0104   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             5B 0F 80 00  81 0A 01 00 81 0A 01 62      [..........b
0110: 69 6B 30 00                                       ik0.            
```

#### Opcodes

```
  0: 0x0104 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             5B 0F 80 00  81 0A 01 00 81 0A 01 62      [..........b
0120: 69 6B 31 00                                       ik1.            
```

#### Opcodes

```
  0: 0x0114 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik1" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0123 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0124   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:             5B 0F 80 00  81 0A 01 00 81 0A 01 62      [..........b
0130: 79 65 30 00                                       ye0.            
```

#### Opcodes

```
  0: 0x0124 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bye0" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0133 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0134   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:             5B 0F 80 00  81 0A 01 00 81 0A 01 66      [..........f
0140: 75 6D 30 00                                       um0.            
```

#### Opcodes

```
  0: 0x0134 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fum0" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0143 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0144   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:             5B 0F 80 00  81 0A 01 00 81 0A 01 66      [..........f
0150: 75 6D 31 00                                       um1.            
```

#### Opcodes

```
  0: 0x0144 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fum1" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0153 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0154   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:             5B 0F 80 00  81 0A 01 00 81 0A 01 68      [..........h
0160: 61 70 30 00                                       ap0.            
```

#### Opcodes

```
  0: 0x0154 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0163 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0164   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:             5B 0F 80 00  81 0A 01 00 81 0A 01 68      [..........h
0170: 61 70 31 00                                       ap1.            
```

#### Opcodes

```
  0: 0x0164 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap1" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0173 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0174   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:             5B 0F 80 00  81 0A 01 00 81 0A 01 6D      [..........m
0180: 6D 6D 30 00                                       mm0.            
```

#### Opcodes

```
  0: 0x0174 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mmm0" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0183 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0184   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:             5B 0F 80 00  81 0A 01 00 81 0A 01 6D      [..........m
0190: 6D 6D 31 00                                       mm1.            
```

#### Opcodes

```
  0: 0x0184 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mmm1" with entities [Goblin Repossessor (ID: 17465600/0x010A8100), Goblin Repossessor (ID: 17465600/0x010A8100)], work=216*
  1: 0x0193 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0194   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:             5B 0F 80 F8  FF FF 7F F8 FF FF 7F 66      [..........f
01A0: 6E 64 30 1C 10 80 5B 0F  80 F8 FF FF 7F F8 FF FF  nd0...[.........
01B0: 7F 66 6E 64 31 00                                 .fnd1.          
```

#### Opcodes

```
  0: 0x0194 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fnd0" with entities [EventEntity, EventEntity], work=216*
  1: 0x01A3 [0x1C] WAIT(120* ticks)
  2: 0x01A6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fnd1" with entities [EventEntity, EventEntity], work=216*
  3: 0x01B5 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B6   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                   5B 0C  80 F8 FF FF 7F F8 FF FF        [.........
01C0: 7F 70 6E 74 30 1C 11 80  00                       .pnt0....       
```

#### Opcodes

```
  0: 0x01B6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnt0" with entities [EventEntity, EventEntity], work=2150*
  1: 0x01C5 [0x1C] WAIT(188* ticks)
  2: 0x01C8 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C9   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                             5B 12 80 F8 FF FF 7F           [......
01D0: F8 FF FF 7F 77 6B 6E 66  1C 13 80 00              ....wknf....    
```

#### Opcodes

```
  0: 0x01C9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wknf" with entities [EventEntity, EventEntity], work=218*
  1: 0x01D8 [0x1C] WAIT(30* ticks)
  2: 0x01DB [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01DC   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                      5B 0E 80 F8              [...
01E0: FF FF 7F F8 FF FF 7F 74  6C 6B 65 1C 13 80 00     .......tlke.... 
```

#### Opcodes

```
  0: 0x01DC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [EventEntity, EventEntity], work=215*
  1: 0x01EB [0x1C] WAIT(30* ticks)
  2: 0x01EE [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01EF   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                                               32                 2
01F0: 14 80 1F 00 15 80 16 80  17 80 1F 01 6F 4A F8 FF  ............oJ..
0200: FF 7F FD 80 0A 01 00                              .......         
```

#### Opcodes

```
  0: 0x01EF [0x32] ExtData[1]->MainSpeed = 17* * 0.1
  1: 0x01F2 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.580*, Z=-0.376*, Y=0.824*
  2: 0x01FA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01FC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01FD [0x4A] EventEntity looks at Moogle (ID: 17465597/0x010A80FD)
  5: 0x0206 [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0207   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                      5B  0C 80 F8 FF FF 7F F8 FF         [........
0210: FF 7F 74 6C 33 30 1C 18  80 00                    ..tl30....      
```

#### Opcodes

```
  0: 0x0207 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl30" with entities [EventEntity, EventEntity], work=2150*
  1: 0x0216 [0x1C] WAIT(80* ticks)
  2: 0x0219 [0x00] END_REQSTACK()
```

### Event 65535.33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x021A   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                                5B 0C 80 F8 FF FF            [.....
0220: 7F F8 FF FF 7F 74 6C 33  31 1C 13 80 00           .....tl31....   
```

#### Opcodes

```
  0: 0x021A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl31" with entities [EventEntity, EventEntity], work=2150*
  1: 0x0229 [0x1C] WAIT(30* ticks)
  2: 0x022C [0x00] END_REQSTACK()
```
