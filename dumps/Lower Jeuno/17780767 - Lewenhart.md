# 17780767 - Lewenhart

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 492 bytes             |
| Total Events     | 14                    |
| References Count | 24                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      6 |              3 |
| [101](#event-101)          | 0x0006       |     10 |              2 |
| [65535.1](#event-655351)   | 0x0010       |     41 |              9 |
| [65535.2](#event-655352)   | 0x0039       |     73 |             15 |
| [65535.3](#event-655353)   | 0x0082       |     19 |              3 |
| [65535.4](#event-655354)   | 0x0095       |     29 |              3 |
| [65535.5](#event-655355)   | 0x00B2       |     19 |              3 |
| [65535.6](#event-655356)   | 0x00C5       |     29 |              3 |
| [65535.7](#event-655357)   | 0x00E2       |     25 |              4 |
| [65535.8](#event-655358)   | 0x00FB       |     35 |              4 |
| [65535.9](#event-655359)   | 0x011E       |      6 |              2 |
| [65535.10](#event-6553510) | 0x0124       |      1 |              1 |
| [65535.11](#event-6553511) | 0x0125       |     14 |              4 |
| [65535.12](#event-6553512) | 0x0133       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFB81C  |  4294948892 |
|       2 | 0xFFFF0CF4  |  4294905076 |
|       3 | 0xFFFFFF9C  |  4294967196 |
|       4 | 0x0D7D      |        3453 |
|       5 | 0xFFFFBB01  |  4294949633 |
|       6 | 0xFFFF11C3  |  4294906307 |
|       7 | 0xFFFFB669  |  4294948457 |
|       8 | 0xFFFF095C  |  4294904156 |
|       9 | 0xFFFF9516  |  4294939926 |
|      10 | 0xFFFF0EA7  |  4294905511 |
|      11 | 0x003C      |          60 |
|      12 | 0xFFFF8A56  |  4294937174 |
|      13 | 0xFFFF11E5  |  4294906341 |
|      14 | 0xFFFFFFDA  |  4294967258 |
|      15 | 0xFFFF7E7F  |  4294934143 |
|      16 | 0xFFFF14FB  |  4294907131 |
|      17 | 0x0000      |           0 |
|      18 | 0xFFFF76F8  |  4294932216 |
|      19 | 0xFFFF0FD5  |  4294905813 |
|      20 | 0xFFFF8788  |  4294936456 |
|      21 | 0xFFFF0DE3  |  4294905315 |
|      22 | 0xFFFF878D  |  4294936461 |
|      23 | 0xFFFF1285  |  4294906501 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 6 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 01 32 00 80 00                                 ".2...          
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   37 01  80 02 80 03 80 04 80 00        7.........
```

#### Opcodes

```
  0: 0x0006 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-18.404*, z=-62.220*, y=-0.100*, direction=303.5°*
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 41 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1F 00 05 80 06 80 03 80  1F 01 6F 1E 1C 50 0F 01  ..........o..P..
0020: 4A 1C 50 0F 01 1F 50 0F  01 6F 76 1C 50 0F 01 4A  J.P...P..ov.P..J
0030: F0 FF FF 7F 1F 50 0F 01  00                       .....P...       
```

#### Opcodes

```
  0: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=-17.663*, Z=-60.989*, Y=-0.100*
  1: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x001B [0x1E] EventEntity looks at Mertaire (ID: 17780764/0x010F501C) and starts talking
  4: 0x0020 [0x4A] Mertaire (ID: 17780764/0x010F501C) looks at Lewenhart (ID: 17780767/0x010F501F)
  5: 0x0029 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x002A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Mertaire (ID: 17780764/0x010F501C) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x002F [0x4A] LocalPlayer looks at Lewenhart (ID: 17780767/0x010F501F)
  8: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 73 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             1F 00 07 80 08 80 03           .......
0040: 80 1F 01 1F 00 09 80 0A  80 03 80 1F 01 27 03 5C  .............'.\
0050: 50 0F 01 09 1C 0B 80 1F  00 0C 80 0D 80 0E 80 1F  P...............
0060: 01 27 04 5C 50 0F 01 0A  1F 00 0F 80 10 80 11 80  .'.\P...........
0070: 1F 01 1F 00 12 80 13 80  11 80 1F 01 7B 1C 50 0F  ............{.P.
0080: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0039 [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.839*, Z=-63.140*, Y=-0.100*
  1: 0x0041 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=-27.370*, Z=-61.785*, Y=-0.100*
  3: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x004D [0x27] REQ_SET(priority=0x03, entity_id=Door:"Merry Minstrel" (ID: 17780828/0x010F505C), tag_num=0x09)
  5: 0x0054 [0x1C] WAIT(60* ticks)
  6: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=-30.122*, Z=-60.955*, Y=-0.038*
  7: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0061 [0x27] REQ_SET(priority=0x04, entity_id=Door:"Merry Minstrel" (ID: 17780828/0x010F505C), tag_num=0x0A)
  9: 0x0068 [0x1F] MOVE_ENTITY: EventEntity moves to X=-33.153*, Z=-60.165*, Y=0.000*
 10: 0x0070 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0072 [0x1F] MOVE_ENTITY: EventEntity moves to X=-35.080*, Z=-61.483*, Y=0.000*
 12: 0x007A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x007C [0x7B] Mertaire (ID: 17780764/0x010F501C) stops talking
 14: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       66 11 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B    f..........tlk
0090: 30 1C 0B 80 00                                    0....           
```

#### Opcodes

```
  0: 0x0082 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  1: 0x0091 [0x1C] WAIT(60* ticks)
  2: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                66 11 80  F8 FF FF 7F F8 FF FF 7F       f..........
00A0: 74 65 6E 30 53 F8 FF FF  7F F8 FF FF 7F 74 65 6E  ten0S........ten
00B0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0095 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [EventEntity, EventEntity], work=0*
  1: 0x00A4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ten0" with entities [EventEntity, EventEntity]
  2: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       66 11 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B    f..........tlk
00C0: 31 1C 0B 80 00                                    1....           
```

#### Opcodes

```
  0: 0x00B2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
  1: 0x00C1 [0x1C] WAIT(60* ticks)
  2: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                66 11 80  F8 FF FF 7F F8 FF FF 7F       f..........
00D0: 74 65 6E 31 53 F8 FF FF  7F F8 FF FF 7F 74 65 6E  ten1S........ten
00E0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x00C5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten1" with entities [EventEntity, EventEntity], work=0*
  1: 0x00D4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ten1" with entities [EventEntity, EventEntity]
  2: 0x00E1 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E2   |
| Data Size    | 25 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:       81 00 F8 FF FF 7F  66 11 80 F8 FF FF 7F F8    ......f.......
00F0: FF FF 7F 74 68 6B 31 1C  0B 80 00                 ...thk1....     
```

#### Opcodes

```
  0: 0x00E2 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x00E8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=0*
  2: 0x00F7 [0x1C] WAIT(60* ticks)
  3: 0x00FA [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FB   |
| Data Size    | 35 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                   81 01 F8 FF FF             .....
0100: 7F 66 11 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32  .f..........thk2
0110: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 00        S........thk2.  
```

#### Opcodes

```
  0: 0x00FB [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  1: 0x0101 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=0*
  2: 0x0110 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  3: 0x011D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011E  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                            5E 69                ^i
0120: 64 6C 30 00                                       dl0.            
```

#### Opcodes

```
  0: 0x011E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0123 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0124  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:             00                                        .           
```

#### Opcodes

```
  0: 0x0124 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0125   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                32 00 80  1F 00 14 80 15 80 11 80       2..........
0130: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0125 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0128 [0x1F] MOVE_ENTITY: EventEntity moves to X=-30.840*, Z=-61.981*, Y=0.000*
  2: 0x0130 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0132 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0133   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          32 00 80 1F 00  16 80 17 80 11 80 1F 01     2............
0140: 00                                                .               
```

#### Opcodes

```
  0: 0x0133 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0136 [0x1F] MOVE_ENTITY: EventEntity moves to X=-30.835*, Z=-60.795*, Y=0.000*
  2: 0x013E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0140 [0x00] END_REQSTACK()
```
