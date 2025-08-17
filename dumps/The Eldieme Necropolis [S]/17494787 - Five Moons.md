# 17494787 - Five Moons

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 172 bytes                            |
| Total Events     | 6                                    |
| References Count | 13                                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [42](#event-42)          | 0x0001       |      1 |              1 |
| [43](#event-43)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     50 |             12 |
| [65535.2](#event-655352) | 0x0035       |      9 |              3 |
| [65535.3](#event-655353) | 0x003E       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000F      |          15 |
|       1 | 0x0023      |          35 |
|       2 | 0x4A652     |      304722 |
|       3 | 0x277E      |       10110 |
|       4 | 0xFFFF9494  |  4294939796 |
|       5 | 0x000D      |          13 |
|       6 | 0x4A6D1     |      304849 |
|       7 | 0x2A0D      |       10765 |
|       8 | 0x0005      |           5 |
|       9 | 0x0102      |         258 |
|      10 | 0x005A      |          90 |
|      11 | 0x4AAAC     |      305836 |
|      12 | 0x4534      |       17716 |

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

### Event 42

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

### Event 43

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
| Data Size    | 50 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          1C 00 80 32 01  80 1F 00 02 80 03 80 04     ...2.........
0010: 80 1F 01 32 05 80 1F 00  06 80 07 80 04 80 1F 01  ...2............
0020: 1E 04 F3 0A 01 1C 08 80  6E 03 F3 0A 01 09 80 99  ........n.......
0030: 03 F3 0A 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0003 [0x1C] WAIT(15* ticks)
  1: 0x0006 [0x32] ExtData[1]->MainSpeed = 35* * 0.1
  2: 0x0009 [0x1F] MOVE_ENTITY: EventEntity moves to X=304.722*, Z=10.110*, Y=-27.500*
  3: 0x0011 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0013 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x0016 [0x1F] MOVE_ENTITY: EventEntity moves to X=304.849*, Z=10.765*, Y=-27.500*
  6: 0x001E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0020 [0x1E] EventEntity looks at Herbert (ID: 17494788/0x010AF304) and starts talking
  8: 0x0025 [0x1C] WAIT(5* ticks)
  9: 0x0028 [0x6E] Five Moons (ID: 17494787/0x010AF303) uses emote 258*
 10: 0x002F [0x99] Wait for Five Moons (ID: 17494787/0x010AF303) animation to complete
 11: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0035  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1C 0A 80  1E 04 F3 0A 01 00             .........  
```

#### Opcodes

```
  0: 0x0035 [0x1C] WAIT(90* ticks)
  1: 0x0038 [0x1E] EventEntity looks at Herbert (ID: 17494788/0x010AF304) and starts talking
  2: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            32 05                2.
0040: 80 1F 00 0B 80 0C 80 04  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x003E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=305.836*, Z=17.716*, Y=-27.500*
  2: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004C [0x00] END_REQSTACK()
```
