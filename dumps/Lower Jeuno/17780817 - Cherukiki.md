# 17780817 - Cherukiki

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 212 bytes             |
| Total Events     | 4                     |
| References Count | 7                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [70](#event-70)          | 0x000D       |      9 |              3 |
| [65535.1](#event-655351) | 0x0016       |     37 |              6 |
| [65535.2](#event-655352) | 0x003B       |     90 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0CC1      |        3265 |
|       1 | 0xA4DD      |       42205 |
|       2 | 0x07CF      |        1999 |
|       3 | 0x061B      |        1563 |
|       4 | 0xFFFFD8F0  |  4294957296 |
|       5 | 0x2AF8      |       11000 |
|       6 | 0x0028      |          40 |

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
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         94 01 F8               ...
0010: FF FF 7F 33 01 00                                 ...3..          
```

#### Opcodes

```
  0: 0x000D [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0013 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 37 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   79 00  F8 FF FF 7F 54 50 0F 01        y.....TP..
0020: 37 00 80 01 80 02 80 03  80 03 00 00 04 80 1A 51  7..............Q
0030: 00 37 01 00 02 00 03 00  04 00 00                 .7.........     
```

#### Opcodes

```
  0: 0x0016 [0x79] EventEntity looks at Nag'molada (ID: 17780820/0x010F5054) (Basic look)
  1: 0x0020 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=3.265*, z=42.205*, y=1.999*, direction=137.4°*
  2: 0x0029 [0x03] ExtData[1]->WorkLocal[0] = 4294957296*
  3: 0x002E [0x1A] CALL_SUBROUTINE(address=0x0051)
  4: 0x0031 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  5: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 90 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   03 00 00 05 80             .....
0040: 1A 51 00 32 06 80 1F 00  01 00 02 00 03 00 1F 01  .Q.2............
0050: 00 3B F8 FF FF 7F 01 00  02 00 03 00 3A F8 FF FF  .;..........:...
0060: 7F 04 00 17 05 00 04 00  00 00 16 06 00 04 00 00  ................
0070: 00 07 01 00 05 00 07 02  00 06 00 1B 17 05 00 04  ................
0080: 00 00 00 16 06 00 04 00  00 00 07 01 00 05 00 07  ................
0090: 02 00 06 00 1B                                    .....           
```

#### Opcodes

```
  0: 0x003B [0x03] ExtData[1]->WorkLocal[0] = 11000*
  1: 0x0040 [0x1A] CALL_SUBROUTINE(address=0x0051)
  2: 0x0043 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0050 [0x00] END_REQSTACK()

SUBROUTINE_0051:
  6: 0x0051 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  7: 0x005C [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  8: 0x0063 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
  9: 0x006A [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
 10: 0x0071 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
 11: 0x0076 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
 12: 0x007B [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x007C [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0083 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x008A [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x008F [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0094 [0x1B] RETURN
```
