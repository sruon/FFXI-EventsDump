# 17572293 - Ajido-Marujido

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Outer Horutoto Ruins (ID: 194) |
| Block Size       | 252 bytes                      |
| Total Events     | 7                              |
| References Count | 22                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [68](#event-68)          | 0x0001       |      1 |              1 |
| [70](#event-70)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     66 |             12 |
| [65535.2](#event-655352) | 0x0045       |     23 |              5 |
| [65535.3](#event-655353) | 0x005C       |     14 |              4 |
| [65535.4](#event-655354) | 0x006A       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFC02B8  |  4294705848 |
|       1 | 0x550B      |       21771 |
|       2 | 0x0000      |           0 |
|       3 | 0x0A3D      |        2621 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFBF862  |  4294703202 |
|       6 | 0x614B      |       24907 |
|       7 | 0x000D      |          13 |
|       8 | 0xFFFBF3D1  |  4294702033 |
|       9 | 0x6587      |       25991 |
|      10 | 0x0151      |         337 |
|      11 | 0xFFFBEF4A  |  4294700874 |
|      12 | 0x673E      |       26430 |
|      13 | 0x0A28      |        2600 |
|      14 | 0xFFFBED0C  |  4294700300 |
|      15 | 0xCB1B      |       51995 |
|      16 | 0xFFFC07D3  |  4294707155 |
|      17 | 0xECCE      |       60622 |
|      18 | 0xFFFFFFEA  |  4294967274 |
|      19 | 0xFFFC08E3  |  4294707427 |
|      20 | 0x12967     |       76135 |
|      21 | 0xFFFFFFC0  |  4294967232 |

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

### Event 68

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

### Event 70

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 66 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 32 04 80 1F     7........2...
0010: 00 05 80 06 80 02 80 1F  01 6F 32 07 80 1F 00 08  .........o2.....
0020: 80 09 80 02 80 1F 01 6F  5B 0A 80 F8 FF FF 7F F8  .......o[.......
0030: FF FF 7F 74 68 6B 31 53  F8 FF FF 7F F8 FF FF 7F  ...thk1S........
0040: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-261.448*, z=21.771*, y=0.000*, direction=230.4°*
  1: 0x000C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-264.094*, Z=24.907*, Y=0.000*
  3: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0019 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x001A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  6: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-265.263*, Z=25.991*, Y=0.000*
  7: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0028 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=337*
 10: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
 11: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                37 0B 80  0C 80 02 80 0D 80 32 04       7........2.
0050: 80 1F 00 0E 80 0F 80 02  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x0045 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-266.422*, z=26.430*, y=0.000*, direction=228.5°*
  1: 0x004E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=-266.996*, Z=51.995*, Y=0.000*
  3: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      32 04 80 1F              2...
0060: 00 10 80 11 80 12 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x005C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=-260.141*, Z=60.622*, Y=-0.022*
  2: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                32 04 80 1F 00 13            2.....
0070: 80 14 80 15 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x006A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=-259.869*, Z=76.135*, Y=-0.064*
  2: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0077 [0x00] END_REQSTACK()
```
