# 17855050 - Araustoix

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 268 bytes              |
| Total Events     | 9                      |
| References Count | 23                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [114](#event-114)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     24 |              6 |
| [125](#event-125)        | 0x001A       |      1 |              1 |
| [65535.2](#event-655352) | 0x001B       |     14 |              4 |
| [131](#event-131)        | 0x0029       |      7 |              2 |
| [65535.3](#event-655353) | 0x0030       |     30 |              8 |
| [65535.4](#event-655354) | 0x004E       |     22 |              6 |
| [65535.5](#event-655355) | 0x0064       |     22 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x3F0A7     |      258215 |
|       2 | 0x62A3D     |      404029 |
|       3 | 0x0226      |         550 |
|       4 | 0x3F0F6     |      258294 |
|       5 | 0x63F85     |      409477 |
|       6 | 0x05FC      |        1532 |
|       7 | 0xFFFD6440  |  4294796352 |
|       8 | 0x60F34     |      397108 |
|       9 | 0x00FD      |         253 |
|      10 | 0x0028      |          40 |
|      11 | 0x19CF8     |      105720 |
|      12 | 0xEDC6      |       60870 |
|      13 | 0xFFFFFBD2  |  4294966226 |
|      14 | 0x1A9C8     |      109000 |
|      15 | 0xF03C      |       61500 |
|      16 | 0xFFFFFF38  |  4294967096 |
|      17 | 0x000F      |          15 |
|      18 | 0x0000      |           0 |
|      19 | 0x1BE7C     |      114300 |
|      20 | 0xEF10      |       61200 |
|      21 | 0x03AC      |         940 |
|      22 | 0x1CAFC     |      117500 |

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

### Event 114

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
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 05 80 06 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=258.215*, Z=404.029*, Y=0.550*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=258.294*, Z=409.477*, Y=1.532*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x00] END_REQSTACK()
```

### Event 125

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                00                           .     
```

#### Opcodes

```
  0: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   32 00 80 1F 00             2....
0020: 07 80 08 80 09 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x001B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=-170.944*, Z=397.108*, Y=0.253*
  2: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0028 [0x00] END_REQSTACK()
```

### Event 131

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0029 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 32 0A 80 1F 00 0B 80 0C  80 0D 80 1F 01 1F 00 0E  2...............
0040: 80 0F 80 10 80 1F 01 1C  11 80 39 12 80 00        ..........9...  
```

#### Opcodes

```
  0: 0x0030 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=105.720*, Z=60.870*, Y=-1.070*
  2: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=109.000*, Z=61.500*, Y=-0.200*
  4: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0047 [0x1C] WAIT(15* ticks)
  6: 0x004A [0x39] SET_ENTITY_DIRECTION(direction=0.0°*)
  7: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            32 00                2.
0050: 80 1F 00 13 80 14 80 15  80 1F 01 1C 11 80 1E 3A  ...............:
0060: 72 10 01 00                                       r...            
```

#### Opcodes

```
  0: 0x004E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=114.300*, Z=61.200*, Y=0.940*
  2: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005B [0x1C] WAIT(15* ticks)
  4: 0x005E [0x1E] EventEntity looks at Nashu (ID: 17855034/0x0110723A) and starts talking
  5: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             32 00 80 1F  00 16 80 14 80 15 80 1F      2...........
0070: 01 1C 11 80 1E 3A 72 10  01 00                    .....:r...      
```

#### Opcodes

```
  0: 0x0064 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=117.500*, Z=61.200*, Y=0.940*
  2: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0071 [0x1C] WAIT(15* ticks)
  4: 0x0074 [0x1E] EventEntity looks at Nashu (ID: 17855034/0x0110723A) and starts talking
  5: 0x0079 [0x00] END_REQSTACK()
```
