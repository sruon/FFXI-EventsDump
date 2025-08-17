# 17621632 - Seed Yagudo

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qu'Bia Arena (ID: 206) |
| Block Size       | 288 bytes              |
| Total Events     | 13                     |
| References Count | 16                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [5](#event-5)              | 0x0001       |      4 |              2 |
| [32001](#event-32001)      | 0x0005       |      4 |              2 |
| [65535.1](#event-655351)   | 0x0009       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0019       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0029       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0039       |     32 |              4 |
| [65535.5](#event-655355)   | 0x0059       |     14 |              4 |
| [65535.6](#event-655356)   | 0x0067       |     10 |              2 |
| [65535.7](#event-655357)   | 0x0071       |      5 |              2 |
| [65535.8](#event-655358)   | 0x0076       |     14 |              4 |
| [65535.9](#event-655359)   | 0x0084       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0094       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x00FE      |         254 |
|       2 | 0x0455      |        1109 |
|       3 | 0x003C      |          60 |
|       4 | 0x0007      |           7 |
|       5 | 0x3020      |       12320 |
|       6 | 0xFFFFF9A7  |  4294965671 |
|       7 | 0x0000      |           0 |
|       8 | 0x012C      |         300 |
|       9 | 0x0934      |        2356 |
|      10 | 0x0004      |           4 |
|      11 | 0x070C      |        1804 |
|      12 | 0xFFFFFCC4  |  4294966468 |
|      13 | 0xFFFFF9A8  |  4294965672 |
|      14 | 0x0359      |         857 |
|      15 | 0x0034      |          52 |

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
0000:                             5B 01 80 80 E2 0C 01           [......
0010: 80 E2 0C 01 74 6C 6B 30  00                       ....tlk0.       
```

#### Opcodes

```
  0: 0x0009 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Seed Yagudo (ID: 17621632/0x010CE280), Seed Yagudo (ID: 17621632/0x010CE280)], work=254*
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
0010:                             5B 01 80 80 E2 0C 01           [......
0020: 80 E2 0C 01 74 6C 6B 31  00                       ....tlk1.       
```

#### Opcodes

```
  0: 0x0019 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Seed Yagudo (ID: 17621632/0x010CE280), Seed Yagudo (ID: 17621632/0x010CE280)], work=254*
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
0020:                             5B 02 80 80 E2 0C 01           [......
0030: 80 E2 0C 01 6D 67 62 30  00                       ....mgb0.       
```

#### Opcodes

```
  0: 0x0029 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mgb0" with entities [Seed Yagudo (ID: 17621632/0x010CE280), Seed Yagudo (ID: 17621632/0x010CE280)], work=1109*
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             5B 02 80 80 E2 0C 01           [......
0040: 80 E2 0C 01 6D 67 62 32  1C 03 80 2C 80 E2 0C 01  ....mgb2...,....
0050: 80 E2 0C 01 65 66 6F 66  00                       ....efof.       
```

#### Opcodes

```
  0: 0x0039 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mgb2" with entities [Seed Yagudo (ID: 17621632/0x010CE280), Seed Yagudo (ID: 17621632/0x010CE280)], work=1109*
  1: 0x0048 [0x1C] WAIT(60* ticks)
  2: 0x004B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "efof" with entities [Seed Yagudo (ID: 17621632/0x010CE280), Seed Yagudo (ID: 17621632/0x010CE280)]
  3: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 04 80 1F 00 03 80           2......
0060: 05 80 06 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=0.060*, Z=12.320*, Y=-1.625*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      6C  80 E2 0C 01 07 80 08 80         l........
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0067 [0x6C] FADE_ENTITY_COLOR(entity_id=Seed Yagudo (ID: 17621632/0x010CE280), end_alpha=0*, fade_time=300*)
  1: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0071  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    B6 00 09 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0071 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2356*)
  1: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   32 0A  80 1F 00 0B 80 0C 80 0D        2.........
0080: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0076 [0x32] ExtData[1]->MainSpeed = 4* * 0.1
  1: 0x0079 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.804*, Z=-0.828*, Y=-1.624*
  2: 0x0081 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             5B 0E 80 80  E2 0C 01 80 E2 0C 01 77      [..........w
0090: 6E 64 31 00                                       nd1.            
```

#### Opcodes

```
  0: 0x0084 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wnd1" with entities [Seed Yagudo (ID: 17621632/0x010CE280), Seed Yagudo (ID: 17621632/0x010CE280)], work=857*
  1: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0094  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             B6 00 0F 80  00                           .....       
```

#### Opcodes

```
  0: 0x0094 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0098 [0x00] END_REQSTACK()
```
