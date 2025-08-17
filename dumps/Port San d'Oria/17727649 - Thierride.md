# 17727649 - Thierride

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 172 bytes                 |
| Total Events     | 7                         |
| References Count | 11                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [792](#event-792)        | 0x0001       |      1 |              1 |
| [793](#event-793)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     10 |              2 |
| [65535.2](#event-655352) | 0x000D       |     10 |              2 |
| [65535.3](#event-655353) | 0x0017       |     23 |              5 |
| [65535.4](#event-655354) | 0x002E       |     38 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0008      |           8 |
|       4 | 0xFFFEE7BF  |  4294895551 |
|       5 | 0xFFFF8785  |  4294936453 |
|       6 | 0xFFFFEA88  |  4294961800 |
|       7 | 0xFFFEF290  |  4294898320 |
|       8 | 0xFFFF8D72  |  4294937970 |
|       9 | 0xFFFEF887  |  4294899847 |
|      10 | 0xFFFF8EB8  |  4294938296 |

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

### Event 792

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

### Event 793

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          6C A1 80 0E 01  00 80 01 80 00              l.........   
```

#### Opcodes

```
  0: 0x0003 [0x6C] FADE_ENTITY_COLOR(entity_id=Thierride (ID: 17727649/0x010E80A1), end_alpha=0*, fade_time=1*)
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         6C A1 80               l..
0010: 0E 01 02 80 01 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x6C] FADE_ENTITY_COLOR(entity_id=Thierride (ID: 17727649/0x010E80A1), end_alpha=128*, fade_time=1*)
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  03 80 1F 00 04 80 05 80         2........
0020: 06 80 1F 01 4A A1 80 0E  01 A2 80 0E 01 00        ....J.........  
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 8* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-71.745*, Z=-30.843*, Y=-5.496*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x4A] Thierride (ID: 17727649/0x010E80A1) looks at ??? (ID: 17727650/0x010E80A2)
  4: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 38 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            32 03                2.
0030: 80 1F 00 07 80 08 80 06  80 1F 01 1F 00 09 80 0A  ................
0040: 80 06 80 1F 01 1E A0 80  0E 01 4A A0 80 0E 01 A1  ..........J.....
0050: 80 0E 01 00                                       ....            
```

#### Opcodes

```
  0: 0x002E [0x32] ExtData[1]->MainSpeed = 8* * 0.1
  1: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=-68.976*, Z=-29.326*, Y=-5.496*
  2: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=-67.449*, Z=-29.000*, Y=-5.496*
  4: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0045 [0x1E] EventEntity looks at Lilisette (ID: 17727648/0x010E80A0) and starts talking
  6: 0x004A [0x4A] Lilisette (ID: 17727648/0x010E80A0) looks at Thierride (ID: 17727649/0x010E80A1)
  7: 0x0053 [0x00] END_REQSTACK()
```
