# 17056432 - Mihli Aliapoh

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Aydeewa Subterrane (ID: 68) |
| Block Size       | 304 bytes                   |
| Total Events     | 10                          |
| References Count | 27                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [34](#event-34)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     10 |              2 |
| [65535.3](#event-655353) | 0x0016       |     15 |              5 |
| [65535.4](#event-655354) | 0x0025       |     15 |              5 |
| [65535.5](#event-655355) | 0x0034       |     15 |              5 |
| [65535.6](#event-655356) | 0x0043       |     15 |              5 |
| [65535.7](#event-655357) | 0x0052       |     35 |              9 |
| [65535.8](#event-655358) | 0x0075       |     20 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0080      |         128 |
|       2 | 0x001E      |          30 |
|       3 | 0x000D      |          13 |
|       4 | 0x53BB6     |      342966 |
|       5 | 0x5A145     |      368965 |
|       6 | 0x06FD      |        1789 |
|       7 | 0x51EC6     |      335558 |
|       8 | 0x5B66E     |      374382 |
|       9 | 0x0672      |        1650 |
|      10 | 0x000B      |          11 |
|      11 | 0x532E1     |      340705 |
|      12 | 0x5AD37     |      372023 |
|      13 | 0x0663      |        1635 |
|      14 | 0x0026      |          38 |
|      15 | 0x50D74     |      331124 |
|      16 | 0x5B31B     |      373531 |
|      17 | 0x06F2      |        1778 |
|      18 | 0x0028      |          40 |
|      19 | 0x546DE     |      345822 |
|      20 | 0x5A235     |      369205 |
|      21 | 0x072E      |        1838 |
|      22 | 0x000F      |          15 |
|      23 | 0x0004      |           4 |
|      24 | 0x5589D     |      350365 |
|      25 | 0x58224     |      360996 |
|      26 | 0x06F6      |        1782 |

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

### Event 34

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
0000:       6C B0 42 04 01 00  80 00 80 00                l.B.......    
```

#### Opcodes

```
  0: 0x0002 [0x6C] FADE_ENTITY_COLOR(entity_id=Mihli Aliapoh (ID: 17056432/0x010442B0), end_alpha=0*, fade_time=0*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      6C B0 42 04              l.B.
0010: 01 01 80 02 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000C [0x6C] FADE_ENTITY_COLOR(entity_id=Mihli Aliapoh (ID: 17056432/0x010442B0), end_alpha=128*, fade_time=30*)
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   32 03  80 1F 00 04 80 05 80 06        2.........
0020: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0016 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=342.966*, Z=368.965*, Y=1.789*
  2: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 03 80  1F 00 07 80 08 80 09 80       2..........
0030: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=335.558*, Z=374.382*, Y=1.650*
  2: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             32 0A 80 1F  00 0B 80 0C 80 0D 80 1F      2...........
0040: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0034 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=340.705*, Z=372.023*, Y=1.635*
  2: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          32 0E 80 1F 00  0F 80 10 80 11 80 1F 01     2............
0050: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0043 [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=331.124*, Z=373.531*, Y=1.778*
  2: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0050 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       32 12 80 1F 00 13  80 14 80 15 80 1F 01 6F    2............o
0060: 1E F0 FF FF 7F 1C 16 80  6E F8 FF FF 7F 17 80 99  ........n.......
0070: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0052 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=345.822*, Z=369.205*, Y=1.838*
  2: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0060 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0065 [0x1C] WAIT(15* ticks)
  6: 0x0068 [0x6E] EventEntity uses emote 4*
  7: 0x006F [0x99] Wait for EventEntity animation to complete
  8: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                32 0E 80  1F 00 18 80 19 80 1A 80       2..........
0080: 1F 01 6F 1E F0 FF FF 7F  00                       ..o......       
```

#### Opcodes

```
  0: 0x0075 [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x0078 [0x1F] MOVE_ENTITY: EventEntity moves to X=350.365*, Z=360.996*, Y=1.782*
  2: 0x0080 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0082 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0083 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0088 [0x00] END_REQSTACK()
```
