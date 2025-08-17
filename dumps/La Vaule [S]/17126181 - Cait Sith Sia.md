# 17126181 - Cait Sith Sia

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | La Vaule [S] (ID: 85) |
| Block Size       | 380 bytes             |
| Total Events     | 13                    |
| References Count | 21                    |

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
| [65535.9](#event-655359)   | 0x0051       |     40 |              9 |
| [65535.10](#event-6553510) | 0x0079       |     45 |             10 |
| [65535.11](#event-6553511) | 0x00A6       |     60 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x409A7     |      264615 |
|       4 | 0xFFFE7E04  |  4294868484 |
|       5 | 0x1C866     |      116838 |
|       6 | 0x0458      |        1112 |
|       7 | 0xFFFEEECF  |  4294897359 |
|       8 | 0x03E8      |        1000 |
|       9 | 0x0032      |          50 |
|      10 | 0x40672     |      263794 |
|      11 | 0x1C097     |      114839 |
|      12 | 0x0C00      |        3072 |
|      13 | 0x4043C     |      263228 |
|      14 | 0xFFFEA3FC  |  4294878204 |
|      15 | 0x001E      |          30 |
|      16 | 0x1C887     |      116871 |
|      17 | 0x40ACC     |      264908 |
|      18 | 0xFFFEC389  |  4294886281 |
|      19 | 0x000A      |          10 |
|      20 | 0x0624      |        1572 |

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
  1: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=264.615*, z=-98.812*, y=116.838*, direction=97.7°*
  2: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 40 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    06 03 00 03 01 00 07  80 02 03 00 08 80 03 78   ..............x
0060: 00 08 01 00 09 80 57 03  00 37 0A 80 01 00 0B 80  ......W..7......
0070: 0C 80 1C 01 80 01 59 00  00                       ......Y..       
```

#### Opcodes

```
  0: 0x0051 [0x06] ExtData[1]->WorkLocal[3] = 0
  1: 0x0054 [0x03] ExtData[1]->WorkLocal[1] = 4294897359*
  2: 0x0059 [0x02] IF !(ExtData[1]->WorkLocal[3] >= 1000*) GOTO 0x0078
  3: 0x0061 [0x08] ExtData[1]->WorkLocal[1] -= 50*
  4: 0x0066 [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[3])
  5: 0x0069 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=263.794*, z=ExtData[1]->WorkLocal[1], y=114.839*, direction=270.0°*
  6: 0x0072 [0x1C] WAIT(1* ticks)
  7: 0x0075 [0x01] GOTO 0x0059
  8: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 45 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             06 03 00 03 00 00 0D           .......
0080: 80 03 01 00 0E 80 02 03  00 08 80 03 A5 00 08 01  ................
0090: 00 0F 80 57 03 00 37 00  00 01 00 10 80 0C 80 1C  ...W..7.........
00A0: 01 80 01 86 00 00                                 ......          
```

#### Opcodes

```
  0: 0x0079 [0x06] ExtData[1]->WorkLocal[3] = 0
  1: 0x007C [0x03] ExtData[1]->WorkLocal[0] = 263228*
  2: 0x0081 [0x03] ExtData[1]->WorkLocal[1] = 4294878204*
  3: 0x0086 [0x02] IF !(ExtData[1]->WorkLocal[3] >= 1000*) GOTO 0x00A5
  4: 0x008E [0x08] ExtData[1]->WorkLocal[1] -= 30*
  5: 0x0093 [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[3])
  6: 0x0096 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=116.871*, direction=270.0°*
  7: 0x009F [0x1C] WAIT(1* ticks)
  8: 0x00A2 [0x01] GOTO 0x0086
  9: 0x00A5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A6   |
| Data Size    | 60 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   06 03  00 03 00 00 11 80 03 01        ..........
00B0: 00 12 80 03 02 00 10 80  02 03 00 08 80 03 E1 00  ................
00C0: 07 00 00 0F 80 07 01 00  13 80 08 02 00 0F 80 57  ...............W
00D0: 03 00 37 00 00 01 00 02  00 14 80 1C 01 80 01 B8  ..7.............
00E0: 00 00                                             ..              
```

#### Opcodes

```
  0: 0x00A6 [0x06] ExtData[1]->WorkLocal[3] = 0
  1: 0x00A9 [0x03] ExtData[1]->WorkLocal[0] = 264908*
  2: 0x00AE [0x03] ExtData[1]->WorkLocal[1] = 4294886281*
  3: 0x00B3 [0x03] ExtData[1]->WorkLocal[2] = 116871*
  4: 0x00B8 [0x02] IF !(ExtData[1]->WorkLocal[3] >= 1000*) GOTO 0x00E1
  5: 0x00C0 [0x07] ExtData[1]->WorkLocal[0] += 30*
  6: 0x00C5 [0x07] ExtData[1]->WorkLocal[1] += 10*
  7: 0x00CA [0x08] ExtData[1]->WorkLocal[2] -= 30*
  8: 0x00CF [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[3])
  9: 0x00D2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=138.2°*
 10: 0x00DB [0x1C] WAIT(1* ticks)
 11: 0x00DE [0x01] GOTO 0x00B8
 12: 0x00E1 [0x00] END_REQSTACK()
```
