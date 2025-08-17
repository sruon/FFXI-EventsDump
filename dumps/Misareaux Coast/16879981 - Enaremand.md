# 16879981 - Enaremand

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Misareaux Coast (ID: 25) |
| Block Size       | 228 bytes                |
| Total Events     | 11                       |
| References Count | 15                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [556](#event-556)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     22 |              4 |
| [557](#event-557)        | 0x0018       |      1 |              1 |
| [65535.2](#event-655352) | 0x0019       |     22 |              4 |
| [65535.3](#event-655353) | 0x002F       |     10 |              2 |
| [65535.4](#event-655354) | 0x0039       |     10 |              2 |
| [558](#event-558)        | 0x0043       |      1 |              1 |
| [65535.5](#event-655355) | 0x0044       |     10 |              2 |
| [65535.6](#event-655356) | 0x004E       |     14 |              4 |
| [65535.7](#event-655357) | 0x005C       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDAF80  |  4294815616 |
|       1 | 0x9DCEB     |      646379 |
|       2 | 0xFFFFC334  |  4294951732 |
|       3 | 0x072D      |        1837 |
|       4 | 0xFFFDAFFA  |  4294815738 |
|       5 | 0x9DFC9     |      647113 |
|       6 | 0xFFFFC33A  |  4294951738 |
|       7 | 0x0BD2      |        3026 |
|       8 | 0x000D      |          13 |
|       9 | 0xFFFDAA79  |  4294814329 |
|      10 | 0x9DDD1     |      646609 |
|      11 | 0xFFFFC315  |  4294951701 |
|      12 | 0xFFFDE0DF  |  4294828255 |
|      13 | 0x9BC18     |      637976 |
|      14 | 0xFFFFC2FB  |  4294951675 |

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

### Event 556

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
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 2F 00 6D 91 01    7......../.m..
0010: 01 4E 00 6D 91 01 01 00                           .N.m....        
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-151.680*, z=646.379*, y=-15.564*, direction=161.5°*
  1: 0x000B [0x2F] Enaremand (ID: 16879981/0x0101916D)->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0011 [0x4E] SET_ENTITY_HIDE_FLAG: Show Enaremand (ID: 16879981/0x0101916D)
  3: 0x0017 [0x00] END_REQSTACK()
```

### Event 557

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          00                               .       
```

#### Opcodes

```
  0: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             2F 00 6D 91 01 01 4E           /.m...N
0020: 00 6D 91 01 01 37 00 80  01 80 02 80 03 80 00     .m...7......... 
```

#### Opcodes

```
  0: 0x0019 [0x2F] Enaremand (ID: 16879981/0x0101916D)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x001F [0x4E] SET_ENTITY_HIDE_FLAG: Show Enaremand (ID: 16879981/0x0101916D)
  2: 0x0025 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-151.680*, z=646.379*, y=-15.564*, direction=161.5°*
  3: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               37                 7
0030: 04 80 05 80 06 80 07 80  00                       .........       
```

#### Opcodes

```
  0: 0x002F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-151.558*, z=647.113*, y=-15.558*, direction=265.9°*
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             37 00 80 01 80 02 80           7......
0040: 03 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0039 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-151.680*, z=646.379*, y=-15.564*, direction=161.5°*
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 558

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          00                                          .            
```

#### Opcodes

```
  0: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             37 00 80 01  80 02 80 03 80 00            7.........  
```

#### Opcodes

```
  0: 0x0044 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-151.680*, z=646.379*, y=-15.564*, direction=161.5°*
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            32 08                2.
0050: 80 1F 00 09 80 0A 80 0B  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x004E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=-152.967*, Z=646.609*, Y=-15.595*
  2: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      32 08 80 1F              2...
0060: 00 0C 80 0D 80 0E 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x005C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=-139.041*, Z=637.976*, Y=-15.621*
  2: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0069 [0x00] END_REQSTACK()
```
