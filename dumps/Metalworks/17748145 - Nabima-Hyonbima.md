# 17748145 - Nabima-Hyonbima

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 416 bytes            |
| Total Events     | 19                   |
| References Count | 36                   |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [900](#event-900)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     14 |              4 |
| [908](#event-908)          | 0x0010       |      1 |              1 |
| [909](#event-909)          | 0x0011       |      1 |              1 |
| [910](#event-910)          | 0x0012       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0013       |     15 |              3 |
| [65535.3](#event-655353)   | 0x0022       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0030       |     15 |              3 |
| [65535.5](#event-655355)   | 0x003F       |     14 |              4 |
| [65535.6](#event-655356)   | 0x004D       |     15 |              3 |
| [65535.7](#event-655357)   | 0x005C       |     14 |              4 |
| [920](#event-920)          | 0x006A       |      1 |              1 |
| [65535.8](#event-655358)   | 0x006B       |     15 |              3 |
| [65535.9](#event-655359)   | 0x007A       |     14 |              4 |
| [65535.10](#event-6553510) | 0x0088       |     14 |              4 |
| [65535.11](#event-6553511) | 0x0096       |     15 |              3 |
| [65535.12](#event-6553512) | 0x00A5       |     14 |              4 |
| [928](#event-928)          | 0x00B3       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFF9ED0  |  4294942416 |
|       2 | 0x004F      |          79 |
|       3 | 0x1F3F      |        7999 |
|       4 | 0xFFFF42AC  |  4294918828 |
|       5 | 0x54FD      |       21757 |
|       6 | 0x0AD5      |        2773 |
|       7 | 0x0990      |        2448 |
|       8 | 0xFFFF3FB6  |  4294918070 |
|       9 | 0x5E30      |       24112 |
|      10 | 0xFFFFCDE1  |  4294954465 |
|      11 | 0xFFFFF120  |  4294963488 |
|      12 | 0x0000      |           0 |
|      13 | 0x07BD      |        1981 |
|      14 | 0xFFFFC77A  |  4294952826 |
|      15 | 0xFFFFFA90  |  4294965904 |
|      16 | 0xFFFE91DD  |  4294873565 |
|      17 | 0xFFFFDC38  |  4294958136 |
|      18 | 0x07CF      |        1999 |
|      19 | 0x002E      |          46 |
|      20 | 0xFFFE9D02  |  4294876418 |
|      21 | 0xFFFFE017  |  4294959127 |
|      22 | 0x07D0      |        2000 |
|      23 | 0xFFFF8BA4  |  4294937508 |
|      24 | 0xFFFFFF54  |  4294967124 |
|      25 | 0x0F05      |        3845 |
|      26 | 0xFFFF95C8  |  4294940104 |
|      27 | 0xFFFFFF86  |  4294967174 |
|      28 | 0xFFFF73AE  |  4294931374 |
|      29 | 0xFFFFFFFF  |  4294967295 |
|      30 | 0xFFFF9C8C  |  4294941836 |
|      31 | 0x0F07      |        3847 |
|      32 | 0x0477      |        1143 |
|      33 | 0x0028      |          40 |
|      34 | 0xFFFFA056  |  4294942806 |
|      35 | 0x0911      |        2321 |

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

### Event 900

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-24.880*, Z=0.079*, Y=7.999*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 908

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 909

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    00                                              .              
```

#### Opcodes

```
  0: 0x0011 [0x00] END_REQSTACK()
```

### Event 910

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       00                                            .             
```

#### Opcodes

```
  0: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          37 04 80 05 80  06 80 07 80 80 F8 FF FF     7............
0020: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-48.468*, z=21.757*, y=2.773*, direction=215.1°*
  1: 0x001C [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       32 00 80 1F 00 08  80 09 80 06 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0022 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=-49.226*, Z=24.112*, Y=2.773*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 37 0A 80 0B 80 0C 80 0D  80 80 F8 FF FF 7F 00     7.............. 
```

#### Opcodes

```
  0: 0x0030 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-12.831*, z=-3.808*, y=0.000*, direction=174.1°*
  1: 0x0039 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               32                 2
0040: 00 80 1F 00 0E 80 0F 80  0C 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x003F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0042 [0x1F] MOVE_ENTITY: EventEntity moves to X=-14.470*, Z=-1.392*, Y=0.000*
  2: 0x004A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         37 10 80               7..
0050: 11 80 12 80 13 80 80 F8  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x004D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-93.731*, z=-9.160*, y=1.999*, direction=4.0°*
  1: 0x0056 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      32 00 80 1F              2...
0060: 00 14 80 15 80 16 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x005C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=-90.878*, Z=-8.169*, Y=2.000*
  2: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0069 [0x00] END_REQSTACK()
```

### Event 920

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   37 17 80 18 80             7....
0070: 03 80 19 80 80 F8 FF FF  7F 00                    ..........      
```

#### Opcodes

```
  0: 0x006B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-29.788*, z=-0.172*, y=7.999*, direction=337.9°*
  1: 0x0074 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                32 00 80 1F 00 1A            2.....
0080: 80 1B 80 03 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x007A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=-27.192*, Z=-0.122*, Y=7.999*
  2: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          32 00 80 1F 00 1C 80 1D          2.......
0090: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0088 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008B [0x1F] MOVE_ENTITY: EventEntity moves to X=-35.922*, Z=-0.001*, Y=7.999*
  2: 0x0093 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0096   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   37 1E  80 1F 80 03 80 20 80 80        7...... ..
00A0: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0096 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-25.460*, z=3.847*, y=7.999*, direction=100.5°*
  1: 0x009F [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                32 21 80  1F 00 22 80 23 80 03 80       2!...".#...
00B0: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x00A5 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-24.490*, Z=2.321*, Y=7.999*
  2: 0x00B0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B2 [0x00] END_REQSTACK()
```

### Event 928

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          00                                          .            
```

#### Opcodes

```
  0: 0x00B3 [0x00] END_REQSTACK()
```
