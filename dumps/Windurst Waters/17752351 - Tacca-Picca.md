# 17752351 - Tacca-Picca

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 216 bytes                 |
| Total Events     | 9                         |
| References Count | 16                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [989](#event-989)        | 0x0001       |      5 |              2 |
| [1016](#event-1016)      | 0x0006       |      5 |              2 |
| [65535.1](#event-655351) | 0x000B       |      5 |              2 |
| [65535.2](#event-655352) | 0x0010       |     24 |              6 |
| [991](#event-991)        | 0x0028       |      5 |              2 |
| [65535.3](#event-655353) | 0x002D       |     19 |              3 |
| [65535.4](#event-655354) | 0x0040       |     20 |              6 |
| [65535.5](#event-655355) | 0x0054       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00AB      |         171 |
|       1 | 0x000E      |          14 |
|       2 | 0x18BE      |        6334 |
|       3 | 0x590A      |       22794 |
|       4 | 0xFFFFFC19  |  4294966297 |
|       5 | 0x00A7      |         167 |
|       6 | 0x1EF2      |        7922 |
|       7 | 0x51BC      |       20924 |
|       8 | 0xFFFFFC18  |  4294966296 |
|       9 | 0x0D5C      |        3420 |
|      10 | 0x000F      |          15 |
|      11 | 0x1111      |        4369 |
|      12 | 0x545F      |       21599 |
|      13 | 0x000A      |          10 |
|      14 | 0xFFFFF9B1  |  4294965681 |
|      15 | 0x5AA0      |       23200 |

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

### Event 989

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 00 00 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=171*)
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 1016

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   B6 00  00 80 00                       .....     
```

#### Opcodes

```
  0: 0x0006 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=171*)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   B6 00 00 80 00             .....
```

#### Opcodes

```
  0: 0x000B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=171*)
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 01 80 1F 00 02 80 03  80 04 80 1F 01 6F 4A 1F  2............oJ.
0020: E1 0E 01 19 E1 0E 01 00                           ........        
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 14* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=6.334*, Z=22.794*, Y=-0.999*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001E [0x4A] Tacca-Picca (ID: 17752351/0x010EE11F) looks at Khoto Rokkorah (ID: 17752345/0x010EE119)
  5: 0x0027 [0x00] END_REQSTACK()
```

### Event 991

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          B6 00 05 80 00                   .....   
```

#### Opcodes

```
  0: 0x0028 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=167*)
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         37 06 80               7..
0030: 07 80 08 80 09 80 4A 1F  E1 0E 01 19 E1 0E 01 00  ......J.........
```

#### Opcodes

```
  0: 0x002D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=7.922*, z=20.924*, y=-1.000*, direction=300.6°*
  1: 0x0036 [0x4A] Tacca-Picca (ID: 17752351/0x010EE11F) looks at Khoto Rokkorah (ID: 17752345/0x010EE119)
  2: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 32 0A 80 1F 00 0B 80 0C  80 08 80 1F 01 6F 1E 1E  2............o..
0050: E1 0E 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0040 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=4.369*, Z=21.599*, Y=-1.000*
  2: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004E [0x1E] EventEntity looks at Cotta-Lotta (ID: 17752350/0x010EE11E) and starts talking
  5: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             32 0D 80 1F  00 0E 80 0F 80 08 80 1F      2...........
0060: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0054 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.615*, Z=23.200*, Y=-1.000*
  2: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0061 [0x00] END_REQSTACK()
```
