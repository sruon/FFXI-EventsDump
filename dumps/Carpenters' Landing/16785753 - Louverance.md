# 16785753 - Louverance

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Carpenters' Landing (ID: 2) |
| Block Size       | 416 bytes                   |
| Total Events     | 10                          |
| References Count | 11                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [37](#event-37)          | 0x0001       |     49 |              8 |
| [65535.1](#event-655351) | 0x0032       |     24 |              7 |
| [65535.2](#event-655352) | 0x004A       |     23 |              7 |
| [65535.3](#event-655353) | 0x0061       |     23 |              7 |
| [65535.4](#event-655354) | 0x0078       |     23 |              7 |
| [65535.5](#event-655355) | 0x008F       |     16 |              2 |
| [65535.6](#event-655356) | 0x009F       |     29 |              3 |
| [65535.7](#event-655357) | 0x00BC       |     29 |              3 |
| [65535.8](#event-655358) | 0x00D9       |     97 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DDAE     |      122286 |
|       1 | 0xFFF9E7B0  |  4294567856 |
|       2 | 0xFFFFE8D0  |  4294961360 |
|       3 | 0x0B4F      |        2895 |
|       4 | 0xFFFFF830  |  4294965296 |
|       5 | 0x003C      |          60 |
|       6 | 0x000D      |          13 |
|       7 | 0x0800      |        2048 |
|       8 | 0x07D0      |        2000 |
|       9 | 0x0FA0      |        4000 |
|      10 | 0x001D      |          29 |

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

### Event 37

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 49 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 92  01 F8 FF FF 7F 37 00 80   ............7..
0010: 01 80 02 80 03 80 03 00  00 04 80 1A F6 00 37 01  ..............7.
0020: 00 02 00 03 00 04 00 79  00 F8 FF FF 7F F0 FF FF  .......y........
0030: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=122.286*, z=-399.440*, y=-5.936*, direction=254.4°*
  3: 0x0016 [0x03] ExtData[1]->WorkLocal[0] = 4294965296*
  4: 0x001B [0x1A] CALL_SUBROUTINE(address=0x00F6)
  5: 0x001E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  6: 0x0027 [0x79] EventEntity looks at LocalPlayer (Basic look)
  7: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 24 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       1C 05 80 4E 00 59  21 00 01 32 06 80 1F 00    ...N.Y!..2....
0040: 00 80 01 80 02 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0032 [0x1C] WAIT(60* ticks)
  1: 0x0035 [0x4E] SET_ENTITY_HIDE_FLAG: Show Louverance (ID: 16785753/0x01002159)
  2: 0x003B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=122.286*, Z=-399.440*, Y=-5.936*
  4: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0048 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                3A F8 FF FF 7F 04            :.....
0050: 00 07 04 00 07 80 39 04  00 7B F8 FF FF 7F 6F 70  ......9..{....op
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x004A [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  1: 0x0051 [0x07] ExtData[1]->WorkLocal[4] += 2048*
  2: 0x0056 [0x39] SET_ENTITY_DIRECTION(direction=ExtData[1]->WorkLocal[4])
  3: 0x0059 [0x7B] EventEntity stops talking
  4: 0x005E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x005F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    32 06 80 03 00 00 08  80 1A F6 00 1F 00 01 00   2..............
0070: 02 00 03 00 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0061 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0064 [0x03] ExtData[1]->WorkLocal[0] = 2000*
  2: 0x0069 [0x1A] CALL_SUBROUTINE(address=0x00F6)
  3: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          32 06 80 03 00 00 09 80          2.......
0080: 1A F6 00 1F 00 01 00 02  00 03 00 1F 01 6F 00     .............o. 
```

#### Opcodes

```
  0: 0x0078 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007B [0x03] ExtData[1]->WorkLocal[0] = 4000*
  2: 0x0080 [0x1A] CALL_SUBROUTINE(address=0x00F6)
  3: 0x0083 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x008B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x008D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               66                 f
0090: 0A 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00     ..........tlk0. 
```

#### Opcodes

```
  0: 0x008F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               66                 f
00A0: 0A 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
00B0: FF FF 7F F8 FF FF 7F 74  6C 6B 31 00              .......tlk1.    
```

#### Opcodes

```
  0: 0x009F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x00AE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      66 0A 80 F8              f...
00C0: FF FF 7F F8 FF FF 7F 74  68 6B 31 53 F8 FF FF 7F  .......thk1S....
00D0: F8 FF FF 7F 74 68 6B 31  00                       ....thk1.       
```

#### Opcodes

```
  0: 0x00BC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x00CB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x00D8 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D9   |
| Data Size    | 97 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                             66 0A 80 F8 FF FF 7F           f......
00E0: F8 FF FF 7F 74 68 6B 32  53 F8 FF FF 7F F8 FF FF  ....thk2S.......
00F0: 7F 74 68 6B 32 00 3B F8  FF FF 7F 01 00 02 00 03  .thk2.;.........
0100: 00 3A F8 FF FF 7F 04 00  17 05 00 04 00 00 00 16  .:..............
0110: 06 00 04 00 00 00 07 01  00 05 00 07 02 00 06 00  ................
0120: 1B 17 05 00 04 00 00 00  16 06 00 04 00 00 00 07  ................
0130: 01 00 05 00 07 02 00 06  00 1B                    ..........      
```

#### Opcodes

```
  0: 0x00D9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  1: 0x00E8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x00F5 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00F6 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
     0x0101 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
     0x0108 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x010F [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0116 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x011B [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0120 [0x1B] RETURN
     0x0121 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0128 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x012F [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x0134 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0139 [0x1B] RETURN
```
