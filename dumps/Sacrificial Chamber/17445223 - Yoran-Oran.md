# 17445223 - Yoran-Oran

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Sacrificial Chamber (ID: 163) |
| Block Size       | 928 bytes                     |
| Total Events     | 33                            |
| References Count | 37                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     35 |              5 |
| [4](#event-4)              | 0x0024       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0025       |     15 |              5 |
| [5](#event-5)              | 0x0034       |      1 |              1 |
| [65535.3](#event-655353)   | 0x0035       |     14 |              3 |
| [65535.4](#event-655354)   | 0x0043       |     26 |              6 |
| [65535.5](#event-655355)   | 0x005D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x006D       |     29 |              3 |
| [65535.7](#event-655357)   | 0x008A       |     16 |              2 |
| [65535.8](#event-655358)   | 0x009A       |     16 |              2 |
| [65535.9](#event-655359)   | 0x00AA       |     18 |              4 |
| [65535.10](#event-6553510) | 0x00BC       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00CC       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00DC       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00EC       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00FC       |     16 |              2 |
| [65535.15](#event-6553515) | 0x010C       |     36 |              6 |
| [65535.16](#event-6553516) | 0x0130       |     18 |              4 |
| [65535.17](#event-6553517) | 0x0142       |     18 |              4 |
| [65535.18](#event-6553518) | 0x0154       |     16 |              2 |
| [65535.19](#event-6553519) | 0x0164       |     16 |              2 |
| [65535.20](#event-6553520) | 0x0174       |     18 |              4 |
| [65535.21](#event-6553521) | 0x0186       |     14 |              4 |
| [65535.22](#event-6553522) | 0x0194       |     16 |              2 |
| [65535.23](#event-6553523) | 0x01A4       |     16 |              2 |
| [65535.24](#event-6553524) | 0x01B4       |     16 |              2 |
| [65535.25](#event-6553525) | 0x01C4       |     32 |              5 |
| [65535.26](#event-6553526) | 0x01E4       |     73 |             12 |
| [65535.27](#event-6553527) | 0x022D       |     19 |              3 |
| [65535.28](#event-6553528) | 0x0240       |     19 |              3 |
| [65535.29](#event-6553529) | 0x0253       |     19 |              3 |
| [65535.30](#event-6553530) | 0x0266       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x000D      |          13 |
|       2 | 0x0013      |          19 |
|       3 | 0x0017      |          23 |
|       4 | 0x0000      |           0 |
|       5 | 0x0032      |          50 |
|       6 | 0xFFFFF9B9  |  4294965689 |
|       7 | 0x9AD3      |       39635 |
|       8 | 0x0078      |         120 |
|       9 | 0x0190      |         400 |
|      10 | 0x0031      |          49 |
|      11 | 0x0028      |          40 |
|      12 | 0x0006      |           6 |
|      13 | 0x0015      |          21 |
|      14 | 0x000F      |          15 |
|      15 | 0x0001      |           1 |
|      16 | 0x0011      |          17 |
|      17 | 0x0029      |          41 |
|      18 | 0x0007      |           7 |
|      19 | 0x13EA      |        5098 |
|      20 | 0x87EA      |       34794 |
|      21 | 0xFFFFF3DD  |  4294964189 |
|      22 | 0x9A40      |       39488 |
|      23 | 0xFFFFFF9C  |  4294967196 |
|      24 | 0x01F4      |         500 |
|      25 | 0x003C      |          60 |
|      26 | 0x0104      |         260 |
|      27 | 0xA2B2      |       41650 |
|      28 | 0xFFFFFA24  |  4294965796 |
|      29 | 0x01D6      |         470 |
|      30 | 0x005A      |          90 |
|      31 | 0x0AD2      |        2770 |
|      32 | 0x008C      |         140 |
|      33 | 0x005C      |          92 |
|      34 | 0x00B4      |         180 |
|      35 | 0xFFFFEF9B  |  4294963099 |
|      36 | 0xA2D5      |       41685 |

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
| Data Size    | 35 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 0B 00 80 01 80 02  80 03 80 03 80 03 80 03   ...............
0010: 80 04 80 04 80 22 00 92  01 F8 FF FF 7F 94 01 F8  ....."..........
0020: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=13*, head=19*, body=23*, hands=23*, legs=23*, feet=23*, main=0*, sub=0*)
  1: 0x0015 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0017 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x001D [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0023 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             00                                        .           
```

#### Opcodes

```
  0: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 05 80  1F 00 06 80 07 80 04 80       2..........
0030: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 50* * 0.1
  1: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.607*, Z=39.635*, Y=0.000*
  2: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0033 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0034  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             00                                        .           
```

#### Opcodes

```
  0: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 14 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1C 08 80  79 00 F8 FF FF 7F 64 31       ...y.....d1
0040: 0A 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0035 [0x1C] WAIT(120* ticks)
  1: 0x0038 [0x79] EventEntity looks at Shantotto (ID: 17445220/0x010A3164) (Basic look)
  2: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 26 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          3A F8 FF FF 7F  00 00 07 00 00 09 80 4B     :...........K
0050: F8 FF FF 7F 00 00 6F 76  F8 FF FF 7F 00           ......ov.....   
```

#### Opcodes

```
  0: 0x0043 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[0])
  1: 0x004A [0x07] ExtData[1]->WorkLocal[0] += 400*
  2: 0x004F [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=ExtData[1]->WorkLocal[0])
  3: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0057 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  5: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         66 0A 80               f..
0060: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 00           ........tlk0.   
```

#### Opcodes

```
  0: 0x005D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  1: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         66 0A 80               f..
0070: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 53 F8 FF FF  ........tlk1S...
0080: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x006D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  1: 0x007C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                66 0B 80 F8 FF FF            f.....
0090: 7F F8 FF FF 7F 74 6C 6B  30 00                    .....tlk0.      
```

#### Opcodes

```
  0: 0x008A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                66 0B 80 F8 FF FF            f.....
00A0: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x009A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                6E F8 FF FF 7F 0C            n.....
00B0: 80 99 F8 FF FF 7F 99 F8  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x00AA [0x6E] EventEntity uses emote 6*
  1: 0x00B1 [0x99] Wait for EventEntity animation to complete
  2: 0x00B6 [0x99] Wait for EventEntity animation to complete
  3: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      66 0B 80 F8              f...
00C0: FF FF 7F F8 FF FF 7F 70  6F 69 30 00              .......poi0.    
```

#### Opcodes

```
  0: 0x00BC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00CB [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                      66 0B 80 F8              f...
00D0: FF FF 7F F8 FF FF 7F 67  6B 72 73 00              .......gkrs.    
```

#### Opcodes

```
  0: 0x00CC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkrs" with entities [EventEntity, EventEntity], work=40*
  1: 0x00DB [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      66 0B 80 F8              f...
00E0: FF FF 7F F8 FF FF 7F 67  6B 72 31 00              .......gkr1.    
```

#### Opcodes

```
  0: 0x00DC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr1" with entities [EventEntity, EventEntity], work=40*
  1: 0x00EB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      66 0B 80 F8              f...
00F0: FF FF 7F F8 FF FF 7F 74  68 6B 31 00              .......thk1.    
```

#### Opcodes

```
  0: 0x00EC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      66 0B 80 F8              f...
0100: FF FF 7F F8 FF FF 7F 74  68 6B 32 00              .......thk2.    
```

#### Opcodes

```
  0: 0x00FC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x010B [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010C   |
| Data Size    | 36 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      6E F8 FF FF              n...
0110: 7F 0D 80 99 F8 FF FF 7F  99 F8 FF FF 7F 1C 0E 80  ................
0120: 66 0B 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 00  f..........tlk0.
```

#### Opcodes

```
  0: 0x010C [0x6E] EventEntity uses emote 21*
  1: 0x0113 [0x99] Wait for EventEntity animation to complete
  2: 0x0118 [0x99] Wait for EventEntity animation to complete
  3: 0x011D [0x1C] WAIT(15* ticks)
  4: 0x0120 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 6E F8 FF FF 7F 0D 80 99  F8 FF FF 7F 99 F8 FF FF  n...............
0140: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0130 [0x6E] EventEntity uses emote 21*
  1: 0x0137 [0x99] Wait for EventEntity animation to complete
  2: 0x013C [0x99] Wait for EventEntity animation to complete
  3: 0x0141 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0142   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       6E F8 FF FF 7F 0F  80 99 F8 FF FF 7F 99 F8    n.............
0150: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0142 [0x6E] EventEntity uses emote 1*
  1: 0x0149 [0x99] Wait for EventEntity animation to complete
  2: 0x014E [0x99] Wait for EventEntity animation to complete
  3: 0x0153 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0154   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:             66 10 80 F8  FF FF 7F F8 FF FF 7F 61      f..........a
0160: 79 6D 30 00                                       ym0.            
```

#### Opcodes

```
  0: 0x0154 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "aym0" with entities [EventEntity, EventEntity], work=17*
  1: 0x0163 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0164   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:             66 11 80 F8  FF FF 7F F8 FF FF 7F 67      f..........g
0170: 6D 6E 31 00                                       mn1.            
```

#### Opcodes

```
  0: 0x0164 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gmn1" with entities [EventEntity, EventEntity], work=41*
  1: 0x0173 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0174   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:             6E F8 FF FF  7F 12 80 99 F8 FF FF 7F      n...........
0180: 99 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0174 [0x6E] EventEntity uses emote 7*
  1: 0x017B [0x99] Wait for EventEntity animation to complete
  2: 0x0180 [0x99] Wait for EventEntity animation to complete
  3: 0x0185 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0186   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                   32 01  80 1F 00 13 80 14 80 04        2.........
0190: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0186 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0189 [0x1F] MOVE_ENTITY: EventEntity moves to X=5.098*, Z=34.794*, Y=0.000*
  2: 0x0191 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0193 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0194   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:             66 11 80 F8  FF FF 7F F8 FF FF 7F 73      f..........s
01A0: 77 61 30 00                                       wa0.            
```

#### Opcodes

```
  0: 0x0194 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "swa0" with entities [EventEntity, EventEntity], work=41*
  1: 0x01A3 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:             66 11 80 F8  FF FF 7F F8 FF FF 7F 73      f..........s
01B0: 77 61 31 00                                       wa1.            
```

#### Opcodes

```
  0: 0x01A4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "swa1" with entities [EventEntity, EventEntity], work=41*
  1: 0x01B3 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:             66 11 80 F8  FF FF 7F F8 FF FF 7F 73      f..........s
01C0: 68 6B 30 00                                       hk0.            
```

#### Opcodes

```
  0: 0x01B4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=41*
  1: 0x01C3 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C4   |
| Data Size    | 32 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:             BA 61 31 0A  01 15 80 16 80 17 80 18      .a1.........
01D0: 80 80 61 31 0A 01 79 00  F8 FF FF 7F 61 31 0A 01  ..a1..y.....a1..
01E0: 1C 19 80 00                                       ....            
```

#### Opcodes

```
  0: 0x01C4 [0xBA] SET_ENTITY_POSITION(entity_id=??? (ID: 17445217/0x010A3161), pos_x=-3.107*, pos_z=39.488*, pos_y=-0.100*, direction=43.9°*)
  1: 0x01D1 [0x80] LOAD_WAIT(entity=??? (ID: 17445217/0x010A3161))
  2: 0x01D6 [0x79] EventEntity looks at ??? (ID: 17445217/0x010A3161) (Basic look)
  3: 0x01E0 [0x1C] WAIT(60* ticks)
  4: 0x01E3 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E4   |
| Data Size    | 73 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:             BA 61 31 0A  01 1A 80 1B 80 1C 80 1D      .a1.........
01F0: 80 80 61 31 0A 01 4A F8  FF FF 7F 61 31 0A 01 6F  ..a1..J....a1..o
0200: 76 F8 FF FF 7F 79 00 F8  FF FF 7F 66 31 0A 01 1C  v....y.....f1...
0210: 08 80 79 00 F8 FF FF 7F  F0 FF FF 7F 1C 08 80 79  ..y............y
0220: 00 F8 FF FF 7F 61 31 0A  01 1C 1E 80 00           .....a1......   
```

#### Opcodes

```
  0: 0x01E4 [0xBA] SET_ENTITY_POSITION(entity_id=??? (ID: 17445217/0x010A3161), pos_x=0.260*, pos_z=41.650*, pos_y=-1.500*, direction=41.3°*)
  1: 0x01F1 [0x80] LOAD_WAIT(entity=??? (ID: 17445217/0x010A3161))
  2: 0x01F6 [0x4A] EventEntity looks at ??? (ID: 17445217/0x010A3161)
  3: 0x01FF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0200 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  5: 0x0205 [0x79] EventEntity looks at Aldo (ID: 17445222/0x010A3166) (Basic look)
  6: 0x020F [0x1C] WAIT(120* ticks)
  7: 0x0212 [0x79] EventEntity looks at LocalPlayer (Basic look)
  8: 0x021C [0x1C] WAIT(120* ticks)
  9: 0x021F [0x79] EventEntity looks at ??? (ID: 17445217/0x010A3161) (Basic look)
 10: 0x0229 [0x1C] WAIT(90* ticks)
 11: 0x022C [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022D   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                         5B 1F 80               [..
0230: F8 FF FF 7F F8 FF FF 7F  7A 74 75 30 1C 20 80 00  ........ztu0. ..
```

#### Opcodes

```
  0: 0x022D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ztu0" with entities [EventEntity, EventEntity], work=2770*
  1: 0x023C [0x1C] WAIT(140* ticks)
  2: 0x023F [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0240   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240: 5B 1F 80 F8 FF FF 7F F8  FF FF 7F 7A 74 75 31 1C  [..........ztu1.
0250: 21 80 00                                          !..             
```

#### Opcodes

```
  0: 0x0240 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ztu1" with entities [EventEntity, EventEntity], work=2770*
  1: 0x024F [0x1C] WAIT(92* ticks)
  2: 0x0252 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0253   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:          66 0B 80 F8 FF  FF 7F F8 FF FF 7F 69 72     f..........ir
0260: 6F 30 1C 22 80 00                                 o0."..          
```

#### Opcodes

```
  0: 0x0253 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0262 [0x1C] WAIT(180* ticks)
  2: 0x0265 [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0266   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                   32 00  80 1F 00 23 80 24 80 04        2....#.$..
0270: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0266 [0x32] ExtData[1]->MainSpeed = 5* * 0.1
  1: 0x0269 [0x1F] MOVE_ENTITY: EventEntity moves to X=-4.197*, Z=41.685*, Y=0.000*
  2: 0x0271 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0273 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0274 [0x00] END_REQSTACK()
```
