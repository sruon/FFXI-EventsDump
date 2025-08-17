# 17171235 - Lehko Habhoka

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 632 bytes                       |
| Total Events     | 28                              |
| References Count | 41                              |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [106](#event-106)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |      5 |              2 |
| [112](#event-112)          | 0x0007       |      1 |              1 |
| [113](#event-113)          | 0x0008       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0009       |      5 |              2 |
| [65535.3](#event-655353)   | 0x000E       |      5 |              2 |
| [65535.4](#event-655354)   | 0x0013       |      5 |              2 |
| [65535.5](#event-655355)   | 0x0018       |     21 |              2 |
| [65535.6](#event-655356)   | 0x002D       |     21 |              2 |
| [65535.7](#event-655357)   | 0x0042       |      5 |              2 |
| [65535.8](#event-655358)   | 0x0047       |     25 |              3 |
| [65535.9](#event-655359)   | 0x0060       |     25 |              3 |
| [65535.10](#event-6553510) | 0x0079       |     25 |              3 |
| [65535.11](#event-6553511) | 0x0092       |     14 |              4 |
| [65535.12](#event-6553512) | 0x00A0       |     14 |              4 |
| [65535.13](#event-6553513) | 0x00AE       |     22 |              6 |
| [65535.14](#event-6553514) | 0x00C4       |     15 |              5 |
| [65535.15](#event-6553515) | 0x00D3       |      5 |              2 |
| [65535.16](#event-6553516) | 0x00D8       |     29 |              4 |
| [65535.17](#event-6553517) | 0x00F5       |      5 |              2 |
| [65535.18](#event-6553518) | 0x00FA       |      5 |              2 |
| [65535.19](#event-6553519) | 0x00FF       |      5 |              2 |
| [65535.20](#event-6553520) | 0x0104       |     29 |              4 |
| [65535.21](#event-6553521) | 0x0121       |     15 |              5 |
| [65535.22](#event-6553522) | 0x0130       |     15 |              5 |
| [65535.23](#event-6553523) | 0x013F       |     15 |              5 |
| [65535.24](#event-6553524) | 0x014E       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0064      |         100 |
|       1 | 0x02F3      |         755 |
|       2 | 0x043C      |        1084 |
|       3 | 0x08C3      |        2243 |
|       4 | 0x0007      |           7 |
|       5 | 0x0003      |           3 |
|       6 | 0x0000      |           0 |
|       7 | 0x005E      |          94 |
|       8 | 0x000E      |          14 |
|       9 | 0x006E      |         110 |
|      10 | 0x0317      |         791 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFFFCF94  |  4294954900 |
|      13 | 0xFFFECAF5  |  4294888181 |
|      14 | 0xFFFEF661  |  4294899297 |
|      15 | 0xFFFFCFBC  |  4294954940 |
|      16 | 0xFFFEC473  |  4294886515 |
|      17 | 0xFFF8DEBA  |  4294500026 |
|      18 | 0xC0BF      |       49343 |
|      19 | 0xFFFF8E45  |  4294938181 |
|      20 | 0x001E      |          30 |
|      21 | 0xFFFF0B61  |  4294904673 |
|      22 | 0x024D      |         589 |
|      23 | 0xFFFED8BF  |  4294891711 |
|      24 | 0x0108      |         264 |
|      25 | 0x08E4      |        2276 |
|      26 | 0x0875      |        2165 |
|      27 | 0x08F6      |        2294 |
|      28 | 0x08D8      |        2264 |
|      29 | 0x000B      |          11 |
|      30 | 0xFFFDF463  |  4294833251 |
|      31 | 0xFFFE64C0  |  4294862016 |
|      32 | 0xFFFED767  |  4294891367 |
|      33 | 0x002C      |          44 |
|      34 | 0xFFFDDE0C  |  4294827532 |
|      35 | 0xFFFE7B7A  |  4294867834 |
|      36 | 0x002A      |          42 |
|      37 | 0xFFFF8D89  |  4294937993 |
|      38 | 0x12ED4     |       77524 |
|      39 | 0xFFFEF5DF  |  4294899167 |
|      40 | 0x0001      |           1 |

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

### Event 106

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       B6 0F 00 80 00                                .....         
```

#### Opcodes

```
  0: 0x0002 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=100*)
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      00                                  .        
```

#### Opcodes

```
  0: 0x0007 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          00                               .       
```

#### Opcodes

```
  0: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             B6 00 01 80 00                 .....  
```

#### Opcodes

```
  0: 0x0009 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=755*)
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            B6 00                ..
0010: 02 80 00                                          ...             
```

#### Opcodes

```
  0: 0x000E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1084*)
  1: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          B6 00 03 80 00                              .....        
```

#### Opcodes

```
  0: 0x0013 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2243*)
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          B6 0B 04 80 05 80 06 80          ........
0020: 07 80 07 80 08 80 08 80  06 80 06 80 00           .............   
```

#### Opcodes

```
  0: 0x0018 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=3*, head=0*, body=94*, hands=94*, legs=14*, feet=14*, main=0*, sub=0*)
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         B6 0B 04               ...
0030: 80 05 80 06 80 07 80 07  80 08 80 08 80 09 80 06  ................
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x002D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=3*, head=0*, body=94*, hands=94*, legs=14*, feet=14*, main=110*, sub=0*)
  1: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0042  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       B6 00 0A 80 00                                .....         
```

#### Opcodes

```
  0: 0x0042 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=791*)
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      B4  00 00 00 3F 3F 3F 00 00         ....???..
0050: 00 00 00 00 00 00 00 00  00 00 00 B5 00 00 00 00  ................
```

#### Opcodes

```
  0: 0x0047 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="???")
  1: 0x005B [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: B4 00 00 00 52 6F 62 65  6C 2D 41 6B 62 65 6C 00  ....Robel-Akbel.
0070: 00 00 00 00 B5 00 00 00  00                       .........       
```

#### Opcodes

```
  0: 0x0060 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Robel-Akbel")
  1: 0x0074 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             B4 00 00 00 30 32 00           ....02.
0080: 00 00 00 00 00 00 00 00  00 00 00 00 00 B5 00 00  ................
0090: 00 00                                             ..              
```

#### Opcodes

```
  0: 0x0079 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="02")
  1: 0x008D [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       32 0B 80 1F 00 0C  80 0D 80 0E 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0092 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0095 [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.396*, Z=-79.115*, Y=-67.999*
  2: 0x009D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009F [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A0   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 32 0B 80 1F 00 0F 80 10  80 0E 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x00A0 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A3 [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.356*, Z=-80.781*, Y=-67.999*
  2: 0x00AB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            32 0B                2.
00B0: 80 5A 00 11 80 12 80 13  80 5A 01 1E F0 FF FF 7F  .Z.......Z......
00C0: 1C 14 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00AE [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B1 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-467.270*, Z=49.343*, Y=-29.115*
  2: 0x00B9 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00BB [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00C0 [0x1C] WAIT(30* ticks)
  5: 0x00C3 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C4   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:             32 0B 80 1F  00 15 80 16 80 17 80 1F      2...........
00D0: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x00C4 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00C7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-62.623*, Z=0.589*, Y=-75.585*
  2: 0x00CF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D3  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          B6 00 18 80 00                              .....        
```

#### Opcodes

```
  0: 0x00D3 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=264*)
  1: 0x00D7 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D8   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                          B6 00 19 80 B4 13 00 00          ........
00E0: 4C 65 68 6B 6F 40 48 61  62 68 6F 6B 61 00 00 00  Lehko@Habhoka...
00F0: B5 00 00 00 00                                    .....           
```

#### Opcodes

```
  0: 0x00D8 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2276*)
  1: 0x00DC [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Lehko@Habhoka")
  2: 0x00F0 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  3: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F5  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                B6 00 1A  80 00                         .....      
```

#### Opcodes

```
  0: 0x00F5 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2165*)
  1: 0x00F9 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FA  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                B6 00 1B 80 00               ..... 
```

#### Opcodes

```
  0: 0x00FA [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2294*)
  1: 0x00FE [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FF  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               B6                 .
0100: 00 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00FF [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=755*)
  1: 0x0103 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0104   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             B6 00 1C 80  B4 13 00 00 52 6F 6D 61      ........Roma
0110: 61 40 4D 69 68 67 6F 00  00 00 00 00 B5 00 00 00  a@Mihgo.........
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0104 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2264*)
  1: 0x0108 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Romaa@Mihgo")
  2: 0x011C [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  3: 0x0120 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0121   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    32 1D 80 1F 00 1E 80  1F 80 20 80 1F 01 6F 00   2........ ...o.
```

#### Opcodes

```
  0: 0x0121 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0124 [0x1F] MOVE_ENTITY: EventEntity moves to X=-134.045*, Z=-105.280*, Y=-75.929*
  2: 0x012C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x012E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 32 21 80 1F 00 22 80 23  80 17 80 1F 01 6F 00     2!...".#.....o. 
```

#### Opcodes

```
  0: 0x0130 [0x32] ExtData[1]->MainSpeed = 44* * 0.1
  1: 0x0133 [0x1F] MOVE_ENTITY: EventEntity moves to X=-139.764*, Z=-99.462*, Y=-75.585*
  2: 0x013B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x013D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x013E [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                               32                 2
0140: 24 80 1F 00 25 80 26 80  27 80 1F 01 6F 00        $...%.&.'...o.  
```

#### Opcodes

```
  0: 0x013F [0x32] ExtData[1]->MainSpeed = 42* * 0.1
  1: 0x0142 [0x1F] MOVE_ENTITY: EventEntity moves to X=-29.303*, Z=77.524*, Y=-68.129*
  2: 0x014A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x014C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x014D [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x014E  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                            C0 28                .(
0150: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x014E [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0151 [0x00] END_REQSTACK()
```
