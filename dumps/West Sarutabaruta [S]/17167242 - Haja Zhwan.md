# 17167242 - Haja Zhwan

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 424 bytes                      |
| Total Events     | 17                             |
| References Count | 29                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [110](#event-110)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     24 |              6 |
| [65535.2](#event-655352)   | 0x001A       |     21 |              2 |
| [65535.3](#event-655353)   | 0x002F       |     21 |              2 |
| [65535.4](#event-655354)   | 0x0044       |     21 |              2 |
| [65535.5](#event-655355)   | 0x0059       |     24 |              6 |
| [65535.6](#event-655356)   | 0x0071       |     24 |              6 |
| [65535.7](#event-655357)   | 0x0089       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0093       |     10 |              2 |
| [65535.9](#event-655359)   | 0x009D       |      1 |              1 |
| [65535.10](#event-6553510) | 0x009E       |     18 |              4 |
| [65535.11](#event-6553511) | 0x00B0       |     10 |              2 |
| [65535.12](#event-6553512) | 0x00BA       |      9 |              3 |
| [65535.13](#event-6553513) | 0x00C3       |      9 |              3 |
| [65535.14](#event-6553514) | 0x00CC       |     10 |              2 |
| [65535.15](#event-6553515) | 0x00D6       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFCEC59  |  4294765657 |
|       2 | 0xFFFCA6E7  |  4294747879 |
|       3 | 0xFFFEF87A  |  4294899834 |
|       4 | 0xFFFCF574  |  4294767988 |
|       5 | 0xFFFCE367  |  4294763367 |
|       6 | 0xFFFEF65C  |  4294899292 |
|       7 | 0x0007      |           7 |
|       8 | 0x0001      |           1 |
|       9 | 0x0000      |           0 |
|      10 | 0x000B      |          11 |
|      11 | 0x00A2      |         162 |
|      12 | 0x001A      |          26 |
|      13 | 0x0023      |          35 |
|      14 | 0x0036      |          54 |
|      15 | 0x00DB      |         219 |
|      16 | 0x0171      |         369 |
|      17 | 0x0006      |           6 |
|      18 | 0x0077      |         119 |
|      19 | 0x0013      |          19 |
|      20 | 0x002B      |          43 |
|      21 | 0xFFFB63BF  |  4294665151 |
|      22 | 0xFFFFCEB4  |  4294954676 |
|      23 | 0xFFFF4480  |  4294919296 |
|      24 | 0xFFFB45AD  |  4294657453 |
|      25 | 0xFFFFCD67  |  4294954343 |
|      26 | 0xFFFB8FD0  |  4294676432 |
|      27 | 0xFFFFCE29  |  4294954537 |
|      28 | 0x0080      |         128 |

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

### Event 110

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 05 80 06 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-201.639*, Z=-219.417*, Y=-67.462*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-199.308*, Z=-203.929*, Y=-68.004*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                B6 0B 07 80 08 80            ......
0020: 09 80 0A 80 0A 80 0B 80  0B 80 09 80 09 80 00     ............... 
```

#### Opcodes

```
  0: 0x001A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=1*, head=0*, body=11*, hands=11*, legs=162*, feet=162*, main=0*, sub=0*)
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               B6                 .
0030: 0B 07 80 0C 80 09 80 0D  80 0E 80 0F 80 09 80 10  ................
0040: 80 09 80 00                                       ....            
```

#### Opcodes

```
  0: 0x002F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=26*, head=0*, body=35*, hands=54*, legs=219*, feet=0*, main=369*, sub=0*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             B6 0B 11 80  11 80 12 80 13 80 13 80      ............
0050: 13 80 13 80 09 80 09 80  00                       .........       
```

#### Opcodes

```
  0: 0x0044 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=6*, head=119*, body=19*, hands=19*, legs=19*, feet=19*, main=0*, sub=0*)
  1: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 14 80 1F 00 15 80           2......
0060: 16 80 17 80 1F 01 1F 00  18 80 19 80 17 80 1F 01  ................
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 43* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.145*, Z=-12.620*, Y=-48.000*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=-309.843*, Z=-12.953*, Y=-48.000*
  4: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    32 0E 80 1F 00 15 80  16 80 17 80 1F 01 1F 00   2..............
0080: 1A 80 1B 80 17 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0071 [0x32] ExtData[1]->MainSpeed = 54* * 0.1
  1: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.145*, Z=-12.620*, Y=-48.000*
  2: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007E [0x1F] MOVE_ENTITY: EventEntity moves to X=-290.864*, Z=-12.759*, Y=-48.000*
  4: 0x0086 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             6C F8 FF FF 7F 09 80           l......
0090: 08 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0089 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0093   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          6C F8 FF FF 7F  1C 80 08 80 00              l.........   
```

#### Opcodes

```
  0: 0x0093 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         00                     .  
```

#### Opcodes

```
  0: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            22 00                ".
00A0: 2F 00 F8 FF FF 7F 6C F8  FF FF 7F 09 80 08 80 00  /.....l.........
```

#### Opcodes

```
  0: 0x009E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00A0 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00A6 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 6C F8 FF FF 7F 1C 80 08  80 00                    l.........      
```

#### Opcodes

```
  0: 0x00B0 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00B9 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BA  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                22 00 2F 00 F8 FF            "./...
00C0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x00BA [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00BC [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C3  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          22 01 2F 01 F8  FF FF 7F 00                 "./......    
```

#### Opcodes

```
  0: 0x00C3 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00C5 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x00CB [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                      6C F8 FF FF              l...
00D0: 7F 09 80 08 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00CC [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x00D5 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D6   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   6C F8  FF FF 7F 1C 80 08 80 00        l.........
```

#### Opcodes

```
  0: 0x00D6 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00DF [0x00] END_REQSTACK()
```
