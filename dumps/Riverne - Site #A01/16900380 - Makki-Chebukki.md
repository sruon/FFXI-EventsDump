# 16900380 - Makki-Chebukki

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Riverne - Site #A01 (ID: 30) |
| Block Size       | 312 bytes                    |
| Total Events     | 7                            |
| References Count | 12                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [100](#event-100)        | 0x000D       |     15 |              3 |
| [65535.1](#event-655351) | 0x001C       |     90 |             18 |
| [65535.2](#event-655352) | 0x0076       |     51 |             11 |
| [65535.3](#event-655353) | 0x00A9       |     16 |              2 |
| [65535.4](#event-655354) | 0x00B9       |     16 |              2 |
| [65535.5](#event-655355) | 0x00C9       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xA4901     |      674049 |
|       1 | 0xFFF8C020  |  4294492192 |
|       2 | 0xFFFF838C  |  4294935436 |
|       3 | 0x09AA      |        2474 |
|       4 | 0x0BB8      |        3000 |
|       5 | 0x000D      |          13 |
|       6 | 0x2710      |       10000 |
|       7 | 0x0028      |          40 |
|       8 | 0x0047      |          71 |
|       9 | 0x0000      |           0 |
|      10 | 0x0150      |         336 |
|      11 | 0x01B9      |         441 |

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
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=674.049*, z=-475.104*, y=-31.860*, direction=217.4°*
  1: 0x0016 [0x1E] EventEntity looks at Spatial Displacement (ID: 16900344/0x0101E0F8) and starts talking
  2: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 90 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      03 00 00 04              ....
0020: 80 1A 32 00 32 05 80 1F  00 01 00 02 00 03 00 1F  ..2.2...........
0030: 01 00 3B F8 FF FF 7F 01  00 02 00 03 00 3A F8 FF  ..;..........:..
0040: FF 7F 04 00 17 05 00 04  00 00 00 16 06 00 04 00  ................
0050: 00 00 07 01 00 05 00 07  02 00 06 00 1B 17 05 00  ................
0060: 04 00 00 00 16 06 00 04  00 00 00 07 01 00 05 00  ................
0070: 07 02 00 06 00 1B                                 ......          
```

#### Opcodes

```
  0: 0x001C [0x03] ExtData[1]->WorkLocal[0] = 3000*
  1: 0x0021 [0x1A] CALL_SUBROUTINE(address=0x0032)
  2: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0031 [0x00] END_REQSTACK()

SUBROUTINE_0032:
  6: 0x0032 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  7: 0x003D [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  8: 0x0044 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
  9: 0x004B [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 10: 0x0052 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 11: 0x0057 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 12: 0x005C [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x005D [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0064 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x006B [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x0070 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0075 [0x1B] RETURN
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 51 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   5E 69  64 6C 30 1E F8 E0 01 01        ^idl0.....
0080: 6F 70 03 00 00 06 80 1A  32 00 32 07 80 1F 00 01  op......2.2.....
0090: 00 02 00 03 00 1F 01 9F  08 80 F8 FF FF 7F F8 FF  ................
00A0: FF 7F 6D 61 69 6E 09 80  00                       ..main...       
```

#### Opcodes

```
  0: 0x0076 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x007B [0x1E] EventEntity looks at Spatial Displacement (ID: 16900344/0x0101E0F8) and starts talking
  2: 0x0080 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0081 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0082 [0x03] ExtData[1]->WorkLocal[0] = 10000*
  5: 0x0087 [0x1A] CALL_SUBROUTINE(address=0x0032)
  6: 0x008A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  7: 0x008D [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  8: 0x0095 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0097 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[71*, 0*]
 10: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             5B 0A 80 F8 FF FF 7F           [......
00B0: F8 FF FF 7F 7A 69 74 30  00                       ....zit0.       
```

#### Opcodes

```
  0: 0x00A9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "zit0" with entities [EventEntity, EventEntity], work=336*
  1: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             5B 0B 80 F8 FF FF 7F           [......
00C0: F8 FF FF 7F 64 66 6D 30  00                       ....dfm0.       
```

#### Opcodes

```
  0: 0x00B9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dfm0" with entities [EventEntity, EventEntity], work=441*
  1: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             5B 0B 80 F8 FF FF 7F           [......
00D0: F8 FF FF 7F 64 66 6D 30  00                       ....dfm0.       
```

#### Opcodes

```
  0: 0x00C9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dfm0" with entities [EventEntity, EventEntity], work=441*
  1: 0x00D8 [0x00] END_REQSTACK()
```
