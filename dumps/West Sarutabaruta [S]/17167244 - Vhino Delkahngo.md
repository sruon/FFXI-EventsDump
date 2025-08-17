# 17167244 - Vhino Delkahngo

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 500 bytes                      |
| Total Events     | 18                             |
| References Count | 35                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [110](#event-110)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     13 |              3 |
| [65535.2](#event-655352)   | 0x000F       |     21 |              2 |
| [65535.3](#event-655353)   | 0x0024       |     21 |              2 |
| [65535.4](#event-655354)   | 0x0039       |     21 |              2 |
| [65535.5](#event-655355)   | 0x004E       |     27 |              7 |
| [65535.6](#event-655356)   | 0x0069       |     36 |              8 |
| [65535.7](#event-655357)   | 0x008D       |     44 |             10 |
| [65535.8](#event-655358)   | 0x00B9       |     10 |              2 |
| [65535.9](#event-655359)   | 0x00C3       |     10 |              2 |
| [65535.10](#event-6553510) | 0x00CD       |      1 |              1 |
| [65535.11](#event-6553511) | 0x00CE       |     18 |              4 |
| [65535.12](#event-6553512) | 0x00E0       |     10 |              2 |
| [65535.13](#event-6553513) | 0x00EA       |      9 |              3 |
| [65535.14](#event-6553514) | 0x00F3       |      9 |              3 |
| [65535.15](#event-6553515) | 0x00FC       |     10 |              2 |
| [65535.16](#event-6553516) | 0x0106       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0004      |           4 |
|       1 | 0x0007      |           7 |
|       2 | 0x000E      |          14 |
|       3 | 0x0089      |         137 |
|       4 | 0x0010      |          16 |
|       5 | 0x011C      |         284 |
|       6 | 0x0000      |           0 |
|       7 | 0x0006      |           6 |
|       8 | 0x0086      |         134 |
|       9 | 0x000F      |          15 |
|      10 | 0x005B      |          91 |
|      11 | 0x0032      |          50 |
|      12 | 0x0005      |           5 |
|      13 | 0x0019      |          25 |
|      14 | 0x0016      |          22 |
|      15 | 0x0014      |          20 |
|      16 | 0x002B      |          43 |
|      17 | 0xFFFB63BF  |  4294665151 |
|      18 | 0xFFFFCEB4  |  4294954676 |
|      19 | 0xFFFF4480  |  4294919296 |
|      20 | 0xFFFB45AD  |  4294657453 |
|      21 | 0xFFFFCD67  |  4294954343 |
|      22 | 0x0050      |          80 |
|      23 | 0x0122      |         290 |
|      24 | 0x0080      |         128 |
|      25 | 0x0001      |           1 |
|      26 | 0xFFFBA9D7  |  4294683095 |
|      27 | 0xFFFFCC8F  |  4294954127 |
|      28 | 0xFFFB884D  |  4294674509 |
|      29 | 0xFFFFCBE5  |  4294953957 |
|      30 | 0xFFFF4481  |  4294919297 |
|      31 | 0xFFFB88D2  |  4294674642 |
|      32 | 0xFFFFA1E0  |  4294943200 |
|      33 | 0xFFFB7A87  |  4294670983 |
|      34 | 0xFFFF97F8  |  4294940664 |

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
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       6E F8 FF FF 7F 00  80 99 F8 FF FF 7F 00       n............ 
```

#### Opcodes

```
  0: 0x0002 [0x6E] EventEntity uses emote 4*
  1: 0x0009 [0x99] Wait for EventEntity animation to complete
  2: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               B6                 .
0010: 0B 01 80 02 80 03 80 03  80 04 80 04 80 04 80 05  ................
0020: 80 06 80 00                                       ....            
```

#### Opcodes

```
  0: 0x000F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=14*, head=137*, body=137*, hands=16*, legs=16*, feet=16*, main=284*, sub=0*)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             B6 0B 01 80  07 80 08 80 08 80 08 80      ............
0030: 09 80 08 80 0A 80 0B 80  00                       .........       
```

#### Opcodes

```
  0: 0x0024 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=6*, head=134*, body=134*, hands=134*, legs=15*, feet=134*, main=91*, sub=50*)
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             B6 0B 0C 80 00 80 0D           .......
0040: 80 0D 80 0D 80 0E 80 0E  80 06 80 06 80 00        ..............  
```

#### Opcodes

```
  0: 0x0039 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=4*, head=25*, body=25*, hands=25*, legs=22*, feet=22*, main=0*, sub=0*)
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            1C 0F                ..
0050: 80 32 10 80 1F 00 11 80  12 80 13 80 1F 01 1F 00  .2..............
0060: 14 80 15 80 13 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x004E [0x1C] WAIT(20* ticks)
  1: 0x0051 [0x32] ExtData[1]->MainSpeed = 43* * 0.1
  2: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.145*, Z=-12.620*, Y=-48.000*
  3: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=-309.843*, Z=-12.953*, Y=-48.000*
  5: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 36 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             32 16 80 1C 17 80 6C           2.....l
0070: F8 FF FF 7F 18 80 19 80  1F 00 11 80 12 80 13 80  ................
0080: 1F 01 1F 00 1A 80 1B 80  13 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x0069 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x006C [0x1C] WAIT(290* ticks)
  2: 0x006F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  3: 0x0078 [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.145*, Z=-12.620*, Y=-48.000*
  4: 0x0080 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=-284.201*, Z=-13.169*, Y=-48.000*
  6: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         32 16 80               2..
0090: 1F 00 1C 80 1D 80 1E 80  1F 01 1F 00 1F 80 20 80  .............. .
00A0: 13 80 1F 01 1F 00 21 80  22 80 13 80 1F 01 1F 00  ......!.".......
00B0: 21 80 22 80 13 80 1F 01  00                       !."......       
```

#### Opcodes

```
  0: 0x008D [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0090 [0x1F] MOVE_ENTITY: EventEntity moves to X=-292.787*, Z=-13.339*, Y=-47.999*
  2: 0x0098 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009A [0x1F] MOVE_ENTITY: EventEntity moves to X=-292.654*, Z=-24.096*, Y=-48.000*
  4: 0x00A2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00A4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-296.313*, Z=-26.632*, Y=-48.000*
  6: 0x00AC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00AE [0x1F] MOVE_ENTITY: EventEntity moves to X=-296.313*, Z=-26.632*, Y=-48.000*
  8: 0x00B6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             6C F8 FF FF 7F 06 80           l......
00C0: 19 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00B9 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          6C F8 FF FF 7F  18 80 19 80 00              l.........   
```

#### Opcodes

```
  0: 0x00C3 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00CC [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         00                     .  
```

#### Opcodes

```
  0: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            22 00                ".
00D0: 2F 00 F8 FF FF 7F 6C F8  FF FF 7F 06 80 19 80 00  /.....l.........
```

#### Opcodes

```
  0: 0x00CE [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00D0 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00D6 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x00DF [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 6C F8 FF FF 7F 18 80 19  80 00                    l.........      
```

#### Opcodes

```
  0: 0x00E0 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00E9 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EA  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                22 00 2F 00 F8 FF            "./...
00F0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x00EA [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00EC [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00F2 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F3  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          22 01 2F 01 F8  FF FF 7F 00                 "./......    
```

#### Opcodes

```
  0: 0x00F3 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00F5 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      6C F8 FF FF              l...
0100: 7F 06 80 19 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00FC [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0105 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0106   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                   6C F8  FF FF 7F 18 80 19 80 00        l.........
```

#### Opcodes

```
  0: 0x0106 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x010F [0x00] END_REQSTACK()
```
