# 17772730 - Luto Mewrilah

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 464 bytes                 |
| Total Events     | 11                        |
| References Count | 48                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10070](#event-10070)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     15 |              3 |
| [65535.2](#event-655352) | 0x0011       |     14 |              4 |
| [65535.3](#event-655353) | 0x001F       |     28 |              6 |
| [65535.4](#event-655354) | 0x003B       |     43 |              9 |
| [65535.5](#event-655355) | 0x0066       |     14 |              4 |
| [65535.6](#event-655356) | 0x0074       |     28 |              6 |
| [65535.7](#event-655357) | 0x0090       |     14 |              4 |
| [65535.8](#event-655358) | 0x009E       |     14 |              4 |
| [65535.9](#event-655359) | 0x00AC       |     38 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFFDDB  |  4294966747 |
|       1 | 0x423E      |       16958 |
|       2 | 0x0BB7      |        2999 |
|       3 | 0x0AF2      |        2802 |
|       4 | 0x0028      |          40 |
|       5 | 0x005F      |          95 |
|       6 | 0x11B4      |        4532 |
|       7 | 0x0274      |         628 |
|       8 | 0xFFFF942D  |  4294939693 |
|       9 | 0x2329      |        9001 |
|      10 | 0x02DE      |         734 |
|      11 | 0x2A6F      |       10863 |
|      12 | 0xFFFF3C65  |  4294917221 |
|      13 | 0x2327      |        8999 |
|      14 | 0x7AD4      |       31444 |
|      15 | 0xFFFF3421  |  4294915105 |
|      16 | 0x232B      |        9003 |
|      17 | 0x0065      |         101 |
|      18 | 0xB80A      |       47114 |
|      19 | 0xFFFF3DE2  |  4294917602 |
|      20 | 0x232A      |        9002 |
|      21 | 0xBD25      |       48421 |
|      22 | 0xFFFFAD68  |  4294946152 |
|      23 | 0x0000      |           0 |
|      24 | 0x8D9A      |       36250 |
|      25 | 0xFFFFB1EB  |  4294947307 |
|      26 | 0x0003      |           3 |
|      27 | 0x000D      |          13 |
|      28 | 0x0197      |         407 |
|      29 | 0x4376      |       17270 |
|      30 | 0x007D      |         125 |
|      31 | 0x7514      |       29972 |
|      32 | 0xFFFFEC79  |  4294962297 |
|      33 | 0x0304      |         772 |
|      34 | 0xFFFFFE0D  |  4294966797 |
|      35 | 0x6727      |       26407 |
|      36 | 0x004C      |          76 |
|      37 | 0x6176      |       24950 |
|      38 | 0x09C3      |        2499 |
|      39 | 0xFFFFFE8E  |  4294966926 |
|      40 | 0x6D22      |       27938 |
|      41 | 0xFFFFFFDC  |  4294967260 |
|      42 | 0x85B1      |       34225 |
|      43 | 0x0CA8      |        3240 |
|      44 | 0x02EC      |         748 |
|      45 | 0x919A      |       37274 |
|      46 | 0x180C      |        6156 |
|      47 | 0x9713      |       38675 |

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

### Event 10070

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
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 80 BA 30 0F 01    7..........0..
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.549*, z=16.958*, y=2.999*, direction=246.3°*
  1: 0x000B [0x80] LOAD_WAIT(entity=Luto Mewrilah (ID: 17772730/0x010F30BA))
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.095*, Z=4.532*, Y=2.999*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               37                 7
0020: 07 80 08 80 09 80 0A 80  80 BA 30 0F 01 32 04 80  ..........0..2..
0030: 1F 00 0B 80 0C 80 0D 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x001F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.628*, z=-27.603*, y=9.001*, direction=64.5°*
  1: 0x0028 [0x80] LOAD_WAIT(entity=Luto Mewrilah (ID: 17772730/0x010F30BA))
  2: 0x002D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=10.863*, Z=-50.075*, Y=8.999*
  4: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   37 0E 80 0F 80             7....
0040: 10 80 11 80 32 04 80 1F  00 12 80 13 80 14 80 1F  ....2...........
0050: 01 1F 00 15 80 16 80 17  80 1F 01 1F 00 18 80 19  ................
0060: 80 1A 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x003B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=31.444*, z=-52.191*, y=9.003*, direction=8.9°*
  1: 0x0044 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=47.114*, Z=-49.694*, Y=9.002*
  3: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=48.421*, Z=-21.144*, Y=0.000*
  5: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=36.250*, Z=-19.989*, Y=0.003*
  7: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   32 1B  80 1F 00 1C 80 1D 80 02        2.........
0070: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0066 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0069 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.407*, Z=17.270*, Y=2.999*
  2: 0x0071 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             37 1E 80 1F  80 20 80 21 80 80 F8 FF      7.... .!....
0080: FF 7F 32 1B 80 1F 00 22  80 23 80 20 80 1F 01 00  ..2....".#. ....
```

#### Opcodes

```
  0: 0x0074 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.125*, z=29.972*, y=-4.999*, direction=67.8°*
  1: 0x007D [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0082 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0085 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.499*, Z=26.407*, Y=-4.999*
  4: 0x008D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 32 1B 80 1F 00 24 80 25  80 26 80 1F 01 00        2....$.%.&....  
```

#### Opcodes

```
  0: 0x0090 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0093 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.076*, Z=24.950*, Y=2.499*
  2: 0x009B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            32 1B                2.
00A0: 80 1F 00 27 80 28 80 20  80 1F 01 00              ...'.(. ....    
```

#### Opcodes

```
  0: 0x009E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.370*, Z=27.938*, Y=-4.999*
  2: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 38 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      37 29 80 2A              7).*
00B0: 80 20 80 2B 80 80 F8 FF  FF 7F 32 1B 80 1F 00 2C  . .+......2....,
00C0: 80 2D 80 20 80 1F 01 1F  00 2E 80 2F 80 20 80 1F  .-. ......./. ..
00D0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00AC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.036*, z=34.225*, y=-4.999*, direction=284.8°*
  1: 0x00B5 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x00BA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x00BD [0x1F] MOVE_ENTITY: EventEntity moves to X=0.748*, Z=37.274*, Y=-4.999*
  4: 0x00C5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00C7 [0x1F] MOVE_ENTITY: EventEntity moves to X=6.156*, Z=38.675*, Y=-4.999*
  6: 0x00CF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00D1 [0x00] END_REQSTACK()
```
