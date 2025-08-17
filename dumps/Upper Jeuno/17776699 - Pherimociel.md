# 17776699 - Pherimociel

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 272 bytes             |
| Total Events     | 5                     |
| References Count | 26                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [207](#event-207)        | 0x0001       |     22 |              4 |
| [65535.1](#event-655351) | 0x0017       |     29 |              7 |
| [65535.2](#event-655352) | 0x0034       |     21 |              7 |
| [65535.3](#event-655353) | 0x0049       |     56 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF015C  |  4294902108 |
|       1 | 0x429A      |       17050 |
|       2 | 0x03E8      |        1000 |
|       3 | 0x0330      |         816 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFF03F6  |  4294902774 |
|       6 | 0x2EBD      |       11965 |
|       7 | 0xFFFF0C45  |  4294904901 |
|       8 | 0x21F0      |        8688 |
|       9 | 0x00C7      |         199 |
|      10 | 0x003C      |          60 |
|      11 | 0xFFFF0F19  |  4294905625 |
|      12 | 0x20E9      |        8425 |
|      13 | 0x0000      |           0 |
|      14 | 0x0238      |         568 |
|      15 | 0xFFFF0B65  |  4294904677 |
|      16 | 0x3014      |       12308 |
|      17 | 0xFFFF38A8  |  4294916264 |
|      18 | 0x5FFF      |       24575 |
|      19 | 0x03E7      |         999 |
|      20 | 0xFFFF8CA8  |  4294937768 |
|      21 | 0x924B      |       37451 |
|      22 | 0xFFFFA7DC  |  4294944732 |
|      23 | 0x8CAF      |       36015 |
|      24 | 0xFFFFC333  |  4294951731 |
|      25 | 0x677A      |       26490 |

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

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 37 00 80   ............7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-65.188*, z=17.050*, y=1.000*, direction=71.7°*
  3: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  04 80 1F 00 05 80 06 80         2........
0020: 02 80 1F 01 1F 00 07 80  08 80 09 80 1F 01 1E 39  ...............9
0030: 40 0F 01 00                                       @...            
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-64.522*, Z=11.965*, Y=1.000*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=-62.395*, Z=8.688*, Y=0.199*
  4: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x002E [0x1E] EventEntity looks at Unnamed NPC (ID: 17776697/0x010F4039) and starts talking
  6: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             1C 0A 80 32  04 80 1F 00 0B 80 0C 80      ...2........
0040: 0D 80 1F 01 6F 39 0E 80  00                       ....o9...       
```

#### Opcodes

```
  0: 0x0034 [0x1C] WAIT(60* ticks)
  1: 0x0037 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.671*, Z=8.425*, Y=0.000*
  3: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0045 [0x39] SET_ENTITY_DIRECTION(direction=3.1°*)
  6: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 56 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             32 04 80 1F 00 0F 80           2......
0050: 10 80 02 80 1F 01 1F 00  11 80 12 80 13 80 1F 01  ................
0060: 1F 00 14 80 15 80 0D 80  1F 01 1F 00 16 80 17 80  ................
0070: 0D 80 1F 01 1F 00 18 80  19 80 0D 80 1F 01 22 01  ..............".
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0049 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=-62.619*, Z=12.308*, Y=1.000*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x1F] MOVE_ENTITY: EventEntity moves to X=-51.032*, Z=24.575*, Y=0.999*
  4: 0x005E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=-29.528*, Z=37.451*, Y=0.000*
  6: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.564*, Z=36.015*, Y=0.000*
  8: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=-15.565*, Z=26.490*, Y=0.000*
 10: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x007E [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 12: 0x0080 [0x00] END_REQSTACK()
```
