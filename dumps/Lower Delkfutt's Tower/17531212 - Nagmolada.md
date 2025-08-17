# 17531212 - Nagmolada

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 488 bytes                        |
| Total Events     | 18                               |
| References Count | 35                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [24](#event-24)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     18 |              4 |
| [65535.2](#event-655352)   | 0x0014       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001E       |      9 |              3 |
| [65535.4](#event-655354)   | 0x0027       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0030       |     10 |              2 |
| [65535.6](#event-655356)   | 0x003A       |     10 |              2 |
| [25](#event-25)            | 0x0044       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0045       |     10 |              2 |
| [65535.8](#event-655358)   | 0x004F       |     22 |              6 |
| [65535.9](#event-655359)   | 0x0065       |     10 |              2 |
| [65535.10](#event-6553510) | 0x006F       |     42 |              9 |
| [65535.11](#event-6553511) | 0x0099       |     10 |              2 |
| [65535.12](#event-6553512) | 0x00A3       |     25 |              7 |
| [65535.13](#event-6553513) | 0x00BC       |     10 |              2 |
| [65535.14](#event-6553514) | 0x00C6       |     51 |             10 |
| [65535.15](#event-6553515) | 0x00F9       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x72536     |      468278 |
|       4 | 0x21209     |      135689 |
|       5 | 0x001C      |          28 |
|       6 | 0x0808      |        2056 |
|       7 | 0x000D      |          13 |
|       8 | 0x717A4     |      464804 |
|       9 | 0x20D17     |      134423 |
|      10 | 0x0031      |          49 |
|      11 | 0x002D      |          45 |
|      12 | 0xFFFE90FA  |  4294873338 |
|      13 | 0xFFFF7B95  |  4294933397 |
|      14 | 0x0BCB      |        3019 |
|      15 | 0x0002      |           2 |
|      16 | 0xFFFEB307  |  4294882055 |
|      17 | 0xFFFF7B1C  |  4294933276 |
|      18 | 0x000F      |          15 |
|      19 | 0x01D2      |         466 |
|      20 | 0x001E      |          30 |
|      21 | 0x0400      |        1024 |
|      22 | 0x0609      |        1545 |
|      23 | 0xFFFEB3EA  |  4294882282 |
|      24 | 0x072C      |        1836 |
|      25 | 0xFFFEC56E  |  4294886766 |
|      26 | 0xFFFF7C5C  |  4294933596 |
|      27 | 0x0014      |          20 |
|      28 | 0xFFFED93B  |  4294891835 |
|      29 | 0x0BF8      |        3064 |
|      30 | 0xFFFF0A36  |  4294904374 |
|      31 | 0xFFFF7BF7  |  4294933495 |
|      32 | 0x0010      |          16 |
|      33 | 0xFFFF078E  |  4294903694 |
|      34 | 0x0C02      |        3074 |

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

### Event 24

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

### Event 65535.1

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

### Event 65535.2

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

### Event 65535.3

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

### Event 65535.4

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

### Event 65535.5

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

### Event 65535.6

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

### Event 25

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

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                37 03 80  04 80 05 80 06 80 00          7......... 
```

#### Opcodes

```
  0: 0x0045 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=468.278*, z=135.689*, y=0.028*, direction=180.7°*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               27                 '
0050: 10 49 81 0B 01 02 32 07  80 1F 00 08 80 09 80 0A  .I....2.........
0060: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x004F [0x27] REQ_SET(priority=0x10, entity_id=Unnamed NPC (ID: 17531209/0x010B8149), tag_num=0x02)
  1: 0x0056 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0059 [0x1F] MOVE_ENTITY: EventEntity moves to X=464.804*, Z=134.423*, Y=0.049*
  3: 0x0061 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0063 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                37 0B 80  0C 80 0D 80 0E 80 00          7......... 
```

#### Opcodes

```
  0: 0x0065 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.045*, z=-93.958*, y=-33.899*, direction=265.3°*
  1: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 42 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               32                 2
0070: 07 80 1F 00 0F 80 10 80  11 80 1F 01 6F 1C 12 80  ............o...
0080: 81 00 4C 81 0B 01 5B 13  80 4C 81 0B 01 4C 81 0B  ..L...[..L...L..
0090: 01 63 6F 6E 30 1C 14 80  00                       .con0....       
```

#### Opcodes

```
  0: 0x006F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0072 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.002*, Z=-85.241*, Y=-34.020*
  2: 0x007A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007D [0x1C] WAIT(15* ticks)
  5: 0x0080 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=Nag'molada (ID: 17531212/0x010B814C))
  6: 0x0086 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "con0" with entities [Nag'molada (ID: 17531212/0x010B814C), Nag'molada (ID: 17531212/0x010B814C)], work=466*
  7: 0x0095 [0x1C] WAIT(30* ticks)
  8: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             37 0F 80 10 80 11 80           7......
00A0: 15 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0099 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.002*, z=-85.241*, y=-34.020*, direction=90.0°*
  1: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          32 07 80 1F 00  16 80 17 80 0D 80 1F 01     2............
00B0: 1F 00 18 80 19 80 1A 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x00A3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A6 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.545*, Z=-85.014*, Y=-33.899*
  2: 0x00AE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B0 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.836*, Z=-80.530*, Y=-33.700*
  4: 0x00B8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00BA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      37 18 80 19              7...
00C0: 80 1A 80 15 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00BC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.836*, z=-80.530*, y=-33.700*, direction=90.0°*
  1: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 51 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   37 1B  80 1C 80 1A 80 1D 80 1C        7.........
00D0: 01 80 1F 00 1B 80 1E 80  1F 80 1F 01 6F 1C 12 80  ............o...
00E0: 81 00 4C 81 0B 01 5B 13  80 4C 81 0B 01 4C 81 0B  ..L...[..L...L..
00F0: 01 63 6F 6E 30 1C 14 80  00                       .con0....       
```

#### Opcodes

```
  0: 0x00C6 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.020*, z=-75.461*, y=-33.700*, direction=269.3°*
  1: 0x00CF [0x1C] WAIT(1* ticks)
  2: 0x00D2 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.020*, Z=-62.922*, Y=-33.801*
  3: 0x00DA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00DC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00DD [0x1C] WAIT(15* ticks)
  6: 0x00E0 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=Nag'molada (ID: 17531212/0x010B814C))
  7: 0x00E6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "con0" with entities [Nag'molada (ID: 17531212/0x010B814C), Nag'molada (ID: 17531212/0x010B814C)], work=466*
  8: 0x00F5 [0x1C] WAIT(30* ticks)
  9: 0x00F8 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F9   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                             37 20 80 21 80 1F 80           7 .!...
0100: 22 80 00                                          "..             
```

#### Opcodes

```
  0: 0x00F9 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.016*, z=-63.602*, y=-33.801*, direction=270.2°*
  1: 0x0102 [0x00] END_REQSTACK()
```
