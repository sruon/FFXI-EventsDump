# 17936389 - Dusky Forest

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Silver Knife (ID: 283) |
| Block Size       | 848 bytes              |
| Total Events     | 37                     |
| References Count | 21                     |

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
| [65535.12](#event-6553512) | 0x00AF       |     22 |              4 |
| [65535.13](#event-6553513) | 0x00C5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00D5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00E3       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00F3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x0101       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0111       |     14 |              2 |
| [65535.19](#event-6553519) | 0x011F       |     16 |              2 |
| [65535.20](#event-6553520) | 0x012F       |     14 |              2 |
| [65535.21](#event-6553521) | 0x013D       |      9 |              3 |
| [65535.22](#event-6553522) | 0x0146       |     16 |              2 |
| [65535.23](#event-6553523) | 0x0156       |     14 |              2 |
| [65535.24](#event-6553524) | 0x0164       |     16 |              2 |
| [65535.25](#event-6553525) | 0x0174       |     14 |              2 |
| [65535.26](#event-6553526) | 0x0182       |     16 |              2 |
| [65535.27](#event-6553527) | 0x0192       |     14 |              2 |
| [65535.28](#event-6553528) | 0x01A0       |     16 |              2 |
| [65535.29](#event-6553529) | 0x01B0       |     14 |              2 |
| [4](#event-4)              | 0x01BE       |     76 |             17 |
| [9](#event-9)              | 0x020A       |      1 |              1 |
| [11](#event-11)            | 0x020B       |      1 |              1 |
| [12](#event-12)            | 0x020C       |      1 |              1 |
| [16](#event-16)            | 0x020D       |      1 |              1 |
| [65535.30](#event-6553530) | 0x020E       |     48 |             12 |
| [65535.31](#event-6553531) | 0x023E       |     26 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x003D      |          61 |
|       2 | 0x0041      |          65 |
|       3 | 0x0045      |          69 |
|       4 | 0x0000      |           0 |
|       5 | 0x1C49      |        7241 |
|       6 | 0x1C4A      |        7242 |
|       7 | 0x00C8      |         200 |
|       8 | 0x0001      |           1 |
|       9 | 0x0028      |          40 |
|      10 | 0xFFFF62B4  |  4294927028 |
|      11 | 0xAE36      |       44598 |
|      12 | 0xFFFFFD77  |  4294966647 |
|      13 | 0xFFFF653C  |  4294927676 |
|      14 | 0x995E      |       39262 |
|      15 | 0x0545      |        1349 |
|      16 | 0x000A      |          10 |
|      17 | 0x000D      |          13 |
|      18 | 0xFFFF4C5A  |  4294921306 |
|      19 | 0xB55C      |       46428 |
|      20 | 0xFFFFFD6B  |  4294966635 |

## String References

- **7241**: Are you finished with your business?
- **7242**: Leave? [Yes./No.]

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
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
0020: 64 6C 30 1C 00 80 00                              dl0....         
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
0020:                      66  00 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 70 61 73 30 00                              ..pas0.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=60*
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
0040: 70 61 73 30 00                                    pas0.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
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
0040:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
0050: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
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
0060: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
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
0070: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=60*
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
0070:          53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32     S........thk2
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
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
0080:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 30   f..........poi0
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=60*
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
0090:    53 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 30 00      S........poi0. 
```

#### Opcodes

```
  0: 0x0091 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
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
00A0: 00 80 F8 FF FF 7F F8 FF  FF 7F 61 6E 67 30 00     ..........ang0. 
```

#### Opcodes

```
  0: 0x009F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=60*
  1: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               53                 S
00B0: F8 FF FF 7F F8 FF FF 7F  61 6E 67 30 5E 69 64 6C  ........ang0^idl
00C0: 30 1C 00 80 00                                    0....           
```

#### Opcodes

```
  0: 0x00AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
  1: 0x00BC [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x00C1 [0x1C] WAIT(60* ticks)
  3: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
00D0: 64 69 73 30 00                                    dis0.           
```

#### Opcodes

```
  0: 0x00C5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=60*
  1: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                53 F8 FF  FF 7F F8 FF FF 7F 64 69       S........di
00E0: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          66 01 80 F8 FF  FF 7F F8 FF FF 7F 77 61     f..........wa
00F0: 76 30 00                                          v0.             
```

#### Opcodes

```
  0: 0x00E3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wav0" with entities [EventEntity, EventEntity], work=61*
  1: 0x00F2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          53 F8 FF FF 7F  F8 FF FF 7F 77 61 76 30     S........wav0
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00F3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wav0" with entities [EventEntity, EventEntity]
  1: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    66 02 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 62 30   f..........tlb0
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0101 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  1: 0x0110 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0111   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 30 00      S........tlb0. 
```

#### Opcodes

```
  0: 0x0111 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb0" with entities [EventEntity, EventEntity]
  1: 0x011E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               66                 f
0120: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 31 00     ..........tlb1. 
```

#### Opcodes

```
  0: 0x011F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
  1: 0x012E [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                               53                 S
0130: F8 FF FF 7F F8 FF FF 7F  74 6C 62 31 00           ........tlb1.   
```

#### Opcodes

```
  0: 0x012F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  1: 0x013C [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013D  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         5E 69 64               ^id
0140: 6C 30 1C 00 80 00                                 l0....          
```

#### Opcodes

```
  0: 0x013D [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0142 [0x1C] WAIT(60* ticks)
  2: 0x0145 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0146   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                   66 03  80 F8 FF FF 7F F8 FF FF        f.........
0150: 7F 73 68 61 30 00                                 .sha0.          
```

#### Opcodes

```
  0: 0x0146 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=69*
  1: 0x0155 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   53 F8  FF FF 7F F8 FF FF 7F 73        S........s
0160: 68 61 30 00                                       ha0.            
```

#### Opcodes

```
  0: 0x0156 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  1: 0x0163 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0164   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:             66 03 80 F8  FF FF 7F F8 FF FF 7F 73      f..........s
0170: 69 72 30 00                                       ir0.            
```

#### Opcodes

```
  0: 0x0164 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir0" with entities [EventEntity, EventEntity], work=69*
  1: 0x0173 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0174   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:             53 F8 FF FF  7F F8 FF FF 7F 73 69 72      S........sir
0180: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0174 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sir0" with entities [EventEntity, EventEntity]
  1: 0x0181 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0182   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:       66 03 80 F8 FF FF  7F F8 FF FF 7F 73 69 72    f..........sir
0190: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0182 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir1" with entities [EventEntity, EventEntity], work=69*
  1: 0x0191 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0192   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:       53 F8 FF FF 7F F8  FF FF 7F 73 69 72 31 00    S........sir1.
```

#### Opcodes

```
  0: 0x0192 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sir1" with entities [EventEntity, EventEntity]
  1: 0x019F [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0: 66 03 80 F8 FF FF 7F F8  FF FF 7F 73 68 61 31 00  f..........sha1.
```

#### Opcodes

```
  0: 0x01A0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=69*
  1: 0x01AF [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B0   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0: 53 F8 FF FF 7F F8 FF FF  7F 73 68 61 31 00        S........sha1.  
```

#### Opcodes

```
  0: 0x01B0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  1: 0x01BD [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BE   |
| Data Size    | 76 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                            03 01                ..
01C0: 10 04 80 1E F0 FF FF 7F  6F 70 1D 05 80 23 24 06  ........op...#$.
01D0: 80 04 80 04 80 25 02 00  10 04 80 00 08 02 42 45  .....%........BE
01E0: 07 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 04 80  ..........fdo1..
01F0: 55 07 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 03  U..........fdo1.
0200: 01 10 08 80 30 01 08 02  21 00                    ....0...!.      
```

#### Opcodes

```
  0: 0x01BE [0x03] Work_Zone[1] = 0*
  1: 0x01C3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x01C8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x01C9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x01CA [0x1D] PRINT_EVENT_MESSAGE(message_id=7241*)
    → "Are you finished with your business?"
  5: 0x01CD [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01CE [0x24] CREATE_DIALOG(message_id=7242*, default_option=0*, option_flags=0*)
    → "Leave? [Yes./No.]"
  7: 0x01D5 [0x25] WAIT_DIALOG_SELECT()
  8: 0x01D6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0208
  9: 0x01DE [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x01DF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x01F0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 12: 0x01FF [0x03] Work_Zone[1] = 1*
 13: 0x0204 [0x30] SET_UCOFF_CONTINUE_ZERO()
 14: 0x0205 [0x01] GOTO 0x0208

SUBROUTINE_0208:
 15: 0x0208 [0x21] END_EVENT
 16: 0x0209 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x020A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                00                           .     
```

#### Opcodes

```
  0: 0x020A [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x020B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                   00                         .    
```

#### Opcodes

```
  0: 0x020B [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x020C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                      00                       .   
```

#### Opcodes

```
  0: 0x020C [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x020D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                         00                     .  
```

#### Opcodes

```
  0: 0x020D [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x020E   |
| Data Size    | 48 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                            32 09                2.
0210: 80 1F 00 0A 80 0B 80 0C  80 1F 01 6F 1F 00 0D 80  ...........o....
0220: 0E 80 0F 80 1F 01 1C 10  80 1E 1C B0 11 01 1C 10  ................
0230: 80 6E F8 FF FF 7F 10 80  99 F8 FF FF 7F 00        .n............  
```

#### Opcodes

```
  0: 0x020E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0211 [0x1F] MOVE_ENTITY: EventEntity moves to X=-40.268*, Z=44.598*, Y=-0.649*
  2: 0x0219 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x021B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x021C [0x1F] MOVE_ENTITY: EventEntity moves to X=-39.620*, Z=39.262*, Y=1.349*
  5: 0x0224 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0226 [0x1C] WAIT(10* ticks)
  7: 0x0229 [0x1E] EventEntity looks at Magh Bihu (ID: 17936412/0x0111B01C) and starts talking
  8: 0x022E [0x1C] WAIT(10* ticks)
  9: 0x0231 [0x6E] EventEntity uses emote 10*
 10: 0x0238 [0x99] Wait for EventEntity animation to complete
 11: 0x023D [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x023E   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                                            32 11                2.
0240: 80 1F 00 0A 80 0B 80 0C  80 1F 01 6F 1F 00 12 80  ...........o....
0250: 13 80 14 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x023E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0241 [0x1F] MOVE_ENTITY: EventEntity moves to X=-40.268*, Z=44.598*, Y=-0.649*
  2: 0x0249 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x024B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x024C [0x1F] MOVE_ENTITY: EventEntity moves to X=-45.990*, Z=46.428*, Y=-0.661*
  5: 0x0254 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0256 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0257 [0x00] END_REQSTACK()
```
