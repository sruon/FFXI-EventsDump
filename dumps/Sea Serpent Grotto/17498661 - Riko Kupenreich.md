# 17498661 - Riko Kupenreich

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Sea Serpent Grotto (ID: 176) |
| Block Size       | 232 bytes                    |
| Total Events     | 10                           |
| References Count | 10                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [20](#event-20)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     19 |              5 |
| [65535.2](#event-655352) | 0x0015       |     16 |              4 |
| [65535.3](#event-655353) | 0x0025       |     16 |              2 |
| [65535.4](#event-655354) | 0x0035       |     16 |              2 |
| [65535.5](#event-655355) | 0x0045       |     16 |              2 |
| [65535.6](#event-655356) | 0x0055       |     16 |              2 |
| [65535.7](#event-655357) | 0x0065       |     16 |              2 |
| [65535.8](#event-655358) | 0x0075       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0937      |        2359 |
|       1 | 0x1B166     |      110950 |
|       2 | 0xFFFE30EA  |  4294848746 |
|       3 | 0x01F3      |         499 |
|       4 | 0x000F      |          15 |
|       5 | 0x0A4C      |        2636 |
|       6 | 0x0A52      |        2642 |
|       7 | 0x0AC2      |        2754 |
|       8 | 0x0AC3      |        2755 |
|       9 | 0x00B4      |         180 |

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

### Event 20

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
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 B6 00 00 80  92 01 F8 FF FF 7F 94 01    ".............
0010: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2359*)
  2: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000E [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                36 01 80  02 80 03 80 80 F8 FF FF       6..........
0020: 7F 1C 04 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0015 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=110.950*, pos_z=-118.550*, pos_y=0.499*)
  1: 0x001C [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0021 [0x1C] WAIT(15* ticks)
  3: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                5B 05 80  F8 FF FF 7F F8 FF FF 7F       [..........
0030: 74 6C 6B 30 00                                    tlk0.           
```

#### Opcodes

```
  0: 0x0025 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                5B 05 80  F8 FF FF 7F F8 FF FF 7F       [..........
0040: 73 74 64 30 00                                    std0.           
```

#### Opcodes

```
  0: 0x0035 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "std0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
0050: 6E 6F 30 30 00                                    no00.           
```

#### Opcodes

```
  0: 0x0045 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "no00" with entities [EventEntity, EventEntity], work=2642*
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
0060: 79 65 73 30 00                                    yes0.           
```

#### Opcodes

```
  0: 0x0055 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes0" with entities [EventEntity, EventEntity], work=2642*
  1: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                5B 07 80  F8 FF FF 7F F8 FF FF 7F       [..........
0070: 62 69 6B 30 00                                    bik0.           
```

#### Opcodes

```
  0: 0x0065 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=2754*
  1: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                5B 08 80  F8 FF FF 7F F8 FF FF 7F       [..........
0080: 70 61 73 30 1C 09 80 00                           pas0....        
```

#### Opcodes

```
  0: 0x0075 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=2755*
  1: 0x0084 [0x1C] WAIT(180* ticks)
  2: 0x0087 [0x00] END_REQSTACK()
```
