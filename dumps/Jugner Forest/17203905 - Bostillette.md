# 17203905 - Bostillette

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Jugner Forest (ID: 104) |
| Block Size       | 440 bytes               |
| Total Events     | 18                      |
| References Count | 29                      |

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
| [65535.8](#event-655358)   | 0x0046       |     29 |              7 |
| [65535.9](#event-655359)   | 0x0063       |     29 |              7 |
| [65535.10](#event-6553510) | 0x0080       |     15 |              5 |
| [65535.11](#event-6553511) | 0x008F       |     15 |              5 |
| [65535.12](#event-6553512) | 0x009E       |     15 |              5 |
| [65535.13](#event-6553513) | 0x00AD       |     14 |              4 |
| [65535.14](#event-6553514) | 0x00BB       |     14 |              4 |
| [65535.15](#event-6553515) | 0x00C9       |     34 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0028      |          40 |
|       4 | 0x7FB6B     |      523115 |
|       5 | 0x85452     |      545874 |
|       6 | 0x0260      |         608 |
|       7 | 0x000D      |          13 |
|       8 | 0x8073C     |      526140 |
|       9 | 0x85AC7     |      547527 |
|      10 | 0x006D      |         109 |
|      11 | 0x7F0F4     |      520436 |
|      12 | 0x82D7A     |      535930 |
|      13 | 0x0316      |         790 |
|      14 | 0x50B46     |      330566 |
|      15 | 0x6D507     |      447751 |
|      16 | 0x03ED      |        1005 |
|      17 | 0x53567     |      341351 |
|      18 | 0x6D998     |      448920 |
|      19 | 0x0958      |        2392 |
|      20 | 0xFFFC8C12  |  4294741010 |
|      21 | 0xFFFD943C  |  4294808636 |
|      22 | 0x0386      |         902 |
|      23 | 0xFFFBCAF3  |  4294691571 |
|      24 | 0xFFFD8582  |  4294804866 |
|      25 | 0xFFFFE0DC  |  4294959324 |
|      26 | 0x0B50      |        2896 |
|      27 | 0x012C      |         300 |
|      28 | 0x0027      |          39 |

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
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 03  80 1F 00 04 80 05 80 06        2.........
0050: 80 1F 01 6F 4A C1 82 06  01 C2 82 06 01 7B C1 82  ...oJ........{..
0060: 06 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=523.115*, Z=545.874*, Y=0.608*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0054 [0x4A] Bostillette (ID: 17203905/0x010682C1) looks at Maxcimille (ID: 17203906/0x010682C2)
  5: 0x005D [0x7B] Bostillette (ID: 17203905/0x010682C1) stops talking
  6: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          32 07 80 1F 00  08 80 09 80 0A 80 1F 01     2............
0070: 6F 4A C1 82 06 01 C0 82  06 01 7B C1 82 06 01 00  oJ........{.....
```

#### Opcodes

```
  0: 0x0063 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=526.140*, Z=547.527*, Y=0.109*
  2: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0070 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0071 [0x4A] Bostillette (ID: 17203905/0x010682C1) looks at Excenmille (ID: 17203904/0x010682C0)
  5: 0x007A [0x7B] Bostillette (ID: 17203905/0x010682C1) stops talking
  6: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 32 07 80 1F 00 0B 80 0C  80 0D 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0080 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0083 [0x1F] MOVE_ENTITY: EventEntity moves to X=520.436*, Z=535.930*, Y=0.790*
  2: 0x008B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               32                 2
0090: 07 80 1F 00 0E 80 0F 80  10 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x008F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0092 [0x1F] MOVE_ENTITY: EventEntity moves to X=330.566*, Z=447.751*, Y=1.005*
  2: 0x009A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            32 03                2.
00A0: 80 1F 00 11 80 12 80 13  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x009E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=341.351*, Z=448.920*, Y=2.392*
  2: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         32 03 80               2..
00B0: 1F 00 14 80 15 80 16 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x00AD [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B0 [0x1F] MOVE_ENTITY: EventEntity moves to X=-226.286*, Z=-158.660*, Y=0.902*
  2: 0x00B8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   32 03 80 1F 00             2....
00C0: 17 80 18 80 19 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x00BB [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00BE [0x1F] MOVE_ENTITY: EventEntity moves to X=-275.725*, Z=-162.430*, Y=-7.972*
  2: 0x00C6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             5B 1A 80 C1 82 06 01           [......
00D0: C1 82 06 01 6B 79 6F 30  1C 1B 80 66 1C 80 C1 82  ....kyo0...f....
00E0: 06 01 C1 82 06 01 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x00C9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kyo0" with entities [Bostillette (ID: 17203905/0x010682C1), Bostillette (ID: 17203905/0x010682C1)], work=2896*
  1: 0x00D8 [0x1C] WAIT(300* ticks)
  2: 0x00DB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Bostillette (ID: 17203905/0x010682C1), Bostillette (ID: 17203905/0x010682C1)], work=39*
  3: 0x00EA [0x00] END_REQSTACK()
```
