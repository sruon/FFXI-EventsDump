# 17780820 - Nagmolada

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 260 bytes             |
| Total Events     | 7                     |
| References Count | 9                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [70](#event-70)          | 0x000D       |      1 |              1 |
| [65535.1](#event-655351) | 0x000E       |     27 |              5 |
| [65535.2](#event-655352) | 0x0029       |     90 |             18 |
| [23](#event-23)          | 0x0083       |      1 |              1 |
| [65535.3](#event-655353) | 0x0084       |     19 |              3 |
| [65535.4](#event-655354) | 0x0097       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0A5A      |        2650 |
|       1 | 0x9D9E      |       40350 |
|       2 | 0x07CF      |        1999 |
|       3 | 0x063A      |        1594 |
|       4 | 0xFFFFF830  |  4294965296 |
|       5 | 0x0FA0      |        4000 |
|       6 | 0x000D      |          13 |
|       7 | 0x01D1      |         465 |
|       8 | 0x001E      |          30 |

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

### Event 70

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         00                     .  
```

#### Opcodes

```
  0: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            37 00                7.
0010: 80 01 80 02 80 03 80 03  00 00 04 80 1A 3F 00 37  .............?.7
0020: 01 00 02 00 03 00 04 00  00                       .........       
```

#### Opcodes

```
  0: 0x000E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=2.650*, z=40.350*, y=1.999*, direction=140.1°*
  1: 0x0017 [0x03] ExtData[1]->WorkLocal[0] = 4294965296*
  2: 0x001C [0x1A] CALL_SUBROUTINE(address=0x003F)
  3: 0x001F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  4: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 90 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             03 00 00 05 80 1A 3F           ......?
0030: 00 32 06 80 1F 00 01 00  02 00 03 00 1F 01 00 3B  .2.............;
0040: F8 FF FF 7F 01 00 02 00  03 00 3A F8 FF FF 7F 04  ..........:.....
0050: 00 17 05 00 04 00 00 00  16 06 00 04 00 00 00 07  ................
0060: 01 00 05 00 07 02 00 06  00 1B 17 05 00 04 00 00  ................
0070: 00 16 06 00 04 00 00 00  07 01 00 05 00 07 02 00  ................
0080: 06 00 1B                                          ...             
```

#### Opcodes

```
  0: 0x0029 [0x03] ExtData[1]->WorkLocal[0] = 4000*
  1: 0x002E [0x1A] CALL_SUBROUTINE(address=0x003F)
  2: 0x0031 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x003E [0x00] END_REQSTACK()

SUBROUTINE_003F:
  6: 0x003F [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  7: 0x004A [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  8: 0x0051 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
  9: 0x0058 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 10: 0x005F [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 11: 0x0064 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 12: 0x0069 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x006A [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0071 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0078 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x007D [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0082 [0x1B] RETURN
```

### Event 23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0083  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          00                                          .            
```

#### Opcodes

```
  0: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             5B 07 80 F8  FF FF 7F F8 FF FF 7F 74      [..........t
0090: 6C 61 30 1C 08 80 00                              la0....         
```

#### Opcodes

```
  0: 0x0084 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=465*
  1: 0x0093 [0x1C] WAIT(30* ticks)
  2: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      5B  07 80 F8 FF FF 7F F8 FF         [........
00A0: FF 7F 74 6C 61 31 53 F8  FF FF 7F F8 FF FF 7F 74  ..tla1S........t
00B0: 6C 61 31 00                                       la1.            
```

#### Opcodes

```
  0: 0x0097 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=465*
  1: 0x00A6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tla1" with entities [EventEntity, EventEntity]
  2: 0x00B3 [0x00] END_REQSTACK()
```
