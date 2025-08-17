# 17867236 - Melisandra

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Marjami Ravine (ID: 266) |
| Block Size       | 268 bytes                |
| Total Events     | 12                       |
| References Count | 23                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [55](#event-55)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     22 |              6 |
| [65535.2](#event-655352) | 0x0018       |     10 |              2 |
| [57](#event-57)          | 0x0022       |      1 |              1 |
| [65535.3](#event-655353) | 0x0023       |     10 |              2 |
| [65535.4](#event-655354) | 0x002D       |     10 |              2 |
| [65](#event-65)          | 0x0037       |      1 |              1 |
| [65535.5](#event-655355) | 0x0038       |     24 |              6 |
| [66](#event-66)          | 0x0050       |      1 |              1 |
| [65535.6](#event-655356) | 0x0051       |     14 |              4 |
| [65535.7](#event-655357) | 0x005F       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFE5B43  |  4294859587 |
|       2 | 0xFFFEBA26  |  4294883878 |
|       3 | 0x4FBC      |       20412 |
|       4 | 0x001E      |          30 |
|       5 | 0x0000      |           0 |
|       6 | 0x003C      |          60 |
|       7 | 0x0040      |          64 |
|       8 | 0x0001      |           1 |
|       9 | 0x0080      |         128 |
|      10 | 0x0028      |          40 |
|      11 | 0x17190     |       94608 |
|      12 | 0xFFFE3036  |  4294848566 |
|      13 | 0x5071      |       20593 |
|      14 | 0x144AE     |       83118 |
|      15 | 0xFFFE4BD4  |  4294855636 |
|      16 | 0x4FA8      |       20392 |
|      17 | 0xFEF1      |       65265 |
|      18 | 0xFFFE813F  |  4294869311 |
|      19 | 0x5256      |       21078 |
|      20 | 0xF0E3      |       61667 |
|      21 | 0xFFFEEBC8  |  4294896584 |
|      22 | 0x43A7      |       17319 |

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

### Event 55

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1E    2.............
0010: E1 A1 10 01 1C 04 80 00                           ........        
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-107.709*, Z=-83.418*, Y=20.412*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1E] EventEntity looks at Nashu (ID: 17867233/0x0110A1E1) and starts talking
  4: 0x0014 [0x1C] WAIT(30* ticks)
  5: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          6C F8 FF FF 7F 05 80 06          l.......
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0018 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x0021 [0x00] END_REQSTACK()
```

### Event 57

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

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          6C F8 FF FF 7F  07 80 08 80 00              l.........   
```

#### Opcodes

```
  0: 0x0023 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=64*, fade_time=1*)
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         6C F8 FF               l..
0030: FF 7F 09 80 08 80 00                              .......         
```

#### Opcodes

```
  0: 0x002D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      00                                  .        
```

#### Opcodes

```
  0: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          32 0A 80 1F 00 0B 80 0C          2.......
0040: 80 0D 80 1F 01 1F 00 0E  80 0F 80 10 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x0038 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=94.608*, Z=-118.730*, Y=20.593*
  2: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=83.118*, Z=-111.660*, Y=20.392*
  4: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004F [0x00] END_REQSTACK()
```

### Event 66

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

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    32 00 80 1F 00 11 80  12 80 13 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0051 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=65.265*, Z=-97.985*, Y=21.078*
  2: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               32                 2
0060: 00 80 1F 00 14 80 15 80  16 80 1F 01 1C 04 80 00  ................
```

#### Opcodes

```
  0: 0x005F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0062 [0x1F] MOVE_ENTITY: EventEntity moves to X=61.667*, Z=-70.712*, Y=17.319*
  2: 0x006A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006C [0x1C] WAIT(30* ticks)
  4: 0x006F [0x00] END_REQSTACK()
```
