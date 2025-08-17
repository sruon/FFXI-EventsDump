# 16888125 - Fardimant

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Phomiuna Aqueducts (ID: 27) |
| Block Size       | 196 bytes                   |
| Total Events     | 6                           |
| References Count | 16                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [38](#event-38)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     27 |              6 |
| [65535.2](#event-655352) | 0x0026       |     17 |              5 |
| [65535.3](#event-655353) | 0x0037       |     20 |              6 |
| [65535.4](#event-655354) | 0x004B       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFC4CEC  |  4294724844 |
|       1 | 0x4F40      |       20288 |
|       2 | 0xFFFFE884  |  4294961284 |
|       3 | 0x0FE9      |        4073 |
|       4 | 0x000D      |          13 |
|       5 | 0x003C      |          60 |
|       6 | 0xFFFC8A77  |  4294740599 |
|       7 | 0x4ECD      |       20173 |
|       8 | 0xFFFFE891  |  4294961297 |
|       9 | 0xFFFC97B3  |  4294743987 |
|      10 | 0x519D      |       20893 |
|      11 | 0xFFFC8C87  |  4294741127 |
|      12 | 0x4EBF      |       20159 |
|      13 | 0xFFFC4EDD  |  4294725341 |
|      14 | 0x4E73      |       20083 |
|      15 | 0xFFFFE877  |  4294961271 |

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

### Event 38

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-242.452*, z=20.288*, y=-6.012*, direction=358.0°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 27 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 79 00             2..y.
0010: 3D B1 01 01 F0 FF FF 7F  1C 05 80 1F 00 06 80 07  =...............
0020: 80 08 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x79] Fardimant (ID: 16888125/0x0101B13D) looks at LocalPlayer (Basic look)
  2: 0x0018 [0x1C] WAIT(60* ticks)
  3: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=-226.697*, Z=20.173*, Y=-5.999*
  4: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   32 04  80 1C 05 80 1F 00 09 80        2.........
0030: 0A 80 08 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0026 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0029 [0x1C] WAIT(60* ticks)
  2: 0x002C [0x1F] MOVE_ENTITY: EventEntity moves to X=-223.309*, Z=20.893*, Y=-5.999*
  3: 0x0034 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  04 80 1C 05 80 1F 00 0B         2........
0040: 80 0C 80 08 80 1F 01 1C  05 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003A [0x1C] WAIT(60* ticks)
  2: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=-226.169*, Z=20.159*, Y=-5.999*
  3: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0047 [0x1C] WAIT(60* ticks)
  5: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   32 04 80 1C 05             2....
0050: 80 1F 00 0D 80 0E 80 0F  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x004B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004E [0x1C] WAIT(60* ticks)
  2: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=-241.955*, Z=20.083*, Y=-6.025*
  3: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005B [0x00] END_REQSTACK()
```
