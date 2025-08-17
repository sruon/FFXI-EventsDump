# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Toraimarai Canal (ID: 169) |
| Block Size       | 388 bytes                  |
| Total Events     | 19                         |
| References Count | 30                         |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     13 |              3 |
| [65535.2](#event-655352)   | 0x000F       |     13 |              3 |
| [49](#event-49)            | 0x001C       |     10 |              2 |
| [50](#event-50)            | 0x0026       |     10 |              2 |
| [51](#event-51)            | 0x0030       |     10 |              2 |
| [65535.3](#event-655353)   | 0x003A       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0044       |     10 |              2 |
| [65535.5](#event-655355)   | 0x004E       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0058       |     13 |              3 |
| [65535.7](#event-655357)   | 0x0065       |     14 |              4 |
| [65535.8](#event-655358)   | 0x0073       |     10 |              2 |
| [65535.9](#event-655359)   | 0x007D       |     13 |              3 |
| [65535.10](#event-6553510) | 0x008A       |     14 |              4 |
| [65535.11](#event-6553511) | 0x0098       |      6 |              2 |
| [65535.12](#event-6553512) | 0x009E       |      6 |              2 |
| [65535.13](#event-6553513) | 0x00A4       |      6 |              2 |
| [65535.14](#event-6553514) | 0x00AA       |      6 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x222E0     |      140000 |
|       1 | 0xFFFFB1E1  |  4294947297 |
|       2 | 0x32C7      |       12999 |
|       3 | 0x0FE3      |        4067 |
|       4 | 0xFFFB6F17  |  4294668055 |
|       5 | 0x3F8ED     |      260333 |
|       6 | 0x3E80      |       16000 |
|       7 | 0x0000      |           0 |
|       8 | 0xFFFDE5F3  |  4294829555 |
|       9 | 0x24547     |      148807 |
|      10 | 0x3E7F      |       15999 |
|      11 | 0x0C33      |        3123 |
|      12 | 0xFFFE88F1  |  4294871281 |
|      13 | 0xFFFF8CB2  |  4294937778 |
|      14 | 0x01CA      |         458 |
|      15 | 0x5103      |       20739 |
|      16 | 0xEE02      |       60930 |
|      17 | 0x4267      |       16999 |
|      18 | 0x056C      |        1388 |
|      19 | 0x22AB7     |      142007 |
|      20 | 0xFFFFC90E  |  4294953230 |
|      21 | 0x01A8      |         424 |
|      22 | 0x22E3D     |      142909 |
|      23 | 0xFFFFBFC8  |  4294950856 |
|      24 | 0x0400      |        1024 |
|      25 | 0x21728     |      137000 |
|      26 | 0xFFFFB1E0  |  4294947296 |
|      27 | 0x0FA0      |        4000 |
|      28 | 0x000D      |          13 |
|      29 | 0x07E8      |        2024 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       47 00 00 80 01 80  02 80 03 80 47 01 00       G.........G.. 
```

#### Opcodes

```
  0: 0x0002 [0x47] UPDATE_PLAYER_POS(140.000*, -19.999*, 12.999*, yaw=357.4°*)
  1: 0x000C [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               47                 G
0010: 00 04 80 05 80 06 80 07  80 47 01 00              .........G..    
```

#### Opcodes

```
  0: 0x000F [0x47] UPDATE_PLAYER_POS(-299.241*, 260.333*, 16.000*, yaw=0.0°*)
  1: 0x0019 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x001B [0x00] END_REQSTACK()
```

### Event 49

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      37 08 80 09              7...
0020: 80 0A 80 0B 80 00                                 ......          
```

#### Opcodes

```
  0: 0x001C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-137.741*, z=148.807*, y=15.999*, direction=274.5°*
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   37 0C  80 0D 80 0A 80 0E 80 00        7.........
```

#### Opcodes

```
  0: 0x0026 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-96.015*, z=-29.518*, y=15.999*, direction=40.3°*
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 37 0F 80 10 80 11 80 12  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0030 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=20.739*, z=60.930*, y=16.999*, direction=122.0°*
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                37 13 80 14 80 02            7.....
0040: 80 15 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=142.007*, z=-14.066*, y=12.999*, direction=37.3°*
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             37 16 80 17  80 02 80 18 80 00            7.........  
```

#### Opcodes

```
  0: 0x0044 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=142.909*, z=-16.440*, y=12.999*, direction=90.0°*
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            37 19                7.
0050: 80 1A 80 02 80 1B 80 00                           ........        
```

#### Opcodes

```
  0: 0x004E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=137.000*, z=-20.000*, y=12.999*, direction=351.6°*
  1: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          47 00 00 80 1A 80 02 80          G.......
0060: 1B 80 47 01 00                                    ..G..           
```

#### Opcodes

```
  0: 0x0058 [0x47] UPDATE_PLAYER_POS(140.000*, -20.000*, 12.999*, yaw=351.6°*)
  1: 0x0062 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                32 1C 80  1F 00 00 80 1A 80 02 80       2..........
0070: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0065 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0068 [0x1F] MOVE_ENTITY: EventEntity moves to X=140.000*, Z=-20.000*, Y=12.999*
  2: 0x0070 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          37 00 80 1A 80  02 80 1D 80 00              7.........   
```

#### Opcodes

```
  0: 0x0073 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=140.000*, z=-20.000*, y=12.999*, direction=177.9°*
  1: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         47 00 19               G..
0080: 80 1A 80 02 80 1D 80 47  01 00                    .......G..      
```

#### Opcodes

```
  0: 0x007D [0x47] UPDATE_PLAYER_POS(137.000*, -20.000*, 12.999*, yaw=177.9°*)
  1: 0x0087 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                32 1C 80 1F 00 19            2.....
0090: 80 1A 80 02 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x008A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008D [0x1F] MOVE_ENTITY: EventEntity moves to X=137.000*, Z=-20.000*, Y=12.999*
  2: 0x0095 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0098  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          03 02 10 0B 7F 00                ......  
```

#### Opcodes

```
  0: 0x0098 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009E  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            03 02                ..
00A0: 10 07 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x009E [0x03] Work_Zone[2] = Entity->Race
  1: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             03 09 10 07  7F 00                        ......      
```

#### Opcodes

```
  0: 0x00A4 [0x03] Work_Zone[9] = Entity->Race
  1: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AA  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                03 02 10 06 7F 00            ......
```

#### Opcodes

```
  0: 0x00AA [0x03] Work_Zone[2] = Entity->JobId (if LocalPlayer)
  1: 0x00AF [0x00] END_REQSTACK()
```
