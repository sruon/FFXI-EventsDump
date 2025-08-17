# 16982226 - Travialce

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 492 bytes                      |
| Total Events     | 23                             |
| References Count | 34                             |

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
| [3027](#event-3027)        | 0x0044       |      1 |              1 |
| [3034](#event-3034)        | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0050       |     10 |              2 |
| [65535.10](#event-6553510) | 0x005A       |     28 |              8 |
| [65535.11](#event-6553511) | 0x0076       |     25 |              7 |
| [65535.12](#event-6553512) | 0x008F       |     10 |              2 |
| [3090](#event-3090)        | 0x0099       |      1 |              1 |
| [3092](#event-3092)        | 0x009A       |      1 |              1 |
| [65535.13](#event-6553513) | 0x009B       |     12 |              3 |
| [65535.14](#event-6553514) | 0x00A7       |     34 |              4 |
| [3220](#event-3220)        | 0x00C9       |      1 |              1 |
| [65535.15](#event-6553515) | 0x00CA       |     22 |              6 |
| [65535.16](#event-6553516) | 0x00E0       |     14 |              4 |
| [3136](#event-3136)        | 0x00EE       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x11797     |       71575 |
|       4 | 0xFFFE09E9  |  4294838761 |
|       5 | 0xFFFFE890  |  4294961296 |
|       6 | 0x08F9      |        2297 |
|       7 | 0x12413     |       74771 |
|       8 | 0xFFFE109F  |  4294840479 |
|       9 | 0x05FD      |        1533 |
|      10 | 0x000D      |          13 |
|      11 | 0x12038     |       73784 |
|      12 | 0xFFFE1628  |  4294841896 |
|      13 | 0x01F4      |         500 |
|      14 | 0x1289E     |       75934 |
|      15 | 0xFFFE19D5  |  4294842837 |
|      16 | 0x12DC7     |       77255 |
|      17 | 0xFFFE1EBA  |  4294844090 |
|      18 | 0xFFFFF008  |  4294963208 |
|      19 | 0xFFFEE7A6  |  4294895526 |
|      20 | 0x03ED      |        1005 |
|      21 | 0x105B8     |       67000 |
|      22 | 0xFFFE14CB  |  4294841547 |
|      23 | 0xFFFFE69C  |  4294960796 |
|      24 | 0x0007      |           7 |
|      25 | 0x037E      |         894 |
|      26 | 0x003C      |          60 |
|      27 | 0x0028      |          40 |
|      28 | 0x5017      |       20503 |
|      29 | 0xFFFF03A0  |  4294902688 |
|      30 | 0xFFFFE891  |  4294961297 |
|      31 | 0x001E      |          30 |
|      32 | 0xFFFE4AB5  |  4294855349 |
|      33 | 0x11DC      |        4572 |

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

### Event 3027

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

### Event 3034

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   37 03  80 04 80 05 80 06 80 00        7.........
```

#### Opcodes

```
  0: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=71.575*, z=-128.535*, y=-6.000*, direction=201.9°*
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 37 07 80 08 80 05 80 09  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0050 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=74.771*, z=-126.817*, y=-6.000*, direction=134.7°*
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                32 0A 80 1F 00 0B            2.....
0060: 80 0C 80 05 80 1F 01 6F  4B F8 FF FF 7F 0D 80 6F  .......oK......o
0070: 76 F8 FF FF 7F 00                                 v.....          
```

#### Opcodes

```
  0: 0x005A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=73.784*, Z=-125.400*, Y=-6.000*
  2: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0068 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=2.7°*)
  5: 0x006F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0070 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   32 0A  80 1F 00 0E 80 0F 80 05        2.........
0080: 80 1F 01 1F 00 10 80 11  80 05 80 1F 01 6F 00     .............o. 
```

#### Opcodes

```
  0: 0x0076 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0079 [0x1F] MOVE_ENTITY: EventEntity moves to X=75.934*, Z=-124.459*, Y=-6.000*
  2: 0x0081 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0083 [0x1F] MOVE_ENTITY: EventEntity moves to X=77.255*, Z=-123.206*, Y=-6.000*
  4: 0x008B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x008D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               37                 7
0090: 12 80 13 80 00 80 14 80  00                       .........       
```

#### Opcodes

```
  0: 0x008F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-4.088*, z=-71.770*, y=0.000*, direction=88.3°*
  1: 0x0098 [0x00] END_REQSTACK()
```

### Event 3090

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0099  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             00                             .      
```

#### Opcodes

```
  0: 0x0099 [0x00] END_REQSTACK()
```

### Event 3092

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                00                           .     
```

#### Opcodes

```
  0: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   33 01 37 15 80             3.7..
00A0: 16 80 17 80 18 80 00                              .......         
```

#### Opcodes

```
  0: 0x009B [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x009D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=67.000*, z=-125.749*, y=-6.500*, direction=0.6°*
  2: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      5B  19 80 D2 20 03 01 D2 20         [... ... 
00B0: 03 01 73 7A 74 30 1C 1A  80 5B 19 80 D2 20 03 01  ..szt0...[... ..
00C0: D2 20 03 01 73 7A 65 30  00                       . ..sze0.       
```

#### Opcodes

```
  0: 0x00A7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "szt0" with entities [Travialce (ID: 16982226/0x010320D2), Travialce (ID: 16982226/0x010320D2)], work=894*
  1: 0x00B6 [0x1C] WAIT(60* ticks)
  2: 0x00B9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sze0" with entities [Travialce (ID: 16982226/0x010320D2), Travialce (ID: 16982226/0x010320D2)], work=894*
  3: 0x00C8 [0x00] END_REQSTACK()
```

### Event 3220

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             00                             .      
```

#### Opcodes

```
  0: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                32 1B 80 1F 00 1C            2.....
00D0: 80 1D 80 1E 80 1F 01 1E  F0 FF FF 7F 1C 1F 80 00  ................
```

#### Opcodes

```
  0: 0x00CA [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00CD [0x1F] MOVE_ENTITY: EventEntity moves to X=20.503*, Z=-64.608*, Y=-5.999*
  2: 0x00D5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00DC [0x1C] WAIT(30* ticks)
  5: 0x00DF [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 32 0A 80 1F 00 20 80 21  80 00 80 1F 01 00        2.... .!......  
```

#### Opcodes

```
  0: 0x00E0 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00E3 [0x1F] MOVE_ENTITY: EventEntity moves to X=-111.947*, Z=4.572*, Y=0.000*
  2: 0x00EB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00ED [0x00] END_REQSTACK()
```

### Event 3136

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EE  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                            92 01                ..
00F0: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x00EE [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00F4 [0x00] END_REQSTACK()
```
