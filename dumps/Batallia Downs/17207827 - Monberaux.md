# 17207827 - Monberaux

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 372 bytes                |
| Total Events     | 9                        |
| References Count | 8                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |     81 |             15 |
| [65535.1](#event-655351) | 0x0052       |     41 |              9 |
| [65535.2](#event-655352) | 0x007B       |     29 |              3 |
| [65535.3](#event-655353) | 0x0098       |     29 |              3 |
| [65535.4](#event-655354) | 0x00B5       |     29 |              3 |
| [65535.5](#event-655355) | 0x00D2       |     19 |              3 |
| [65535.6](#event-655356) | 0x00E5       |     29 |              3 |
| [65535.7](#event-655357) | 0x0102       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x7694C     |      485708 |
|       1 | 0xFFFD8C39  |  4294806585 |
|       2 | 0x200E      |        8206 |
|       3 | 0x0829      |        2089 |
|       4 | 0xFFFFFA24  |  4294965796 |
|       5 | 0x000D      |          13 |
|       6 | 0x0129      |         297 |
|       7 | 0x0078      |         120 |

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

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 81 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 92  01 F8 FF FF 7F 00 3B F8   .............;.
0010: FF FF 7F 01 00 02 00 03  00 3A F8 FF FF 7F 04 00  .........:......
0020: 17 05 00 04 00 00 00 16  06 00 04 00 00 00 07 01  ................
0030: 00 05 00 07 02 00 06 00  1B 17 05 00 04 00 00 00  ................
0040: 16 06 00 04 00 00 00 07  01 00 05 00 07 02 00 06  ................
0050: 00 1B                                             ..              
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x000E [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
     0x0019 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
     0x0020 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0027 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x002E [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x0033 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0038 [0x1B] RETURN
     0x0039 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0040 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0047 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x004C [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0051 [0x1B] RETURN
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 41 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       37 00 80 01 80 02  80 03 80 03 00 00 04 80    7.............
0060: 1A 0E 00 37 01 00 02 00  03 00 04 00 32 05 80 1F  ...7........2...
0070: 00 00 80 01 80 02 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x0052 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=485.708*, z=-160.711*, y=8.206*, direction=183.6°*
  1: 0x005B [0x03] ExtData[1]->WorkLocal[0] = 4294965796*
  2: 0x0060 [0x1A] CALL_SUBROUTINE(address=0x000E)
  3: 0x0063 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  4: 0x006C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=485.708*, Z=-160.711*, Y=8.206*
  6: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0079 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   5B 06 80 F8 FF             [....
0080: FF 7F F8 FF FF 7F 74 6C  6B 30 53 F8 FF FF 7F F8  ......tlk0S.....
0090: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x007B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=297*
  1: 0x008A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          5B 06 80 F8 FF FF 7F F8          [.......
00A0: FF FF 7F 74 6C 6B 31 53  F8 FF FF 7F F8 FF FF 7F  ...tlk1S........
00B0: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x0098 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=297*
  1: 0x00A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
00C0: 70 61 73 30 53 F8 FF FF  7F F8 FF FF 7F 70 61 73  pas0S........pas
00D0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x00B5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=297*
  1: 0x00C4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x00D1 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D2   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       5B 06 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B    [..........tlk
00E0: 30 1C 07 80 00                                    0....           
```

#### Opcodes

```
  0: 0x00D2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=297*
  1: 0x00E1 [0x1C] WAIT(120* ticks)
  2: 0x00E4 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E5   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
00F0: 74 68 6B 31 53 F8 FF FF  7F F8 FF FF 7F 74 68 6B  thk1S........thk
0100: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x00E5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=297*
  1: 0x00F4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x0101 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       5B 06 80 F8 FF FF  7F F8 FF FF 7F 74 68 6B    [..........thk
0110: 32 53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     2S........thk2. 
```

#### Opcodes

```
  0: 0x0102 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=297*
  1: 0x0111 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x011E [0x00] END_REQSTACK()
```
