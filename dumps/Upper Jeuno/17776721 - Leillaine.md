# 17776721 - Leillaine

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 216 bytes             |
| Total Events     | 7                     |
| References Count | 18                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10](#event-10)          | 0x0001       |     13 |              3 |
| [207](#event-207)        | 0x000E       |     13 |              3 |
| [65535.1](#event-655351) | 0x001B       |     24 |              6 |
| [65535.2](#event-655352) | 0x0033       |     23 |              5 |
| [65535.3](#event-655353) | 0x004A       |     25 |              4 |
| [33](#event-33)          | 0x0063       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF3D07  |  4294917383 |
|       1 | 0x0BD3      |        3027 |
|       2 | 0xFFFFFE0D  |  4294966797 |
|       3 | 0x0211      |         529 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF415E  |  4294918494 |
|       6 | 0x07C6      |        1990 |
|       7 | 0x001E      |          30 |
|       8 | 0xFFFF40F8  |  4294918392 |
|       9 | 0x16B5      |        5813 |
|      10 | 0xFFFF364B  |  4294915659 |
|      11 | 0x1B27      |        6951 |
|      12 | 0x0272      |         626 |
|      13 | 0xFFFF3EE4  |  4294917860 |
|      14 | 0xFFFFF3C0  |  4294964160 |
|      15 | 0x0F1E      |        3870 |
|      16 | 0x0000      |           0 |
|      17 | 0x0001      |           1 |

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

### Event 10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 00         .............  
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            92 01                ..
0010: F8 FF FF 7F 94 01 F8 FF  FF 7F 00                 ...........     
```

#### Opcodes

```
  0: 0x000E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0014 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   37 00 80 01 80             7....
0020: 02 80 03 80 32 04 80 1F  00 05 80 06 80 02 80 1F  ....2...........
0030: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x001B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-49.913*, z=3.027*, y=-0.499*, direction=46.5°*
  1: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-48.802*, Z=1.990*, Y=-0.499*
  3: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          1C 07 80 1F 00  08 80 09 80 02 80 1F 01     .............
0040: 37 0A 80 0B 80 02 80 0C  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0033 [0x1C] WAIT(30* ticks)
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-48.904*, Z=5.813*, Y=-0.499*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-51.637*, z=6.951*, y=-0.499*, direction=55.0°*
  4: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 25 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                37 0D 80 0E 80 02            7.....
0050: 80 0F 80 6C F8 FF FF 7F  10 80 11 80 92 01 F8 FF  ...l............
0060: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x004A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-49.436*, z=-3.136*, y=-0.499*, direction=340.1°*
  1: 0x0053 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  2: 0x005C [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x0062 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```
