# 17727601 - Shikaree X

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 468 bytes                 |
| Total Events     | 10                        |
| References Count | 19                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [4](#event-4)            | 0x000D       |     12 |              3 |
| [65535.1](#event-655351) | 0x0019       |     26 |              8 |
| [65535.2](#event-655352) | 0x0033       |     91 |             18 |
| [65535.3](#event-655353) | 0x008E       |     29 |              9 |
| [65535.4](#event-655354) | 0x00AB       |     94 |             19 |
| [65535.5](#event-655355) | 0x0109       |     16 |              2 |
| [65535.6](#event-655356) | 0x0119       |     19 |              3 |
| [65535.7](#event-655357) | 0x012C       |     16 |              2 |
| [65535.8](#event-655358) | 0x013C       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF4D3C  |  4294921532 |
|       1 | 0xFFFF9629  |  4294940201 |
|       2 | 0xFFFFF061  |  4294963297 |
|       3 | 0x0100      |         256 |
|       4 | 0x000D      |          13 |
|       5 | 0x05DC      |        1500 |
|       6 | 0xFFFF6575  |  4294927733 |
|       7 | 0xFFFF85EC  |  4294936044 |
|       8 | 0x0000      |           0 |
|       9 | 0xFFFFEC78  |  4294962296 |
|      10 | 0x1388      |        5000 |
|      11 | 0x0B14      |        2836 |
|      12 | 0x0014      |          20 |
|      13 | 0x07D0      |        2000 |
|      14 | 0x2710      |       10000 |
|      15 | 0x00F0      |         240 |
|      16 | 0x029A      |         666 |
|      17 | 0x003C      |          60 |
|      18 | 0x003B      |          59 |

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

### Event 4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         A4 01 37               ..7
0010: 00 80 01 80 02 80 03 80  00                       .........       
```

#### Opcodes

```
  0: 0x000D [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x000F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-45.764*, z=-27.095*, y=-3.999*, direction=22.5°*
  2: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 04 80 03 00 00 05           2......
0020: 80 1A C5 00 32 04 80 1F  00 01 00 02 00 03 00 1F  ....2...........
0030: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001C [0x03] ExtData[1]->WorkLocal[0] = 1500*
  2: 0x0021 [0x1A] CALL_SUBROUTINE(address=0x00C5)
  3: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  4: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  5: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 91 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          79 00 F8 FF FF  7F 70 80 0E 01 03 01 00     y.....p......
0040: 06 80 03 02 00 07 80 03  03 00 02 80 03 04 00 08  ................
0050: 80 03 00 00 09 80 17 05  00 04 00 00 00 16 06 00  ................
0060: 04 00 00 00 07 01 00 05  00 07 02 00 06 00 37 01  ..............7.
0070: 00 02 00 03 00 04 00 03  00 00 0A 80 1A C5 00 32  ...............2
0080: 04 80 1F 00 01 00 02 00  03 00 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x0033 [0x79] EventEntity looks at Ulmia (ID: 17727600/0x010E8070) (Basic look)
  1: 0x003D [0x03] ExtData[1]->WorkLocal[1] = 4294927733*
  2: 0x0042 [0x03] ExtData[1]->WorkLocal[2] = 4294936044*
  3: 0x0047 [0x03] ExtData[1]->WorkLocal[3] = 4294963297*
  4: 0x004C [0x03] ExtData[1]->WorkLocal[4] = 0*
  5: 0x0051 [0x03] ExtData[1]->WorkLocal[0] = 4294962296*
  6: 0x0056 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
  7: 0x005D [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
  8: 0x0064 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
  9: 0x0069 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 10: 0x006E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
 11: 0x0077 [0x03] ExtData[1]->WorkLocal[0] = 5000*
 12: 0x007C [0x1A] CALL_SUBROUTINE(address=0x00C5)
 13: 0x007F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
 14: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
 15: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 16: 0x008C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 17: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 29 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            39 0B                9.
0090: 80 1C 0C 80 03 00 00 0D  80 1A C5 00 32 04 80 1F  ............2...
00A0: 00 01 00 02 00 03 00 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x008E [0x39] SET_ENTITY_DIRECTION(direction=15.6°*)
  1: 0x0091 [0x1C] WAIT(20* ticks)
  2: 0x0094 [0x03] ExtData[1]->WorkLocal[0] = 2000*
  3: 0x0099 [0x1A] CALL_SUBROUTINE(address=0x00C5)
  4: 0x009C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x009F [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  6: 0x00A7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00A9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 94 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   03 00 00 0E 80             .....
00B0: 1A C5 00 32 04 80 31 00  01 00 02 00 03 00 0F 80  ...2..1.........
00C0: 31 01 22 01 00 3B F8 FF  FF 7F 01 00 02 00 03 00  1."..;..........
00D0: 3A F8 FF FF 7F 04 00 17  05 00 04 00 00 00 16 06  :...............
00E0: 00 04 00 00 00 07 01 00  05 00 07 02 00 06 00 1B  ................
00F0: 17 05 00 04 00 00 00 16  06 00 04 00 00 00 07 01  ................
0100: 00 05 00 07 02 00 06 00  1B                       .........       
```

#### Opcodes

```
  0: 0x00AB [0x03] ExtData[1]->WorkLocal[0] = 10000*
  1: 0x00B0 [0x1A] CALL_SUBROUTINE(address=0x00C5)
  2: 0x00B3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x00B6 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3], Time=240*
  4: 0x00C0 [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  5: 0x00C2 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x00C4 [0x00] END_REQSTACK()

SUBROUTINE_00C5:
  7: 0x00C5 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  8: 0x00D0 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  9: 0x00D7 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 10: 0x00DE [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 11: 0x00E5 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 12: 0x00EA [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 13: 0x00EF [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00F0 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00F7 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00FE [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x0103 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0108 [0x1B] RETURN
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0109   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                             5B 10 80 F8 FF FF 7F           [......
0110: F8 FF FF 7F 74 6C 6E 30  00                       ....tln0.       
```

#### Opcodes

```
  0: 0x0109 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tln0" with entities [EventEntity, EventEntity], work=666*
  1: 0x0118 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0119   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             5B 10 80 F8 FF FF 7F           [......
0120: F8 FF FF 7F 74 6C 6E 31  1C 11 80 00              ....tln1....    
```

#### Opcodes

```
  0: 0x0119 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tln1" with entities [EventEntity, EventEntity], work=666*
  1: 0x0128 [0x1C] WAIT(60* ticks)
  2: 0x012B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                      66 12 80 F8              f...
0130: FF FF 7F F8 FF FF 7F 74  68 6B 31 00              .......thk1.    
```

#### Opcodes

```
  0: 0x012C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=59*
  1: 0x013B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013C   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                      66 12 80 F8              f...
0140: FF FF 7F F8 FF FF 7F 74  68 6B 32 1C 11 80 00     .......thk2.... 
```

#### Opcodes

```
  0: 0x013C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=59*
  1: 0x014B [0x1C] WAIT(60* ticks)
  2: 0x014E [0x00] END_REQSTACK()
```
