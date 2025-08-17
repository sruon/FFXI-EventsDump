# 16785751 - Louverance

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Carpenters' Landing (ID: 2) |
| Block Size       | 140 bytes                   |
| Total Events     | 4                           |
| References Count | 8                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |     45 |              8 |
| [65535.1](#event-655351) | 0x002E       |     15 |              3 |
| [65535.2](#event-655352) | 0x003D       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0xFFFE1F0F  |  4294844175 |
|       2 | 0xFFF8C989  |  4294494601 |
|       3 | 0xFFFFE934  |  4294961460 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFDFEC9  |  4294835913 |
|       6 | 0xFFF8AFEE  |  4294488046 |
|       7 | 0xFFFFEA00  |  4294961664 |

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

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 45 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 80 F8 FF   ...............
0010: FF 7F 7E 01 F8 FF FF 7F  7E 02 F8 FF FF 7F 37 00  ..~.....~.....7.
0020: 80 00 80 00 80 00 80 4E  00 57 21 00 01 00        .......N.W!...  
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x80] LOAD_WAIT(entity=EventEntity)
  3: 0x0012 [0x7E] CHOCOBO_MOUNT: Mount chocobo on EventEntity (status = 5)
  4: 0x0018 [0x7E] CHOCOBO_MOUNT: Execute attachment function on EventEntity
  5: 0x001E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=0.000*, y=0.000*, direction=0.0°*
  6: 0x0027 [0x4E] SET_ENTITY_HIDE_FLAG: Show Louverance (ID: 16785751/0x01002157)
  7: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            37 01                7.
0030: 80 02 80 03 80 00 80 80  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x002E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-123.121*, z=-472.695*, y=-5.836*, direction=0.0°*
  1: 0x0037 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         32 04 80               2..
0040: 1F 00 05 80 06 80 07 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x003D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=-131.383*, Z=-479.250*, Y=-5.632*
  2: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004A [0x00] END_REQSTACK()
```
