# 17363387 - Peculiar Fissure

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 80 bytes                   |
| Total Events     | 4                          |
| References Count | 2                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [126](#event-126)        | 0x0001       |      1 |              1 |
| [128](#event-128)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     35 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00F0      |         240 |
|       1 | 0x0000      |           0 |

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

### Event 126

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

### Event 128

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 35 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          9F 00 80 BC F1  08 01 BC F1 08 01 6B 69     ...........ki
0010: 65 30 01 80 9F 00 80 BD  F1 08 01 BD F1 08 01 6B  e0.............k
0020: 69 65 30 01 80 00                                 ie0...          
```

#### Opcodes

```
  0: 0x0003 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "kie0" with entities [Sirius (ID: 17363388/0x0108F1BC), Sirius (ID: 17363388/0x0108F1BC)], work=[240*, 0*]
  1: 0x0014 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "kie0" with entities [Almid (ID: 17363389/0x0108F1BD), Almid (ID: 17363389/0x0108F1BD)], work=[240*, 0*]
  2: 0x0025 [0x00] END_REQSTACK()
```
