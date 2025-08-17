# 16822549 - Mighty Minded Generajiq

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Oldton Movalpolos (ID: 11) |
| Block Size       | 180 bytes                  |
| Total Events     | 6                          |
| References Count | 16                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [63](#event-63)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     15 |              5 |
| [65535.2](#event-655352) | 0x001A       |     24 |              6 |
| [64](#event-64)          | 0x0032       |     10 |              2 |
| [65535.3](#event-655353) | 0x003C       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDE4F8  |  4294829304 |
|       1 | 0x2563F     |      153151 |
|       2 | 0x1F3F      |        7999 |
|       3 | 0x0B78      |        2936 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFDDDAD  |  4294827437 |
|       6 | 0x25712     |      153362 |
|       7 | 0xFFFDE3BC  |  4294828988 |
|       8 | 0x25BAC     |      154540 |
|       9 | 0xFFFDE2EC  |  4294828780 |
|      10 | 0x25EFF     |      155391 |
|      11 | 0xFFFDDD5F  |  4294827359 |
|      12 | 0x25755     |      153429 |
|      13 | 0x0BFC      |        3068 |
|      14 | 0xFFFDE252  |  4294828626 |
|      15 | 0x23910     |      145680 |

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

### Event 63

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-137.992*, z=153.151*, y=7.999*, direction=258.0°*
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
0010: 05 80 06 80 02 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-139.859*, Z=153.362*, Y=7.999*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 04 80 1F 00 07            2.....
0020: 80 08 80 02 80 1F 01 1F  00 09 80 0A 80 02 80 1F  ................
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-138.308*, Z=154.540*, Y=7.999*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-138.516*, Z=155.391*, Y=7.999*
  4: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0031 [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       37 0B 80 0C 80 02  80 0D 80 00                7.........    
```

#### Opcodes

```
  0: 0x0032 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-139.937*, z=153.429*, y=7.999*, direction=269.6°*
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      32 04 80 1F              2...
0040: 00 0E 80 0F 80 02 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x003C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=-138.670*, Z=145.680*, Y=7.999*
  2: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0049 [0x00] END_REQSTACK()
```
