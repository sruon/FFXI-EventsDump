# 17719529 - Leservieus

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 144 bytes                     |
| Total Events     | 6                             |
| References Count | 12                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [734](#event-734)        | 0x0002       |      1 |              1 |
| [65535.2](#event-655352) | 0x0003       |     10 |              2 |
| [65535.3](#event-655353) | 0x000D       |     25 |              7 |
| [65535.4](#event-655354) | 0x0026       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x6346      |       25414 |
|       1 | 0x1334      |        4916 |
|       2 | 0x0000      |           0 |
|       3 | 0x0010      |          16 |
|       4 | 0x000D      |          13 |
|       5 | 0x8199      |       33177 |
|       6 | 0x11BE      |        4542 |
|       7 | 0xFFFFF449  |  4294964297 |
|       8 | 0x8EDF      |       36575 |
|       9 | 0x0307      |         775 |
|      10 | 0x8E72      |       36466 |
|      11 | 0xFFFFF5B5  |  4294964661 |

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

### Event 65535.1

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

### Event 734

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 00              7.........   
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=25.414*, z=4.916*, y=0.000*, direction=1.4°*
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         32 04 80               2..
0010: 1F 00 05 80 06 80 07 80  1F 01 1F 00 08 80 09 80  ................
0020: 07 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x000D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=33.177*, Z=4.542*, Y=-2.999*
  2: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=36.575*, Z=0.775*, Y=-2.999*
  4: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   32 04  80 1F 00 0A 80 0B 80 07        2.........
0030: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0026 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0029 [0x1F] MOVE_ENTITY: EventEntity moves to X=36.466*, Z=-2.635*, Y=-2.999*
  2: 0x0031 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0033 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0034 [0x00] END_REQSTACK()
```
