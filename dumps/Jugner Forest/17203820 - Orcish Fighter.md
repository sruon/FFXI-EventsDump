# 17203820 - Orcish Fighter

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Jugner Forest (ID: 104) |
| Block Size       | 212 bytes               |
| Total Events     | 6                       |
| References Count | 14                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [14](#event-14)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     10 |              2 |
| [65535.2](#event-655352) | 0x0015       |     27 |              5 |
| [65535.3](#event-655353) | 0x0030       |     55 |              8 |
| [65535.4](#event-655354) | 0x0067       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF8BA43  |  4294490691 |
|       1 | 0x4C3DC     |      312284 |
|       2 | 0x1FF7      |        8183 |
|       3 | 0x0B9C      |        2972 |
|       4 | 0xFFF8B912  |  4294490386 |
|       5 | 0x4BA20     |      309792 |
|       6 | 0x2074      |        8308 |
|       7 | 0x0AC5      |        2757 |
|       8 | 0x000D      |          13 |
|       9 | 0x0078      |         120 |
|      10 | 0x0028      |          40 |
|      11 | 0x000A      |          10 |
|      12 | 0x003C      |          60 |
|      13 | 0x0000      |           0 |

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

### Event 14

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-476.605*, z=312.284*, y=8.183*, direction=261.2°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   37 04 80 05 80             7....
0010: 06 80 07 80 00                                    .....           
```

#### Opcodes

```
  0: 0x000B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-476.910*, z=309.792*, y=8.308*, direction=242.3°*
  1: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 08 80  3B 68 82 06 01 00 00 01       2..;h......
0020: 00 02 00 31 00 00 00 01  00 02 00 09 80 31 01 00  ...1.........1..
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0018 [0x3B] GET_ENTITY_POSITION(entity=Ailbeche (ID: 17203816/0x01068268), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  2: 0x0023 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2], Time=120*
  3: 0x002D [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  4: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 55 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 2C F8 FF FF 7F 68 82 06  01 61 74 69 31 1C 0A 80  ,....h...ati1...
0040: 2C F8 FF FF 7F F8 FF FF  7F 64 61 6D 67 1C 0B 80  ,........damg...
0050: 2C F8 FF FF 7F F8 FF FF  7F 64 65 61 64 1C 0C 80  ,........dead...
0060: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0030 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ati1" with entities [EventEntity, Ailbeche (ID: 17203816/0x01068268)]
  1: 0x003D [0x1C] WAIT(40* ticks)
  2: 0x0040 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "damg" with entities [EventEntity, EventEntity]
  3: 0x004D [0x1C] WAIT(10* ticks)
  4: 0x0050 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [EventEntity, EventEntity]
  5: 0x005D [0x1C] WAIT(60* ticks)
  6: 0x0060 [0x92] EventEntity->Render.Flags3 ^= 0x01
  7: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      6C  F8 FF FF 7F 0D 80 0C 80         l........
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0067 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x0070 [0x00] END_REQSTACK()
```
