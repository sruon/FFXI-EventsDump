# 17776702 - Chapi Galepilai

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 140 bytes             |
| Total Events     | 3                     |
| References Count | 13                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [207](#event-207)        | 0x0001       |     22 |              4 |
| [65535.1](#event-655351) | 0x0017       |     36 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF09A3  |  4294904227 |
|       1 | 0x447A      |       17530 |
|       2 | 0x03E8      |        1000 |
|       3 | 0x0431      |        1073 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFF44A0  |  4294919328 |
|       6 | 0x7A3A      |       31290 |
|       7 | 0x0000      |           0 |
|       8 | 0xFFFF41F4  |  4294918644 |
|       9 | 0x9930      |       39216 |
|      10 | 0xFFFFFF39  |  4294967097 |
|      11 | 0xFFFF2F2C  |  4294913836 |
|      12 | 0xD19A      |       53658 |

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
  2: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-63.069*, z=17.530*, y=1.000*, direction=94.3°*
  3: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 36 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  04 80 1F 00 05 80 06 80         2........
0020: 07 80 1F 01 1F 00 08 80  09 80 0A 80 1F 01 1F 00  ................
0030: 0B 80 0C 80 07 80 1F 01  22 01 00                 ........"..     
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-47.968*, Z=31.290*, Y=0.000*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=-48.652*, Z=39.216*, Y=-0.199*
  4: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=-53.460*, Z=53.658*, Y=0.000*
  6: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0038 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  8: 0x003A [0x00] END_REQSTACK()
```
