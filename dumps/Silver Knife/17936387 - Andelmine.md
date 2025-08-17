# 17936387 - Andelmine

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Silver Knife (ID: 283) |
| Block Size       | 708 bytes              |
| Total Events     | 38                     |
| References Count | 7                      |

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
| [65535.19](#event-6553519) | 0x0117       |     16 |              2 |
| [65535.20](#event-6553520) | 0x0127       |     14 |              2 |
| [65535.21](#event-6553521) | 0x0135       |     16 |              2 |
| [65535.22](#event-6553522) | 0x0145       |     14 |              2 |
| [65535.23](#event-6553523) | 0x0153       |     16 |              2 |
| [65535.24](#event-6553524) | 0x0163       |     14 |              2 |
| [65535.25](#event-6553525) | 0x0171       |     16 |              2 |
| [65535.26](#event-6553526) | 0x0181       |     14 |              2 |
| [65535.27](#event-6553527) | 0x018F       |     16 |              2 |
| [65535.28](#event-6553528) | 0x019F       |     14 |              2 |
| [65535.29](#event-6553529) | 0x01AD       |     16 |              2 |
| [65535.30](#event-6553530) | 0x01BD       |     14 |              2 |
| [65535.31](#event-6553531) | 0x01CB       |     16 |              2 |
| [65535.32](#event-6553532) | 0x01DB       |     14 |              2 |
| [2](#event-2)              | 0x01E9       |     17 |              9 |
| [9](#event-9)              | 0x01FA       |      1 |              1 |
| [11](#event-11)            | 0x01FB       |      1 |              1 |
| [12](#event-12)            | 0x01FC       |      1 |              1 |
| [14](#event-14)            | 0x01FD       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x003C      |          60 |
|       2 | 0x0021      |          33 |
|       3 | 0x001F      |          31 |
|       4 | 0x0020      |          32 |
|       5 | 0x1C3F      |        7231 |
|       6 | 0x1C40      |        7232 |

## String References

- **7231**: I have been charged with permitting only our valuable clientele to participate in the auctions.
- **7232**: Unfortunately, your name is not on my register. Please leave.

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
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
  2: 0x0023 [0x1C] WAIT(60* ticks)
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
0030: FF 7F 74 6C 62 30 00                              ..tlb0.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=33*
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
0040: 74 6C 62 30 00                                    tlb0.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb0" with entities [EventEntity, EventEntity]
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
0050: 74 6C 62 31 00                                    tlb1.           
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=33*
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
0050:                53 F8 FF  FF 7F F8 FF FF 7F 74 6C       S........tl
0060: 62 31 00                                          b1.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
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
0060:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 68     f..........th
0070: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=30*
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
0070:          53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31     S........thk1
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
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
0080:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32   f..........thk2
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
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
0090:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00      S........thk2. 
```

#### Opcodes

```
  0: 0x0091 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
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
00A0: 00 80 F8 FF FF 7F F8 FF  FF 7F 64 69 73 30 00     ..........dis0. 
```

#### Opcodes

```
  0: 0x009F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=30*
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
00B0: F8 FF FF 7F F8 FF FF 7F  64 69 73 30 00           ........dis0.   
```

#### Opcodes

```
  0: 0x00AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
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
00B0:                                         66 00 80               f..
00C0: F8 FF FF 7F F8 FF FF 7F  70 6F 69 30 00           ........poi0.   
```

#### Opcodes

```
  0: 0x00BD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=30*
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
00D0:                                   66 00 80 F8 FF             f....
00E0: FF 7F F8 FF FF 7F 70 6F  69 31 00                 ......poi1.     
```

#### Opcodes

```
  0: 0x00DB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=30*
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
0100: F8 FF FF 7F 77 65 62 30  00                       ....web0.       
```

#### Opcodes

```
  0: 0x00F9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "web0" with entities [EventEntity, EventEntity], work=31*
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
0110: FF 7F 77 65 62 30 00                              ..web0.         
```

#### Opcodes

```
  0: 0x0109 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "web0" with entities [EventEntity, EventEntity]
  1: 0x0116 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0117   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      66  00 80 F8 FF FF 7F F8 FF         f........
0120: FF 7F 70 61 73 30 00                              ..pas0.         
```

#### Opcodes

```
  0: 0x0117 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=30*
  1: 0x0126 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0127   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0130: 70 61 73 30 00                                    pas0.           
```

#### Opcodes

```
  0: 0x0127 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x0134 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0135   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                66 04 80  F8 FF FF 7F F8 FF FF 7F       f..........
0140: 73 74 64 30 00                                    std0.           
```

#### Opcodes

```
  0: 0x0135 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=32*
  1: 0x0144 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0145   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                53 F8 FF  FF 7F F8 FF FF 7F 73 74       S........st
0150: 64 30 00                                          d0.             
```

#### Opcodes

```
  0: 0x0145 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "std0" with entities [EventEntity, EventEntity]
  1: 0x0152 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0153   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:          66 04 80 F8 FF  FF 7F F8 FF FF 7F 73 74     f..........st
0160: 64 31 00                                          d1.             
```

#### Opcodes

```
  0: 0x0153 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std1" with entities [EventEntity, EventEntity], work=32*
  1: 0x0162 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0163   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:          53 F8 FF FF 7F  F8 FF FF 7F 73 74 64 31     S........std1
0170: 00                                                .               
```

#### Opcodes

```
  0: 0x0163 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "std1" with entities [EventEntity, EventEntity]
  1: 0x0170 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0171   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:    66 04 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 63 30   f..........tlc0
0180: 00                                                .               
```

#### Opcodes

```
  0: 0x0171 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=32*
  1: 0x0180 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0181   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 63 30 00      S........tlc0. 
```

#### Opcodes

```
  0: 0x0181 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc0" with entities [EventEntity, EventEntity]
  1: 0x018E [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                               66                 f
0190: 04 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 63 31 00     ..........tlc1. 
```

#### Opcodes

```
  0: 0x018F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=32*
  1: 0x019E [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                               53                 S
01A0: F8 FF FF 7F F8 FF FF 7F  74 6C 63 31 00           ........tlc1.   
```

#### Opcodes

```
  0: 0x019F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc1" with entities [EventEntity, EventEntity]
  1: 0x01AC [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AD   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                         66 04 80               f..
01B0: F8 FF FF 7F F8 FF FF 7F  74 63 73 74 00           ........tcst.   
```

#### Opcodes

```
  0: 0x01AD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tcst" with entities [EventEntity, EventEntity], work=32*
  1: 0x01BC [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BD   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                         53 F8 FF               S..
01C0: FF 7F F8 FF FF 7F 74 63  73 74 00                 ......tcst.     
```

#### Opcodes

```
  0: 0x01BD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tcst" with entities [EventEntity, EventEntity]
  1: 0x01CA [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01CB   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                   66 04 80 F8 FF             f....
01D0: FF 7F F8 FF FF 7F 73 74  74 63 00                 ......sttc.     
```

#### Opcodes

```
  0: 0x01CB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sttc" with entities [EventEntity, EventEntity], work=32*
  1: 0x01DA [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01DB   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                   53 F8 FF FF 7F             S....
01E0: F8 FF FF 7F 73 74 74 63  00                       ....sttc.       
```

#### Opcodes

```
  0: 0x01DB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sttc" with entities [EventEntity, EventEntity]
  1: 0x01E8 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E9   |
| Data Size    | 17 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                             1E F0 FF FF 7F 6F 70           .....op
01F0: 1D 05 80 23 1D 06 80 23  21 00                    ...#...#!.      
```

#### Opcodes

```
  0: 0x01E9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x01EE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x01EF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x01F0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7231*)
    → "I have been charged with permitting only our valuable clientele to participate in the auctions."
  4: 0x01F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x01F4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7232*)
    → "Unfortunately, your name is not on my register. Please leave."
  6: 0x01F7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x01F8 [0x21] END_EVENT
  8: 0x01F9 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01FA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                00                           .     
```

#### Opcodes

```
  0: 0x01FA [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01FB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                   00                         .    
```

#### Opcodes

```
  0: 0x01FB [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01FC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                      00                       .   
```

#### Opcodes

```
  0: 0x01FC [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01FD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                         00                     .  
```

#### Opcodes

```
  0: 0x01FD [0x00] END_REQSTACK()
```
