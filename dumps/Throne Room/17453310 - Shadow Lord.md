# 17453310 - Shadow Lord

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Throne Room (ID: 165) |
| Block Size       | 372 bytes             |
| Total Events     | 9                     |
| References Count | 32                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32004](#event-32004)    | 0x0001       |     16 |              3 |
| [7](#event-7)            | 0x0011       |     16 |              3 |
| [65535.1](#event-655351) | 0x0021       |    100 |             12 |
| [65535.2](#event-655352) | 0x0085       |     10 |              2 |
| [65535.3](#event-655353) | 0x008F       |     19 |              3 |
| [65535.4](#event-655354) | 0x00A2       |     10 |              2 |
| [65535.5](#event-655355) | 0x00AC       |     10 |              2 |
| [65535.6](#event-655356) | 0x00B6       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF8F031  |  4294504497 |
|       1 | 0xFFFC56BA  |  4294727354 |
|       2 | 0xFFFD72E1  |  4294800097 |
|       3 | 0x0FF9      |        4089 |
|       4 | 0xFFF908BE  |  4294510782 |
|       5 | 0xFFFC56A4  |  4294727332 |
|       6 | 0x0011      |          17 |
|       7 | 0x0050      |          80 |
|       8 | 0x003C      |          60 |
|       9 | 0x0060      |          96 |
|      10 | 0x0030      |          48 |
|      11 | 0x0048      |          72 |
|      12 | 0x0020      |          32 |
|      13 | 0x0068      |         104 |
|      14 | 0x0038      |          56 |
|      15 | 0x0070      |         112 |
|      16 | 0x0040      |          64 |
|      17 | 0x0000      |           0 |
|      18 | 0x00B4      |         180 |
|      19 | 0xFFF9C4E4  |  4294558948 |
|      20 | 0xFFFC577E  |  4294727550 |
|      21 | 0xFFFD74A3  |  4294800547 |
|      22 | 0x07EB      |        2027 |
|      23 | 0x0080      |         128 |
|      24 | 0x0001      |           1 |
|      25 | 0x0811      |        2065 |
|      26 | 0xFFF4112D  |  4294185261 |
|      27 | 0xFFF8ACE2  |  4294487266 |
|      28 | 0xFFF9C961  |  4294560097 |
|      29 | 0xFFEF2F22  |  4293865250 |
|      30 | 0xFFF503C9  |  4294247369 |
|      31 | 0xFFF61FE2  |  4294320098 |

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

### Event 32004

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2F 00 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   /.....7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-462.799*, z=-239.942*, y=-167.199*, direction=359.4°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    2F 00 F8 FF FF 7F 37  04 80 05 80 02 80 06 80   /.....7........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0017 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-456.514*, z=-239.964*, y=-167.199*, direction=1.5°*
  2: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0021    |
| Data Size    | 100 bytes |
| Instructions | 12        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    6C F8 FF FF 7F 07 80  08 80 6C F8 FF FF 7F 09   l........l.....
0030: 80 08 80 6C F8 FF FF 7F  0A 80 08 80 6C F8 FF FF  ...l........l...
0040: 7F 0B 80 08 80 6C F8 FF  FF 7F 0C 80 08 80 6C F8  .....l........l.
0050: FF FF 7F 0D 80 08 80 6C  F8 FF FF 7F 0E 80 08 80  .......l........
0060: 6C F8 FF FF 7F 0F 80 08  80 6C F8 FF FF 7F 10 80  l........l......
0070: 08 80 6C F8 FF FF 7F 09  80 08 80 6C F8 FF FF 7F  ..l........l....
0080: 11 80 12 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0021 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=80*, fade_time=60*)
  1: 0x002A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=96*, fade_time=60*)
  2: 0x0033 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=48*, fade_time=60*)
  3: 0x003C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=72*, fade_time=60*)
  4: 0x0045 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=32*, fade_time=60*)
  5: 0x004E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=104*, fade_time=60*)
  6: 0x0057 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=56*, fade_time=60*)
  7: 0x0060 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=112*, fade_time=60*)
  8: 0x0069 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=64*, fade_time=60*)
  9: 0x0072 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=96*, fade_time=60*)
 10: 0x007B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=180*)
 11: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                37 13 80  14 80 15 80 16 80 00          7......... 
```

#### Opcodes

```
  0: 0x0085 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-408.348*, z=-239.746*, y=-166.749*, direction=178.1°*
  1: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               6C                 l
0090: F8 FF FF 7F 17 80 18 80  37 04 80 05 80 02 80 19  ........7.......
00A0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x008F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0098 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-456.514*, z=-239.964*, y=-167.199*, direction=181.5°*
  2: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x00A2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-462.799*, z=-239.942*, y=-167.199*, direction=359.4°*
  1: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      37 1A 80 1B              7...
00B0: 80 1C 80 03 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00AC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-782.035*, z=-480.030*, y=-407.199*, direction=359.4°*
  1: 0x00B5 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B6   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   37 1D  80 1E 80 1F 80 03 80 00        7.........
```

#### Opcodes

```
  0: 0x00B6 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1102.046*, z=-719.927*, y=-647.198*, direction=359.4°*
  1: 0x00BF [0x00] END_REQSTACK()
```
