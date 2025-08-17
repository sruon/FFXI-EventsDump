# 17719613 - Tek Lengyon

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 104 bytes                     |
| Total Events     | 7                             |
| References Count | 6                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [908](#event-908)        | 0x0001       |      1 |              1 |
| [910](#event-910)        | 0x0002       |      1 |              1 |
| [912](#event-912)        | 0x0003       |      1 |              1 |
| [914](#event-914)        | 0x0004       |      1 |              1 |
| [65535.1](#event-655351) | 0x0005       |     14 |              4 |
| [65535.2](#event-655352) | 0x0013       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFD3302  |  4294783746 |
|       2 | 0x15D4      |        5588 |
|       3 | 0xFFFFFC18  |  4294966296 |
|       4 | 0xFFFD2A49  |  4294781513 |
|       5 | 0x2039      |        8249 |

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

### Event 908

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

### Event 910

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

### Event 912

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

### Event 914

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                32 00 80  1F 00 01 80 02 80 03 80       2..........
0010: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0005 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0008 [0x1F] MOVE_ENTITY: EventEntity moves to X=-183.550*, Z=5.588*, Y=-1.000*
  2: 0x0010 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          32 00 80 1F 00  04 80 05 80 03 80 1F 01     2............
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0013 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0016 [0x1F] MOVE_ENTITY: EventEntity moves to X=-185.783*, Z=8.249*, Y=-1.000*
  2: 0x001E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0020 [0x00] END_REQSTACK()
```
