# 17281591 - Ildy-Goldy

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Yuhtunga Jungle (ID: 123) |
| Block Size       | 368 bytes                 |
| Total Events     | 14                        |
| References Count | 20                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     18 |              4 |
| [65535.2](#event-655352)   | 0x0013       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0025       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0035       |     14 |              2 |
| [28](#event-28)            | 0x0043       |     15 |              4 |
| [65535.5](#event-655355)   | 0x0052       |     10 |              2 |
| [65535.6](#event-655356)   | 0x005C       |     15 |              5 |
| [65535.7](#event-655357)   | 0x006B       |     31 |              7 |
| [29](#event-29)            | 0x008A       |     15 |              4 |
| [65535.8](#event-655358)   | 0x0099       |     10 |              2 |
| [65535.9](#event-655359)   | 0x00A3       |     22 |              8 |
| [65535.10](#event-6553510) | 0x00B9       |     15 |              5 |
| [65535.11](#event-6553511) | 0x00C8       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0008      |           8 |
|       1 | 0x002C      |          44 |
|       2 | 0x0028      |          40 |
|       3 | 0x62860     |      403552 |
|       4 | 0x3CDBE     |      249278 |
|       5 | 0x53DD      |       21469 |
|       6 | 0x055B      |        1371 |
|       7 | 0x64FBE     |      413630 |
|       8 | 0x3E0CF     |      254159 |
|       9 | 0x54C7      |       21703 |
|      10 | 0x5510E     |      348430 |
|      11 | 0x3379E     |      210846 |
|      12 | 0x1191      |        4497 |
|      13 | 0x0F28      |        3880 |
|      14 | 0x586C7     |      362183 |
|      15 | 0x354F3     |      218355 |
|      16 | 0x0F9F      |        3999 |
|      17 | 0x000D      |          13 |
|      18 | 0x5841A     |      361498 |
|      19 | 0x35336     |      217910 |

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
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    6E F8 FF FF 7F 00 80  99 F8 FF FF 7F 99 F8 FF   n..............
0010: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x6E] EventEntity uses emote 8*
  1: 0x0008 [0x99] Wait for EventEntity animation to complete
  2: 0x000D [0x99] Wait for EventEntity animation to complete
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          6E F8 FF FF 7F  01 80 99 F8 FF FF 7F 99     n............
0020: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0013 [0x6E] EventEntity uses emote 44*
  1: 0x001A [0x99] Wait for EventEntity animation to complete
  2: 0x001F [0x99] Wait for EventEntity animation to complete
  3: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                66 02 80  F8 FF FF 7F F8 FF FF 7F       f..........
0030: 64 69 73 30 00                                    dis0.           
```

#### Opcodes

```
  0: 0x0025 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                53 F8 FF  FF 7F F8 FF FF 7F 64 69       S........di
0040: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0035 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          92 01 F8 FF FF  7F 94 01 F8 FF FF 7F A4     .............
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0043 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0049 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x004F [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  3: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       37 03 80 04 80 05  80 06 80 00                7.........    
```

#### Opcodes

```
  0: 0x0052 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=403.552*, z=249.278*, y=21.469*, direction=120.5°*
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      32 02 80 1F              2...
0060: 00 07 80 08 80 09 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x005C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=413.630*, Z=254.159*, Y=21.703*
  2: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0069 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 31 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   4A 37 B2 07 01             J7...
0070: 38 B2 07 01 6F 76 37 B2  07 01 4A 37 B2 07 01 38  8...ov7...J7...8
0080: B2 07 01 6F 76 37 B2 07  01 00                    ...ov7....      
```

#### Opcodes

```
  0: 0x006B [0x4A] Ildy-Goldy (ID: 17281591/0x0107B237) looks at 1 (ID: 17281592/0x0107B238)
  1: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0075 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Ildy-Goldy (ID: 17281591/0x0107B237) Render.Flags0 and Render.Flags3 conditions are met
  3: 0x007A [0x4A] Ildy-Goldy (ID: 17281591/0x0107B237) looks at 1 (ID: 17281592/0x0107B238)
  4: 0x0083 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0084 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Ildy-Goldy (ID: 17281591/0x0107B237) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0089 [0x00] END_REQSTACK()
```

### Event 29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                92 01 F8 FF FF 7F            ......
0090: 94 01 F8 FF FF 7F A4 01  00                       .........       
```

#### Opcodes

```
  0: 0x008A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0090 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0096 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  3: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             37 0A 80 0B 80 0C 80           7......
00A0: 0D 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0099 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=348.430*, z=210.846*, y=4.497*, direction=341.0°*
  1: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          32 02 80 1F 00  0E 80 0F 80 10 80 1F 01     2............
00B0: 6F 1E F0 FF FF 7F 6F 70  00                       o.....op.       
```

#### Opcodes

```
  0: 0x00A3 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A6 [0x1F] MOVE_ENTITY: EventEntity moves to X=362.183*, Z=218.355*, Y=3.999*
  2: 0x00AE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B1 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x00B6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00B7 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             32 11 80 1F 00 12 80           2......
00C0: 13 80 10 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x00B9 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BC [0x1F] MOVE_ENTITY: EventEntity moves to X=361.498*, Z=217.910*, Y=3.999*
  2: 0x00C4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00C7 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C8   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          32 02 80 1F 00 0A 80 0B          2.......
00D0: 80 0C 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x00C8 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00CB [0x1F] MOVE_ENTITY: EventEntity moves to X=348.430*, Z=210.846*, Y=4.497*
  2: 0x00D3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D5 [0x00] END_REQSTACK()
```
