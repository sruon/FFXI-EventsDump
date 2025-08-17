# 17404398 - Karaha-Baruha

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | The Boyahda Tree (ID: 153) |
| Block Size       | 132 bytes                  |
| Total Events     | 5                          |
| References Count | 11                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [13](#event-13)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     24 |              6 |
| [65535.3](#event-655353) | 0x0024       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFE835  |  4294961205 |
|       1 | 0xFFFFB202  |  4294947330 |
|       2 | 0xFFFFF31C  |  4294963996 |
|       3 | 0x0FDB      |        4059 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFFF439  |  4294964281 |
|       6 | 0xFFFFB2C0  |  4294947520 |
|       7 | 0xFFFFF15B  |  4294963547 |
|       8 | 0xFFFFFBF0  |  4294966256 |
|       9 | 0xFFFFA4F5  |  4294943989 |
|      10 | 0xFFFFA069  |  4294942825 |

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

### Event 13

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-6.091*, z=-19.966*, y=-3.300*, direction=356.7°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 04 80 1F              2...
0010: 00 05 80 06 80 07 80 1F  01 1F 00 08 80 09 80 07  ................
0020: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-3.015*, Z=-19.776*, Y=-3.749*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.040*, Z=-23.307*, Y=-3.749*
  4: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 04 80 1F  00 08 80 0A 80 07 80 1F      2...........
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.040*, Z=-24.471*, Y=-3.749*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x00] END_REQSTACK()
```
