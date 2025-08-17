# 17834333 - The Keeper

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Rala Waterways (ID: 258) |
| Block Size       | 184 bytes                |
| Total Events     | 7                        |
| References Count | 12                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [376](#event-376)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [65535.2](#event-655352) | 0x0010       |     19 |              5 |
| [65535.3](#event-655353) | 0x0023       |     19 |              5 |
| [65535.4](#event-655354) | 0x0036       |     19 |              5 |
| [65535.5](#event-655355) | 0x0049       |     16 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFDAB60  |  4294814560 |
|       2 | 0x5D2A      |       23850 |
|       3 | 0xFFFFE97B  |  4294961531 |
|       4 | 0x0032      |          50 |
|       5 | 0x0019      |          25 |
|       6 | 0x0082      |         130 |
|       7 | 0x001E      |          30 |
|       8 | 0x0024      |          36 |
|       9 | 0x0013      |          19 |
|      10 | 0xFFFD80AA  |  4294803626 |
|      11 | 0x572F      |       22319 |

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

### Event 376

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-152.736*, Z=23.850*, Y=-5.765*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1C 04 80 6E F8 FF FF 7F  05 80 99 F8 FF FF 7F 1C  ...n............
0020: 06 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0010 [0x1C] WAIT(50* ticks)
  1: 0x0013 [0x6E] EventEntity uses emote 25*
  2: 0x001A [0x99] Wait for EventEntity animation to complete
  3: 0x001F [0x1C] WAIT(130* ticks)
  4: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1C 07 80 6E F8  FF FF 7F 08 80 99 F8 FF     ...n.........
0030: FF 7F 1C 06 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0023 [0x1C] WAIT(30* ticks)
  1: 0x0026 [0x6E] EventEntity uses emote 36*
  2: 0x002D [0x99] Wait for EventEntity animation to complete
  3: 0x0032 [0x1C] WAIT(130* ticks)
  4: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   1C 04  80 6E F8 FF FF 7F 09 80        ...n......
0040: 99 F8 FF FF 7F 1C 06 80  00                       .........       
```

#### Opcodes

```
  0: 0x0036 [0x1C] WAIT(50* ticks)
  1: 0x0039 [0x6E] EventEntity uses emote 19*
  2: 0x0040 [0x99] Wait for EventEntity animation to complete
  3: 0x0045 [0x1C] WAIT(130* ticks)
  4: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             32 00 80 1F 00 0A 80           2......
0050: 0B 80 03 80 1F 01 22 01  00                       ......"..       
```

#### Opcodes

```
  0: 0x0049 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=-163.670*, Z=22.319*, Y=-5.765*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x0058 [0x00] END_REQSTACK()
```
