# 17134072 - Hrichter Karst

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 120 bytes                   |
| Total Events     | 4                           |
| References Count | 10                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [34](#event-34)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     32 |              8 |
| [65535.2](#event-655352) | 0x0022       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x15C88     |       89224 |
|       2 | 0x2920      |       10528 |
|       3 | 0xFFFFB136  |  4294947126 |
|       4 | 0x160FB     |       90363 |
|       5 | 0x2C6D      |       11373 |
|       6 | 0x001E      |          30 |
|       7 | 0x000D      |          13 |
|       8 | 0x15C16     |       89110 |
|       9 | 0x21E5      |        8677 |

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

### Event 34

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
| Data Size    | 32 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 05 80 03 80 1F  01 1E F1 71 05 01 1C 06  ...........q....
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=89.224*, Z=10.528*, Y=-20.170*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=90.363*, Z=11.373*, Y=-20.170*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x1E] EventEntity looks at Prien (ID: 17134065/0x010571F1) and starts talking
  6: 0x001E [0x1C] WAIT(30* ticks)
  7: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       32 07 80 1F 00 08  80 09 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0022 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=89.110*, Z=8.677*, Y=-20.170*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x00] END_REQSTACK()
```
