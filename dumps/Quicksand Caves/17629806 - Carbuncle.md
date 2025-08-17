# 17629806 - Carbuncle

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Quicksand Caves (ID: 208) |
| Block Size       | 180 bytes                 |
| Total Events     | 10                        |
| References Count | 7                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [106](#event-106)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     16 |              2 |
| [65535.2](#event-655352) | 0x0018       |     14 |              2 |
| [65535.3](#event-655353) | 0x0026       |     16 |              2 |
| [65535.4](#event-655354) | 0x0036       |     14 |              2 |
| [65535.5](#event-655355) | 0x0044       |      5 |              2 |
| [65535.6](#event-655356) | 0x0049       |      5 |              2 |
| [107](#event-107)        | 0x004E       |      1 |              1 |
| [65535.7](#event-655357) | 0x004F       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0198      |         408 |
|       1 | 0x0034      |          52 |
|       2 | 0x03D2      |         978 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFFF15A0  |  4294907296 |
|       5 | 0x4AB50     |      306000 |
|       6 | 0xFFFFB9B0  |  4294949296 |

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

### Event 106

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          5B 00 80 F8 FF FF 7F F8          [.......
0010: FF FF 7F 70 6F 70 30 00                           ...pop0.        
```

#### Opcodes

```
  0: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pop0" with entities [EventEntity, EventEntity], work=408*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          53 F8 FF FF 7F F8 FF FF          S.......
0020: 7F 70 6F 70 30 00                                 .pop0.          
```

#### Opcodes

```
  0: 0x0018 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pop0" with entities [EventEntity, EventEntity]
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   5B 00  80 F8 FF FF 7F F8 FF FF        [.........
0030: 7F 70 6F 70 66 00                                 .popf.          
```

#### Opcodes

```
  0: 0x0026 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "popf" with entities [EventEntity, EventEntity], work=408*
  1: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   53 F8  FF FF 7F F8 FF FF 7F 70        S........p
0040: 6F 70 66 00                                       opf.            
```

#### Opcodes

```
  0: 0x0036 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "popf" with entities [EventEntity, EventEntity]
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             B6 00 01 80  00                           .....       
```

#### Opcodes

```
  0: 0x0044 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0049  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             B6 00 02 80 00                 .....  
```

#### Opcodes

```
  0: 0x0049 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=978*)
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            00                   . 
```

#### Opcodes

```
  0: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 03 80 1F 00 04 80 05 80  06 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.000*, Z=306.000*, Y=-18.000*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x00] END_REQSTACK()
```
