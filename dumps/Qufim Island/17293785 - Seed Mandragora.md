# 17293785 - Seed Mandragora

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qufim Island (ID: 126) |
| Block Size       | 180 bytes              |
| Total Events     | 10                     |
| References Count | 12                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [31](#event-31)          | 0x0001       |      4 |              2 |
| [65535.1](#event-655351) | 0x0005       |      5 |              2 |
| [65535.2](#event-655352) | 0x000A       |      5 |              2 |
| [65535.3](#event-655353) | 0x000F       |      5 |              2 |
| [65535.4](#event-655354) | 0x0014       |      5 |              2 |
| [32](#event-32)          | 0x0019       |      4 |              2 |
| [65535.5](#event-655355) | 0x001D       |     20 |              5 |
| [65535.6](#event-655356) | 0x0031       |     20 |              5 |
| [34](#event-34)          | 0x0045       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x015C      |         348 |
|       2 | 0x00C7      |         199 |
|       3 | 0x012C      |         300 |
|       4 | 0x0930      |        2352 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFE0378  |  4294837112 |
|       7 | 0x47C5F     |      293983 |
|       8 | 0xFFFFB3E3  |  4294947811 |
|       9 | 0x0028      |          40 |
|      10 | 0xFFFE20C4  |  4294844612 |
|      11 | 0x48DF3     |      298483 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                B6 00 01  80 00                         .....      
```

#### Opcodes

```
  0: 0x0005 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=348*)
  1: 0x0009 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                B6 00 02 80 00               ..... 
```

#### Opcodes

```
  0: 0x000A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=199*)
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               B6                 .
0010: 00 03 80 00                                       ....            
```

#### Opcodes

```
  0: 0x000F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=300*)
  1: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             B6 00 04 80  00                           .....       
```

#### Opcodes

```
  0: 0x0014 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2352*)
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             C0 00 80 00                    ....   
```

#### Opcodes

```
  0: 0x0019 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         59 04 D9               Y..
0020: E1 07 01 05 80 1F 00 06  80 07 80 08 80 1F 01 6F  ...............o
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x001D [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293785/0x0107E1D9) main speed = 13* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=-130.184*, Z=293.983*, Y=-19.485*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0030 [0x00] END_REQSTACK()
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
0030:    59 04 D9 E1 07 01 09  80 1F 00 0A 80 0B 80 08   Y..............
0040: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0031 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293785/0x0107E1D9) main speed = 40* * 0.1
  1: 0x0039 [0x1F] MOVE_ENTITY: EventEntity moves to X=-122.684*, Z=298.483*, Y=-19.485*
  2: 0x0041 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0043 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0044 [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                C0 00 80  00                            ....       
```

#### Opcodes

```
  0: 0x0045 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0048 [0x00] END_REQSTACK()
```
