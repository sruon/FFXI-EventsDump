# 17293779 - Seed Mandragora

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qufim Island (ID: 126) |
| Block Size       | 492 bytes              |
| Total Events     | 24                     |
| References Count | 29                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [31](#event-31)            | 0x0001       |      4 |              2 |
| [65535.1](#event-655351)   | 0x0005       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0015       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0025       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0035       |     16 |              2 |
| [65535.5](#event-655355)   | 0x0045       |     12 |              3 |
| [65535.6](#event-655356)   | 0x0051       |     12 |              3 |
| [65535.7](#event-655357)   | 0x005D       |     12 |              3 |
| [65535.8](#event-655358)   | 0x0069       |     12 |              3 |
| [65535.9](#event-655359)   | 0x0075       |      5 |              2 |
| [65535.10](#event-6553510) | 0x007A       |     15 |              5 |
| [65535.11](#event-6553511) | 0x0089       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0099       |     20 |              5 |
| [65535.13](#event-6553513) | 0x00AD       |     20 |              5 |
| [65535.14](#event-6553514) | 0x00C1       |      5 |              2 |
| [65535.15](#event-6553515) | 0x00C6       |      5 |              2 |
| [65535.16](#event-6553516) | 0x00CB       |      5 |              2 |
| [65535.17](#event-6553517) | 0x00D0       |      5 |              2 |
| [65535.18](#event-6553518) | 0x00D5       |      5 |              2 |
| [32](#event-32)            | 0x00DA       |      4 |              2 |
| [65535.19](#event-6553519) | 0x00DE       |     20 |              5 |
| [65535.20](#event-6553520) | 0x00F2       |     20 |              5 |
| [34](#event-34)            | 0x0106       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0A0F      |        2575 |
|       2 | 0x0000      |           0 |
|       3 | 0x0078      |         120 |
|       4 | 0x0080      |         128 |
|       5 | 0x092E      |        2350 |
|       6 | 0x000A      |          10 |
|       7 | 0xFFFE3200  |  4294849024 |
|       8 | 0x4B72D     |      309037 |
|       9 | 0xFFFFBEF2  |  4294950642 |
|      10 | 0x0A09      |        2569 |
|      11 | 0x000D      |          13 |
|      12 | 0xB45E      |       46174 |
|      13 | 0x3EA47     |      256583 |
|      14 | 0xFFFFAC13  |  4294945811 |
|      15 | 0xFFFEC28A  |  4294886026 |
|      16 | 0x51D2E     |      335150 |
|      17 | 0xFFFF5E2A  |  4294925866 |
|      18 | 0x0034      |          52 |
|      19 | 0x015C      |         348 |
|      20 | 0x0020      |          32 |
|      21 | 0x012C      |         300 |
|      22 | 0x0930      |        2352 |
|      23 | 0xFFFE0B48  |  4294839112 |
|      24 | 0x48047     |      294983 |
|      25 | 0xFFFFB3E3  |  4294947811 |
|      26 | 0x0028      |          40 |
|      27 | 0xFFFE1700  |  4294842112 |
|      28 | 0x48BFF     |      297983 |

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

### Event 31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    C0 00 80 00                                     ....           
```

#### Opcodes

```
  0: 0x0001 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                5B 01 80  D3 E1 07 01 D3 E1 07 01       [..........
0010: 73 6D 61 30 00                                    sma0.           
```

#### Opcodes

```
  0: 0x0005 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sma0" with entities [Seed Mandragora (ID: 17293779/0x0107E1D3), Seed Mandragora (ID: 17293779/0x0107E1D3)], work=2575*
  1: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                5B 01 80  D3 E1 07 01 D3 E1 07 01       [..........
0020: 73 6D 61 31 00                                    sma1.           
```

#### Opcodes

```
  0: 0x0015 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sma1" with entities [Seed Mandragora (ID: 17293779/0x0107E1D3), Seed Mandragora (ID: 17293779/0x0107E1D3)], work=2575*
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                5B 01 80  D3 E1 07 01 D3 E1 07 01       [..........
0030: 73 6D 61 32 00                                    sma2.           
```

#### Opcodes

```
  0: 0x0025 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sma2" with entities [Seed Mandragora (ID: 17293779/0x0107E1D3), Seed Mandragora (ID: 17293779/0x0107E1D3)], work=2575*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                5B 01 80  D3 E1 07 01 D3 E1 07 01       [..........
0040: 73 6D 61 35 00                                    sma5.           
```

#### Opcodes

```
  0: 0x0035 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sma5" with entities [Seed Mandragora (ID: 17293779/0x0107E1D3), Seed Mandragora (ID: 17293779/0x0107E1D3)], work=2575*
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                A4 00 6C  D3 E1 07 01 02 80 03 80       ..l........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0045 [0xA4] EventEntity->Flags3.unknown_3_2 = 0
  1: 0x0047 [0x6C] FADE_ENTITY_COLOR(entity_id=Seed Mandragora (ID: 17293779/0x0107E1D3), end_alpha=0*, fade_time=120*)
  2: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    6C D3 E1 07 01 04 80  03 80 A4 01 00            l...........   
```

#### Opcodes

```
  0: 0x0051 [0x6C] FADE_ENTITY_COLOR(entity_id=Seed Mandragora (ID: 17293779/0x0107E1D3), end_alpha=128*, fade_time=120*)
  1: 0x005A [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  2: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         A4 00 6C               ..l
0060: D3 E1 07 01 02 80 02 80  00                       .........       
```

#### Opcodes

```
  0: 0x005D [0xA4] EventEntity->Flags3.unknown_3_2 = 0
  1: 0x005F [0x6C] FADE_ENTITY_COLOR(entity_id=Seed Mandragora (ID: 17293779/0x0107E1D3), end_alpha=0*, fade_time=0*)
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             6C D3 E1 07 01 04 80           l......
0070: 02 80 A4 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0069 [0x6C] FADE_ENTITY_COLOR(entity_id=Seed Mandragora (ID: 17293779/0x0107E1D3), end_alpha=128*, fade_time=0*)
  1: 0x0072 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  2: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0075  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                B6 00 05  80 00                         .....      
```

#### Opcodes

```
  0: 0x0075 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2350*)
  1: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                32 06 80 1F 00 07            2.....
0080: 80 08 80 09 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x007A [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=-118.272*, Z=309.037*, Y=-16.654*
  2: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0087 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             5B 0A 80 D3 E1 07 01           [......
0090: D3 E1 07 01 79 65 73 30  00                       ....yes0.       
```

#### Opcodes

```
  0: 0x0089 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes0" with entities [Seed Mandragora (ID: 17293779/0x0107E1D3), Seed Mandragora (ID: 17293779/0x0107E1D3)], work=2569*
  1: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             59 04 D3 E1 07 01 0B           Y......
00A0: 80 1F 00 0C 80 0D 80 0E  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x0099 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293779/0x0107E1D3) main speed = 13* * 0.1
  1: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=46.174*, Z=256.583*, Y=-21.485*
  2: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         59 04 D3               Y..
00B0: E1 07 01 0B 80 1F 00 0F  80 10 80 11 80 1F 01 6F  ...............o
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AD [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293779/0x0107E1D3) main speed = 13* * 0.1
  1: 0x00B5 [0x1F] MOVE_ENTITY: EventEntity moves to X=-81.270*, Z=335.150*, Y=-41.430*
  2: 0x00BD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C1  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    B6 00 12 80 00                                  .....          
```

#### Opcodes

```
  0: 0x00C1 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C6  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   B6 00  13 80 00                       .....     
```

#### Opcodes

```
  0: 0x00C6 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=348*)
  1: 0x00CA [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CB  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                   B6 00 14 80 00             .....
```

#### Opcodes

```
  0: 0x00CB [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=32*)
  1: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D0  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: B6 00 15 80 00                                    .....           
```

#### Opcodes

```
  0: 0x00D0 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=300*)
  1: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D5  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                B6 00 16  80 00                         .....      
```

#### Opcodes

```
  0: 0x00D5 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2352*)
  1: 0x00D9 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DA  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                C0 00 80 00                  ....  
```

#### Opcodes

```
  0: 0x00DA [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x00DD [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DE   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            59 04                Y.
00E0: D3 E1 07 01 0B 80 1F 00  17 80 18 80 19 80 1F 01  ................
00F0: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x00DE [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293779/0x0107E1D3) main speed = 13* * 0.1
  1: 0x00E6 [0x1F] MOVE_ENTITY: EventEntity moves to X=-128.184*, Z=294.983*, Y=-19.485*
  2: 0x00EE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00F1 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F2   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       59 04 D3 E1 07 01  1A 80 1F 00 1B 80 1C 80    Y.............
0100: 19 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x00F2 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293779/0x0107E1D3) main speed = 40* * 0.1
  1: 0x00FA [0x1F] MOVE_ENTITY: EventEntity moves to X=-125.184*, Z=297.983*, Y=-19.485*
  2: 0x0102 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0104 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0105 [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0106  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                   00                                    .         
```

#### Opcodes

```
  0: 0x0106 [0x00] END_REQSTACK()
```
