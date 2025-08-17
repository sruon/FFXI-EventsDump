# 17727648 - Lilisette

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 212 bytes                 |
| Total Events     | 6                         |
| References Count | 19                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [793](#event-793)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     49 |             11 |
| [65535.2](#event-655352) | 0x0033       |     24 |              6 |
| [65535.3](#event-655353) | 0x004B       |     10 |              2 |
| [65535.4](#event-655354) | 0x0055       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0023      |          35 |
|       1 | 0xFFFF0EF6  |  4294905590 |
|       2 | 0xFFFF73C2  |  4294931394 |
|       3 | 0xFFFFEE70  |  4294962800 |
|       4 | 0xFFFF0B8B  |  4294904715 |
|       5 | 0xFFFF760A  |  4294931978 |
|       6 | 0xFFFEFDB3  |  4294901171 |
|       7 | 0xFFFF8078  |  4294934648 |
|       8 | 0xFFFFEA88  |  4294961800 |
|       9 | 0xFFFEF919  |  4294899993 |
|      10 | 0xFFFF8403  |  4294935555 |
|      11 | 0xFFFF1525  |  4294907173 |
|      12 | 0xFFFF7322  |  4294931234 |
|      13 | 0xFFFF40E7  |  4294918375 |
|      14 | 0xFFFF6B89  |  4294929289 |
|      15 | 0xFFFFF060  |  4294963296 |
|      16 | 0x0000      |           0 |
|      17 | 0x0001      |           1 |
|      18 | 0x0080      |         128 |

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

### Event 793

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
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 05 80 03 80 1F  01 1F 00 06 80 07 80 08  ................
0020: 80 1F 01 1F 00 09 80 0A  80 08 80 1F 01 1E A1 80  ................
0030: 0E 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 35* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.706*, Z=-35.902*, Y=-4.496*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-62.581*, Z=-35.318*, Y=-4.496*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=-66.125*, Z=-32.648*, Y=-5.496*
  6: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=-67.303*, Z=-31.741*, Y=-5.496*
  8: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x002D [0x1E] EventEntity looks at Thierride (ID: 17727649/0x010E80A1) and starts talking
 10: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 00 80 1F 00  0B 80 0C 80 03 80 1F 01     2............
0040: 1F 00 0D 80 0E 80 0F 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 35* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.123*, Z=-36.062*, Y=-4.496*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=-48.921*, Z=-38.007*, Y=-4.000*
  4: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   6C A0 80 0E 01             l....
0050: 10 80 11 80 00                                    .....           
```

#### Opcodes

```
  0: 0x004B [0x6C] FADE_ENTITY_COLOR(entity_id=Lilisette (ID: 17727648/0x010E80A0), end_alpha=0*, fade_time=1*)
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                6C A0 80  0E 01 12 80 11 80 00          l......... 
```

#### Opcodes

```
  0: 0x0055 [0x6C] FADE_ENTITY_COLOR(entity_id=Lilisette (ID: 17727648/0x010E80A0), end_alpha=128*, fade_time=1*)
  1: 0x005E [0x00] END_REQSTACK()
```
