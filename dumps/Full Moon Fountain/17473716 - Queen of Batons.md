# 17473716 - Queen of Batons

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 268 bytes                    |
| Total Events     | 13                           |
| References Count | 8                            |

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
| [61](#event-61)          | 0x0074       |     16 |              3 |
| [65535.7](#event-655357) | 0x0084       |     30 |              6 |
| [62](#event-62)          | 0x00A2       |      1 |              1 |
| [32000](#event-32000)    | 0x00A3       |      1 |              1 |
| [32004](#event-32004)    | 0x00A4       |      1 |              1 |
| [32001](#event-32001)    | 0x00A5       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00B5      |         181 |
|       1 | 0x00B6      |         182 |
|       2 | 0xFFFF1BFE  |  4294908926 |
|       3 | 0x42FA      |       17146 |
|       4 | 0x27D3      |       10195 |
|       5 | 0x0C00      |        3072 |
|       6 | 0x000D      |          13 |
|       7 | 0x1F40      |        8000 |

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

### Event 61

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             92 01 F8 FF  FF 7F 37 02 80 03 80 04      ......7.....
0080: 80 05 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0074 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x007A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-58.370*, z=17.146*, y=10.195*, direction=270.0°*
  2: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 30 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             32 06 80 3B  F8 FF FF 7F 00 00 02 00      2..;........
0090: 01 00 07 02 00 07 80 1F  00 00 00 02 00 01 00 1F  ................
00A0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0084 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0087 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[1])
  2: 0x0092 [0x07] ExtData[1]->WorkLocal[2] += 8000*
  3: 0x0097 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  4: 0x009F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00A1 [0x00] END_REQSTACK()
```

### Event 62

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       00                                            .             
```

#### Opcodes

```
  0: 0x00A2 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          00                                          .            
```

#### Opcodes

```
  0: 0x00A3 [0x00] END_REQSTACK()
```

### Event 32004

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             00                                        .           
```

#### Opcodes

```
  0: 0x00A4 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                00                                      .          
```

#### Opcodes

```
  0: 0x00A5 [0x00] END_REQSTACK()
```
