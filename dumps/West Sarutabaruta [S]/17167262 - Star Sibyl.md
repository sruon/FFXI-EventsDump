# 17167262 - Star Sibyl

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 424 bytes                      |
| Total Events     | 19                             |
| References Count | 31                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [105](#event-105)          | 0x0001       |      1 |              1 |
| [110](#event-110)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     15 |              5 |
| [65535.2](#event-655352)   | 0x0012       |      5 |              2 |
| [65535.3](#event-655353)   | 0x0017       |      5 |              2 |
| [65535.4](#event-655354)   | 0x001C       |     26 |              6 |
| [65535.5](#event-655355)   | 0x0036       |     37 |              9 |
| [65535.6](#event-655356)   | 0x005B       |     15 |              5 |
| [65535.7](#event-655357)   | 0x006A       |     14 |              4 |
| [65535.8](#event-655358)   | 0x0078       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0082       |     10 |              2 |
| [65535.10](#event-6553510) | 0x008C       |      1 |              1 |
| [65535.11](#event-6553511) | 0x008D       |     18 |              4 |
| [65535.12](#event-6553512) | 0x009F       |     10 |              2 |
| [65535.13](#event-6553513) | 0x00A9       |      9 |              3 |
| [65535.14](#event-6553514) | 0x00B2       |      9 |              3 |
| [65535.15](#event-6553515) | 0x00BB       |     10 |              2 |
| [65535.16](#event-6553516) | 0x00C5       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000B      |          11 |
|       1 | 0xFFFF71D3  |  4294930899 |
|       2 | 0x2064C     |      132684 |
|       3 | 0xFFFFC181  |  4294951297 |
|       4 | 0x0108      |         264 |
|       5 | 0x004B      |          75 |
|       6 | 0x00C8      |         200 |
|       7 | 0x002A      |          42 |
|       8 | 0xFFFB428D  |  4294656653 |
|       9 | 0xFFFFC8E8  |  4294953192 |
|      10 | 0xFFFF4480  |  4294919296 |
|      11 | 0x0014      |          20 |
|      12 | 0x0046      |          70 |
|      13 | 0xFFFB4E6C  |  4294659692 |
|      14 | 0xFFFFC76F  |  4294952815 |
|      15 | 0xFFFF4481  |  4294919297 |
|      16 | 0xFFFB6BE8  |  4294667240 |
|      17 | 0xFFFFEA35  |  4294961717 |
|      18 | 0xFFFB8399  |  4294673305 |
|      19 | 0x20D1      |        8401 |
|      20 | 0x000D      |          13 |
|      21 | 0x0FFC      |        4092 |
|      22 | 0x2075      |        8309 |
|      23 | 0xFFFF9C65  |  4294941797 |
|      24 | 0x0009      |           9 |
|      25 | 0xFFFFFF05  |  4294967045 |
|      26 | 0x1C81      |        7297 |
|      27 | 0xFFFF9C64  |  4294941796 |
|      28 | 0x0000      |           0 |
|      29 | 0x0001      |           1 |
|      30 | 0x0080      |         128 |

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

### Event 105

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

### Event 110

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
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=-36.397*, Z=132.684*, Y=-15.999*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       B6 00 04 80 00                                .....         
```

#### Opcodes

```
  0: 0x0012 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=264*)
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      B6  00 05 80 00                     .....    
```

#### Opcodes

```
  0: 0x0017 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=75*)
  1: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 26 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      1C 06 80 6B              ...k
0020: 69 64 6C 30 F8 FF FF 7F  32 07 80 1F 00 08 80 09  idl0....2.......
0030: 80 0A 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x001C [0x1C] WAIT(200* ticks)
  1: 0x001F [0x6B] STOP_AND_IDLE: EventEntity stops current action and resets to idle (animation="idl0")
  2: 0x0028 [0x32] ExtData[1]->MainSpeed = 42* * 0.1
  3: 0x002B [0x1F] MOVE_ENTITY: EventEntity moves to X=-310.643*, Z=-14.104*, Y=-48.000*
  4: 0x0033 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   1C 0B  80 32 0C 80 1F 00 0D 80        ...2......
0040: 0E 80 0F 80 1F 01 1F 00  10 80 11 80 0F 80 1F 01  ................
0050: 1F 00 12 80 13 80 0F 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0036 [0x1C] WAIT(20* ticks)
  1: 0x0039 [0x32] ExtData[1]->MainSpeed = 70* * 0.1
  2: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-307.604*, Z=-14.481*, Y=-47.999*
  3: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=-300.056*, Z=-5.579*, Y=-47.999*
  5: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0050 [0x1F] MOVE_ENTITY: EventEntity moves to X=-293.991*, Z=8.401*, Y=-47.999*
  7: 0x0058 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   32 14 80 1F 00             2....
0060: 15 80 16 80 17 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x005B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=4.092*, Z=8.309*, Y=-25.499*
  2: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0068 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                32 18 80 1F 00 19            2.....
0070: 80 1A 80 1B 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x006A [0x32] ExtData[1]->MainSpeed = 9* * 0.1
  1: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.251*, Z=7.297*, Y=-25.500*
  2: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          6C F8 FF FF 7F 1C 80 1D          l.......
0080: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0078 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       6C F8 FF FF 7F 1E  80 1D 80 00                l.........    
```

#### Opcodes

```
  0: 0x0082 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      00                       .   
```

#### Opcodes

```
  0: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         22 00 2F               "./
0090: 00 F8 FF FF 7F 6C F8 FF  FF 7F 1C 80 1D 80 00     .....l......... 
```

#### Opcodes

```
  0: 0x008D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x008F [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0095 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               6C                 l
00A0: F8 FF FF 7F 1E 80 1D 80  00                       .........       
```

#### Opcodes

```
  0: 0x009F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A9  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             22 00 2F 00 F8 FF FF           "./....
00B0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x00A9 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00AB [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B2  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       22 01 2F 01 F8 FF  FF 7F 00                   "./......     
```

#### Opcodes

```
  0: 0x00B2 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00B4 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   6C F8 FF FF 7F             l....
00C0: 1C 80 1D 80 00                                    .....           
```

#### Opcodes

```
  0: 0x00BB [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                6C F8 FF  FF 7F 1E 80 1D 80 00          l......... 
```

#### Opcodes

```
  0: 0x00C5 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00CE [0x00] END_REQSTACK()
```
