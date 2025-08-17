# 17473713 - Queen of Wands

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 608 bytes                    |
| Total Events     | 28                           |
| References Count | 13                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      6 |              2 |
| [65535.2](#event-655352)   | 0x0007       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0017       |     14 |              2 |
| [65535.4](#event-655354)   | 0x0025       |     16 |              2 |
| [65535.5](#event-655355)   | 0x0035       |     14 |              2 |
| [65535.6](#event-655356)   | 0x0043       |     16 |              2 |
| [65535.7](#event-655357)   | 0x0053       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0061       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0071       |     14 |              2 |
| [65535.10](#event-6553510) | 0x007F       |     16 |              2 |
| [65535.11](#event-6553511) | 0x008F       |     14 |              2 |
| [65535.12](#event-6553512) | 0x009D       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00AD       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00BB       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00CB       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00D9       |     16 |              2 |
| [65535.17](#event-6553517) | 0x00E9       |     14 |              2 |
| [65535.18](#event-6553518) | 0x00F7       |     29 |              3 |
| [65535.19](#event-6553519) | 0x0114       |     16 |              2 |
| [61](#event-61)            | 0x0124       |     16 |              3 |
| [65535.20](#event-6553520) | 0x0134       |     30 |              6 |
| [62](#event-62)            | 0x0152       |      1 |              1 |
| [65535.21](#event-6553521) | 0x0153       |     43 |              9 |
| [65535.22](#event-6553522) | 0x017E       |     43 |              7 |
| [32000](#event-32000)      | 0x01A9       |      1 |              1 |
| [32004](#event-32004)      | 0x01AA       |      1 |              1 |
| [32001](#event-32001)      | 0x01AB       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00B5      |         181 |
|       1 | 0x00B6      |         182 |
|       2 | 0xFFFF1BFE  |  4294908926 |
|       3 | 0x5096      |       20630 |
|       4 | 0x2740      |       10048 |
|       5 | 0x0C00      |        3072 |
|       6 | 0x000D      |          13 |
|       7 | 0x1F40      |        8000 |
|       8 | 0x01F4      |         500 |
|       9 | 0x0028      |          40 |
|      10 | 0xFFFF1CB5  |  4294909109 |
|      11 | 0x9779      |       38777 |
|      12 | 0x24CC      |        9420 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5E 69 64 6C 30 00                               ^idl0.         
```

#### Opcodes

```
  0: 0x0001 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0010: FF 7F 6B 61 61 30 00                              ..kaa0.         
```

#### Opcodes

```
  0: 0x0007 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kaa0" with entities [EventEntity, EventEntity], work=181*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0020: 6B 61 61 30 00                                    kaa0.           
```

#### Opcodes

```
  0: 0x0017 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kaa0" with entities [EventEntity, EventEntity]
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                5B 00 80  F8 FF FF 7F F8 FF FF 7F       [..........
0030: 6B 61 61 31 00                                    kaa1.           
```

#### Opcodes

```
  0: 0x0025 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kaa1" with entities [EventEntity, EventEntity], work=181*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                53 F8 FF  FF 7F F8 FF FF 7F 6B 61       S........ka
0040: 61 31 00                                          a1.             
```

#### Opcodes

```
  0: 0x0035 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kaa1" with entities [EventEntity, EventEntity]
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 6B 61     [..........ka
0050: 62 30 00                                          b0.             
```

#### Opcodes

```
  0: 0x0043 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kab0" with entities [EventEntity, EventEntity], work=181*
  1: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          53 F8 FF FF 7F  F8 FF FF 7F 6B 61 62 30     S........kab0
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0053 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kab0" with entities [EventEntity, EventEntity]
  1: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6B 61 62 31   [..........kab1
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0061 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kab1" with entities [EventEntity, EventEntity], work=181*
  1: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    53 F8 FF FF 7F F8 FF  FF 7F 6B 61 62 31 00      S........kab1. 
```

#### Opcodes

```
  0: 0x0071 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kab1" with entities [EventEntity, EventEntity]
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               5B                 [
0080: 00 80 F8 FF FF 7F F8 FF  FF 7F 6B 61 63 30 00     ..........kac0. 
```

#### Opcodes

```
  0: 0x007F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kac0" with entities [EventEntity, EventEntity], work=181*
  1: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               53                 S
0090: F8 FF FF 7F F8 FF FF 7F  6B 61 63 30 00           ........kac0.   
```

#### Opcodes

```
  0: 0x008F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kac0" with entities [EventEntity, EventEntity]
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         5B 00 80               [..
00A0: F8 FF FF 7F F8 FF FF 7F  6B 61 63 31 00           ........kac1.   
```

#### Opcodes

```
  0: 0x009D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kac1" with entities [EventEntity, EventEntity], work=181*
  1: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         53 F8 FF               S..
00B0: FF 7F F8 FF FF 7F 6B 61  63 30 00                 ......kac0.     
```

#### Opcodes

```
  0: 0x00AD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kac0" with entities [EventEntity, EventEntity]
  1: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   5B 00 80 F8 FF             [....
00C0: FF 7F F8 FF FF 7F 64 65  64 30 00                 ......ded0.     
```

#### Opcodes

```
  0: 0x00BB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ded0" with entities [EventEntity, EventEntity], work=181*
  1: 0x00CA [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CB   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                   53 F8 FF FF 7F             S....
00D0: F8 FF FF 7F 64 65 64 30  00                       ....ded0.       
```

#### Opcodes

```
  0: 0x00CB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ded0" with entities [EventEntity, EventEntity]
  1: 0x00D8 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                             5B 01 80 F8 FF FF 7F           [......
00E0: F8 FF FF 7F 61 77 6B 30  00                       ....awk0.       
```

#### Opcodes

```
  0: 0x00D9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "awk0" with entities [EventEntity, EventEntity], work=182*
  1: 0x00E8 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E9   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                             53 F8 FF FF 7F F8 FF           S......
00F0: FF 7F 61 77 6B 30 00                              ..awk0.         
```

#### Opcodes

```
  0: 0x00E9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "awk0" with entities [EventEntity, EventEntity]
  1: 0x00F6 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F7   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      5B  01 80 F8 FF FF 7F F8 FF         [........
0100: FF 7F 64 77 6E 30 53 F8  FF FF 7F F8 FF FF 7F 64  ..dwn0S........d
0110: 77 6E 30 00                                       wn0.            
```

#### Opcodes

```
  0: 0x00F7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dwn0" with entities [EventEntity, EventEntity], work=182*
  1: 0x0106 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dwn0" with entities [EventEntity, EventEntity]
  2: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             5B 01 80 F8  FF FF 7F F8 FF FF 7F 73      [..........s
0120: 63 6B 30 00                                       ck0.            
```

#### Opcodes

```
  0: 0x0114 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sck0" with entities [EventEntity, EventEntity], work=182*
  1: 0x0123 [0x00] END_REQSTACK()
```

### Event 61

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0124   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:             92 01 F8 FF  FF 7F 37 02 80 03 80 04      ......7.....
0130: 80 05 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0124 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x012A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-58.370*, z=20.630*, y=10.048*, direction=270.0°*
  2: 0x0133 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0134   |
| Data Size    | 30 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:             32 06 80 3B  F8 FF FF 7F 00 00 02 00      2..;........
0140: 01 00 07 02 00 07 80 1F  00 00 00 02 00 01 00 1F  ................
0150: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0134 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0137 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[1])
  2: 0x0142 [0x07] ExtData[1]->WorkLocal[2] += 8000*
  3: 0x0147 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  4: 0x014F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0151 [0x00] END_REQSTACK()
```

### Event 62

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0152  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:       00                                            .             
```

#### Opcodes

```
  0: 0x0152 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0153   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:          32 06 80 3B F8  FF FF 7F 00 00 02 00 01     2..;.........
0160: 00 08 00 00 08 80 08 02  00 08 80 1F 00 00 00 02  ................
0170: 00 01 00 1F 01 6F 29 08  B1 A0 0A 01 02 00        .....o).......  
```

#### Opcodes

```
  0: 0x0153 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0156 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[1])
  2: 0x0161 [0x08] ExtData[1]->WorkLocal[0] -= 500*
  3: 0x0166 [0x08] ExtData[1]->WorkLocal[2] -= 500*
  4: 0x016B [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  5: 0x0173 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0175 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0176 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Queen of Wands (ID: 17473713/0x010AA0B1), tag_num=0x02)
  8: 0x017D [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017E   |
| Data Size    | 43 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                            32 09                2.
0180: 80 1F 00 0A 80 0B 80 0C  80 1F 01 6F 5B 00 80 F8  ...........o[...
0190: FF FF 7F F8 FF FF 7F 64  65 64 30 53 F8 FF FF 7F  .......ded0S....
01A0: F8 FF FF 7F 64 65 64 30  00                       ....ded0.       
```

#### Opcodes

```
  0: 0x017E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0181 [0x1F] MOVE_ENTITY: EventEntity moves to X=-58.187*, Z=38.777*, Y=9.420*
  2: 0x0189 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x018B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x018C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ded0" with entities [EventEntity, EventEntity], work=181*
  5: 0x019B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ded0" with entities [EventEntity, EventEntity]
  6: 0x01A8 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01A9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                             00                             .      
```

#### Opcodes

```
  0: 0x01A9 [0x00] END_REQSTACK()
```

### Event 32004

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01AA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                00                           .     
```

#### Opcodes

```
  0: 0x01AA [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01AB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                   00                         .    
```

#### Opcodes

```
  0: 0x01AB [0x00] END_REQSTACK()
```
