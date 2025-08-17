# 17449505 - Laurimaux

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Garlaige Citadel [S] (ID: 164) |
| Block Size       | 364 bytes                      |
| Total Events     | 12                             |
| References Count | 18                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [20](#event-20)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     35 |              9 |
| [65535.2](#event-655352) | 0x0025       |     35 |              9 |
| [33](#event-33)          | 0x0048       |      1 |              1 |
| [65535.3](#event-655353) | 0x0049       |     21 |              2 |
| [65535.4](#event-655354) | 0x005E       |     21 |              2 |
| [65535.5](#event-655355) | 0x0073       |     21 |              2 |
| [65535.6](#event-655356) | 0x0088       |     13 |              3 |
| [65535.7](#event-655357) | 0x0095       |     13 |              3 |
| [65535.8](#event-655358) | 0x00A2       |     15 |              5 |
| [65535.9](#event-655359) | 0x00B1       |     50 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x000D      |          13 |
|       2 | 0x0004      |           4 |
|       3 | 0x0008      |           8 |
|       4 | 0x000C      |          12 |
|       5 | 0x00FB      |         251 |
|       6 | 0x001B      |          27 |
|       7 | 0x007C      |         124 |
|       8 | 0x0015      |          21 |
|       9 | 0x0000      |           0 |
|      10 | 0x0003      |           3 |
|      11 | 0x0038      |          56 |
|      12 | 0x010E      |         270 |
|      13 | 0x002B      |          43 |
|      14 | 0x0002      |           2 |
|      15 | 0xFFFFE467  |  4294960231 |
|      16 | 0xFFFBB56F  |  4294686063 |
|      17 | 0x0516      |        1302 |

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

### Event 20

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
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 25 10 03  02 00 27 10 03 01 00 26    ...%....'....&
0010: 10 03 03 00 28 10 32 00  80 1F 00 00 00 02 00 01  ....(.2.........
0020: 00 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0007 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x000C [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0011 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0016 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                03 00 00  25 10 03 02 00 27 10 03       ...%....'..
0030: 01 00 26 10 03 03 00 28  10 32 01 80 1F 00 00 00  ..&....(.2......
0040: 02 00 01 00 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0025 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x002A [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x002F [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0034 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0046 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0047 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          00                               .       
```

#### Opcodes

```
  0: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             B6 0B 02 80 03 80 04           .......
0050: 80 04 80 04 80 04 80 04  80 05 80 06 80 00        ..............  
```

#### Opcodes

```
  0: 0x0049 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=8*, head=12*, body=12*, hands=12*, legs=12*, feet=12*, main=251*, sub=27*)
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            B6 0B                ..
0060: 02 80 03 80 07 80 07 80  08 80 08 80 08 80 09 80  ................
0070: 09 80 00                                          ...             
```

#### Opcodes

```
  0: 0x005E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=8*, head=124*, body=124*, hands=21*, legs=21*, feet=21*, main=0*, sub=0*)
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          B6 0B 0A 80 03  80 0B 80 04 80 04 80 04     .............
0080: 80 04 80 0C 80 06 80 00                           ........        
```

#### Opcodes

```
  0: 0x0073 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=8*, head=56*, body=12*, hands=12*, legs=12*, feet=12*, main=270*, sub=27*)
  1: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          6E F8 FF FF 7F 0D 80 99          n.......
0090: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0088 [0x6E] EventEntity uses emote 43*
  1: 0x008F [0x99] Wait for EventEntity animation to complete
  2: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                6E F8 FF  FF 7F 0E 80 99 F8 FF FF       n..........
00A0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0095 [0x6E] EventEntity uses emote 2*
  1: 0x009C [0x99] Wait for EventEntity animation to complete
  2: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       32 00 80 1F 00 0F  80 10 80 09 80 1F 01 6F    2............o
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A2 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A5 [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.065*, Z=-281.233*, Y=0.000*
  2: 0x00AD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 50 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    32 00 80 1F 00 0F 80  10 80 09 80 1F 01 6F 4A   2............oJ
00C0: 21 42 0A 01 4B 42 0A 01  7B 21 42 0A 01 6F 76 21  !B..KB..{!B..ov!
00D0: 42 0A 01 5B 11 80 21 42  0A 01 21 42 0A 01 6C 62  B..[..!B..!B..lb
00E0: 74 30 00                                          t0.             
```

#### Opcodes

```
  0: 0x00B1 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.065*, Z=-281.233*, Y=0.000*
  2: 0x00BC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00BF [0x4A] Laurimaux (ID: 17449505/0x010A4221) looks at C (ID: 17449547/0x010A424B)
  5: 0x00C8 [0x7B] Laurimaux (ID: 17449505/0x010A4221) stops talking
  6: 0x00CD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00CE [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Laurimaux (ID: 17449505/0x010A4221) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x00D3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "lbt0" with entities [Laurimaux (ID: 17449505/0x010A4221), Laurimaux (ID: 17449505/0x010A4221)], work=1302*
  9: 0x00E2 [0x00] END_REQSTACK()
```
