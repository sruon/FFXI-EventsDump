# 17834336 - Tuffle-Buffle

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Rala Waterways (ID: 258) |
| Block Size       | 96 bytes                 |
| Total Events     | 6                        |
| References Count | 6                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [377](#event-377)        | 0x0001       |      1 |              1 |
| [378](#event-378)        | 0x0002       |      1 |              1 |
| [379](#event-379)        | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     14 |              4 |
| [65535.2](#event-655352) | 0x0012       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x50528     |      329000 |
|       2 | 0xFFF9E968  |  4294568296 |
|       3 | 0xFFFFCF22  |  4294954786 |
|       4 | 0x001E      |          30 |
|       5 | 0x589F8     |      363000 |

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

### Event 377

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

### Event 378

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

### Event 379

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=329.000*, Z=-399.000*, Y=-12.510*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       32 04 80 1F 00 05  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0012 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x0015 [0x1F] MOVE_ENTITY: EventEntity moves to X=363.000*, Z=-399.000*, Y=-12.510*
  2: 0x001D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001F [0x00] END_REQSTACK()
```
