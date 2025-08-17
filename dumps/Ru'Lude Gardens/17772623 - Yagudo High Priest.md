# 17772623 - Yagudo High Priest

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 128 bytes                 |
| Total Events     | 7                         |
| References Count | 9                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [10010](#event-10010)    | 0x0002       |      1 |              1 |
| [65535.2](#event-655352) | 0x0003       |      1 |              1 |
| [65535.3](#event-655353) | 0x0004       |     16 |              3 |
| [65535.4](#event-655354) | 0x0014       |     14 |              4 |
| [65535.5](#event-655355) | 0x0022       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE4DE6  |  4294856166 |
|       1 | 0x1896E     |      100718 |
|       2 | 0xFFFEE6C0  |  4294895296 |
|       3 | 0x0BB8      |        3000 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFE44C8  |  4294853832 |
|       6 | 0x18E73     |      102003 |
|       7 | 0xFFFE728B  |  4294865547 |
|       8 | 0x173AD     |       95149 |

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

### Event 65535.1

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

### Event 10010

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

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             37 00 80 01  80 02 80 03 80 4E 00 4F      7........N.O
0010: 30 0F 01 00                                       0...            
```

#### Opcodes

```
  0: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-111.130*, z=100.718*, y=-72.000*, direction=263.7°*
  1: 0x000D [0x4E] SET_ENTITY_HIDE_FLAG: Show Yagudo High Priest (ID: 17772623/0x010F304F)
  2: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             32 04 80 1F  00 05 80 06 80 02 80 1F      2...........
0020: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0014 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0017 [0x1F] MOVE_ENTITY: EventEntity moves to X=-113.464*, Z=102.003*, Y=-72.000*
  2: 0x001F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       32 04 80 1F 00 07  80 08 80 02 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0022 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=-101.749*, Z=95.149*, Y=-72.000*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x00] END_REQSTACK()
```
