# 17563918 - Yoran-Oran

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Inner Horutoto Ruins (ID: 192) |
| Block Size       | 640 bytes                      |
| Total Events     | 29                             |
| References Count | 23                             |

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
| [65535.16](#event-6553516) | 0x00EB       |     22 |              4 |
| [65535.17](#event-6553517) | 0x0101       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0111       |     14 |              2 |
| [65535.19](#event-6553519) | 0x011F       |      9 |              3 |
| [73](#event-73)            | 0x0128       |      1 |              1 |
| [65535.20](#event-6553520) | 0x0129       |     10 |              2 |
| [65535.21](#event-6553521) | 0x0133       |     37 |              9 |
| [65535.22](#event-6553522) | 0x0158       |     14 |              4 |
| [65535.23](#event-6553523) | 0x0166       |     17 |              5 |
| [65535.24](#event-6553524) | 0x0177       |      9 |              5 |
| [65535.25](#event-6553525) | 0x0180       |      5 |              3 |
| [65535.26](#event-6553526) | 0x0185       |      5 |              3 |
| [65535.27](#event-6553527) | 0x018A       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0029      |          41 |
|       3 | 0x002A      |          42 |
|       4 | 0xFFFC8510  |  4294739216 |
|       5 | 0x237AF     |      145327 |
|       6 | 0x0000      |           0 |
|       7 | 0x0CD3      |        3283 |
|       8 | 0x000D      |          13 |
|       9 | 0xFFFC85ED  |  4294739437 |
|      10 | 0x23C50     |      146512 |
|      11 | 0xFFFC86B2  |  4294739634 |
|      12 | 0x2415A     |      147802 |
|      13 | 0x0FBC      |        4028 |
|      14 | 0xFFFC8E28  |  4294741544 |
|      15 | 0x242A1     |      148129 |
|      16 | 0x0015      |          21 |
|      17 | 0x1CC6      |        7366 |
|      18 | 0x1CC9      |        7369 |
|      19 | 0x1CCA      |        7370 |
|      20 | 0x1CCB      |        7371 |
|      21 | 0x1CCC      |        7372 |
|      22 | 0x1CD0      |        7376 |

## String References

- **7366**: What might-ethy this be?
- **7369**: You imbeciles! This is a new bud--a bud of the Great Star Tree.
- **7370**: The Great Star Tree knows-ethy that it is in danger. It buds to save-ethy itself, it does.
- **7371**: But, until now, no light shone-ethy in here. The bud cried for help-ethy. It is good that we got-ethy here in time.
- **7372**: I thank-ethy you, adventurer. You saved-ethy the Great Star Tree!
- **7376**: But to be so weak to know-ethy it's in danger... This is definitely-ethy a serious problem.

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
0060:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 70 6F     f..........po
0070: 69 30 00                                          i0.             
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=40*
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
0070:          53 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 30     S........poi0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
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
0080:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 73 79 75 30   f..........syu0
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "syu0" with entities [EventEntity, EventEntity], work=40*
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
0090:    53 F8 FF FF 7F F8 FF  FF 7F 73 79 75 30 00      S........syu0. 
```

#### Opcodes

```
  0: 0x0091 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "syu0" with entities [EventEntity, EventEntity]
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
00A0: 00 80 F8 FF FF 7F F8 FF  FF 7F 69 72 6F 30 00     ..........iro0. 
```

#### Opcodes

```
  0: 0x009F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
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
00B0: F8 FF FF 7F F8 FF FF 7F  69 72 6F 30 00           ........iro0.   
```

#### Opcodes

```
  0: 0x00AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro0" with entities [EventEntity, EventEntity]
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
00C0: F8 FF FF 7F F8 FF FF 7F  67 68 6E 30 00           ........ghn0.   
```

#### Opcodes

```
  0: 0x00BD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ghn0" with entities [EventEntity, EventEntity], work=41*
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
00D0: FF 7F F8 FF FF 7F 67 68  6E 30 00                 ......ghn0.     
```

#### Opcodes

```
  0: 0x00CD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ghn0" with entities [EventEntity, EventEntity]
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
00E0: FF 7F F8 FF FF 7F 62 69  6B 30 00                 ......bik0.     
```

#### Opcodes

```
  0: 0x00DB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=42*
  1: 0x00EA [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EB   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                   53 F8 FF FF 7F             S....
00F0: F8 FF FF 7F 62 69 6B 30  5E 69 64 6C 30 1C 01 80  ....bik0^idl0...
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00EB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
  1: 0x00F8 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x00FD [0x1C] WAIT(30* ticks)
  3: 0x0100 [0x00] END_REQSTACK()
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
0100:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 70 61 73 30   f..........pas0
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0101 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=40*
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
0110:    53 F8 FF FF 7F F8 FF  FF 7F 70 61 73 30 00      S........pas0. 
```

#### Opcodes

```
  0: 0x0111 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
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

### Event 73

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
  0: 0x0129 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-228.080*, z=145.327*, y=0.000*, direction=288.5°*
  1: 0x0132 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0133   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          32 08 80 1F 00  09 80 0A 80 06 80 1F 01     2............
0140: 1F 00 0B 80 0C 80 06 80  1F 01 4B 0E 01 0C 01 0D  ..........K.....
0150: 80 6F 76 0E 01 0C 01 00                           .ov.....        
```

#### Opcodes

```
  0: 0x0133 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0136 [0x1F] MOVE_ENTITY: EventEntity moves to X=-227.859*, Z=146.512*, Y=0.000*
  2: 0x013E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0140 [0x1F] MOVE_ENTITY: EventEntity moves to X=-227.662*, Z=147.802*, Y=0.000*
  4: 0x0148 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x014A [0x4B] UPDATE_ENTITY_YAW(entity=Yoran-Oran (ID: 17563918/0x010C010E), yaw=22.1°*)
  6: 0x0151 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0152 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Yoran-Oran (ID: 17563918/0x010C010E) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x0157 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0158   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                          32 08 80 1F 00 0E 80 0F          2.......
0160: 80 06 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0158 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x015B [0x1F] MOVE_ENTITY: EventEntity moves to X=-225.752*, Z=148.129*, Y=0.000*
  2: 0x0163 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0165 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0166   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                   6E F8  FF FF 7F 10 80 99 F8 FF        n.........
0170: FF 7F 1D 11 80 23 00                              .....#.         
```

#### Opcodes

```
  0: 0x0166 [0x6E] EventEntity uses emote 21*
  1: 0x016D [0x99] Wait for EventEntity animation to complete
  2: 0x0172 [0x1D] PRINT_EVENT_MESSAGE(message_id=7366*)
    → "What might-ethy this be?"
  3: 0x0175 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0176 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0177  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                      1D  12 80 23 1D 13 80 23 00         ...#...#.
```

#### Opcodes

```
  0: 0x0177 [0x1D] PRINT_EVENT_MESSAGE(message_id=7369*)
    → "You imbeciles! This is a new bud--a bud of the Great Star Tree."
  1: 0x017A [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x017B [0x1D] PRINT_EVENT_MESSAGE(message_id=7370*)
    → "The Great Star Tree knows-ethy that it is in danger. It buds to save-ethy itself, it does."
  3: 0x017E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x017F [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0180  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180: 1D 14 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x0180 [0x1D] PRINT_EVENT_MESSAGE(message_id=7371*)
    → "But, until now, no light shone-ethy in here. The bud cried for help-ethy. It is good that we got-ethy here in time."
  1: 0x0183 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0184 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0185  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                1D 15 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x0185 [0x1D] PRINT_EVENT_MESSAGE(message_id=7372*)
    → "I thank-ethy you, adventurer. You saved-ethy the Great Star Tree!"
  1: 0x0188 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0189 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018A   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                29 08 0E 01 0C 01            ).....
0190: 03 1D 16 80 23 29 08 0E  01 0C 01 04 00           ....#).......   
```

#### Opcodes

```
  0: 0x018A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Yoran-Oran (ID: 17563918/0x010C010E), tag_num=0x03)
  1: 0x0191 [0x1D] PRINT_EVENT_MESSAGE(message_id=7376*)
    → "But to be so weak to know-ethy it's in danger... This is definitely-ethy a serious problem."
  2: 0x0194 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0195 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Yoran-Oran (ID: 17563918/0x010C010E), tag_num=0x04)
  4: 0x019C [0x00] END_REQSTACK()
```
