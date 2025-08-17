# 17556018 - Vauderame

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | King Ranperre's Tomb (ID: 190) |
| Block Size       | 488 bytes                      |
| Total Events     | 25                             |
| References Count | 11                             |

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
| [4](#event-4)              | 0x0120       |      1 |              1 |
| [65535.20](#event-6553520) | 0x0121       |      5 |              3 |
| [65535.21](#event-6553521) | 0x0126       |      5 |              3 |
| [65535.22](#event-6553522) | 0x012B       |     14 |              4 |
| [65535.23](#event-6553523) | 0x0139       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x001E      |          30 |
|       2 | 0x0015      |          21 |
|       3 | 0x1C98      |        7320 |
|       4 | 0x1C99      |        7321 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFFF429  |  4294964265 |
|       7 | 0xFFFE9411  |  4294874129 |
|       8 | 0x0000      |           0 |
|       9 | 0xFFFFFC87  |  4294966407 |
|      10 | 0xFFFEB7F8  |  4294883320 |

## String References

- **7320**: Say not another word, Rochefogne!
- **7321**: Adventurer, look no further than bats for your proof of tomb-robbing. Whoever came left much before departing.

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
0020:                      66  00 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
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
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
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
00B0:                                         66 02 80               f..
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
00D0:                                   66 02 80 F8 FF             f....
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
00F0:                             66 02 80 F8 FF FF 7F           f......
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

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0120  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0120 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0121  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    1D 03 80 23 00                                  ...#.          
```

#### Opcodes

```
  0: 0x0121 [0x1D] PRINT_EVENT_MESSAGE(message_id=7320*)
    → "Say not another word, Rochefogne!"
  1: 0x0124 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0125 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0126  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                   1D 04  80 23 00                       ...#.     
```

#### Opcodes

```
  0: 0x0126 [0x1D] PRINT_EVENT_MESSAGE(message_id=7321*)
    → "Adventurer, look no further than bats for your proof of tomb-robbing. Whoever came left much before departing."
  1: 0x0129 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x012A [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   32 05 80 1F 00             2....
0130: 06 80 07 80 08 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x012B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x012E [0x1F] MOVE_ENTITY: EventEntity moves to X=-3.031*, Z=-93.167*, Y=0.000*
  2: 0x0136 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0138 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0139   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             32 05 80 1F 00 09 80           2......
0140: 0A 80 08 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0139 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x013C [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.889*, Z=-83.976*, Y=0.000*
  2: 0x0144 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0146 [0x00] END_REQSTACK()
```
