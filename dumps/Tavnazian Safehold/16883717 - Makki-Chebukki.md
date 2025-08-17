# 16883717 - Makki-Chebukki

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 324 bytes                   |
| Total Events     | 11                          |
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
| [105](#event-105)        | 0x005C       |      1 |              1 |
| [110](#event-110)        | 0x005D       |     10 |              2 |
| [65535.5](#event-655355) | 0x0067       |     15 |              5 |
| [65535.6](#event-655356) | 0x0076       |     18 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFEF79  |  4294963065 |
|       1 | 0x1F6E2     |      128738 |
|       2 | 0xFFFF9AEC  |  4294941420 |
|       3 | 0x0BEC      |        3052 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFFF0DC  |  4294963420 |
|       6 | 0x1FBD1     |      130001 |
|       7 | 0xFFFF9AFE  |  4294941438 |
|       8 | 0x5FE5      |       24549 |
|       9 | 0x90B9      |       37049 |
|      10 | 0xFFFFD151  |  4294955345 |
|      11 | 0x0C6E      |        3182 |
|      12 | 0x63E0      |       25568 |
|      13 | 0x9E25      |       40485 |
|      14 | 0xFFFFD120  |  4294955296 |
|      15 | 0x6073      |       24691 |
|      16 | 0x8F5D      |       36701 |
|      17 | 0xFFFFD157  |  4294955351 |
|      18 | 0x6363      |       25443 |
|      19 | 0x6E26      |       28198 |
|      20 | 0xFFFFD1D1  |  4294955473 |
|      21 | 0x12EBE     |       77502 |
|      22 | 0xE122      |       57634 |
|      23 | 0xFFFF7672  |  4294932082 |
|      24 | 0x0C1B      |        3099 |
|      25 | 0x130A2     |       77986 |
|      26 | 0xFA1A      |       64026 |
|      27 | 0xFFFF7B23  |  4294933283 |
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
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-4.231*, z=128.738*, y=-25.876*, direction=268.2°*
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
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-3.876*, Z=130.001*, Y=-25.858*
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
  1: 0x0024 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=24.549*, z=37.049*, y=-11.951*, direction=279.7°*
  2: 0x002D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=25.568*, Z=40.485*, Y=-12.000*
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
0040: 0F 80 10 80 11 80 1F 01  1E 07 A0 01 01 00        ..............  
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=24.691*, Z=36.701*, Y=-11.945*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x1E] EventEntity looks at Cherukiki (ID: 16883719/0x0101A007) and starts talking
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

### Event 105

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      00                       .   
```

#### Opcodes

```
  0: 0x005C [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         37 15 80               7..
0060: 16 80 17 80 18 80 00                              .......         
```

#### Opcodes

```
  0: 0x005D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=77.502*, z=57.634*, y=-35.214*, direction=272.4°*
  1: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      32  04 80 1F 00 19 80 1A 80         2........
0070: 1B 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0067 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=77.986*, Z=64.026*, Y=-34.013*
  2: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   1C 1C  80 32 04 80 1F 00 1D 80        ...2......
0080: 1E 80 1F 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0076 [0x1C] WAIT(30* ticks)
  1: 0x0079 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x007C [0x1F] MOVE_ENTITY: EventEntity moves to X=79.846*, Z=51.776*, Y=-36.000*
  3: 0x0084 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0086 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0087 [0x00] END_REQSTACK()
```
