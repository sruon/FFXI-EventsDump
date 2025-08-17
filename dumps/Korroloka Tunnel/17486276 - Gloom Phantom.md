# 17486276 - Gloom Phantom

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Korroloka Tunnel (ID: 173) |
| Block Size       | 312 bytes                  |
| Total Events     | 12                         |
| References Count | 27                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [14](#event-14)          | 0x0001       |      7 |              2 |
| [15](#event-15)          | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |      7 |              3 |
| [65535.2](#event-655352) | 0x0016       |      7 |              3 |
| [65535.3](#event-655353) | 0x001D       |      5 |              2 |
| [65535.4](#event-655354) | 0x0022       |      5 |              2 |
| [65535.5](#event-655355) | 0x0027       |     15 |              5 |
| [65535.6](#event-655356) | 0x0036       |     14 |              4 |
| [65535.7](#event-655357) | 0x0044       |     14 |              4 |
| [65535.8](#event-655358) | 0x0052       |     14 |              4 |
| [65535.9](#event-655359) | 0x0060       |     44 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0C55      |        3157 |
|       3 | 0x0E00      |        3584 |
|       4 | 0x000D      |          13 |
|       5 | 0xCAD6      |       51926 |
|       6 | 0x12218     |       74264 |
|       7 | 0x0138      |         312 |
|       8 | 0xC0BC      |       49340 |
|       9 | 0x13CEA     |       81130 |
|      10 | 0x01F4      |         500 |
|      11 | 0xC2EC      |       49900 |
|      12 | 0x13704     |       79620 |
|      13 | 0xB982      |       47490 |
|      14 | 0x13754     |       79700 |
|      15 | 0x0186      |         390 |
|      16 | 0x0028      |          40 |
|      17 | 0xA780      |       42880 |
|      18 | 0x12FF2     |       77810 |
|      19 | 0x956A      |       38250 |
|      20 | 0x10ACC     |       68300 |
|      21 | 0x7706      |       30470 |
|      22 | 0xD84A      |       55370 |
|      23 | 0x0618      |        1560 |
|      24 | 0x317E      |       12670 |
|      25 | 0x9EDE      |       40670 |
|      26 | 0x0280      |         640 |

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

### Event 14

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

### Event 15

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               AB                 .
0010: 03 AC 01 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000F [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0011 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   AC 01  01 80 AB 04 00                 .......   
```

#### Opcodes

```
  0: 0x0016 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x001A [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         B6 00 02               ...
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x001D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3157*)
  1: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       B6 00 03 80 00                                .....         
```

#### Opcodes

```
  0: 0x0022 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3584*)
  1: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  04 80 1F 00 05 80 06 80         2........
0030: 07 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=51.926*, Z=74.264*, Y=0.312*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   32 04  80 1F 00 08 80 09 80 0A        2.........
0040: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0036 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0039 [0x1F] MOVE_ENTITY: EventEntity moves to X=49.340*, Z=81.130*, Y=0.500*
  2: 0x0041 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             32 04 80 1F  00 0B 80 0C 80 0A 80 1F      2...........
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0044 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=49.900*, Z=79.620*, Y=0.500*
  2: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       32 04 80 1F 00 0D  80 0E 80 0F 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0052 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=47.490*, Z=79.700*, Y=0.390*
  2: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 32 10 80 1F 00 11 80 12  80 01 80 1F 01 1F 00 13  2...............
0070: 80 14 80 0A 80 1F 01 1F  00 15 80 16 80 17 80 1F  ................
0080: 01 1F 00 18 80 19 80 1A  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x0060 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=42.880*, Z=77.810*, Y=0.000*
  2: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=38.250*, Z=68.300*, Y=0.500*
  4: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0077 [0x1F] MOVE_ENTITY: EventEntity moves to X=30.470*, Z=55.370*, Y=1.560*
  6: 0x007F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0081 [0x1F] MOVE_ENTITY: EventEntity moves to X=12.670*, Z=40.670*, Y=0.640*
  8: 0x0089 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x008B [0x00] END_REQSTACK()
```
