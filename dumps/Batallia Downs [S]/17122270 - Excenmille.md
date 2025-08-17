# 17122270 - Excenmille

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
| Block Size       | 376 bytes                   |
| Total Events     | 21                          |
| References Count | 23                          |

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
| [114](#event-114)          | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     14 |              4 |
| [65535.9](#event-655359)   | 0x0053       |     10 |              2 |
| [65535.10](#event-6553510) | 0x005D       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0067       |      4 |              2 |
| [65535.12](#event-6553512) | 0x006B       |      4 |              2 |
| [115](#event-115)          | 0x006F       |      1 |              1 |
| [117](#event-117)          | 0x0070       |      1 |              1 |
| [65535.13](#event-6553513) | 0x0071       |     21 |              5 |
| [65535.14](#event-6553514) | 0x0086       |     11 |              3 |
| [65535.15](#event-6553515) | 0x0091       |     12 |              4 |
| [65535.16](#event-6553516) | 0x009D       |     11 |              3 |
| [65535.17](#event-6553517) | 0x00A8       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFFF1988  |  4294908296 |
|       5 | 0x6AAB7     |      436919 |
|       6 | 0x03CC      |         972 |
|       7 | 0xFFFF1D60  |  4294909280 |
|       8 | 0x6B32B     |      439083 |
|       9 | 0x0384      |         900 |
|      10 | 0xFFFF2026  |  4294909990 |
|      11 | 0x6AF00     |      438016 |
|      12 | 0x0360      |         864 |
|      13 | 0xFFFF25F8  |  4294911480 |
|      14 | 0x6ACC9     |      437449 |
|      15 | 0x030A      |         778 |
|      16 | 0xFFFF2E9B  |  4294913691 |
|      17 | 0x6AC9E     |      437406 |
|      18 | 0x022C      |         556 |
|      19 | 0x000D      |          13 |
|      20 | 0xFFFF2DD8  |  4294913496 |
|      21 | 0x6B766     |      440166 |
|      22 | 0x023F      |         575 |

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

### Event 114

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                32 03 80  1F 00 04 80 05 80 06 80       2..........
0050: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0045 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=-59.000*, Z=436.919*, Y=0.972*
  2: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          6C DE 43 05 01  00 80 01 80 00              l.C.......   
```

#### Opcodes

```
  0: 0x0053 [0x6C] FADE_ENTITY_COLOR(entity_id=Excenmille (ID: 17122270/0x010543DE), end_alpha=0*, fade_time=1*)
  1: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         6C DE 43               l.C
0060: 05 01 02 80 01 80 00                              .......         
```

#### Opcodes

```
  0: 0x005D [0x6C] FADE_ENTITY_COLOR(entity_id=Excenmille (ID: 17122270/0x010543DE), end_alpha=128*, fade_time=1*)
  1: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      C0  01 80 00                        ....     
```

#### Opcodes

```
  0: 0x0067 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   C0 00 80 00                .... 
```

#### Opcodes

```
  0: 0x006B [0xC0] EventEntity->Render.Flags3 &= ~0x1000 // Clear bit 12 (from 0*)
  1: 0x006E [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               00                 .
```

#### Opcodes

```
  0: 0x006F [0x00] END_REQSTACK()
```

### Event 117

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0070  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    1F 00 07 80 08 80 09  80 1F 01 6F 4A DE 43 05   ..........oJ.C.
0080: 01 E3 43 05 01 00                                 ..C...          
```

#### Opcodes

```
  0: 0x0071 [0x1F] MOVE_ENTITY: EventEntity moves to X=-58.016*, Z=439.083*, Y=0.900*
  1: 0x0079 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x007B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x007C [0x4A] Excenmille (ID: 17122270/0x010543DE) looks at Alphonimile (ID: 17122275/0x010543E3)
  4: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   1F 00  0A 80 0B 80 0C 80 1F 01        ..........
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0086 [0x1F] MOVE_ENTITY: EventEntity moves to X=-57.306*, Z=438.016*, Y=0.864*
  1: 0x008E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    1F 00 0D 80 0E 80 0F  80 1F 01 6F 00            ..........o.   
```

#### Opcodes

```
  0: 0x0091 [0x1F] MOVE_ENTITY: EventEntity moves to X=-55.816*, Z=437.449*, Y=0.778*
  1: 0x0099 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x009B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         1F 00 10               ...
00A0: 80 11 80 12 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x009D [0x1F] MOVE_ENTITY: EventEntity moves to X=-53.605*, Z=437.406*, Y=0.556*
  1: 0x00A5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00A7 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A8   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                          32 13 80 1F 00 14 80 15          2.......
00B0: 80 16 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x00A8 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00AB [0x1F] MOVE_ENTITY: EventEntity moves to X=-53.800*, Z=440.166*, Y=0.575*
  2: 0x00B3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B5 [0x00] END_REQSTACK()
```
