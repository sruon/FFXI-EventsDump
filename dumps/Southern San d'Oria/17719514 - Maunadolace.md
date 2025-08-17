# 17719514 - Maunadolace

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 192 bytes                     |
| Total Events     | 6                             |
| References Count | 16                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [503](#event-503)        | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     25 |              7 |
| [65535.2](#event-655352) | 0x0027       |     13 |              4 |
| [65535.3](#event-655353) | 0x0034       |     19 |              3 |
| [65535.4](#event-655354) | 0x0047       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFE641C  |  4294861852 |
|       2 | 0xFFFF3953  |  4294916435 |
|       3 | 0x0000      |           0 |
|       4 | 0x0E13      |        3603 |
|       5 | 0xFFFE693D  |  4294863165 |
|       6 | 0xFFFF3E22  |  4294917666 |
|       7 | 0x03E7      |         999 |
|       8 | 0xFFFE7CE9  |  4294868201 |
|       9 | 0xFFFF50EC  |  4294922476 |
|      10 | 0x03E8      |        1000 |
|      11 | 0xFFFEBA2B  |  4294883883 |
|      12 | 0xFFFF9120  |  4294938912 |
|      13 | 0x07CF      |        1999 |
|      14 | 0x001D      |          29 |
|      15 | 0x003C      |          60 |

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
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-105.444*, z=-50.861*, y=0.000*, direction=316.7°*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            33 01                3.
0010: 5A 00 05 80 06 80 07 80  5A 01 33 00 1F 00 08 80  Z.......Z.3.....
0020: 09 80 0A 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x000E [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0010 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-104.131*, Z=-49.630*, Y=0.999*
  2: 0x0018 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x001A [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  4: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.095*, Z=-44.820*, Y=1.000*
  5: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      1F  00 0B 80 0C 80 0D 80 1F         .........
0030: 01 22 01 00                                       ."..            
```

#### Opcodes

```
  0: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-83.413*, Z=-28.384*, Y=1.999*
  1: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0031 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             66 0E 80 F8  FF FF 7F F8 FF FF 7F 74      f..........t
0040: 6C 6B 30 1C 0F 80 00                              lk0....         
```

#### Opcodes

```
  0: 0x0034 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0043 [0x1C] WAIT(60* ticks)
  2: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      66  0E 80 F8 FF FF 7F F8 FF         f........
0050: FF 7F 74 6C 6B 31 00                              ..tlk1.         
```

#### Opcodes

```
  0: 0x0047 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0056 [0x00] END_REQSTACK()
```
