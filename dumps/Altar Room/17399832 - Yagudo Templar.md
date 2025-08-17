# 17399832 - Yagudo Templar

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Altar Room (ID: 152) |
| Block Size       | 84 bytes             |
| Total Events     | 6                    |
| References Count | 5                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [44](#event-44)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |      1 |              1 |
| [65535.2](#event-655352) | 0x0004       |      5 |              3 |
| [65535.3](#event-655353) | 0x0009       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C74      |        7284 |
|       1 | 0x000D      |          13 |
|       2 | 0xFFFE7500  |  4294866176 |
|       3 | 0x17CDE     |       97502 |
|       4 | 0xFFFEE6C0  |  4294895296 |

## String References

- **7284**: Gawk! Orastery minister? And I am Aviatory minister! How do we know what you speak is not lies? Gawk!

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
  0: 0x0004 [0x1D] PRINT_EVENT_MESSAGE(message_id=7284*)
    → "Gawk! Orastery minister? And I am Aviatory minister! How do we know what you speak is not lies? Gawk!"
  1: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0009   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             32 01 80 1F 00 02 80           2......
0010: 03 80 04 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0009 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000C [0x1F] MOVE_ENTITY: EventEntity moves to X=-101.120*, Z=97.502*, Y=-72.000*
  2: 0x0014 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0016 [0x00] END_REQSTACK()
```
