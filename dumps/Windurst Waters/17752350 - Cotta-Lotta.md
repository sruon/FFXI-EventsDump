# 17752350 - Cotta-Lotta

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 184 bytes                 |
| Total Events     | 8                         |
| References Count | 13                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [989](#event-989)        | 0x0001       |      1 |              1 |
| [1016](#event-1016)      | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     24 |              6 |
| [65535.2](#event-655352) | 0x001B       |     14 |              4 |
| [991](#event-991)        | 0x0029       |      1 |              1 |
| [65535.3](#event-655353) | 0x002A       |     19 |              3 |
| [65535.4](#event-655354) | 0x003D       |     20 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000F      |          15 |
|       1 | 0x1987      |        6535 |
|       2 | 0x552E      |       21806 |
|       3 | 0xFFFFFC19  |  4294966297 |
|       4 | 0x0007      |           7 |
|       5 | 0x0364      |         868 |
|       6 | 0x793E      |       31038 |
|       7 | 0xFFFFFC18  |  4294966296 |
|       8 | 0x1FDE      |        8158 |
|       9 | 0x5A1D      |       23069 |
|      10 | 0x0D5C      |        3420 |
|      11 | 0x1444      |        5188 |
|      12 | 0x5291      |       21137 |

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

### Event 989

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

### Event 1016

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
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 4A 1E E1 0E 01 19 E1  0E 01 00                 oJ.........     
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=6.535*, Z=21.806*, Y=-0.999*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x4A] Cotta-Lotta (ID: 17752350/0x010EE11E) looks at Khoto Rokkorah (ID: 17752345/0x010EE119)
  5: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

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
0020: 05 80 06 80 07 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x001B [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  1: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=0.868*, Z=31.038*, Y=-1.000*
  2: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0028 [0x00] END_REQSTACK()
```

### Event 991

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                37 08 80 09 80 07            7.....
0030: 80 0A 80 4A 1E E1 0E 01  19 E1 0E 01 00           ...J.........   
```

#### Opcodes

```
  0: 0x002A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=8.158*, z=23.069*, y=-1.000*, direction=300.6°*
  1: 0x0033 [0x4A] Cotta-Lotta (ID: 17752350/0x010EE11E) looks at Khoto Rokkorah (ID: 17752345/0x010EE119)
  2: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         32 00 80               2..
0040: 1F 00 0B 80 0C 80 07 80  1F 01 6F 1E 1F E1 0E 01  ..........o.....
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x003D [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=5.188*, Z=21.137*, Y=-1.000*
  2: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004B [0x1E] EventEntity looks at Tacca-Picca (ID: 17752351/0x010EE11F) and starts talking
  5: 0x0050 [0x00] END_REQSTACK()
```
