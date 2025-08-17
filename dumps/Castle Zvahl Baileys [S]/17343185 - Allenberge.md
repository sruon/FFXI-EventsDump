# 17343185 - Allenberge

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 212 bytes                          |
| Total Events     | 6                                  |
| References Count | 18                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [12](#event-12)          | 0x0001       |      7 |              2 |
| [13](#event-13)          | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     23 |              7 |
| [65535.2](#event-655352) | 0x0026       |     15 |              5 |
| [65535.3](#event-655353) | 0x0035       |     44 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x005A      |          90 |
|       1 | 0x000A      |          10 |
|       2 | 0x4EFBC     |      323516 |
|       3 | 0xFFFFB0E4  |  4294947044 |
|       4 | 0xFFFFC180  |  4294951296 |
|       5 | 0x0028      |          40 |
|       6 | 0x4E5F8     |      321016 |
|       7 | 0x4A926     |      305446 |
|       8 | 0xFFFFB226  |  4294947366 |
|       9 | 0xFFFFC168  |  4294951272 |
|      10 | 0x49C6A     |      302186 |
|      11 | 0xFFFFB7E9  |  4294948841 |
|      12 | 0x49586     |      300422 |
|      13 | 0xFFFFC5DE  |  4294952414 |
|      14 | 0xFFFFC165  |  4294951269 |
|      15 | 0x492B3     |      299699 |
|      16 | 0x1009      |        4105 |
|      17 | 0xFFFFC17E  |  4294951294 |

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
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               1E                 .
0010: CA A2 08 01 1C 00 80 32  01 80 1F 00 02 80 03 80  .......2........
0020: 04 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x000F [0x1E] EventEntity looks at Volker (ID: 17343178/0x0108A2CA) and starts talking
  1: 0x0014 [0x1C] WAIT(90* ticks)
  2: 0x0017 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  3: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=323.516*, Z=-20.252*, Y=-16.000*
  4: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   32 05  80 1F 00 06 80 03 80 04        2.........
0030: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0026 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0029 [0x1F] MOVE_ENTITY: EventEntity moves to X=321.016*, Z=-20.252*, Y=-16.000*
  2: 0x0031 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0033 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                32 05 80  1F 00 07 80 08 80 09 80       2..........
0040: 1F 01 1F 00 0A 80 0B 80  04 80 1F 01 1F 00 0C 80  ................
0050: 0D 80 0E 80 1F 01 1F 00  0F 80 10 80 11 80 1F 01  ................
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0035 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=305.446*, Z=-19.930*, Y=-16.024*
  2: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0042 [0x1F] MOVE_ENTITY: EventEntity moves to X=302.186*, Z=-18.455*, Y=-16.000*
  4: 0x004A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=300.422*, Z=-14.882*, Y=-16.027*
  6: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0056 [0x1F] MOVE_ENTITY: EventEntity moves to X=299.699*, Z=4.105*, Y=-16.002*
  8: 0x005E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0060 [0x00] END_REQSTACK()
```
