# 17113968 - Kingslayer Doggvdegg

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 304 bytes                  |
| Total Events     | 15                         |
| References Count | 14                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [204](#event-204)        | 0x0001       |      1 |              1 |
| [205](#event-205)        | 0x0002       |      1 |              1 |
| [206](#event-206)        | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     35 |              9 |
| [65535.2](#event-655352) | 0x0027       |     35 |              9 |
| [211](#event-211)        | 0x004A       |      1 |              1 |
| [65535.3](#event-655353) | 0x004B       |      5 |              2 |
| [65535.4](#event-655354) | 0x0050       |      5 |              2 |
| [65535.5](#event-655355) | 0x0055       |     35 |              9 |
| [215](#event-215)        | 0x0078       |      1 |              1 |
| [65535.6](#event-655356) | 0x0079       |     14 |              4 |
| [65535.7](#event-655357) | 0x0087       |      9 |              3 |
| [65535.8](#event-655358) | 0x0090       |     14 |              4 |
| [65535.9](#event-655359) | 0x009E       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x000D      |          13 |
|       2 | 0x0078      |         120 |
|       3 | 0x0064      |         100 |
|       4 | 0x0012      |          18 |
|       5 | 0xFFF94086  |  4294525062 |
|       6 | 0xFFF8F439  |  4294505529 |
|       7 | 0x038F      |         911 |
|       8 | 0xFFF9F450  |  4294571088 |
|       9 | 0xFFF95F49  |  4294532937 |
|      10 | 0xFFFFFFE1  |  4294967265 |
|      11 | 0xFFF9D314  |  4294562580 |
|      12 | 0xFFF9B048  |  4294553672 |
|      13 | 0x0352      |         850 |

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

### Event 204

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

### Event 205

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

### Event 206

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             03 00 00 25  10 03 01 00 27 10 03 02      ...%....'...
0010: 00 26 10 03 03 00 28 10  32 00 80 1F 00 00 00 01  .&....(.2.......
0020: 00 02 00 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0004 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0009 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[39]
  2: 0x000E [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[38]
  3: 0x0013 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0018 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  6: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      03  00 00 25 10 03 01 00 27         ...%....'
0030: 10 03 02 00 26 10 03 03  00 28 10 32 01 80 1F 00  ....&....(.2....
0040: 00 00 01 00 02 00 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0027 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x002C [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[39]
  2: 0x0031 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[38]
  3: 0x0036 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x003B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  6: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0048 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0049 [0x00] END_REQSTACK()
```

### Event 211

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                00                           .     
```

#### Opcodes

```
  0: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004B  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   B6 0F 02 80 00             .....
```

#### Opcodes

```
  0: 0x004B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=120*)
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0050  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: B6 0F 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0050 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=100*)
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                03 00 00  25 10 03 01 00 27 10 03       ...%....'..
0060: 02 00 26 10 03 03 00 28  10 32 04 80 1F 00 00 00  ..&....(.2......
0070: 01 00 02 00 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0055 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x005A [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[39]
  2: 0x005F [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[38]
  3: 0x0064 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0069 [0x32] ExtData[1]->MainSpeed = 18* * 0.1
  5: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  6: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0077 [0x00] END_REQSTACK()
```

### Event 215

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0078  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          00                               .       
```

#### Opcodes

```
  0: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             32 01 80 1F 00 05 80           2......
0080: 06 80 07 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0079 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007C [0x1F] MOVE_ENTITY: EventEntity moves to X=-442.234*, Z=-461.767*, Y=0.911*
  2: 0x0084 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0087  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      1C  02 80 1E 56 23 05 01 00         ....V#...
```

#### Opcodes

```
  0: 0x0087 [0x1C] WAIT(120* ticks)
  1: 0x008A [0x1E] EventEntity looks at Zogbog (ID: 17113942/0x01052356) and starts talking
  2: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 32 00 80 5A 00 08 80 09  80 0A 80 5A 01 00        2..Z.......Z..  
```

#### Opcodes

```
  0: 0x0090 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0093 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-396.208*, Z=-434.359*, Y=-0.031*
  2: 0x009B [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            32 00                2.
00A0: 80 5A 00 0B 80 0C 80 0D  80 5A 01 00              .Z.......Z..    
```

#### Opcodes

```
  0: 0x009E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A1 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-404.716*, Z=-413.624*, Y=0.850*
  2: 0x00A9 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00AB [0x00] END_REQSTACK()
```
