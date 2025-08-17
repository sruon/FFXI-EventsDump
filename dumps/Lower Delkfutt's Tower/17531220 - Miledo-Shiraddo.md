# 17531220 - Miledo-Shiraddo

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 320 bytes                        |
| Total Events     | 16                               |
| References Count | 29                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [27](#event-27)            | 0x0001       |      1 |              1 |
| [28](#event-28)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     15 |              3 |
| [65535.2](#event-655352)   | 0x0012       |     15 |              3 |
| [65535.3](#event-655353)   | 0x0021       |     14 |              4 |
| [65535.4](#event-655354)   | 0x002F       |     15 |              3 |
| [65535.5](#event-655355)   | 0x003E       |     14 |              4 |
| [65535.6](#event-655356)   | 0x004C       |     15 |              3 |
| [65535.7](#event-655357)   | 0x005B       |     14 |              4 |
| [29](#event-29)            | 0x0069       |      1 |              1 |
| [65535.8](#event-655358)   | 0x006A       |      1 |              1 |
| [65535.9](#event-655359)   | 0x006B       |      1 |              1 |
| [65535.10](#event-6553510) | 0x006C       |     14 |              4 |
| [30](#event-30)            | 0x007A       |      1 |              1 |
| [65535.11](#event-6553511) | 0x007B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x882C1     |      557761 |
|       1 | 0xFFFF9874  |  4294940788 |
|       2 | 0xFFFFFFF3  |  4294967283 |
|       3 | 0x0525      |        1317 |
|       4 | 0x87501     |      554241 |
|       5 | 0xFFFF7E58  |  4294934104 |
|       6 | 0x00E0      |         224 |
|       7 | 0x0933      |        2355 |
|       8 | 0x0028      |          40 |
|       9 | 0x874DE     |      554206 |
|      10 | 0xFFFF8933  |  4294936883 |
|      11 | 0x002F      |          47 |
|      12 | 0x8DE17     |      581143 |
|      13 | 0xFFFFB251  |  4294947409 |
|      14 | 0x0000      |           0 |
|      15 | 0x0877      |        2167 |
|      16 | 0x000D      |          13 |
|      17 | 0x8D84C     |      579660 |
|      18 | 0xFFFFA201  |  4294943233 |
|      19 | 0x87605     |      554501 |
|      20 | 0xFFFF776A  |  4294932330 |
|      21 | 0x015F      |         351 |
|      22 | 0x08B4      |        2228 |
|      23 | 0x87867     |      555111 |
|      24 | 0xFFFF7691  |  4294932113 |
|      25 | 0x0184      |         388 |
|      26 | 0x86E2A     |      552490 |
|      27 | 0xFFFF6BE2  |  4294929378 |
|      28 | 0x014C      |         332 |

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

### Event 27

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

### Event 28

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
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 80 F8 FF FF     7............
0010: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=557.761*, z=-26.508*, y=-0.013*, direction=115.7°*
  1: 0x000C [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       37 04 80 05 80 06  80 07 80 80 F8 FF FF 7F    7.............
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0012 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=554.241*, z=-33.192*, y=0.224*, direction=207.0°*
  1: 0x001B [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 08 80 1F 00 09 80  0A 80 0B 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=554.206*, Z=-30.413*, Y=0.047*
  2: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               37                 7
0030: 0C 80 0D 80 0E 80 0F 80  80 F8 FF FF 7F 00        ..............  
```

#### Opcodes

```
  0: 0x002F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=581.143*, z=-19.887*, y=0.000*, direction=190.5°*
  1: 0x0038 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            32 10                2.
0040: 80 1F 00 11 80 12 80 0E  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x003E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=579.660*, Z=-24.063*, Y=0.000*
  2: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      37 13 80 14              7...
0050: 80 15 80 16 80 80 F8 FF  FF 7F 00                 ...........     
```

#### Opcodes

```
  0: 0x004C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=554.501*, z=-34.966*, y=0.351*, direction=195.8°*
  1: 0x0055 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   32 10 80 1F 00             2....
0060: 17 80 18 80 19 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x005B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=555.111*, Z=-35.183*, Y=0.388*
  2: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0068 [0x00] END_REQSTACK()
```

### Event 29

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0069  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             00                             .      
```

#### Opcodes

```
  0: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                00                           .     
```

#### Opcodes

```
  0: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   00                         .    
```

#### Opcodes

```
  0: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      32 10 80 1F              2...
0070: 00 1A 80 1B 80 1C 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x006C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=552.490*, Z=-37.918*, Y=0.332*
  2: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0079 [0x00] END_REQSTACK()
```

### Event 30

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                00                           .     
```

#### Opcodes

```
  0: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   00                         .    
```

#### Opcodes

```
  0: 0x007B [0x00] END_REQSTACK()
```
