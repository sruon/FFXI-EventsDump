# 17494765 - Ernestine

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 148 bytes                            |
| Total Events     | 4                                    |
| References Count | 12                                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [17](#event-17)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     24 |              6 |
| [65535.2](#event-655352) | 0x0020       |     34 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x5374D     |      341837 |
|       2 | 0xFFFE08E7  |  4294838503 |
|       3 | 0xFFFF8300  |  4294935296 |
|       4 | 0x0EA5      |        3749 |
|       5 | 0x003C      |          60 |
|       6 | 0x5375F     |      341855 |
|       7 | 0xFFFE0881  |  4294838401 |
|       8 | 0x53581     |      341377 |
|       9 | 0xFFFE05DC  |  4294837724 |
|      10 | 0x534E9     |      341225 |
|      11 | 0xFFFDF8FF  |  4294834431 |

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

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 4B F8 FF  FF 7F 04 80 1C 05 80 00  .....K..........
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=341.837*, Z=-128.793*, Y=-32.000*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=20.6°*)
  4: 0x001C [0x1C] WAIT(60* ticks)
  5: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 32 00 80 1F 00 06 80 07  80 03 80 1F 01 1F 00 08  2...............
0030: 80 09 80 03 80 1F 01 1F  00 0A 80 0B 80 03 80 1F  ................
0040: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0020 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=341.855*, Z=-128.895*, Y=-32.000*
  2: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=341.377*, Z=-129.572*, Y=-32.000*
  4: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=341.225*, Z=-132.865*, Y=-32.000*
  6: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0041 [0x00] END_REQSTACK()
```
