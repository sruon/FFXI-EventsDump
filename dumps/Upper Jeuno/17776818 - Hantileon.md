# 17776818 - Hantileon

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 280 bytes             |
| Total Events     | 11                    |
| References Count | 23                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10095](#event-10095)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     15 |              3 |
| [65535.2](#event-655352) | 0x0011       |     14 |              4 |
| [65535.3](#event-655353) | 0x001F       |     14 |              4 |
| [10100](#event-10100)    | 0x002D       |      1 |              1 |
| [65535.4](#event-655354) | 0x002E       |     15 |              3 |
| [65535.5](#event-655355) | 0x003D       |     32 |              8 |
| [65535.6](#event-655356) | 0x005D       |     19 |              5 |
| [65535.7](#event-655357) | 0x0070       |     15 |              3 |
| [10109](#event-10109)    | 0x007F       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF4521  |  4294919457 |
|       1 | 0x1797E     |       96638 |
|       2 | 0x1F3F      |        7999 |
|       3 | 0x06C6      |        1734 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF3132  |  4294914354 |
|       6 | 0x16D94     |       93588 |
|       7 | 0x2007      |        8199 |
|       8 | 0xFFFF5333  |  4294923059 |
|       9 | 0x15013     |       86035 |
|      10 | 0x1CEE      |        7406 |
|      11 | 0x0F03      |        3843 |
|      12 | 0xFFFF5B12  |  4294925074 |
|      13 | 0x15466     |       87142 |
|      14 | 0xFFFF5B83  |  4294925187 |
|      15 | 0x16072     |       90226 |
|      16 | 0x001E      |          30 |
|      17 | 0xFFFF4EDC  |  4294921948 |
|      18 | 0x17B58     |       97112 |
|      19 | 0xFFFFF17B  |  4294963579 |
|      20 | 0xFFFE800F  |  4294869007 |
|      21 | 0xFFFFFF9D  |  4294967197 |
|      22 | 0x0828      |        2088 |

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

### Event 10095

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
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 80 F8 FF FF 7F    7.............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-47.839*, z=96.638*, y=7.999*, direction=152.4°*
  1: 0x000B [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-52.942*, Z=93.588*, Y=8.199*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 04 80 1F 00 00 80 01 80  02 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-47.839*, Z=96.638*, Y=7.999*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x00] END_REQSTACK()
```

### Event 10100

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         00                     .  
```

#### Opcodes

```
  0: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            37 08                7.
0030: 80 09 80 0A 80 0B 80 80  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x002E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-44.237*, z=86.035*, y=7.406*, direction=337.8°*
  1: 0x0037 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 32 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         32 04 80               2..
0040: 1F 00 0C 80 0D 80 02 80  1F 01 1F 00 0E 80 0F 80  ................
0050: 02 80 1F 01 1C 10 80 1E  B1 40 0F 01 00           .........@...   
```

#### Opcodes

```
  0: 0x003D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.222*, Z=87.142*, Y=7.999*
  2: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004A [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.109*, Z=90.226*, Y=7.999*
  4: 0x0052 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0054 [0x1C] WAIT(30* ticks)
  6: 0x0057 [0x1E] EventEntity looks at Chocobo (ID: 17776817/0x010F40B1) and starts talking
  7: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         32 04 80               2..
0060: 1F 00 11 80 12 80 02 80  1F 01 1E F0 FF FF 7F 00  ................
```

#### Opcodes

```
  0: 0x005D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=-45.348*, Z=97.112*, Y=7.999*
  2: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006A [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0070   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 37 13 80 14 80 15 80 16  80 80 F8 FF FF 7F 00     7.............. 
```

#### Opcodes

```
  0: 0x0070 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-3.717*, z=-98.289*, y=-0.099*, direction=183.5°*
  1: 0x0079 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x007E [0x00] END_REQSTACK()
```

### Event 10109

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               00                 .
```

#### Opcodes

```
  0: 0x007F [0x00] END_REQSTACK()
```
