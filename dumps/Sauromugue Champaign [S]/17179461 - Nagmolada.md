# 17179461 - Nagmolada

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 204 bytes                         |
| Total Events     | 7                                 |
| References Count | 15                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [5](#event-5)            | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     14 |              4 |
| [65535.2](#event-655352) | 0x0016       |     22 |              6 |
| [65535.3](#event-655353) | 0x002C       |     39 |              9 |
| [9](#event-9)            | 0x0053       |     11 |              3 |
| [65535.4](#event-655354) | 0x005E       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x6BE4      |       27620 |
|       2 | 0xFA3A      |       64058 |
|       3 | 0x07CB      |        1995 |
|       4 | 0x6AEF      |       27375 |
|       5 | 0x10117     |       65815 |
|       6 | 0x001E      |          30 |
|       7 | 0x674A      |       26442 |
|       8 | 0xFA44      |       64068 |
|       9 | 0x005A      |          90 |
|      10 | 0x57D5      |       22485 |
|      11 | 0xF9FE      |       63998 |
|      12 | 0x07CF      |        1999 |
|      13 | 0x0034      |          52 |
|      14 | 0x03D9      |         985 |

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

### Event 5

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
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=27.620*, Z=64.058*, Y=1.995*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   32 00  80 1F 00 04 80 05 80 03        2.........
0020: 80 1F 01 1E 44 23 06 01  1C 06 80 00              ....D#......    
```

#### Opcodes

```
  0: 0x0016 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=27.375*, Z=65.815*, Y=1.995*
  2: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0023 [0x1E] EventEntity looks at Brandolf (ID: 17179460/0x01062344) and starts talking
  4: 0x0028 [0x1C] WAIT(30* ticks)
  5: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 39 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      32 00 80 1F              2...
0030: 00 07 80 08 80 03 80 1F  01 1E 43 23 06 01 27 05  ..........C#..'.
0040: 43 23 06 01 02 1C 09 80  1F 00 0A 80 0B 80 0C 80  C#..............
0050: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x002C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=26.442*, Z=64.068*, Y=1.995*
  2: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0039 [0x1E] EventEntity looks at Unnamed NPC (ID: 17179459/0x01062343) and starts talking
  4: 0x003E [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17179459/0x01062343), tag_num=0x02)
  5: 0x0045 [0x1C] WAIT(90* ticks)
  6: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=22.485*, Z=63.998*, Y=1.999*
  7: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0052 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          92 01 F8 FF FF  7F B6 00 0D 80 00           ...........  
```

#### Opcodes

```
  0: 0x0053 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0059 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  2: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005E  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            B6 00                ..
0060: 0E 80 00                                          ...             
```

#### Opcodes

```
  0: 0x005E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=985*)
  1: 0x0062 [0x00] END_REQSTACK()
```
