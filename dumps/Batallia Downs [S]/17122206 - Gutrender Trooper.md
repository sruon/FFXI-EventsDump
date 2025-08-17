# 17122206 - Gutrender Trooper

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
| Block Size       | 332 bytes                   |
| Total Events     | 18                          |
| References Count | 21                          |

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
| [3](#event-3)              | 0x0044       |      4 |              2 |
| [4](#event-4)              | 0x0048       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0049       |     14 |              4 |
| [65535.9](#event-655359)   | 0x0057       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0066       |      5 |              2 |
| [65535.11](#event-6553511) | 0x006B       |      5 |              2 |
| [65535.12](#event-6553512) | 0x0070       |     24 |              6 |
| [65535.13](#event-6553513) | 0x0088       |     14 |              4 |
| [21](#event-21)            | 0x0096       |      1 |              1 |
| [24](#event-24)            | 0x0097       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0x67F7A     |      425850 |
|       5 | 0x83905     |      538885 |
|       6 | 0x0586      |        1414 |
|       7 | 0x0026      |          38 |
|       8 | 0xFFFDB102  |  4294816002 |
|       9 | 0xFFFDD056  |  4294824022 |
|      10 | 0x4DE0      |       19936 |
|      11 | 0x084E      |        2126 |
|      12 | 0x07FA      |        2042 |
|      13 | 0x002A      |          42 |
|      14 | 0xFFFE7027  |  4294864935 |
|      15 | 0xFFFD6A03  |  4294797827 |
|      16 | 0xFFFE97F1  |  4294875121 |
|      17 | 0xFFFD96D6  |  4294809302 |
|      18 | 0x003C      |          60 |
|      19 | 0xFFFEA92A  |  4294879530 |
|      20 | 0xFFFDC80C  |  4294821900 |

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

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             C0 01 80 00                               ....        
```

#### Opcodes

```
  0: 0x0044 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          00                               .       
```

#### Opcodes

```
  0: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             32 03 80 1F 00 04 80           2......
0050: 05 80 06 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0049 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=425.850*, Z=538.885*, Y=1.414*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      32  07 80 1F 00 08 80 09 80         2........
0060: 0A 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0057 [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=-151.294*, Z=-143.274*, Y=19.936*
  2: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0064 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   B6 00  0B 80 00                       .....     
```

#### Opcodes

```
  0: 0x0066 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2126*)
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   B6 00 0C 80 00             .....
```

#### Opcodes

```
  0: 0x006B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2042*)
  1: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0070   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 32 0D 80 1F 00 0E 80 0F  80 00 80 1F 01 1F 00 10  2...............
0080: 80 11 80 00 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x0070 [0x32] ExtData[1]->MainSpeed = 42* * 0.1
  1: 0x0073 [0x1F] MOVE_ENTITY: EventEntity moves to X=-102.361*, Z=-169.469*, Y=0.000*
  2: 0x007B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=-92.175*, Z=-157.994*, Y=0.000*
  4: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          32 12 80 1F 00 13 80 14          2.......
0090: 80 00 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0088 [0x32] ExtData[1]->MainSpeed = 60* * 0.1
  1: 0x008B [0x1F] MOVE_ENTITY: EventEntity moves to X=-87.766*, Z=-145.396*, Y=0.000*
  2: 0x0093 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0095 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0096  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   00                                    .         
```

#### Opcodes

```
  0: 0x0096 [0x00] END_REQSTACK()
```

### Event 24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0097  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0097 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x009D [0x00] END_REQSTACK()
```
