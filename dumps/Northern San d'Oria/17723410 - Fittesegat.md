# 17723410 - Fittesegat

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 380 bytes                     |
| Total Events     | 15                            |
| References Count | 24                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [38](#event-38)          | 0x0001       |      1 |              1 |
| [51](#event-51)          | 0x0002       |     19 |              3 |
| [65535.1](#event-655351) | 0x0015       |     10 |              2 |
| [65535.2](#event-655352) | 0x001F       |     10 |              2 |
| [1](#event-1)            | 0x0029       |      3 |              2 |
| [589](#event-589)        | 0x002C       |      1 |              1 |
| [65535.3](#event-655353) | 0x002D       |     20 |              6 |
| [693](#event-693)        | 0x0041       |      1 |              1 |
| [639](#event-639)        | 0x0042       |      1 |              1 |
| [65535.4](#event-655354) | 0x0043       |     42 |             10 |
| [16](#event-16)          | 0x006D       |     48 |              8 |
| [0](#event-0)            | 0x009D       |     28 |              5 |
| [869](#event-869)        | 0x00B9       |     10 |              2 |
| [870](#event-870)        | 0x00C3       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x22F60     |      143200 |
|       1 | 0x21B10     |      138000 |
|       2 | 0x0000      |           0 |
|       3 | 0x0E00      |        3584 |
|       4 | 0x000D      |          13 |
|       5 | 0x001E      |          30 |
|       6 | 0x003C      |          60 |
|       7 | 0x225E0     |      140768 |
|       8 | 0x21F40     |      139072 |
|       9 | 0x00AB      |         171 |
|      10 | 0x0008      |           8 |
|      11 | 0x17042     |       94274 |
|      12 | 0x11D82     |       73090 |
|      13 | 0x06D5      |        1749 |
|      14 | 0x0B88      |        2952 |
|      15 | 0x16761     |       92001 |
|      16 | 0x12839     |       75833 |
|      17 | 0x0BC1      |        3009 |
|      18 | 0xFFFFD484  |  4294956164 |
|      19 | 0x0D7F      |        3455 |
|      20 | 0xFFFFFF39  |  4294967097 |
|      21 | 0x22B3B     |      142139 |
|      22 | 0x220FA     |      139514 |
|      23 | 0x0484      |        1156 |

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

### Event 38

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

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       3B F8 FF FF 7F 00  00 01 00 02 00 3A F8 FF    ;..........:..
0010: FF 7F 03 00 00                                    .....           
```

#### Opcodes

```
  0: 0x0002 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x000D [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[3])
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                37 00 00  01 00 02 00 03 00 00          7......... 
```

#### Opcodes

```
  0: 0x0015 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               37                 7
0020: 00 80 01 80 02 80 03 80  00                       .........       
```

#### Opcodes

```
  0: 0x001F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=143.200*, z=138.000*, y=0.000*, direction=315.0°*
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             22 01 00                       "..    
```

#### Opcodes

```
  0: 0x0029 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 589

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      00                       .   
```

#### Opcodes

```
  0: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 04 80               2..
0030: 1F 00 00 80 01 80 02 80  1F 01 1C 05 80 39 03 80  .............9..
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=143.200*, Z=138.000*, Y=0.000*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x1C] WAIT(30* ticks)
  4: 0x003D [0x39] SET_ENTITY_DIRECTION(direction=19.7°*)
  5: 0x0040 [0x00] END_REQSTACK()
```

### Event 693

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0041  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    00                                              .              
```

#### Opcodes

```
  0: 0x0041 [0x00] END_REQSTACK()
```

### Event 639

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0042  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       00                                            .             
```

#### Opcodes

```
  0: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          1C 06 80 4A 13  70 0E 01 03 70 0E 01 6F     ...J.p...p..o
0050: 76 13 70 0E 01 1C 06 80  32 04 80 1F 00 07 80 08  v.p.....2.......
0060: 80 02 80 1F 01 4B 12 70  0E 01 09 80 00           .....K.p.....   
```

#### Opcodes

```
  0: 0x0043 [0x1C] WAIT(60* ticks)
  1: 0x0046 [0x4A] Prerivon (ID: 17723411/0x010E7013) looks at Pieuje (ID: 17723395/0x010E7003)
  2: 0x004F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0050 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Prerivon (ID: 17723411/0x010E7013) Render.Flags0 and Render.Flags3 conditions are met
  4: 0x0055 [0x1C] WAIT(60* ticks)
  5: 0x0058 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  6: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=140.768*, Z=139.072*, Y=0.000*
  7: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0065 [0x4B] UPDATE_ENTITY_YAW(entity=Fittesegat (ID: 17723410/0x010E7012), yaw=0.9°*)
  9: 0x006C [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 48 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         22 00 92               "..
0070: 01 F8 FF FF 7F 02 87 7F  0A 80 00 89 00 37 0B 80  .............7..
0080: 0C 80 0D 80 0E 80 01 92  00 37 0F 80 10 80 0D 80  .........7......
0090: 11 80 79 00 F8 FF FF 7F  04 70 0E 01 00           ..y......p...   
```

#### Opcodes

```
  0: 0x006D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x006F [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0075 [0x02] IF !(LocalPlayer->Race == 8*) GOTO 0x0089
  3: 0x007D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=94.274*, z=73.090*, y=1.749*, direction=259.4°*
  4: 0x0086 [0x01] GOTO 0x0092
  5: 0x0089 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=92.001*, z=75.833*, y=1.749*, direction=264.5°*

SUBROUTINE_0092:
  6: 0x0092 [0x79] EventEntity looks at Claidie (ID: 17723396/0x010E7004) (Basic look)
  7: 0x009C [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         22 00 92               "..
00A0: 01 F8 FF FF 7F 37 12 80  13 80 14 80 02 80 79 00  .....7........y.
00B0: F8 FF FF 7F 02 70 0E 01  00                       .....p...       
```

#### Opcodes

```
  0: 0x009D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x009F [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x00A5 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-11.132*, z=3.455*, y=-0.199*, direction=0.0°*
  3: 0x00AE [0x79] EventEntity looks at Trion (ID: 17723394/0x010E7002) (Basic look)
  4: 0x00B8 [0x00] END_REQSTACK()
```

### Event 869

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             37 15 80 16 80 02 80           7......
00C0: 17 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00B9 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=142.139*, z=139.514*, y=0.000*, direction=101.6°*
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 870

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          37 15 80 16 80  02 80 17 80 00              7.........   
```

#### Opcodes

```
  0: 0x00C3 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=142.139*, z=139.514*, y=0.000*, direction=101.6°*
  1: 0x00CC [0x00] END_REQSTACK()
```
