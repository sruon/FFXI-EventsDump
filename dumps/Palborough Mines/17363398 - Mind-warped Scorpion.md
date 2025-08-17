# 17363398 - Mind-warped Scorpion

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 248 bytes                  |
| Total Events     | 7                          |
| References Count | 0                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [130](#event-130)        | 0x0001       |      7 |              2 |
| [131](#event-131)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     27 |              3 |
| [65535.2](#event-655352) | 0x002A       |     27 |              3 |
| [65535.3](#event-655353) | 0x0045       |     53 |              5 |
| [65535.4](#event-655354) | 0x007A       |     79 |              7 |

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

### Event 130

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 131

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               2C                 ,
0010: F8 FF FF 7F F8 FF FF 7F  73 70 30 30 53 F8 FF FF  ........sp00S...
0020: 7F F8 FF FF 7F 73 70 30  30 00                    .....sp00.      
```

#### Opcodes

```
  0: 0x000F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp00" with entities [EventEntity, EventEntity]
  1: 0x001C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp00" with entities [EventEntity, EventEntity]
  2: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                2C F8 FF FF 7F F8            ,.....
0030: FF FF 7F 63 61 73 74 53  F8 FF FF 7F F8 FF FF 7F  ...castS........
0040: 63 61 73 74 00                                    cast.           
```

#### Opcodes

```
  0: 0x002A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "cast" with entities [EventEntity, EventEntity]
  1: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "cast" with entities [EventEntity, EventEntity]
  2: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 53 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                2C F8 FF  FF 7F F8 FF FF 7F 73 70       ,........sp
0050: 32 30 53 F8 FF FF 7F F8  FF FF 7F 73 70 32 30 2C  20S........sp20,
0060: F8 FF FF 7F F8 FF FF 7F  73 70 30 30 53 F8 FF FF  ........sp00S...
0070: 7F F8 FF FF 7F 73 70 30  30 00                    .....sp00.      
```

#### Opcodes

```
  0: 0x0045 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp20" with entities [EventEntity, EventEntity]
  1: 0x0052 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp20" with entities [EventEntity, EventEntity]
  2: 0x005F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp00" with entities [EventEntity, EventEntity]
  3: 0x006C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp00" with entities [EventEntity, EventEntity]
  4: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 79 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                2C F8 FF FF 7F F8            ,.....
0080: FF FF 7F 73 70 31 30 53  F8 FF FF 7F F8 FF FF 7F  ...sp10S........
0090: 73 70 31 30 2C F8 FF FF  7F F8 FF FF 7F 73 70 30  sp10,........sp0
00A0: 30 53 F8 FF FF 7F F8 FF  FF 7F 73 70 30 30 2C F8  0S........sp00,.
00B0: FF FF 7F F8 FF FF 7F 73  70 32 30 53 F8 FF FF 7F  .......sp20S....
00C0: F8 FF FF 7F 73 70 32 30  00                       ....sp20.       
```

#### Opcodes

```
  0: 0x007A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp10" with entities [EventEntity, EventEntity]
  1: 0x0087 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp10" with entities [EventEntity, EventEntity]
  2: 0x0094 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp00" with entities [EventEntity, EventEntity]
  3: 0x00A1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp00" with entities [EventEntity, EventEntity]
  4: 0x00AE [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp20" with entities [EventEntity, EventEntity]
  5: 0x00BB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp20" with entities [EventEntity, EventEntity]
  6: 0x00C8 [0x00] END_REQSTACK()
```
