# 17666764 - Elmemague

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Vunkerl (ID: 217) |
| Block Size       | 128 bytes                   |
| Total Events     | 4                           |
| References Count | 8                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1046](#event-1046)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     33 |              5 |
| [65535.2](#event-655352) | 0x0023       |     29 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFB3207  |  4294652423 |
|       1 | 0xA4FD5     |      675797 |
|       2 | 0xFFFF632E  |  4294927150 |
|       3 | 0x0800      |        2048 |
|       4 | 0xFFFB0944  |  4294641988 |
|       5 | 0xA4B0C     |      674572 |
|       6 | 0xFFFF6471  |  4294927473 |
|       7 | 0x0078      |         120 |

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

### Event 1046

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
| Data Size    | 33 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 2C F8 FF FF 7F    7........,....
0010: F8 FF FF 7F 64 65 72 75  1F 00 04 80 05 80 06 80  ....deru........
0020: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-314.873*, z=675.797*, y=-40.146*, direction=180.0°*
  1: 0x000B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "deru" with entities [EventEntity, EventEntity]
  2: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=-325.308*, Z=674.572*, Y=-39.823*
  3: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1F 00 00 80 01  80 02 80 1F 01 2C F8 FF     ..........,..
0030: FF 7F F8 FF FF 7F 6B 65  73 75 1C 07 80 22 01 00  ......kesu..."..
```

#### Opcodes

```
  0: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=-314.873*, Z=675.797*, Y=-40.146*
  1: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x002D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "kesu" with entities [EventEntity, EventEntity]
  3: 0x003A [0x1C] WAIT(120* ticks)
  4: 0x003D [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  5: 0x003F [0x00] END_REQSTACK()
```
