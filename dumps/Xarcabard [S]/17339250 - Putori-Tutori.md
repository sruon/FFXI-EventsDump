# 17339250 - Putori-Tutori

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 488 bytes               |
| Total Events     | 16                      |
| References Count | 32                      |

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
| [65535.8](#event-655358)   | 0x0044       |     30 |              7 |
| [65535.9](#event-655359)   | 0x0062       |     29 |              6 |
| [65535.10](#event-6553510) | 0x007F       |     32 |              7 |
| [65535.11](#event-6553511) | 0x009F       |     78 |             15 |
| [65535.12](#event-6553512) | 0x00ED       |     20 |              5 |
| [65535.13](#event-6553513) | 0x0101       |     20 |              5 |
| [21](#event-21)            | 0x0115       |      1 |              1 |
| [22](#event-22)            | 0x0116       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0xE031      |       57393 |
|       5 | 0xFFFCBCAC  |  4294753452 |
|       6 | 0xFFFFA372  |  4294943602 |
|       7 | 0xE176      |       57718 |
|       8 | 0xFFFCBB6B  |  4294753131 |
|       9 | 0xFFFFA362  |  4294943586 |
|      10 | 0xE078      |       57464 |
|      11 | 0xFFFCB9DA  |  4294752730 |
|      12 | 0xFFFFA349  |  4294943561 |
|      13 | 0x000F      |          15 |
|      14 | 0xE1A5      |       57765 |
|      15 | 0xFFFCBC39  |  4294753337 |
|      16 | 0xFFFFA36D  |  4294943597 |
|      17 | 0x0028      |          40 |
|      18 | 0x0007      |           7 |
|      19 | 0x0082      |         130 |
|      20 | 0xCF31      |       53041 |
|      21 | 0xFFFCAE0F  |  4294749711 |
|      22 | 0xFFFFA3EA  |  4294943722 |
|      23 | 0xD7C2      |       55234 |
|      24 | 0xFFFCA268  |  4294746728 |
|      25 | 0xE2DC      |       58076 |
|      26 | 0xFFFCA951  |  4294748497 |
|      27 | 0xFFFFA2CB  |  4294943435 |
|      28 | 0x0026      |          38 |
|      29 | 0x128D3     |       75987 |
|      30 | 0xFFFC36F0  |  4294719216 |
|      31 | 0xFFFFA153  |  4294943059 |

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 30 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             59 04 F8 FF  FF 7F 03 80 1F 00 04 80      Y...........
0050: 05 80 06 80 1F 01 1F 00  07 80 08 80 09 80 1F 01  ................
0060: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0044 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=57.393*, Z=-213.844*, Y=-23.694*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x1F] MOVE_ENTITY: EventEntity moves to X=57.718*, Z=-214.165*, Y=-23.710*
  4: 0x005E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0060 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       59 04 F8 FF FF 7F  03 80 1F 00 0A 80 0B 80    Y.............
0070: 0C 80 1F 01 6F 4A F8 FF  FF 7F 56 93 08 01 00     ....oJ....V.... 
```

#### Opcodes

```
  0: 0x0062 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=57.464*, Z=-214.566*, Y=-23.735*
  2: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0075 [0x4A] EventEntity looks at Lilisette (ID: 17339222/0x01089356)
  5: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 32 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               59                 Y
0080: 04 F8 FF FF 7F 03 80 1C  0D 80 1F 00 0E 80 0F 80  ................
0090: 10 80 1F 01 6F 4A F8 FF  FF 7F 56 93 08 01 00     ....oJ....V.... 
```

#### Opcodes

```
  0: 0x007F [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x0087 [0x1C] WAIT(15* ticks)
  2: 0x008A [0x1F] MOVE_ENTITY: EventEntity moves to X=57.765*, Z=-213.959*, Y=-23.699*
  3: 0x0092 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0094 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0095 [0x4A] EventEntity looks at Lilisette (ID: 17339222/0x01089356)
  6: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 78 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               66                 f
00A0: 11 80 73 93 08 01 73 93  08 01 77 61 76 30 7B 72  ..s...s...wav0{r
00B0: 93 08 01 6E 72 93 08 01  12 80 99 72 93 08 01 1C  ...nr......r....
00C0: 13 80 59 04 72 93 08 01  03 80 1F 00 14 80 15 80  ..Y.r...........
00D0: 16 80 1F 01 6F 7B 73 93  08 01 27 10 73 93 08 01  ....o{s...'.s...
00E0: 0C 1F 00 17 80 18 80 0C  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x009F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wav0" with entities [Atori-Tutori (ID: 17339251/0x01089373), Atori-Tutori (ID: 17339251/0x01089373)], work=40*
  1: 0x00AE [0x7B] Putori-Tutori (ID: 17339250/0x01089372) stops talking
  2: 0x00B3 [0x6E] Putori-Tutori (ID: 17339250/0x01089372) uses emote 7*
  3: 0x00BA [0x99] Wait for Putori-Tutori (ID: 17339250/0x01089372) animation to complete
  4: 0x00BF [0x1C] WAIT(130* ticks)
  5: 0x00C2 [0x59] UPDATE_ENTITY_DATA: Set Putori-Tutori (ID: 17339250/0x01089372) main speed = 13* * 0.1
  6: 0x00CA [0x1F] MOVE_ENTITY: EventEntity moves to X=53.041*, Z=-217.585*, Y=-23.574*
  7: 0x00D2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x00D4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x00D5 [0x7B] Atori-Tutori (ID: 17339251/0x01089373) stops talking
 10: 0x00DA [0x27] REQ_SET(priority=0x10, entity_id=Atori-Tutori (ID: 17339251/0x01089373), tag_num=0x0C)
 11: 0x00E1 [0x1F] MOVE_ENTITY: EventEntity moves to X=55.234*, Z=-220.568*, Y=-23.735*
 12: 0x00E9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x00EB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 14: 0x00EC [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00ED   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                         59 04 73               Y.s
00F0: 93 08 01 03 80 1F 00 19  80 1A 80 1B 80 1F 01 6F  ...............o
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00ED [0x59] UPDATE_ENTITY_DATA: Set Atori-Tutori (ID: 17339251/0x01089373) main speed = 13* * 0.1
  1: 0x00F5 [0x1F] MOVE_ENTITY: EventEntity moves to X=58.076*, Z=-218.799*, Y=-23.861*
  2: 0x00FD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00FF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    59 04 F8 FF FF 7F 1C  80 1F 00 1D 80 1E 80 1F   Y..............
0110: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0101 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 38* * 0.1
  1: 0x0109 [0x1F] MOVE_ENTITY: EventEntity moves to X=75.987*, Z=-248.080*, Y=-24.237*
  2: 0x0111 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0113 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0114 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0115  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                00                                      .          
```

#### Opcodes

```
  0: 0x0115 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0116  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   00                                    .         
```

#### Opcodes

```
  0: 0x0116 [0x00] END_REQSTACK()
```
