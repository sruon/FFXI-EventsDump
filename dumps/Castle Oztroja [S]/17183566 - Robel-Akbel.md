# 17183566 - Robel-Akbel

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Oztroja [S] (ID: 99) |
| Block Size       | 148 bytes                   |
| Total Events     | 4                           |
| References Count | 12                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [100](#event-100)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     29 |              7 |
| [65535.2](#event-655352) | 0x001F       |     35 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDC132  |  4294820146 |
|       1 | 0xFFFFB6F5  |  4294948597 |
|       2 | 0x00C5      |         197 |
|       3 | 0x0978      |        2424 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFDF199  |  4294832537 |
|       6 | 0xFFFFB93E  |  4294949182 |
|       7 | 0x0055      |          85 |
|       8 | 0x000D      |          13 |
|       9 | 0xFFFDF5AC  |  4294833580 |
|      10 | 0xFFFFB9B3  |  4294949299 |
|      11 | 0x055D      |        1373 |

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

### Event 100

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
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 32 04 80 1F 00    7........2....
0010: 05 80 06 80 07 80 1F 01  6F 1E 4F 33 06 01 00     ........o.O3... 
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-147.150*, z=-18.699*, y=0.197*, direction=213.0°*
  1: 0x000B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-134.759*, Z=-18.114*, Y=0.085*
  3: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0019 [0x1E] EventEntity looks at Ghyo Molkot (ID: 17183567/0x0106334F) and starts talking
  6: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 35 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 08 80 1F 00 09 80 0A 80  07 80 1F 01 6F 1E 4F 33  ............o.O3
0030: 06 01 5B 0B 80 4E 33 06  01 4E 33 06 01 67 75 64  ..[..N3..N3..gud
0040: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-133.716*, Z=-17.997*, Y=0.085*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002D [0x1E] EventEntity looks at Ghyo Molkot (ID: 17183567/0x0106334F) and starts talking
  5: 0x0032 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gud0" with entities [Robel-Akbel (ID: 17183566/0x0106334E), Robel-Akbel (ID: 17183566/0x0106334E)], work=1373*
  6: 0x0041 [0x00] END_REQSTACK()
```
