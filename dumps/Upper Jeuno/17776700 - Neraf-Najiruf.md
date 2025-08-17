# 17776700 - Neraf-Najiruf

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 124 bytes             |
| Total Events     | 3                     |
| References Count | 11                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [207](#event-207)        | 0x0001       |     22 |              4 |
| [65535.1](#event-655351) | 0x0017       |     26 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF0F9A  |  4294905754 |
|       1 | 0x41C4      |       16836 |
|       2 | 0x03E8      |        1000 |
|       3 | 0x0463      |        1123 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFF4A9E  |  4294920862 |
|       6 | 0x6F6F      |       28527 |
|       7 | 0x0000      |           0 |
|       8 | 0x23D9      |        9177 |
|       9 | 0x11199     |       70041 |
|      10 | 0x07CF      |        1999 |

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

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 37 00 80   ............7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-61.542*, z=16.836*, y=1.000*, direction=98.7°*
  3: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  04 80 1F 00 05 80 06 80         2........
0020: 07 80 1F 01 1F 00 08 80  09 80 0A 80 1F 01 22 01  ..............".
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-46.434*, Z=28.527*, Y=0.000*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=9.177*, Z=70.041*, Y=1.999*
  4: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x002E [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x0030 [0x00] END_REQSTACK()
```
