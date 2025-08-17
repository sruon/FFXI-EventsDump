# 17167250 - Doron-Fulun

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 444 bytes                      |
| Total Events     | 14                             |
| References Count | 34                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [110](#event-110)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     37 |              9 |
| [65535.2](#event-655352)   | 0x0027       |     56 |             12 |
| [65535.3](#event-655353)   | 0x005F       |     54 |             12 |
| [65535.4](#event-655354)   | 0x0095       |     10 |              2 |
| [65535.5](#event-655355)   | 0x009F       |     10 |              2 |
| [65535.6](#event-655356)   | 0x00A9       |      1 |              1 |
| [65535.7](#event-655357)   | 0x00AA       |     18 |              4 |
| [65535.8](#event-655358)   | 0x00BC       |     10 |              2 |
| [65535.9](#event-655359)   | 0x00C6       |      9 |              3 |
| [65535.10](#event-6553510) | 0x00CF       |      9 |              3 |
| [65535.11](#event-6553511) | 0x00D8       |     10 |              2 |
| [65535.12](#event-6553512) | 0x00E2       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x002B      |          43 |
|       1 | 0x0005      |           5 |
|       2 | 0xFFFB7848  |  4294670408 |
|       3 | 0xFFFFCD01  |  4294954241 |
|       4 | 0xFFFF4480  |  4294919296 |
|       5 | 0xFFFB66BA  |  4294665914 |
|       6 | 0xFFFFCEF9  |  4294954745 |
|       7 | 0xFFFB4444  |  4294657092 |
|       8 | 0xFFFFCC9E  |  4294954142 |
|       9 | 0x004B      |          75 |
|      10 | 0x00FA      |         250 |
|      11 | 0x0080      |         128 |
|      12 | 0x0001      |           1 |
|      13 | 0xFFFB56B6  |  4294661814 |
|      14 | 0xFFFFD16F  |  4294955375 |
|      15 | 0xFFFF4481  |  4294919297 |
|      16 | 0xFFFB7107  |  4294668551 |
|      17 | 0xFFFFF042  |  4294963266 |
|      18 | 0xFFFB7BC6  |  4294671302 |
|      19 | 0x072E      |        1838 |
|      20 | 0xFFFB7EA4  |  4294672036 |
|      21 | 0x29B8      |       10680 |
|      22 | 0x0050      |          80 |
|      23 | 0xFFFB8958  |  4294674776 |
|      24 | 0xFFFFCCEE  |  4294954222 |
|      25 | 0xFFFB828D  |  4294673037 |
|      26 | 0xFFFFD299  |  4294955673 |
|      27 | 0xFFFB80BB  |  4294672571 |
|      28 | 0xFFFFE207  |  4294959623 |
|      29 | 0xFFFB7106  |  4294668550 |
|      30 | 0x1688      |        5768 |
|      31 | 0xFFFB764E  |  4294669902 |
|      32 | 0x26FF      |        9983 |
|      33 | 0x0000      |           0 |

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

### Event 110

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1C 01 80  1F 00 02 80 03 80 04 80    2.............
0010: 1F 01 1F 00 05 80 06 80  04 80 1F 01 1F 00 07 80  ................
0020: 08 80 04 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 43* * 0.1
  1: 0x0005 [0x1C] WAIT(5* ticks)
  2: 0x0008 [0x1F] MOVE_ENTITY: EventEntity moves to X=-296.888*, Z=-13.055*, Y=-48.000*
  3: 0x0010 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-301.382*, Z=-12.551*, Y=-48.000*
  5: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=-310.204*, Z=-13.154*, Y=-48.000*
  7: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 56 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  09 80 1C 0A 80 6C F8 FF         2.....l..
0030: FF 7F 0B 80 0C 80 1F 00  0D 80 0E 80 0F 80 1F 01  ................
0040: 1F 00 10 80 11 80 0F 80  1F 01 1F 00 12 80 13 80  ................
0050: 0F 80 1F 01 1F 00 14 80  15 80 0F 80 1F 01 00     ............... 
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 75* * 0.1
  1: 0x002A [0x1C] WAIT(250* ticks)
  2: 0x002D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  3: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-305.482*, Z=-11.921*, Y=-47.999*
  4: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=-298.745*, Z=-4.030*, Y=-47.999*
  6: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x004A [0x1F] MOVE_ENTITY: EventEntity moves to X=-295.994*, Z=1.838*, Y=-47.999*
  8: 0x0052 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=-295.260*, Z=10.680*, Y=-47.999*
 10: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 54 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               32                 2
0060: 16 80 1F 00 17 80 18 80  0F 80 1F 01 1F 00 19 80  ................
0070: 1A 80 0F 80 1F 01 1F 00  1B 80 1C 80 0F 80 1F 01  ................
0080: 1F 00 1D 80 1E 80 0F 80  1F 01 1F 00 1F 80 20 80  .............. .
0090: 0F 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x005F [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0062 [0x1F] MOVE_ENTITY: EventEntity moves to X=-292.520*, Z=-13.074*, Y=-47.999*
  2: 0x006A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=-294.259*, Z=-11.623*, Y=-47.999*
  4: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0076 [0x1F] MOVE_ENTITY: EventEntity moves to X=-294.725*, Z=-7.673*, Y=-47.999*
  6: 0x007E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0080 [0x1F] MOVE_ENTITY: EventEntity moves to X=-298.746*, Z=5.768*, Y=-47.999*
  8: 0x0088 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x008A [0x1F] MOVE_ENTITY: EventEntity moves to X=-297.394*, Z=9.983*, Y=-47.999*
 10: 0x0092 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                6C F8 FF  FF 7F 21 80 0C 80 00          l....!.... 
```

#### Opcodes

```
  0: 0x0095 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               6C                 l
00A0: F8 FF FF 7F 0B 80 0C 80  00                       .........       
```

#### Opcodes

```
  0: 0x009F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             00                             .      
```

#### Opcodes

```
  0: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                22 00 2F 00 F8 FF            "./...
00B0: FF 7F 6C F8 FF FF 7F 21  80 0C 80 00              ..l....!....    
```

#### Opcodes

```
  0: 0x00AA [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00AC [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00B2 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      6C F8 FF FF              l...
00C0: 7F 0B 80 0C 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00BC [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C6  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   22 00  2F 00 F8 FF FF 7F 00           "./...... 
```

#### Opcodes

```
  0: 0x00C6 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00C8 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00CE [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CF  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                               22                 "
00D0: 01 2F 01 F8 FF FF 7F 00                           ./......        
```

#### Opcodes

```
  0: 0x00CF [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00D1 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x00D7 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D8   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                          6C F8 FF FF 7F 21 80 0C          l....!..
00E0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00D8 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x00E1 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E2   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:       6C F8 FF FF 7F 0B  80 0C 80 00                l.........    
```

#### Opcodes

```
  0: 0x00E2 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00EB [0x00] END_REQSTACK()
```
