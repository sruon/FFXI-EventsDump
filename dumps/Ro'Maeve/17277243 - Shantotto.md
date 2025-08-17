# 17277243 - Shantotto

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Ro'Maeve (ID: 122) |
| Block Size       | 340 bytes          |
| Total Events     | 15                 |
| References Count | 18                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [71](#event-71)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     19 |              5 |
| [65535.2](#event-655352)   | 0x0015       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0025       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0035       |     19 |              3 |
| [65535.5](#event-655355)   | 0x0048       |     19 |              3 |
| [65535.6](#event-655356)   | 0x005B       |     14 |              4 |
| [65535.7](#event-655357)   | 0x0069       |     19 |              3 |
| [65535.8](#event-655358)   | 0x007C       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0086       |      3 |              2 |
| [65535.10](#event-6553510) | 0x0089       |     18 |              4 |
| [65535.11](#event-6553511) | 0x009B       |      2 |              2 |
| [65535.12](#event-6553512) | 0x009D       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00AD       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0941      |        2369 |
|       1 | 0x0031      |          49 |
|       2 | 0x0AD3      |        2771 |
|       3 | 0x0060      |          96 |
|       4 | 0x00B4      |         180 |
|       5 | 0x001E      |          30 |
|       6 | 0xFFFD1822  |  4294776866 |
|       7 | 0x4BD2      |       19410 |
|       8 | 0xFFFFEFE3  |  4294963171 |
|       9 | 0x0ACA      |        2762 |
|      10 | 0x027C      |         636 |
|      11 | 0x0000      |           0 |
|      12 | 0xFFFCDDF8  |  4294761976 |
|      13 | 0x7AAD      |       31405 |
|      14 | 0xFFFFEF95  |  4294963093 |
|      15 | 0x01E0      |         480 |
|      16 | 0x000F      |          15 |
|      17 | 0x007D      |         125 |

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

### Event 71

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
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       B6 00 00 80 22 00  92 01 F8 FF FF 7F 94 01    ....".........
0010: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0002 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2369*)
  1: 0x0006 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000E [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0014 [0x00] END_REQSTACK()
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
0010:                66 01 80  F8 FF FF 7F F8 FF FF 7F       f..........
0020: 74 6C 6B 30 00                                    tlk0.           
```

#### Opcodes

```
  0: 0x0015 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
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
0020:                66 01 80  F8 FF FF 7F F8 FF FF 7F       f..........
0030: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x0025 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                5B 02 80  F8 FF FF 7F F8 FF FF 7F       [..........
0040: 6F 6A 69 30 1C 03 80 00                           oji0....        
```

#### Opcodes

```
  0: 0x0035 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "oji0" with entities [EventEntity, EventEntity], work=2771*
  1: 0x0044 [0x1C] WAIT(96* ticks)
  2: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          5B 02 80 F8 FF FF 7F F8          [.......
0050: FF FF 7F 6F 6A 69 31 1C  04 80 00                 ...oji1....     
```

#### Opcodes

```
  0: 0x0048 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "oji1" with entities [EventEntity, EventEntity], work=2771*
  1: 0x0057 [0x1C] WAIT(180* ticks)
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   32 05 80 1F 00             2....
0060: 06 80 07 80 08 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x005B [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=-190.430*, Z=19.410*, Y=-4.125*
  2: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             5B 09 80 F8 FF FF 7F           [......
0070: F8 FF FF 7F 69 6B 69 30  1C 0A 80 00              ....iki0....    
```

#### Opcodes

```
  0: 0x0069 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "iki0" with entities [EventEntity, EventEntity], work=2762*
  1: 0x0078 [0x1C] WAIT(636* ticks)
  2: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      6C F8 FF FF              l...
0080: 7F 0B 80 0B 80 00                                 ......          
```

#### Opcodes

```
  0: 0x007C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0086  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   A4 01  00                             ...       
```

#### Opcodes

```
  0: 0x0086 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             84 BA F8 FF FF 7F 0C           .......
0090: 80 0D 80 0E 80 0F 80 1C  10 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0089 [0x84] ADJUST_RENDER_FLAGS3_BIT0()
  1: 0x008A [0xBA] SET_ENTITY_POSITION(entity_id=EventEntity, pos_x=-205.320*, pos_z=31.405*, pos_y=-4.203*, direction=42.2°*)
  2: 0x0097 [0x1C] WAIT(15* ticks)
  3: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009B  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   84 00                      ..   
```

#### Opcodes

```
  0: 0x009B [0x84] ADJUST_RENDER_FLAGS3_BIT0()
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         5B 02 80               [..
00A0: F8 FF FF 7F F8 FF FF 7F  6D 73 6F 30 00           ........mso0.   
```

#### Opcodes

```
  0: 0x009D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mso0" with entities [EventEntity, EventEntity], work=2771*
  1: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         5B 02 80               [..
00B0: F8 FF FF 7F F8 FF FF 7F  6D 73 6F 31 1C 11 80 00  ........mso1....
```

#### Opcodes

```
  0: 0x00AD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mso1" with entities [EventEntity, EventEntity], work=2771*
  1: 0x00BC [0x1C] WAIT(125* ticks)
  2: 0x00BF [0x00] END_REQSTACK()
```
