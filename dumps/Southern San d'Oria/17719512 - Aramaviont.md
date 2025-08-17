# 17719512 - Aramaviont

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 212 bytes                     |
| Total Events     | 6                             |
| References Count | 18                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [503](#event-503)        | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     35 |              9 |
| [65535.2](#event-655352) | 0x0031       |     13 |              4 |
| [65535.3](#event-655353) | 0x003E       |     19 |              3 |
| [65535.4](#event-655354) | 0x0051       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFE579C  |  4294858652 |
|       2 | 0xFFFF3803  |  4294916099 |
|       3 | 0x0000      |           0 |
|       4 | 0x0DE0      |        3552 |
|       5 | 0xFFFE5B9A  |  4294859674 |
|       6 | 0xFFFF3F65  |  4294917989 |
|       7 | 0xFFFE616E  |  4294861166 |
|       8 | 0xFFFF462F  |  4294919727 |
|       9 | 0x03E7      |         999 |
|      10 | 0xFFFE71B3  |  4294865331 |
|      11 | 0xFFFF4EF0  |  4294921968 |
|      12 | 0x03E8      |        1000 |
|      13 | 0xFFFEACBF  |  4294880447 |
|      14 | 0xFFFF9692  |  4294940306 |
|      15 | 0x07CF      |        1999 |
|      16 | 0x001D      |          29 |
|      17 | 0x003C      |          60 |

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

### Event 503

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    32 00 80 37 01 80 02  80 03 80 04 80 00         2..7.........  
```

#### Opcodes

```
  0: 0x0001 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-108.644*, z=-51.197*, y=0.000*, direction=312.2°*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1F 00                ..
0010: 05 80 06 80 03 80 1F 01  33 01 5A 00 07 80 08 80  ........3.Z.....
0020: 09 80 5A 01 33 00 1F 00  0A 80 0B 80 0C 80 1F 01  ..Z.3...........
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-107.622*, Z=-49.307*, Y=0.000*
  1: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0018 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  3: 0x001A [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-106.130*, Z=-47.569*, Y=0.999*
  4: 0x0022 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  5: 0x0024 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  6: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-101.965*, Z=-45.328*, Y=1.000*
  7: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    1F 00 0D 80 0E 80 0F  80 1F 01 22 01 00         .........."..  
```

#### Opcodes

```
  0: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=-86.849*, Z=-26.990*, Y=1.999*
  1: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x003B [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            66 10                f.
0040: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1C 11 80  .........tlk0...
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x003E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x004D [0x1C] WAIT(60* ticks)
  2: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    66 10 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31   f..........tlk1
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0051 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0060 [0x00] END_REQSTACK()
```
