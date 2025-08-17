# 17126176 - Cait Sith Aon

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | La Vaule [S] (ID: 85) |
| Block Size       | 336 bytes             |
| Total Events     | 14                    |
| References Count | 19                    |

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
| [65535.11](#event-6553511) | 0x0069       |     40 |              9 |
| [65535.12](#event-6553512) | 0x0091       |     40 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x40EB7     |      265911 |
|       4 | 0xFFFE8266  |  4294869606 |
|       5 | 0x1C47F     |      115839 |
|       6 | 0x0535      |        1333 |
|       7 | 0x412B3     |      266931 |
|       8 | 0xFFFE7309  |  4294865673 |
|       9 | 0x0AFC      |        2812 |
|      10 | 0x41421     |      267297 |
|      11 | 0xFFFE7C35  |  4294868021 |
|      12 | 0x1C887     |      116871 |
|      13 | 0x0753      |        1875 |
|      14 | 0x03E8      |        1000 |
|      15 | 0x000E      |          14 |
|      16 | 0x0550      |        1360 |
|      17 | 0x000A      |          10 |
|      18 | 0x0A00      |        2560 |

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
  1: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=265.911*, z=-97.690*, y=115.839*, direction=117.2°*
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
  1: 0x0053 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=266.931*, z=-101.623*, y=115.839*, direction=247.1°*
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
  1: 0x005F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=267.297*, z=-99.275*, y=116.871*, direction=164.8°*
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 40 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             06 01 00 03 00 00 05           .......
0070: 80 02 01 00 0E 80 03 90  00 07 00 00 0F 80 57 01  ..............W.
0080: 00 37 03 80 04 80 00 00  10 80 1C 01 80 01 71 00  .7............q.
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0069 [0x06] ExtData[1]->WorkLocal[1] = 0
  1: 0x006C [0x03] ExtData[1]->WorkLocal[0] = 115839*
  2: 0x0071 [0x02] IF !(ExtData[1]->WorkLocal[1] >= 1000*) GOTO 0x0090
  3: 0x0079 [0x07] ExtData[1]->WorkLocal[0] += 14*
  4: 0x007E [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[1])
  5: 0x0081 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=265.911*, z=-97.690*, y=ExtData[1]->WorkLocal[0], direction=119.5°*
  6: 0x008A [0x1C] WAIT(1* ticks)
  7: 0x008D [0x01] GOTO 0x0071
  8: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 40 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    06 01 00 03 00 00 05  80 02 01 00 0E 80 03 B8   ...............
00A0: 00 07 00 00 11 80 57 01  00 37 07 80 08 80 00 00  ......W..7......
00B0: 12 80 1C 01 80 01 99 00  00                       .........       
```

#### Opcodes

```
  0: 0x0091 [0x06] ExtData[1]->WorkLocal[1] = 0
  1: 0x0094 [0x03] ExtData[1]->WorkLocal[0] = 115839*
  2: 0x0099 [0x02] IF !(ExtData[1]->WorkLocal[1] >= 1000*) GOTO 0x00B8
  3: 0x00A1 [0x07] ExtData[1]->WorkLocal[0] += 10*
  4: 0x00A6 [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[1])
  5: 0x00A9 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=266.931*, z=-101.623*, y=ExtData[1]->WorkLocal[0], direction=225.0°*
  6: 0x00B2 [0x1C] WAIT(1* ticks)
  7: 0x00B5 [0x01] GOTO 0x0099
  8: 0x00B8 [0x00] END_REQSTACK()
```
