# 17203908 - Alphonimile

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Jugner Forest (ID: 104) |
| Block Size       | 444 bytes               |
| Total Events     | 22                      |
| References Count | 17                      |

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
| [65535.8](#event-655358)   | 0x0046       |     11 |              3 |
| [65535.9](#event-655359)   | 0x0051       |     21 |              2 |
| [65535.10](#event-6553510) | 0x0066       |     21 |              2 |
| [65535.11](#event-6553511) | 0x007B       |     21 |              2 |
| [65535.12](#event-6553512) | 0x0090       |     21 |              2 |
| [65535.13](#event-6553513) | 0x00A5       |     10 |              2 |
| [65535.14](#event-6553514) | 0x00AF       |     10 |              2 |
| [65535.15](#event-6553515) | 0x00B9       |     10 |              2 |
| [65535.16](#event-6553516) | 0x00C3       |     10 |              2 |
| [65535.17](#event-6553517) | 0x00CD       |     15 |              5 |
| [65535.18](#event-6553518) | 0x00DC       |     25 |              3 |
| [65535.19](#event-6553519) | 0x00F5       |     25 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFB63CD  |  4294665165 |
|       4 | 0x16EC2     |       93890 |
|       5 | 0xFFFFDC11  |  4294958097 |
|       6 | 0x0003      |           3 |
|       7 | 0x0002      |           2 |
|       8 | 0x003C      |          60 |
|       9 | 0x00D9      |         217 |
|      10 | 0x0045      |          69 |
|      11 | 0x00D1      |         209 |
|      12 | 0x0040      |          64 |
|      13 | 0x000D      |          13 |
|      14 | 0x7FC5C     |      523356 |
|      15 | 0x85346     |      545606 |
|      16 | 0x027B      |         635 |

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
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   1F 00  03 80 04 80 05 80 1F 01        ..........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.131*, Z=93.890*, Y=-9.199*
  1: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    B6 0B 06 80 07 80 00  80 08 80 09 80 09 80 09   ...............
0060: 80 0A 80 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0051 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=60*, hands=217*, legs=217*, feet=217*, main=69*, sub=0*)
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   B6 0B  06 80 07 80 00 80 08 80        ..........
0070: 09 80 09 80 09 80 00 80  00 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0066 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=60*, hands=217*, legs=217*, feet=217*, main=0*, sub=0*)
  1: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   B6 0B 06 80 07             .....
0080: 80 08 80 08 80 09 80 09  80 09 80 0B 80 00 80 00  ................
```

#### Opcodes

```
  0: 0x007B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=60*, body=60*, hands=217*, legs=217*, feet=217*, main=209*, sub=0*)
  1: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: B6 0B 06 80 07 80 00 80  06 80 06 80 06 80 06 80  ................
00A0: 00 80 00 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0090 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=3*, hands=3*, legs=3*, feet=3*, main=0*, sub=0*)
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                6C C4 82  06 01 00 80 01 80 00          l......... 
```

#### Opcodes

```
  0: 0x00A5 [0x6C] FADE_ENTITY_COLOR(entity_id=Alphonimile (ID: 17203908/0x010682C4), end_alpha=0*, fade_time=1*)
  1: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               6C                 l
00B0: C4 82 06 01 00 80 08 80  00                       .........       
```

#### Opcodes

```
  0: 0x00AF [0x6C] FADE_ENTITY_COLOR(entity_id=Alphonimile (ID: 17203908/0x010682C4), end_alpha=0*, fade_time=60*)
  1: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             6C C4 82 06 01 02 80           l......
00C0: 08 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00B9 [0x6C] FADE_ENTITY_COLOR(entity_id=Alphonimile (ID: 17203908/0x010682C4), end_alpha=128*, fade_time=60*)
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          6C C4 82 06 01  0C 80 08 80 00              l.........   
```

#### Opcodes

```
  0: 0x00C3 [0x6C] FADE_ENTITY_COLOR(entity_id=Alphonimile (ID: 17203908/0x010682C4), end_alpha=64*, fade_time=60*)
  1: 0x00CC [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CD   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         32 0D 80               2..
00D0: 1F 00 0E 80 0F 80 10 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x00CD [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00D0 [0x1F] MOVE_ENTITY: EventEntity moves to X=523.356*, Z=545.606*, Y=0.635*
  2: 0x00D8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00DB [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DC   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      B4 13 00 00              ....
00E0: 41 6C 70 68 6F 6E 69 6D  69 6C 65 00 00 00 00 00  Alphonimile.....
00F0: B5 00 00 00 00                                    .....           
```

#### Opcodes

```
  0: 0x00DC [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Alphonimile")
  1: 0x00F0 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                B4 13 00  00 4D 61 78 63 69 6D 69       ....Maxcimi
0100: 6C 6C 65 00 00 00 00 00  00 B5 00 00 00 00        lle...........  
```

#### Opcodes

```
  0: 0x00F5 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Maxcimille")
  1: 0x0109 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x010D [0x00] END_REQSTACK()
```
