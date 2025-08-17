# 17510701 - CrystalKnight

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Stellar Fulcrum (ID: 179) |
| Block Size       | 244 bytes                 |
| Total Events     | 8                         |
| References Count | 11                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [0](#event-0)            | 0x000D       |     38 |              5 |
| [6](#event-6)            | 0x0033       |     10 |              2 |
| [17](#event-17)          | 0x003D       |     10 |              2 |
| [65535.1](#event-655351) | 0x0047       |     27 |              3 |
| [65535.2](#event-655352) | 0x0062       |     27 |              3 |
| [65535.3](#event-655353) | 0x007D       |     25 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFFBF0  |  4294966256 |
|       1 | 0xE82F      |       59439 |
|       2 | 0xFFFFEC75  |  4294962293 |
|       3 | 0x0800      |        2048 |
|       4 | 0x0000      |           0 |
|       5 | 0x002B      |          43 |
|       6 | 0x0080      |         128 |
|       7 | 0x0078      |         120 |
|       8 | 0x1DEF      |        7663 |
|       9 | 0x1DF0      |        7664 |
|      10 | 0x1DF1      |        7665 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 01 F8 FF FF 7F 92 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 38 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         22 00 37               ".7
0010: 00 80 01 80 02 80 03 80  6C F8 FF FF 7F 04 80 04  ........l.......
0020: 80 62 05 80 F8 FF FF 7F  F8 FF FF 7F 00 FE FE FE  .b..............
0030: 04 80 00                                          ...             
```

#### Opcodes

```
  0: 0x000D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.040*, z=59.439*, y=-5.003*, direction=180.0°*
  2: 0x0018 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  3: 0x0021 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=[43*, 0*]
  4: 0x0032 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          37 00 80 01 80  02 80 03 80 00              7.........   
```

#### Opcodes

```
  0: 0x0033 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.040*, z=59.439*, y=-5.003*, direction=180.0°*
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         37 00 80               7..
0040: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x003D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.040*, z=59.439*, y=-5.003*, direction=180.0°*
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      62  05 80 F8 FF FF 7F F8 FF         b........
0050: FF 7F 6D 61 69 6E 04 80  6C F8 FF FF 7F 06 80 07  ..main..l.......
0060: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0047 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[43*, 0*]
  1: 0x0058 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=120*)
  2: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       62 05 80 F8 FF FF  7F F8 FF FF 7F 6D 61 69    b..........mai
0070: 6E 04 80 6C F8 FF FF 7F  04 80 07 80 00           n..l.........   
```

#### Opcodes

```
  0: 0x0062 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[43*, 0*]
  1: 0x0073 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=120*)
  2: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         2B 27 31               +'1
0080: 0B 01 08 80 23 2B 27 31  0B 01 09 80 23 2B 27 31  ....#+'1....#+'1
0090: 0B 01 0A 80 23 00                                 ....#.          
```

#### Opcodes

```
  0: 0x007D [0x2B] Eald'narche (ID: 17510695/0x010B3127) [7663*]:
    → "I plan to use her ability to unlock the "memories of the ancients" and project them into Delkfutt's Tower, thus regenerating the Chrysalis Core and opening the path to Tu'Lia."
  1: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0085 [0x2B] Eald'narche (ID: 17510695/0x010B3127) [7664*]:
    → "Once Tu'Lia has been awakened, I can continue my preparations there."
  3: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x008D [0x2B] Eald'narche (ID: 17510695/0x010B3127) [7665*]:
    → "Just as I did ten thousand years ago."
  5: 0x0094 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0095 [0x00] END_REQSTACK()
```
