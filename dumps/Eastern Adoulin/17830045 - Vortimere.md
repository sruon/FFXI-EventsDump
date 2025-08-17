# 17830045 - Vortimere

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 600 bytes                 |
| Total Events     | 25                        |
| References Count | 36                        |

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
| [1500](#event-1500)        | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     13 |              3 |
| [65535.9](#event-655359)   | 0x0052       |     42 |             10 |
| [65535.10](#event-6553510) | 0x007C       |     22 |              6 |
| [65535.11](#event-6553511) | 0x0092       |     39 |              7 |
| [65535.12](#event-6553512) | 0x00B9       |     24 |              6 |
| [65535.13](#event-6553513) | 0x00D1       |     22 |              6 |
| [1507](#event-1507)        | 0x00E7       |      1 |              1 |
| [65535.14](#event-6553514) | 0x00E8       |     26 |              8 |
| [1509](#event-1509)        | 0x0102       |      1 |              1 |
| [1510](#event-1510)        | 0x0103       |      1 |              1 |
| [1515](#event-1515)        | 0x0104       |      1 |              1 |
| [65535.15](#event-6553515) | 0x0105       |     34 |              8 |
| [1549](#event-1549)        | 0x0127       |      1 |              1 |
| [65535.16](#event-6553516) | 0x0128       |     14 |              4 |
| [65535.17](#event-6553517) | 0x0136       |     14 |              4 |
| [65535.18](#event-6553518) | 0x0144       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x001E      |          30 |
|       4 | 0x000D      |          13 |
|       5 | 0x0104      |         260 |
|       6 | 0xFFFFE7CA  |  4294961098 |
|       7 | 0xFFFFFA24  |  4294965796 |
|       8 | 0x0B30      |        2864 |
|       9 | 0xFFFFE125  |  4294959397 |
|      10 | 0x12BF      |        4799 |
|      11 | 0xFFFFBF7A  |  4294950778 |
|      12 | 0x0045      |          69 |
|      13 | 0xFFFFC6A4  |  4294952612 |
|      14 | 0x0800      |        2048 |
|      15 | 0x0CB9      |        3257 |
|      16 | 0x0462      |        1122 |
|      17 | 0xFFFFC7EB  |  4294952939 |
|      18 | 0x1189      |        4489 |
|      19 | 0xFFFFD04C  |  4294955084 |
|      20 | 0xFFFF0F7A  |  4294905722 |
|      21 | 0xFFFFD558  |  4294956376 |
|      22 | 0xFFFFFE0D  |  4294966797 |
|      23 | 0xFFFF3A60  |  4294916704 |
|      24 | 0xFFFFC98E  |  4294953358 |
|      25 | 0xFFFF4107  |  4294918407 |
|      26 | 0xFFFFC992  |  4294953362 |
|      27 | 0xFFFF4FBA  |  4294922170 |
|      28 | 0xFFFFC984  |  4294953348 |
|      29 | 0xFFFF7C0B  |  4294933515 |
|      30 | 0xFFFFCC6C  |  4294954092 |
|      31 | 0xFFFFFE0C  |  4294966796 |
|      32 | 0xFFFFFFDE  |  4294967262 |
|      33 | 0xFFFFBC3B  |  4294949947 |
|      34 | 0xFFFFFF8B  |  4294967179 |
|      35 | 0xFFFFC012  |  4294950930 |

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

### Event 1500

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                92 01 F8  FF FF 7F 94 01 F8 FF FF       ...........
0050: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0045 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x004B [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       1C 03 80 32 04 80  1F 00 05 80 06 80 07 80    ...2..........
0060: 1F 01 1F 00 08 80 09 80  07 80 1F 01 6F 4A F8 FF  ............oJ..
0070: FF 7F 93 10 10 01 7B F8  FF FF 7F 00              ......{.....    
```

#### Opcodes

```
  0: 0x0052 [0x1C] WAIT(30* ticks)
  1: 0x0055 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.260*, Z=-6.198*, Y=-1.500*
  3: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0062 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.864*, Z=-7.899*, Y=-1.500*
  5: 0x006A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x006C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x006D [0x4A] EventEntity looks at Hildebert (ID: 17830035/0x01101093)
  8: 0x0076 [0x7B] EventEntity stops talking
  9: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      32 04 80 1F              2...
0080: 00 0A 80 0B 80 07 80 1F  01 6F 4B F8 FF FF 7F 00  .........oK.....
0090: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x007C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007F [0x1F] MOVE_ENTITY: EventEntity moves to X=4.799*, Z=-16.518*, Y=-1.500*
  2: 0x0087 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0089 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008A [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=0.0°*)
  5: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 39 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       32 04 80 1F 00 0C  80 0D 80 07 80 1F 01 4B    2............K
00A0: F8 FF FF 7F 0E 80 1C 03  80 5B 0F 80 9D 10 10 01  .........[......
00B0: 9D 10 10 01 74 6C 6B 30  00                       ....tlk0.       
```

#### Opcodes

```
  0: 0x0092 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0095 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.069*, Z=-14.684*, Y=-1.500*
  2: 0x009D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009F [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=11.2°*)
  4: 0x00A6 [0x1C] WAIT(30* ticks)
  5: 0x00A9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Vortimere (ID: 17830045/0x0110109D), Vortimere (ID: 17830045/0x0110109D)], work=3257*
  6: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             32 04 80 1F 00 10 80           2......
00C0: 11 80 07 80 1F 01 6F 4A  F8 FF FF 7F 9F 10 10 01  ......oJ........
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B9 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BC [0x1F] MOVE_ENTITY: EventEntity moves to X=1.122*, Z=-14.357*, Y=-1.500*
  2: 0x00C4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00C7 [0x4A] EventEntity looks at Unnamed NPC (ID: 17830047/0x0110109F)
  5: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    32 04 80 1F 00 12 80  13 80 07 80 1F 01 6F 4B   2............oK
00E0: F8 FF FF 7F 00 80 00                              .......         
```

#### Opcodes

```
  0: 0x00D1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00D4 [0x1F] MOVE_ENTITY: EventEntity moves to X=4.489*, Z=-12.212*, Y=-1.500*
  2: 0x00DC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00DF [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=0.0°*)
  5: 0x00E6 [0x00] END_REQSTACK()
```

### Event 1507

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                      00                                  .        
```

#### Opcodes

```
  0: 0x00E7 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E8   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                          32 04 80 1F 00 14 80 15          2.......
00F0: 80 16 80 1F 01 6F 1E 90  10 10 01 6F 76 F8 FF FF  .....o.....ov...
0100: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x00E8 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00EB [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.574*, Z=-10.920*, Y=-0.499*
  2: 0x00F3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00F6 [0x1E] EventEntity looks at Arciela (ID: 17830032/0x01101090) and starts talking
  5: 0x00FB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00FC [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0101 [0x00] END_REQSTACK()
```

### Event 1509

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0102  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       00                                            .             
```

#### Opcodes

```
  0: 0x0102 [0x00] END_REQSTACK()
```

### Event 1510

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0103  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          00                                          .            
```

#### Opcodes

```
  0: 0x0103 [0x00] END_REQSTACK()
```

### Event 1515

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0104  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             00                                        .           
```

#### Opcodes

```
  0: 0x0104 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0105   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                32 04 80  1F 00 17 80 18 80 16 80       2..........
0110: 1F 01 1F 00 19 80 1A 80  00 80 1F 01 1F 00 1B 80  ................
0120: 1C 80 00 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0105 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0108 [0x1F] MOVE_ENTITY: EventEntity moves to X=-50.592*, Z=-13.938*, Y=-0.499*
  2: 0x0110 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0112 [0x1F] MOVE_ENTITY: EventEntity moves to X=-48.889*, Z=-13.934*, Y=0.000*
  4: 0x011A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x011C [0x1F] MOVE_ENTITY: EventEntity moves to X=-45.126*, Z=-13.948*, Y=0.000*
  6: 0x0124 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0126 [0x00] END_REQSTACK()
```

### Event 1549

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0127  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                      00                                  .        
```

#### Opcodes

```
  0: 0x0127 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0128   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          32 04 80 1F 00 1D 80 1E          2.......
0130: 80 1F 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0128 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x012B [0x1F] MOVE_ENTITY: EventEntity moves to X=-33.781*, Z=-13.204*, Y=-0.500*
  2: 0x0133 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0135 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0136   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                   32 04  80 1F 00 20 80 21 80 07        2.... .!..
0140: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0136 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0139 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.034*, Z=-17.349*, Y=-1.500*
  2: 0x0141 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0143 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0144   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:             32 04 80 1F  00 22 80 23 80 07 80 1F      2....".#....
0150: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0144 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0147 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.117*, Z=-16.366*, Y=-1.500*
  2: 0x014F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0151 [0x00] END_REQSTACK()
```
