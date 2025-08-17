# 17134064 - Pale Eagle

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 300 bytes                   |
| Total Events     | 10                          |
| References Count | 24                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [120](#event-120)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     17 |              5 |
| [65535.2](#event-655352) | 0x0019       |     17 |              5 |
| [34](#event-34)          | 0x002A       |      1 |              1 |
| [65535.3](#event-655353) | 0x002B       |     22 |              6 |
| [65535.4](#event-655354) | 0x0041       |     15 |              5 |
| [65535.5](#event-655355) | 0x0050       |     29 |              7 |
| [65535.6](#event-655356) | 0x006D       |     14 |              4 |
| [65535.7](#event-655357) | 0x007B       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFC99E8  |  4294744552 |
|       2 | 0xFFFE6D1B  |  4294864155 |
|       3 | 0xFFFFE891  |  4294961297 |
|       4 | 0x001E      |          30 |
|       5 | 0xFFFD191F  |  4294777119 |
|       6 | 0xFFFE96AF  |  4294874799 |
|       7 | 0x141C7     |       82375 |
|       8 | 0xFFFFFDE1  |  4294966753 |
|       9 | 0xFFFFB3B4  |  4294947764 |
|      10 | 0x14523     |       83235 |
|      11 | 0xFFFFFF51  |  4294967121 |
|      12 | 0x15B5A     |       88922 |
|      13 | 0x21A1      |        8609 |
|      14 | 0xFFFFB136  |  4294947126 |
|      15 | 0x1600E     |       90126 |
|      16 | 0x2524      |        9508 |
|      17 | 0x15C16     |       89110 |
|      18 | 0x21E5      |        8677 |
|      19 | 0x15A48     |       88648 |
|      20 | 0x1F74      |        8052 |
|      21 | 0x15A58     |       88664 |
|      22 | 0x1441      |        5185 |
|      23 | 0xFFFFB138  |  4294947128 |

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

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 1C 04 80  00                       .........       
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-222.744*, Z=-103.141*, Y=-5.999*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x1C] WAIT(30* ticks)
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 00 80 1F 00 05 80           2......
0020: 06 80 03 80 1F 01 1C 04  80 00                    ..........      
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=-190.177*, Z=-92.497*, Y=-5.999*
  2: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0026 [0x1C] WAIT(30* ticks)
  4: 0x0029 [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                00                           .     
```

#### Opcodes

```
  0: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   32 00 80 1F 00             2....
0030: 07 80 08 80 09 80 1F 01  1E B4 71 05 01 1C 04 80  ..........q.....
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=82.375*, Z=-0.543*, Y=-19.532*
  2: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0038 [0x1E] EventEntity looks at Volker (ID: 17134004/0x010571B4) and starts talking
  4: 0x003D [0x1C] WAIT(30* ticks)
  5: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    32 00 80 1F 00 0A 80  0B 80 09 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0041 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=83.235*, Z=-0.175*, Y=-19.532*
  2: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 00 80 1F 00 0C 80 0D  80 0E 80 1F 01 1F 00 0F  2...............
0060: 80 10 80 0E 80 1F 01 1E  F1 71 05 01 00           .........q...   
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=88.922*, Z=8.609*, Y=-20.170*
  2: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=90.126*, Z=9.508*, Y=-20.170*
  4: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0067 [0x1E] EventEntity looks at Prien (ID: 17134065/0x010571F1) and starts talking
  6: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         32 00 80               2..
0070: 1F 00 11 80 12 80 0E 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x006D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=89.110*, Z=8.677*, Y=-20.170*
  2: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   32 00 80 1F 00             2....
0080: 13 80 14 80 0E 80 1F 01  1F 00 15 80 16 80 17 80  ................
0090: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x007B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007E [0x1F] MOVE_ENTITY: EventEntity moves to X=88.648*, Z=8.052*, Y=-20.170*
  2: 0x0086 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0088 [0x1F] MOVE_ENTITY: EventEntity moves to X=88.664*, Z=5.185*, Y=-20.168*
  4: 0x0090 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0092 [0x00] END_REQSTACK()
```
