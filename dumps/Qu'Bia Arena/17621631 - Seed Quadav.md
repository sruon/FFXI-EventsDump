# 17621631 - Seed Quadav

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qu'Bia Arena (ID: 206) |
| Block Size       | 288 bytes              |
| Total Events     | 14                     |
| References Count | 15                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [5](#event-5)              | 0x0001       |      4 |              2 |
| [32001](#event-32001)      | 0x0005       |      4 |              2 |
| [65535.1](#event-655351)   | 0x0009       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0019       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0029       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0039       |     14 |              4 |
| [65535.5](#event-655355)   | 0x0047       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0048       |     10 |              2 |
| [65535.7](#event-655357)   | 0x0052       |      5 |              2 |
| [65535.8](#event-655358)   | 0x0057       |     14 |              4 |
| [65535.9](#event-655359)   | 0x0065       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0075       |     32 |              4 |
| [65535.11](#event-6553511) | 0x0095       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x00E3      |         227 |
|       2 | 0x0007      |           7 |
|       3 | 0x003C      |          60 |
|       4 | 0x3020      |       12320 |
|       5 | 0xFFFFF9A7  |  4294965671 |
|       6 | 0x0000      |           0 |
|       7 | 0x00B4      |         180 |
|       8 | 0x0933      |        2355 |
|       9 | 0x0005      |           5 |
|      10 | 0xFFFFFDB3  |  4294966707 |
|      11 | 0x0319      |         793 |
|      12 | 0xFFFFF9A8  |  4294965672 |
|      13 | 0x091F      |        2335 |
|      14 | 0x0034      |          52 |

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

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    C0 00 80 00                                     ....           
```

#### Opcodes

```
  0: 0x0001 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                C0 00 80  00                            ....       
```

#### Opcodes

```
  0: 0x0005 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0009   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             5B 01 80 7F E2 0C 01           [......
0010: 7F E2 0C 01 65 76 62 30  00                       ....evb0.       
```

#### Opcodes

```
  0: 0x0009 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "evb0" with entities [Seed Quadav (ID: 17621631/0x010CE27F), Seed Quadav (ID: 17621631/0x010CE27F)], work=227*
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             5B 01 80 7F E2 0C 01           [......
0020: 7F E2 0C 01 74 6C 62 30  00                       ....tlb0.       
```

#### Opcodes

```
  0: 0x0019 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [Seed Quadav (ID: 17621631/0x010CE27F), Seed Quadav (ID: 17621631/0x010CE27F)], work=227*
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             5B 01 80 7F E2 0C 01           [......
0030: 7F E2 0C 01 74 6C 6B 31  00                       ....tlk1.       
```

#### Opcodes

```
  0: 0x0029 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Seed Quadav (ID: 17621631/0x010CE27F), Seed Quadav (ID: 17621631/0x010CE27F)], work=227*
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 02 80 1F 00 03 80           2......
0040: 04 80 05 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=0.060*, Z=12.320*, Y=-1.625*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          6C 7F E2 0C 01 06 80 07          l.......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0048 [0x6C] FADE_ENTITY_COLOR(entity_id=Seed Quadav (ID: 17621631/0x010CE27F), end_alpha=0*, fade_time=180*)
  1: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0052  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       B6 00 08 80 00                                .....         
```

#### Opcodes

```
  0: 0x0052 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2355*)
  1: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      32  09 80 1F 00 0A 80 0B 80         2........
0060: 0C 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0057 [0x32] ExtData[1]->MainSpeed = 5* * 0.1
  1: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.589*, Z=0.793*, Y=-1.624*
  2: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                5B 0D 80  7F E2 0C 01 7F E2 0C 01       [..........
0070: 67 72 64 30 00                                    grd0.           
```

#### Opcodes

```
  0: 0x0065 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "grd0" with entities [Seed Quadav (ID: 17621631/0x010CE27F), Seed Quadav (ID: 17621631/0x010CE27F)], work=2335*
  1: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                5B 0D 80  7F E2 0C 01 7F E2 0C 01       [..........
0080: 64 65 64 63 1C 03 80 2C  7F E2 0C 01 7F E2 0C 01  dedc...,........
0090: 65 66 6F 66 00                                    efof.           
```

#### Opcodes

```
  0: 0x0075 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dedc" with entities [Seed Quadav (ID: 17621631/0x010CE27F), Seed Quadav (ID: 17621631/0x010CE27F)], work=2335*
  1: 0x0084 [0x1C] WAIT(60* ticks)
  2: 0x0087 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "efof" with entities [Seed Quadav (ID: 17621631/0x010CE27F), Seed Quadav (ID: 17621631/0x010CE27F)]
  3: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0095  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                B6 00 0E  80 00                         .....      
```

#### Opcodes

```
  0: 0x0095 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0099 [0x00] END_REQSTACK()
```
