# 17339107 - Alphonimile

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 108 bytes               |
| Total Events     | 6                       |
| References Count | 7                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [30](#event-30)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     10 |              2 |
| [65535.2](#event-655352) | 0x000D       |     10 |              2 |
| [65535.3](#event-655353) | 0x0017       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0006      |           6 |
|       4 | 0x8630C     |      549644 |
|       5 | 0xFFFBD5E4  |  4294694372 |
|       6 | 0xFFFFFF91  |  4294967185 |

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

### Event 1

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

### Event 30

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
0000:          6C E3 92 08 01  00 80 01 80 00              l.........   
```

#### Opcodes

```
  0: 0x0003 [0x6C] FADE_ENTITY_COLOR(entity_id=Alphonimile (ID: 17339107/0x010892E3), end_alpha=0*, fade_time=1*)
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
0000:                                         6C E3 92               l..
0010: 08 01 02 80 01 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x6C] FADE_ENTITY_COLOR(entity_id=Alphonimile (ID: 17339107/0x010892E3), end_alpha=128*, fade_time=1*)
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  03 80 1F 00 04 80 05 80         2........
0020: 06 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 6* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=549.644*, Z=-272.924*, Y=-0.111*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x00] END_REQSTACK()
```
