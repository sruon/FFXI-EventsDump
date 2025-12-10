# 17203903 - Excenmille

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Jugner Forest (ID: 104) |
| Block Size       | 420 bytes               |
| Total Events     | 19                      |
| References Count | 30                      |

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
| [65535.9](#event-655359)   | 0x0051       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0060       |     15 |              5 |
| [65535.11](#event-6553511) | 0x006F       |     15 |              5 |
| [65535.12](#event-6553512) | 0x007E       |     15 |              5 |
| [65535.13](#event-6553513) | 0x008D       |     15 |              5 |
| [65535.14](#event-6553514) | 0x009C       |     20 |              6 |
| [65535.15](#event-6553515) | 0x00B0       |     15 |              5 |
| [65535.16](#event-6553516) | 0x00BF       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x7FF25     |      524069 |
|       4 | 0x88807     |      559111 |
|       5 | 0x0027      |          39 |
|       6 | 0xFFFDE444  |  4294829124 |
|       7 | 0x4A81      |       19073 |
|       8 | 0xFFFFF830  |  4294965296 |
|       9 | 0x0028      |          40 |
|      10 | 0xFFFEBF2F  |  4294885167 |
|      11 | 0x04CD      |        1229 |
|      12 | 0x07CF      |        1999 |
|      13 | 0x000D      |          13 |
|      14 | 0x8017A     |      524666 |
|      15 | 0x856F8     |      546552 |
|      16 | 0x01AD      |         429 |
|      17 | 0x51629     |      333353 |
|      18 | 0x6D243     |      447043 |
|      19 | 0x0548      |        1352 |
|      20 | 0x53567     |      341351 |
|      21 | 0x6D998     |      448920 |
|      22 | 0x0958      |        2392 |
|      23 | 0xFFFDE412  |  4294829074 |
|      24 | 0x4950      |       18768 |
|      25 | 0x7FBAD     |      523181 |
|      26 | 0x84FA0     |      544672 |
|      27 | 0x02D9      |         729 |
|      28 | 0xFFFDD68C  |  4294825612 |
|      29 | 0x454B      |       17739 |

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
0040:                   1F 00  03 80 04 80 00 80 1F 01        ..........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=524.069*, Z=559.111*, Y=0.000*
  1: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    32 05 80 1F 00 06 80  07 80 08 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0051 [0x32] ExtData[1]->MainSpeed = 39* * 0.1
  1: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=-138.172*, Z=19.073*, Y=-2.000*
  2: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 32 09 80 1F 00 0A 80 0B  80 0C 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0060 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=-82.129*, Z=1.229*, Y=1.999*
  2: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               32                 2
0070: 0D 80 1F 00 0E 80 0F 80  10 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x006F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0072 [0x1F] MOVE_ENTITY: EventEntity moves to X=524.666*, Z=546.552*, Y=0.429*
  2: 0x007A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            32 0D                2.
0080: 80 1F 00 11 80 12 80 13  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x007E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0081 [0x1F] MOVE_ENTITY: EventEntity moves to X=333.353*, Z=447.043*, Y=1.352*
  2: 0x0089 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         32 0D 80               2..
0090: 1F 00 14 80 15 80 16 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x008D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0090 [0x1F] MOVE_ENTITY: EventEntity moves to X=341.351*, Z=448.920*, Y=2.392*
  2: 0x0098 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      32 09 80 1F              2...
00A0: 00 17 80 18 80 08 80 1F  01 6F 1E C4 82 06 01 00  .........o......
```

#### Opcodes

```
  0: 0x009C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x009F [0x1F] MOVE_ENTITY: EventEntity moves to X=-138.222*, Z=18.768*, Y=-2.000*
  2: 0x00A7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AA [0x1E] EventEntity looks at gare (ID: 17203908/0x010682C4) and starts talking
  5: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 32 09 80 1F 00 19 80 1A  80 1B 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x00B0 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B3 [0x1F] MOVE_ENTITY: EventEntity moves to X=523.181*, Z=544.672*, Y=0.729*
  2: 0x00BB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               32                 2
00C0: 09 80 1F 00 1C 80 1D 80  08 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x00BF [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00C2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-141.684*, Z=17.739*, Y=-2.000*
  2: 0x00CA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00CC [0x00] END_REQSTACK()
```
