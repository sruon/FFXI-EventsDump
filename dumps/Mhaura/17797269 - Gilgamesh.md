# 17797269 - Gilgamesh

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 168 bytes        |
| Total Events     | 7                |
| References Count | 14               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [368](#event-368)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [65535.2](#event-655352) | 0x0010       |     14 |              4 |
| [370](#event-370)        | 0x001E       |      1 |              1 |
| [65535.3](#event-655353) | 0x001F       |     22 |              6 |
| [65535.4](#event-655354) | 0x0035       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFF0BB3  |  4294904755 |
|       2 | 0x7E96      |       32406 |
|       3 | 0xFFFFA252  |  4294943314 |
|       4 | 0xFFFF6E56  |  4294930006 |
|       5 | 0xAFDE      |       45022 |
|       6 | 0xFFFFC180  |  4294951296 |
|       7 | 0xFFFEDA01  |  4294892033 |
|       8 | 0x7BDA      |       31706 |
|       9 | 0xFFFFA240  |  4294943296 |
|      10 | 0x001E      |          30 |
|      11 | 0xFFFEF63B  |  4294899259 |
|      12 | 0x7DB0      |       32176 |
|      13 | 0xFFFFA241  |  4294943297 |

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

### Event 368

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-62.541*, Z=32.406*, Y=-23.982*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 00 80 5A 00 04 80 05  80 06 80 5A 01 00        2..Z.......Z..  
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0013 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-37.290*, Z=45.022*, Y=-16.000*
  2: 0x001B [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x001D [0x00] END_REQSTACK()
```

### Event 370

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 00 80 1F 00 07 80 08 80  09 80 1F 01 1E F0 FF FF  ................
0030: 7F 1C 0A 80 00                                    .....           
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-75.263*, Z=31.706*, Y=-24.000*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0031 [0x1C] WAIT(30* ticks)
  5: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                32 00 80  1F 00 0B 80 0C 80 0D 80       2..........
0040: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0035 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=-68.037*, Z=32.176*, Y=-23.999*
  2: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0042 [0x00] END_REQSTACK()
```
