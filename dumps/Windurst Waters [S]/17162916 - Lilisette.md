# 17162916 - Lilisette

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 528 bytes                    |
| Total Events     | 22                           |
| References Count | 38                           |

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
| [178](#event-178)          | 0x0044       |      1 |              1 |
| [179](#event-179)          | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     21 |              5 |
| [65535.9](#event-655359)   | 0x005B       |     42 |              8 |
| [65535.10](#event-6553510) | 0x0085       |     12 |              4 |
| [41](#event-41)            | 0x0091       |      1 |              1 |
| [42](#event-42)            | 0x0092       |      1 |              1 |
| [43](#event-43)            | 0x0093       |      1 |              1 |
| [65535.11](#event-6553511) | 0x0094       |     34 |              8 |
| [65535.12](#event-6553512) | 0x00B6       |     15 |              5 |
| [65535.13](#event-6553513) | 0x00C5       |     24 |              6 |
| [65535.14](#event-6553514) | 0x00DD       |     31 |              7 |
| [65535.15](#event-6553515) | 0x00FC       |     10 |              2 |
| [65535.16](#event-6553516) | 0x0106       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x754F      |       30031 |
|       4 | 0x028C      |         652 |
|       5 | 0xFFFF9A71  |  4294941297 |
|       6 | 0xFFFFF582  |  4294964610 |
|       7 | 0x048F      |        1167 |
|       8 | 0xFFFF9C64  |  4294941796 |
|       9 | 0x08C7      |        2247 |
|      10 | 0xFFFFF8AD  |  4294965421 |
|      11 | 0x09B9      |        2489 |
|      12 | 0xFFFF9C65  |  4294941797 |
|      13 | 0x0028      |          40 |
|      14 | 0x089D      |        2205 |
|      15 | 0x96D3      |       38611 |
|      16 | 0xFFFFFC18  |  4294966296 |
|      17 | 0xFFFFFE93  |  4294966931 |
|      18 | 0xC114      |       49428 |
|      19 | 0xFFFFEA6D  |  4294961773 |
|      20 | 0x108ED     |       67821 |
|      21 | 0x000D      |          13 |
|      22 | 0xFFFF67AF  |  4294928303 |
|      23 | 0x35CE3     |      220387 |
|      24 | 0xFFFFECB6  |  4294962358 |
|      25 | 0xFFFF67A1  |  4294928289 |
|      26 | 0x3364A     |      210506 |
|      27 | 0xFFFFEC00  |  4294962176 |
|      28 | 0xFFFF5B07  |  4294925063 |
|      29 | 0x30A4F     |      199247 |
|      30 | 0xFFFFEBA1  |  4294962081 |
|      31 | 0xFFFFCB02  |  4294953730 |
|      32 | 0x1488F     |       84111 |
|      33 | 0xFFFFEC79  |  4294962297 |
|      34 | 0xFFFFEE09  |  4294962697 |
|      35 | 0x11F38     |       73528 |
|      36 | 0xFFFFF00C  |  4294963212 |
|      37 | 0xE6D8      |       59096 |

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

### Event 178

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

### Event 179

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
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   1F 00  03 80 04 80 05 80 1F 01        ..........
0050: 6F 4A A4 E2 05 01 A2 E2  05 01 00                 oJ.........     
```

#### Opcodes

```
  0: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=30.031*, Z=0.652*, Y=-25.999*
  1: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0050 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0051 [0x4A] Lilisette (ID: 17162916/0x0105E2A4) looks at Velda-Galda (ID: 17162914/0x0105E2A2)
  4: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 42 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   1F 00 06 80 07             .....
0060: 80 08 80 1F 01 6F 4A A4  E2 05 01 18 E2 05 01 6F  .....oJ........o
0070: 76 A4 E2 05 01 5B 09 80  A4 E2 05 01 A4 E2 05 01  v....[..........
0080: 73 74 64 30 00                                    std0.           
```

#### Opcodes

```
  0: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.686*, Z=1.167*, Y=-25.500*
  1: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0065 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0066 [0x4A] Lilisette (ID: 17162916/0x0105E2A4) looks at Robel-Akbel (ID: 17162776/0x0105E218)
  4: 0x006F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0070 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Lilisette (ID: 17162916/0x0105E2A4) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0075 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "std0" with entities [Lilisette (ID: 17162916/0x0105E2A4), Lilisette (ID: 17162916/0x0105E2A4)], work=2247*
  7: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                1F 00 0A  80 0B 80 0C 80 1F 01 6F       ..........o
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0085 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.875*, Z=2.489*, Y=-25.499*
  1: 0x008D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x008F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0090 [0x00] END_REQSTACK()
```

### Event 41

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0091  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    00                                              .              
```

#### Opcodes

```
  0: 0x0091 [0x00] END_REQSTACK()
```

### Event 42

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0092  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       00                                            .             
```

#### Opcodes

```
  0: 0x0092 [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0093  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          00                                          .            
```

#### Opcodes

```
  0: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             32 0D 80 1F  00 0E 80 0F 80 10 80 1F      2...........
00A0: 01 1F 00 11 80 12 80 10  80 1F 01 1F 00 13 80 14  ................
00B0: 80 10 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0094 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0097 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.205*, Z=38.611*, Y=-1.000*
  2: 0x009F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.365*, Z=49.428*, Y=-1.000*
  4: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00AB [0x1F] MOVE_ENTITY: EventEntity moves to X=-5.523*, Z=67.821*, Y=-1.000*
  6: 0x00B3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00B5 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B6   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   32 15  80 1F 00 16 80 17 80 18        2.........
00C0: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x00B6 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B9 [0x1F] MOVE_ENTITY: EventEntity moves to X=-38.993*, Z=220.387*, Y=-4.938*
  2: 0x00C1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                32 0D 80  1F 00 19 80 1A 80 1B 80       2..........
00D0: 1F 01 1F 00 1C 80 1D 80  1E 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x00C5 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00C8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-39.007*, Z=210.506*, Y=-5.120*
  2: 0x00D0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.233*, Z=199.247*, Y=-5.215*
  4: 0x00DA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 31 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         1F 00 1F               ...
00E0: 80 20 80 21 80 1F 01 1F  00 22 80 23 80 10 80 1F  . .!.....".#....
00F0: 01 1F 00 24 80 25 80 10  80 1F 01 00              ...$.%......    
```

#### Opcodes

```
  0: 0x00DD [0x1F] MOVE_ENTITY: EventEntity moves to X=-13.566*, Z=84.111*, Y=-4.999*
  1: 0x00E5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00E7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-4.599*, Z=73.528*, Y=-1.000*
  3: 0x00EF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00F1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-4.084*, Z=59.096*, Y=-1.000*
  5: 0x00F9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      6C F8 FF FF              l...
0100: 7F 00 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00FC [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0105 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0106   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                   6C F8  FF FF 7F 02 80 01 80 00        l.........
```

#### Opcodes

```
  0: 0x0106 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x010F [0x00] END_REQSTACK()
```
