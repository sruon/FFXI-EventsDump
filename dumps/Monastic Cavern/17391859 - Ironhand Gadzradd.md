# 17391859 - Ironhand Gadzradd

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Monastic Cavern (ID: 150) |
| Block Size       | 120 bytes                 |
| Total Events     | 4                         |
| References Count | 11                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [9](#event-9)            | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     15 |              5 |
| [65535.2](#event-655352) | 0x001A       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDDA43  |  4294826563 |
|       1 | 0xFFFFA02C  |  4294942764 |
|       2 | 0xFFFFDC2E  |  4294958126 |
|       3 | 0x0741      |        1857 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFDD020  |  4294823968 |
|       6 | 0xFFFF9CAA  |  4294941866 |
|       7 | 0xFFFFDD93  |  4294958483 |
|       8 | 0xFFFDF43F  |  4294833215 |
|       9 | 0xFFFF79D7  |  4294932951 |
|      10 | 0xFFFFDE2F  |  4294958639 |

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

### Event 9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-140.733*, z=-24.532*, y=-9.170*, direction=163.2°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-143.328*, Z=-25.430*, Y=-8.813*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 04 80 1F 00 08            2.....
0020: 80 09 80 0A 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-134.081*, Z=-34.345*, Y=-8.657*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0028 [0x00] END_REQSTACK()
```
