# 17113941 - Fingerfilcher Dradzad

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 216 bytes                  |
| Total Events     | 9                          |
| References Count | 20                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [200](#event-200)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     15 |              5 |
| [201](#event-201)        | 0x0011       |      1 |              1 |
| [202](#event-202)        | 0x0012       |      1 |              1 |
| [203](#event-203)        | 0x0013       |      1 |              1 |
| [65535.2](#event-655352) | 0x0014       |     28 |              6 |
| [65535.3](#event-655353) | 0x0030       |      4 |              2 |
| [65535.4](#event-655354) | 0x0034       |     29 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x11C45     |       72773 |
|       2 | 0x51F7C     |      335740 |
|       3 | 0x03A3      |         931 |
|       4 | 0x0028      |          40 |
|       5 | 0x124F5     |       74997 |
|       6 | 0x4D48E     |      316558 |
|       7 | 0x002F      |          47 |
|       8 | 0x0BF1      |        3057 |
|       9 | 0x11FE4     |       73700 |
|      10 | 0x51A69     |      334441 |
|      11 | 0x02F1      |         753 |
|      12 | 0x13A1A     |       80410 |
|      13 | 0x45489     |      283785 |
|      14 | 0xFFFFFFF5  |  4294967285 |
|      15 | 0x0762      |        1890 |
|      16 | 0x11B7C     |       72572 |
|      17 | 0x47863     |      292963 |
|      18 | 0x0269      |         617 |
|      19 | 0x0A39      |        2617 |

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

### Event 200

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
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=72.773*, Z=335.740*, Y=0.931*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x00] END_REQSTACK()
```

### Event 201

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    00                                              .              
```

#### Opcodes

```
  0: 0x0011 [0x00] END_REQSTACK()
```

### Event 202

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       00                                            .             
```

#### Opcodes

```
  0: 0x0012 [0x00] END_REQSTACK()
```

### Event 203

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          00                                          .            
```

#### Opcodes

```
  0: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             32 04 80 BA  55 23 05 01 05 80 06 80      2...U#......
0020: 07 80 08 80 1F 00 09 80  0A 80 0B 80 1F 01 6F 00  ..............o.
```

#### Opcodes

```
  0: 0x0014 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0017 [0xBA] SET_ENTITY_POSITION(entity_id=Fingerfilcher Dradzad (ID: 17113941/0x01052355), pos_x=74.997*, pos_z=316.558*, pos_y=0.047*, direction=268.7°*)
  2: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=73.700*, Z=334.441*, Y=0.753*
  3: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 32 00 80 00                                       2...            
```

#### Opcodes

```
  0: 0x0030 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 29 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             BA 55 23 05  01 0C 80 0D 80 0E 80 0F      .U#.........
0040: 80 32 04 80 31 00 10 80  11 80 12 80 13 80 31 01  .2..1.........1.
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0034 [0xBA] SET_ENTITY_POSITION(entity_id=Fingerfilcher Dradzad (ID: 17113941/0x01052355), pos_x=80.410*, pos_z=283.785*, pos_y=-0.011*, direction=166.1°*)
  1: 0x0041 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0044 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=72.572*, Z=292.963*, Y=0.617*, Time=2617*
  3: 0x004E [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  4: 0x0050 [0x00] END_REQSTACK()
```
