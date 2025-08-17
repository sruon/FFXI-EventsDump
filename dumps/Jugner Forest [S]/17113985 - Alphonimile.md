# 17113985 - Alphonimile

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 300 bytes                  |
| Total Events     | 10                         |
| References Count | 15                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     28 |              4 |
| [65535.2](#event-655352) | 0x001D       |      7 |              2 |
| [65535.3](#event-655353) | 0x0024       |     15 |              5 |
| [206](#event-206)        | 0x0033       |      1 |              1 |
| [65535.4](#event-655354) | 0x0034       |     35 |              9 |
| [65535.5](#event-655355) | 0x0057       |     35 |              9 |
| [215](#event-215)        | 0x007A       |      1 |              1 |
| [65535.6](#event-655356) | 0x007B       |     22 |              6 |
| [65535.7](#event-655357) | 0x0091       |     37 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x0001      |           1 |
|       2 | 0x13090     |       77968 |
|       3 | 0x4AD65     |      306533 |
|       4 | 0x021E      |         542 |
|       5 | 0x0028      |          40 |
|       6 | 0x000D      |          13 |
|       7 | 0xFFF93E55  |  4294524501 |
|       8 | 0xFFF8CFCB  |  4294496203 |
|       9 | 0x00F4      |         244 |
|      10 | 0x001E      |          30 |
|      11 | 0xFFF937FB  |  4294522875 |
|      12 | 0xFFF8C533  |  4294493491 |
|      13 | 0x0093      |         147 |
|      14 | 0x001D      |          29 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    32 00 80 7E 06 F8 FF  FF 7F 01 80 01 80 01 80   2..~...........
0010: 01 80 01 80 01 80 7E 04  F8 FF FF 7F 00           ......~......   
```

#### Opcodes

```
  0: 0x0001 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0004 [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on EventEntity
  2: 0x0016 [0x7E] CHOCOBO_MOUNT: Mode 4 on EventEntity
  3: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         7E 05 F8               ~..
0020: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x001D [0x7E] CHOCOBO_MOUNT: Dismount EventEntity (status = 0)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 00 80 1F  00 02 80 03 80 04 80 1F      2...........
0030: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=77.968*, Z=306.533*, Y=0.542*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0032 [0x00] END_REQSTACK()
```

### Event 206

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0033  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          00                                          .            
```

#### Opcodes

```
  0: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             03 00 00 25  10 03 01 00 27 10 03 02      ...%....'...
0040: 00 26 10 03 03 00 28 10  32 05 80 1F 00 00 00 01  .&....(.2.......
0050: 00 02 00 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0034 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0039 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[39]
  2: 0x003E [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[38]
  3: 0x0043 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0048 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  6: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0055 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      03  00 00 25 10 03 01 00 27         ...%....'
0060: 10 03 02 00 26 10 03 03  00 28 10 32 06 80 1F 00  ....&....(.2....
0070: 00 00 01 00 02 00 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0057 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x005C [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[39]
  2: 0x0061 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[38]
  3: 0x0066 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x006B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x006E [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  6: 0x0076 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0078 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0079 [0x00] END_REQSTACK()
```

### Event 215

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                00                           .     
```

#### Opcodes

```
  0: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   32 06 80 1F 00             2....
0080: 07 80 08 80 09 80 1F 01  1E F0 FF FF 7F 1C 0A 80  ................
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x007B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007E [0x1F] MOVE_ENTITY: EventEntity moves to X=-442.795*, Z=-471.093*, Y=0.244*
  2: 0x0086 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0088 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x008D [0x1C] WAIT(30* ticks)
  5: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 37 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    32 06 80 1F 00 0B 80  0C 80 0D 80 1F 01 1E 80   2..............
00A0: 23 05 01 1C 0A 80 66 0E  80 81 23 05 01 81 23 05  #.....f...#...#.
00B0: 01 74 6C 6B 30 00                                 .tlk0.          
```

#### Opcodes

```
  0: 0x0091 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0094 [0x1F] MOVE_ENTITY: EventEntity moves to X=-444.421*, Z=-473.805*, Y=0.147*
  2: 0x009C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009E [0x1E] EventEntity looks at Unknown NPC (ID: 17113984/0x01052380) and starts talking
  4: 0x00A3 [0x1C] WAIT(30* ticks)
  5: 0x00A6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Alphonimile (ID: 17113985/0x01052381), Alphonimile (ID: 17113985/0x01052381)], work=29*
  6: 0x00B5 [0x00] END_REQSTACK()
```
