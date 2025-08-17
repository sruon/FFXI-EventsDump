# 17739928 - Iruki-Waraki

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Bastok Markets (ID: 235) |
| Block Size       | 116 bytes                |
| Total Events     | 5                        |
| References Count | 9                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [439](#event-439)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     19 |              5 |
| [65535.3](#event-655353) | 0x001F       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE3966  |  4294850918 |
|       1 | 0xFFFFF375  |  4294964085 |
|       2 | 0x0000      |           0 |
|       3 | 0x0BF5      |        3061 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFE2B66  |  4294847334 |
|       6 | 0xFFFFDEE1  |  4294958817 |
|       7 | 0xFFFE29DA  |  4294846938 |
|       8 | 0xFFFFDF14  |  4294958868 |

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

### Event 439

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-116.378*, z=-3.211*, y=0.000*, direction=269.0°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 04 80 1F              2...
0010: 00 05 80 06 80 02 80 1F  01 1E 9A B0 0E 01 00     ............... 
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-119.962*, Z=-8.479*, Y=0.000*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x1E] EventEntity looks at Shamarhaan (ID: 17739930/0x010EB09A) and starts talking
  4: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1F                 .
0020: 00 07 80 08 80 02 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x001F [0x1F] MOVE_ENTITY: EventEntity moves to X=-120.358*, Z=-8.428*, Y=0.000*
  1: 0x0027 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0029 [0x00] END_REQSTACK()
```
