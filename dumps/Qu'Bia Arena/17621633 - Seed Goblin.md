# 17621633 - Seed Goblin

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qu'Bia Arena (ID: 206) |
| Block Size       | 324 bytes              |
| Total Events     | 15                     |
| References Count | 15                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [5](#event-5)              | 0x0001       |      4 |              2 |
| [32001](#event-32001)      | 0x0005       |      4 |              2 |
| [65535.1](#event-655351)   | 0x0009       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0019       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0029       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0037       |     10 |              2 |
| [65535.5](#event-655355)   | 0x0041       |      5 |              2 |
| [65535.6](#event-655356)   | 0x0046       |     14 |              4 |
| [65535.7](#event-655357)   | 0x0054       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0064       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0074       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0084       |     16 |              2 |
| [65535.11](#event-6553511) | 0x0094       |     32 |              4 |
| [65535.12](#event-6553512) | 0x00B4       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0866      |        2150 |
|       2 | 0x0007      |           7 |
|       3 | 0x003C      |          60 |
|       4 | 0x3020      |       12320 |
|       5 | 0xFFFFF9A7  |  4294965671 |
|       6 | 0x0000      |           0 |
|       7 | 0x00B4      |         180 |
|       8 | 0x0931      |        2353 |
|       9 | 0x0005      |           5 |
|      10 | 0xFFFFF5E4  |  4294964708 |
|      11 | 0x0956      |        2390 |
|      12 | 0x00D8      |         216 |
|      13 | 0x00D7      |         215 |
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
0000:                             5B 01 80 81 E2 0C 01           [......
0010: 81 E2 0C 01 74 6C 33 30  00                       ....tl30.       
```

#### Opcodes

```
  0: 0x0009 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl30" with entities [Seed Goblin (ID: 17621633/0x010CE281), Seed Goblin (ID: 17621633/0x010CE281)], work=2150*
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
0010:                             5B 01 80 81 E2 0C 01           [......
0020: 81 E2 0C 01 74 6C 33 31  00                       ....tl31.       
```

#### Opcodes

```
  0: 0x0019 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl31" with entities [Seed Goblin (ID: 17621633/0x010CE281), Seed Goblin (ID: 17621633/0x010CE281)], work=2150*
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             32 02 80 1F 00 03 80           2......
0030: 04 80 05 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0029 [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  1: 0x002C [0x1F] MOVE_ENTITY: EventEntity moves to X=0.060*, Z=12.320*, Y=-1.625*
  2: 0x0034 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      6C  81 E2 0C 01 06 80 07 80         l........
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0037 [0x6C] FADE_ENTITY_COLOR(entity_id=Seed Goblin (ID: 17621633/0x010CE281), end_alpha=0*, fade_time=180*)
  1: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0041  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    B6 00 08 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0041 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2353*)
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 09  80 1F 00 0A 80 0B 80 05        2.........
0050: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 5* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.588*, Z=2.390*, Y=-1.625*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             5B 0C 80 81  E2 0C 01 81 E2 0C 01 66      [..........f
0060: 6E 64 31 00                                       nd1.            
```

#### Opcodes

```
  0: 0x0054 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fnd1" with entities [Seed Goblin (ID: 17621633/0x010CE281), Seed Goblin (ID: 17621633/0x010CE281)], work=216*
  1: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             5B 0D 80 81  E2 0C 01 81 E2 0C 01 63      [..........c
0070: 6F 72 30 00                                       or0.            
```

#### Opcodes

```
  0: 0x0064 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "cor0" with entities [Seed Goblin (ID: 17621633/0x010CE281), Seed Goblin (ID: 17621633/0x010CE281)], work=215*
  1: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             5B 0D 80 81  E2 0C 01 81 E2 0C 01 6F      [..........o
0080: 6B 69 30 00                                       ki0.            
```

#### Opcodes

```
  0: 0x0074 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "oki0" with entities [Seed Goblin (ID: 17621633/0x010CE281), Seed Goblin (ID: 17621633/0x010CE281)], work=215*
  1: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             5B 0D 80 81  E2 0C 01 81 E2 0C 01 74      [..........t
0090: 6C 6B 32 00                                       lk2.            
```

#### Opcodes

```
  0: 0x0084 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [Seed Goblin (ID: 17621633/0x010CE281), Seed Goblin (ID: 17621633/0x010CE281)], work=215*
  1: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             5B 0D 80 81  E2 0C 01 81 E2 0C 01 74      [..........t
00A0: 61 6F 31 1C 03 80 2C 81  E2 0C 01 81 E2 0C 01 65  ao1...,........e
00B0: 66 6F 66 00                                       fof.            
```

#### Opcodes

```
  0: 0x0094 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tao1" with entities [Seed Goblin (ID: 17621633/0x010CE281), Seed Goblin (ID: 17621633/0x010CE281)], work=215*
  1: 0x00A3 [0x1C] WAIT(60* ticks)
  2: 0x00A6 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "efof" with entities [Seed Goblin (ID: 17621633/0x010CE281), Seed Goblin (ID: 17621633/0x010CE281)]
  3: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B4  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             B6 00 0E 80  00                           .....       
```

#### Opcodes

```
  0: 0x00B4 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x00B8 [0x00] END_REQSTACK()
```
