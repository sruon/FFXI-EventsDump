# 16883729 - Louverance

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 328 bytes                   |
| Total Events     | 10                          |
| References Count | 31                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [112](#event-112)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     25 |              7 |
| [65535.2](#event-655352) | 0x002A       |     14 |              4 |
| [118](#event-118)        | 0x0038       |     10 |              2 |
| [65535.3](#event-655353) | 0x0042       |     15 |              5 |
| [65535.4](#event-655354) | 0x0051       |     15 |              5 |
| [65535.5](#event-655355) | 0x0060       |     24 |              6 |
| [65535.6](#event-655356) | 0x0078       |     14 |              4 |
| [65535.7](#event-655357) | 0x0086       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x19E07     |      105991 |
|       1 | 0xFFFE8CE1  |  4294872289 |
|       2 | 0xFFFF63C0  |  4294927296 |
|       3 | 0x0C3C      |        3132 |
|       4 | 0x000D      |          13 |
|       5 | 0x19DF1     |      105969 |
|       6 | 0xFFFE9CE9  |  4294876393 |
|       7 | 0x1AAEA     |      109290 |
|       8 | 0xFFFEB4E2  |  4294882530 |
|       9 | 0xFFFF63B1  |  4294927281 |
|      10 | 0x1A754     |      108372 |
|      11 | 0xFFFEC11D  |  4294885661 |
|      12 | 0x1A94D     |      108877 |
|      13 | 0xFFFECDF4  |  4294888948 |
|      14 | 0x025B      |         603 |
|      15 | 0x1ABC0     |      109504 |
|      16 | 0xFFFEBF94  |  4294885268 |
|      17 | 0x1A893     |      108691 |
|      18 | 0xFFFEBD3A  |  4294884666 |
|      19 | 0x18E81     |      102017 |
|      20 | 0xFFFF199C  |  4294908316 |
|      21 | 0xFFFF5EDE  |  4294926046 |
|      22 | 0x0BEF      |        3055 |
|      23 | 0x18E5E     |      101982 |
|      24 | 0xFFFF1F79  |  4294909817 |
|      25 | 0xFFFF5FD8  |  4294926296 |
|      26 | 0x1A3BA     |      107450 |
|      27 | 0xFFFECBB9  |  4294888377 |
|      28 | 0x18C30     |      101424 |
|      29 | 0xFFFF39FC  |  4294916604 |
|      30 | 0xFFFF60C3  |  4294926531 |

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

### Event 112

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
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=105.991*, z=-95.007*, y=-40.000*, direction=275.3°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 1F 00   2..............
0020: 07 80 08 80 09 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=105.969*, Z=-90.903*, Y=-40.000*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=109.290*, Z=-84.766*, Y=-40.015*
  4: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 04 80 1F 00 0A            2.....
0030: 80 0B 80 09 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=108.372*, Z=-81.635*, Y=-40.015*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          37 0C 80 0D 80 02 80 0E          7.......
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0038 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=108.877*, z=-78.348*, y=-40.000*, direction=53.0°*
  1: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       32 04 80 1F 00 0F  80 10 80 09 80 1F 01 6F    2............o
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0042 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=109.504*, Z=-82.028*, Y=-40.015*
  2: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    32 04 80 1F 00 11 80  12 80 09 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0051 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=108.691*, Z=-82.630*, Y=-40.015*
  2: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 37 13 80 14 80 15 80 16  80 32 04 80 1F 00 17 80  7........2......
0070: 18 80 19 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0060 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=102.017*, z=-58.980*, y=-41.250*, direction=268.5°*
  1: 0x0069 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=101.982*, Z=-57.479*, Y=-41.000*
  3: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          32 04 80 1F 00 1A 80 1B          2.......
0080: 80 02 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0078 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007B [0x1F] MOVE_ENTITY: EventEntity moves to X=107.450*, Z=-78.919*, Y=-40.000*
  2: 0x0083 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   32 04  80 1F 00 1C 80 1D 80 1E        2.........
0090: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0086 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0089 [0x1F] MOVE_ENTITY: EventEntity moves to X=101.424*, Z=-50.692*, Y=-40.765*
  2: 0x0091 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0093 [0x00] END_REQSTACK()
```
