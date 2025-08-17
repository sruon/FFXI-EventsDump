# 17363406 - Talking Doll

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 88 bytes                   |
| Total Events     | 4                          |
| References Count | 2                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [132](#event-132)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     16 |              2 |
| [65535.2](#event-655352) | 0x0018       |     22 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FC      |         252 |
|       1 | 0x001E      |          30 |

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

### Event 132

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
0010: FF FF 7F 62 72 75 30 00                           ...bru0.        
```

#### Opcodes

```
  0: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bru0" with entities [EventEntity, EventEntity], work=252*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          53 F8 FF FF 7F F8 FF FF          S.......
0020: 7F 62 72 75 30 5E 69 64  6C 30 1C 01 80 00        .bru0^idl0....  
```

#### Opcodes

```
  0: 0x0018 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bru0" with entities [EventEntity, EventEntity]
  1: 0x0025 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x002A [0x1C] WAIT(30* ticks)
  3: 0x002D [0x00] END_REQSTACK()
```
