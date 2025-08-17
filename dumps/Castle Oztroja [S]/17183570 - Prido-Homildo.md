# 17183570 - Prido-Homildo

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Oztroja [S] (ID: 99) |
| Block Size       | 92 bytes                    |
| Total Events     | 3                           |
| References Count | 8                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [100](#event-100)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     29 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDA985  |  4294814085 |
|       1 | 0xFFFFB159  |  4294947161 |
|       2 | 0x00E0      |         224 |
|       3 | 0x0978      |        2424 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFDEFE7  |  4294832103 |
|       6 | 0xFFFFB4EA  |  4294948074 |
|       7 | 0x0055      |          85 |

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
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-153.211*, z=-20.135*, y=0.224*, direction=213.0°*
  1: 0x000B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-135.193*, Z=-19.222*, Y=0.085*
  3: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0019 [0x1E] EventEntity looks at Ghyo Molkot (ID: 17183567/0x0106334F) and starts talking
  6: 0x001E [0x00] END_REQSTACK()
```
