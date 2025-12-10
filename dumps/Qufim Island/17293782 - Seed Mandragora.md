# 17293782 - Seed Mandragora

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qufim Island (ID: 126) |
| Block Size       | 216 bytes              |
| Total Events     | 11                     |
| References Count | 15                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [31](#event-31)          | 0x0001       |      4 |              2 |
| [65535.1](#event-655351) | 0x0005       |     20 |              5 |
| [65535.2](#event-655352) | 0x0019       |      5 |              2 |
| [65535.3](#event-655353) | 0x001E       |      5 |              2 |
| [65535.4](#event-655354) | 0x0023       |      5 |              2 |
| [65535.5](#event-655355) | 0x0028       |      5 |              2 |
| [32](#event-32)          | 0x002D       |      4 |              2 |
| [65535.6](#event-655356) | 0x0031       |     20 |              5 |
| [65535.7](#event-655357) | 0x0045       |     20 |              5 |
| [34](#event-34)          | 0x0059       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x000D      |          13 |
|       2 | 0x1191      |        4497 |
|       3 | 0x351BA     |      217530 |
|       4 | 0xFFFFA7C7  |  4294944711 |
|       5 | 0x0164      |         356 |
|       6 | 0x00ED      |         237 |
|       7 | 0x012C      |         300 |
|       8 | 0x0930      |        2352 |
|       9 | 0xFFFE0760  |  4294838112 |
|      10 | 0x47C5F     |      293983 |
|      11 | 0xFFFFB3E3  |  4294947811 |
|      12 | 0x0028      |          40 |
|      13 | 0xFFFE12B4  |  4294841012 |
|      14 | 0x4855B     |      296283 |

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

### Event 31

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                59 04 D6  E1 07 01 01 80 1F 00 02       Y..........
0010: 80 03 80 04 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0005 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293782/0x0107E1D6) main speed = 13* * 0.1
  1: 0x000D [0x1F] MOVE_ENTITY: EventEntity moves to X=4.497*, Z=217.530*, Y=-22.585*
  2: 0x0015 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0017 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             B6 00 05 80 00                 .....  
```

#### Opcodes

```
  0: 0x0019 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=356*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            B6 00                ..
0020: 06 80 00                                          ...             
```

#### Opcodes

```
  0: 0x001E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=237*)
  1: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          B6 00 07 80 00                              .....        
```

#### Opcodes

```
  0: 0x0023 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=300*)
  1: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          B6 00 08 80 00                   .....   
```

#### Opcodes

```
  0: 0x0028 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2352*)
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         C0 00 80               ...
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x002D [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    59 04 D6 E1 07 01 01  80 1F 00 09 80 0A 80 0B   Y..............
0040: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0031 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293782/0x0107E1D6) main speed = 13* * 0.1
  1: 0x0039 [0x1F] MOVE_ENTITY: EventEntity moves to X=-129.184*, Z=293.983*, Y=-19.485*
  2: 0x0041 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0043 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                59 04 D6  E1 07 01 0C 80 1F 00 0D       Y..........
0050: 80 0E 80 0B 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0045 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293782/0x0107E1D6) main speed = 40* * 0.1
  1: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=-126.284*, Z=296.283*, Y=-19.485*
  2: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0057 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0058 [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0059  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             C0 00 80 00                    ....   
```

#### Opcodes

```
  0: 0x0059 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x005C [0x00] END_REQSTACK()
```
