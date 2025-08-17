# 17416322 - Five Moons

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Throne Room [S] (ID: 156) |
| Block Size       | 192 bytes                 |
| Total Events     | 7                         |
| References Count | 15                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [12](#event-12)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     14 |              4 |
| [32001](#event-32001)    | 0x0016       |      7 |              2 |
| [65535.2](#event-655352) | 0x001D       |     22 |              6 |
| [65535.3](#event-655353) | 0x0033       |     22 |              6 |
| [65535.4](#event-655354) | 0x0049       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFF93698  |  4294522520 |
|       2 | 0xFFFC5289  |  4294726281 |
|       3 | 0xFFFD72E1  |  4294800097 |
|       4 | 0xFFF91135  |  4294512949 |
|       5 | 0xFFFC8A5D  |  4294740573 |
|       6 | 0xFFFD7372  |  4294800242 |
|       7 | 0x001E      |          30 |
|       8 | 0xFFF9083F  |  4294510655 |
|       9 | 0xFFFC6274  |  4294730356 |
|      10 | 0xFFFD7378  |  4294800248 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFF967D1  |  4294535121 |
|      13 | 0xFFFC5738  |  4294727480 |
|      14 | 0xFFFD7343  |  4294800195 |

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

### Event 12

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-444.776*, Z=-241.015*, Y=-167.199*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0016 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         32 00 80               2..
0020: 1F 00 04 80 05 80 06 80  1F 01 1E 7F C0 09 01 1C  ................
0030: 07 80 00                                          ...             
```

#### Opcodes

```
  0: 0x001D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=-454.347*, Z=-226.723*, Y=-167.054*
  2: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002A [0x1E] EventEntity looks at Volker (ID: 17416319/0x0109C07F) and starts talking
  4: 0x002F [0x1C] WAIT(30* ticks)
  5: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 00 80 1F 00  08 80 09 80 0A 80 1F 01     2............
0040: 1E 83 C0 09 01 1C 07 80  00                       .........       
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-456.641*, Z=-236.940*, Y=-167.048*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x1E] EventEntity looks at Klara (ID: 17416323/0x0109C083) and starts talking
  4: 0x0045 [0x1C] WAIT(30* ticks)
  5: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             32 0B 80 1F 00 0C 80           2......
0050: 0D 80 0E 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0049 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=-432.175*, Z=-239.816*, Y=-167.101*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x00] END_REQSTACK()
```
