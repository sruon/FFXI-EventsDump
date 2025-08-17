# 17604681 - Uran-Mafran

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Cloister of Storms (ID: 202) |
| Block Size       | 788 bytes                    |
| Total Events     | 32                           |
| References Count | 25                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     32 |              4 |
| [65535.3](#event-655353)   | 0x0031       |     50 |              5 |
| [65535.4](#event-655354)   | 0x0063       |     35 |              4 |
| [65535.5](#event-655355)   | 0x0086       |     34 |              4 |
| [65535.6](#event-655356)   | 0x00A8       |     44 |              4 |
| [65535.7](#event-655357)   | 0x00D4       |     28 |              4 |
| [65535.8](#event-655358)   | 0x00F0       |     14 |              2 |
| [65535.9](#event-655359)   | 0x00FE       |     22 |              3 |
| [65535.10](#event-6553510) | 0x0114       |     20 |              3 |
| [65535.11](#event-6553511) | 0x0128       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0138       |     14 |              2 |
| [65535.13](#event-6553513) | 0x0146       |     16 |              2 |
| [65535.14](#event-6553514) | 0x0156       |     29 |              3 |
| [65535.15](#event-6553515) | 0x0173       |     22 |              3 |
| [65535.16](#event-6553516) | 0x0189       |     14 |              2 |
| [65535.17](#event-6553517) | 0x0197       |     16 |              2 |
| [65535.18](#event-6553518) | 0x01A7       |     20 |              3 |
| [65535.19](#event-6553519) | 0x01BB       |     22 |              3 |
| [32000](#event-32000)      | 0x01D1       |      1 |              1 |
| [32001](#event-32001)      | 0x01D2       |      1 |              1 |
| [65535.20](#event-6553520) | 0x01D3       |      1 |              1 |
| [65535.21](#event-6553521) | 0x01D4       |     10 |              2 |
| [65535.22](#event-6553522) | 0x01DE       |      1 |              1 |
| [65535.23](#event-6553523) | 0x01DF       |     16 |              3 |
| [65535.24](#event-6553524) | 0x01EF       |     14 |              4 |
| [65535.25](#event-6553525) | 0x01FD       |     14 |              4 |
| [65535.26](#event-6553526) | 0x020B       |      5 |              3 |
| [65535.27](#event-6553527) | 0x0210       |      5 |              3 |
| [65535.28](#event-6553528) | 0x0215       |      5 |              3 |
| [65535.29](#event-6553529) | 0x021A       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x000F      |          15 |
|       2 | 0x003C      |          60 |
|       3 | 0x002A      |          42 |
|       4 | 0x002E      |          46 |
|       5 | 0x001E      |          30 |
|       6 | 0x585B      |       22619 |
|       7 | 0x76C2      |       30402 |
|       8 | 0xFFFFB909  |  4294949129 |
|       9 | 0x0DF8      |        3576 |
|      10 | 0x69EC      |       27116 |
|      11 | 0x876B      |       34667 |
|      12 | 0xFFFFB4B9  |  4294948025 |
|      13 | 0x05EB      |        1515 |
|      14 | 0x000D      |          13 |
|      15 | 0x6205      |       25093 |
|      16 | 0x7E20      |       32288 |
|      17 | 0xFFFFB82E  |  4294948910 |
|      18 | 0x591F      |       22815 |
|      19 | 0x74BE      |       29886 |
|      20 | 0xFFFFB8FE  |  4294949118 |
|      21 | 0x1E20      |        7712 |
|      22 | 0x1E26      |        7718 |
|      23 | 0x1E35      |        7733 |
|      24 | 0x1E3B      |        7739 |

## String References

- **7712**: To win against such opponents...
- **7718**: ...Ah, Ildy-Goldy.
- **7733**: Have you forgotten what my specialty is? I cloaked a m-m-magical doll with an illusion...
- **7739**: Let us be going, Ildy-Goldy. The slum-m-mbering power of the protocrystals awaits... With your skill in battle, all of that energy will soon be m-m-mine...

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 66 01   S........tlk0f.
0020: 80 F8 FF FF 7F F8 FF FF  7F 73 74 64 30 1C 02 80  .........std0...
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=15*
  2: 0x002D [0x1C] WAIT(60* ticks)
  3: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 50 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    81 00 F8 FF FF 7F 66  03 80 49 A0 0C 01 49 A0   ......f..I...I.
0040: 0C 01 77 6F 6E 32 66 04  80 F8 FF FF 7F F8 FF FF  ..won2f.........
0050: 7F 6D 67 63 30 53 F8 FF  FF 7F F8 FF FF 7F 6D 67  .mgc0S........mg
0060: 63 30 00                                          c0.             
```

#### Opcodes

```
  0: 0x0031 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "won2" with entities [Uran-Mafran (ID: 17604681/0x010CA049), Uran-Mafran (ID: 17604681/0x010CA049)], work=42*
  2: 0x0046 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "mgc0" with entities [EventEntity, EventEntity], work=46*
  3: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mgc0" with entities [EventEntity, EventEntity]
  4: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 35 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          66 04 80 F8 FF  FF 7F F8 FF FF 7F 6D 64     f..........md
0070: 71 32 53 F8 FF FF 7F F8  FF FF 7F 6D 64 71 32 81  q2S........mdq2.
0080: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "mdq2" with entities [EventEntity, EventEntity], work=46*
  1: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mdq2" with entities [EventEntity, EventEntity]
  2: 0x007F [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  3: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   66 03  80 49 A0 0C 01 49 A0 0C        f..I...I..
0090: 01 77 6F 66 32 66 01 80  F8 FF FF 7F F8 FF FF 7F  .wof2f..........
00A0: 73 74 64 30 1C 05 80 00                           std0....        
```

#### Opcodes

```
  0: 0x0086 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wof2" with entities [Uran-Mafran (ID: 17604681/0x010CA049), Uran-Mafran (ID: 17604681/0x010CA049)], work=42*
  1: 0x0095 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=15*
  2: 0x00A4 [0x1C] WAIT(30* ticks)
  3: 0x00A7 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A8   |
| Data Size    | 44 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                          66 03 80 49 A0 0C 01 49          f..I...I
00B0: A0 0C 01 77 6F 66 32 66  01 80 F8 FF FF 7F F8 FF  ...wof2f........
00C0: FF 7F 73 74 64 30 53 F8  FF FF 7F F8 FF FF 7F 73  ..std0S........s
00D0: 74 64 30 00                                       td0.            
```

#### Opcodes

```
  0: 0x00A8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wof2" with entities [Uran-Mafran (ID: 17604681/0x010CA049), Uran-Mafran (ID: 17604681/0x010CA049)], work=42*
  1: 0x00B7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=15*
  2: 0x00C6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "std0" with entities [EventEntity, EventEntity]
  3: 0x00D3 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D4   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             81 00 F8 FF  FF 7F 7C 00 F8 FF FF 7F      ......|.....
00E0: 66 01 80 F8 FF FF 7F F8  FF FF 7F 77 72 75 30 00  f..........wru0.
```

#### Opcodes

```
  0: 0x00D4 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x00DA [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x00E0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wru0" with entities [EventEntity, EventEntity], work=15*
  3: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 53 F8 FF FF 7F F8 FF FF  7F 77 72 75 30 00        S........wru0.  
```

#### Opcodes

```
  0: 0x00F0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wru0" with entities [EventEntity, EventEntity]
  1: 0x00FD [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FE   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            7C 01                |.
0100: F8 FF FF 7F 66 01 80 F8  FF FF 7F F8 FF FF 7F 77  ....f..........w
0110: 72 75 31 00                                       ru1.            
```

#### Opcodes

```
  0: 0x00FE [0x7C] EventEntity->Render.Flags2 |= 0x01
  1: 0x0104 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wru1" with entities [EventEntity, EventEntity], work=15*
  2: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             53 F8 FF FF  7F F8 FF FF 7F 77 72 75      S........wru
0120: 31 81 01 F8 FF FF 7F 00                           1.......        
```

#### Opcodes

```
  0: 0x0114 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wru1" with entities [EventEntity, EventEntity]
  1: 0x0121 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x0127 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0128   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          66 01 80 F8 FF FF 7F F8          f.......
0130: FF FF 7F 69 6B 75 30 00                           ...iku0.        
```

#### Opcodes

```
  0: 0x0128 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iku0" with entities [EventEntity, EventEntity], work=15*
  1: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          53 F8 FF FF 7F F8 FF FF          S.......
0140: 7F 69 6B 75 30 00                                 .iku0.          
```

#### Opcodes

```
  0: 0x0138 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iku0" with entities [EventEntity, EventEntity]
  1: 0x0145 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0146   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                   66 01  80 F8 FF FF 7F F8 FF FF        f.........
0150: 7F 69 6B 75 31 00                                 .iku1.          
```

#### Opcodes

```
  0: 0x0146 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iku1" with entities [EventEntity, EventEntity], work=15*
  1: 0x0155 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   53 F8  FF FF 7F F8 FF FF 7F 69        S........i
0160: 6B 75 31 66 01 80 F8 FF  FF 7F F8 FF FF 7F 73 74  ku1f..........st
0170: 64 30 00                                          d0.             
```

#### Opcodes

```
  0: 0x0156 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iku1" with entities [EventEntity, EventEntity]
  1: 0x0163 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=15*
  2: 0x0172 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0173   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:          81 00 F8 FF FF  7F 66 01 80 F8 FF FF 7F     ......f......
0180: F8 FF FF 7F 75 6B 6D 30  00                       ....ukm0.       
```

#### Opcodes

```
  0: 0x0173 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0179 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ukm0" with entities [EventEntity, EventEntity], work=15*
  2: 0x0188 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0189   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                             53 F8 FF FF 7F F8 FF           S......
0190: FF 7F 75 6B 6D 30 00                              ..ukm0.         
```

#### Opcodes

```
  0: 0x0189 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ukm0" with entities [EventEntity, EventEntity]
  1: 0x0196 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0197   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                      66  01 80 F8 FF FF 7F F8 FF         f........
01A0: FF 7F 75 6B 6D 31 00                              ..ukm1.         
```

#### Opcodes

```
  0: 0x0197 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ukm1" with entities [EventEntity, EventEntity], work=15*
  1: 0x01A6 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A7   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
01B0: 75 6B 6D 31 81 01 F8 FF  FF 7F 00                 ukm1.......     
```

#### Opcodes

```
  0: 0x01A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ukm1" with entities [EventEntity, EventEntity]
  1: 0x01B4 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x01BA [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BB   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                   94 01 F8 FF FF             .....
01C0: 7F 66 04 80 F8 FF FF 7F  F8 FF FF 7F 00 FE FE FE  .f..............
01D0: 00                                                .               
```

#### Opcodes

```
  0: 0x01BB [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x01C1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=46*
  2: 0x01D0 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01D1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:    00                                              .              
```

#### Opcodes

```
  0: 0x01D1 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01D2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:       00                                            .             
```

#### Opcodes

```
  0: 0x01D2 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01D3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:          00                                          .            
```

#### Opcodes

```
  0: 0x01D3 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D4   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:             37 06 80 07  80 08 80 09 80 00            7.........  
```

#### Opcodes

```
  0: 0x01D4 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.619*, z=30.402*, y=-18.167*, direction=314.3°*
  1: 0x01DD [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01DE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                            00                   . 
```

#### Opcodes

```
  0: 0x01DE [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01DF   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                               92                 .
01E0: 01 F8 FF FF 7F 37 0A 80  0B 80 0C 80 0D 80 00     .....7......... 
```

#### Opcodes

```
  0: 0x01DF [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x01E5 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=27.116*, z=34.667*, y=-19.271*, direction=133.2°*
  2: 0x01EE [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01EF   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                                               32                 2
01F0: 0E 80 5A 00 0F 80 10 80  11 80 5A 01 00           ..Z.......Z..   
```

#### Opcodes

```
  0: 0x01EF [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01F2 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=25.093*, Z=32.288*, Y=-18.386*
  2: 0x01FA [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x01FC [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01FD   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                         32 0E 80               2..
0200: 5A 00 12 80 13 80 14 80  5A 01 00                 Z.......Z..     
```

#### Opcodes

```
  0: 0x01FD [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0200 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=22.815*, Z=29.886*, Y=-18.178*
  2: 0x0208 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x020A [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x020B  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                   1D 15 80 23 00             ...#.
```

#### Opcodes

```
  0: 0x020B [0x1D] PRINT_EVENT_MESSAGE(message_id=7712*)
    → "To win against such opponents..."
  1: 0x020E [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x020F [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0210  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210: 1D 16 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x0210 [0x1D] PRINT_EVENT_MESSAGE(message_id=7718*)
    → "...Ah, Ildy-Goldy."
  1: 0x0213 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0214 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0215  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                1D 17 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x0215 [0x1D] PRINT_EVENT_MESSAGE(message_id=7733*)
    → "Have you forgotten what my specialty is? I cloaked a m-m-magical doll with an illusion..."
  1: 0x0218 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0219 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x021A  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                                1D 18 80 23 00               ...#. 
```

#### Opcodes

```
  0: 0x021A [0x1D] PRINT_EVENT_MESSAGE(message_id=7739*)
    → "Let us be going, Ildy-Goldy. The slum-m-mbering power of the protocrystals awaits... With your skill in battle, all of that energy will soon be m-m-mine..."
  1: 0x021D [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x021E [0x00] END_REQSTACK()
```
