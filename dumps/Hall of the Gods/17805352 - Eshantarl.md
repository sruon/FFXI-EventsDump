# 17805352 - Eshantarl

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Hall of the Gods (ID: 251) |
| Block Size       | 336 bytes                  |
| Total Events     | 16                         |
| References Count | 26                         |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [14](#event-14)            | 0x0001       |      1 |              1 |
| [17](#event-17)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     22 |              6 |
| [65535.2](#event-655352)   | 0x0019       |     14 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     14 |              4 |
| [15](#event-15)            | 0x0035       |      1 |              1 |
| [65535.4](#event-655354)   | 0x0036       |     14 |              4 |
| [65535.5](#event-655355)   | 0x0044       |     22 |              6 |
| [16](#event-16)            | 0x005A       |      1 |              1 |
| [18](#event-18)            | 0x005B       |      1 |              1 |
| [65535.6](#event-655356)   | 0x005C       |     14 |              4 |
| [65535.7](#event-655357)   | 0x006A       |     14 |              4 |
| [65535.8](#event-655358)   | 0x0078       |     24 |              6 |
| [65535.9](#event-655359)   | 0x0090       |      3 |              2 |
| [65535.10](#event-6553510) | 0x0093       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x0507      |        1287 |
|       2 | 0xFFFFF808  |  4294965256 |
|       3 | 0xFFFFCD39  |  4294954297 |
|       4 | 0x001E      |          30 |
|       5 | 0x0D0A      |        3338 |
|       6 | 0x1B78      |        7032 |
|       7 | 0x03B0      |         944 |
|       8 | 0xB2E4      |       45796 |
|       9 | 0xFFFFCFF4  |  4294954996 |
|      10 | 0x03AA      |         938 |
|      11 | 0xD818      |       55320 |
|      12 | 0xFFFFFC8F  |  4294966415 |
|      13 | 0x23A1E     |      145950 |
|      14 | 0xFFFFAF2B  |  4294946603 |
|      15 | 0x0028      |          40 |
|      16 | 0xFFFFFF4B  |  4294967115 |
|      17 | 0x1BEA4     |      114340 |
|      18 | 0xFFFFB0B6  |  4294946998 |
|      19 | 0xFFFFFFF7  |  4294967287 |
|      20 | 0x1EA64     |      125540 |
|      21 | 0xFFFFB630  |  4294948400 |
|      22 | 0xFFFFFFDB  |  4294967259 |
|      23 | 0x22EEF     |      143087 |
|      24 | 0x0061      |          97 |
|      25 | 0x1D599     |      120217 |

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

### Event 14

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

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 1E F0 FF FF 7F 1C 04 80  00                       .........       
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.287*, Z=-2.040*, Y=-12.999*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0015 [0x1C] WAIT(30* ticks)
  5: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 00 80 1F 00 05 80           2......
0020: 06 80 03 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=3.338*, Z=7.032*, Y=-12.999*
  2: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  00 80 1F 00 07 80 08 80         2........
0030: 09 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=0.944*, Z=45.796*, Y=-12.300*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0035  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                00                                      .          
```

#### Opcodes

```
  0: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   32 00  80 1F 00 0A 80 0B 80 09        2.........
0040: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0036 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0039 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.938*, Z=55.320*, Y=-12.300*
  2: 0x0041 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             32 00 80 1F  00 0C 80 0D 80 0E 80 1F      2...........
0050: 01 1E 03 B0 0F 01 1C 04  80 00                    ..........      
```

#### Opcodes

```
  0: 0x0044 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.881*, Z=145.950*, Y=-20.693*
  2: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0051 [0x1E] EventEntity looks at Yve'noile (ID: 17805315/0x010FB003) and starts talking
  4: 0x0056 [0x1C] WAIT(30* ticks)
  5: 0x0059 [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                00                           .     
```

#### Opcodes

```
  0: 0x005A [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   00                         .    
```

#### Opcodes

```
  0: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      32 0F 80 1F              2...
0060: 00 10 80 11 80 12 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x005C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.181*, Z=114.340*, Y=-20.298*
  2: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                32 0F 80 1F 00 13            2.....
0070: 80 14 80 15 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x006A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.009*, Z=125.540*, Y=-18.896*
  2: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          32 00 80 1F 00 16 80 17          2.......
0080: 80 0E 80 1F 01 1F 00 18  80 19 80 15 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x0078 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007B [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.037*, Z=143.087*, Y=-20.693*
  2: 0x0083 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0085 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.097*, Z=120.217*, Y=-18.896*
  4: 0x008D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0090  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 61 01 00                                          a..             
```

#### Opcodes

```
  0: 0x0090 [0x61] EventEntity->Render.Flags2 |= 0x00000001
  1: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0093  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          61 00 00                                    a..          
```

#### Opcodes

```
  0: 0x0093 [0x61] EventEntity->Render.Flags2 &= ~0x00000001
  1: 0x0095 [0x00] END_REQSTACK()
```
