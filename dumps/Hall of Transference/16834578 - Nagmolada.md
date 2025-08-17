# 16834578 - Nagmolada

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Hall of Transference (ID: 14) |
| Block Size       | 316 bytes                     |
| Total Events     | 8                             |
| References Count | 19                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [155](#event-155)        | 0x000D       |     16 |              3 |
| [65535.1](#event-655351) | 0x001D       |     14 |              4 |
| [65535.2](#event-655352) | 0x002B       |     57 |              5 |
| [65535.3](#event-655353) | 0x0064       |     14 |              4 |
| [65535.4](#event-655354) | 0x0072       |     44 |              8 |
| [65535.5](#event-655355) | 0x009E       |     16 |              2 |
| [65535.6](#event-655356) | 0x00AE       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x445C0     |      280000 |
|       1 | 0xFFFF3FF0  |  4294918128 |
|       2 | 0xFFFEC505  |  4294886661 |
|       3 | 0x0BC5      |        3013 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF38C8  |  4294916296 |
|       6 | 0x01D3      |         467 |
|       7 | 0xFFFF63C0  |  4294927296 |
|       8 | 0xFFFEBBBB  |  4294884283 |
|       9 | 0x445A7     |      279975 |
|      10 | 0xFFFF92A0  |  4294939296 |
|      11 | 0xFFFEB04A  |  4294881354 |
|      12 | 0x0BF9      |        3065 |
|      13 | 0x445B2     |      279986 |
|      14 | 0xFFFF9465  |  4294939749 |
|      15 | 0xFFFEAE45  |  4294880837 |
|      16 | 0x000A      |          10 |
|      17 | 0x0283      |         643 |
|      18 | 0x005A      |          90 |

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
0000: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 155

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         94 01 F8               ...
0010: FF FF 7F 37 00 80 01 80  02 80 03 80 00           ...7.........   
```

#### Opcodes

```
  0: 0x000D [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=280.000*, z=-49.168*, y=-80.635*, direction=264.8°*
  2: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         32 04 80               2..
0020: 1F 00 00 80 05 80 02 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x001D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=280.000*, Z=-51.000*, Y=-80.635*
  2: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 57 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   5B 06 80 F8 FF             [....
0030: FF 7F F8 FF FF 7F 62 69  6E 30 53 F8 FF FF 7F F8  ......bin0S.....
0040: FF FF 7F 62 69 6E 30 5B  06 80 F8 FF FF 7F F8 FF  ...bin0[........
0050: FF 7F 62 69 6E 31 53 F8  FF FF 7F F8 FF FF 7F 62  ..bin1S........b
0060: 69 6E 31 00                                       in1.            
```

#### Opcodes

```
  0: 0x002B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bin0" with entities [EventEntity, EventEntity], work=467*
  1: 0x003A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bin0" with entities [EventEntity, EventEntity]
  2: 0x0047 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bin1" with entities [EventEntity, EventEntity], work=467*
  3: 0x0056 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bin1" with entities [EventEntity, EventEntity]
  4: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             32 04 80 1F  00 00 80 07 80 08 80 1F      2...........
0070: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0064 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=280.000*, Z=-40.000*, Y=-83.013*
  2: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 44 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       32 04 80 37 09 80  0A 80 0B 80 0C 80 1F 00    2..7..........
0080: 0D 80 0E 80 0F 80 1F 01  1C 10 80 5B 11 80 F8 FF  ...........[....
0090: FF 7F F8 FF FF 7F 74 72  30 30 1C 12 80 00        ......tr00....  
```

#### Opcodes

```
  0: 0x0072 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0075 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=279.975*, z=-28.000*, y=-85.942*, direction=269.4°*
  2: 0x007E [0x1F] MOVE_ENTITY: EventEntity moves to X=279.986*, Z=-27.547*, Y=-86.459*
  3: 0x0086 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0088 [0x1C] WAIT(10* ticks)
  5: 0x008B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tr00" with entities [EventEntity, EventEntity], work=643*
  6: 0x009A [0x1C] WAIT(90* ticks)
  7: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            5B 11                [.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 74 72 30 30 00        .........tr00.  
```

#### Opcodes

```
  0: 0x009E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tr00" with entities [EventEntity, EventEntity], work=643*
  1: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            5B 11                [.
00B0: 80 F8 FF FF 7F F8 FF FF  7F 74 72 30 31 00        .........tr01.  
```

#### Opcodes

```
  0: 0x00AE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tr01" with entities [EventEntity, EventEntity], work=643*
  1: 0x00BD [0x00] END_REQSTACK()
```
