# 17772736 - Shantotto

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 508 bytes                 |
| Total Events     | 18                        |
| References Count | 16                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [10094](#event-10094)      | 0x0001       |     18 |              4 |
| [65535.1](#event-655351)   | 0x0013       |     10 |              2 |
| [65535.2](#event-655352)   | 0x001D       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0027       |     29 |              3 |
| [65535.4](#event-655354)   | 0x0044       |     29 |              3 |
| [65535.5](#event-655355)   | 0x0061       |     29 |              3 |
| [65535.6](#event-655356)   | 0x007E       |     29 |              3 |
| [65535.7](#event-655357)   | 0x009B       |     24 |              4 |
| [65535.8](#event-655358)   | 0x00B3       |     16 |              2 |
| [65535.9](#event-655359)   | 0x00C3       |     29 |              3 |
| [65535.10](#event-6553510) | 0x00E0       |     29 |              3 |
| [65535.11](#event-6553511) | 0x00FD       |     29 |              3 |
| [65535.12](#event-6553512) | 0x011A       |     29 |              3 |
| [10097](#event-10097)      | 0x0137       |      7 |              2 |
| [65535.13](#event-6553513) | 0x013E       |     22 |              6 |
| [65535.14](#event-6553514) | 0x0154       |     14 |              4 |
| [10098](#event-10098)      | 0x0162       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x8DAF      |       36271 |
|       1 | 0x10E57     |       69207 |
|       2 | 0x07CB      |        1995 |
|       3 | 0x0872      |        2162 |
|       4 | 0x8838      |       34872 |
|       5 | 0x10BB2     |       68530 |
|       6 | 0x07C7      |        1991 |
|       7 | 0x0800      |        2048 |
|       8 | 0x0766      |        1894 |
|       9 | 0x0028      |          40 |
|      10 | 0x0029      |          41 |
|      11 | 0x0096      |         150 |
|      12 | 0x000D      |          13 |
|      13 | 0x879B      |       34715 |
|      14 | 0x10D41     |       68929 |
|      15 | 0x001E      |          30 |

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

### Event 10094

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 01 94 01 F8 FF FF  7F 37 00 80 01 80 02 80   ".......7......
0010: 03 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0003 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.271*, z=69.207*, y=1.995*, direction=190.0°*
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          37 04 80 05 80  06 80 07 80 00              7.........   
```

#### Opcodes

```
  0: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=34.872*, z=68.530*, y=1.991*, direction=180.0°*
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         37 00 80               7..
0020: 01 80 02 80 08 80 00                              .......         
```

#### Opcodes

```
  0: 0x001D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.271*, z=69.207*, y=1.995*, direction=166.5°*
  1: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      66  09 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 74 6C 6B 30 53 F8  FF FF 7F F8 FF FF 7F 74  ..tlk0S........t
0040: 6C 6B 30 00                                       lk0.            
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0036 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             66 09 80 F8  FF FF 7F F8 FF FF 7F 74      f..........t
0050: 6C 6B 31 53 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31  lk1S........tlk1
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0044 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0053 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    66 09 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   f..........thk1
0070: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 00        S........thk1.  
```

#### Opcodes

```
  0: 0x0061 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0070 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            66 09                f.
0080: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 53 F8 FF  .........thk2S..
0090: FF 7F F8 FF FF 7F 74 68  6B 32 00                 ......thk2.     
```

#### Opcodes

```
  0: 0x007E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x008D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   66 0A 80 F8 FF             f....
00A0: FF 7F F8 FF FF 7F 6F 68  68 30 1C 0B 80 5E 69 64  ......ohh0...^id
00B0: 6C 30 00                                          l0.             
```

#### Opcodes

```
  0: 0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ohh0" with entities [EventEntity, EventEntity], work=41*
  1: 0x00AA [0x1C] WAIT(150* ticks)
  2: 0x00AD [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  3: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          66 0A 80 F8 FF  FF 7F F8 FF FF 7F 6F 68     f..........oh
00C0: 68 30 00                                          h0.             
```

#### Opcodes

```
  0: 0x00B3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ohh0" with entities [EventEntity, EventEntity], work=41*
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          66 0A 80 F8 FF  FF 7F F8 FF FF 7F 73 68     f..........sh
00D0: 6B 30 53 F8 FF FF 7F F8  FF FF 7F 73 68 6B 30 00  k0S........shk0.
```

#### Opcodes

```
  0: 0x00C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=41*
  1: 0x00D2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shk0" with entities [EventEntity, EventEntity]
  2: 0x00DF [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 66 09 80 F8 FF FF 7F F8  FF FF 7F 64 69 73 30 53  f..........dis0S
00F0: F8 FF FF 7F F8 FF FF 7F  64 69 73 30 00           ........dis0.   
```

#### Opcodes

```
  0: 0x00E0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00EF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  2: 0x00FC [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FD   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         66 09 80               f..
0100: F8 FF FF 7F F8 FF FF 7F  69 72 6F 30 53 F8 FF FF  ........iro0S...
0110: 7F F8 FF FF 7F 69 72 6F  30 00                    .....iro0.      
```

#### Opcodes

```
  0: 0x00FD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
  1: 0x010C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro0" with entities [EventEntity, EventEntity]
  2: 0x0119 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011A   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                66 0A 80 F8 FF FF            f.....
0120: 7F F8 FF FF 7F 65 68 6E  30 53 F8 FF FF 7F F8 FF  .....ehn0S......
0130: FF 7F 65 68 6E 30 00                              ..ehn0.         
```

#### Opcodes

```
  0: 0x011A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ehn0" with entities [EventEntity, EventEntity], work=41*
  1: 0x0129 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehn0" with entities [EventEntity, EventEntity]
  2: 0x0136 [0x00] END_REQSTACK()
```

### Event 10097

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0137  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0137 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x013D [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            32 0C                2.
0140: 80 1F 00 0D 80 0E 80 06  80 1F 01 1E C5 30 0F 01  .............0..
0150: 1C 0F 80 00                                       ....            
```

#### Opcodes

```
  0: 0x013E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0141 [0x1F] MOVE_ENTITY: EventEntity moves to X=34.715*, Z=68.929*, Y=1.991*
  2: 0x0149 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x014B [0x1E] EventEntity looks at Trion (ID: 17772741/0x010F30C5) and starts talking
  4: 0x0150 [0x1C] WAIT(30* ticks)
  5: 0x0153 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0154   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:             32 0C 80 1F  00 00 80 01 80 02 80 1F      2...........
0160: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0154 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0157 [0x1F] MOVE_ENTITY: EventEntity moves to X=36.271*, Z=69.207*, Y=1.995*
  2: 0x015F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0161 [0x00] END_REQSTACK()
```

### Event 10098

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0162  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:       00                                            .             
```

#### Opcodes

```
  0: 0x0162 [0x00] END_REQSTACK()
```
