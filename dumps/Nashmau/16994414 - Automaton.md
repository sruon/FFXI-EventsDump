# 16994414 - Automaton

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 268 bytes        |
| Total Events     | 8                |
| References Count | 26               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [290](#event-290)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     19 |              5 |
| [65535.3](#event-655353) | 0x001F       |     24 |              6 |
| [65535.4](#event-655354) | 0x0037       |     23 |              5 |
| [65535.5](#event-655355) | 0x004E       |     23 |              5 |
| [65535.6](#event-655356) | 0x0065       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x6A70      |       27248 |
|       1 | 0xEC07      |       60423 |
|       2 | 0xFFFFE891  |  4294961297 |
|       3 | 0x0401      |        1025 |
|       4 | 0x000D      |          13 |
|       5 | 0x6843      |       26691 |
|       6 | 0xE589      |       58761 |
|       7 | 0x0028      |          40 |
|       8 | 0x6524      |       25892 |
|       9 | 0xF79C      |       63388 |
|      10 | 0xFFFFE890  |  4294961296 |
|      11 | 0x455C      |       17756 |
|      12 | 0x1125B     |       70235 |
|      13 | 0x04DC      |        1244 |
|      14 | 0xFFFFA088  |  4294942856 |
|      15 | 0x0000      |           0 |
|      16 | 0x0562      |        1378 |
|      17 | 0xFFFFF88E  |  4294965390 |
|      18 | 0xFFFF7AF4  |  4294933236 |
|      19 | 0xFFFFF631  |  4294964785 |
|      20 | 0xFFFF7628  |  4294932008 |
|      21 | 0x04B0      |        1200 |
|      22 | 0xFFFFE591  |  4294960529 |
|      23 | 0xFFFF6E27  |  4294929959 |
|      24 | 0xFFFFFC4A  |  4294966346 |
|      25 | 0xFFFF8481  |  4294935681 |

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
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=27.248*, z=60.423*, y=-5.999*, direction=90.1°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 04 80 1F              2...
0010: 00 05 80 06 80 02 80 1F  01 1E F0 FF FF 7F 00     ............... 
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=26.691*, Z=58.761*, Y=-5.999*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 07 80 1F 00 08 80 09 80  0A 80 1F 01 1F 00 0B 80  ................
0030: 0C 80 02 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=25.892*, Z=63.388*, Y=-6.000*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x1F] MOVE_ENTITY: EventEntity moves to X=17.756*, Z=70.235*, Y=-5.999*
  4: 0x0034 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      37  0D 80 0E 80 0F 80 10 80         7........
0040: 32 04 80 1F 00 11 80 12  80 0F 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0037 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.244*, z=-24.440*, y=0.000*, direction=121.1°*
  1: 0x0040 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.906*, Z=-34.060*, Y=0.000*
  3: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            37 13                7.
0050: 80 14 80 0F 80 15 80 32  04 80 1F 00 16 80 17 80  .......2........
0060: 0F 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x004E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-2.511*, z=-35.288*, y=0.000*, direction=105.5°*
  1: 0x0057 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=-6.767*, Z=-37.337*, Y=0.000*
  3: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                32 07 80  1F 00 18 80 19 80 0F 80       2..........
0070: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0065 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0068 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.950*, Z=-31.615*, Y=0.000*
  2: 0x0070 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0072 [0x00] END_REQSTACK()
```
