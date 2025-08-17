# 17162687 - Tek Lengyon

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 124 bytes                    |
| Total Events     | 6                            |
| References Count | 9                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [171](#event-171)        | 0x0001       |      1 |              1 |
| [174](#event-174)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     14 |              4 |
| [65535.2](#event-655352) | 0x0011       |     14 |              4 |
| [65535.3](#event-655353) | 0x001F       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0019      |          25 |
|       1 | 0x2469B     |      149147 |
|       2 | 0x3CFE8     |      249832 |
|       3 | 0xFFFFE13D  |  4294959421 |
|       4 | 0x25AAF     |      154287 |
|       5 | 0x3E2A8     |      254632 |
|       6 | 0xFFFE40CD  |  4294852813 |
|       7 | 0xFFFD902A  |  4294807594 |
|       8 | 0xFFFFFC18  |  4294966296 |

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

### Event 171

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

### Event 174

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 25* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=149.147*, Z=249.832*, Y=-7.875*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 00 80 1F 00 04 80  05 80 03 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 25* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=154.287*, Z=254.632*, Y=-7.875*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 00 80 1F 00 06 80 07 80  08 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 25* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-114.483*, Z=-159.702*, Y=-1.000*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x00] END_REQSTACK()
```
