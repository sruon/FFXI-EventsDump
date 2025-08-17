# 17171191 - Nhiko Rhaabel

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 428 bytes                       |
| Total Events     | 19                              |
| References Count | 28                              |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [102](#event-102)          | 0x0001       |      1 |              1 |
| [103](#event-103)          | 0x0002       |      1 |              1 |
| [101](#event-101)          | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     29 |              7 |
| [105](#event-105)          | 0x0021       |      1 |              1 |
| [113](#event-113)          | 0x0022       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0023       |      5 |              2 |
| [65535.3](#event-655353)   | 0x0028       |      5 |              2 |
| [65535.4](#event-655354)   | 0x002D       |      5 |              2 |
| [65535.5](#event-655355)   | 0x0032       |     21 |              2 |
| [65535.6](#event-655356)   | 0x0047       |     21 |              2 |
| [65535.7](#event-655357)   | 0x005C       |      5 |              2 |
| [65535.8](#event-655358)   | 0x0061       |     25 |              3 |
| [65535.9](#event-655359)   | 0x007A       |     25 |              3 |
| [65535.10](#event-6553510) | 0x0093       |     25 |              3 |
| [65535.11](#event-6553511) | 0x00AC       |     14 |              4 |
| [65535.12](#event-6553512) | 0x00BA       |     14 |              4 |
| [65535.13](#event-6553513) | 0x00C8       |     22 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x3122F     |      201263 |
|       1 | 0x7074      |       28788 |
|       2 | 0xFFFF9384  |  4294939524 |
|       3 | 0x020C      |         524 |
|       4 | 0x0028      |          40 |
|       5 | 0x305A6     |      198054 |
|       6 | 0x85A0      |       34208 |
|       7 | 0xFFFF9283  |  4294939267 |
|       8 | 0x02F3      |         755 |
|       9 | 0x043C      |        1084 |
|      10 | 0x08C3      |        2243 |
|      11 | 0x0007      |           7 |
|      12 | 0x0003      |           3 |
|      13 | 0x0000      |           0 |
|      14 | 0x005E      |          94 |
|      15 | 0x000E      |          14 |
|      16 | 0x006E      |         110 |
|      17 | 0x0317      |         791 |
|      18 | 0x000D      |          13 |
|      19 | 0xFFFFCF94  |  4294954900 |
|      20 | 0xFFFECAF5  |  4294888181 |
|      21 | 0xFFFEF661  |  4294899297 |
|      22 | 0xFFFFCFBC  |  4294954940 |
|      23 | 0xFFFEC473  |  4294886515 |
|      24 | 0xFFF8DEBA  |  4294500026 |
|      25 | 0xC0BF      |       49343 |
|      26 | 0xFFFF8E45  |  4294938181 |
|      27 | 0x001E      |          30 |

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

### Event 102

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

### Event 103

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

### Event 101

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             37 00 80 01  80 02 80 03 80 32 04 80      7........2..
0010: 1F 00 05 80 06 80 07 80  1F 01 6F 1E F2 02 06 01  ..........o.....
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=201.263*, z=28.788*, y=-27.772*, direction=46.1°*
  1: 0x000D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=198.054*, Z=34.208*, Y=-28.029*
  3: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x001B [0x1E] EventEntity looks at Ajido-Marujido (ID: 17171186/0x010602F2) and starts talking
  6: 0x0020 [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0021  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    00                                              .              
```

#### Opcodes

```
  0: 0x0021 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       00                                            .             
```

#### Opcodes

```
  0: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          B6 00 08 80 00                              .....        
```

#### Opcodes

```
  0: 0x0023 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=755*)
  1: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          B6 00 09 80 00                   .....   
```

#### Opcodes

```
  0: 0x0028 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1084*)
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         B6 00 0A               ...
0030: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x002D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2243*)
  1: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       B6 0B 0B 80 0C 80  0D 80 0E 80 0E 80 0F 80    ..............
0040: 0F 80 0D 80 0D 80 00                              .......         
```

#### Opcodes

```
  0: 0x0032 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=3*, head=0*, body=94*, hands=94*, legs=14*, feet=14*, main=0*, sub=0*)
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      B6  0B 0B 80 0C 80 0D 80 0E         .........
0050: 80 0E 80 0F 80 0F 80 10  80 0D 80 00              ............    
```

#### Opcodes

```
  0: 0x0047 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=3*, head=0*, body=94*, hands=94*, legs=14*, feet=14*, main=110*, sub=0*)
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      B6 00 11 80              ....
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x005C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=791*)
  1: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    B4 00 00 00 3F 3F 3F  00 00 00 00 00 00 00 00   ....???........
0070: 00 00 00 00 00 B5 00 00  00 00                    ..........      
```

#### Opcodes

```
  0: 0x0061 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="???")
  1: 0x0075 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                B4 00 00 00 52 6F            ....Ro
0080: 62 65 6C 2D 41 6B 62 65  6C 00 00 00 00 00 B5 00  bel-Akbel.......
0090: 00 00 00                                          ...             
```

#### Opcodes

```
  0: 0x007A [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Robel-Akbel")
  1: 0x008E [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0093   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          B4 00 00 00 30  32 00 00 00 00 00 00 00     ....02.......
00A0: 00 00 00 00 00 00 00 B5  00 00 00 00              ............    
```

#### Opcodes

```
  0: 0x0093 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="02")
  1: 0x00A7 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      32 12 80 1F              2...
00B0: 00 13 80 14 80 15 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x00AC [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00AF [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.396*, Z=-79.115*, Y=-67.999*
  2: 0x00B7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B9 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BA   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                32 12 80 1F 00 16            2.....
00C0: 80 17 80 15 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x00BA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BD [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.356*, Z=-80.781*, Y=-67.999*
  2: 0x00C5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C7 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C8   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          32 12 80 5A 00 18 80 19          2..Z....
00D0: 80 1A 80 5A 01 1E F0 FF  FF 7F 1C 1B 80 00        ...Z..........  
```

#### Opcodes

```
  0: 0x00C8 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00CB [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-467.270*, Z=49.343*, Y=-29.115*
  2: 0x00D3 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00D5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00DA [0x1C] WAIT(30* ticks)
  5: 0x00DD [0x00] END_REQSTACK()
```
