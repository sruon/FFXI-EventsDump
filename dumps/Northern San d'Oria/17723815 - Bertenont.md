# 17723815 - Bertenont

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 312 bytes                     |
| Total Events     | 13                            |
| References Count | 25                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [869](#event-869)        | 0x0000       |      1 |              1 |
| [870](#event-870)        | 0x0001       |      1 |              1 |
| [65535](#event-65535)    | 0x0002       |     14 |              4 |
| [65535.1](#event-655351) | 0x0010       |     14 |              4 |
| [65535.2](#event-655352) | 0x001E       |     14 |              4 |
| [65535.3](#event-655353) | 0x002C       |     14 |              4 |
| [65535.4](#event-655354) | 0x003A       |     14 |              4 |
| [65535.5](#event-655355) | 0x0048       |     24 |              6 |
| [65535.6](#event-655356) | 0x0060       |     14 |              4 |
| [65535.7](#event-655357) | 0x006E       |     14 |              4 |
| [65535.8](#event-655358) | 0x007C       |     10 |              2 |
| [65535.9](#event-655359) | 0x0086       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x1F1BA     |      127418 |
|       2 | 0x1D226     |      119334 |
|       3 | 0x0000      |           0 |
|       4 | 0x0010      |          16 |
|       5 | 0x1AD20     |      109856 |
|       6 | 0x18D92     |      101778 |
|       7 | 0x12243     |       74307 |
|       8 | 0x1040A     |       66570 |
|       9 | 0x1C548     |      116040 |
|      10 | 0x1A609     |      108041 |
|      11 | 0x0028      |          40 |
|      12 | 0x1BC84     |      113796 |
|      13 | 0x19EBE     |      106174 |
|      14 | 0x1A140     |      106816 |
|      15 | 0x18169     |       98665 |
|      16 | 0x195BC     |      103868 |
|      17 | 0x1752C     |       95532 |
|      18 | 0x06D5      |        1749 |
|      19 | 0x1818B     |       98699 |
|      20 | 0x16100     |       90368 |
|      21 | 0x17969     |       96617 |
|      22 | 0x15938     |       88376 |
|      23 | 0x0001      |           1 |
|      24 | 0x0080      |         128 |

## Events

### Event 869

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

### Event 870

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
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=127.418*, Z=119.334*, Y=0.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 04 80 1F 00 05 80 06  80 03 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 16* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=109.856*, Z=101.778*, Y=0.000*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            32 00                2.
0020: 80 1F 00 07 80 08 80 03  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x001E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0021 [0x1F] MOVE_ENTITY: EventEntity moves to X=74.307*, Z=66.570*, Y=0.000*
  2: 0x0029 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      32 00 80 1F              2...
0030: 00 09 80 0A 80 03 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x002C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=116.040*, Z=108.041*, Y=0.000*
  2: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                32 0B 80 1F 00 0C            2.....
0040: 80 0D 80 03 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x003A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=113.796*, Z=106.174*, Y=0.000*
  2: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          32 0B 80 1F 00 0E 80 0F          2.......
0050: 80 03 80 1F 01 1F 00 10  80 11 80 12 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x0048 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=106.816*, Z=98.665*, Y=0.000*
  2: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=103.868*, Z=95.532*, Y=1.749*
  4: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 32 0B 80 1F 00 13 80 14  80 12 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0060 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=98.699*, Z=90.368*, Y=1.749*
  2: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            32 0B                2.
0070: 80 1F 00 15 80 16 80 12  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x006E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0071 [0x1F] MOVE_ENTITY: EventEntity moves to X=96.617*, Z=88.376*, Y=1.749*
  2: 0x0079 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      6C A7 71 0E              l.q.
0080: 01 03 80 17 80 00                                 ......          
```

#### Opcodes

```
  0: 0x007C [0x6C] FADE_ENTITY_COLOR(entity_id=Bertenont (ID: 17723815/0x010E71A7), end_alpha=0*, fade_time=1*)
  1: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   6C A7  71 0E 01 18 80 17 80 00        l.q.......
```

#### Opcodes

```
  0: 0x0086 [0x6C] FADE_ENTITY_COLOR(entity_id=Bertenont (ID: 17723815/0x010E71A7), end_alpha=128*, fade_time=1*)
  1: 0x008F [0x00] END_REQSTACK()
```
