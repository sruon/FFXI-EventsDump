# 17723439 - Doggomehr

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 180 bytes                     |
| Total Events     | 5                             |
| References Count | 15                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [535](#event-535)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     23 |              5 |
| [16](#event-16)          | 0x0019       |     28 |              5 |
| [0](#event-0)            | 0x0035       |     28 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0xFFFDCBB0  |  4294822832 |
|       2 | 0x27D79     |      163193 |
|       3 | 0x2EDF      |       11999 |
|       4 | 0x07D6      |        2006 |
|       5 | 0xFFFD7467  |  4294800487 |
|       6 | 0x27149     |      160073 |
|       7 | 0x14000     |       81920 |
|       8 | 0xFBCF      |       64463 |
|       9 | 0x00F9      |         249 |
|      10 | 0x0CFC      |        3324 |
|      11 | 0xFFFFDED4  |  4294958804 |
|      12 | 0x1CFA      |        7418 |
|      13 | 0xFFFFFF39  |  4294967097 |
|      14 | 0x0F11      |        3857 |

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

### Event 535

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
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 37 01 80  02 80 03 80 04 80 1F 00    2..7..........
0010: 05 80 06 80 03 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 20* * 0.1
  1: 0x0005 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-144.464*, z=163.193*, y=11.999*, direction=176.3°*
  2: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-166.809*, Z=160.073*, Y=11.999*
  3: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             22 00 92 01 F8 FF FF           "......
0020: 7F 37 07 80 08 80 09 80  0A 80 79 00 F8 FF FF 7F  .7........y.....
0030: 04 70 0E 01 00                                    .p...           
```

#### Opcodes

```
  0: 0x0019 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x001B [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0021 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=81.920*, z=64.463*, y=0.249*, direction=292.1°*
  3: 0x002A [0x79] EventEntity looks at Claidie (ID: 17723396/0x010E7004) (Basic look)
  4: 0x0034 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                22 00 92  01 F8 FF FF 7F 37 0B 80       ".......7..
0040: 0C 80 0D 80 0E 80 79 00  F8 FF FF 7F 02 70 0E 01  ......y......p..
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0035 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0037 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x003D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-8.492*, z=7.418*, y=-0.199*, direction=339.0°*
  3: 0x0046 [0x79] EventEntity looks at Trion (ID: 17723394/0x010E7002) (Basic look)
  4: 0x0050 [0x00] END_REQSTACK()
```
