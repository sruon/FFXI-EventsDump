# 17473751 - Carbuncle

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 508 bytes                    |
| Total Events     | 21                           |
| References Count | 40                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [60](#event-60)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     18 |              4 |
| [65535.2](#event-655352)   | 0x0014       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001E       |      9 |              3 |
| [65535.4](#event-655354)   | 0x0027       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0030       |     10 |              2 |
| [65535.6](#event-655356)   | 0x003A       |     10 |              2 |
| [32000](#event-32000)      | 0x0044       |      7 |              2 |
| [32001](#event-32001)      | 0x004B       |      7 |              2 |
| [65535.7](#event-655357)   | 0x0052       |     10 |              2 |
| [65535.8](#event-655358)   | 0x005C       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0066       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0070       |     10 |              2 |
| [65535.11](#event-6553511) | 0x007A       |     15 |              5 |
| [65535.12](#event-6553512) | 0x0089       |     41 |              6 |
| [65535.13](#event-6553513) | 0x00B2       |     10 |              2 |
| [65535.14](#event-6553514) | 0x00BC       |     17 |              5 |
| [65535.15](#event-6553515) | 0x00CD       |     14 |              4 |
| [65535.16](#event-6553516) | 0x00DB       |     14 |              4 |
| [65535.17](#event-6553517) | 0x00E9       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x532C0     |      340672 |
|       4 | 0xFFFADC03  |  4294630403 |
|       5 | 0xB922      |       47394 |
|       6 | 0x0C02      |        3074 |
|       7 | 0x53473     |      341107 |
|       8 | 0xFFFADB0E  |  4294630158 |
|       9 | 0xB936      |       47414 |
|      10 | 0x0BAB      |        2987 |
|      11 | 0x007F      |         127 |
|      12 | 0x0096      |         150 |
|      13 | 0x52FB9     |      339897 |
|      14 | 0xFFFAD57E  |  4294628734 |
|      15 | 0xB91D      |       47389 |
|      16 | 0x040D      |        1037 |
|      17 | 0x000B      |          11 |
|      18 | 0x52F31     |      339761 |
|      19 | 0xFFFAD023  |  4294627363 |
|      20 | 0xB92B      |       47403 |
|      21 | 0x003C      |          60 |
|      22 | 0x0198      |         408 |
|      23 | 0x52D19     |      339225 |
|      24 | 0xFFFAC7A7  |  4294625191 |
|      25 | 0xB9B6      |       47542 |
|      26 | 0x057A      |        1402 |
|      27 | 0x000A      |          10 |
|      28 | 0x52D7A     |      339322 |
|      29 | 0xFFFAC37D  |  4294624125 |
|      30 | 0xBA0B      |       47627 |
|      31 | 0x002D      |          45 |
|      32 | 0x0009      |           9 |
|      33 | 0x52E45     |      339525 |
|      34 | 0xFFFAC0D2  |  4294623442 |
|      35 | 0xBA47      |       47687 |
|      36 | 0x52DF7     |      339447 |
|      37 | 0xFFFAD821  |  4294629409 |
|      38 | 0xB931      |       47409 |
|      39 | 0x0026      |          38 |

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

### Event 60

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

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             92 01 D7 A0  0A 01 00                     .......     
```

#### Opcodes

```
  0: 0x0044 [0x92] Carbuncle (ID: 17473751/0x010AA0D7)->Render.Flags3 ^= 0x01
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   92 01 D7 A0 0A             .....
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x004B [0x92] Carbuncle (ID: 17473751/0x010AA0D7)->Render.Flags3 ^= 0x01
  1: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.7

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
  0: 0x0052 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=340.672*, z=-336.893*, y=47.394*, direction=270.2°*
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      37 07 80 08              7...
0060: 80 09 80 0A 80 00                                 ......          
```

#### Opcodes

```
  0: 0x005C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=341.107*, z=-337.138*, y=47.414*, direction=262.5°*
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   6C F8  FF FF 7F 0B 80 0C 80 00        l.........
```

#### Opcodes

```
  0: 0x0066 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=127*, fade_time=150*)
  1: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0070   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 37 0D 80 0E 80 0F 80 10  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0070 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=339.897*, z=-338.562*, y=47.389*, direction=91.1°*
  1: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                32 11 80 1F 00 12            2.....
0080: 80 13 80 14 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x007A [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=339.761*, Z=-339.933*, Y=47.403*
  2: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0087 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 41 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             1C 15 80 5B 16 80 F8           ...[...
0090: FF FF 7F F8 FF FF 7F 00  FE FE FE 22 00 80 F8 FF  ..........."....
00A0: FF 7F 5B 16 80 F8 FF FF  7F F8 FF FF 7F 70 6F 70  ..[..........pop
00B0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0089 [0x1C] WAIT(60* ticks)
  1: 0x008C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=408*
  2: 0x009B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x009D [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x00A2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pop0" with entities [EventEntity, EventEntity], work=408*
  5: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       37 17 80 18 80 19  80 1A 80 00                7.........    
```

#### Opcodes

```
  0: 0x00B2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=339.225*, z=-342.105*, y=47.542*, direction=123.2°*
  1: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      32 1B 80 1F              2...
00C0: 00 1C 80 1D 80 1E 80 1F  01 1C 1F 80 00           .............   
```

#### Opcodes

```
  0: 0x00BC [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x00BF [0x1F] MOVE_ENTITY: EventEntity moves to X=339.322*, Z=-343.171*, Y=47.627*
  2: 0x00C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C9 [0x1C] WAIT(45* ticks)
  4: 0x00CC [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CD   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         32 20 80               2 .
00D0: 1F 00 21 80 22 80 23 80  1F 01 00                 ..!.".#....     
```

#### Opcodes

```
  0: 0x00CD [0x32] ExtData[1]->MainSpeed = 9* * 0.1
  1: 0x00D0 [0x1F] MOVE_ENTITY: EventEntity moves to X=339.525*, Z=-343.854*, Y=47.687*
  2: 0x00D8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DA [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DB   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   32 11 80 1F 00             2....
00E0: 24 80 25 80 26 80 1F 01  00                       $.%.&....       
```

#### Opcodes

```
  0: 0x00DB [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x00DE [0x1F] MOVE_ENTITY: EventEntity moves to X=339.447*, Z=-337.887*, Y=47.409*
  2: 0x00E6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E8 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E9   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                             32 27 80 1F 00 12 80           2'.....
00F0: 13 80 14 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x00E9 [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x00EC [0x1F] MOVE_ENTITY: EventEntity moves to X=339.761*, Z=-339.933*, Y=47.403*
  2: 0x00F4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00F7 [0x00] END_REQSTACK()
```
