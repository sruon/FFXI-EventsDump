# 17399857 - Tzee Xicu the Manifest

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Altar Room (ID: 152) |
| Block Size       | 172 bytes            |
| Total Events     | 6                    |
| References Count | 16                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [49](#event-49)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     15 |              5 |
| [50](#event-50)          | 0x001A       |     10 |              2 |
| [65535.2](#event-655352) | 0x0024       |     15 |              5 |
| [65535.3](#event-655353) | 0x0033       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFB122A  |  4294644266 |
|       1 | 0x14E1      |        5345 |
|       2 | 0x5C78      |       23672 |
|       3 | 0x0DAC      |        3500 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFB1C53  |  4294646867 |
|       6 | 0x17F3      |        6131 |
|       7 | 0x5DBF      |       23999 |
|       8 | 0xFFFB1A84  |  4294646404 |
|       9 | 0x15CA      |        5578 |
|      10 | 0x0C77      |        3191 |
|      11 | 0xFFFB2387  |  4294648711 |
|      12 | 0x186D      |        6253 |
|      13 | 0xFFFAF9E2  |  4294638050 |
|      14 | 0x0360      |         864 |
|      15 | 0x5EDE      |       24286 |

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

### Event 49

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-323.030*, z=5.345*, y=23.672*, direction=307.6°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-320.429*, Z=6.131*, Y=23.999*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                37 08 80 09 80 07            7.....
0020: 80 0A 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-320.892*, z=5.578*, y=23.999*, direction=280.5°*
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 04 80 1F  00 0B 80 0C 80 07 80 1F      2...........
0030: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-318.585*, Z=6.253*, Y=23.999*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 04 80 1F 00  0D 80 0E 80 0F 80 1F 01     2............
0040: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-329.246*, Z=0.864*, Y=24.286*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0041 [0x00] END_REQSTACK()
```
