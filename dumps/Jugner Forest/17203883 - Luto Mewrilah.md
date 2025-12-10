# 17203883 - Luto Mewrilah

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Jugner Forest (ID: 104) |
| Block Size       | 360 bytes               |
| Total Events     | 12                      |
| References Count | 32                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [31](#event-31)            | 0x0001       |     16 |              3 |
| [65535.1](#event-655351)   | 0x0011       |     14 |              4 |
| [65535.2](#event-655352)   | 0x001F       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0029       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0037       |     13 |              3 |
| [65535.5](#event-655355)   | 0x0044       |     14 |              4 |
| [65535.6](#event-655356)   | 0x0052       |     23 |              5 |
| [65535.7](#event-655357)   | 0x0069       |     19 |              5 |
| [65535.8](#event-655358)   | 0x007C       |     14 |              4 |
| [65535.9](#event-655359)   | 0x008A       |     14 |              4 |
| [65535.10](#event-6553510) | 0x0098       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFD7AB7  |  4294802103 |
|       1 | 0x7201A     |      466970 |
|       2 | 0x0175      |         373 |
|       3 | 0x00DC      |         220 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFD8274  |  4294804084 |
|       6 | 0x71FE8     |      466920 |
|       7 | 0x01F7      |         503 |
|       8 | 0x006E      |         110 |
|       9 | 0xFFFD8E94  |  4294807188 |
|      10 | 0x72072     |      467058 |
|      11 | 0x01D4      |         468 |
|      12 | 0xFFFDA3E3  |  4294812643 |
|      13 | 0x7101D     |      462877 |
|      14 | 0x06A1      |        1697 |
|      15 | 0x0028      |          40 |
|      16 | 0xFFFD9C0D  |  4294810637 |
|      17 | 0x73A1C     |      473628 |
|      18 | 0x0210      |         528 |
|      19 | 0xFFFDB023  |  4294815779 |
|      20 | 0x720D7     |      467159 |
|      21 | 0x0C47      |        3143 |
|      22 | 0x007E      |         126 |
|      23 | 0xFFFDB873  |  4294817907 |
|      24 | 0x71CB2     |      466098 |
|      25 | 0x0FC3      |        4035 |
|      26 | 0xFFFD96A7  |  4294809255 |
|      27 | 0x71847     |      464967 |
|      28 | 0x03A9      |         937 |
|      29 | 0xFFFD2982  |  4294781314 |
|      30 | 0x6C38A     |      443274 |
|      31 | 0x0255      |         597 |

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

### Event 31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2F 00 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   /.....7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-165.193*, z=466.970*, y=0.373*, direction=19.3°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-163.212*, Z=466.920*, Y=0.503*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               37                 7
0020: 05 80 06 80 07 80 08 80  00                       .........       
```

#### Opcodes

```
  0: 0x001F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-163.212*, z=466.920*, y=0.503*, direction=9.7°*
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             32 04 80 1F 00 09 80           2......
0030: 0A 80 0B 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0029 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002C [0x1F] MOVE_ENTITY: EventEntity moves to X=-160.108*, Z=467.058*, Y=0.468*
  2: 0x0034 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      36  0C 80 0D 80 0E 80 1E AA         6........
0040: 82 06 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0037 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=-154.653*, pos_z=462.877*, pos_y=1.697*)
  1: 0x003E [0x1E] EventEntity looks at Palometa (ID: 17203882/0x010682AA) and starts talking
  2: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             32 0F 80 1F  00 10 80 11 80 12 80 1F      2...........
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0044 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=-156.659*, Z=473.628*, Y=0.528*
  2: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       37 13 80 14 80 15  80 16 80 32 04 80 1F 00    7........2....
0060: 17 80 18 80 19 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0052 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-151.517*, z=467.159*, y=3.143*, direction=11.1°*
  1: 0x005B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=-149.389*, Z=466.098*, Y=4.035*
  3: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             32 04 80 1F 00 1A 80           2......
0070: 1B 80 1C 80 1F 01 1E F0  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x0069 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=-158.041*, Z=464.967*, Y=0.937*
  2: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0076 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      32 04 80 1F              2...
0080: 00 10 80 11 80 12 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x007C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007F [0x1F] MOVE_ENTITY: EventEntity moves to X=-156.659*, Z=473.628*, Y=0.528*
  2: 0x0087 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                32 04 80 1F 00 00            2.....
0090: 80 01 80 02 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x008A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008D [0x1F] MOVE_ENTITY: EventEntity moves to X=-165.193*, Z=466.970*, Y=0.373*
  2: 0x0095 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          32 04 80 1F 00 1D 80 1E          2.......
00A0: 80 1F 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0098 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x009B [0x1F] MOVE_ENTITY: EventEntity moves to X=-185.982*, Z=443.274*, Y=0.597*
  2: 0x00A3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A5 [0x00] END_REQSTACK()
```
