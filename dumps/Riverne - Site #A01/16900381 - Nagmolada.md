# 16900381 - Nagmolada

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Riverne - Site #A01 (ID: 30) |
| Block Size       | 256 bytes                    |
| Total Events     | 4                            |
| References Count | 10                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [100](#event-100)        | 0x000D       |     15 |              3 |
| [65535.1](#event-655351) | 0x001C       |    104 |             21 |
| [65535.2](#event-655352) | 0x0084       |     52 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xA34ED     |      668909 |
|       1 | 0xFFF8D4BC  |  4294497468 |
|       2 | 0xFFFF8372  |  4294935410 |
|       3 | 0x0991      |        2449 |
|       4 | 0x0FA0      |        4000 |
|       5 | 0x000D      |          13 |
|       6 | 0x02CE      |         718 |
|       7 | 0x03E8      |        1000 |
|       8 | 0x0047      |          71 |
|       9 | 0x0000      |           0 |

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
0000: 92 01 F8 FF FF 7F 94 00  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x94] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 100

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 1E F8  E0 01 01 00              ............    
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=668.909*, z=-469.828*, y=-31.886*, direction=215.2°*
  1: 0x0016 [0x1E] EventEntity looks at Spatial Displacement (ID: 16900344/0x0101E0F8) and starts talking
  2: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x001C    |
| Data Size    | 104 bytes |
| Instructions | 16        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      03 00 00 04              ....
0020: 80 1A 40 00 32 05 80 1F  00 01 00 02 00 03 00 1F  ..@.2...........
0030: 01 6F 39 06 80 79 00 F8  FF FF 7F 18 E1 01 01 00  .o9..y..........
0040: 3B F8 FF FF 7F 01 00 02  00 03 00 3A F8 FF FF 7F  ;..........:....
0050: 04 00 17 05 00 04 00 00  00 16 06 00 04 00 00 00  ................
0060: 07 01 00 05 00 07 02 00  06 00 1B 17 05 00 04 00  ................
0070: 00 00 16 06 00 04 00 00  00 07 01 00 05 00 07 02  ................
0080: 00 06 00 1B                                       ....            
```

#### Opcodes

```
  0: 0x001C [0x03] ExtData[1]->WorkLocal[0] = 4000*
  1: 0x0021 [0x1A] CALL_SUBROUTINE(address=0x0040)
  2: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0032 [0x39] SET_ENTITY_DIRECTION(direction=3.9°*)
  7: 0x0035 [0x79] EventEntity looks at Prishe (ID: 16900376/0x0101E118) (Basic look)
  8: 0x003F [0x00] END_REQSTACK()

SUBROUTINE_0040:
  9: 0x0040 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
 10: 0x004B [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
 11: 0x0052 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 12: 0x0059 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 13: 0x0060 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 14: 0x0065 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 15: 0x006A [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x006B [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0072 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0079 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x007E [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0083 [0x1B] RETURN
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             7B F8 FF FF  7F 1E F8 E0 01 01 6F 70      {.........op
0090: 03 00 00 07 80 1A 40 00  32 05 80 1F 00 01 00 02  ......@.2.......
00A0: 00 03 00 1F 01 6F 9F 08  80 F8 FF FF 7F F8 FF FF  .....o..........
00B0: 7F 6D 61 69 6E 09 80 00                           .main...        
```

#### Opcodes

```
  0: 0x0084 [0x7B] EventEntity stops talking
  1: 0x0089 [0x1E] EventEntity looks at Spatial Displacement (ID: 16900344/0x0101E0F8) and starts talking
  2: 0x008E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x008F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0090 [0x03] ExtData[1]->WorkLocal[0] = 1000*
  5: 0x0095 [0x1A] CALL_SUBROUTINE(address=0x0040)
  6: 0x0098 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  7: 0x009B [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  8: 0x00A3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00A5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x00A6 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[71*, 0*]
 11: 0x00B7 [0x00] END_REQSTACK()
```
