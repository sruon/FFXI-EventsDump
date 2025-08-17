# 17167252 - Rakocha-Mukocha

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 352 bytes                      |
| Total Events     | 14                             |
| References Count | 21                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [110](#event-110)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     27 |              7 |
| [65535.2](#event-655352)   | 0x001D       |     36 |              8 |
| [65535.3](#event-655353)   | 0x0041       |     44 |             10 |
| [65535.4](#event-655354)   | 0x006D       |     10 |              2 |
| [65535.5](#event-655355)   | 0x0077       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0081       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0082       |     18 |              4 |
| [65535.8](#event-655358)   | 0x0094       |     10 |              2 |
| [65535.9](#event-655359)   | 0x009E       |      9 |              3 |
| [65535.10](#event-6553510) | 0x00A7       |      9 |              3 |
| [65535.11](#event-6553511) | 0x00B0       |     10 |              2 |
| [65535.12](#event-6553512) | 0x00BA       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x002B      |          43 |
|       2 | 0xFFFB63BF  |  4294665151 |
|       3 | 0xFFFFCEB4  |  4294954676 |
|       4 | 0xFFFF4480  |  4294919296 |
|       5 | 0xFFFB45AD  |  4294657453 |
|       6 | 0xFFFFCD67  |  4294954343 |
|       7 | 0x0050      |          80 |
|       8 | 0x0122      |         290 |
|       9 | 0x0080      |         128 |
|      10 | 0x0001      |           1 |
|      11 | 0xFFFBA9D7  |  4294683095 |
|      12 | 0xFFFFCC8F  |  4294954127 |
|      13 | 0xFFFB884D  |  4294674509 |
|      14 | 0xFFFFCBE5  |  4294953957 |
|      15 | 0xFFFF4481  |  4294919297 |
|      16 | 0xFFFB88D2  |  4294674642 |
|      17 | 0xFFFFA1E0  |  4294943200 |
|      18 | 0xFFFB7A87  |  4294670983 |
|      19 | 0xFFFF97F8  |  4294940664 |
|      20 | 0x0000      |           0 |

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
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1C 00 80 32 01 80  1F 00 02 80 03 80 04 80    ...2..........
0010: 1F 01 1F 00 05 80 06 80  04 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x0002 [0x1C] WAIT(20* ticks)
  1: 0x0005 [0x32] ExtData[1]->MainSpeed = 43* * 0.1
  2: 0x0008 [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.145*, Z=-12.620*, Y=-48.000*
  3: 0x0010 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-309.843*, Z=-12.953*, Y=-48.000*
  5: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 36 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         32 07 80               2..
0020: 1C 08 80 6C F8 FF FF 7F  09 80 0A 80 1F 00 02 80  ...l............
0030: 03 80 04 80 1F 01 1F 00  0B 80 0C 80 04 80 1F 01  ................
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x001D [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0020 [0x1C] WAIT(290* ticks)
  2: 0x0023 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  3: 0x002C [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.145*, Z=-12.620*, Y=-48.000*
  4: 0x0034 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-284.201*, Z=-13.169*, Y=-48.000*
  6: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    32 07 80 1F 00 0D 80  0E 80 0F 80 1F 01 1F 00   2..............
0050: 10 80 11 80 04 80 1F 01  1F 00 12 80 13 80 04 80  ................
0060: 1F 01 1F 00 12 80 13 80  04 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x0041 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=-292.787*, Z=-13.339*, Y=-47.999*
  2: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=-292.654*, Z=-24.096*, Y=-48.000*
  4: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=-296.313*, Z=-26.632*, Y=-48.000*
  6: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0062 [0x1F] MOVE_ENTITY: EventEntity moves to X=-296.313*, Z=-26.632*, Y=-48.000*
  8: 0x006A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         6C F8 FF               l..
0070: FF 7F 14 80 0A 80 00                              .......         
```

#### Opcodes

```
  0: 0x006D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      6C  F8 FF FF 7F 09 80 0A 80         l........
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0077 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0081  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    00                                              .              
```

#### Opcodes

```
  0: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 14    "./.....l.....
0090: 80 0A 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0082 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0084 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x008A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             6C F8 FF FF  7F 09 80 0A 80 00            l.........  
```

#### Opcodes

```
  0: 0x0094 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            22 00                ".
00A0: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x009E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00A0 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A7  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x00A7 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00A9 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 6C F8 FF FF 7F 14 80 0A  80 00                    l.........      
```

#### Opcodes

```
  0: 0x00B0 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x00B9 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BA   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                6C F8 FF FF 7F 09            l.....
00C0: 80 0A 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00BA [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00C3 [0x00] END_REQSTACK()
```
