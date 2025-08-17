# 17867234 - Soraa Ishakal

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Marjami Ravine (ID: 266) |
| Block Size       | 300 bytes                |
| Total Events     | 13                       |
| References Count | 26                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [55](#event-55)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [57](#event-57)          | 0x000C       |      1 |              1 |
| [65535.2](#event-655352) | 0x000D       |     10 |              2 |
| [65535.3](#event-655353) | 0x0017       |     10 |              2 |
| [65535.4](#event-655354) | 0x0021       |     14 |              4 |
| [65535.5](#event-655355) | 0x002F       |     22 |              6 |
| [65535.6](#event-655356) | 0x0045       |     14 |              4 |
| [65](#event-65)          | 0x0053       |      1 |              1 |
| [65535.7](#event-655357) | 0x0054       |     19 |              5 |
| [65535.8](#event-655358) | 0x0067       |     24 |              6 |
| [66](#event-66)          | 0x007F       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x003C      |          60 |
|       2 | 0x0040      |          64 |
|       3 | 0x0001      |           1 |
|       4 | 0x0080      |         128 |
|       5 | 0x000D      |          13 |
|       6 | 0x1518D     |       86413 |
|       7 | 0xFFFE3FAC  |  4294852524 |
|       8 | 0x4F30      |       20272 |
|       9 | 0x0028      |          40 |
|      10 | 0xF75D      |       63325 |
|      11 | 0xFFFED7D4  |  4294891476 |
|      12 | 0x4A80      |       19072 |
|      13 | 0x001E      |          30 |
|      14 | 0x0180      |         384 |
|      15 | 0xFFFF7B74  |  4294933364 |
|      16 | 0x4E1F      |       19999 |
|      17 | 0x180E4     |       98532 |
|      18 | 0xFFFE1DC3  |  4294843843 |
|      19 | 0x51BE      |       20926 |
|      20 | 0x17190     |       94608 |
|      21 | 0xFFFE3036  |  4294848566 |
|      22 | 0x5071      |       20593 |
|      23 | 0x13F06     |       81670 |
|      24 | 0xFFFE3F47  |  4294852423 |
|      25 | 0x4EBC      |       20156 |

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

### Event 55

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
  0: 0x0002 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 57

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      00                       .   
```

#### Opcodes

```
  0: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         6C F8 FF               l..
0010: FF 7F 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=64*, fade_time=1*)
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      6C  F8 FF FF 7F 04 80 03 80         l........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0017 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 05 80 1F 00 06 80  07 80 08 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=86.413*, Z=-114.772*, Y=20.272*
  2: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 09 80 1F 00 0A 80 0B 80  0C 80 1F 01 1E F0 FF FF  ................
0040: 7F 1C 0D 80 00                                    .....           
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=63.325*, Z=-75.820*, Y=19.072*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0041 [0x1C] WAIT(30* ticks)
  5: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                32 09 80  1F 00 0E 80 0F 80 10 80       2..........
0050: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0045 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.384*, Z=-33.932*, Y=19.999*
  2: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0052 [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0053  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          00                                          .            
```

#### Opcodes

```
  0: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             32 09 80 1F  00 11 80 12 80 13 80 1F      2...........
0060: 01 1E E1 A1 10 01 00                              .......         
```

#### Opcodes

```
  0: 0x0054 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=98.532*, Z=-123.453*, Y=20.926*
  2: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0061 [0x1E] EventEntity looks at Nashu (ID: 17867233/0x0110A1E1) and starts talking
  4: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      32  09 80 1F 00 14 80 15 80         2........
0070: 16 80 1F 01 1F 00 17 80  18 80 19 80 1F 01 00     ............... 
```

#### Opcodes

```
  0: 0x0067 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=94.608*, Z=-118.730*, Y=20.593*
  2: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=81.670*, Z=-114.873*, Y=20.156*
  4: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x007E [0x00] END_REQSTACK()
```

### Event 66

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
