# 17768536 - Doron-Fulun

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 696 bytes               |
| Total Events     | 28                      |
| References Count | 30                      |

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
| [65535.22](#event-6553522) | 0x0141       |     26 |              6 |
| [65535.23](#event-6553523) | 0x015B       |     66 |             14 |
| [65535.24](#event-6553524) | 0x019D       |     11 |              3 |
| [65535.25](#event-6553525) | 0x01A8       |      5 |              3 |
| [65535.26](#event-6553526) | 0x01AD       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0029      |          41 |
|       3 | 0x002A      |          42 |
|       4 | 0xFFFF8C8C  |  4294937740 |
|       5 | 0x10D87     |       68999 |
|       6 | 0x0259      |         601 |
|       7 | 0x0FF3      |        4083 |
|       8 | 0xFFFF843C  |  4294935612 |
|       9 | 0x10E64     |       69220 |
|      10 | 0xFFFF8148  |  4294934856 |
|      11 | 0x10F64     |       69476 |
|      12 | 0xFFFFA61A  |  4294944282 |
|      13 | 0x10C5E     |       68702 |
|      14 | 0x010B      |         267 |
|      15 | 0xFFFFB9F8  |  4294949368 |
|      16 | 0x10D3D     |       68925 |
|      17 | 0x0000      |           0 |
|      18 | 0xFFFFC1A7  |  4294951335 |
|      19 | 0x10F14     |       69396 |
|      20 | 0x023E      |         574 |
|      21 | 0xFFFFD1F3  |  4294955507 |
|      22 | 0x113BE     |       70590 |
|      23 | 0xFFFFD310  |  4294955792 |
|      24 | 0x1155D     |       71005 |
|      25 | 0xFFFFD584  |  4294956420 |
|      26 | 0x142C3     |       82627 |
|      27 | 0x0094      |         148 |
|      28 | 0x1F20      |        7968 |
|      29 | 0x1F2C      |        7980 |

## String References

- **7968**: Minister Shantotto! According to the W.W. $1, our company is the only one to become stuck and stranded!
- **7980**: Minister Shantotto, please calm down and control yourself!

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
  0: 0x0129 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-29.556*, z=68.999*, y=0.601*, direction=358.8°*
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
0130:          32 00 80 1F 00  08 80 09 80 06 80 1F 01     2............
0140: 00                                                .               
```

#### Opcodes

```
  0: 0x0133 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0136 [0x1F] MOVE_ENTITY: EventEntity moves to X=-31.684*, Z=69.220*, Y=0.601*
  2: 0x013E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0140 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0141   |
| Data Size    | 26 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:    1F 00 0A 80 0B 80 06  80 1F 01 4A 58 20 0F 01   ..........JX ..
0150: 55 20 0F 01 6F 76 58 20  0F 01 00                 U ..ovX ...     
```

#### Opcodes

```
  0: 0x0141 [0x1F] MOVE_ENTITY: EventEntity moves to X=-32.440*, Z=69.476*, Y=0.601*
  1: 0x0149 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x014B [0x4A] Doron-Fulun (ID: 17768536/0x010F2058) looks at Shantotto (ID: 17768533/0x010F2055)
  3: 0x0154 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0155 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Doron-Fulun (ID: 17768536/0x010F2058) Render.Flags0 and Render.Flags3 conditions are met
  5: 0x015A [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015B   |
| Data Size    | 66 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                   1F 00 0C 80 0D             .....
0160: 80 0E 80 1F 01 1F 00 0F  80 10 80 11 80 1F 01 1F  ................
0170: 00 12 80 13 80 14 80 1F  01 1F 00 15 80 16 80 06  ................
0180: 80 1F 01 1F 00 17 80 18  80 06 80 1F 01 4A 58 20  .............JX 
0190: 0F 01 55 20 0F 01 6F 76  58 20 0F 01 00           ..U ..ovX ...   
```

#### Opcodes

```
  0: 0x015B [0x1F] MOVE_ENTITY: EventEntity moves to X=-23.014*, Z=68.702*, Y=0.267*
  1: 0x0163 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0165 [0x1F] MOVE_ENTITY: EventEntity moves to X=-17.928*, Z=68.925*, Y=0.000*
  3: 0x016D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x016F [0x1F] MOVE_ENTITY: EventEntity moves to X=-15.961*, Z=69.396*, Y=0.574*
  5: 0x0177 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0179 [0x1F] MOVE_ENTITY: EventEntity moves to X=-11.789*, Z=70.590*, Y=0.601*
  7: 0x0181 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0183 [0x1F] MOVE_ENTITY: EventEntity moves to X=-11.504*, Z=71.005*, Y=0.601*
  9: 0x018B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x018D [0x4A] Doron-Fulun (ID: 17768536/0x010F2058) looks at Shantotto (ID: 17768533/0x010F2055)
 11: 0x0196 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 12: 0x0197 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Doron-Fulun (ID: 17768536/0x010F2058) Render.Flags0 and Render.Flags3 conditions are met
 13: 0x019C [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019D   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                         1F 00 19               ...
01A0: 80 1A 80 1B 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x019D [0x1F] MOVE_ENTITY: EventEntity moves to X=-10.876*, Z=82.627*, Y=0.148*
  1: 0x01A5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x01A7 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01A8  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                          1D 1C 80 23 00                   ...#.   
```

#### Opcodes

```
  0: 0x01A8 [0x1D] PRINT_EVENT_MESSAGE(message_id=7968*)
    → "Minister Shantotto! According to the W.W. $1, our company is the only one to become stuck and stranded!"
  1: 0x01AB [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x01AC [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AD   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                         29 08 58               ).X
01B0: 20 0F 01 0F 1D 1D 80 23  29 08 58 20 0F 01 10 00   ......#).X ....
```

#### Opcodes

```
  0: 0x01AD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Doron-Fulun (ID: 17768536/0x010F2058), tag_num=0x0F)
  1: 0x01B4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7980*)
    → "Minister Shantotto, please calm down and control yourself!"
  2: 0x01B7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01B8 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Doron-Fulun (ID: 17768536/0x010F2058), tag_num=0x10)
  4: 0x01BF [0x00] END_REQSTACK()
```
