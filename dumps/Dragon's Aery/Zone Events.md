# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Dragon's Aery (ID: 154) |
| Block Size       | 480 bytes               |
| Total Events     | 18                      |
| References Count | 60                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [0](#event-0)              | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535](#event-65535)      | 0x0002       |     10 |              2 |
| [65535.1](#event-655351)   | 0x000C       |     10 |              2 |
| [65535.2](#event-655352)   | 0x0016       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0020       |     10 |              2 |
| [65535.4](#event-655354)   | 0x002A       |     10 |              2 |
| [65535.5](#event-655355)   | 0x0034       |     10 |              2 |
| [65535.6](#event-655356)   | 0x003E       |     10 |              2 |
| [65535.7](#event-655357)   | 0x0048       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0052       |     10 |              2 |
| [65535.9](#event-655359)   | 0x005C       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0066       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0070       |     10 |              2 |
| [65535.12](#event-6553512) | 0x007A       |     10 |              2 |
| [65535.13](#event-6553513) | 0x0084       |     10 |              2 |
| [65535.14](#event-6553514) | 0x008E       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE6D84  |  4294864260 |
|       1 | 0x1521D     |       86557 |
|       2 | 0xFFFEE6C0  |  4294895296 |
|       3 | 0x064C      |        1612 |
|       4 | 0x9DC49     |      646217 |
|       5 | 0xFFFD6E64  |  4294798948 |
|       6 | 0x00A1      |         161 |
|       7 | 0x0C85      |        3205 |
|       8 | 0xFFFFADA3  |  4294946211 |
|       9 | 0xE9CA      |       59850 |
|      10 | 0xFFFFF799  |  4294965145 |
|      11 | 0x0D28      |        3368 |
|      12 | 0xFFFEABF4  |  4294880244 |
|      13 | 0xFFFA4EB6  |  4294594230 |
|      14 | 0x012D      |         301 |
|      15 | 0x06A4      |        1700 |
|      16 | 0xFFFDB3A7  |  4294816679 |
|      17 | 0x4EF1      |       20209 |
|      18 | 0xFFFFBFF4  |  4294950900 |
|      19 | 0x084E      |        2126 |
|      20 | 0x000A      |          10 |
|      21 | 0xFFFF6A35  |  4294928949 |
|      22 | 0x2327      |        8999 |
|      23 | 0x03ED      |        1005 |
|      24 | 0xFFFCAEE9  |  4294749929 |
|      25 | 0x70C05     |      461829 |
|      26 | 0x17BF0     |       97264 |
|      27 | 0x08E7      |        2279 |
|      28 | 0xFFFC4F0B  |  4294725387 |
|      29 | 0x51564     |      333156 |
|      30 | 0xFFFFD0E8  |  4294955240 |
|      31 | 0x0278      |         632 |
|      32 | 0xFFFA9423  |  4294612003 |
|      33 | 0xFFFE6DB2  |  4294864306 |
|      34 | 0x3C71      |       15473 |
|      35 | 0x08EC      |        2284 |
|      36 | 0x6D91F     |      448799 |
|      37 | 0xFFFF8D5B  |  4294937947 |
|      38 | 0xFFFF64E1  |  4294927585 |
|      39 | 0x0240      |         576 |
|      40 | 0xFFFFBB04  |  4294949636 |
|      41 | 0xD3E9      |       54249 |
|      42 | 0xFFFFFE47  |  4294966855 |
|      43 | 0x0AC4      |        2756 |
|      44 | 0xFFFFB53C  |  4294948156 |
|      45 | 0x4B66      |       19302 |
|      46 | 0x9EA9      |       40617 |
|      47 | 0x03A7      |         935 |
|      48 | 0x11D84     |       73092 |
|      49 | 0xFFFD607B  |  4294795387 |
|      50 | 0x0F9F      |        3999 |
|      51 | 0x0402      |        1026 |
|      52 | 0xFFFFB137  |  4294947127 |
|      53 | 0x7A43      |       31299 |
|      54 | 0xFFFFD8F2  |  4294957298 |
|      55 | 0x0D4B      |        3403 |
|      56 | 0xFFFFC860  |  4294953056 |
|      57 | 0xD01B      |       53275 |
|      58 | 0xFFFFFD7F  |  4294966655 |
|      59 | 0x0BF0      |        3056 |

## Events

### Event 0

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

### Event 65534

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

### Event 65535

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
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-103.036*, z=86.557*, y=-72.000*, direction=141.7°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      37 04 80 05              7...
0010: 80 06 80 07 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=646.217*, z=-168.348*, y=0.161*, direction=281.7°*
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   37 08  80 09 80 0A 80 0B 80 00        7.........
```

#### Opcodes

```
  0: 0x0016 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-21.085*, z=59.850*, y=-2.151*, direction=296.0°*
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 37 0C 80 0D 80 0E 80 0F  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0020 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-87.052*, z=-373.066*, y=0.301*, direction=149.4°*
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                37 10 80 11 80 12            7.....
0030: 80 13 80 00                                       ....            
```

#### Opcodes

```
  0: 0x002A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-150.617*, z=20.209*, y=-16.396*, direction=186.8°*
  1: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             37 14 80 15  80 16 80 17 80 00            7.........  
```

#### Opcodes

```
  0: 0x0034 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.010*, z=-38.347*, y=8.999*, direction=88.3°*
  1: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            37 18                7.
0040: 80 19 80 1A 80 1B 80 00                           ........        
```

#### Opcodes

```
  0: 0x003E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-217.367*, z=461.829*, y=97.264*, direction=200.3°*
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          37 1C 80 1D 80 1E 80 1F          7.......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0048 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-241.909*, z=333.156*, y=-12.056*, direction=55.5°*
  1: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       37 20 80 21 80 22  80 23 80 00                7 .!.".#..    
```

#### Opcodes

```
  0: 0x0052 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-355.293*, z=-102.990*, y=15.473*, direction=200.7°*
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      37 24 80 25              7$.%
0060: 80 26 80 27 80 00                                 .&.'..          
```

#### Opcodes

```
  0: 0x005C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=448.799*, z=-29.349*, y=-39.711*, direction=50.6°*
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   37 28  80 29 80 2A 80 2B 80 00        7(.).*.+..
```

#### Opcodes

```
  0: 0x0066 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-17.660*, z=54.249*, y=-0.441*, direction=242.2°*
  1: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0070   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 37 2C 80 2D 80 2E 80 2F  80 00                    7,.-.../..      
```

#### Opcodes

```
  0: 0x0070 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-19.140*, z=19.302*, y=40.617*, direction=82.2°*
  1: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                37 30 80 31 80 32            70.1.2
0080: 80 33 80 00                                       .3..            
```

#### Opcodes

```
  0: 0x007A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=73.092*, z=-171.909*, y=3.999*, direction=90.2°*
  1: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             37 34 80 35  80 36 80 37 80 00            74.5.6.7..  
```

#### Opcodes

```
  0: 0x0084 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-20.169*, z=31.299*, y=-9.998*, direction=299.1°*
  1: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            37 38                78
0090: 80 39 80 3A 80 3B 80 00                           .9.:.;..        
```

#### Opcodes

```
  0: 0x008E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-14.240*, z=53.275*, y=-0.641*, direction=268.6°*
  1: 0x0097 [0x00] END_REQSTACK()
```
