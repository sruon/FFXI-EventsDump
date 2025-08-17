# 17731662 - Bacherume

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 540 bytes                     |
| Total Events     | 16                            |
| References Count | 35                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [563](#event-563)          | 0x0001       |     21 |              2 |
| [65535.1](#event-655351)   | 0x0016       |     10 |              2 |
| [65535.2](#event-655352)   | 0x0020       |     39 |             11 |
| [112](#event-112)          | 0x0047       |     16 |              3 |
| [65535.3](#event-655353)   | 0x0057       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0065       |     25 |              5 |
| [65535.5](#event-655355)   | 0x007E       |     13 |              3 |
| [65535.6](#event-655356)   | 0x008B       |      6 |              2 |
| [43](#event-43)            | 0x0091       |     12 |              3 |
| [65535.7](#event-655357)   | 0x009D       |     20 |              6 |
| [65535.8](#event-655358)   | 0x00B1       |     26 |              7 |
| [65535.9](#event-655359)   | 0x00CB       |     29 |              3 |
| [65535.10](#event-6553510) | 0x00E8       |     29 |              3 |
| [65535.11](#event-6553511) | 0x0105       |     29 |              3 |
| [65535.12](#event-6553512) | 0x0122       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x0008      |           8 |
|       2 | 0x001A      |          26 |
|       3 | 0x001C      |          28 |
|       4 | 0x0000      |           0 |
|       5 | 0x0173      |         371 |
|       6 | 0xFFFFFCEF  |  4294966511 |
|       7 | 0x0DC6      |        3526 |
|       8 | 0x0028      |          40 |
|       9 | 0x0002      |           2 |
|      10 | 0x0078      |         120 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFFFC8AA  |  4294953130 |
|      13 | 0x0FC5      |        4037 |
|      14 | 0xFFFFFD1E  |  4294966558 |
|      15 | 0x0853      |        2131 |
|      16 | 0x09E4      |        2532 |
|      17 | 0xFFFFFEF8  |  4294967032 |
|      18 | 0x03C3      |         963 |
|      19 | 0xFFFFE9FD  |  4294961661 |
|      20 | 0x003C      |          60 |
|      21 | 0x0428      |        1064 |
|      22 | 0x001B      |          27 |
|      23 | 0xFFFFC84B  |  4294953035 |
|      24 | 0x5D99      |       23961 |
|      25 | 0xFFFFF177  |  4294963575 |
|      26 | 0x0E2C      |        3628 |
|      27 | 0x6188      |       24968 |
|      28 | 0xFFFFF4BC  |  4294964412 |
|      29 | 0x000A      |          10 |
|      30 | 0x576A      |       22378 |
|      31 | 0xFFFFEE51  |  4294962769 |
|      32 | 0x3D90      |       15760 |
|      33 | 0xFFFFEDB1  |  4294962609 |
|      34 | 0x001D      |          29 |

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

### Event 563

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 0B 00 80 01 80 02  80 03 80 02 80 03 80 02   ...............
0010: 80 04 80 04 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=8*, head=26*, body=28*, hands=26*, legs=28*, feet=26*, main=0*, sub=0*)
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   37 05  80 06 80 04 80 07 80 00        7.........
```

#### Opcodes

```
  0: 0x0016 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.371*, z=-0.785*, y=0.000*, direction=309.9°*
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 39 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 1C 08 80 1E 08 90 0E 01  6F 70 6E F8 FF FF 7F 09  ........opn.....
0030: 80 99 F8 FF FF 7F 1C 0A  80 32 0B 80 1F 00 05 80  .........2......
0040: 0C 80 04 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0020 [0x1C] WAIT(40* ticks)
  1: 0x0023 [0x1E] EventEntity looks at Rahal (ID: 17731592/0x010E9008) and starts talking
  2: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0029 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x002A [0x6E] EventEntity uses emote 2*
  5: 0x0031 [0x99] Wait for EventEntity animation to complete
  6: 0x0036 [0x1C] WAIT(120* ticks)
  7: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  8: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=0.371*, Z=-14.166*, Y=0.000*
  9: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x0046 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      94  01 F8 FF FF 7F 37 0D 80         ......7..
0050: 0E 80 04 80 0F 80 00                              .......         
```

#### Opcodes

```
  0: 0x0047 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x004D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=4.037*, z=-0.738*, y=0.000*, direction=187.3°*
  2: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      32  08 80 1F 00 10 80 11 80         2........
0060: 04 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0057 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=2.532*, Z=-0.264*, Y=0.000*
  2: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 25 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                32 0B 80  31 00 12 80 13 80 04 80       2..1.......
0070: 14 80 31 01 37 12 80 13  80 04 80 15 80 00        ..1.7.........  
```

#### Opcodes

```
  0: 0x0065 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0068 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=0.963*, Z=-5.635*, Y=0.000*, Time=60*
  2: 0x0072 [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  3: 0x0074 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.963*, z=-5.635*, y=0.000*, direction=93.5°*
  4: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            31 00                1.
0080: 16 80 17 80 04 80 14 80  31 01 00                 ........1..     
```

#### Opcodes

```
  0: 0x007E [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=0.027*, Z=-14.261*, Y=0.000*, Time=60*
  1: 0x0088 [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  2: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008B  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   1E 51 90 0E 01             .Q...
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x008B [0x1E] EventEntity looks at Vijartal (ID: 17731665/0x010E9051) and starts talking
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    22 01 37 18 80 19 80  04 80 1A 80 00            ".7.........   
```

#### Opcodes

```
  0: 0x0091 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0093 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.961*, z=-3.721*, y=0.000*, direction=318.9°*
  2: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         32 0B 80               2..
00A0: 1F 00 1B 80 1C 80 04 80  1F 01 6F 1E 0C 90 0E 01  ..........o.....
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x009D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A0 [0x1F] MOVE_ENTITY: EventEntity moves to X=24.968*, Z=-2.884*, Y=0.000*
  2: 0x00A8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AB [0x1E] EventEntity looks at Curilla (ID: 17731596/0x010E900C) and starts talking
  5: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    1C 1D 80 1F 00 1E 80  1F 80 04 80 1F 01 1F 00   ...............
00C0: 20 80 21 80 04 80 1F 01  22 01 00                  .!....."..     
```

#### Opcodes

```
  0: 0x00B1 [0x1C] WAIT(10* ticks)
  1: 0x00B4 [0x1F] MOVE_ENTITY: EventEntity moves to X=22.378*, Z=-4.527*, Y=0.000*
  2: 0x00BC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BE [0x1F] MOVE_ENTITY: EventEntity moves to X=15.760*, Z=-4.687*, Y=0.000*
  4: 0x00C6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00C8 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x00CA [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CB   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                   66 22 80 F8 FF             f"...
00D0: FF 7F F8 FF FF 7F 74 6C  6B 30 53 F8 FF FF 7F F8  ......tlk0S.....
00E0: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x00CB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x00DA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x00E7 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E8   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                          66 22 80 F8 FF FF 7F F8          f"......
00F0: FF FF 7F 74 6C 6B 31 53  F8 FF FF 7F F8 FF FF 7F  ...tlk1S........
0100: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x00E8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x00F7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x0104 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0105   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                66 22 80  F8 FF FF 7F F8 FF FF 7F       f".........
0110: 74 68 6B 31 53 F8 FF FF  7F F8 FF FF 7F 74 68 6B  thk1S........thk
0120: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0105 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0114 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x0121 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0122   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:       66 22 80 F8 FF FF  7F F8 FF FF 7F 74 68 6B    f".........thk
0130: 32 53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     2S........thk2. 
```

#### Opcodes

```
  0: 0x0122 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  1: 0x0131 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x013E [0x00] END_REQSTACK()
```
