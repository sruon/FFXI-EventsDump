# 17723815 - Lilisette

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 192 bytes                     |
| Total Events     | 7                             |
| References Count | 16                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [870](#event-870)        | 0x0000       |      1 |              1 |
| [65535](#event-65535)    | 0x0001       |     14 |              4 |
| [65535.1](#event-655351) | 0x000F       |     14 |              4 |
| [65535.2](#event-655352) | 0x001D       |     24 |              6 |
| [65535.3](#event-655353) | 0x0035       |     14 |              4 |
| [65535.4](#event-655354) | 0x0043       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x21A9F     |      137887 |
|       2 | 0x1FB08     |      129800 |
|       3 | 0x0000      |           0 |
|       4 | 0x1B5C2     |      112066 |
|       5 | 0x19587     |      103815 |
|       6 | 0x1A140     |      106816 |
|       7 | 0x18169     |       98665 |
|       8 | 0x195BC     |      103868 |
|       9 | 0x1752C     |       95532 |
|      10 | 0x06D5      |        1749 |
|      11 | 0x0028      |          40 |
|      12 | 0x15BC2     |       89026 |
|      13 | 0x13A27     |       80423 |
|      14 | 0xE5B2      |       58802 |
|      15 | 0xC443      |       50243 |

## Events

### Event 870

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

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    32 00 80 1F 00 01 80  02 80 03 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0001 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0004 [0x1F] MOVE_ENTITY: EventEntity moves to X=137.887*, Z=129.800*, Y=0.000*
  2: 0x000C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 04 80 05 80  03 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=112.066*, Z=103.815*, Y=0.000*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         32 00 80               2..
0020: 1F 00 06 80 07 80 03 80  1F 01 1F 00 08 80 09 80  ................
0030: 0A 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x001D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=106.816*, Z=98.665*, Y=0.000*
  2: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=103.868*, Z=95.532*, Y=1.749*
  4: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                32 0B 80  1F 00 0C 80 0D 80 0A 80       2..........
0040: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0035 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=89.026*, Z=80.423*, Y=1.749*
  2: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          32 0B 80 1F 00  0E 80 0F 80 03 80 1F 01     2............
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0043 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=58.802*, Z=50.243*, Y=0.000*
  2: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0050 [0x00] END_REQSTACK()
```
