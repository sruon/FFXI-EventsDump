# 17350957 - Sureshot Snatgat

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ghelsba Outpost (ID: 140) |
| Block Size       | 96 bytes                  |
| Total Events     | 3                         |
| References Count | 9                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      3 |              2 |
| [32000](#event-32000)    | 0x0003       |     10 |              2 |
| [65535.1](#event-655351) | 0x000D       |     19 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDCBAA  |  4294822826 |
|       1 | 0x155A9     |       87465 |
|       2 | 0xFFFFCAD1  |  4294953681 |
|       3 | 0x0612      |        1554 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFDBFE7  |  4294819815 |
|       6 | 0x148E7     |       84199 |
|       7 | 0xFFFFC79E  |  4294952862 |
|       8 | 0x060B      |        1547 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 01 00                                          "..             
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0002 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 00              7.........   
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-144.470*, z=87.465*, y=-13.615*, direction=136.6°*
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 19 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         22 00 32               ".2
0010: 04 80 1F 00 05 80 06 80  07 80 1F 01 39 08 80 00  ............9...
```

#### Opcodes

```
  0: 0x000D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-147.481*, Z=84.199*, Y=-14.434*
  3: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001C [0x39] SET_ENTITY_DIRECTION(direction=8.5°*)
  5: 0x001F [0x00] END_REQSTACK()
```
