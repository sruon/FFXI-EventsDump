# 17531177 - Crooked Arrow

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 320 bytes                        |
| Total Events     | 10                               |
| References Count | 27                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [22](#event-22)          | 0x000D       |     10 |              2 |
| [38](#event-38)          | 0x0017       |      1 |              1 |
| [39](#event-39)          | 0x0018       |      1 |              1 |
| [65535.1](#event-655351) | 0x0019       |     43 |             12 |
| [65535.2](#event-655352) | 0x0044       |     10 |              2 |
| [65535.3](#event-655353) | 0x004E       |     27 |              3 |
| [65535.4](#event-655354) | 0x0069       |     10 |              2 |
| [65535.5](#event-655355) | 0x0073       |     15 |              5 |
| [65535.6](#event-655356) | 0x0082       |     23 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x28398     |      164760 |
|       1 | 0xFFFFB317  |  4294947607 |
|       2 | 0xFFFFB2F3  |  4294947571 |
|       3 | 0x080B      |        2059 |
|       4 | 0x000A      |          10 |
|       5 | 0x0028      |          40 |
|       6 | 0x25670     |      153200 |
|       7 | 0xFFFFB53A  |  4294948154 |
|       8 | 0xFFFFB2BF  |  4294947519 |
|       9 | 0x1FA50     |      129616 |
|      10 | 0xFFFFDC44  |  4294958148 |
|      11 | 0xFFFFB1AA  |  4294947242 |
|      12 | 0x12500     |       75008 |
|      13 | 0x651C      |       25884 |
|      14 | 0xFFFFB3A1  |  4294947745 |
|      15 | 0x6F7B2     |      456626 |
|      16 | 0x1F7B5     |      128949 |
|      17 | 0x0000      |           0 |
|      18 | 0x020F      |         527 |
|      19 | 0xFFFFF882  |  4294965378 |
|      20 | 0xFFFE3D7F  |  4294851967 |
|      21 | 0xFFFF7554  |  4294931796 |
|      22 | 0x0B69      |        2921 |
|      23 | 0x000D      |          13 |
|      24 | 0x0014      |          20 |
|      25 | 0xFFFFF80F  |  4294965263 |
|      26 | 0xFFFE69C0  |  4294863296 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 01 F8 FF FF 7F 92 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=164.760*, z=-19.689*, y=-19.725*, direction=181.0°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      00                                  .        
```

#### Opcodes

```
  0: 0x0017 [0x00] END_REQSTACK()
```

### Event 39

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          00                               .       
```

#### Opcodes

```
  0: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 43 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1C 04 80 32 05 80 33           ...2..3
0020: 01 5A 00 06 80 07 80 08  80 5A 01 5A 00 09 80 0A  .Z.......Z.Z....
0030: 80 0B 80 5A 01 5A 00 0C  80 0D 80 0E 80 5A 01 33  ...Z.Z.......Z.3
0040: 00 22 01 00                                       ."..            
```

#### Opcodes

```
  0: 0x0019 [0x1C] WAIT(10* ticks)
  1: 0x001C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x001F [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  3: 0x0021 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=153.200*, Z=-19.142*, Y=-19.777*
  4: 0x0029 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  5: 0x002B [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=129.616*, Z=-9.148*, Y=-20.054*
  6: 0x0033 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x0035 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=75.008*, Z=25.884*, Y=-19.551*
  8: 0x003D [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  9: 0x003F [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
 10: 0x0041 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 11: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             37 0F 80 10  80 11 80 12 80 00            7.........  
```

#### Opcodes

```
  0: 0x0044 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=456.626*, z=128.949*, y=0.000*, direction=46.3°*
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            2C F8                ,.
0050: FF FF 7F F8 FF FF 7F 63  6F 72 70 53 F8 FF FF 7F  .......corpS....
0060: F8 FF FF 7F 63 6F 72 70  00                       ....corp.       
```

#### Opcodes

```
  0: 0x004E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [EventEntity, EventEntity]
  1: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "corp" with entities [EventEntity, EventEntity]
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             37 13 80 14 80 15 80           7......
0070: 16 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0069 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.918*, z=-115.329*, y=-35.500*, direction=256.7°*
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          32 17 80 1F 00  13 80 14 80 15 80 1F 01     2............
0080: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0073 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0076 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.918*, Z=-115.329*, Y=-35.500*
  2: 0x007E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0080 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       1C 18 80 32 05 80  1F 00 19 80 1A 80 15 80    ...2..........
0090: 1F 01 6F 1E 22 81 0B 01  00                       ..o."....       
```

#### Opcodes

```
  0: 0x0082 [0x1C] WAIT(20* ticks)
  1: 0x0085 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0088 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.033*, Z=-104.000*, Y=-35.500*
  3: 0x0090 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0092 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0093 [0x1E] EventEntity looks at Wolfgang (ID: 17531170/0x010B8122) and starts talking
  6: 0x0098 [0x00] END_REQSTACK()
```
