# 16994415 - Elisabeth

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 336 bytes        |
| Total Events     | 15               |
| References Count | 29               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [290](#event-290)          | 0x0001       |      1 |              1 |
| [291](#event-291)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     10 |              2 |
| [65535.2](#event-655352)   | 0x000D       |     14 |              4 |
| [65535.3](#event-655353)   | 0x001B       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0029       |     10 |              2 |
| [65535.5](#event-655355)   | 0x0033       |     19 |              5 |
| [65535.6](#event-655356)   | 0x0046       |     14 |              4 |
| [65535.7](#event-655357)   | 0x0054       |     10 |              2 |
| [65535.8](#event-655358)   | 0x005E       |      4 |              2 |
| [65535.9](#event-655359)   | 0x0062       |     11 |              3 |
| [65535.10](#event-6553510) | 0x006D       |     11 |              3 |
| [65535.11](#event-6553511) | 0x0078       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0082       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2E38      |       11832 |
|       1 | 0xFFFF7BC2  |  4294933442 |
|       2 | 0x0000      |           0 |
|       3 | 0x0B58      |        2904 |
|       4 | 0x000D      |          13 |
|       5 | 0x4300      |       17152 |
|       6 | 0xFFFF517D  |  4294922621 |
|       7 | 0x3B74      |       15220 |
|       8 | 0xFFFF4AFA  |  4294920954 |
|       9 | 0xFFFFDE75  |  4294958709 |
|      10 | 0xFFFF6116  |  4294926614 |
|      11 | 0x0DA8      |        3496 |
|      12 | 0xFFFFE5DF  |  4294960607 |
|      13 | 0xFFFF65CA  |  4294927818 |
|      14 | 0xFFFFBB75  |  4294949749 |
|      15 | 0xFFFF79FF  |  4294932991 |
|      16 | 0x305D      |       12381 |
|      17 | 0xFFFF55A1  |  4294923681 |
|      18 | 0x0150      |         336 |
|      19 | 0x00C8      |         200 |
|      20 | 0x1C5E      |        7262 |
|      21 | 0xFFFF64B1  |  4294927537 |
|      22 | 0x140A      |        5130 |
|      23 | 0xFFFF6EA3  |  4294930083 |
|      24 | 0x00EE      |         238 |
|      25 | 0xFFFF8535  |  4294935861 |
|      26 | 0x03FA      |        1018 |
|      27 | 0x04DA      |        1242 |
|      28 | 0xFFFF5994  |  4294924692 |

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

### Event 290

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

### Event 291

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 00              7.........   
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=11.832*, z=-33.854*, y=0.000*, direction=255.2°*
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         32 04 80               2..
0010: 1F 00 05 80 06 80 02 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x000D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.152*, Z=-44.675*, Y=0.000*
  2: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   32 04 80 1F 00             2....
0020: 07 80 08 80 02 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x001B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=15.220*, Z=-46.342*, Y=0.000*
  2: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             37 09 80 0A 80 02 80           7......
0030: 0B 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0029 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-8.587*, z=-40.682*, y=0.000*, direction=307.3°*
  1: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 04 80 1F 00  0C 80 0D 80 02 80 1F 01     2............
0040: 1E 6D 50 03 01 00                                 .mP...          
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-6.689*, Z=-39.478*, Y=0.000*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x1E] EventEntity looks at Yafahb (ID: 16994413/0x0103506D) and starts talking
  4: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 04  80 1F 00 0E 80 0F 80 02        2.........
0050: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=-17.547*, Z=-34.305*, Y=0.000*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             37 10 80 11  80 02 80 12 80 00            7.........  
```

#### Opcodes

```
  0: 0x0054 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=12.381*, z=-43.615*, y=0.000*, direction=29.5°*
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005E  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            1C 13                ..
0060: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x005E [0x1C] WAIT(200* ticks)
  1: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       1F 00 14 80 15 80  02 80 1F 01 00             ...........   
```

#### Opcodes

```
  0: 0x0062 [0x1F] MOVE_ENTITY: EventEntity moves to X=7.262*, Z=-39.759*, Y=0.000*
  1: 0x006A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         1F 00 16               ...
0070: 80 17 80 02 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=5.130*, Z=-37.213*, Y=0.000*
  1: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          37 18 80 19 80 02 80 1A          7.......
0080: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0078 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.238*, z=-31.435*, y=0.000*, direction=89.5°*
  1: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       1F 00 1B 80 1C 80  02 80 1F 01 00             ...........   
```

#### Opcodes

```
  0: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.242*, Z=-42.604*, Y=0.000*
  1: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x008C [0x00] END_REQSTACK()
```
