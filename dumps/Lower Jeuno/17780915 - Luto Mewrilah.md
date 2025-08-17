# 17780915 - Luto Mewrilah

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 388 bytes             |
| Total Events     | 17                    |
| References Count | 37                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [10049](#event-10049)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     10 |              2 |
| [65535.2](#event-655352)   | 0x000C       |     14 |              4 |
| [65535.3](#event-655353)   | 0x001A       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0024       |     10 |              2 |
| [10050](#event-10050)      | 0x002E       |      1 |              1 |
| [65535.5](#event-655355)   | 0x002F       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0039       |     14 |              4 |
| [65535.7](#event-655357)   | 0x0047       |     23 |              5 |
| [65535.8](#event-655358)   | 0x005E       |     14 |              4 |
| [10051](#event-10051)      | 0x006C       |      1 |              1 |
| [65535.9](#event-655359)   | 0x006D       |     14 |              4 |
| [65535.10](#event-6553510) | 0x007B       |     14 |              4 |
| [65535.11](#event-6553511) | 0x0089       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0093       |      3 |              2 |
| [65535.13](#event-6553513) | 0x0096       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x4CF4      |       19700 |
|       1 | 0xFFFFE825  |  4294961189 |
|       2 | 0xFFFFFF9C  |  4294967196 |
|       3 | 0x0D69      |        3433 |
|       4 | 0x000D      |          13 |
|       5 | 0x571C      |       22300 |
|       6 | 0x0423      |        1059 |
|       7 | 0xFFFFFF91  |  4294967185 |
|       8 | 0xFFFF93D9  |  4294939609 |
|       9 | 0x1903A     |      102458 |
|      10 | 0xFFFFEB7F  |  4294962047 |
|      11 | 0x0ADB      |        2779 |
|      12 | 0x5543      |       21827 |
|      13 | 0x0CD0      |        3280 |
|      14 | 0x5B9E      |       23454 |
|      15 | 0x0AF4      |        2804 |
|      16 | 0xFFFFFF9D  |  4294967197 |
|      17 | 0x0B2F      |        2863 |
|      18 | 0x58DA      |       22746 |
|      19 | 0x1110      |        4368 |
|      20 | 0xFFFF89CA  |  4294937034 |
|      21 | 0xFFFF6251  |  4294926929 |
|      22 | 0x0000      |           0 |
|      23 | 0x0C27      |        3111 |
|      24 | 0xFFFF95CB  |  4294940107 |
|      25 | 0xFFFF7B6A  |  4294933354 |
|      26 | 0x0028      |          40 |
|      27 | 0xFFFFD896  |  4294957206 |
|      28 | 0xFFFFFC20  |  4294966304 |
|      29 | 0x4145      |       16709 |
|      30 | 0xFFFFF17D  |  4294963581 |
|      31 | 0x8BFD      |       35837 |
|      32 | 0xFFFFC44C  |  4294952012 |
|      33 | 0x4911      |       18705 |
|      34 | 0xFFFF21AD  |  4294910381 |
|      35 | 0x0F1D      |        3869 |
|      36 | 0x02B2      |         690 |

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

### Event 10049

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
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=19.700*, z=-6.107*, y=-0.100*, direction=301.7°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

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
0010: 00 05 80 06 80 07 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=22.300*, Z=1.059*, Y=-0.111*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                37 08 80 09 80 0A            7.....
0020: 80 0B 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-27.687*, z=102.458*, y=-5.249*, direction=244.2°*
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             37 0C 80 06  80 07 80 0D 80 00            7.........  
```

#### Opcodes

```
  0: 0x0024 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=21.827*, z=1.059*, y=-0.111*, direction=288.3°*
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 10050

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.5

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
0030: 0E 80 0F 80 10 80 11 80  00                       .........       
```

#### Opcodes

```
  0: 0x002F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.454*, z=2.804*, y=-0.099*, direction=251.6°*
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 04 80 1F 00 12 80           2......
0040: 13 80 10 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=22.746*, Z=4.368*, Y=-0.099*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      37  14 80 15 80 16 80 17 80         7........
0050: 32 04 80 1F 00 18 80 19  80 16 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-30.262*, z=-40.367*, y=0.000*, direction=273.4°*
  1: 0x0050 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=-27.189*, Z=-33.942*, Y=0.000*
  3: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            32 1A                2.
0060: 80 1F 00 1B 80 1C 80 16  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x005E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=-10.090*, Z=-0.992*, Y=0.000*
  2: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006B [0x00] END_REQSTACK()
```

### Event 10051

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      00                       .   
```

#### Opcodes

```
  0: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         32 04 80               2..
0070: 1F 00 1D 80 1E 80 07 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x006D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=16.709*, Z=-3.715*, Y=-0.111*
  2: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   32 04 80 1F 00             2....
0080: 1F 80 20 80 07 80 1F 01  00                       .. ......       
```

#### Opcodes

```
  0: 0x007B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007E [0x1F] MOVE_ENTITY: EventEntity moves to X=35.837*, Z=-15.284*, Y=-0.111*
  2: 0x0086 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             37 21 80 22 80 23 80           7!.".#.
0090: 24 80 00                                          $..             
```

#### Opcodes

```
  0: 0x0089 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=18.705*, z=-56.915*, y=3.869*, direction=60.6°*
  1: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0093  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          33 01 00                                    3..          
```

#### Opcodes

```
  0: 0x0093 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0096  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   33 00  00                             3..       
```

#### Opcodes

```
  0: 0x0096 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  1: 0x0098 [0x00] END_REQSTACK()
```
