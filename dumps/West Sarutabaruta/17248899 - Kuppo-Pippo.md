# 17248899 - Kuppo-Pippo

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 208 bytes                   |
| Total Events     | 9                           |
| References Count | 16                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      5 |              2 |
| [65535.2](#event-655352) | 0x0006       |      5 |              2 |
| [65535.3](#event-655353) | 0x000B       |     24 |              6 |
| [65535.4](#event-655354) | 0x0023       |     14 |              4 |
| [65535.5](#event-655355) | 0x0031       |      5 |              2 |
| [65535.6](#event-655356) | 0x0036       |      5 |              2 |
| [65535.7](#event-655357) | 0x003B       |     19 |              3 |
| [65535.8](#event-655358) | 0x004E       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00A6      |         166 |
|       1 | 0x0018      |          24 |
|       2 | 0x1EF2      |        7922 |
|       3 | 0x51BC      |       20924 |
|       4 | 0xFFFFFC18  |  4294966296 |
|       5 | 0x0009      |           9 |
|       6 | 0xFFFFF5D6  |  4294964694 |
|       7 | 0x6BC2      |       27586 |
|       8 | 0x00AC      |         172 |
|       9 | 0x1987      |        6535 |
|      10 | 0x552E      |       21806 |
|      11 | 0xFFFFFC19  |  4294966297 |
|      12 | 0x0A20      |        2592 |
|      13 | 0x000F      |          15 |
|      14 | 0xFFFFFA3D  |  4294965821 |
|      15 | 0x6478      |       25720 |

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
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 00 00 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=166*)
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   B6 00  00 80 00                       .....     
```

#### Opcodes

```
  0: 0x0006 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=166*)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 01 80 1F 00             2....
0010: 02 80 03 80 04 80 1F 01  6F 4A 83 32 07 01 81 32  ........oJ.2...2
0020: 07 01 00                                          ...             
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 24* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=7.922*, Z=20.924*, Y=-1.000*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x4A] Kuppo-Pippo (ID: 17248899/0x01073283) looks at Khoto Rokkorah (ID: 17248897/0x01073281)
  5: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          32 05 80 1F 00  06 80 07 80 04 80 1F 01     2............
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0023 [0x32] ExtData[1]->MainSpeed = 9* * 0.1
  1: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.602*, Z=27.586*, Y=-1.000*
  2: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0031  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    B6 00 08 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0031 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=172*)
  1: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0036  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   B6 00  08 80 00                       .....     
```

#### Opcodes

```
  0: 0x0036 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=172*)
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   37 09 80 0A 80             7....
0040: 0B 80 0C 80 4A 83 32 07  01 81 32 07 01 00        ....J.2...2...  
```

#### Opcodes

```
  0: 0x003B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=6.535*, z=21.806*, y=-0.999*, direction=227.8°*
  1: 0x0044 [0x4A] Kuppo-Pippo (ID: 17248899/0x01073283) looks at Khoto Rokkorah (ID: 17248897/0x01073281)
  2: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            32 0D                2.
0050: 80 1F 00 0E 80 0F 80 04  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x004E [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.475*, Z=25.720*, Y=-1.000*
  2: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005B [0x00] END_REQSTACK()
```
