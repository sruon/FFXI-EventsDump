# 16986760 - Salwa-Molwa

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Wajaom Woodlands (ID: 51) |
| Block Size       | 576 bytes                 |
| Total Events     | 20                        |
| References Count | 43                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      9 |              3 |
| [65535.2](#event-655352)   | 0x000A       |      4 |              2 |
| [65535.3](#event-655353)   | 0x000E       |      2 |              2 |
| [65535.4](#event-655354)   | 0x0010       |      9 |              3 |
| [513](#event-513)          | 0x0019       |      1 |              1 |
| [65535.5](#event-655355)   | 0x001A       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0024       |     12 |              4 |
| [65535.7](#event-655357)   | 0x0030       |     12 |              4 |
| [65535.8](#event-655358)   | 0x003C       |     16 |              4 |
| [65535.9](#event-655359)   | 0x004C       |     61 |              9 |
| [65535.10](#event-6553510) | 0x0089       |     16 |              4 |
| [65535.11](#event-6553511) | 0x0099       |     16 |              4 |
| [65535.12](#event-6553512) | 0x00A9       |     19 |              5 |
| [65535.13](#event-6553513) | 0x00BC       |      3 |              2 |
| [65535.14](#event-6553514) | 0x00BF       |      3 |              2 |
| [65535.15](#event-6553515) | 0x00C2       |     32 |              4 |
| [65535.16](#event-6553516) | 0x00E2       |     10 |              2 |
| [65535.17](#event-6553517) | 0x00EC       |     70 |             20 |
| [20](#event-20)            | 0x0132       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0xA7680     |      685696 |
|       2 | 0x35B80     |      220032 |
|       3 | 0xFFFFBBDC  |  4294949852 |
|       4 | 0x0800      |        2048 |
|       5 | 0xA6464     |      681060 |
|       6 | 0x35B1B     |      219931 |
|       7 | 0xFFFFC30F  |  4294951695 |
|       8 | 0xA62F7     |      680695 |
|       9 | 0x3255E     |      206174 |
|      10 | 0xFFFFC207  |  4294951431 |
|      11 | 0x005A      |          90 |
|      12 | 0x00C8      |         200 |
|      13 | 0x003C      |          60 |
|      14 | 0x0102      |         258 |
|      15 | 0x0018      |          24 |
|      16 | 0x0028      |          40 |
|      17 | 0x0015      |          21 |
|      18 | 0x000A      |          10 |
|      19 | 0x0031      |          49 |
|      20 | 0xA47DF     |      673759 |
|      21 | 0x318BA     |      202938 |
|      22 | 0xFFFFC062  |  4294951010 |
|      23 | 0x0AC6      |        2758 |
|      24 | 0xA398A     |      670090 |
|      25 | 0x31B31     |      203569 |
|      26 | 0xFFFFBC86  |  4294950022 |
|      27 | 0x002A      |          42 |
|      28 | 0xA3399     |      668569 |
|      29 | 0x2FF5D     |      196445 |
|      30 | 0xFFFFBA4B  |  4294949451 |
|      31 | 0x002C      |          44 |
|      32 | 0xA2951     |      665937 |
|      33 | 0x30D41     |      200001 |
|      34 | 0xFFFFB9B0  |  4294949296 |
|      35 | 0x002E      |          46 |
|      36 | 0xA19F1     |      662001 |
|      37 | 0x2F77A     |      194426 |
|      38 | 0xFFFFB7A1  |  4294948769 |
|      39 | 0x0032      |          50 |
|      40 | 0x9FA14     |      653844 |
|      41 | 0x2E78F     |      190351 |
|      42 | 0xFFFFB556  |  4294948182 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 00                     "./......      
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                95 00 80 00                  ....  
```

#### Opcodes

```
  0: 0x000A [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 1*)
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            96 00                ..
```

#### Opcodes

```
  0: 0x000E [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 22 01 2F 01 F8 FF FF 7F  00                       "./......       
```

#### Opcodes

```
  0: 0x0010 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0012 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0018 [0x00] END_REQSTACK()
```

### Event 513

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             00                             .      
```

#### Opcodes

```
  0: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                37 01 80 02 80 03            7.....
0020: 80 04 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=685.696*, z=220.032*, y=-17.444*, direction=180.0°*
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             1F 00 05 80  06 80 07 80 1F 01 6F 00      ..........o.
```

#### Opcodes

```
  0: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=681.060*, Z=219.931*, Y=-15.601*
  1: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1F 00 08 80 09 80 0A 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=680.695*, Z=206.174*, Y=-15.865*
  1: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x003A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      6E F8 FF FF              n...
0040: 7F 00 80 99 F8 FF FF 7F  1C 0B 80 00              ............    
```

#### Opcodes

```
  0: 0x003C [0x6E] EventEntity uses emote 1*
  1: 0x0043 [0x99] Wait for EventEntity animation to complete
  2: 0x0048 [0x1C] WAIT(90* ticks)
  3: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 61 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      59 03 F8 FF              Y...
0050: FF 7F 0C 80 79 00 F8 FF  FF 7F 8A 32 03 01 1C 0D  ....y......2....
0060: 80 59 03 F8 FF FF 7F 0C  80 79 00 F8 FF FF 7F F0  .Y.......y......
0070: FF FF 7F 1C 0D 80 59 03  F8 FF FF 7F 0C 80 79 00  ......Y.......y.
0080: F8 FF FF 7F 8A 32 03 01  00                       .....2...       
```

#### Opcodes

```
  0: 0x004C [0x59] UPDATE_ENTITY_DATA: Set EventEntity turn speed head = 200*
  1: 0x0054 [0x79] EventEntity looks at Clavauert (ID: 16986762/0x0103328A) (Basic look)
  2: 0x005E [0x1C] WAIT(60* ticks)
  3: 0x0061 [0x59] UPDATE_ENTITY_DATA: Set EventEntity turn speed head = 200*
  4: 0x0069 [0x79] EventEntity looks at LocalPlayer (Basic look)
  5: 0x0073 [0x1C] WAIT(60* ticks)
  6: 0x0076 [0x59] UPDATE_ENTITY_DATA: Set EventEntity turn speed head = 200*
  7: 0x007E [0x79] EventEntity looks at Clavauert (ID: 16986762/0x0103328A) (Basic look)
  8: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             6E F8 FF FF 7F 0E 80           n......
0090: 99 F8 FF FF 7F 1C 0B 80  00                       .........       
```

#### Opcodes

```
  0: 0x0089 [0x6E] EventEntity uses emote 258*
  1: 0x0090 [0x99] Wait for EventEntity animation to complete
  2: 0x0095 [0x1C] WAIT(90* ticks)
  3: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             6E F8 FF FF 7F 0F 80           n......
00A0: 99 F8 FF FF 7F 1C 0B 80  00                       .........       
```

#### Opcodes

```
  0: 0x0099 [0x6E] EventEntity uses emote 24*
  1: 0x00A0 [0x99] Wait for EventEntity animation to complete
  2: 0x00A5 [0x1C] WAIT(90* ticks)
  3: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             1C 10 80 6E F8 FF FF           ...n...
00B0: 7F 11 80 99 F8 FF FF 7F  1C 0D 80 00              ............    
```

#### Opcodes

```
  0: 0x00A9 [0x1C] WAIT(40* ticks)
  1: 0x00AC [0x6E] EventEntity uses emote 21*
  2: 0x00B3 [0x99] Wait for EventEntity animation to complete
  3: 0x00B8 [0x1C] WAIT(60* ticks)
  4: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BC  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      22 01 00                 ".. 
```

#### Opcodes

```
  0: 0x00BC [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BF  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               22                 "
00C0: 00 00                                             ..              
```

#### Opcodes

```
  0: 0x00BF [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00C1 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C2   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       1C 12 80 66 13 80  F8 FF FF 7F F8 FF FF 7F    ...f..........
00D0: 73 68 61 30 53 F8 FF FF  7F F8 FF FF 7F 73 68 61  sha0S........sha
00E0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x00C2 [0x1C] WAIT(10* ticks)
  1: 0x00C5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=49*
  2: 0x00D4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  3: 0x00E1 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E2   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:       37 14 80 15 80 16  80 17 80 00                7.........    
```

#### Opcodes

```
  0: 0x00E2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=673.759*, z=202.938*, y=-16.286*, direction=242.4°*
  1: 0x00EB [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EC   |
| Data Size    | 70 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      32 10 80 1F              2...
00F0: 00 18 80 19 80 1A 80 1F  01 6F 32 1B 80 1F 00 1C  .........o2.....
0100: 80 1D 80 1E 80 1F 01 6F  32 1F 80 1F 00 20 80 21  .......o2.... .!
0110: 80 22 80 1F 01 6F 32 23  80 1F 00 24 80 25 80 26  ."...o2#...$.%.&
0120: 80 1F 01 6F 32 27 80 1F  00 28 80 29 80 2A 80 1F  ...o2'...(.).*..
0130: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00EC [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00EF [0x1F] MOVE_ENTITY: EventEntity moves to X=670.090*, Z=203.569*, Y=-17.274*
  2: 0x00F7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00FA [0x32] ExtData[1]->MainSpeed = 42* * 0.1
  5: 0x00FD [0x1F] MOVE_ENTITY: EventEntity moves to X=668.569*, Z=196.445*, Y=-17.845*
  6: 0x0105 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0107 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0108 [0x32] ExtData[1]->MainSpeed = 44* * 0.1
  9: 0x010B [0x1F] MOVE_ENTITY: EventEntity moves to X=665.937*, Z=200.001*, Y=-18.000*
 10: 0x0113 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0115 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 12: 0x0116 [0x32] ExtData[1]->MainSpeed = 46* * 0.1
 13: 0x0119 [0x1F] MOVE_ENTITY: EventEntity moves to X=662.001*, Z=194.426*, Y=-18.527*
 14: 0x0121 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 15: 0x0123 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 16: 0x0124 [0x32] ExtData[1]->MainSpeed = 50* * 0.1
 17: 0x0127 [0x1F] MOVE_ENTITY: EventEntity moves to X=653.844*, Z=190.351*, Y=-19.114*
 18: 0x012F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 19: 0x0131 [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0132  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:       00                                            .             
```

#### Opcodes

```
  0: 0x0132 [0x00] END_REQSTACK()
```
