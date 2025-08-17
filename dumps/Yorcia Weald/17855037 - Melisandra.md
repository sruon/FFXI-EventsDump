# 17855037 - Melisandra

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 416 bytes              |
| Total Events     | 13                     |
| References Count | 37                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [102](#event-102)        | 0x0001       |      7 |              2 |
| [104](#event-104)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     19 |              5 |
| [65535.2](#event-655352) | 0x0022       |     19 |              5 |
| [107](#event-107)        | 0x0035       |      1 |              1 |
| [114](#event-114)        | 0x0036       |      1 |              1 |
| [65535.3](#event-655353) | 0x0037       |     24 |              6 |
| [131](#event-131)        | 0x004F       |      7 |              2 |
| [65535.4](#event-655354) | 0x0056       |     30 |              8 |
| [65535.5](#event-655355) | 0x0074       |     22 |              6 |
| [65535.6](#event-655356) | 0x008A       |     22 |              6 |
| [65535.7](#event-655357) | 0x00A0       |     40 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x3EFA4     |      257956 |
|       2 | 0x5DE18     |      384536 |
|       3 | 0xFFFFF63D  |  4294964797 |
|       4 | 0x3D6ED     |      251629 |
|       5 | 0x5FF11     |      392977 |
|       6 | 0xFFFFFD0C  |  4294966540 |
|       7 | 0x3E197     |      254359 |
|       8 | 0x6168F     |      398991 |
|       9 | 0x00CE      |         206 |
|      10 | 0x0089      |         137 |
|      11 | 0x001E      |          30 |
|      12 | 0x0028      |          40 |
|      13 | 0x189B6     |      100790 |
|      14 | 0xE5CE      |       58830 |
|      15 | 0xFFFFF682  |  4294964866 |
|      16 | 0x18E52     |      101970 |
|      17 | 0xEB3C      |       60220 |
|      18 | 0xFFFFF79A  |  4294965146 |
|      19 | 0x000F      |          15 |
|      20 | 0x0000      |           0 |
|      21 | 0x1CAFC     |      117500 |
|      22 | 0xEA60      |       60000 |
|      23 | 0x03E8      |        1000 |
|      24 | 0x1D812     |      120850 |
|      25 | 0xEC4A      |       60490 |
|      26 | 0x03CA      |         970 |
|      27 | 0x07FF      |        2047 |
|      28 | 0x1BCB0     |      113840 |
|      29 | 0xEC72      |       60530 |
|      30 | 0x02C6      |         710 |
|      31 | 0x1A202     |      107010 |
|      32 | 0xEEAC      |       61100 |
|      33 | 0xFFFFFD30  |  4294966576 |
|      34 | 0x19410     |      103440 |
|      35 | 0xED6C      |       60780 |
|      36 | 0xFFFFF880  |  4294965376 |

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

### Event 102

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 1E F0 FF FF  ................
0020: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=257.956*, Z=384.536*, Y=-2.499*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       32 00 80 1F 00 04  80 05 80 06 80 1F 01 1E    2.............
0030: 3A 72 10 01 00                                    :r...           
```

#### Opcodes

```
  0: 0x0022 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=251.629*, Z=392.977*, Y=-0.756*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x1E] EventEntity looks at Nashu (ID: 17855034/0x0110723A) and starts talking
  4: 0x0034 [0x00] END_REQSTACK()
```

### Event 107

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

### Event 114

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0036  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   00                                    .         
```

#### Opcodes

```
  0: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  00 80 1F 00 07 80 08 80         2........
0040: 09 80 1F 01 4B F8 FF FF  7F 0A 80 1C 0B 80 00     ....K.......... 
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=254.359*, Z=398.991*, Y=0.206*
  2: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0044 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=0.8°*)
  4: 0x004B [0x1C] WAIT(30* ticks)
  5: 0x004E [0x00] END_REQSTACK()
```

### Event 131

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               92                 .
0050: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x004F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   32 0C  80 1F 00 0D 80 0E 80 0F        2.........
0060: 80 1F 01 1F 00 10 80 11  80 12 80 1F 01 1C 13 80  ................
0070: 39 14 80 00                                       9...            
```

#### Opcodes

```
  0: 0x0056 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0059 [0x1F] MOVE_ENTITY: EventEntity moves to X=100.790*, Z=58.830*, Y=-2.430*
  2: 0x0061 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=101.970*, Z=60.220*, Y=-2.150*
  4: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x006D [0x1C] WAIT(15* ticks)
  6: 0x0070 [0x39] SET_ENTITY_DIRECTION(direction=0.0°*)
  7: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             32 0B 80 1F  00 15 80 16 80 17 80 1F      2...........
0080: 01 1C 13 80 1E 3A 72 10  01 00                    .....:r...      
```

#### Opcodes

```
  0: 0x0074 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x0077 [0x1F] MOVE_ENTITY: EventEntity moves to X=117.500*, Z=60.000*, Y=1.000*
  2: 0x007F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0081 [0x1C] WAIT(15* ticks)
  4: 0x0084 [0x1E] EventEntity looks at Nashu (ID: 17855034/0x0110723A) and starts talking
  5: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                32 00 80 1F 00 18            2.....
0090: 80 19 80 1A 80 1F 01 1C  13 80 1E 3B 72 10 01 00  ...........;r...
```

#### Opcodes

```
  0: 0x008A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008D [0x1F] MOVE_ENTITY: EventEntity moves to X=120.850*, Z=60.490*, Y=0.970*
  2: 0x0095 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0097 [0x1C] WAIT(15* ticks)
  4: 0x009A [0x1E] EventEntity looks at Soraa Ishakal (ID: 17855035/0x0110723B) and starts talking
  5: 0x009F [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A0   |
| Data Size    | 40 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 39 1B 80 1C 13 80 32 00  80 1F 00 1C 80 1D 80 1E  9.....2.........
00B0: 80 1F 01 1F 00 1F 80 20  80 21 80 1F 01 1F 00 22  ....... .!....."
00C0: 80 23 80 24 80 1F 01 00                           .#.$....        
```

#### Opcodes

```
  0: 0x00A0 [0x39] SET_ENTITY_DIRECTION(direction=11.2°*)
  1: 0x00A3 [0x1C] WAIT(15* ticks)
  2: 0x00A6 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x00A9 [0x1F] MOVE_ENTITY: EventEntity moves to X=113.840*, Z=60.530*, Y=0.710*
  4: 0x00B1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00B3 [0x1F] MOVE_ENTITY: EventEntity moves to X=107.010*, Z=61.100*, Y=-0.720*
  6: 0x00BB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00BD [0x1F] MOVE_ENTITY: EventEntity moves to X=103.440*, Z=60.780*, Y=-1.920*
  8: 0x00C5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00C7 [0x00] END_REQSTACK()
```
