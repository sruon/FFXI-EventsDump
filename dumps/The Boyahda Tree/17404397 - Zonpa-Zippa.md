# 17404397 - Zonpa-Zippa

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | The Boyahda Tree (ID: 153) |
| Block Size       | 632 bytes                  |
| Total Events     | 27                         |
| References Count | 22                         |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0037       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0045       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0055       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0063       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0073       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0081       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0091       |     14 |              2 |
| [65535.11](#event-6553511) | 0x009F       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00AF       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00BD       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00CD       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00DB       |      9 |              3 |
| [65535.16](#event-6553516) | 0x00E4       |     29 |              3 |
| [65535.17](#event-6553517) | 0x0101       |     41 |              5 |
| [13](#event-13)            | 0x012A       |      1 |              1 |
| [65535.18](#event-6553518) | 0x012B       |     14 |              4 |
| [65535.19](#event-6553519) | 0x0139       |     15 |              5 |
| [65535.20](#event-6553520) | 0x0148       |     10 |              2 |
| [65535.21](#event-6553521) | 0x0152       |     15 |              5 |
| [65535.22](#event-6553522) | 0x0161       |     10 |              2 |
| [65535.23](#event-6553523) | 0x016B       |     14 |              4 |
| [65535.24](#event-6553524) | 0x0179       |     14 |              4 |
| [65535.25](#event-6553525) | 0x0187       |     29 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x025C      |         604 |
|       1 | 0x001E      |          30 |
|       2 | 0x0151      |         337 |
|       3 | 0x0159      |         345 |
|       4 | 0x0028      |          40 |
|       5 | 0x1946D     |      103533 |
|       6 | 0x224E1     |      140513 |
|       7 | 0x2134      |        8500 |
|       8 | 0x000D      |          13 |
|       9 | 0x199BB     |      104891 |
|      10 | 0x2249C     |      140444 |
|      11 | 0x2135      |        8501 |
|      12 | 0x078A      |        1930 |
|      13 | 0xFFFFFC78  |  4294966392 |
|      14 | 0xFFFF9BEB  |  4294941675 |
|      15 | 0xFFFFF15B  |  4294963547 |
|      16 | 0x0D56      |        3414 |
|      17 | 0xFFFFFC6C  |  4294966380 |
|      18 | 0xFFFF9D7F  |  4294942079 |
|      19 | 0x18F92     |      102290 |
|      20 | 0x225FC     |      140796 |
|      21 | 0x212B      |        8491 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 65 72 73 30   [..........ers0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ers0" with entities [EventEntity, EventEntity], work=604*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 65 72 73 30 5E 69   S........ers0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ers0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 65 72 73 31 00                              ..ers1.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ers1" with entities [EventEntity, EventEntity], work=604*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 65 72 73 31 00                                    ers1.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ers1" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                5B 00 80  F8 FF FF 7F F8 FF FF 7F       [..........
0050: 65 72 73 32 00                                    ers2.           
```

#### Opcodes

```
  0: 0x0045 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ers2" with entities [EventEntity, EventEntity], work=604*
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                53 F8 FF  FF 7F F8 FF FF 7F 65 72       S........er
0060: 73 32 00                                          s2.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ers2" with entities [EventEntity, EventEntity]
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 61 6B     [..........ak
0070: 72 30 00                                          r0.             
```

#### Opcodes

```
  0: 0x0063 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "akr0" with entities [EventEntity, EventEntity], work=604*
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          53 F8 FF FF 7F  F8 FF FF 7F 61 6B 72 30     S........akr0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "akr0" with entities [EventEntity, EventEntity]
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    5B 02 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   [..........thk1
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0081 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=337*
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 00      S........thk1. 
```

#### Opcodes

```
  0: 0x0091 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               5B                 [
00A0: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     ..........thk2. 
```

#### Opcodes

```
  0: 0x009F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=337*
  1: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               53                 S
00B0: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x00AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x00BC [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BD   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                         5B 02 80               [..
00C0: F8 FF FF 7F F8 FF FF 7F  70 61 73 30 00           ........pas0.   
```

#### Opcodes

```
  0: 0x00BD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=337*
  1: 0x00CC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CD   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         53 F8 FF               S..
00D0: FF 7F F8 FF FF 7F 70 61  73 30 00                 ......pas0.     
```

#### Opcodes

```
  0: 0x00CD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x00DA [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DB  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   5E 69 64 6C 30             ^idl0
00E0: 1C 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00DB [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00E0 [0x1C] WAIT(30* ticks)
  2: 0x00E3 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E4   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             5B 03 80 F8  FF FF 7F F8 FF FF 7F 6D      [..........m
00F0: 65 69 30 53 F8 FF FF 7F  F8 FF FF 7F 6D 65 69 30  ei0S........mei0
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00E4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mei0" with entities [EventEntity, EventEntity], work=345*
  1: 0x00F3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mei0" with entities [EventEntity, EventEntity]
  2: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    7C 00 F8 FF FF 7F 5B  03 80 F8 FF FF 7F F8 FF   |.....[........
0110: FF 7F 6D 65 69 31 53 F8  FF FF 7F F8 FF FF 7F 6D  ..mei1S........m
0120: 65 69 31 7C 01 F8 FF FF  7F 00                    ei1|......      
```

#### Opcodes

```
  0: 0x0101 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0107 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mei1" with entities [EventEntity, EventEntity], work=345*
  2: 0x0116 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mei1" with entities [EventEntity, EventEntity]
  3: 0x0123 [0x7C] EventEntity->Render.Flags2 |= 0x01
  4: 0x0129 [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x012A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                00                           .     
```

#### Opcodes

```
  0: 0x012A [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   32 04 80 1F 00             2....
0130: 05 80 06 80 07 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x012B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x012E [0x1F] MOVE_ENTITY: EventEntity moves to X=103.533*, Z=140.513*, Y=8.500*
  2: 0x0136 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0138 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0139   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             32 08 80 1F 00 09 80           2......
0140: 0A 80 0B 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0139 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x013C [0x1F] MOVE_ENTITY: EventEntity moves to X=104.891*, Z=140.444*, Y=8.501*
  2: 0x0144 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0146 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0147 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0148   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                          37 05 80 06 80 07 80 0C          7.......
0150: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0148 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=103.533*, z=140.513*, y=8.500*, direction=169.6°*
  1: 0x0151 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0152   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:       32 08 80 1F 00 05  80 06 80 07 80 1F 01 6F    2............o
0160: 00                                                .               
```

#### Opcodes

```
  0: 0x0152 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0155 [0x1F] MOVE_ENTITY: EventEntity moves to X=103.533*, Z=140.513*, Y=8.500*
  2: 0x015D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x015F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0160 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0161   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:    37 0D 80 0E 80 0F 80  10 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0161 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.904*, z=-25.621*, y=-3.749*, direction=300.0°*
  1: 0x016A [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                   32 08 80 1F 00             2....
0170: 11 80 12 80 0F 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x016B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x016E [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.916*, Z=-25.217*, Y=-3.749*
  2: 0x0176 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0178 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0179   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                             32 08 80 1F 00 05 80           2......
0180: 06 80 07 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0179 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x017C [0x1F] MOVE_ENTITY: EventEntity moves to X=103.533*, Z=140.513*, Y=8.500*
  2: 0x0184 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0186 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0187   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                      32  08 80 1F 00 13 80 14 80         2........
0190: 15 80 1F 01 6F 29 08 ED  91 09 01 0D 29 08 ED 91  ....o)......)...
01A0: 09 01 0E 00                                       ....            
```

#### Opcodes

```
  0: 0x0187 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x018A [0x1F] MOVE_ENTITY: EventEntity moves to X=102.290*, Z=140.796*, Y=8.491*
  2: 0x0192 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0194 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0195 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Zonpa-Zippa (ID: 17404397/0x010991ED), tag_num=0x0D)
  5: 0x019C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Zonpa-Zippa (ID: 17404397/0x010991ED), tag_num=0x0E)
  6: 0x01A3 [0x00] END_REQSTACK()
```
