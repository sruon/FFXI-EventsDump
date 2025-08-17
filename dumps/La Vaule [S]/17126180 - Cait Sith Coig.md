# 17126180 - Cait Sith Coig

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | La Vaule [S] (ID: 85) |
| Block Size       | 564 bytes             |
| Total Events     | 17                    |
| References Count | 30                    |

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
| [65535.12](#event-6553512) | 0x0075       |     60 |             13 |
| [65535.13](#event-6553513) | 0x00B1       |     70 |             13 |
| [65535.14](#event-6553514) | 0x00F7       |     60 |             13 |
| [65535.15](#event-6553515) | 0x0133       |     50 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x3FECF     |      261839 |
|       4 | 0xFFFE674A  |  4294862666 |
|       5 | 0x1C866     |      116838 |
|       6 | 0x09A2      |        2466 |
|       7 | 0x408DB     |      264411 |
|       8 | 0xFFFE8806  |  4294871046 |
|       9 | 0x032C      |         812 |
|      10 | 0x40CBA     |      265402 |
|      11 | 0xFFFE8C25  |  4294872101 |
|      12 | 0x1C47F     |      115839 |
|      13 | 0x0AFC      |        2812 |
|      14 | 0x40E96     |      265878 |
|      15 | 0xFFFE8523  |  4294870307 |
|      16 | 0x064B      |        1611 |
|      17 | 0x3DE19     |      253465 |
|      18 | 0xFFFE3BBD  |  4294851517 |
|      19 | 0x20F58     |      135000 |
|      20 | 0x03E8      |        1000 |
|      21 | 0x001E      |          30 |
|      22 | 0x000A      |          10 |
|      23 | 0x0A00      |        2560 |
|      24 | 0x0585      |        1413 |
|      25 | 0x1C887     |      116871 |
|      26 | 0x401B4     |      262580 |
|      27 | 0xFFFE6998  |  4294863256 |
|      28 | 0x0028      |          40 |
|      29 | 0x0168      |         360 |

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
  1: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=261.839*, z=-104.630*, y=116.838*, direction=216.7°*
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
0050:    33 01 37 07 80 08 80  05 80 09 80 00            3.7.........   
```

#### Opcodes

```
  0: 0x0051 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0053 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=264.411*, z=-96.250*, y=116.838*, direction=71.4°*
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
0060: 0A 80 0B 80 0C 80 0D 80  00                       .........       
```

#### Opcodes

```
  0: 0x005D [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x005F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=265.402*, z=-95.195*, y=115.839*, direction=247.1°*
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
0060:                             33 01 37 0E 80 0F 80           3.7....
0070: 05 80 10 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0069 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x006B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=265.878*, z=-96.989*, y=116.838*, direction=141.6°*
  2: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 60 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                06 03 00  03 00 00 11 80 03 01 00       ...........
0080: 12 80 03 02 00 13 80 02  03 00 14 80 03 B0 00 07  ................
0090: 00 00 15 80 07 01 00 16  80 08 02 00 15 80 57 03  ..............W.
00A0: 00 37 00 00 01 00 02 00  17 80 1C 01 80 01 87 00  .7..............
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x0075 [0x06] ExtData[1]->WorkLocal[3] = 0
  1: 0x0078 [0x03] ExtData[1]->WorkLocal[0] = 253465*
  2: 0x007D [0x03] ExtData[1]->WorkLocal[1] = 4294851517*
  3: 0x0082 [0x03] ExtData[1]->WorkLocal[2] = 135000*
  4: 0x0087 [0x02] IF !(ExtData[1]->WorkLocal[3] >= 1000*) GOTO 0x00B0
  5: 0x008F [0x07] ExtData[1]->WorkLocal[0] += 30*
  6: 0x0094 [0x07] ExtData[1]->WorkLocal[1] += 10*
  7: 0x0099 [0x08] ExtData[1]->WorkLocal[2] -= 30*
  8: 0x009E [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[3])
  9: 0x00A1 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=225.0°*
 10: 0x00AA [0x1C] WAIT(1* ticks)
 11: 0x00AD [0x01] GOTO 0x0087
 12: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 70 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    5B 18 80 24 53 05 01  24 53 05 01 6B 61 69 30   [..$S..$S..kai0
00C0: 06 03 00 03 00 00 03 80  03 01 00 04 80 03 02 00  ................
00D0: 19 80 02 03 00 14 80 03  F6 00 07 00 00 15 80 07  ................
00E0: 01 00 15 80 57 03 00 37  00 00 01 00 05 80 17 80  ....W..7........
00F0: 1C 01 80 01 D2 00 00                              .......         
```

#### Opcodes

```
  0: 0x00B1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kai0" with entities [Cait Sith Coig (ID: 17126180/0x01055324), Cait Sith Coig (ID: 17126180/0x01055324)], work=1413*
  1: 0x00C0 [0x06] ExtData[1]->WorkLocal[3] = 0
  2: 0x00C3 [0x03] ExtData[1]->WorkLocal[0] = 261839*
  3: 0x00C8 [0x03] ExtData[1]->WorkLocal[1] = 4294862666*
  4: 0x00CD [0x03] ExtData[1]->WorkLocal[2] = 116871*
  5: 0x00D2 [0x02] IF !(ExtData[1]->WorkLocal[3] >= 1000*) GOTO 0x00F6
  6: 0x00DA [0x07] ExtData[1]->WorkLocal[0] += 30*
  7: 0x00DF [0x07] ExtData[1]->WorkLocal[1] += 30*
  8: 0x00E4 [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[3])
  9: 0x00E7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=116.838*, direction=225.0°*
 10: 0x00F0 [0x1C] WAIT(1* ticks)
 11: 0x00F3 [0x01] GOTO 0x00D2
 12: 0x00F6 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F7   |
| Data Size    | 60 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      06  03 00 03 00 00 1A 80 03         .........
0100: 01 00 1B 80 03 02 00 05  80 02 03 00 14 80 03 32  ...............2
0110: 01 07 00 00 15 80 07 01  00 15 80 08 02 00 01 80  ................
0120: 57 03 00 37 00 00 01 00  02 00 17 80 1C 01 80 01  W..7............
0130: 09 01 00                                          ...             
```

#### Opcodes

```
  0: 0x00F7 [0x06] ExtData[1]->WorkLocal[3] = 0
  1: 0x00FA [0x03] ExtData[1]->WorkLocal[0] = 262580*
  2: 0x00FF [0x03] ExtData[1]->WorkLocal[1] = 4294863256*
  3: 0x0104 [0x03] ExtData[1]->WorkLocal[2] = 116838*
  4: 0x0109 [0x02] IF !(ExtData[1]->WorkLocal[3] >= 1000*) GOTO 0x0132
  5: 0x0111 [0x07] ExtData[1]->WorkLocal[0] += 30*
  6: 0x0116 [0x07] ExtData[1]->WorkLocal[1] += 30*
  7: 0x011B [0x08] ExtData[1]->WorkLocal[2] -= 1*
  8: 0x0120 [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[3])
  9: 0x0123 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=225.0°*
 10: 0x012C [0x1C] WAIT(1* ticks)
 11: 0x012F [0x01] GOTO 0x0109
 12: 0x0132 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0133   |
| Data Size    | 50 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          06 03 00 03 00  00 0A 80 03 01 00 0B 80     .............
0140: 02 03 00 14 80 03 64 01  08 00 00 1C 80 08 01 00  ......d.........
0150: 1C 80 57 03 00 37 00 00  01 00 0C 80 1D 80 1C 01  ..W..7..........
0160: 80 01 40 01 00                                    ..@..           
```

#### Opcodes

```
  0: 0x0133 [0x06] ExtData[1]->WorkLocal[3] = 0
  1: 0x0136 [0x03] ExtData[1]->WorkLocal[0] = 265402*
  2: 0x013B [0x03] ExtData[1]->WorkLocal[1] = 4294872101*
  3: 0x0140 [0x02] IF !(ExtData[1]->WorkLocal[3] >= 1000*) GOTO 0x0164
  4: 0x0148 [0x08] ExtData[1]->WorkLocal[0] -= 40*
  5: 0x014D [0x08] ExtData[1]->WorkLocal[1] -= 40*
  6: 0x0152 [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[3])
  7: 0x0155 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=115.839*, direction=31.6°*
  8: 0x015E [0x1C] WAIT(1* ticks)
  9: 0x0161 [0x01] GOTO 0x0140
 10: 0x0164 [0x00] END_REQSTACK()
```
