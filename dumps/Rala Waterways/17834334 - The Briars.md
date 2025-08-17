# 17834334 - The Briars

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Rala Waterways (ID: 258) |
| Block Size       | 204 bytes                |
| Total Events     | 7                        |
| References Count | 14                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [376](#event-376)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [65535.2](#event-655352) | 0x0010       |     31 |              9 |
| [65535.3](#event-655353) | 0x002F       |     19 |              5 |
| [65535.4](#event-655354) | 0x0042       |     19 |              5 |
| [65535.5](#event-655355) | 0x0055       |     16 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFDAD7E  |  4294815102 |
|       2 | 0x5644      |       22084 |
|       3 | 0xFFFFE97B  |  4294961531 |
|       4 | 0x0082      |         130 |
|       5 | 0x0022      |          34 |
|       6 | 0x0096      |         150 |
|       7 | 0x005A      |          90 |
|       8 | 0x0007      |           7 |
|       9 | 0x003C      |          60 |
|      10 | 0x0046      |          70 |
|      11 | 0x0005      |           5 |
|      12 | 0xFFFD87B8  |  4294805432 |
|      13 | 0x49E1      |       18913 |

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
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-152.194*, Z=22.084*, Y=-5.765*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1C 04 80 1E 5D 21 10 01  6F 70 6E F8 FF FF 7F 05  ....]!..opn.....
0020: 80 99 F8 FF FF 7F 1C 06  80 1E 5B 21 10 01 00     ..........[!... 
```

#### Opcodes

```
  0: 0x0010 [0x1C] WAIT(130* ticks)
  1: 0x0013 [0x1E] EventEntity looks at The Keeper (ID: 17834333/0x0110215D) and starts talking
  2: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0019 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x001A [0x6E] EventEntity uses emote 34*
  5: 0x0021 [0x99] Wait for EventEntity animation to complete
  6: 0x0026 [0x1C] WAIT(150* ticks)
  7: 0x0029 [0x1E] EventEntity looks at Margret (ID: 17834331/0x0110215B) and starts talking
  8: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               1C                 .
0030: 07 80 6E F8 FF FF 7F 08  80 99 F8 FF FF 7F 1C 09  ..n.............
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x002F [0x1C] WAIT(90* ticks)
  1: 0x0032 [0x6E] EventEntity uses emote 7*
  2: 0x0039 [0x99] Wait for EventEntity animation to complete
  3: 0x003E [0x1C] WAIT(60* ticks)
  4: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       1C 0A 80 6E F8 FF  FF 7F 0B 80 99 F8 FF FF    ...n..........
0050: 7F 1C 04 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0042 [0x1C] WAIT(70* ticks)
  1: 0x0045 [0x6E] EventEntity uses emote 5*
  2: 0x004C [0x99] Wait for EventEntity animation to complete
  3: 0x0051 [0x1C] WAIT(130* ticks)
  4: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                32 00 80  1F 00 0C 80 0D 80 03 80       2..........
0060: 1F 01 22 01 00                                    .."..           
```

#### Opcodes

```
  0: 0x0055 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=-161.864*, Z=18.913*, Y=-5.765*
  2: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0062 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x0064 [0x00] END_REQSTACK()
```
