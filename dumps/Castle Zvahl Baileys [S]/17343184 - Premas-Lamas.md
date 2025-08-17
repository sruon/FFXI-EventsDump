# 17343184 - Premas-Lamas

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 272 bytes                          |
| Total Events     | 6                                  |
| References Count | 24                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [12](#event-12)          | 0x0001       |      7 |              2 |
| [13](#event-13)          | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     58 |             14 |
| [65535.2](#event-655352) | 0x0049       |     13 |              3 |
| [65535.3](#event-655353) | 0x0056       |     47 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x0015      |          21 |
|       2 | 0x0096      |         150 |
|       3 | 0x0028      |          40 |
|       4 | 0x4F344     |      324420 |
|       5 | 0xFFFFAC73  |  4294945907 |
|       6 | 0xFFFFC174  |  4294951284 |
|       7 | 0x4EB2A     |      322346 |
|       8 | 0xFFFFAA8B  |  4294945419 |
|       9 | 0xFFFFC178  |  4294951288 |
|      10 | 0x0008      |           8 |
|      11 | 0x002D      |          45 |
|      12 | 0x4A926     |      305446 |
|      13 | 0xFFFFB226  |  4294947366 |
|      14 | 0xFFFFC168  |  4294951272 |
|      15 | 0x49C6A     |      302186 |
|      16 | 0xFFFFB7E9  |  4294948841 |
|      17 | 0xFFFFC180  |  4294951296 |
|      18 | 0x49586     |      300422 |
|      19 | 0xFFFFC5DE  |  4294952414 |
|      20 | 0xFFFFC165  |  4294951269 |
|      21 | 0x492B3     |      299699 |
|      22 | 0x1009      |        4105 |
|      23 | 0xFFFFC17E  |  4294951294 |

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

### Event 12

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

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 58 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               1E                 .
0010: CB A2 08 01 1C 00 80 6E  D0 A2 08 01 01 80 99 D0  .......n........
0020: A2 08 01 1C 02 80 7B D0  A2 08 01 32 03 80 1F 00  ......{....2....
0030: 04 80 05 80 06 80 1F 01  1F 00 07 80 08 80 09 80  ................
0040: 1F 01 6F 1E CA A2 08 01  00                       ..o......       
```

#### Opcodes

```
  0: 0x000F [0x1E] EventEntity looks at Zeid (ID: 17343179/0x0108A2CB) and starts talking
  1: 0x0014 [0x1C] WAIT(60* ticks)
  2: 0x0017 [0x6E] Premas-Lamas (ID: 17343184/0x0108A2D0) uses emote 21*
  3: 0x001E [0x99] Wait for Premas-Lamas (ID: 17343184/0x0108A2D0) animation to complete
  4: 0x0023 [0x1C] WAIT(150* ticks)
  5: 0x0026 [0x7B] Premas-Lamas (ID: 17343184/0x0108A2D0) stops talking
  6: 0x002B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  7: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=324.420*, Z=-21.389*, Y=-16.012*
  8: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=322.346*, Z=-21.877*, Y=-16.008*
 10: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0042 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 12: 0x0043 [0x1E] EventEntity looks at Volker (ID: 17343178/0x0108A2CA) and starts talking
 13: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             6E D0 A2 08 01 0A 80           n......
0050: 99 D0 A2 08 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0049 [0x6E] Premas-Lamas (ID: 17343184/0x0108A2D0) uses emote 8*
  1: 0x0050 [0x99] Wait for Premas-Lamas (ID: 17343184/0x0108A2D0) animation to complete
  2: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   1C 0B  80 32 03 80 1F 00 0C 80        ...2......
0060: 0D 80 0E 80 1F 01 1F 00  0F 80 10 80 11 80 1F 01  ................
0070: 1F 00 12 80 13 80 14 80  1F 01 1F 00 15 80 16 80  ................
0080: 17 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0056 [0x1C] WAIT(45* ticks)
  1: 0x0059 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=305.446*, Z=-19.930*, Y=-16.024*
  3: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=302.186*, Z=-18.455*, Y=-16.000*
  5: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=300.422*, Z=-14.882*, Y=-16.027*
  7: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=299.699*, Z=4.105*, Y=-16.002*
  9: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x0084 [0x00] END_REQSTACK()
```
