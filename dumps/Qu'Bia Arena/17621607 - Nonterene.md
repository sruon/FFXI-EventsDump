# 17621607 - Nonterene

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qu'Bia Arena (ID: 206) |
| Block Size       | 232 bytes              |
| Total Events     | 7                      |
| References Count | 17                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32001](#event-32001)    | 0x0001       |     20 |              3 |
| [65535.1](#event-655351) | 0x0015       |     23 |              7 |
| [65535.2](#event-655352) | 0x002C       |     26 |              8 |
| [65535.3](#event-655353) | 0x0046       |     11 |              3 |
| [65535.4](#event-655354) | 0x0051       |     19 |              3 |
| [65535.5](#event-655355) | 0x0064       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF4E87  |  4294921863 |
|       1 | 0xFFFED3DE  |  4294890462 |
|       2 | 0xFFFF90AD  |  4294938797 |
|       3 | 0x0D4D      |        3405 |
|       4 | 0x0028      |          40 |
|       5 | 0x003C      |          60 |
|       6 | 0xFFFF6301  |  4294927105 |
|       7 | 0xFFFEF583  |  4294899075 |
|       8 | 0xFFFF90C7  |  4294938823 |
|       9 | 0x0078      |         120 |
|      10 | 0x000D      |          13 |
|      11 | 0xFFFF5D81  |  4294925697 |
|      12 | 0xFFFEF359  |  4294898521 |
|      13 | 0xFFFF90B8  |  4294938808 |
|      14 | 0x0109      |         265 |
|      15 | 0x001D      |          29 |
|      16 | 0x001E      |          30 |

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

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 79 00 F8 FF FF 7F   7........y.....
0010: 5C E2 0C 01 00                                    \....           
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-45.433*, z=-76.834*, y=-28.499*, direction=299.3°*
  1: 0x000A [0x79] EventEntity looks at Trion (ID: 17621596/0x010CE25C) (Basic look)
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 04 80  1C 05 80 1F 00 06 80 07       2..........
0020: 80 08 80 1F 01 6F 1E 5C  E2 0C 01 00              .....o.\....    
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0018 [0x1C] WAIT(60* ticks)
  2: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=-40.191*, Z=-68.221*, Y=-28.473*
  3: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0026 [0x1E] EventEntity looks at Trion (ID: 17621596/0x010CE25C) and starts talking
  6: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      1E 66 E2 0C              .f..
0030: 01 1C 09 80 32 0A 80 1F  00 0B 80 0C 80 0D 80 1F  ....2...........
0040: 01 6F 39 0E 80 00                                 .o9...          
```

#### Opcodes

```
  0: 0x002C [0x1E] EventEntity looks at Pieuje (ID: 17621606/0x010CE266) and starts talking
  1: 0x0031 [0x1C] WAIT(120* ticks)
  2: 0x0034 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=-41.599*, Z=-68.775*, Y=-28.488*
  4: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0042 [0x39] SET_ENTITY_DIRECTION(direction=1.5°*)
  7: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   1F 00  00 80 01 80 02 80 1F 01        ..........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=-45.433*, Z=-76.834*, Y=-28.499*
  1: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    66 0F 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0060: 1C 10 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0051 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0060 [0x1C] WAIT(30* ticks)
  2: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             66 0F 80 F8  FF FF 7F F8 FF FF 7F 74      f..........t
0070: 6C 6B 31 1C 10 80 00                              lk1....         
```

#### Opcodes

```
  0: 0x0064 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0073 [0x1C] WAIT(30* ticks)
  2: 0x0076 [0x00] END_REQSTACK()
```
