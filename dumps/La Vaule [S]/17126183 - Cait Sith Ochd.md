# 17126183 - Cait Sith Ochd

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | La Vaule [S] (ID: 85) |
| Block Size       | 376 bytes             |
| Total Events     | 14                    |
| References Count | 24                    |

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
| [65535.11](#event-6553511) | 0x0069       |     50 |             11 |
| [65535.12](#event-6553512) | 0x009B       |     50 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x411B1     |      266673 |
|       4 | 0xFFFE5951  |  4294859089 |
|       5 | 0x1C097     |      114839 |
|       6 | 0x0BC4      |        3012 |
|       7 | 0x40A01     |      264705 |
|       8 | 0xFFFE646D  |  4294861933 |
|       9 | 0x1C866     |      116838 |
|      10 | 0x0AFC      |        2812 |
|      11 | 0x41710     |      268048 |
|      12 | 0xFFFE815E  |  4294869342 |
|      13 | 0x1C666     |      116326 |
|      14 | 0x0AFB      |        2811 |
|      15 | 0x426B7     |      272055 |
|      16 | 0xFFFE477F  |  4294854527 |
|      17 | 0x03E8      |        1000 |
|      18 | 0x0028      |          40 |
|      19 | 0x1C137     |      114999 |
|      20 | 0x0800      |        2048 |
|      21 | 0x409FF     |      264703 |
|      22 | 0xFFFE6E6E  |  4294864494 |
|      23 | 0x0029      |          41 |

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
  1: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=266.673*, z=-108.207*, y=114.839*, direction=264.7°*
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
  1: 0x0053 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=264.705*, z=-105.363*, y=116.838*, direction=247.1°*
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
  1: 0x005F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=268.048*, z=-97.954*, y=116.326*, direction=247.1°*
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 50 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             06 02 00 03 00 00 0F           .......
0070: 80 03 01 00 10 80 02 02  00 11 80 03 9A 00 08 00  ................
0080: 00 12 80 07 01 00 12 80  57 02 00 37 00 00 01 00  ........W..7....
0090: 13 80 14 80 1C 01 80 01  76 00 00                 ........v..     
```

#### Opcodes

```
  0: 0x0069 [0x06] ExtData[1]->WorkLocal[2] = 0
  1: 0x006C [0x03] ExtData[1]->WorkLocal[0] = 272055*
  2: 0x0071 [0x03] ExtData[1]->WorkLocal[1] = 4294854527*
  3: 0x0076 [0x02] IF !(ExtData[1]->WorkLocal[2] >= 1000*) GOTO 0x009A
  4: 0x007E [0x08] ExtData[1]->WorkLocal[0] -= 40*
  5: 0x0083 [0x07] ExtData[1]->WorkLocal[1] += 40*
  6: 0x0088 [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[2])
  7: 0x008B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=114.999*, direction=180.0°*
  8: 0x0094 [0x1C] WAIT(1* ticks)
  9: 0x0097 [0x01] GOTO 0x0076
 10: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 50 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   06 02 00 03 00             .....
00A0: 00 15 80 03 01 00 16 80  02 02 00 11 80 03 CC 00  ................
00B0: 08 00 00 17 80 07 01 00  17 80 57 02 00 37 00 00  ..........W..7..
00C0: 01 00 13 80 0E 80 1C 01  80 01 A8 00 00           .............   
```

#### Opcodes

```
  0: 0x009B [0x06] ExtData[1]->WorkLocal[2] = 0
  1: 0x009E [0x03] ExtData[1]->WorkLocal[0] = 264703*
  2: 0x00A3 [0x03] ExtData[1]->WorkLocal[1] = 4294864494*
  3: 0x00A8 [0x02] IF !(ExtData[1]->WorkLocal[2] >= 1000*) GOTO 0x00CC
  4: 0x00B0 [0x08] ExtData[1]->WorkLocal[0] -= 41*
  5: 0x00B5 [0x07] ExtData[1]->WorkLocal[1] += 41*
  6: 0x00BA [0x57] CREATE_FRAME_DELAY(delay=ExtData[1]->WorkLocal[2])
  7: 0x00BD [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=114.999*, direction=247.1°*
  8: 0x00C6 [0x1C] WAIT(1* ticks)
  9: 0x00C9 [0x01] GOTO 0x00A8
 10: 0x00CC [0x00] END_REQSTACK()
```
