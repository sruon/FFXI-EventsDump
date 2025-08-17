# 17723567 - Rainemard

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 608 bytes                     |
| Total Events     | 17                            |
| References Count | 42                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      4 |              2 |
| [37](#event-37)            | 0x0004       |     12 |              3 |
| [49](#event-49)            | 0x0010       |     24 |              5 |
| [65535.1](#event-655351)   | 0x0028       |     24 |              6 |
| [65535.2](#event-655352)   | 0x0040       |     58 |              9 |
| [65535.3](#event-655353)   | 0x007A       |     16 |              4 |
| [65535.4](#event-655354)   | 0x008A       |     26 |              5 |
| [65535.5](#event-655355)   | 0x00A4       |     10 |              2 |
| [65535.6](#event-655356)   | 0x00AE       |     29 |              4 |
| [65535.7](#event-655357)   | 0x00CB       |     27 |              3 |
| [65535.8](#event-655358)   | 0x00E6       |     11 |              3 |
| [65535.9](#event-655359)   | 0x00F1       |     29 |              3 |
| [65535.10](#event-6553510) | 0x010E       |     11 |              2 |
| [65535.11](#event-6553511) | 0x0119       |      7 |              3 |
| [65535.12](#event-6553512) | 0x0120       |     20 |              4 |
| [65535.13](#event-6553513) | 0x0134       |     37 |             10 |
| [65535.14](#event-6553514) | 0x0159       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x1FACD     |      129741 |
|       2 | 0x1DBAF     |      121775 |
|       3 | 0x1963      |        6499 |
|       4 | 0x0DFC      |        3580 |
|       5 | 0x0040      |          64 |
|       6 | 0x0000      |           0 |
|       7 | 0x1C3E4     |      115684 |
|       8 | 0x1A4A9     |      107689 |
|       9 | 0x05F6      |        1526 |
|      10 | 0x20498     |      132248 |
|      11 | 0x1E545     |      124229 |
|      12 | 0x1B614     |      112148 |
|      13 | 0x19701     |      104193 |
|      14 | 0x1A389     |      107401 |
|      15 | 0x18440     |       99392 |
|      16 | 0x1964A     |      104010 |
|      17 | 0x177A7     |       96167 |
|      18 | 0x06D5      |        1749 |
|      19 | 0x0624      |        1572 |
|      20 | 0x192E8     |      103144 |
|      21 | 0x174A7     |       95399 |
|      22 | 0x005A      |          90 |
|      23 | 0x0060      |          96 |
|      24 | 0x0621      |        1569 |
|      25 | 0x18E39     |      101945 |
|      26 | 0x16FB9     |       94137 |
|      27 | 0x0014      |          20 |
|      28 | 0x0DE8      |        3560 |
|      29 | 0x195C7     |      103879 |
|      30 | 0x1762D     |       95789 |
|      31 | 0x1A4AB     |      107691 |
|      32 | 0x1854C     |       99660 |
|      33 | 0x0E17      |        3607 |
|      34 | 0x1A62B     |      108075 |
|      35 | 0x18790     |      100240 |
|      36 | 0x0291      |         657 |
|      37 | 0x003C      |          60 |
|      38 | 0x0078      |         120 |
|      39 | 0x0E1D      |        3613 |
|      40 | 0x1CA8C     |      117388 |
|      41 | 0x1AAB8     |      109240 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 32 00 80 00                                       2...            
```

#### Opcodes

```
  0: 0x0000 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             22 01 37 01  80 02 80 03 80 04 80 00      ".7.........
```

#### Opcodes

```
  0: 0x0004 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0006 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=129.741*, z=121.775*, y=6.499*, direction=314.6°*
  2: 0x000F [0x00] END_REQSTACK()
```

### Event 49

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 22 01 32 00 80 6C F8 FF  FF 7F 05 80 06 80 37 07  ".2..l........7.
0020: 80 08 80 06 80 09 80 00                           ........        
```

#### Opcodes

```
  0: 0x0010 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0012 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0015 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=64*, fade_time=0*)
  3: 0x001E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=115.684*, z=107.689*, y=0.000*, direction=134.1°*
  4: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          61 00 22 00 6C F8 FF FF          a.".l...
0030: 7F 05 80 06 80 1F 00 0A  80 0B 80 03 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x0028 [0x61] EventEntity->Render.Flags2 &= ~0x00000001
  1: 0x002A [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x002C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=64*, fade_time=0*)
  3: 0x0035 [0x1F] MOVE_ENTITY: EventEntity moves to X=132.248*, Z=124.229*, Y=6.499*
  4: 0x003D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 58 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 4E 00 AF 70 0E 01 1F 00  0C 80 0D 80 06 80 1F 01  N..p............
0050: 4A AF 70 0E 01 29 70 0E  01 6F 76 AF 70 0E 01 2C  J.p..)p..ov.p..,
0060: F8 FF FF 7F F8 FF FF 7F  73 68 62 6B 53 F8 FF FF  ........shbkS...
0070: 7F F8 FF FF 7F 73 68 62  6B 00                    .....shbk.      
```

#### Opcodes

```
  0: 0x0040 [0x4E] SET_ENTITY_HIDE_FLAG: Show Rainemard (ID: 17723567/0x010E70AF)
  1: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=112.148*, Z=104.193*, Y=0.000*
  2: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0050 [0x4A] Rainemard (ID: 17723567/0x010E70AF) looks at Aurege (ID: 17723433/0x010E7029)
  4: 0x0059 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x005A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rainemard (ID: 17723567/0x010E70AF) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x005F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "shbk" with entities [EventEntity, EventEntity]
  7: 0x006C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shbk" with entities [EventEntity, EventEntity]
  8: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                7B F8 FF FF 7F 1F            {.....
0080: 00 0E 80 0F 80 06 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x007A [0x7B] EventEntity stops talking
  1: 0x007F [0x1F] MOVE_ENTITY: EventEntity moves to X=107.401*, Z=99.392*, Y=0.000*
  2: 0x0087 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 26 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                92 01 F8 FF FF 7F            ......
0090: 37 10 80 11 80 12 80 13  80 1F 00 14 80 15 80 12  7...............
00A0: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x008A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0090 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=104.010*, z=96.167*, y=1.749*, direction=138.2°*
  2: 0x0099 [0x1F] MOVE_ENTITY: EventEntity moves to X=103.144*, Z=95.399*, Y=1.749*
  3: 0x00A1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             6C AF 70 0E  01 06 80 16 80 00            l.p.......  
```

#### Opcodes

```
  0: 0x00A4 [0x6C] FADE_ENTITY_COLOR(entity_id=Rainemard (ID: 17723567/0x010E70AF), end_alpha=0*, fade_time=90*)
  1: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            6C AF                l.
00B0: 70 0E 01 17 80 06 80 37  14 80 15 80 12 80 18 80  p......7........
00C0: 79 00 F8 FF FF 7F B0 70  0E 01 00                 y......p...     
```

#### Opcodes

```
  0: 0x00AE [0x6C] FADE_ENTITY_COLOR(entity_id=Rainemard (ID: 17723567/0x010E70AF), end_alpha=96*, fade_time=0*)
  1: 0x00B7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=103.144*, z=95.399*, y=1.749*, direction=137.9°*
  2: 0x00C0 [0x79] EventEntity looks at Unnamed NPC (ID: 17723568/0x010E70B0) (Basic look)
  3: 0x00CA [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CB   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                   2C F8 FF FF 7F             ,....
00D0: F8 FF FF 7F 73 68 62 6B  53 F8 FF FF 7F F8 FF FF  ....shbkS.......
00E0: 7F 73 68 62 6B 00                                 .shbk.          
```

#### Opcodes

```
  0: 0x00CB [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "shbk" with entities [EventEntity, EventEntity]
  1: 0x00D8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shbk" with entities [EventEntity, EventEntity]
  2: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   1F 00  19 80 1A 80 12 80 1F 01        ..........
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E6 [0x1F] MOVE_ENTITY: EventEntity moves to X=101.945*, Z=94.137*, Y=1.749*
  1: 0x00EE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    66 1B 80 F8 FF FF 7F  F8 FF FF 7F 70 61 73 30   f..........pas0
0100: 53 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 00        S........pas0.  
```

#### Opcodes

```
  0: 0x00F1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
  1: 0x0100 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x010D [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010E   |
| Data Size    | 11 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                            79 00                y.
0110: B1 70 0E 01 AF 70 0E 01  00                       .p...p...       
```

#### Opcodes

```
  0: 0x010E [0x79] Curilla (ID: 17723569/0x010E70B1) looks at Rainemard (ID: 17723567/0x010E70AF) (Basic look)
  1: 0x0118 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0119  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             39 1C 80 1C 16 80 00           9......
```

#### Opcodes

```
  0: 0x0119 [0x39] SET_ENTITY_DIRECTION(direction=19.6°*)
  1: 0x011C [0x1C] WAIT(90* ticks)
  2: 0x011F [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 1F 00 1D 80 1E 80 12 80  1F 01 37 1F 80 20 80 06  ..........7.. ..
0130: 80 21 80 00                                       .!..            
```

#### Opcodes

```
  0: 0x0120 [0x1F] MOVE_ENTITY: EventEntity moves to X=103.879*, Z=95.789*, Y=1.749*
  1: 0x0128 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x012A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=107.691*, z=99.660*, y=0.000*, direction=317.0°*
  3: 0x0133 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0134   |
| Data Size    | 37 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:             1F 00 22 80  23 80 06 80 1F 01 6F 39      ..".#.....o9
0140: 24 80 1C 25 80 79 00 F8  FF FF 7F B1 70 0E 01 1C  $..%.y......p...
0150: 26 80 39 27 80 1C 25 80  00                       &.9'..%..       
```

#### Opcodes

```
  0: 0x0134 [0x1F] MOVE_ENTITY: EventEntity moves to X=108.075*, Z=100.240*, Y=0.000*
  1: 0x013C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x013E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x013F [0x39] SET_ENTITY_DIRECTION(direction=3.6°*)
  4: 0x0142 [0x1C] WAIT(60* ticks)
  5: 0x0145 [0x79] EventEntity looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
  6: 0x014F [0x1C] WAIT(120* ticks)
  7: 0x0152 [0x39] SET_ENTITY_DIRECTION(direction=19.8°*)
  8: 0x0155 [0x1C] WAIT(60* ticks)
  9: 0x0158 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0159   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                             1F 00 28 80 29 80 06           ..(.)..
0160: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0159 [0x1F] MOVE_ENTITY: EventEntity moves to X=117.388*, Z=109.240*, Y=0.000*
  1: 0x0161 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0163 [0x00] END_REQSTACK()
```
