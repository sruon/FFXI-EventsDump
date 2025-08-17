# 17735823 - Fasodo-Shiraddo

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 472 bytes              |
| Total Events     | 13                     |
| References Count | 41                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [502](#event-502)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     15 |              3 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              4 |
| [65535.3](#event-655353)   | 0x001F       |     28 |              6 |
| [65535.4](#event-655354)   | 0x003B       |     48 |             10 |
| [65535.5](#event-655355)   | 0x006B       |     15 |              3 |
| [65535.6](#event-655356)   | 0x007A       |     44 |             10 |
| [65535.7](#event-655357)   | 0x00A6       |     15 |              3 |
| [65535.8](#event-655358)   | 0x00B5       |     14 |              4 |
| [65535.9](#event-655359)   | 0x00C3       |     15 |              3 |
| [65535.10](#event-6553510) | 0x00D2       |     15 |              3 |
| [65535.11](#event-6553511) | 0x00E1       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFE2B5  |  4294959797 |
|       1 | 0xFFFFD8E5  |  4294957285 |
|       2 | 0xFFFFFFD6  |  4294967254 |
|       3 | 0x07B8      |        1976 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFFCF2D  |  4294954797 |
|       6 | 0xFFFFD9DE  |  4294957534 |
|       7 | 0xFFFFFFD4  |  4294967252 |
|       8 | 0xFFFF89CF  |  4294937039 |
|       9 | 0xFFFFD390  |  4294955920 |
|      10 | 0x0CE2      |        3298 |
|      11 | 0xFFFF8968  |  4294936936 |
|      12 | 0xFFFFDC54  |  4294958164 |
|      13 | 0x0028      |          40 |
|      14 | 0xFFFFAABE  |  4294945470 |
|      15 | 0xFFFFC955  |  4294953301 |
|      16 | 0x001E      |          30 |
|      17 | 0x003C      |          60 |
|      18 | 0xFFFFB900  |  4294949120 |
|      19 | 0xFFFFD272  |  4294955634 |
|      20 | 0xFFFFFFD2  |  4294967250 |
|      21 | 0x08DC      |        2268 |
|      22 | 0xFFFFD977  |  4294957431 |
|      23 | 0xFFFFD846  |  4294957126 |
|      24 | 0xFFFFFFC8  |  4294967240 |
|      25 | 0xFFFFE947  |  4294961479 |
|      26 | 0xFFFFCEA3  |  4294954659 |
|      27 | 0x0000      |           0 |
|      28 | 0xFFFFB39D  |  4294947741 |
|      29 | 0xFFFFD372  |  4294955890 |
|      30 | 0x0440      |        1088 |
|      31 | 0xFFFFBE34  |  4294950452 |
|      32 | 0xFFFFCFDA  |  4294954970 |
|      33 | 0xFFFFC536  |  4294952246 |
|      34 | 0xFFFFEC5B  |  4294962267 |
|      35 | 0x00B3      |         179 |
|      36 | 0xFFFFE965  |  4294961509 |
|      37 | 0xFFFFEBFC  |  4294962172 |
|      38 | 0x03DE      |         990 |
|      39 | 0xFFFFE82E  |  4294961198 |
|      40 | 0xFFFFD942  |  4294957378 |

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

### Event 502

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
0000:       37 00 80 01 80 02  80 03 80 80 8F A0 0E 01    7.............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-7.499*, z=-10.011*, y=-0.042*, direction=173.7°*
  1: 0x000B [0x80] LOAD_WAIT(entity=Fasodo-Shiraddo (ID: 17735823/0x010EA08F))
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
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.499*, Z=-9.762*, Y=-0.044*
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
0020: 08 80 09 80 07 80 0A 80  80 F8 FF FF 7F 32 04 80  .............2..
0030: 1F 00 0B 80 0C 80 07 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x001F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-30.257*, z=-11.376*, y=-0.044*, direction=289.9°*
  1: 0x0028 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x002D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=-30.360*, Z=-9.132*, Y=-0.044*
  4: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 48 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   32 0D 80 1F 00             2....
0040: 0E 80 0F 80 07 80 1F 01  1C 10 80 66 0D 80 8F A0  ...........f....
0050: 0E 01 8F A0 0E 01 7A 69  74 30 1C 11 80 32 0D 80  ......zit0...2..
0060: 1F 00 12 80 13 80 14 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=-21.826*, Z=-13.995*, Y=-0.044*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x1C] WAIT(30* ticks)
  4: 0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "zit0" with entities [Fasodo-Shiraddo (ID: 17735823/0x010EA08F), Fasodo-Shiraddo (ID: 17735823/0x010EA08F)], work=40*
  5: 0x005A [0x1C] WAIT(60* ticks)
  6: 0x005D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  7: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.176*, Z=-11.662*, Y=-0.046*
  8: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   37 05 80 06 80             7....
0070: 07 80 15 80 80 F8 FF FF  7F 00                    ..........      
```

#### Opcodes

```
  0: 0x006B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-12.499*, z=-9.762*, y=-0.044*, direction=199.3°*
  1: 0x0074 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                32 04 80 1F 00 16            2.....
0080: 80 17 80 18 80 1F 01 27  05 4F A0 0E 01 02 1C 11  .......'.O......
0090: 80 1F 00 00 80 01 80 02  80 1F 01 1F 00 19 80 1A  ................
00A0: 80 1B 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x007A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.865*, Z=-10.170*, Y=-0.056*
  2: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0087 [0x27] REQ_SET(priority=0x05, entity_id=Door:Boytz's Knickknacks (ID: 17735759/0x010EA04F), tag_num=0x02)
  4: 0x008E [0x1C] WAIT(60* ticks)
  5: 0x0091 [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.499*, Z=-10.011*, Y=-0.042*
  6: 0x0099 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x009B [0x1F] MOVE_ENTITY: EventEntity moves to X=-5.817*, Z=-12.637*, Y=0.000*
  8: 0x00A3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00A5 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A6   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   37 1C  80 1D 80 14 80 1E 80 80        7.........
00B0: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x00A6 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-19.555*, z=-11.406*, y=-0.046*, direction=95.6°*
  1: 0x00AF [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                32 0D 80  1F 00 1F 80 20 80 14 80       2...... ...
00C0: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x00B5 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-16.844*, Z=-12.326*, Y=-0.046*
  2: 0x00C0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          37 21 80 22 80  07 80 23 80 80 F8 FF FF     7!."...#.....
00D0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x00C3 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-15.050*, z=-5.029*, y=-0.044*, direction=15.7°*
  1: 0x00CC [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x00D1 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D2   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       37 24 80 25 80 1B  80 26 80 80 F8 FF FF 7F    7$.%...&......
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-5.787*, z=-5.124*, y=0.000*, direction=87.0°*
  1: 0x00DB [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    32 04 80 1F 00 27 80  28 80 1B 80 1F 01 00      2....'.(...... 
```

#### Opcodes

```
  0: 0x00E1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00E4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-6.098*, Z=-9.918*, Y=0.000*
  2: 0x00EC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00EE [0x00] END_REQSTACK()
```
