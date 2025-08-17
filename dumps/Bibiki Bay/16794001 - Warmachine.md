# 16794001 - Warmachine

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Bibiki Bay (ID: 4) |
| Block Size       | 344 bytes          |
| Total Events     | 11                 |
| References Count | 21                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     53 |              5 |
| [32](#event-32)          | 0x0036       |     13 |              3 |
| [33](#event-33)          | 0x0043       |     13 |              3 |
| [65535.2](#event-655352) | 0x0050       |     10 |              2 |
| [65535.3](#event-655353) | 0x005A       |     15 |              5 |
| [34](#event-34)          | 0x0069       |      1 |              1 |
| [65535.4](#event-655354) | 0x006A       |      9 |              3 |
| [65535.5](#event-655355) | 0x0073       |     10 |              2 |
| [65535.6](#event-655356) | 0x007D       |     74 |             16 |
| [43](#event-43)          | 0x00C7       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFABB6C  |  4294622060 |
|       1 | 0xFFF1194D  |  4293990733 |
|       2 | 0xFFFFF38C  |  4294964108 |
|       3 | 0x0BCE      |        3022 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFABF9A  |  4294623130 |
|       6 | 0xFFF13070  |  4293996656 |
|       7 | 0xFFFFF3D1  |  4294964177 |
|       8 | 0xFFFB06D2  |  4294641362 |
|       9 | 0xFFF48F31  |  4294217521 |
|      10 | 0xFFFFF319  |  4294963993 |
|      11 | 0x0C6C      |        3180 |
|      12 | 0x0000      |           0 |
|      13 | 0x0800      |        2048 |
|      14 | 0x0020      |          32 |
|      15 | 0x1000      |        4096 |
|      16 | 0x0001      |           1 |
|      17 | 0x000C      |          12 |
|      18 | 0xFFFAE870  |  4294633584 |
|      19 | 0xFFF44C84  |  4294200452 |
|      20 | 0xFFFFF5E8  |  4294964712 |

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
| Data Size    | 53 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2C F8 FF FF 7F F8 FF  FF 7F 64 65 61 64 53 F8   ,........deadS.
0010: FF FF 7F F8 FF FF 7F 64  65 61 64 2C F8 FF FF 7F  .......dead,....
0020: F8 FF FF 7F 63 6F 72 70  53 F8 FF FF 7F F8 FF FF  ....corpS.......
0030: 7F 63 6F 72 70 00                                 .corp.          
```

#### Opcodes

```
  0: 0x0001 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [EventEntity, EventEntity]
  1: 0x000E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dead" with entities [EventEntity, EventEntity]
  2: 0x001B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [EventEntity, EventEntity]
  3: 0x0028 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "corp" with entities [EventEntity, EventEntity]
  4: 0x0035 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   92 01  F8 FF FF 7F 94 01 F8 FF        ..........
0040: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0036 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x003C [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0042 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          92 01 F8 FF FF  7F 94 01 F8 FF FF 7F 00     .............
```

#### Opcodes

```
  0: 0x0043 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0049 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 37 00 80 01 80 02 80 03  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0050 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-345.236*, z=-976.563*, y=-3.188*, direction=265.6°*
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                32 04 80 1F 00 05            2.....
0060: 80 06 80 07 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x005A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=-344.166*, Z=-970.640*, Y=-3.119*
  2: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0068 [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0069  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             00                             .      
```

#### Opcodes

```
  0: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006A  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                22 00 2F 00 F8 FF            "./...
0070: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x006A [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x006C [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          37 08 80 09 80  0A 80 0B 80 00              7.........   
```

#### Opcodes

```
  0: 0x0073 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-325.934*, z=-749.775*, y=-3.303*, direction=279.5°*
  1: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 74 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         3A F8 FF               :..
0080: FF 7F 01 00 03 00 00 0C  80 02 00 00 0D 80 01 B1  ................
0090: 00 07 00 00 0E 80 07 01  00 0E 80 02 01 00 0F 80  ................
00A0: 04 A8 00 03 01 00 0C 80  39 01 00 1C 10 80 01 89  ........9.......
00B0: 00 27 10 F0 FF FF 7F 1E  32 11 80 1F 00 12 80 13  .'......2.......
00C0: 80 14 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x007D [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[1])
  1: 0x0084 [0x03] ExtData[1]->WorkLocal[0] = 0*
  2: 0x0089 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2048*) GOTO 0x00B1
  3: 0x0091 [0x07] ExtData[1]->WorkLocal[0] += 32*
  4: 0x0096 [0x07] ExtData[1]->WorkLocal[1] += 32*
  5: 0x009B [0x02] IF !(ExtData[1]->WorkLocal[1] < 4096*) GOTO 0x00A8
  6: 0x00A3 [0x03] ExtData[1]->WorkLocal[1] = 0*
  7: 0x00A8 [0x39] SET_ENTITY_DIRECTION(direction=ExtData[1]->WorkLocal[1])
  8: 0x00AB [0x1C] WAIT(1* ticks)
  9: 0x00AE [0x01] GOTO 0x0089
 10: 0x00B1 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x1E)
 11: 0x00B8 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
 12: 0x00BB [0x1F] MOVE_ENTITY: EventEntity moves to X=-333.712*, Z=-766.844*, Y=-2.584*
 13: 0x00C3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 14: 0x00C5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 15: 0x00C6 [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      00                                  .        
```

#### Opcodes

```
  0: 0x00C7 [0x00] END_REQSTACK()
```
