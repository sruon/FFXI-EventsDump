# 17752352 - Rahmi Yamilahto

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 96 bytes                  |
| Total Events     | 4                         |
| References Count | 7                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [991](#event-991)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     19 |              3 |
| [65535.2](#event-655352) | 0x0015       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2178      |        8568 |
|       1 | 0x5524      |       21796 |
|       2 | 0xFFFFFC18  |  4294966296 |
|       3 | 0x0D5C      |        3420 |
|       4 | 0x000C      |          12 |
|       5 | 0xFFFFFF5D  |  4294967133 |
|       6 | 0x455B      |       17755 |

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

### Event 991

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
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 4A 20 E1 0E 01    7........J ...
0010: 19 E1 0E 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=8.568*, z=21.796*, y=-1.000*, direction=300.6°*
  1: 0x000B [0x4A] Rahmi Yamilahto (ID: 17752352/0x010EE120) looks at Khoto Rokkorah (ID: 17752345/0x010EE119)
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 04 80  1F 00 05 80 06 80 02 80       2..........
0020: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.163*, Z=17.755*, Y=-1.000*
  2: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0022 [0x00] END_REQSTACK()
```
