# 17388030 - Rochefogne

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Davoi (ID: 149) |
| Block Size       | 688 bytes       |
| Total Events     | 35              |
| References Count | 19              |

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
| [65535.15](#event-6553515) | 0x00DB       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00EB       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00F9       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0109       |     14 |              2 |
| [65535.19](#event-6553519) | 0x0117       |      9 |              3 |
| [65535.20](#event-6553520) | 0x0120       |     16 |              2 |
| [65535.21](#event-6553521) | 0x0130       |     14 |              2 |
| [65535.22](#event-6553522) | 0x013E       |     16 |              2 |
| [65535.23](#event-6553523) | 0x014E       |     14 |              2 |
| [65535.24](#event-6553524) | 0x015C       |     16 |              2 |
| [65535.25](#event-6553525) | 0x016C       |     14 |              2 |
| [65535.26](#event-6553526) | 0x017A       |     16 |              2 |
| [116](#event-116)          | 0x018A       |      1 |              1 |
| [65535.27](#event-6553527) | 0x018B       |     10 |              2 |
| [65535.28](#event-6553528) | 0x0195       |     14 |              4 |
| [65535.29](#event-6553529) | 0x01A3       |     14 |              4 |
| [65535.30](#event-6553530) | 0x01B1       |      5 |              3 |
| [65535.31](#event-6553531) | 0x01B6       |      5 |              3 |
| [65535.32](#event-6553532) | 0x01BB       |      5 |              3 |
| [65535.33](#event-6553533) | 0x01C0       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x001E      |          30 |
|       2 | 0x001D      |          29 |
|       3 | 0x0015      |          21 |
|       4 | 0x358F0     |      219376 |
|       5 | 0xFFFF1412  |  4294906898 |
|       6 | 0x0ABD      |        2749 |
|       7 | 0x0C5C      |        3164 |
|       8 | 0x000D      |          13 |
|       9 | 0x35B69     |      220009 |
|      10 | 0xFFFF2E29  |  4294913577 |
|      11 | 0x07A5      |        1957 |
|      12 | 0x357CF     |      219087 |
|      13 | 0xFFFF4738  |  4294919992 |
|      14 | 0x0147      |         327 |
|      15 | 0x1D55      |        7509 |
|      16 | 0x1D57      |        7511 |
|      17 | 0x1D58      |        7512 |
|      18 | 0x1D5A      |        7514 |

## String References

- **7509**: I assumed that because the Orcs, too, were searching for something that...
- **7511**: ...I must inquire with my sister.
- **7512**: At her coming-of-age, she learned all there was to know of that sword from our father.
- **7514**: Will you lend me a hand, Vauderame? I know my sister has left something for me, and I intend to find it.

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
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
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
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
0020:                      66  02 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
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
0040: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
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
0040:                66 02 80  F8 FF FF 7F F8 FF FF 7F       f..........
0050: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
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
0050:                53 F8 FF  FF 7F F8 FF FF 7F 74 68       S........th
0060: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
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
0060:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 70 61     f..........pa
0070: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
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
0070:          53 F8 FF FF 7F  F8 FF FF 7F 70 61 73 30     S........pas0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
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
0080:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 31   f..........poi1
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=20*
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
0090:    53 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 31 00      S........poi1. 
```

#### Opcodes

```
  0: 0x0091 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
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
0090:                                               66                 f
00A0: 00 80 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 32 00     ..........poi2. 
```

#### Opcodes

```
  0: 0x009F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi2" with entities [EventEntity, EventEntity], work=20*
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
00B0: F8 FF FF 7F F8 FF FF 7F  70 6F 69 32 00           ........poi2.   
```

#### Opcodes

```
  0: 0x00AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi2" with entities [EventEntity, EventEntity]
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
00B0:                                         66 03 80               f..
00C0: F8 FF FF 7F F8 FF FF 7F  70 6F 69 30 00           ........poi0.   
```

#### Opcodes

```
  0: 0x00BD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=21*
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
00D0: FF 7F F8 FF FF 7F 70 6F  69 30 00                 ......poi0.     
```

#### Opcodes

```
  0: 0x00CD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x00DA [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DB   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   66 03 80 F8 FF             f....
00E0: FF 7F F8 FF FF 7F 70 6F  69 31 00                 ......poi1.     
```

#### Opcodes

```
  0: 0x00DB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=21*
  1: 0x00EA [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EB   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                   53 F8 FF FF 7F             S....
00F0: F8 FF FF 7F 70 6F 69 31  00                       ....poi1.       
```

#### Opcodes

```
  0: 0x00EB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
  1: 0x00F8 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                             66 03 80 F8 FF FF 7F           f......
0100: F8 FF FF 7F 64 69 73 30  00                       ....dis0.       
```

#### Opcodes

```
  0: 0x00F9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=21*
  1: 0x0108 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0109   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                             53 F8 FF FF 7F F8 FF           S......
0110: FF 7F 64 69 73 30 00                              ..dis0.         
```

#### Opcodes

```
  0: 0x0109 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x0116 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0117  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      5E  69 64 6C 30 1C 01 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0117 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x011C [0x1C] WAIT(30* ticks)
  2: 0x011F [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 66 02 80 F8 FF FF 7F F8  FF FF 7F 73 68 61 30 00  f..........sha0.
```

#### Opcodes

```
  0: 0x0120 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  1: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 53 F8 FF FF 7F F8 FF FF  7F 73 68 61 30 00        S........sha0.  
```

#### Opcodes

```
  0: 0x0130 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  1: 0x013D [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            66 02                f.
0140: 80 F8 FF FF 7F F8 FF FF  7F 73 68 61 31 00        .........sha1.  
```

#### Opcodes

```
  0: 0x013E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  1: 0x014D [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                            53 F8                S.
0150: FF FF 7F F8 FF FF 7F 73  68 61 31 00              .......sha1.    
```

#### Opcodes

```
  0: 0x014E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  1: 0x015B [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                      66 02 80 F8              f...
0160: FF FF 7F F8 FF FF 7F 73  69 72 30 00              .......sir0.    
```

#### Opcodes

```
  0: 0x015C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir0" with entities [EventEntity, EventEntity], work=29*
  1: 0x016B [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                      53 F8 FF FF              S...
0170: 7F F8 FF FF 7F 73 69 72  30 00                    .....sir0.      
```

#### Opcodes

```
  0: 0x016C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sir0" with entities [EventEntity, EventEntity]
  1: 0x0179 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                66 02 80 F8 FF FF            f.....
0180: 7F F8 FF FF 7F 73 69 72  31 00                    .....sir1.      
```

#### Opcodes

```
  0: 0x017A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0189 [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x018A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                00                           .     
```

#### Opcodes

```
  0: 0x018A [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                   37 04 80 05 80             7....
0190: 06 80 07 80 00                                    .....           
```

#### Opcodes

```
  0: 0x018B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=219.376*, z=-60.398*, y=2.749*, direction=278.1°*
  1: 0x0194 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0195   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                32 08 80  1F 00 09 80 0A 80 0B 80       2..........
01A0: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0195 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0198 [0x1F] MOVE_ENTITY: EventEntity moves to X=220.009*, Z=-53.719*, Y=1.957*
  2: 0x01A0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01A2 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A3   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:          32 08 80 1F 00  0C 80 0D 80 0E 80 1F 01     2............
01B0: 00                                                .               
```

#### Opcodes

```
  0: 0x01A3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01A6 [0x1F] MOVE_ENTITY: EventEntity moves to X=219.087*, Z=-47.304*, Y=0.327*
  2: 0x01AE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01B0 [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B1  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:    1D 0F 80 23 00                                  ...#.          
```

#### Opcodes

```
  0: 0x01B1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7509*)
    → "I assumed that because the Orcs, too, were searching for something that..."
  1: 0x01B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x01B5 [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B6  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                   1D 10  80 23 00                       ...#.     
```

#### Opcodes

```
  0: 0x01B6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7511*)
    → "...I must inquire with my sister."
  1: 0x01B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x01BA [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01BB  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                   1D 11 80 23 00             ...#.
```

#### Opcodes

```
  0: 0x01BB [0x1D] PRINT_EVENT_MESSAGE(message_id=7512*)
    → "At her coming-of-age, she learned all there was to know of that sword from our father."
  1: 0x01BE [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x01BF [0x00] END_REQSTACK()
```

### Event 65535.33

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C0  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: 1D 12 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x01C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7514*)
    → "Will you lend me a hand, Vauderame? I know my sister has left something for me, and I intend to find it."
  1: 0x01C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x01C4 [0x00] END_REQSTACK()
```
