# 17399833 - Yagudo Templar

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Altar Room (ID: 152) |
| Block Size       | 112 bytes            |
| Total Events     | 7                    |
| References Count | 8                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [44](#event-44)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |      1 |              1 |
| [65535.2](#event-655352) | 0x0004       |      5 |              3 |
| [65535.3](#event-655353) | 0x0009       |     10 |              2 |
| [65535.4](#event-655354) | 0x0013       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C75      |        7285 |
|       1 | 0xFFFE831D  |  4294869789 |
|       2 | 0x18538     |       99640 |
|       3 | 0xFFFEE6C0  |  4294895296 |
|       4 | 0x03D7      |         983 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFE822D  |  4294869549 |
|       7 | 0x177E5     |       96229 |

## String References

- **7285**: I should cut you up and send you to Heavens Tower! Gawk! Gawk!

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

### Event 44

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

### Event 65535.1

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

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             1D 00 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0004 [0x1D] PRINT_EVENT_MESSAGE(message_id=7285*)
    → "I should cut you up and send you to Heavens Tower! Gawk! Gawk!"
  1: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0009   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             37 01 80 02 80 03 80           7......
0010: 04 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-97.507*, z=99.640*, y=-72.000*, direction=86.4°*
  1: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          32 05 80 1F 00  06 80 07 80 03 80 1F 01     2............
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0013 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0016 [0x1F] MOVE_ENTITY: EventEntity moves to X=-97.747*, Z=96.229*, Y=-72.000*
  2: 0x001E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0020 [0x00] END_REQSTACK()
```
