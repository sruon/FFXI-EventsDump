# 17756325 - Muhk Johldy

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 404 bytes                |
| Total Events     | 15                       |
| References Count | 26                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     33 |              3 |
| [65535.4](#event-655354)   | 0x0040       |     14 |              2 |
| [65535.5](#event-655355)   | 0x004E       |     24 |              4 |
| [473](#event-473)          | 0x0066       |      7 |              2 |
| [65535.6](#event-655356)   | 0x006D       |     10 |              2 |
| [65535.7](#event-655357)   | 0x0077       |     19 |              5 |
| [65535.8](#event-655358)   | 0x008A       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0094       |     29 |              3 |
| [65535.10](#event-6553510) | 0x00B1       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00BF       |     10 |              2 |
| [65535.12](#event-6553512) | 0x00C9       |     10 |              2 |
| [65535.13](#event-6553513) | 0x00D3       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x01FB      |         507 |
|       1 | 0x0078      |         120 |
|       2 | 0x0000      |           0 |
|       3 | 0x002A      |          42 |
|       4 | 0x001E      |          30 |
|       5 | 0xFFFE87BD  |  4294870973 |
|       6 | 0x2EE27     |      192039 |
|       7 | 0xFFFFCD38  |  4294954296 |
|       8 | 0x0A48      |        2632 |
|       9 | 0x000D      |          13 |
|      10 | 0xFFFE780A  |  4294866954 |
|      11 | 0x30144     |      196932 |
|      12 | 0xFFFFD120  |  4294955296 |
|      13 | 0xFFFE7AF7  |  4294867703 |
|      14 | 0x31DA6     |      204198 |
|      15 | 0xFFFFD121  |  4294955297 |
|      16 | 0x0617      |        1559 |
|      17 | 0xFFFE7BB5  |  4294867893 |
|      18 | 0x31D42     |      204098 |
|      19 | 0x0663      |        1635 |
|      20 | 0xFFFE7ADA  |  4294867674 |
|      21 | 0x31AC4     |      203460 |
|      22 | 0x02CC      |         716 |
|      23 | 0xFFFE78F4  |  4294867188 |
|      24 | 0x31750     |      202576 |
|      25 | 0x0526      |        1318 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 79 6D 69 30   [..........ymi0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ymi0" with entities [EventEntity, EventEntity], work=507*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 79 6D 69 30 00      S........ymi0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ymi0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               45                 E
0020: 01 80 F8 FF FF 7F F8 FF  FF 7F 73 65 32 35 02 80  ..........se25..
0030: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 79 6D 69 31 00  [..........ymi1.
```

#### Opcodes

```
  0: 0x001F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se25" with entities [EventEntity, EventEntity], work=[120*, 0*]
  1: 0x0030 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ymi1" with entities [EventEntity, EventEntity], work=507*
  2: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 53 F8 FF FF 7F F8 FF FF  7F 79 6D 69 31 00        S........ymi1.  
```

#### Opcodes

```
  0: 0x0040 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ymi1" with entities [EventEntity, EventEntity]
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            66 03                f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 77 6F 66 32 5E 69 64  .........wof2^id
0060: 6C 30 1C 04 80 00                                 l0....          
```

#### Opcodes

```
  0: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wof2" with entities [EventEntity, EventEntity], work=42*
  1: 0x005D [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0062 [0x1C] WAIT(30* ticks)
  3: 0x0065 [0x00] END_REQSTACK()
```

### Event 473

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0066 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         37 05 80               7..
0070: 06 80 07 80 08 80 00                              .......         
```

#### Opcodes

```
  0: 0x006D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-96.323*, z=192.039*, y=-13.000*, direction=231.3°*
  1: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      32  09 80 5A 00 0A 80 0B 80         2..Z.....
0080: 0C 80 5A 01 1E 9E F0 0E  01 00                    ..Z.......      
```

#### Opcodes

```
  0: 0x0077 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007A [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-100.342*, Z=196.932*, Y=-12.000*
  2: 0x0082 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0084 [0x1E] EventEntity looks at ??? (ID: 17756318/0x010EF09E) and starts talking
  4: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                37 0D 80 0E 80 0F            7.....
0090: 80 10 80 00                                       ....            
```

#### Opcodes

```
  0: 0x008A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-99.593*, z=204.198*, y=-11.999*, direction=137.0°*
  1: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             66 03 80 F8  FF FF 7F F8 FF FF 7F 77      f..........w
00A0: 6F 6E 32 2C F8 FF FF 7F  F8 FF FF 7F 6C 63 30 36  on2,........lc06
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x0094 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "won2" with entities [EventEntity, EventEntity], work=42*
  1: 0x00A3 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "lc06" with entities [EventEntity, EventEntity]
  2: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    53 F8 FF FF 7F F8 FF  FF 7F 6C 63 30 36 00      S........lc06. 
```

#### Opcodes

```
  0: 0x00B1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "lc06" with entities [EventEntity, EventEntity]
  1: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               37                 7
00C0: 11 80 12 80 0F 80 13 80  00                       .........       
```

#### Opcodes

```
  0: 0x00BF [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-99.403*, z=204.098*, y=-11.999*, direction=143.7°*
  1: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             37 14 80 15 80 0F 80           7......
00D0: 16 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00C9 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-99.622*, z=203.460*, y=-11.999*, direction=62.9°*
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          37 17 80 18 80  0C 80 19 80 00              7.........   
```

#### Opcodes

```
  0: 0x00D3 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-100.108*, z=202.576*, y=-12.000*, direction=115.8°*
  1: 0x00DC [0x00] END_REQSTACK()
```
