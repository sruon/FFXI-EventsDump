# 17105600 - Cait Sith Naoi

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 324 bytes                        |
| Total Events     | 11                               |
| References Count | 19                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [147](#event-147)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     10 |              2 |
| [65535.3](#event-655353) | 0x0016       |     10 |              2 |
| [65535.4](#event-655354) | 0x0020       |     10 |              2 |
| [65535.5](#event-655355) | 0x002A       |     37 |              7 |
| [65535.6](#event-655356) | 0x004F       |     22 |              6 |
| [65535.7](#event-655357) | 0x0065       |     22 |              6 |
| [65535.8](#event-655358) | 0x007B       |     22 |              6 |
| [65535.9](#event-655359) | 0x0091       |     41 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0040      |          64 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0000      |           0 |
|       4 | 0x0078      |         120 |
|       5 | 0x000D      |          13 |
|       6 | 0x0939      |        2361 |
|       7 | 0x9F16      |       40726 |
|       8 | 0xFFFFF830  |  4294965296 |
|       9 | 0x001E      |          30 |
|      10 | 0x0582      |        1410 |
|      11 | 0xFFFF9B7E  |  4294941566 |
|      12 | 0xFFFFEEBD  |  4294962877 |
|      13 | 0xFFFFDD59  |  4294958425 |
|      14 | 0xFFFFEDA5  |  4294962597 |
|      15 | 0xFFFFEC02  |  4294962178 |
|      16 | 0xFFFFF9DD  |  4294965725 |
|      17 | 0x0028      |          40 |
|      18 | 0x007F      |         127 |

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

### Event 147

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       6C F8 FF FF 7F 00  80 01 80 00                l.........    
```

#### Opcodes

```
  0: 0x0002 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=64*, fade_time=1*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      6C F8 FF FF              l...
0010: 7F 02 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   6C F8  FF FF 7F 03 80 01 80 00        l.........
```

#### Opcodes

```
  0: 0x0016 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 6C F8 FF FF 7F 03 80 04  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0020 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=120*)
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 37 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 05 80 1F 00 06            2.....
0030: 80 07 80 08 80 1F 01 1E  EF 01 05 01 1C 09 80 5B  ...............[
0040: 0A 80 F8 FF FF 7F F8 FF  FF 7F 68 69 67 30 00     ..........hig0. 
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=2.361*, Z=40.726*, Y=-2.000*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x1E] EventEntity looks at Raustigne (ID: 17105391/0x010501EF) and starts talking
  4: 0x003C [0x1C] WAIT(30* ticks)
  5: 0x003F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hig0" with entities [EventEntity, EventEntity], work=1410*
  6: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 05 80 1F 00 0B 80 0C 80  03 80 1F 01 1E 86 02 05  ................
0060: 01 1C 09 80 00                                    .....           
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-25.730*, Z=-4.419*, Y=0.000*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x1E] EventEntity looks at Ragelise (ID: 17105542/0x01050286) and starts talking
  4: 0x0061 [0x1C] WAIT(30* ticks)
  5: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                32 05 80  1F 00 0D 80 0E 80 03 80       2..........
0070: 1F 01 1E B0 02 05 01 1C  09 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0065 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0068 [0x1F] MOVE_ENTITY: EventEntity moves to X=-8.871*, Z=-4.699*, Y=0.000*
  2: 0x0070 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0072 [0x1E] EventEntity looks at Noillurie (ID: 17105584/0x010502B0) and starts talking
  4: 0x0077 [0x1C] WAIT(30* ticks)
  5: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   32 05 80 1F 00             2....
0080: 0F 80 10 80 03 80 1F 01  1E B0 02 05 01 1C 09 80  ................
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x007B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007E [0x1F] MOVE_ENTITY: EventEntity moves to X=-5.118*, Z=-1.571*, Y=0.000*
  2: 0x0086 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0088 [0x1E] EventEntity looks at Noillurie (ID: 17105584/0x010502B0) and starts talking
  4: 0x008D [0x1C] WAIT(30* ticks)
  5: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    1C 11 80 9F 12 80 F8  FF FF 7F F8 FF FF 7F 73   ..............s
00A0: 74 72 30 03 80 1C 09 80  9F 12 80 F8 FF FF 7F F8  tr0.............
00B0: FF FF 7F 6B 69 6C 6C 03  80 00                    ...kill...      
```

#### Opcodes

```
  0: 0x0091 [0x1C] WAIT(40* ticks)
  1: 0x0094 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "str0" with entities [EventEntity, EventEntity], work=[127*, 0*]
  2: 0x00A5 [0x1C] WAIT(30* ticks)
  3: 0x00A8 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "kill" with entities [EventEntity, EventEntity], work=[127*, 0*]
  4: 0x00B9 [0x00] END_REQSTACK()
```
