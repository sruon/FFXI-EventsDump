# 17126179 - Cait Sith Ceithir

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | La Vaule [S] (ID: 85) |
| Block Size       | 384 bytes             |
| Total Events     | 15                    |
| References Count | 25                    |

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
| [6](#event-6)              | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     12 |              3 |
| [65535.9](#event-655359)   | 0x0051       |     12 |              3 |
| [65535.10](#event-6553510) | 0x005D       |     12 |              3 |
| [65535.11](#event-6553511) | 0x0069       |     12 |              3 |
| [65535.12](#event-6553512) | 0x0075       |     40 |              9 |
| [65535.13](#event-6553513) | 0x009D       |     50 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x3FBFB     |      261115 |
|       4 | 0xFFFE75D8  |  4294866392 |
|       5 | 0x1C867     |      116839 |
|       6 | 0x0457      |        1111 |
|       7 | 0x405AE     |      263598 |
|       8 | 0xFFFE7CE7  |  4294868199 |
|       9 | 0x1CF2C     |      118572 |
|      10 | 0x0AFB      |        2811 |
|      11 | 0x40FDC     |      266204 |
|      12 | 0xFFFE8375  |  4294869877 |
|      13 | 0x1CC4F     |      117839 |
|      14 | 0x0458      |        1112 |
|      15 | 0x4095A     |      264538 |
|      16 | 0xFFFE7BB1  |  4294867889 |
|      17 | 0x1CC6F     |      117871 |
|      18 | 0x032B      |         811 |
|      19 | 0x1D037     |      118839 |
|      20 | 0x03E8      |        1000 |
|      21 | 0x0028      |          40 |
|      22 | 0x0550      |        1360 |
|      23 | 0x001E      |          30 |
|      24 | 0x0488      |        1160 |

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

### Event 6

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
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                33 01 37  03 80 04 80 05 80 06 80       3.7........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0045 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=261.115*, z=-100.904*, y=116.839*, direction=97.6°*
  2: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    33 01 37 07 80 08 80  09 80 0A 80 00            3.7.........   
```

#### Opcodes

```
  0: 0x0051 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0053 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=263.598*, z=-99.097*, y=118.572*, direction=247.1°*
  2: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         33 01 37               3.7
0060: 0B 80 0C 80 0D 80 0E 80  00                       .........       
```

#### Opcodes

```
  0: 0x005D [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x005F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=266.204*, z=-97.419*, y=117.839*, direction=97.7°*
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             33 01 37 0F 80 10 80           3.7....
0070: 11 80 12 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0069 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x006B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=264.538*, z=-99.407*, y=117.871*, direction=71.3°*
  2: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 40 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                06 03 00  03 02 00 13 80 02 03 00       ...........
0080: 14 80 03 9C 00 08 02 00  15 80 57 03 00 37 07 80  ..........W..7..
0090: 08 80 02 00 16 80 1C 01  80 01 7D 00 00           ..........}..   
```

#### Opcodes

```
  0: 0x0075 [0x06] ExtData[1]->WorkLocal[3] = 0
  1: 0x0078 [0x03] ExtData[1]->WorkLocal[2] = 118839*
  2: 0x007D [0x02] IF !(ExtData[1]->WorkLocal[3] >= 1000*) GOTO 0x009C
  3: 0x0085 [0x08] ExtData[1]->WorkLocal[2] -= 40*
  4: 0x008A [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[3])
  5: 0x008D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=263.598*, z=-99.097*, y=ExtData[1]->WorkLocal[2], direction=119.5°*
  6: 0x0096 [0x1C] WAIT(1* ticks)
  7: 0x0099 [0x01] GOTO 0x007D
  8: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 50 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         06 03 00               ...
00A0: 03 00 00 0B 80 03 01 00  0C 80 02 03 00 14 80 03  ................
00B0: CE 00 08 00 00 17 80 08  01 00 17 80 57 03 00 37  ............W..7
00C0: 00 00 01 00 0D 80 18 80  1C 01 80 01 AA 00 00     ............... 
```

#### Opcodes

```
  0: 0x009D [0x06] ExtData[1]->WorkLocal[3] = 0
  1: 0x00A0 [0x03] ExtData[1]->WorkLocal[0] = 266204*
  2: 0x00A5 [0x03] ExtData[1]->WorkLocal[1] = 4294869877*
  3: 0x00AA [0x02] IF !(ExtData[1]->WorkLocal[3] >= 1000*) GOTO 0x00CE
  4: 0x00B2 [0x08] ExtData[1]->WorkLocal[0] -= 30*
  5: 0x00B7 [0x08] ExtData[1]->WorkLocal[1] -= 30*
  6: 0x00BC [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[3])
  7: 0x00BF [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=117.839*, direction=102.0°*
  8: 0x00C8 [0x1C] WAIT(1* ticks)
  9: 0x00CB [0x01] GOTO 0x00AA
 10: 0x00CE [0x00] END_REQSTACK()
```
