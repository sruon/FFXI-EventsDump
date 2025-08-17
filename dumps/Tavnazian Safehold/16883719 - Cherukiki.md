# 16883719 - Cherukiki

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 320 bytes                   |
| Total Events     | 10                          |
| References Count | 32                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [101](#event-101)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     15 |              5 |
| [103](#event-103)        | 0x0020       |      1 |              1 |
| [65535.2](#event-655352) | 0x0021       |     26 |              7 |
| [65535.3](#event-655353) | 0x003B       |     19 |              5 |
| [65535.4](#event-655354) | 0x004E       |     14 |              4 |
| [110](#event-110)        | 0x005C       |     10 |              2 |
| [65535.5](#event-655355) | 0x0066       |     15 |              5 |
| [65535.6](#event-655356) | 0x0075       |     18 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFE179  |  4294959481 |
|       1 | 0x1EF81     |      126849 |
|       2 | 0xFFFF9B31  |  4294941489 |
|       3 | 0x0C78      |        3192 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFFE73A  |  4294960954 |
|       6 | 0x1F954     |      129364 |
|       7 | 0xFFFF9AE6  |  4294941414 |
|       8 | 0x638E      |       25486 |
|       9 | 0x8BBA      |       35770 |
|      10 | 0xFFFFD178  |  4294955384 |
|      11 | 0x0C63      |        3171 |
|      12 | 0x6BA5      |       27557 |
|      13 | 0x9E2D      |       40493 |
|      14 | 0xFFFFD153  |  4294955347 |
|      15 | 0x6446      |       25670 |
|      16 | 0x8C5F      |       35935 |
|      17 | 0xFFFFD17F  |  4294955391 |
|      18 | 0x6363      |       25443 |
|      19 | 0x6E26      |       28198 |
|      20 | 0xFFFFD1D1  |  4294955473 |
|      21 | 0x13895     |       80021 |
|      22 | 0xDAB1      |       55985 |
|      23 | 0xFFFF76FF  |  4294932223 |
|      24 | 0x0C5B      |        3163 |
|      25 | 0x138F4     |       80116 |
|      26 | 0xF81E      |       63518 |
|      27 | 0xFFFF7B30  |  4294933296 |
|      28 | 0x001E      |          30 |
|      29 | 0x137E6     |       79846 |
|      30 | 0xCA40      |       51776 |
|      31 | 0xFFFF7360  |  4294931296 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      37  00 80 01 80 02 80 03 80         7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-7.815*, z=126.849*, y=-25.807*, direction=280.5°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-6.342*, Z=129.364*, Y=-25.882*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001F [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0020  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 04 80 37 08 80 09  80 0A 80 0B 80 22 00 1F   2..7........"..
0030: 00 0C 80 0D 80 0E 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0024 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=25.486*, z=35.770*, y=-11.912*, direction=278.7°*
  2: 0x002D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=27.557*, Z=40.493*, Y=-11.949*
  4: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0039 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   32 04 80 1F 00             2....
0040: 0F 80 10 80 11 80 1F 01  1E 05 A0 01 01 00        ..............  
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=25.670*, Z=35.935*, Y=-11.905*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x1E] EventEntity looks at Makki-Chebukki (ID: 16883717/0x0101A005) and starts talking
  4: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            32 04                2.
0050: 80 1F 00 12 80 13 80 14  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x004E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=25.443*, Z=28.198*, Y=-11.823*
  2: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005B [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      37 15 80 16              7...
0060: 80 17 80 18 80 00                                 ......          
```

#### Opcodes

```
  0: 0x005C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=80.021*, z=55.985*, y=-35.073*, direction=278.0°*
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   32 04  80 1F 00 19 80 1A 80 1B        2.........
0070: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0066 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0069 [0x1F] MOVE_ENTITY: EventEntity moves to X=80.116*, Z=63.518*, Y=-34.000*
  2: 0x0071 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0073 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                1C 1C 80  32 04 80 1F 00 1D 80 1E       ...2.......
0080: 80 1F 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0075 [0x1C] WAIT(30* ticks)
  1: 0x0078 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x007B [0x1F] MOVE_ENTITY: EventEntity moves to X=79.846*, Z=51.776*, Y=-36.000*
  3: 0x0083 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0085 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0086 [0x00] END_REQSTACK()
```
