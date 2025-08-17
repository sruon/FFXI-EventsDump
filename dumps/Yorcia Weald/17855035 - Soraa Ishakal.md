# 17855035 - Soraa Ishakal

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 472 bytes              |
| Total Events     | 14                     |
| References Count | 43                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [102](#event-102)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     14 |              4 |
| [65535.2](#event-655352) | 0x0016       |     17 |              5 |
| [104](#event-104)        | 0x0027       |      7 |              2 |
| [65535.3](#event-655353) | 0x002E       |     19 |              5 |
| [65535.4](#event-655354) | 0x0041       |     22 |              6 |
| [65535.5](#event-655355) | 0x0057       |     22 |              6 |
| [114](#event-114)        | 0x006D       |      1 |              1 |
| [65535.6](#event-655356) | 0x006E       |     22 |              6 |
| [131](#event-131)        | 0x0084       |      7 |              2 |
| [65535.7](#event-655357) | 0x008B       |     33 |              9 |
| [65535.8](#event-655358) | 0x00AC       |     14 |              4 |
| [65535.9](#event-655359) | 0x00BA       |     40 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x3EEB0     |      257712 |
|       2 | 0x61329     |      398121 |
|       3 | 0x01A0      |         416 |
|       4 | 0x3ED0F     |      257295 |
|       5 | 0x61814     |      399380 |
|       6 | 0x0191      |         401 |
|       7 | 0x001E      |          30 |
|       8 | 0x3EB2C     |      256812 |
|       9 | 0x5DEAD     |      384685 |
|      10 | 0xFFFFF676  |  4294964854 |
|      11 | 0x3D124     |      250148 |
|      12 | 0x605AC     |      394668 |
|      13 | 0xFFFFFDCA  |  4294966730 |
|      14 | 0x3D4AD     |      251053 |
|      15 | 0x5F72F     |      390959 |
|      16 | 0xFFFFFAD2  |  4294965970 |
|      17 | 0x3E995     |      256405 |
|      18 | 0x616FE     |      399102 |
|      19 | 0x0171      |         369 |
|      20 | 0x003C      |          60 |
|      21 | 0x0028      |          40 |
|      22 | 0x1771E     |       96030 |
|      23 | 0xDE6C      |       56940 |
|      24 | 0xFFFFF556  |  4294964566 |
|      25 | 0x18A88     |      101000 |
|      26 | 0xE524      |       58660 |
|      27 | 0xFFFFF6AA  |  4294964906 |
|      28 | 0x000F      |          15 |
|      29 | 0x0000      |           0 |
|      30 | 0x1CEE4     |      118500 |
|      31 | 0xE678      |       59000 |
|      32 | 0x03B6      |         950 |
|      33 | 0x07FF      |        2047 |
|      34 | 0x1B864     |      112740 |
|      35 | 0xE682      |       59010 |
|      36 | 0x0230      |         560 |
|      37 | 0x1A054     |      106580 |
|      38 | 0xE812      |       59410 |
|      39 | 0xFFFFFCB8  |  4294966456 |
|      40 | 0x194EC     |      103660 |
|      41 | 0xEB28      |       60200 |
|      42 | 0xFFFFF934  |  4294965556 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=257.712*, Z=398.121*, Y=0.416*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   32 00  80 1F 00 04 80 05 80 06        2.........
0020: 80 1F 01 1C 07 80 00                              .......         
```

#### Opcodes

```
  0: 0x0016 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=257.295*, Z=399.380*, Y=0.401*
  2: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0023 [0x1C] WAIT(30* ticks)
  4: 0x0026 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0027 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            32 00                2.
0030: 80 1F 00 08 80 09 80 0A  80 1F 01 1E F0 FF FF 7F  ................
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x002E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=256.812*, Z=384.685*, Y=-2.442*
  2: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    32 00 80 1F 00 0B 80  0C 80 0D 80 1F 01 1E 3A   2.............:
0050: 72 10 01 1C 07 80 00                              r......         
```

#### Opcodes

```
  0: 0x0041 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=250.148*, Z=394.668*, Y=-0.566*
  2: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004E [0x1E] EventEntity looks at Nashu (ID: 17855034/0x0110723A) and starts talking
  4: 0x0053 [0x1C] WAIT(30* ticks)
  5: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      32  00 80 1F 00 0E 80 0F 80         2........
0060: 10 80 1F 01 1E F0 FF FF  7F 1C 07 80 00           .............   
```

#### Opcodes

```
  0: 0x0057 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=251.053*, Z=390.959*, Y=-1.326*
  2: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0064 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0069 [0x1C] WAIT(30* ticks)
  5: 0x006C [0x00] END_REQSTACK()
```

### Event 114

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         00                     .  
```

#### Opcodes

```
  0: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            32 00                2.
0070: 80 1F 00 11 80 12 80 13  80 1F 01 1E 3A 72 10 01  ............:r..
0080: 1C 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x006E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0071 [0x1F] MOVE_ENTITY: EventEntity moves to X=256.405*, Z=399.102*, Y=0.369*
  2: 0x0079 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007B [0x1E] EventEntity looks at Nashu (ID: 17855034/0x0110723A) and starts talking
  4: 0x0080 [0x1C] WAIT(30* ticks)
  5: 0x0083 [0x00] END_REQSTACK()
```

### Event 131

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0084  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0084 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   1C 14 80 32 15             ...2.
0090: 80 1F 00 16 80 17 80 18  80 1F 01 1F 00 19 80 1A  ................
00A0: 80 1B 80 1F 01 1C 1C 80  39 1D 80 00              ........9...    
```

#### Opcodes

```
  0: 0x008B [0x1C] WAIT(60* ticks)
  1: 0x008E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0091 [0x1F] MOVE_ENTITY: EventEntity moves to X=96.030*, Z=56.940*, Y=-2.730*
  3: 0x0099 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x009B [0x1F] MOVE_ENTITY: EventEntity moves to X=101.000*, Z=58.660*, Y=-2.390*
  5: 0x00A3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00A5 [0x1C] WAIT(15* ticks)
  7: 0x00A8 [0x39] SET_ENTITY_DIRECTION(direction=0.0°*)
  8: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      32 07 80 1F              2...
00B0: 00 1E 80 1F 80 20 80 1F  01 00                    ..... ....      
```

#### Opcodes

```
  0: 0x00AC [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x00AF [0x1F] MOVE_ENTITY: EventEntity moves to X=118.500*, Z=59.000*, Y=0.950*
  2: 0x00B7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B9 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BA   |
| Data Size    | 40 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                39 21 80 1C 1C 80            9!....
00C0: 32 00 80 1F 00 22 80 23  80 24 80 1F 01 1F 00 25  2....".#.$.....%
00D0: 80 26 80 27 80 1F 01 1F  00 28 80 29 80 2A 80 1F  .&.'.....(.).*..
00E0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00BA [0x39] SET_ENTITY_DIRECTION(direction=11.2°*)
  1: 0x00BD [0x1C] WAIT(15* ticks)
  2: 0x00C0 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x00C3 [0x1F] MOVE_ENTITY: EventEntity moves to X=112.740*, Z=59.010*, Y=0.560*
  4: 0x00CB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00CD [0x1F] MOVE_ENTITY: EventEntity moves to X=106.580*, Z=59.410*, Y=-0.840*
  6: 0x00D5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00D7 [0x1F] MOVE_ENTITY: EventEntity moves to X=103.660*, Z=60.200*, Y=-1.740*
  8: 0x00DF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00E1 [0x00] END_REQSTACK()
```
