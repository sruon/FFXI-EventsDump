# 17473740 - Ace of Batons

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 208 bytes                    |
| Total Events     | 10                           |
| References Count | 6                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      6 |              2 |
| [65535.2](#event-655352) | 0x0007       |     16 |              2 |
| [65535.3](#event-655353) | 0x0017       |     14 |              2 |
| [65535.4](#event-655354) | 0x0025       |     34 |              4 |
| [65535.5](#event-655355) | 0x0047       |     29 |              3 |
| [65535.6](#event-655356) | 0x0064       |     16 |              2 |
| [62](#event-62)          | 0x0074       |      1 |              1 |
| [65535.7](#event-655357) | 0x0075       |     10 |              2 |
| [32000](#event-32000)    | 0x007F       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00B5      |         181 |
|       1 | 0x00B6      |         182 |
|       2 | 0xFFFF0112  |  4294902034 |
|       3 | 0xC65A      |       50778 |
|       4 | 0x2605      |        9733 |
|       5 | 0x0D6F      |        3439 |

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

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5E 69 64 6C 30 00                               ^idl0.         
```

#### Opcodes

```
  0: 0x0001 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0010: FF 7F 64 65 64 30 00                              ..ded0.         
```

#### Opcodes

```
  0: 0x0007 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ded0" with entities [EventEntity, EventEntity], work=181*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0020: 64 65 64 30 00                                    ded0.           
```

#### Opcodes

```
  0: 0x0017 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ded0" with entities [EventEntity, EventEntity]
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                5B 01 80  F8 FF FF 7F F8 FF FF 7F       [..........
0030: 61 77 6B 30 53 F8 FF FF  7F F8 FF FF 7F 61 77 6B  awk0S........awk
0040: 30 1E A8 A0 0A 01 00                              0......         
```

#### Opcodes

```
  0: 0x0025 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "awk0" with entities [EventEntity, EventEntity], work=182*
  1: 0x0034 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "awk0" with entities [EventEntity, EventEntity]
  2: 0x0041 [0x1E] EventEntity looks at Unnamed NPC (ID: 17473704/0x010AA0A8) and starts talking
  3: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      5B  01 80 F8 FF FF 7F F8 FF         [........
0050: FF 7F 64 77 6E 30 53 F8  FF FF 7F F8 FF FF 7F 64  ..dwn0S........d
0060: 77 6E 30 00                                       wn0.            
```

#### Opcodes

```
  0: 0x0047 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dwn0" with entities [EventEntity, EventEntity], work=182*
  1: 0x0056 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dwn0" with entities [EventEntity, EventEntity]
  2: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             5B 01 80 F8  FF FF 7F F8 FF FF 7F 73      [..........s
0070: 63 6B 30 00                                       ck0.            
```

#### Opcodes

```
  0: 0x0064 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sck0" with entities [EventEntity, EventEntity], work=182*
  1: 0x0073 [0x00] END_REQSTACK()
```

### Event 62

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0074  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             00                                        .           
```

#### Opcodes

```
  0: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                37 02 80  03 80 04 80 05 80 00          7......... 
```

#### Opcodes

```
  0: 0x0075 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-65.262*, z=50.778*, y=9.733*, direction=302.2°*
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               00                 .
```

#### Opcodes

```
  0: 0x007F [0x00] END_REQSTACK()
```
