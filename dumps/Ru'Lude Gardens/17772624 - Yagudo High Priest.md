# 17772624 - Yagudo High Priest

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 96 bytes                  |
| Total Events     | 6                         |
| References Count | 7                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [10010](#event-10010)    | 0x0002       |      1 |              1 |
| [65535.2](#event-655352) | 0x0003       |      1 |              1 |
| [65535.3](#event-655353) | 0x0004       |     10 |              2 |
| [65535.4](#event-655354) | 0x000E       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE89D6  |  4294871510 |
|       1 | 0x154E2     |       87266 |
|       2 | 0xFFFEE6C0  |  4294895296 |
|       3 | 0x0C89      |        3209 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFE7C1A  |  4294867994 |
|       6 | 0x16AB5     |       92853 |

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

### Event 65535.1

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

### Event 10010

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

### Event 65535.2

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

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             37 00 80 01  80 02 80 03 80 00            7.........  
```

#### Opcodes

```
  0: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-95.786*, z=87.266*, y=-72.000*, direction=282.0°*
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            32 04                2.
0010: 80 1F 00 05 80 06 80 02  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x000E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0011 [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.302*, Z=92.853*, Y=-72.000*
  2: 0x0019 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001B [0x00] END_REQSTACK()
```
