# 17768538 - Rakocha-Mukocha

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 664 bytes               |
| Total Events     | 28                      |
| References Count | 24                      |

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
| [65535.19](#event-6553519) | 0x011F       |      9 |              3 |
| [271](#event-271)          | 0x0128       |      1 |              1 |
| [65535.20](#event-6553520) | 0x0129       |     10 |              2 |
| [65535.21](#event-6553521) | 0x0133       |     14 |              4 |
| [65535.22](#event-6553522) | 0x0141       |     42 |             10 |
| [65535.23](#event-6553523) | 0x016B       |     39 |              9 |
| [65535.24](#event-6553524) | 0x0192       |     11 |              3 |
| [65535.25](#event-6553525) | 0x019D       |      5 |              3 |
| [65535.26](#event-6553526) | 0x01A2       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0029      |          41 |
|       3 | 0x002A      |          42 |
|       4 | 0xFFFFBA7C  |  4294949500 |
|       5 | 0x10BB7     |       68535 |
|       6 | 0x0000      |           0 |
|       7 | 0x0FFE      |        4094 |
|       8 | 0xFFFF8D65  |  4294937957 |
|       9 | 0x10EE9     |       69353 |
|      10 | 0x0259      |         601 |
|      11 | 0x003C      |          60 |
|      12 | 0xFFFF8558  |  4294935896 |
|      13 | 0x10B0D     |       68365 |
|      14 | 0xFFFF7BBA  |  4294933434 |
|      15 | 0x10CA7     |       68775 |
|      16 | 0xFFFFCF4D  |  4294954829 |
|      17 | 0x10904     |       67844 |
|      18 | 0xFFFFD9D0  |  4294957520 |
|      19 | 0x12114     |       74004 |
|      20 | 0xFFFFDC4C  |  4294958156 |
|      21 | 0x13CA0     |       81056 |
|      22 | 0x1F23      |        7971 |
|      23 | 0x1F31      |        7985 |

## String References

- **7971**: I've a re-port sta-ting that a dread dra-gon is ham-per-ing a group of red ma-ges' pro-gress through the gate-way.
- **7985**: Hey, is there a-ny way of shut-ting this doll up?

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
0020:                      66  00 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
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
0040:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
0050: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
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
0060:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 77 61     f..........wa
0070: 76 30 00                                          v0.             
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wav0" with entities [EventEntity, EventEntity], work=40*
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
0070:          53 F8 FF FF 7F  F8 FF FF 7F 77 61 76 30     S........wav0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wav0" with entities [EventEntity, EventEntity]
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
0080:    66 02 80 F8 FF FF 7F  F8 FF FF 7F 73 68 6B 30   f..........shk0
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=41*
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
0090:    53 F8 FF FF 7F F8 FF  FF 7F 73 68 6B 30 00      S........shk0. 
```

#### Opcodes

```
  0: 0x0091 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shk0" with entities [EventEntity, EventEntity]
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
00A0: 03 80 F8 FF FF 7F F8 FF  FF 7F 62 69 6B 30 00     ..........bik0. 
```

#### Opcodes

```
  0: 0x009F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=42*
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
00B0: F8 FF FF 7F F8 FF FF 7F  62 69 6B 30 5E 69 64 6C  ........bik0^idl
00C0: 30 1C 01 80 00                                    0....           
```

#### Opcodes

```
  0: 0x00AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
  1: 0x00BC [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x00C1 [0x1C] WAIT(30* ticks)
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
00D0: 73 79 75 30 00                                    syu0.           
```

#### Opcodes

```
  0: 0x00C5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "syu0" with entities [EventEntity, EventEntity], work=40*
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
00D0:                53 F8 FF  FF 7F F8 FF FF 7F 73 79       S........sy
00E0: 75 30 00                                          u0.             
```

#### Opcodes

```
  0: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "syu0" with entities [EventEntity, EventEntity]
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
00E0:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 69 72     f..........ir
00F0: 6F 30 00                                          o0.             
```

#### Opcodes

```
  0: 0x00E3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
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
00F0:          53 F8 FF FF 7F  F8 FF FF 7F 69 72 6F 30     S........iro0
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00F3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro0" with entities [EventEntity, EventEntity]
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
0100:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 30   f..........poi0
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0101 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=40*
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
0110:    53 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 30 00      S........poi0. 
```

#### Opcodes

```
  0: 0x0111 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x011E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011F  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               5E                 ^
0120: 69 64 6C 30 1C 01 80 00                           idl0....        
```

#### Opcodes

```
  0: 0x011F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0124 [0x1C] WAIT(30* ticks)
  2: 0x0127 [0x00] END_REQSTACK()
```

### Event 271

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0128  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          00                               .       
```

#### Opcodes

```
  0: 0x0128 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0129   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                             37 04 80 05 80 06 80           7......
0130: 07 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0129 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-17.796*, z=68.535*, y=0.000*, direction=359.8°*
  1: 0x0132 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0133   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          32 00 80 1F 00  08 80 09 80 0A 80 1F 01     2............
0140: 00                                                .               
```

#### Opcodes

```
  0: 0x0133 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0136 [0x1F] MOVE_ENTITY: EventEntity moves to X=-29.339*, Z=69.353*, Y=0.601*
  2: 0x013E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0140 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0141   |
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:    4A 5A 20 0F 01 55 20  0F 01 6F 76 5A 20 0F 01   JZ ..U ..ovZ ..
0150: 1C 0B 80 32 00 80 1F 00  0C 80 0D 80 0A 80 1F 01  ...2............
0160: 1F 00 0E 80 0F 80 0A 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0141 [0x4A] Rakocha-Mukocha (ID: 17768538/0x010F205A) looks at Shantotto (ID: 17768533/0x010F2055)
  1: 0x014A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x014B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rakocha-Mukocha (ID: 17768538/0x010F205A) Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0150 [0x1C] WAIT(60* ticks)
  4: 0x0153 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x0156 [0x1F] MOVE_ENTITY: EventEntity moves to X=-31.400*, Z=68.365*, Y=0.601*
  6: 0x015E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0160 [0x1F] MOVE_ENTITY: EventEntity moves to X=-33.862*, Z=68.775*, Y=0.601*
  8: 0x0168 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x016A [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016B   |
| Data Size    | 39 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                   32 00 80 1F 00             2....
0170: 10 80 11 80 0A 80 1F 01  1F 00 12 80 13 80 0A 80  ................
0180: 1F 01 4A 5A 20 0F 01 55  20 0F 01 6F 76 5A 20 0F  ..JZ ..U ..ovZ .
0190: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x016B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x016E [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.467*, Z=67.844*, Y=0.601*
  2: 0x0176 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0178 [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.776*, Z=74.004*, Y=0.601*
  4: 0x0180 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0182 [0x4A] Rakocha-Mukocha (ID: 17768538/0x010F205A) looks at Shantotto (ID: 17768533/0x010F2055)
  6: 0x018B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x018C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rakocha-Mukocha (ID: 17768538/0x010F205A) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x0191 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0192   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:       1F 00 14 80 15 80  06 80 1F 01 00             ...........   
```

#### Opcodes

```
  0: 0x0192 [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.140*, Z=81.056*, Y=0.000*
  1: 0x019A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x019C [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x019D  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                         1D 16 80               ...
01A0: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x019D [0x1D] PRINT_EVENT_MESSAGE(message_id=7971*)
    → "I've a re-port sta-ting that a dread dra-gon is ham-per-ing a group of red ma-ges' pro-gress through the gate-way."
  1: 0x01A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x01A1 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A2   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:       29 08 5A 20 0F 01  0D 1D 17 80 23 29 08 5A    ).Z ......#).Z
01B0: 20 0F 01 0E 00                                     ....           
```

#### Opcodes

```
  0: 0x01A2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rakocha-Mukocha (ID: 17768538/0x010F205A), tag_num=0x0D)
  1: 0x01A9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7985*)
    → "Hey, is there a-ny way of shut-ting this doll up?"
  2: 0x01AC [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01AD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rakocha-Mukocha (ID: 17768538/0x010F205A), tag_num=0x0E)
  4: 0x01B4 [0x00] END_REQSTACK()
```
