# 16908438 - Louverance

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Sealion's Den (ID: 32) |
| Block Size       | 512 bytes              |
| Total Events     | 15                     |
| References Count | 52                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [31](#event-31)          | 0x000D       |      7 |              2 |
| [32](#event-32)          | 0x0014       |      7 |              2 |
| [65535.1](#event-655351) | 0x001B       |     10 |              2 |
| [65535.2](#event-655352) | 0x0025       |     10 |              2 |
| [65535.3](#event-655353) | 0x002F       |     23 |              5 |
| [2](#event-2)            | 0x0046       |     10 |              2 |
| [65535.4](#event-655354) | 0x0050       |     14 |              4 |
| [65535.5](#event-655355) | 0x005E       |     14 |              4 |
| [13](#event-13)          | 0x006C       |     10 |              2 |
| [65535.6](#event-655356) | 0x0076       |     15 |              5 |
| [65535.7](#event-655357) | 0x0085       |     43 |              9 |
| [15](#event-15)          | 0x00B0       |     10 |              2 |
| [65535.8](#event-655358) | 0x00BA       |     15 |              5 |
| [65535.9](#event-655359) | 0x00C9       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF63BA7  |  4294327207 |
|       1 | 0xFFF62450  |  4294321232 |
|       2 | 0x30397     |      197527 |
|       3 | 0x0C25      |        3109 |
|       4 | 0xFFF4189C  |  4294187164 |
|       5 | 0xFFFEA361  |  4294878049 |
|       6 | 0xFFFE6C4D  |  4294863949 |
|       7 | 0x0CC8      |        3272 |
|       8 | 0x0028      |          40 |
|       9 | 0xFFF4208D  |  4294189197 |
|      10 | 0xFFFECFE1  |  4294889441 |
|      11 | 0xFFF41942  |  4294187330 |
|      12 | 0xFFFEA1DA  |  4294877658 |
|      13 | 0x0C00      |        3072 |
|      14 | 0xFFF4190C  |  4294187276 |
|      15 | 0xFFFEB20C  |  4294881804 |
|      16 | 0x000D      |          13 |
|      17 | 0xFFF63C13  |  4294327315 |
|      18 | 0xFFF62846  |  4294322246 |
|      19 | 0x952E7     |      611047 |
|      20 | 0xBE88D     |      780429 |
|      21 | 0x20599     |      132505 |
|      22 | 0x0348      |         840 |
|      23 | 0x95604     |      611844 |
|      24 | 0xBD43C     |      775228 |
|      25 | 0x2067C     |      132732 |
|      26 | 0x93D01     |      605441 |
|      27 | 0xB76E6     |      751334 |
|      28 | 0x20BD9     |      134105 |
|      29 | 0x03F3      |        1011 |
|      30 | 0x93C0C     |      605196 |
|      31 | 0xB5D68     |      744808 |
|      32 | 0x20E4E     |      134734 |
|      33 | 0x93F65     |      606053 |
|      34 | 0xB5507     |      742663 |
|      35 | 0x20EF0     |      134896 |
|      36 | 0x9515F     |      610655 |
|      37 | 0xB4944     |      739652 |
|      38 | 0x210DA     |      135386 |
|      39 | 0x95AF8     |      613112 |
|      40 | 0xBB7C7     |      767943 |
|      41 | 0x20651     |      132689 |
|      42 | 0x0C24      |        3108 |
|      43 | 0x9599C     |      612764 |
|      44 | 0xBCAF8     |      772856 |
|      45 | 0x206CB     |      132811 |
|      46 | 0x9576D     |      612205 |
|      47 | 0xBB920     |      768288 |
|      48 | 0x20645     |      132677 |
|      49 | 0x93E2C     |      605740 |
|      50 | 0xB98AD     |      759981 |
|      51 | 0x20C91     |      134289 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         94 01 F8               ...
0010: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x000D [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0013 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             94 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0014 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   37 00 80 01 80             7....
0020: 02 80 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x001B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-640.089*, z=-646.064*, y=197.527*, direction=273.2°*
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                37 04 80  05 80 06 80 07 80 00          7......... 
```

#### Opcodes

```
  0: 0x0025 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-780.132*, z=-89.247*, y=-103.347*, direction=287.6°*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 08 80 1F 00 09 80 0A 80  06 80 1F 01 4A 8F 00 02  ............J...
0040: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=-778.099*, Z=-77.855*, Y=-103.347*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x4A] Ulmia (ID: 16908431/0x0102008F) looks at EventEntity
  4: 0x0045 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   37 0B  80 0C 80 06 80 0D 80 00        7.........
```

#### Opcodes

```
  0: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-779.966*, z=-89.638*, y=-103.347*, direction=270.0°*
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 08 80 1F 00 0E 80 0F  80 06 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=-780.020*, Z=-85.492*, Y=-103.347*
  2: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            32 10                2.
0060: 80 1F 00 11 80 12 80 02  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x005E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=-639.981*, Z=-645.050*, Y=197.527*
  2: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006B [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      37 13 80 14              7...
0070: 80 15 80 16 80 00                                 ......          
```

#### Opcodes

```
  0: 0x006C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=611.047*, z=780.429*, y=132.505*, direction=73.8°*
  1: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   32 10  80 1F 00 17 80 18 80 19        2.........
0080: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0076 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0079 [0x1F] MOVE_ENTITY: EventEntity moves to X=611.844*, Z=775.228*, Y=132.732*
  2: 0x0081 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0083 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                32 10 80  37 1A 80 1B 80 1C 80 1D       2..7.......
0090: 80 1F 00 1E 80 1F 80 20  80 1F 01 1F 00 21 80 22  ....... .....!."
00A0: 80 23 80 1F 01 1F 00 24  80 25 80 26 80 1F 01 00  .#.....$.%.&....
```

#### Opcodes

```
  0: 0x0085 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0088 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=605.441*, z=751.334*, y=134.105*, direction=88.9°*
  2: 0x0091 [0x1F] MOVE_ENTITY: EventEntity moves to X=605.196*, Z=744.808*, Y=134.734*
  3: 0x0099 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x009B [0x1F] MOVE_ENTITY: EventEntity moves to X=606.053*, Z=742.663*, Y=134.896*
  5: 0x00A3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00A5 [0x1F] MOVE_ENTITY: EventEntity moves to X=610.655*, Z=739.652*, Y=135.386*
  7: 0x00AD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x00AF [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 37 27 80 28 80 29 80 2A  80 00                    7'.(.).*..      
```

#### Opcodes

```
  0: 0x00B0 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=613.112*, z=767.943*, y=132.689*, direction=273.2°*
  1: 0x00B9 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BA   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                32 10 80 1F 00 2B            2....+
00C0: 80 2C 80 2D 80 1F 01 6F  00                       .,.-...o.       
```

#### Opcodes

```
  0: 0x00BA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BD [0x1F] MOVE_ENTITY: EventEntity moves to X=612.764*, Z=772.856*, Y=132.811*
  2: 0x00C5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             32 10 80 1F 00 2E 80           2......
00D0: 2F 80 30 80 1F 01 1F 00  31 80 32 80 33 80 1F 01  /.0.....1.2.3...
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00C9 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00CC [0x1F] MOVE_ENTITY: EventEntity moves to X=612.205*, Z=768.288*, Y=132.677*
  2: 0x00D4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D6 [0x1F] MOVE_ENTITY: EventEntity moves to X=605.740*, Z=759.981*, Y=134.289*
  4: 0x00DE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00E0 [0x00] END_REQSTACK()
```
