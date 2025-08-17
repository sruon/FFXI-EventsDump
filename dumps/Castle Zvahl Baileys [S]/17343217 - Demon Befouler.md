# 17343217 - Demon Befouler

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 188 bytes                          |
| Total Events     | 10                                 |
| References Count | 15                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [2](#event-2)            | 0x0002       |      1 |              1 |
| [14](#event-14)          | 0x0003       |      1 |              1 |
| [3](#event-3)            | 0x0004       |      1 |              1 |
| [65535.1](#event-655351) | 0x0005       |     10 |              2 |
| [65535.2](#event-655352) | 0x000F       |     10 |              2 |
| [65535.3](#event-655353) | 0x0019       |     14 |              4 |
| [65535.4](#event-655354) | 0x0027       |     14 |              4 |
| [65535.5](#event-655355) | 0x0035       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFFFF194  |  4294963604 |
|       5 | 0xFFFFDB12  |  4294957842 |
|       6 | 0xFFFFD93D  |  4294957373 |
|       7 | 0x0044      |          68 |
|       8 | 0xFFFA54EE  |  4294595822 |
|       9 | 0x58C9      |       22729 |
|      10 | 0xFFFF6DBA  |  4294929850 |
|      11 | 0x00B4      |         180 |
|      12 | 0x214E2     |      136418 |
|      13 | 0x5015      |       20501 |
|      14 | 0xFFFFA233  |  4294943283 |

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

### Event 1

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

### Event 2

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

### Event 14

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

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                6C F1 A2  08 01 00 80 01 80 00          l......... 
```

#### Opcodes

```
  0: 0x0005 [0x6C] FADE_ENTITY_COLOR(entity_id=Demon Befouler (ID: 17343217/0x0108A2F1), end_alpha=0*, fade_time=1*)
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               6C                 l
0010: F1 A2 08 01 02 80 01 80  00                       .........       
```

#### Opcodes

```
  0: 0x000F [0x6C] FADE_ENTITY_COLOR(entity_id=Demon Befouler (ID: 17343217/0x0108A2F1), end_alpha=128*, fade_time=1*)
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 03 80 1F 00 04 80           2......
0020: 05 80 06 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=-3.692*, Z=-9.454*, Y=-9.923*
  2: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  07 80 1F 00 08 80 09 80         2........
0030: 0A 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 68* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=-371.474*, Z=22.729*, Y=-37.446*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1C 0B 80  32 07 80 1F 00 0C 80 0D       ...2.......
0040: 80 0E 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0035 [0x1C] WAIT(180* ticks)
  1: 0x0038 [0x32] ExtData[1]->MainSpeed = 68* * 0.1
  2: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=136.418*, Z=20.501*, Y=-24.013*
  3: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0045 [0x00] END_REQSTACK()
```
