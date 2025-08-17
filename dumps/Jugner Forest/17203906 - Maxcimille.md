# 17203906 - Maxcimille

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Jugner Forest (ID: 104) |
| Block Size       | 384 bytes               |
| Total Events     | 19                      |
| References Count | 18                      |

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
| [44](#event-44)            | 0x0044       |      1 |              1 |
| [45](#event-45)            | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     25 |              7 |
| [65535.9](#event-655359)   | 0x005F       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0069       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0073       |     10 |              2 |
| [65535.12](#event-6553512) | 0x007D       |     15 |              5 |
| [65535.13](#event-6553513) | 0x008C       |     15 |              5 |
| [65535.14](#event-6553514) | 0x009B       |     25 |              3 |
| [65535.15](#event-6553515) | 0x00B4       |     25 |              3 |
| [65535.16](#event-6553516) | 0x00CD       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0x7FE3C     |      523836 |
|       5 | 0x85D67     |      548199 |
|       6 | 0x0176      |         374 |
|       7 | 0x003C      |          60 |
|       8 | 0x0011      |          17 |
|       9 | 0x7FC5C     |      523356 |
|      10 | 0x85346     |      545606 |
|      11 | 0x027B      |         635 |
|      12 | 0x7E8F0     |      518384 |
|      13 | 0x82B5C     |      535388 |
|      14 | 0x0343      |         835 |
|      15 | 0x7FEDE     |      523998 |
|      16 | 0x870AF     |      553135 |
|      17 | 0x008C      |         140 |

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

### Event 44

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

### Event 45

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
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 03  80 1F 00 04 80 05 80 06        2.........
0050: 80 1F 01 6F 1E C0 82 06  01 7B C2 82 06 01 00     ...o.....{..... 
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=523.836*, Z=548.199*, Y=0.374*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0054 [0x1E] EventEntity looks at Excenmille (ID: 17203904/0x010682C0) and starts talking
  5: 0x0059 [0x7B] Maxcimille (ID: 17203906/0x010682C2) stops talking
  6: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               6C                 l
0060: C2 82 06 01 00 80 07 80  00                       .........       
```

#### Opcodes

```
  0: 0x005F [0x6C] FADE_ENTITY_COLOR(entity_id=Maxcimille (ID: 17203906/0x010682C2), end_alpha=0*, fade_time=60*)
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             6C C2 82 06 01 00 80           l......
0070: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0069 [0x6C] FADE_ENTITY_COLOR(entity_id=Maxcimille (ID: 17203906/0x010682C2), end_alpha=0*, fade_time=1*)
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          6C C2 82 06 01  02 80 07 80 00              l.........   
```

#### Opcodes

```
  0: 0x0073 [0x6C] FADE_ENTITY_COLOR(entity_id=Maxcimille (ID: 17203906/0x010682C2), end_alpha=128*, fade_time=60*)
  1: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         32 08 80               2..
0080: 1F 00 09 80 0A 80 0B 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x007D [0x32] ExtData[1]->MainSpeed = 17* * 0.1
  1: 0x0080 [0x1F] MOVE_ENTITY: EventEntity moves to X=523.356*, Z=545.606*, Y=0.635*
  2: 0x0088 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      32 03 80 1F              2...
0090: 00 0C 80 0D 80 0E 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x008C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008F [0x1F] MOVE_ENTITY: EventEntity moves to X=518.384*, Z=535.388*, Y=0.835*
  2: 0x0097 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0099 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   B4 13 00 00 3F             ....?
00A0: 3F 3F 00 00 00 00 00 00  00 00 00 00 00 00 00 B5  ??..............
00B0: 00 00 00 00                                       ....            
```

#### Opcodes

```
  0: 0x009B [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="???")
  1: 0x00AF [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             B4 13 00 00  4D 61 78 63 69 6D 69 6C      ....Maxcimil
00C0: 6C 65 00 00 00 00 00 00  B5 00 00 00 00           le...........   
```

#### Opcodes

```
  0: 0x00B4 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Maxcimille")
  1: 0x00C8 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x00CC [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CD   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         32 03 80               2..
00D0: 1F 00 0F 80 10 80 11 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x00CD [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00D0 [0x1F] MOVE_ENTITY: EventEntity moves to X=523.998*, Z=553.135*, Y=0.140*
  2: 0x00D8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00DB [0x00] END_REQSTACK()
```
