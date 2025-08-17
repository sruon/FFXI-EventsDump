# 17826101 - Lhaiso Neftereh

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 684 bytes                 |
| Total Events     | 31                        |
| References Count | 29                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x005B       |     16 |              2 |
| [65535.8](#event-655358)   | 0x006B       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0079       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0089       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0097       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00A7       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00B5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00C5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00D3       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00E3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00F1       |     16 |              4 |
| [65535.18](#event-6553518) | 0x0101       |     16 |              4 |
| [65535.19](#event-6553519) | 0x0111       |     16 |              4 |
| [54](#event-54)            | 0x0121       |      1 |              1 |
| [65535.20](#event-6553520) | 0x0122       |     16 |              3 |
| [65535.21](#event-6553521) | 0x0132       |      8 |              3 |
| [65535.22](#event-6553522) | 0x013A       |     14 |              4 |
| [65535.23](#event-6553523) | 0x0148       |     14 |              4 |
| [65535.24](#event-6553524) | 0x0156       |     14 |              4 |
| [65535.25](#event-6553525) | 0x0164       |     16 |              5 |
| [65](#event-65)            | 0x0174       |      1 |              1 |
| [65535.26](#event-6553526) | 0x0175       |     10 |              2 |
| [65535.27](#event-6553527) | 0x017F       |     29 |              9 |
| [65535.28](#event-6553528) | 0x019C       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C7      |         199 |
|       1 | 0x007F      |         127 |
|       2 | 0x003B      |          59 |
|       3 | 0x0006      |           6 |
|       4 | 0x003C      |          60 |
|       5 | 0x0018      |          24 |
|       6 | 0x0082      |         130 |
|       7 | 0x0013      |          19 |
|       8 | 0x10C03     |       68611 |
|       9 | 0x21028     |      135208 |
|      10 | 0x7CFF      |       31999 |
|      11 | 0x01CF      |         463 |
|      12 | 0x000D      |          13 |
|      13 | 0x123CD     |       74701 |
|      14 | 0x213C7     |      136135 |
|      15 | 0x123EE     |       74734 |
|      16 | 0x20C1C     |      134172 |
|      17 | 0x7CF4      |       31988 |
|      18 | 0x12611     |       75281 |
|      19 | 0x21142     |      135490 |
|      20 | 0x10E96     |       69270 |
|      21 | 0x216D7     |      136919 |
|      22 | 0x106E5     |       67301 |
|      23 | 0x2111C     |      135452 |
|      24 | 0x7D00      |       32000 |
|      25 | 0x0FA6      |        4006 |
|      26 | 0x0028      |          40 |
|      27 | 0x126D2     |       75474 |
|      28 | 0x21006     |      135174 |

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=199*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00      S........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               66                 f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 00     ..........tlk1. 
```

#### Opcodes

```
  0: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=199*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         66 01 80               f..
0040: F8 FF FF 7F F8 FF FF 7F  70 61 73 30 00           ........pas0.   
```

#### Opcodes

```
  0: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=127*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         53 F8 FF               S..
0050: FF 7F F8 FF FF 7F 70 61  73 30 00                 ......pas0.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   66 01 80 F8 FF             f....
0060: FF 7F F8 FF FF 7F 73 69  6E 62 00                 ......sinb.     
```

#### Opcodes

```
  0: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sinb" with entities [EventEntity, EventEntity], work=127*
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   53 F8 FF FF 7F             S....
0070: F8 FF FF 7F 73 69 6E 62  00                       ....sinb.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sinb" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             66 02 80 F8 FF FF 7F           f......
0080: F8 FF FF 7F 74 6C 6B 30  00                       ....tlk0.       
```

#### Opcodes

```
  0: 0x0079 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             53 F8 FF FF 7F F8 FF           S......
0090: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x0089 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      66  02 80 F8 FF FF 7F F8 FF         f........
00A0: FF 7F 74 6C 6B 31 00                              ..tlk1.         
```

#### Opcodes

```
  0: 0x0097 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00B0: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x00A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                66 02 80  F8 FF FF 7F F8 FF FF 7F       f..........
00C0: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x00B5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=59*
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                53 F8 FF  FF 7F F8 FF FF 7F 74 68       S........th
00D0: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x00C5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          66 02 80 F8 FF  FF 7F F8 FF FF 7F 74 68     f..........th
00E0: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x00D3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=59*
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32     S........thk2
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    6E F8 FF FF 7F 03 80  99 F8 FF FF 7F 1C 04 80   n..............
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00F1 [0x6E] EventEntity uses emote 6*
  1: 0x00F8 [0x99] Wait for EventEntity animation to complete
  2: 0x00FD [0x1C] WAIT(60* ticks)
  3: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    6E F8 FF FF 7F 05 80  99 F8 FF FF 7F 1C 06 80   n..............
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0101 [0x6E] EventEntity uses emote 24*
  1: 0x0108 [0x99] Wait for EventEntity animation to complete
  2: 0x010D [0x1C] WAIT(130* ticks)
  3: 0x0110 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0111   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    6E F8 FF FF 7F 07 80  99 F8 FF FF 7F 1C 04 80   n..............
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0111 [0x6E] EventEntity uses emote 19*
  1: 0x0118 [0x99] Wait for EventEntity animation to complete
  2: 0x011D [0x1C] WAIT(60* ticks)
  3: 0x0120 [0x00] END_REQSTACK()
```

### Event 54

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0121  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    00                                              .              
```

#### Opcodes

```
  0: 0x0121 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0122   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:       2F 00 F8 FF FF 7F  37 08 80 09 80 0A 80 0B    /.....7.......
0130: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0122 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0128 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=68.611*, z=135.208*, y=31.999*, direction=40.7°*
  2: 0x0131 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0132  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:       22 00 80 35 01 10  01 00                      "..5....      
```

#### Opcodes

```
  0: 0x0132 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0134 [0x80] LOAD_WAIT(entity=Lhaiso Neftereh (ID: 17826101/0x01100135))
  2: 0x0139 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                32 0C 80 1F 00 0D            2.....
0140: 80 0E 80 0A 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x013A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x013D [0x1F] MOVE_ENTITY: EventEntity moves to X=74.701*, Z=136.135*, Y=31.999*
  2: 0x0145 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0147 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0148   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                          32 0C 80 1F 00 0F 80 10          2.......
0150: 80 11 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0148 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x014B [0x1F] MOVE_ENTITY: EventEntity moves to X=74.734*, Z=134.172*, Y=31.988*
  2: 0x0153 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0155 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   32 0C  80 1F 00 12 80 13 80 0A        2.........
0160: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0156 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0159 [0x1F] MOVE_ENTITY: EventEntity moves to X=75.281*, Z=135.490*, Y=31.999*
  2: 0x0161 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0163 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0164   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:             32 0C 80 1F  00 14 80 15 80 0A 80 1F      2...........
0170: 01 22 01 00                                       ."..            
```

#### Opcodes

```
  0: 0x0164 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0167 [0x1F] MOVE_ENTITY: EventEntity moves to X=69.270*, Z=136.919*, Y=31.999*
  2: 0x016F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0171 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x0173 [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0174  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:             00                                        .           
```

#### Opcodes

```
  0: 0x0174 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0175   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                37 16 80  17 80 18 80 19 80 00          7......... 
```

#### Opcodes

```
  0: 0x0175 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=67.301*, z=135.452*, y=32.000*, direction=352.1°*
  1: 0x017E [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017F   |
| Data Size    | 29 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                               2F                 /
0180: 00 F8 FF FF 7F 22 00 32  1A 80 1F 00 1B 80 1C 80  .....".2........
0190: 0A 80 1F 01 1E 8A 00 10  01 6F 70 00              .........op.    
```

#### Opcodes

```
  0: 0x017F [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0185 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0187 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x018A [0x1F] MOVE_ENTITY: EventEntity moves to X=75.474*, Z=135.174*, Y=31.999*
  4: 0x0192 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0194 [0x1E] EventEntity looks at Sylvie (ID: 17825930/0x0110008A) and starts talking
  6: 0x0199 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x019A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x019B [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                      32 0C 80 1F              2...
01A0: 00 16 80 17 80 18 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x019C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x019F [0x1F] MOVE_ENTITY: EventEntity moves to X=67.301*, Z=135.452*, Y=32.000*
  2: 0x01A7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01A9 [0x00] END_REQSTACK()
```
