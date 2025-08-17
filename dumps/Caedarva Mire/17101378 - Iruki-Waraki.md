# 17101378 - Iruki-Waraki

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Caedarva Mire (ID: 79) |
| Block Size       | 304 bytes              |
| Total Events     | 11                     |
| References Count | 32                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [15](#event-15)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     14 |              4 |
| [65535.3](#event-655353) | 0x001A       |     23 |              5 |
| [65535.4](#event-655354) | 0x0031       |      4 |              2 |
| [65535.5](#event-655355) | 0x0035       |     10 |              2 |
| [65535.6](#event-655356) | 0x003F       |     14 |              4 |
| [65535.7](#event-655357) | 0x004D       |     10 |              2 |
| [65535.8](#event-655358) | 0x0057       |     14 |              4 |
| [65535.9](#event-655359) | 0x0065       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x22B97     |      142231 |
|       1 | 0xFFF68EAB  |  4294348459 |
|       2 | 0x0000      |           0 |
|       3 | 0x063E      |        1598 |
|       4 | 0x0028      |          40 |
|       5 | 0x211A3     |      135587 |
|       6 | 0xFFF6755E  |  4294341982 |
|       7 | 0x017A      |         378 |
|       8 | 0x227EF     |      141295 |
|       9 | 0xFFF679E8  |  4294343144 |
|      10 | 0x0D55      |        3413 |
|      11 | 0x000D      |          13 |
|      12 | 0x22BC4     |      142276 |
|      13 | 0xFFF6808C  |  4294344844 |
|      14 | 0x0DAC      |        3500 |
|      15 | 0x760F5     |      483573 |
|      16 | 0x16F8E     |       94094 |
|      17 | 0xFFFF7B31  |  4294933297 |
|      18 | 0x065F      |        1631 |
|      19 | 0x73A04     |      473604 |
|      20 | 0x13397     |       78743 |
|      21 | 0xFFFF8395  |  4294935445 |
|      22 | 0x73C54     |      474196 |
|      23 | 0x13E6B     |       81515 |
|      24 | 0xFFFF8370  |  4294935408 |
|      25 | 0x0D19      |        3353 |
|      26 | 0x7426F     |      475759 |
|      27 | 0x14913     |       84243 |
|      28 | 0xFFFF82D3  |  4294935251 |
|      29 | 0x74345     |      475973 |
|      30 | 0x14AA4     |       84644 |
|      31 | 0xFFFF82A9  |  4294935209 |

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

### Event 15

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=142.231*, z=-618.837*, y=0.000*, direction=140.4°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 04 80 1F              2...
0010: 00 05 80 06 80 07 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=135.587*, Z=-625.314*, Y=0.378*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                37 08 80 09 80 02            7.....
0020: 80 0A 80 32 0B 80 1F 00  0C 80 0D 80 02 80 1F 01  ...2............
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=141.295*, z=-624.152*, y=0.000*, direction=300.0°*
  1: 0x0023 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=142.276*, Z=-622.452*, Y=0.000*
  3: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0031  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    39 0E 80 00                                     9...           
```

#### Opcodes

```
  0: 0x0031 [0x39] SET_ENTITY_DIRECTION(direction=19.2°*)
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                37 0F 80  10 80 11 80 12 80 00          7......... 
```

#### Opcodes

```
  0: 0x0035 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=483.573*, z=94.094*, y=-33.999*, direction=143.3°*
  1: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               32                 2
0040: 04 80 1F 00 13 80 14 80  15 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x003F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0042 [0x1F] MOVE_ENTITY: EventEntity moves to X=473.604*, Z=78.743*, Y=-31.851*
  2: 0x004A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         37 16 80               7..
0050: 17 80 18 80 19 80 00                              .......         
```

#### Opcodes

```
  0: 0x004D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=474.196*, z=81.515*, y=-31.888*, direction=294.7°*
  1: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      32  0B 80 1F 00 1A 80 1B 80         2........
0060: 1C 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0057 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=475.759*, Z=84.243*, Y=-32.045*
  2: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                32 0B 80  1F 00 1D 80 1E 80 1F 80       2..........
0070: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0065 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0068 [0x1F] MOVE_ENTITY: EventEntity moves to X=475.973*, Z=84.644*, Y=-32.087*
  2: 0x0070 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0072 [0x00] END_REQSTACK()
```
