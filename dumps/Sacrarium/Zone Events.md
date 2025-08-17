# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Sacrarium (ID: 28) |
| Block Size       | 608 bytes          |
| Total Events     | 27                 |
| References Count | 41                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |      6 |              2 |
| [65535.2](#event-655352)   | 0x0008       |      6 |              2 |
| [65535.3](#event-655353)   | 0x000E       |      6 |              2 |
| [65535.4](#event-655354)   | 0x0014       |      6 |              2 |
| [65535.5](#event-655355)   | 0x001A       |      6 |              2 |
| [65535.6](#event-655356)   | 0x0020       |     10 |              2 |
| [65535.7](#event-655357)   | 0x002A       |     14 |              4 |
| [65535.8](#event-655358)   | 0x0038       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0042       |     10 |              2 |
| [65535.10](#event-6553510) | 0x004C       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0056       |     13 |              3 |
| [65535.12](#event-6553512) | 0x0063       |     10 |              2 |
| [65535.13](#event-6553513) | 0x006D       |     15 |              5 |
| [65535.14](#event-6553514) | 0x007C       |     18 |              8 |
| [65535.15](#event-6553515) | 0x008E       |     10 |              2 |
| [65535.16](#event-6553516) | 0x0098       |     10 |              2 |
| [65535.17](#event-6553517) | 0x00A2       |     27 |              3 |
| [65535.18](#event-6553518) | 0x00BD       |     27 |              3 |
| [65535.19](#event-6553519) | 0x00D8       |     27 |              3 |
| [103](#event-103)          | 0x00F3       |     13 |              3 |
| [104](#event-104)          | 0x0100       |     10 |              2 |
| [105](#event-105)          | 0x010A       |     14 |              4 |
| [107](#event-107)          | 0x0118       |     13 |              3 |
| [108](#event-108)          | 0x0125       |     10 |              2 |
| [109](#event-109)          | 0x012F       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xA0FC      |       41212 |
|       1 | 0x3507      |       13575 |
|       2 | 0x0000      |           0 |
|       3 | 0x086F      |        2159 |
|       4 | 0x000D      |          13 |
|       5 | 0x8A9E      |       35486 |
|       6 | 0x6E53      |       28243 |
|       7 | 0x3E6C      |       15980 |
|       8 | 0x07BB      |        1979 |
|       9 | 0x5614      |       22036 |
|      10 | 0x358C      |       13708 |
|      11 | 0x07CF      |        1999 |
|      12 | 0x0527      |        1319 |
|      13 | 0x49F8      |       18936 |
|      14 | 0x2FF1      |       12273 |
|      15 | 0x07D0      |        2000 |
|      16 | 0x042B      |        1067 |
|      17 | 0xA865      |       43109 |
|      18 | 0x2754      |       10068 |
|      19 | 0x0800      |        2048 |
|      20 | 0xD6D8      |       55000 |
|      21 | 0x2710      |       10000 |
|      22 | 0x008F      |         143 |
|      23 | 0x07FF      |        2047 |
|      24 | 0xCB20      |       52000 |
|      25 | 0x0053      |          83 |
|      26 | 0x001E      |          30 |
|      27 | 0x4C90      |       19600 |
|      28 | 0xFFFFFE70  |  4294966896 |
|      29 | 0x06DF      |        1759 |
|      30 | 0x47E0      |       18400 |
|      31 | 0x00C8      |         200 |
|      32 | 0x09C4      |        2500 |
|      33 | 0x4E09      |       19977 |
|      34 | 0x542C      |       21548 |
|      35 | 0x0BF0      |        3056 |
|      36 | 0x4E79      |       20089 |
|      37 | 0x4383      |       17283 |
|      38 | 0x0BEF      |        3055 |
|      39 | 0xB986      |       47494 |
|      40 | 0x26EB      |        9963 |

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

### Event 65534

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 02 10 0B 7F 00                             ......        
```

#### Opcodes

```
  0: 0x0002 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          03 02 10 07 7F 00                ......  
```

#### Opcodes

```
  0: 0x0008 [0x03] Work_Zone[2] = Entity->Race
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            03 09                ..
0010: 10 07 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x000E [0x03] Work_Zone[9] = Entity->Race
  1: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             03 02 10 06  7F 00                        ......      
```

#### Opcodes

```
  0: 0x0014 [0x03] Work_Zone[2] = Entity->JobId (if LocalPlayer)
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                03 08 10 07 7F 00            ......
```

#### Opcodes

```
  0: 0x001A [0x03] Work_Zone[8] = Entity->Race
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 37 00 80 01 80 02 80 03  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0020 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=41.212*, z=13.575*, y=0.000*, direction=189.8°*
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 04 80 1F 00 05            2.....
0030: 80 01 80 02 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=35.486*, Z=13.575*, Y=0.000*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          37 06 80 07 80 02 80 08          7.......
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0038 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.243*, z=15.980*, y=0.000*, direction=173.9°*
  1: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       37 09 80 0A 80 0B  80 0C 80 00                7.........    
```

#### Opcodes

```
  0: 0x0042 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.036*, z=13.708*, y=1.999*, direction=115.9°*
  1: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      37 0D 80 0E              7...
0050: 80 0F 80 10 80 00                                 ......          
```

#### Opcodes

```
  0: 0x004C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=18.936*, z=12.273*, y=2.000*, direction=93.8°*
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   47 00  11 80 12 80 02 80 13 80        G.........
0060: 47 01 00                                          G..             
```

#### Opcodes

```
  0: 0x0056 [0x47] UPDATE_PLAYER_POS(43.109*, 10.068*, 0.000*, yaw=180.0°*)
  1: 0x0060 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          37 14 80 15 80  16 80 17 80 00              7.........   
```

#### Opcodes

```
  0: 0x0063 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=55.000*, z=10.000*, y=0.143*, direction=179.9°*
  1: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         32 04 80               2..
0070: 1F 00 18 80 15 80 19 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x006D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=52.000*, Z=10.000*, Y=0.083*
  2: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 18 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      1E F2 C0 01              ....
0080: 01 6F 70 1C 1A 80 1E F2  C0 01 01 6F 70 00        .op........op.  
```

#### Opcodes

```
  0: 0x007C [0x1E] EventEntity looks at Prishe (ID: 16892146/0x0101C0F2) and starts talking
  1: 0x0081 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0082 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0083 [0x1C] WAIT(30* ticks)
  4: 0x0086 [0x1E] EventEntity looks at Prishe (ID: 16892146/0x0101C0F2) and starts talking
  5: 0x008B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x008C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            37 1B                7.
0090: 80 1C 80 0B 80 1D 80 00                           ........        
```

#### Opcodes

```
  0: 0x008E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=19.600*, z=-0.400*, y=1.999*, direction=154.6°*
  1: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          37 1E 80 1F 80 0B 80 20          7...... 
00A0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0098 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=18.400*, z=0.200*, y=1.999*, direction=219.7°*
  1: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       2C F0 FF FF 7F F0  FF FF 7F 72 65 73 30 53    ,........res0S
00B0: F0 FF FF 7F F0 FF FF 7F  72 65 73 30 00           ........res0.   
```

#### Opcodes

```
  0: 0x00A2 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [LocalPlayer, LocalPlayer]
  1: 0x00AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res0" with entities [LocalPlayer, LocalPlayer]
  2: 0x00BC [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BD   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                         2C F0 FF               ,..
00C0: FF 7F F0 FF FF 7F 72 65  73 31 53 F0 FF FF 7F F0  ......res1S.....
00D0: FF FF 7F 72 65 73 31 00                           ...res1.        
```

#### Opcodes

```
  0: 0x00BD [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res1" with entities [LocalPlayer, LocalPlayer]
  1: 0x00CA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res1" with entities [LocalPlayer, LocalPlayer]
  2: 0x00D7 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D8   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                          2C F0 FF FF 7F F0 FF FF          ,.......
00E0: 7F 72 65 73 32 53 F0 FF  FF 7F F0 FF FF 7F 72 65  .res2S........re
00F0: 73 32 00                                          s2.             
```

#### Opcodes

```
  0: 0x00D8 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res2" with entities [LocalPlayer, LocalPlayer]
  1: 0x00E5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res2" with entities [LocalPlayer, LocalPlayer]
  2: 0x00F2 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F3   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          47 00 21 80 22  80 0B 80 23 80 47 01 00     G.!."...#.G..
```

#### Opcodes

```
  0: 0x00F3 [0x47] UPDATE_PLAYER_POS(19.977*, 21.548*, 1.999*, yaw=268.6°*)
  1: 0x00FD [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x00FF [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0100   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 37 24 80 25 80 0B 80 26  80 00                    7$.%...&..      
```

#### Opcodes

```
  0: 0x0100 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=20.089*, z=17.283*, y=1.999*, direction=268.5°*
  1: 0x0109 [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                32 04 80 1F 00 21            2....!
0110: 80 22 80 0B 80 1F 01 00                           ."......        
```

#### Opcodes

```
  0: 0x010A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x010D [0x1F] MOVE_ENTITY: EventEntity moves to X=19.977*, Z=21.548*, Y=1.999*
  2: 0x0115 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0117 [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0118   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                          47 00 11 80 12 80 02 80          G.......
0120: 13 80 47 01 00                                    ..G..           
```

#### Opcodes

```
  0: 0x0118 [0x47] UPDATE_PLAYER_POS(43.109*, 10.068*, 0.000*, yaw=180.0°*)
  1: 0x0122 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x0124 [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0125   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                37 27 80  28 80 02 80 13 80 00          7'.(...... 
```

#### Opcodes

```
  0: 0x0125 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=47.494*, z=9.963*, y=0.000*, direction=180.0°*
  1: 0x012E [0x00] END_REQSTACK()
```

### Event 109

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                               32                 2
0130: 04 80 1F 00 11 80 12 80  02 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x012F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0132 [0x1F] MOVE_ENTITY: EventEntity moves to X=43.109*, Z=10.068*, Y=0.000*
  2: 0x013A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x013C [0x00] END_REQSTACK()
```
