# 17343166 - Cousseraux

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 140 bytes                          |
| Total Events     | 10                                 |
| References Count | 4                                  |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [2](#event-2)            | 0x0002       |      1 |              1 |
| [14](#event-14)          | 0x0003       |      1 |              1 |
| [15](#event-15)          | 0x0004       |      1 |              1 |
| [3](#event-3)            | 0x0005       |      1 |              1 |
| [65535.1](#event-655351) | 0x0006       |     10 |              2 |
| [65535.2](#event-655352) | 0x0010       |     10 |              2 |
| [65535.3](#event-655353) | 0x001A       |     11 |              4 |
| [65535.4](#event-655354) | 0x0025       |     31 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0064      |         100 |

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

### Event 1

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

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                00                                      .          
```

#### Opcodes

```
  0: 0x0005 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   6C BE  A2 08 01 00 80 01 80 00        l.........
```

#### Opcodes

```
  0: 0x0006 [0x6C] FADE_ENTITY_COLOR(entity_id=Cousseraux (ID: 17343166/0x0108A2BE), end_alpha=0*, fade_time=1*)
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 6C BE A2 08 01 02 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=Cousseraux (ID: 17343166/0x0108A2BE), end_alpha=128*, fade_time=1*)
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                B6 0F 03 80 80 BE            ......
0020: A2 08 01 00 00                                    .....           
```

#### Opcodes

```
  0: 0x001A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=100*)
  1: 0x001E [0x80] LOAD_WAIT(entity=Cousseraux (ID: 17343166/0x0108A2BE))
  2: 0x0023 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0024 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 31 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                7E 06 F8  FF FF 7F 01 80 00 80 01       ~..........
0030: 80 01 80 01 80 01 80 7E  04 F8 FF FF 7F 80 F8 FF  .......~........
0040: FF 7F 00 00                                       ....            
```

#### Opcodes

```
  0: 0x0025 [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on EventEntity
  1: 0x0037 [0x7E] CHOCOBO_MOUNT: Mode 4 on EventEntity
  2: 0x003D [0x80] LOAD_WAIT(entity=EventEntity)
  3: 0x0042 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0043 [0x00] END_REQSTACK()
```
