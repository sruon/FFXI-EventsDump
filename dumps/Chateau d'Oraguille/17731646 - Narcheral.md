# 17731646 - Narcheral

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 168 bytes                     |
| Total Events     | 6                             |
| References Count | 17                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [551](#event-551)        | 0x0001       |     10 |              2 |
| [552](#event-552)        | 0x000B       |      1 |              1 |
| [65535.1](#event-655351) | 0x000C       |     14 |              4 |
| [65535.2](#event-655352) | 0x001A       |     10 |              2 |
| [65535.3](#event-655353) | 0x0024       |     23 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF6BFA  |  4294929402 |
|       1 | 0x4807      |       18439 |
|       2 | 0xFFFFF02E  |  4294963246 |
|       3 | 0x05A8      |        1448 |
|       4 | 0x000D      |          13 |
|       5 | 0x4FD7      |       20439 |
|       6 | 0xFFFF6DEB  |  4294929899 |
|       7 | 0x733A      |       29498 |
|       8 | 0xFFFFF15B  |  4294963547 |
|       9 | 0x07B6      |        1974 |
|      10 | 0xFFFF7371  |  4294931313 |
|      11 | 0x5952      |       22866 |
|      12 | 0xFFFFF15A  |  4294963546 |
|      13 | 0x02A1      |         673 |
|      14 | 0xFFFF776D  |  4294932333 |
|      15 | 0x4C4B      |       19531 |
|      16 | 0xFFFFF131  |  4294963505 |

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

### Event 551

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-37.894*, z=18.439*, y=-4.050*, direction=127.3°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 552

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   00                         .    
```

#### Opcodes

```
  0: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 04 80 1F              2...
0010: 00 00 80 05 80 02 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-37.894*, Z=20.439*, Y=-4.050*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                37 06 80 07 80 08            7.....
0020: 80 09 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-37.397*, z=29.498*, y=-3.749*, direction=173.5°*
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 04 80 37  0A 80 0B 80 0C 80 0D 80      2..7........
0030: 1F 00 0E 80 0F 80 10 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0027 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-35.983*, z=22.866*, y=-3.750*, direction=59.1°*
  2: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=-34.963*, Z=19.531*, Y=-3.791*
  3: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x003A [0x00] END_REQSTACK()
```
