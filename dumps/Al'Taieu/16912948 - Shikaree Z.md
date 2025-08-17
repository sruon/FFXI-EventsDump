# 16912948 - Shikaree Z

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al'Taieu (ID: 33) |
| Block Size       | 108 bytes         |
| Total Events     | 4                 |
| References Count | 7                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [164](#event-164)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     15 |              5 |
| [65535.2](#event-655352) | 0x0020       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFFD08  |  4294966536 |
|       1 | 0xFFF8CDDB  |  4294495707 |
|       2 | 0xFFFFD8F1  |  4294957297 |
|       3 | 0x0CC6      |        3270 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFF8EA7F  |  4294503039 |
|       6 | 0xFFFFFAB0  |  4294965936 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 164

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      37  00 80 01 80 02 80 03 80         7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.760*, z=-471.589*, y=-9.999*, direction=287.4°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 00 80  05 80 02 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.760*, Z=-464.257*, Y=-9.999*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 32 04 80 1F 00 06 80 01  80 02 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0020 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.360*, Z=-471.589*, Y=-9.999*
  2: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002E [0x00] END_REQSTACK()
```
