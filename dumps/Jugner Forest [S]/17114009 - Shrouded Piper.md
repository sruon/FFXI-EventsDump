# 17114009 - Shrouded Piper

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 380 bytes                  |
| Total Events     | 12                         |
| References Count | 31                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [106](#event-106)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     29 |              9 |
| [65535.2](#event-655352) | 0x0025       |     29 |              3 |
| [65535.3](#event-655353) | 0x0042       |     23 |              7 |
| [65535.4](#event-655354) | 0x0059       |     18 |              6 |
| [65535.5](#event-655355) | 0x006B       |     14 |              4 |
| [107](#event-107)        | 0x0079       |      7 |              2 |
| [65535.6](#event-655356) | 0x0080       |     22 |              6 |
| [65535.7](#event-655357) | 0x0096       |      5 |              2 |
| [65535.8](#event-655358) | 0x009B       |     14 |              4 |
| [65535.9](#event-655359) | 0x00A9       |     23 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x1B25B     |      111195 |
|       2 | 0x6CF15     |      446229 |
|       3 | 0x068B      |        1675 |
|       4 | 0x003C      |          60 |
|       5 | 0x1B474     |      111732 |
|       6 | 0x6D033     |      446515 |
|       7 | 0x05B3      |        1459 |
|       8 | 0x0009      |           9 |
|       9 | 0x1B32D     |      111405 |
|      10 | 0x6CF84     |      446340 |
|      11 | 0x063B      |        1595 |
|      12 | 0x001E      |          30 |
|      13 | 0x0028      |          40 |
|      14 | 0x1A608     |      108040 |
|      15 | 0x6ABDC     |      437212 |
|      16 | 0x0ED3      |        3795 |
|      17 | 0x0005      |           5 |
|      18 | 0x1B1BF     |      111039 |
|      19 | 0x69E51     |      433745 |
|      20 | 0x086B      |        2155 |
|      21 | 0x19264     |      103012 |
|      22 | 0x6B716     |      440086 |
|      23 | 0x15EF      |        5615 |
|      24 | 0x0043      |          67 |
|      25 | 0x19192     |      102802 |
|      26 | 0x6B647     |      439879 |
|      27 | 0x160B      |        5643 |
|      28 | 0x191BE     |      102846 |
|      29 | 0x6B70B     |      440075 |
|      30 | 0x1604      |        5636 |

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

### Event 106

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
| Data Size    | 29 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 6F 1C 04  80 1F 00 05 80 06 80 07  .....o..........
0020: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=111.195*, Z=446.229*, Y=1.675*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0016 [0x1C] WAIT(60* ticks)
  5: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=111.732*, Z=446.515*, Y=1.459*
  6: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                66 08 80  99 23 05 01 99 23 05 01       f...#...#..
0030: 73 68 61 30 53 99 23 05  01 99 23 05 01 73 68 61  sha0S.#...#..sha
0040: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0025 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [Shrouded Piper (ID: 17114009/0x01052399), Shrouded Piper (ID: 17114009/0x01052399)], work=9*
  1: 0x0034 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [Shrouded Piper (ID: 17114009/0x01052399), Shrouded Piper (ID: 17114009/0x01052399)]
  2: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       32 00 80 1F 00 09  80 0A 80 0B 80 1F 01 6F    2............o
0050: 1E F0 FF FF 7F 1C 0C 80  00                       .........       
```

#### Opcodes

```
  0: 0x0042 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=111.405*, Z=446.340*, Y=1.595*
  2: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0050 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0055 [0x1C] WAIT(30* ticks)
  6: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 0D 80 1F 00 0E 80           2......
0060: 0F 80 10 80 1F 01 6F 1C  11 80 00                 ......o....     
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=108.040*, Z=437.212*, Y=3.795*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0067 [0x1C] WAIT(5* ticks)
  5: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   32 00 80 1F 00             2....
0070: 12 80 13 80 14 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x006B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006E [0x1F] MOVE_ENTITY: EventEntity moves to X=111.039*, Z=433.745*, Y=2.155*
  2: 0x0076 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0078 [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0079  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0079 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 32 00 80 1F 00 15 80 16  80 17 80 1F 01 1E F0 FF  2...............
0090: FF 7F 1C 0C 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0080 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0083 [0x1F] MOVE_ENTITY: EventEntity moves to X=103.012*, Z=440.086*, Y=5.615*
  2: 0x008B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008D [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0092 [0x1C] WAIT(30* ticks)
  5: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0096  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   B6 0A  18 80 00                       .....     
```

#### Opcodes

```
  0: 0x0096 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Ranged, value=67*)
  1: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   32 00 80 1F 00             2....
00A0: 19 80 1A 80 1B 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x009B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x009E [0x1F] MOVE_ENTITY: EventEntity moves to X=102.802*, Z=439.879*, Y=5.643*
  2: 0x00A6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             32 00 80 1F 00 1C 80           2......
00B0: 1D 80 1E 80 1F 01 6F 1E  F0 FF FF 7F 1C 0C 80 00  ......o.........
```

#### Opcodes

```
  0: 0x00A9 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00AC [0x1F] MOVE_ENTITY: EventEntity moves to X=102.846*, Z=440.075*, Y=5.636*
  2: 0x00B4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x00BC [0x1C] WAIT(30* ticks)
  6: 0x00BF [0x00] END_REQSTACK()
```
