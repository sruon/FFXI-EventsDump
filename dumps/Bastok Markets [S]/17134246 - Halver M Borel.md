# 17134246 - Halver M Borel

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 512 bytes                   |
| Total Events     | 18                          |
| References Count | 28                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [175](#event-175)          | 0x0044       |      1 |              1 |
| [176](#event-176)          | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     38 |              6 |
| [65535.9](#event-655359)   | 0x006C       |     19 |              4 |
| [65535.10](#event-6553510) | 0x007F       |     42 |              9 |
| [65535.11](#event-6553511) | 0x00A9       |     54 |             10 |
| [65535.12](#event-6553512) | 0x00DF       |     19 |              4 |
| [65535.13](#event-6553513) | 0x00F2       |     32 |              7 |
| [65535.14](#event-6553514) | 0x0112       |     19 |              4 |
| [65535.15](#event-6553515) | 0x0125       |     19 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFFCD681  |  4294760065 |
|       5 | 0x6F80      |       28544 |
|       6 | 0xFFFFE0C0  |  4294959296 |
|       7 | 0xFFFCE8B8  |  4294764728 |
|       8 | 0x5D86      |       23942 |
|       9 | 0xFFFFDECE  |  4294958798 |
|      10 | 0x151B8     |       86456 |
|      11 | 0xFFFFFF36  |  4294967094 |
|      12 | 0xFFFFB3B4  |  4294947764 |
|      13 | 0x166E0     |       91872 |
|      14 | 0x0033      |          51 |
|      15 | 0x000E      |          14 |
|      16 | 0x18061     |       98401 |
|      17 | 0xFFFFB136  |  4294947126 |
|      18 | 0x18FBD     |      102333 |
|      19 | 0xFFFCF15E  |  4294766942 |
|      20 | 0x3667      |       13927 |
|      21 | 0xFFFFD8F2  |  4294957298 |
|      22 | 0xFFFC9ECF  |  4294745807 |
|      23 | 0x7D4C      |       32076 |
|      24 | 0xFFFC7B4D  |  4294736717 |
|      25 | 0xFFFFE921  |  4294961441 |
|      26 | 0xFFFC44D8  |  4294722776 |
|      27 | 0xFFFFF060  |  4294963296 |

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 175

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 176

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 38 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   59 04  A6 72 05 01 03 80 1F 00        Y..r......
0050: 04 80 05 80 06 80 1F 01  4A A6 72 05 01 A3 72 05  ........J.r...r.
0060: 01 79 00 A6 72 05 01 A3  72 05 01 00              .y..r...r...    
```

#### Opcodes

```
  0: 0x0046 [0x59] UPDATE_ENTITY_DATA: Set Halver M Borel (ID: 17134246/0x010572A6) main speed = 13* * 0.1
  1: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=-207.231*, Z=28.544*, Y=-8.000*
  2: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0058 [0x4A] Halver M Borel (ID: 17134246/0x010572A6) looks at Radford (ID: 17134243/0x010572A3)
  4: 0x0061 [0x79] Halver M Borel (ID: 17134246/0x010572A6) looks at Radford (ID: 17134243/0x010572A3) (Basic look)
  5: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      59 04 A6 72              Y..r
0070: 05 01 03 80 1F 00 07 80  08 80 09 80 1F 01 00     ............... 
```

#### Opcodes

```
  0: 0x006C [0x59] UPDATE_ENTITY_DATA: Set Halver M Borel (ID: 17134246/0x010572A6) main speed = 13* * 0.1
  1: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=-202.568*, Z=23.942*, Y=-8.498*
  2: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 42 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               59                 Y
0080: 04 A6 72 05 01 03 80 1F  00 0A 80 0B 80 0C 80 1F  ..r.............
0090: 01 1F 00 0D 80 0E 80 0C  80 1F 01 4B A6 72 05 01  ...........K.r..
00A0: 00 80 6F 76 A6 72 05 01  00                       ..ov.r...       
```

#### Opcodes

```
  0: 0x007F [0x59] UPDATE_ENTITY_DATA: Set Halver M Borel (ID: 17134246/0x010572A6) main speed = 13* * 0.1
  1: 0x0087 [0x1F] MOVE_ENTITY: EventEntity moves to X=86.456*, Z=-0.202*, Y=-19.532*
  2: 0x008F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0091 [0x1F] MOVE_ENTITY: EventEntity moves to X=91.872*, Z=0.051*, Y=-19.532*
  4: 0x0099 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x009B [0x4B] UPDATE_ENTITY_YAW(entity=Halver M Borel (ID: 17134246/0x010572A6), yaw=0.0°*)
  6: 0x00A2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00A3 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Halver M Borel (ID: 17134246/0x010572A6) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 54 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             59 04 A6 72 05 01 0F           Y..r...
00B0: 80 1F 00 10 80 00 80 11  80 1F 01 1F 00 12 80 00  ................
00C0: 80 11 80 1F 01 4A A6 72  05 01 F1 71 05 01 79 00  .....J.r...q..y.
00D0: A6 72 05 01 F1 71 05 01  6F 76 A6 72 05 01 00     .r...q..ov.r... 
```

#### Opcodes

```
  0: 0x00A9 [0x59] UPDATE_ENTITY_DATA: Set Halver M Borel (ID: 17134246/0x010572A6) main speed = 14* * 0.1
  1: 0x00B1 [0x1F] MOVE_ENTITY: EventEntity moves to X=98.401*, Z=0.000*, Y=-20.170*
  2: 0x00B9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BB [0x1F] MOVE_ENTITY: EventEntity moves to X=102.333*, Z=0.000*, Y=-20.170*
  4: 0x00C3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00C5 [0x4A] Halver M Borel (ID: 17134246/0x010572A6) looks at Prien (ID: 17134065/0x010571F1)
  6: 0x00CE [0x79] Halver M Borel (ID: 17134246/0x010572A6) looks at Prien (ID: 17134065/0x010571F1) (Basic look)
  7: 0x00D8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00D9 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Halver M Borel (ID: 17134246/0x010572A6) Render.Flags0 and Render.Flags3 conditions are met
  9: 0x00DE [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DF   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               59                 Y
00E0: 04 A6 72 05 01 03 80 1F  00 13 80 14 80 15 80 1F  ..r.............
00F0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00DF [0x59] UPDATE_ENTITY_DATA: Set Halver M Borel (ID: 17134246/0x010572A6) main speed = 13* * 0.1
  1: 0x00E7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-200.354*, Z=13.927*, Y=-9.998*
  2: 0x00EF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F1 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F2   |
| Data Size    | 32 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       59 04 A6 72 05 01  03 80 1F 00 16 80 17 80    Y..r..........
0100: 06 80 1F 01 4B A6 72 05  01 00 80 6F 76 A6 72 05  ....K.r....ov.r.
0110: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00F2 [0x59] UPDATE_ENTITY_DATA: Set Halver M Borel (ID: 17134246/0x010572A6) main speed = 13* * 0.1
  1: 0x00FA [0x1F] MOVE_ENTITY: EventEntity moves to X=-221.489*, Z=32.076*, Y=-8.000*
  2: 0x0102 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0104 [0x4B] UPDATE_ENTITY_YAW(entity=Halver M Borel (ID: 17134246/0x010572A6), yaw=0.0°*)
  4: 0x010B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x010C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Halver M Borel (ID: 17134246/0x010572A6) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0111 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0112   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:       59 04 A6 72 05 01  03 80 1F 00 18 80 17 80    Y..r..........
0120: 19 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0112 [0x59] UPDATE_ENTITY_DATA: Set Halver M Borel (ID: 17134246/0x010572A6) main speed = 13* * 0.1
  1: 0x011A [0x1F] MOVE_ENTITY: EventEntity moves to X=-230.579*, Z=32.076*, Y=-5.855*
  2: 0x0122 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0124 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0125   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                59 04 A6  72 05 01 03 80 1F 00 1A       Y..r.......
0130: 80 17 80 1B 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x0125 [0x59] UPDATE_ENTITY_DATA: Set Halver M Borel (ID: 17134246/0x010572A6) main speed = 13* * 0.1
  1: 0x012D [0x1F] MOVE_ENTITY: EventEntity moves to X=-244.520*, Z=32.076*, Y=-4.000*
  2: 0x0135 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0137 [0x00] END_REQSTACK()
```
