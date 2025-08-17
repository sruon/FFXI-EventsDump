# 17383488 - ZaDha Adamantking

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Qulun Dome (ID: 148) |
| Block Size       | 132 bytes            |
| Total Events     | 5                    |
| References Count | 11                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [63](#event-63)          | 0x0001       |     10 |              2 |
| [64](#event-64)          | 0x000B       |     10 |              2 |
| [65535.1](#event-655351) | 0x0015       |     14 |              4 |
| [65535.2](#event-655352) | 0x0023       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x3759      |       14169 |
|       1 | 0xFFFF4587  |  4294919559 |
|       2 | 0x640C      |       25612 |
|       3 | 0x0AC8      |        2760 |
|       4 | 0x000D      |          13 |
|       5 | 0x332B      |       13099 |
|       6 | 0xFFFF4600  |  4294919680 |
|       7 | 0x6409      |       25609 |
|       8 | 0x4CCB      |       19659 |
|       9 | 0xFFFF49F3  |  4294920691 |
|      10 | 0x6470      |       25712 |

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

### Event 63

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=14.169*, z=-47.737*, y=25.612*, direction=242.6°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   37 00 80 01 80             7....
0010: 02 80 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x000B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=14.169*, z=-47.737*, y=25.612*, direction=242.6°*
  1: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 04 80  1F 00 05 80 06 80 07 80       2..........
0020: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=13.099*, Z=-47.616*, Y=25.609*
  2: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          32 04 80 1F 00  08 80 09 80 0A 80 1F 01     2............
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0023 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.659*, Z=-46.605*, Y=25.712*
  2: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0030 [0x00] END_REQSTACK()
```
