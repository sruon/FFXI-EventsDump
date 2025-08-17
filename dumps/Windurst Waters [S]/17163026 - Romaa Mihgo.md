# 17163026 - Romaa Mihgo

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 980 bytes                    |
| Total Events     | 47                           |
| References Count | 10                           |

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
| [65535.9](#event-655359)   | 0x0079       |      9 |              3 |
| [65535.10](#event-6553510) | 0x0082       |     18 |              4 |
| [65535.11](#event-6553511) | 0x0094       |     27 |              3 |
| [65535.12](#event-6553512) | 0x00AF       |     27 |              3 |
| [65535.13](#event-6553513) | 0x00CA       |     27 |              3 |
| [65535.14](#event-6553514) | 0x00E5       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00F5       |     14 |              2 |
| [65535.16](#event-6553516) | 0x0103       |     16 |              2 |
| [65535.17](#event-6553517) | 0x0113       |     14 |              2 |
| [65535.18](#event-6553518) | 0x0121       |     16 |              2 |
| [65535.19](#event-6553519) | 0x0131       |     14 |              2 |
| [65535.20](#event-6553520) | 0x013F       |     16 |              2 |
| [65535.21](#event-6553521) | 0x014F       |     14 |              2 |
| [65535.22](#event-6553522) | 0x015D       |     16 |              2 |
| [65535.23](#event-6553523) | 0x016D       |     14 |              2 |
| [65535.24](#event-6553524) | 0x017B       |     22 |              3 |
| [65535.25](#event-6553525) | 0x0191       |     14 |              2 |
| [65535.26](#event-6553526) | 0x019F       |     16 |              2 |
| [65535.27](#event-6553527) | 0x01AF       |     20 |              3 |
| [65535.28](#event-6553528) | 0x01C3       |     16 |              2 |
| [65535.29](#event-6553529) | 0x01D3       |     14 |              2 |
| [65535.30](#event-6553530) | 0x01E1       |     16 |              2 |
| [65535.31](#event-6553531) | 0x01F1       |     14 |              2 |
| [65535.32](#event-6553532) | 0x01FF       |     16 |              2 |
| [65535.33](#event-6553533) | 0x020F       |     14 |              2 |
| [65535.34](#event-6553534) | 0x021D       |     16 |              2 |
| [65535.35](#event-6553535) | 0x022D       |     14 |              2 |
| [65535.36](#event-6553536) | 0x023B       |     16 |              2 |
| [65535.37](#event-6553537) | 0x024B       |     14 |              2 |
| [65535.38](#event-6553538) | 0x0259       |     16 |              2 |
| [65535.39](#event-6553539) | 0x0269       |     14 |              2 |
| [65535.40](#event-6553540) | 0x0277       |     16 |              2 |
| [65535.41](#event-6553541) | 0x0287       |     14 |              2 |
| [65535.42](#event-6553542) | 0x0295       |     22 |              3 |
| [65535.43](#event-6553543) | 0x02AB       |     14 |              2 |
| [65535.44](#event-6553544) | 0x02B9       |     16 |              2 |
| [65535.45](#event-6553545) | 0x02C9       |     20 |              3 |
| [530](#event-530)          | 0x02DD       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003B      |          59 |
|       1 | 0x003C      |          60 |
|       2 | 0x0019      |          25 |
|       3 | 0x052F      |        1327 |
|       4 | 0x0530      |        1328 |
|       5 | 0x0563      |        1379 |
|       6 | 0x05F9      |        1529 |
|       7 | 0x096E      |        2414 |
|       8 | 0x096F      |        2415 |
|       9 | 0x0906      |        2310 |

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
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
  0: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
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
0030:                                         66 00 80               f..
0040: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 00           ........thk1.   
```

#### Opcodes

```
  0: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=59*
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
0050: FF 7F F8 FF FF 7F 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
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
0050:                                   66 00 80 F8 FF             f....
0060: FF 7F F8 FF FF 7F 74 68  6B 32 00                 ......thk2.     
```

#### Opcodes

```
  0: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=59*
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
0070: F8 FF FF 7F 74 68 6B 32  00                       ....thk2.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0079  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             5E 69 64 6C 30 1C 01           ^idl0..
0080: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0079 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x007E [0x1C] WAIT(60* ticks)
  2: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       6E F8 FF FF 7F 02  80 99 F8 FF FF 7F 99 F8    n.............
0090: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0082 [0x6E] EventEntity uses emote 25*
  1: 0x0089 [0x99] Wait for EventEntity animation to complete
  2: 0x008E [0x99] Wait for EventEntity animation to complete
  3: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             2C F8 FF FF  7F F8 FF FF 7F 72 65 73      ,........res
00A0: 30 53 F8 FF FF 7F F8 FF  FF 7F 72 65 73 30 00     0S........res0. 
```

#### Opcodes

```
  0: 0x0094 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [EventEntity, EventEntity]
  1: 0x00A1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res0" with entities [EventEntity, EventEntity]
  2: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               2C                 ,
00B0: F8 FF FF 7F F8 FF FF 7F  72 65 73 31 53 F8 FF FF  ........res1S...
00C0: 7F F8 FF FF 7F 72 65 73  31 00                    .....res1.      
```

#### Opcodes

```
  0: 0x00AF [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res1" with entities [EventEntity, EventEntity]
  1: 0x00BC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res1" with entities [EventEntity, EventEntity]
  2: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                2C F8 FF FF 7F F8            ,.....
00D0: FF FF 7F 72 65 73 32 53  F8 FF FF 7F F8 FF FF 7F  ...res2S........
00E0: 72 65 73 32 00                                    res2.           
```

#### Opcodes

```
  0: 0x00CA [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res2" with entities [EventEntity, EventEntity]
  1: 0x00D7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res2" with entities [EventEntity, EventEntity]
  2: 0x00E4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                5B 03 80  F8 FF FF 7F F8 FF FF 7F       [..........
00F0: 73 74 61 30 00                                    sta0.           
```

#### Opcodes

```
  0: 0x00E5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sta0" with entities [EventEntity, EventEntity], work=1327*
  1: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                53 F8 FF  FF 7F F8 FF FF 7F 73 74       S........st
0100: 61 30 00                                          a0.             
```

#### Opcodes

```
  0: 0x00F5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sta0" with entities [EventEntity, EventEntity]
  1: 0x0102 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0103   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          5B 03 80 F8 FF  FF 7F F8 FF FF 7F 73 74     [..........st
0110: 61 31 00                                          a1.             
```

#### Opcodes

```
  0: 0x0103 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sta1" with entities [EventEntity, EventEntity], work=1327*
  1: 0x0112 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0113   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          53 F8 FF FF 7F  F8 FF FF 7F 73 74 61 31     S........sta1
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0113 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sta1" with entities [EventEntity, EventEntity]
  1: 0x0120 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0121   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    5B 03 80 F8 FF FF 7F  F8 FF FF 7F 73 74 62 30   [..........stb0
0130: 00                                                .               
```

#### Opcodes

```
  0: 0x0121 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "stb0" with entities [EventEntity, EventEntity], work=1327*
  1: 0x0130 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0131   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:    53 F8 FF FF 7F F8 FF  FF 7F 73 74 62 30 00      S........stb0. 
```

#### Opcodes

```
  0: 0x0131 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "stb0" with entities [EventEntity, EventEntity]
  1: 0x013E [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                               5B                 [
0140: 03 80 F8 FF FF 7F F8 FF  FF 7F 73 74 62 31 00     ..........stb1. 
```

#### Opcodes

```
  0: 0x013F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "stb1" with entities [EventEntity, EventEntity], work=1327*
  1: 0x014E [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                               53                 S
0150: F8 FF FF 7F F8 FF FF 7F  73 74 62 31 00           ........stb1.   
```

#### Opcodes

```
  0: 0x014F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "stb1" with entities [EventEntity, EventEntity]
  1: 0x015C [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                         5B 03 80               [..
0160: F8 FF FF 7F F8 FF FF 7F  6E 79 61 30 00           ........nya0.   
```

#### Opcodes

```
  0: 0x015D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nya0" with entities [EventEntity, EventEntity], work=1327*
  1: 0x016C [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                         53 F8 FF               S..
0170: FF 7F F8 FF FF 7F 6E 79  61 30 00                 ......nya0.     
```

#### Opcodes

```
  0: 0x016D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "nya0" with entities [EventEntity, EventEntity]
  1: 0x017A [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017B   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                   81 00 F8 FF FF             .....
0180: 7F 5B 04 80 F8 FF FF 7F  F8 FF FF 7F 69 72 6F 30  .[..........iro0
0190: 00                                                .               
```

#### Opcodes

```
  0: 0x017B [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0181 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=1328*
  2: 0x0190 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0191   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:    53 F8 FF FF 7F F8 FF  FF 7F 69 72 6F 30 00      S........iro0. 
```

#### Opcodes

```
  0: 0x0191 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro0" with entities [EventEntity, EventEntity]
  1: 0x019E [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                               5B                 [
01A0: 04 80 F8 FF FF 7F F8 FF  FF 7F 69 72 6F 31 00     ..........iro1. 
```

#### Opcodes

```
  0: 0x019F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "iro1" with entities [EventEntity, EventEntity], work=1328*
  1: 0x01AE [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AF   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                               53                 S
01B0: F8 FF FF 7F F8 FF FF 7F  69 72 6F 31 81 01 F8 FF  ........iro1....
01C0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x01AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro1" with entities [EventEntity, EventEntity]
  1: 0x01BC [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x01C2 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:          5B 05 80 F8 FF  FF 7F F8 FF FF 7F 72 6D     [..........rm
01D0: 6C 30 00                                          l0.             
```

#### Opcodes

```
  0: 0x01C3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rml0" with entities [EventEntity, EventEntity], work=1379*
  1: 0x01D2 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:          53 F8 FF FF 7F  F8 FF FF 7F 72 6D 6C 30     S........rml0
01E0: 00                                                .               
```

#### Opcodes

```
  0: 0x01D3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "rml0" with entities [EventEntity, EventEntity]
  1: 0x01E0 [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:    5B 06 80 F8 FF FF 7F  F8 FF FF 7F 73 64 6F 6E   [..........sdon
01F0: 00                                                .               
```

#### Opcodes

```
  0: 0x01E1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sdon" with entities [EventEntity, EventEntity], work=1529*
  1: 0x01F0 [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:    53 F8 FF FF 7F F8 FF  FF 7F 73 64 6F 6E 00      S........sdon. 
```

#### Opcodes

```
  0: 0x01F1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sdon" with entities [EventEntity, EventEntity]
  1: 0x01FE [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01FF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                               5B                 [
0200: 06 80 F8 FF FF 7F F8 FF  FF 7F 73 64 6F 66 00     ..........sdof. 
```

#### Opcodes

```
  0: 0x01FF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sdof" with entities [EventEntity, EventEntity], work=1529*
  1: 0x020E [0x00] END_REQSTACK()
```

### Event 65535.33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x020F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                               53                 S
0210: F8 FF FF 7F F8 FF FF 7F  73 64 6F 66 00           ........sdof.   
```

#### Opcodes

```
  0: 0x020F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sdof" with entities [EventEntity, EventEntity]
  1: 0x021C [0x00] END_REQSTACK()
```

### Event 65535.34

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x021D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                                         5B 07 80               [..
0220: F8 FF FF 7F F8 FF FF 7F  65 68 6E 30 00           ........ehn0.   
```

#### Opcodes

```
  0: 0x021D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ehn0" with entities [EventEntity, EventEntity], work=2414*
  1: 0x022C [0x00] END_REQSTACK()
```

### Event 65535.35

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                         53 F8 FF               S..
0230: FF 7F F8 FF FF 7F 65 68  6E 30 00                 ......ehn0.     
```

#### Opcodes

```
  0: 0x022D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehn0" with entities [EventEntity, EventEntity]
  1: 0x023A [0x00] END_REQSTACK()
```

### Event 65535.36

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x023B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                                   5B 07 80 F8 FF             [....
0240: FF 7F F8 FF FF 7F 6E 72  69 30 00                 ......nri0.     
```

#### Opcodes

```
  0: 0x023B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nri0" with entities [EventEntity, EventEntity], work=2414*
  1: 0x024A [0x00] END_REQSTACK()
```

### Event 65535.37

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                   53 F8 FF FF 7F             S....
0250: F8 FF FF 7F 6E 72 69 30  00                       ....nri0.       
```

#### Opcodes

```
  0: 0x024B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "nri0" with entities [EventEntity, EventEntity]
  1: 0x0258 [0x00] END_REQSTACK()
```

### Event 65535.38

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0259   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:                             5B 08 80 F8 FF FF 7F           [......
0260: F8 FF FF 7F 64 6B 69 30  00                       ....dki0.       
```

#### Opcodes

```
  0: 0x0259 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dki0" with entities [EventEntity, EventEntity], work=2415*
  1: 0x0268 [0x00] END_REQSTACK()
```

### Event 65535.39

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0269   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                             53 F8 FF FF 7F F8 FF           S......
0270: FF 7F 64 6B 69 30 00                              ..dki0.         
```

#### Opcodes

```
  0: 0x0269 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dki0" with entities [EventEntity, EventEntity]
  1: 0x0276 [0x00] END_REQSTACK()
```

### Event 65535.40

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0277   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                      5B  08 80 F8 FF FF 7F F8 FF         [........
0280: FF 7F 64 6B 69 31 00                              ..dki1.         
```

#### Opcodes

```
  0: 0x0277 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dki1" with entities [EventEntity, EventEntity], work=2415*
  1: 0x0286 [0x00] END_REQSTACK()
```

### Event 65535.41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0287   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0280:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0290: 64 6B 69 31 00                                    dki1.           
```

#### Opcodes

```
  0: 0x0287 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dki1" with entities [EventEntity, EventEntity]
  1: 0x0294 [0x00] END_REQSTACK()
```

### Event 65535.42

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0295   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:                81 00 F8  FF FF 7F 5B 09 80 F8 FF       ......[....
02A0: FF 7F F8 FF FF 7F 61 61  6E 30 00                 ......aan0.     
```

#### Opcodes

```
  0: 0x0295 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x029B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "aan0" with entities [EventEntity, EventEntity], work=2310*
  2: 0x02AA [0x00] END_REQSTACK()
```

### Event 65535.43

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02AB   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02A0:                                   53 F8 FF FF 7F             S....
02B0: F8 FF FF 7F 61 61 6E 30  00                       ....aan0.       
```

#### Opcodes

```
  0: 0x02AB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "aan0" with entities [EventEntity, EventEntity]
  1: 0x02B8 [0x00] END_REQSTACK()
```

### Event 65535.44

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02B9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                             5B 09 80 F8 FF FF 7F           [......
02C0: F8 FF FF 7F 61 61 6E 31  00                       ....aan1.       
```

#### Opcodes

```
  0: 0x02B9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "aan1" with entities [EventEntity, EventEntity], work=2310*
  1: 0x02C8 [0x00] END_REQSTACK()
```

### Event 65535.45

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02C9   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:                             53 F8 FF FF 7F F8 FF           S......
02D0: FF 7F 61 61 6E 31 81 01  F8 FF FF 7F 00           ..aan1.......   
```

#### Opcodes

```
  0: 0x02C9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "aan1" with entities [EventEntity, EventEntity]
  1: 0x02D6 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x02DC [0x00] END_REQSTACK()
```

### Event 530

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02DD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02D0:                                         00                     .  
```

#### Opcodes

```
  0: 0x02DD [0x00] END_REQSTACK()
```
