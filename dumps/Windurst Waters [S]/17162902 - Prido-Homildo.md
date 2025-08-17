# 17162902 - Prido-Homildo

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 108 bytes                    |
| Total Events     | 5                            |
| References Count | 7                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [182](#event-182)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     19 |              5 |
| [24](#event-24)          | 0x0015       |      1 |              1 |
| [65535.2](#event-655352) | 0x0016       |     21 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFC410  |  4294951952 |
|       1 | 0x044B      |        1099 |
|       2 | 0xFFFF9A70  |  4294941296 |
|       3 | 0x0004      |           4 |
|       4 | 0x265C      |        9820 |
|       5 | 0x2A18      |       10776 |
|       6 | 0xFFFF9977  |  4294941047 |

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

### Event 182

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
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1F 00 00 80 01 80  02 80 1F 01 6F 4B 96 E2    ..........oK..
0010: 05 01 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0002 [0x1F] MOVE_ENTITY: EventEntity moves to X=-15.344*, Z=1.099*, Y=-26.000*
  1: 0x000A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x000C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000D [0x4B] UPDATE_ENTITY_YAW(entity=Prido-Homildo (ID: 17162902/0x0105E296), yaw=0.0°*)
  4: 0x0014 [0x00] END_REQSTACK()
```

### Event 24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                00                                      .          
```

#### Opcodes

```
  0: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   1F 00  04 80 05 80 06 80 1F 01        ..........
0020: 1E 18 E2 05 01 7B 96 E2  05 01 00                 .....{.....     
```

#### Opcodes

```
  0: 0x0016 [0x1F] MOVE_ENTITY: EventEntity moves to X=9.820*, Z=10.776*, Y=-26.249*
  1: 0x001E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0020 [0x1E] EventEntity looks at Robel-Akbel (ID: 17162776/0x0105E218) and starts talking
  3: 0x0025 [0x7B] Prido-Homildo (ID: 17162902/0x0105E296) stops talking
  4: 0x002A [0x00] END_REQSTACK()
```
