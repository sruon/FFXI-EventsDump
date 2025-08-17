# 17449537 - Rongelouts N Distaud

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Garlaige Citadel [S] (ID: 164) |
| Block Size       | 176 bytes                      |
| Total Events     | 7                              |
| References Count | 6                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [33](#event-33)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     35 |              9 |
| [65535.2](#event-655352) | 0x0025       |     35 |              9 |
| [65535.3](#event-655353) | 0x0048       |     10 |              2 |
| [65535.4](#event-655354) | 0x0052       |     10 |              2 |
| [65535.5](#event-655355) | 0x005C       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x000D      |          13 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0080      |         128 |
|       5 | 0x0002      |           2 |

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

### Event 33

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
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 25 10 03  02 00 27 10 03 01 00 26    ...%....'....&
0010: 10 03 03 00 28 10 32 00  80 1F 00 00 00 02 00 01  ....(.2.........
0020: 00 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0007 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x000C [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0011 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0016 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                03 00 00  25 10 03 02 00 27 10 03       ...%....'..
0030: 01 00 26 10 03 03 00 28  10 32 01 80 1F 00 00 00  ..&....(.2......
0040: 02 00 01 00 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0025 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x002A [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x002F [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0034 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0046 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          6C F8 FF FF 7F 02 80 03          l.......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0048 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       6C F8 FF FF 7F 04  80 03 80 00                l.........    
```

#### Opcodes

```
  0: 0x0052 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      6E F8 FF FF              n...
0060: 7F 05 80 99 F8 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x005C [0x6E] EventEntity uses emote 2*
  1: 0x0063 [0x99] Wait for EventEntity animation to complete
  2: 0x0068 [0x00] END_REQSTACK()
```
