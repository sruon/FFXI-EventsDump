# 16867740 - Nagmolada

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Promyvion - Vahzl (ID: 22) |
| Block Size       | 88 bytes                   |
| Total Events     | 4                          |
| References Count | 6                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [50](#event-50)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     10 |              2 |
| [65535.2](#event-655352) | 0x0012       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0xFFFF5C10  |  4294925328 |
|       2 | 0x0C35      |        3125 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFFFA5F1  |  4294944241 |
|       5 | 0x09C3      |        2499 |

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

### Event 50

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          37 00 80 01 80 00 80 02          7.......
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0008 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=-41.968*, y=0.000*, direction=274.7°*
  1: 0x0011 [0x00] END_REQSTACK()
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
0010:       32 03 80 5A 00 00  80 04 80 05 80 5A 01 00    2..Z.......Z..
```

#### Opcodes

```
  0: 0x0012 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0015 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=0.000*, Z=-23.055*, Y=2.499*
  2: 0x001D [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x001F [0x00] END_REQSTACK()
```
