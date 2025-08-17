# 17531174 - Neraf-Najiruf

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 280 bytes                        |
| Total Events     | 10                               |
| References Count | 27                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [22](#event-22)          | 0x000D       |     10 |              2 |
| [38](#event-38)          | 0x0017       |      1 |              1 |
| [39](#event-39)          | 0x0018       |      1 |              1 |
| [65535.1](#event-655351) | 0x0019       |     10 |              2 |
| [65535.2](#event-655352) | 0x0023       |     10 |              2 |
| [65535.3](#event-655353) | 0x002D       |     14 |              4 |
| [65535.4](#event-655354) | 0x003B       |     10 |              2 |
| [65535.5](#event-655355) | 0x0045       |     21 |              7 |
| [65535.6](#event-655356) | 0x005A       |     23 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2910E     |      168206 |
|       1 | 0xFFFFAC42  |  4294945858 |
|       2 | 0xFFFFB29F  |  4294947487 |
|       3 | 0x0F4F      |        3919 |
|       4 | 0x713DC     |      463836 |
|       5 | 0x1FDA5     |      130469 |
|       6 | 0x0007      |           7 |
|       7 | 0x0877      |        2167 |
|       8 | 0x70919     |      461081 |
|       9 | 0x1F191     |      127377 |
|      10 | 0x0000      |           0 |
|      11 | 0x043D      |        1085 |
|      12 | 0x0028      |          40 |
|      13 | 0x70AF7     |      461559 |
|      14 | 0x19C23     |      105507 |
|      15 | 0x0CB1      |        3249 |
|      16 | 0xFFFFFB50  |  4294966096 |
|      17 | 0xFFFE1B68  |  4294843240 |
|      18 | 0xFFFF6F45  |  4294930245 |
|      19 | 0x0B77      |        2935 |
|      20 | 0x003C      |          60 |
|      21 | 0x07AD      |        1965 |
|      22 | 0xFFFE4A5B  |  4294855259 |
|      23 | 0xFFFF7554  |  4294931796 |
|      24 | 0x000B      |          11 |
|      25 | 0x0639      |        1593 |
|      26 | 0xFFFE67C3  |  4294862787 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 01 F8 FF FF 7F 92 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=168.206*, z=-21.438*, y=-19.809*, direction=344.4°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      00                                  .        
```

#### Opcodes

```
  0: 0x0017 [0x00] END_REQSTACK()
```

### Event 39

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          00                               .       
```

#### Opcodes

```
  0: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             37 04 80 05 80 06 80           7......
0020: 07 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0019 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=463.836*, z=130.469*, y=0.007*, direction=190.5°*
  1: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          37 08 80 09 80  0A 80 0B 80 00              7.........   
```

#### Opcodes

```
  0: 0x0023 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=461.081*, z=127.377*, y=0.000*, direction=95.4°*
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 0C 80               2..
0030: 1F 00 0D 80 0E 80 0F 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=461.559*, Z=105.507*, Y=3.249*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   37 10 80 11 80             7....
0040: 12 80 13 80 00                                    .....           
```

#### Opcodes

```
  0: 0x003B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.200*, z=-124.056*, y=-37.051*, direction=258.0°*
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                1C 14 80  32 0C 80 1F 00 15 80 16       ...2.......
0050: 80 17 80 1F 01 6F 39 18  80 00                    .....o9...      
```

#### Opcodes

```
  0: 0x0045 [0x1C] WAIT(60* ticks)
  1: 0x0048 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=1.965*, Z=-112.037*, Y=-35.500*
  3: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0055 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0056 [0x39] SET_ENTITY_DIRECTION(direction=0.1°*)
  6: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                1C 14 80 32 0C 80            ...2..
0060: 1F 00 19 80 1A 80 17 80  1F 01 6F 1E 22 81 0B 01  ..........o."...
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x005A [0x1C] WAIT(60* ticks)
  1: 0x005D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.593*, Z=-104.509*, Y=-35.500*
  3: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x006A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x006B [0x1E] EventEntity looks at Wolfgang (ID: 17531170/0x010B8122) and starts talking
  6: 0x0070 [0x00] END_REQSTACK()
```
