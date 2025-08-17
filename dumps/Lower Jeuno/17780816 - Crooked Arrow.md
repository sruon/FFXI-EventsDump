# 17780816 - Crooked Arrow

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 236 bytes             |
| Total Events     | 5                     |
| References Count | 9                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [70](#event-70)          | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     27 |              5 |
| [65535.2](#event-655352) | 0x0029       |     31 |              9 |
| [65535.3](#event-655353) | 0x0048       |     92 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0031      |          49 |
|       1 | 0x88FE      |       35070 |
|       2 | 0x07CF      |        1999 |
|       3 | 0x0C00      |        3072 |
|       4 | 0xFFFFEC78  |  4294962296 |
|       5 | 0x0023      |          35 |
|       6 | 0x1388      |        5000 |
|       7 | 0x0028      |          40 |
|       8 | 0x3A98      |       15000 |

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

### Event 70

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 92  01 F8 FF FF 7F 00         .............  
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x00] END_REQSTACK()
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
0010: 80 01 80 02 80 03 80 03  00 00 04 80 1A 60 00 37  .............`.7
0020: 01 00 02 00 03 00 04 00  00                       .........       
```

#### Opcodes

```
  0: 0x000E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.049*, z=35.070*, y=1.999*, direction=270.0°*
  1: 0x0017 [0x03] ExtData[1]->WorkLocal[0] = 4294962296*
  2: 0x001C [0x1A] CALL_SUBROUTINE(address=0x0060)
  3: 0x001F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  4: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1C 05 80 03 00 00 06           .......
0030: 80 1A 60 00 32 07 80 1F  00 01 00 02 00 03 00 1F  ..`.2...........
0040: 01 6F 1E 54 50 0F 01 00                           .o.TP...        
```

#### Opcodes

```
  0: 0x0029 [0x1C] WAIT(35* ticks)
  1: 0x002C [0x03] ExtData[1]->WorkLocal[0] = 5000*
  2: 0x0031 [0x1A] CALL_SUBROUTINE(address=0x0060)
  3: 0x0034 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  4: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  5: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0042 [0x1E] EventEntity looks at Nag'molada (ID: 17780820/0x010F5054) and starts talking
  8: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 92 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          03 00 00 08 80 1A 60 00          ......`.
0050: 32 07 80 1F 00 01 00 02  00 03 00 1F 01 22 01 00  2............"..
0060: 3B F8 FF FF 7F 01 00 02  00 03 00 3A F8 FF FF 7F  ;..........:....
0070: 04 00 17 05 00 04 00 00  00 16 06 00 04 00 00 00  ................
0080: 07 01 00 05 00 07 02 00  06 00 1B 17 05 00 04 00  ................
0090: 00 00 16 06 00 04 00 00  00 07 01 00 05 00 07 02  ................
00A0: 00 06 00 1B                                       ....            
```

#### Opcodes

```
  0: 0x0048 [0x03] ExtData[1]->WorkLocal[0] = 15000*
  1: 0x004D [0x1A] CALL_SUBROUTINE(address=0x0060)
  2: 0x0050 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x005D [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x005F [0x00] END_REQSTACK()

SUBROUTINE_0060:
  7: 0x0060 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  8: 0x006B [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  9: 0x0072 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 10: 0x0079 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 11: 0x0080 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 12: 0x0085 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 13: 0x008A [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x008B [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0092 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0099 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x009E [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x00A3 [0x1B] RETURN
```
