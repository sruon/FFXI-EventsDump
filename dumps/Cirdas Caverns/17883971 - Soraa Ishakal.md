# 17883971 - Soraa Ishakal

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Cirdas Caverns (ID: 270) |
| Block Size       | 200 bytes                |
| Total Events     | 8                        |
| References Count | 17                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [27](#event-27)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      5 |              2 |
| [65535.2](#event-655352) | 0x0007       |     24 |              6 |
| [65535.3](#event-655353) | 0x001F       |     14 |              4 |
| [33](#event-33)          | 0x002D       |      1 |              1 |
| [65535.4](#event-655354) | 0x002E       |     22 |              6 |
| [65535.5](#event-655355) | 0x0044       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x005D      |          93 |
|       1 | 0x000D      |          13 |
|       2 | 0xFFFE7856  |  4294867030 |
|       3 | 0x33304     |      209668 |
|       4 | 0x79B1      |       31153 |
|       5 | 0x0350      |         848 |
|       6 | 0x001E      |          30 |
|       7 | 0xFFFE7D0C  |  4294868236 |
|       8 | 0x30B3B     |      199483 |
|       9 | 0x7A4C      |       31308 |
|      10 | 0x57483     |      357507 |
|      11 | 0x2F963     |      194915 |
|      12 | 0x75B4      |       30132 |
|      13 | 0x0028      |          40 |
|      14 | 0x59808     |      366600 |
|      15 | 0x30B5F     |      199519 |
|      16 | 0x75AE      |       30126 |

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

### Event 27

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       B6 0F 00 80 00                                .....         
```

#### Opcodes

```
  0: 0x0002 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=93*)
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      32  01 80 1F 00 02 80 03 80         2........
0010: 04 80 1F 01 4B F8 FF FF  7F 05 80 1C 06 80 00     ....K.......... 
```

#### Opcodes

```
  0: 0x0007 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000A [0x1F] MOVE_ENTITY: EventEntity moves to X=-100.266*, Z=209.668*, Y=31.153*
  2: 0x0012 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0014 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=4.7°*)
  4: 0x001B [0x1C] WAIT(30* ticks)
  5: 0x001E [0x00] END_REQSTACK()
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
0020: 01 80 1F 00 07 80 08 80  09 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.060*, Z=199.483*, Y=31.308*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x00] END_REQSTACK()
```

### Event 33

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            32 01                2.
0030: 80 1F 00 0A 80 0B 80 0C  80 1F 01 1E 42 E3 10 01  ............B...
0040: 1C 06 80 00                                       ....            
```

#### Opcodes

```
  0: 0x002E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=357.507*, Z=194.915*, Y=30.132*
  2: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003B [0x1E] EventEntity looks at Nashu (ID: 17883970/0x0110E342) and starts talking
  4: 0x0040 [0x1C] WAIT(30* ticks)
  5: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             32 0D 80 1F  00 0E 80 0F 80 10 80 1F      2...........
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0044 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=366.600*, Z=199.519*, Y=30.126*
  2: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0051 [0x00] END_REQSTACK()
```
