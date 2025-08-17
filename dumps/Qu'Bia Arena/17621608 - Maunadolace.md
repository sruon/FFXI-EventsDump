# 17621608 - Maunadolace

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qu'Bia Arena (ID: 206) |
| Block Size       | 224 bytes              |
| Total Events     | 7                      |
| References Count | 16                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32001](#event-32001)    | 0x0001       |     20 |              3 |
| [65535.1](#event-655351) | 0x0015       |     20 |              6 |
| [65535.2](#event-655352) | 0x0029       |     26 |              8 |
| [65535.3](#event-655353) | 0x0043       |     11 |              3 |
| [65535.4](#event-655354) | 0x004E       |     19 |              3 |
| [65535.5](#event-655355) | 0x0061       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF592F  |  4294924591 |
|       1 | 0xFFFED8FD  |  4294891773 |
|       2 | 0xFFFF90AD  |  4294938797 |
|       3 | 0x0D47      |        3399 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFF66F5  |  4294928117 |
|       6 | 0xFFFEF071  |  4294897777 |
|       7 | 0xFFFF90BF  |  4294938815 |
|       8 | 0x0078      |         120 |
|       9 | 0x000D      |          13 |
|      10 | 0xFFFF68ED  |  4294928621 |
|      11 | 0xFFFEEDA9  |  4294897065 |
|      12 | 0xFFFF90BA  |  4294938810 |
|      13 | 0x090D      |        2317 |
|      14 | 0x001D      |          29 |
|      15 | 0x001E      |          30 |

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-42.705*, z=-75.523*, y=-28.499*, direction=298.7°*
  1: 0x000A [0x79] EventEntity looks at Trion (ID: 17621596/0x010CE25C) (Basic look)
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 04 80  1F 00 05 80 06 80 07 80       2..........
0020: 1F 01 6F 1E 5C E2 0C 01  00                       ..o.\....       
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=-39.179*, Z=-69.519*, Y=-28.481*
  2: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0023 [0x1E] EventEntity looks at Trion (ID: 17621596/0x010CE25C) and starts talking
  5: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1E 66 E2 0C 01 1C 08           .f.....
0030: 80 32 09 80 1F 00 0A 80  0B 80 0C 80 1F 01 6F 39  .2............o9
0040: 0D 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0029 [0x1E] EventEntity looks at Pieuje (ID: 17621606/0x010CE266) and starts talking
  1: 0x002E [0x1C] WAIT(120* ticks)
  2: 0x0031 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=-38.675*, Z=-70.231*, Y=-28.486*
  4: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x003F [0x39] SET_ENTITY_DIRECTION(direction=12.7°*)
  7: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          1F 00 00 80 01  80 02 80 1F 01 00           ...........  
```

#### Opcodes

```
  0: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.705*, Z=-75.523*, Y=-28.499*
  1: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            66 0E                f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1C 0F 80  .........tlk0...
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x005D [0x1C] WAIT(30* ticks)
  2: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    66 0E 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31   f..........tlk1
0070: 1C 0F 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0061 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0070 [0x1C] WAIT(30* ticks)
  2: 0x0073 [0x00] END_REQSTACK()
```
