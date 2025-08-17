# 17339132 - Rivetpounder Mekglok

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 152 bytes               |
| Total Events     | 6                       |
| References Count | 12                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [7](#event-7)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     10 |              2 |
| [65535.3](#event-655353) | 0x0016       |     19 |              5 |
| [65535.4](#event-655354) | 0x0029       |     21 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0028      |          40 |
|       4 | 0x2C1F1     |      180721 |
|       5 | 0xFFFC50DE  |  4294725854 |
|       6 | 0x00F4      |         244 |
|       7 | 0x2AB94     |      174996 |
|       8 | 0xFFFCD82F  |  4294760495 |
|       9 | 0x0196      |         406 |
|      10 | 0x27BE5     |      162789 |
|      11 | 0xFFFCE910  |  4294764816 |

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

### Event 7

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
0000:       6C FC 92 08 01 00  80 01 80 00                l.........    
```

#### Opcodes

```
  0: 0x0002 [0x6C] FADE_ENTITY_COLOR(entity_id=Rivetpounder Mekglok (ID: 17339132/0x010892FC), end_alpha=0*, fade_time=1*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      6C FC 92 08              l...
0010: 01 02 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000C [0x6C] FADE_ENTITY_COLOR(entity_id=Rivetpounder Mekglok (ID: 17339132/0x010892FC), end_alpha=128*, fade_time=1*)
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   32 03  80 1F 00 04 80 05 80 06        2.........
0020: 80 1F 01 1E FB 92 08 01  00                       .........       
```

#### Opcodes

```
  0: 0x0016 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=180.721*, Z=-241.442*, Y=0.244*
  2: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0023 [0x1E] EventEntity looks at Zogbog (ID: 17339131/0x010892FB) and starts talking
  4: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1F 00 07 80 08 80 09           .......
0030: 80 1F 01 1F 00 0A 80 0B  80 00 80 1F 01 00        ..............  
```

#### Opcodes

```
  0: 0x0029 [0x1F] MOVE_ENTITY: EventEntity moves to X=174.996*, Z=-206.801*, Y=0.406*
  1: 0x0031 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=162.789*, Z=-202.480*, Y=0.000*
  3: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x003D [0x00] END_REQSTACK()
```
