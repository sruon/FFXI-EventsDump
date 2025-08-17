# 17723398 - Bacherume

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 256 bytes                     |
| Total Events     | 11                            |
| References Count | 10                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |      1 |              1 |
| [568](#event-568)        | 0x0002       |      1 |              1 |
| [569](#event-569)        | 0x0003       |      1 |              1 |
| [54](#event-54)          | 0x0004       |      1 |              1 |
| [65535.1](#event-655351) | 0x0005       |      4 |              2 |
| [810](#event-810)        | 0x0009       |      1 |              1 |
| [65535.2](#event-655352) | 0x000A       |     27 |              5 |
| [65535.3](#event-655353) | 0x0025       |     25 |              6 |
| [65535.4](#event-655354) | 0x003E       |     84 |             17 |
| [878](#event-878)        | 0x0092       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0400      |        1024 |
|       1 | 0xFFFFF47F  |  4294964351 |
|       2 | 0x180EC     |       98540 |
|       3 | 0x0000      |           0 |
|       4 | 0x07C8      |        1992 |
|       5 | 0xFFFFF830  |  4294965296 |
|       6 | 0x000D      |          13 |
|       7 | 0xFFFFF10D  |  4294963469 |
|       8 | 0x1A3BD     |      107453 |
|       9 | 0xFFFFF448  |  4294964296 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 568

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 569

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 54

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                39 00 80  00                            9...       
```

#### Opcodes

```
  0: 0x0005 [0x39] SET_ENTITY_DIRECTION(direction=5.6°*)
  1: 0x0008 [0x00] END_REQSTACK()
```

### Event 810

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             00                             .      
```

#### Opcodes

```
  0: 0x0009 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000A   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                37 01 80 02 80 03            7.....
0010: 80 04 80 03 00 00 05 80  1A 4E 00 37 01 00 02 00  .........N.7....
0020: 03 00 04 00 00                                    .....           
```

#### Opcodes

```
  0: 0x000A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-2.945*, z=98.540*, y=0.000*, direction=175.1°*
  1: 0x0013 [0x03] ExtData[1]->WorkLocal[0] = 4294965296*
  2: 0x0018 [0x1A] CALL_SUBROUTINE(address=0x004E)
  3: 0x001B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  4: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 06 80  1F 00 01 80 02 80 03 80       2..........
0030: 1F 01 6F 79 00 F8 FF FF  7F F0 FF FF 7F 00        ..oy..........  
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.945*, Z=98.540*, Y=0.000*
  2: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0033 [0x79] EventEntity looks at LocalPlayer (Basic look)
  5: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 84 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            32 06                2.
0040: 80 1F 00 07 80 08 80 09  80 1F 01 22 01 00 3B F8  ..........."..;.
0050: FF FF 7F 01 00 02 00 03  00 3A F8 FF FF 7F 04 00  .........:......
0060: 17 05 00 04 00 00 00 16  06 00 04 00 00 00 07 01  ................
0070: 00 05 00 07 02 00 06 00  1B 17 05 00 04 00 00 00  ................
0080: 16 06 00 04 00 00 00 07  01 00 05 00 07 02 00 06  ................
0090: 00 1B                                             ..              
```

#### Opcodes

```
  0: 0x003E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=-3.827*, Z=107.453*, Y=-3.000*
  2: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004B [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x004D [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x004E [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
     0x0059 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
     0x0060 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0067 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x006E [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x0073 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0078 [0x1B] RETURN
     0x0079 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0080 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0087 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x008C [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0091 [0x1B] RETURN
```

### Event 878

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0092  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0092 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0098 [0x00] END_REQSTACK()
```
