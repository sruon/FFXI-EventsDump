# 17277245 - Yoran-Oran

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Ro'Maeve (ID: 122) |
| Block Size       | 608 bytes          |
| Total Events     | 24                 |
| References Count | 32                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [71](#event-71)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     35 |              5 |
| [65535.2](#event-655352)   | 0x0025       |     10 |              2 |
| [65535.3](#event-655353)   | 0x002F       |     21 |              5 |
| [65535.4](#event-655354)   | 0x0044       |     14 |              4 |
| [65535.5](#event-655355)   | 0x0052       |     14 |              4 |
| [65535.6](#event-655356)   | 0x0060       |     14 |              4 |
| [65535.7](#event-655357)   | 0x006E       |     16 |              2 |
| [65535.8](#event-655358)   | 0x007E       |     16 |              2 |
| [65535.9](#event-655359)   | 0x008E       |     16 |              2 |
| [65535.10](#event-6553510) | 0x009E       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00AE       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00BE       |     19 |              3 |
| [65535.13](#event-6553513) | 0x00D1       |     19 |              3 |
| [65535.14](#event-6553514) | 0x00E4       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00F4       |     19 |              3 |
| [65535.16](#event-6553516) | 0x0107       |     19 |              3 |
| [65535.17](#event-6553517) | 0x011A       |     16 |              2 |
| [65535.18](#event-6553518) | 0x012A       |     13 |              3 |
| [65535.19](#event-6553519) | 0x0137       |      7 |              2 |
| [65535.20](#event-6553520) | 0x013E       |     16 |              2 |
| [65535.21](#event-6553521) | 0x014E       |     18 |              4 |
| [65535.22](#event-6553522) | 0x0160       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x000D      |          13 |
|       2 | 0x0013      |          19 |
|       3 | 0x0017      |          23 |
|       4 | 0x0000      |           0 |
|       5 | 0x0032      |          50 |
|       6 | 0xFFFC9603  |  4294743555 |
|       7 | 0xFFFE75A9  |  4294866345 |
|       8 | 0xFFFFE675  |  4294960757 |
|       9 | 0x0320      |         800 |
|      10 | 0xFFFCC62F  |  4294755887 |
|      11 | 0x8E29      |       36393 |
|      12 | 0xFFFFEFE3  |  4294963171 |
|      13 | 0x000A      |          10 |
|      14 | 0xFFFCC326  |  4294755110 |
|      15 | 0x909E      |       37022 |
|      16 | 0x0028      |          40 |
|      17 | 0xFFFD1822  |  4294776866 |
|      18 | 0x4BD2      |       19410 |
|      19 | 0x0031      |          49 |
|      20 | 0x002A      |          42 |
|      21 | 0x0029      |          41 |
|      22 | 0x005A      |          90 |
|      23 | 0x003C      |          60 |
|      24 | 0x00B4      |         180 |
|      25 | 0x00AC      |         172 |
|      26 | 0x0015      |          21 |
|      27 | 0x0AD2      |        2770 |
|      28 | 0xFFFCC23D  |  4294754877 |
|      29 | 0x8EDF      |       36575 |
|      30 | 0x01BC      |         444 |
|      31 | 0x000F      |          15 |

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

### Event 71

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 35 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       B6 0B 00 80 01 80  02 80 03 80 03 80 03 80    ..............
0010: 03 80 04 80 04 80 22 00  92 01 F8 FF FF 7F 94 01  ......".........
0020: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0002 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=13*, head=19*, body=23*, hands=23*, legs=23*, feet=23*, main=0*, sub=0*)
  1: 0x0016 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0018 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x001E [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                6C F8 FF  FF 7F 04 80 04 80 00          l......... 
```

#### Opcodes

```
  0: 0x0025 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 05 80 1F 00 06 80 07 80  08 80 1F 01 4B F8 FF FF  ............K...
0040: 7F 09 80 00                                       ....            
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 50* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=-223.741*, Z=-100.951*, Y=-6.539*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=4.4°*)
  4: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             32 05 80 1F  00 0A 80 0B 80 0C 80 1F      2...........
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0044 [0x32] ExtData[1]->MainSpeed = 50* * 0.1
  1: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=-211.409*, Z=36.393*, Y=-4.125*
  2: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       32 0D 80 1F 00 0E  80 0F 80 0C 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0052 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=-212.186*, Z=37.022*, Y=-4.125*
  2: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 32 10 80 1F 00 11 80 12  80 0C 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0060 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=-190.430*, Z=19.410*, Y=-4.125*
  2: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            66 13                f.
0070: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 00        .........tlk0.  
```

#### Opcodes

```
  0: 0x006E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  1: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            66 13                f.
0080: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 00        .........tlk1.  
```

#### Opcodes

```
  0: 0x007E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  1: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            66 14                f.
0090: 80 F8 FF FF 7F F8 FF FF  7F 62 69 6B 30 00        .........bik0.  
```

#### Opcodes

```
  0: 0x008E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=42*
  1: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            66 14                f.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 62 69 6B 31 00        .........bik1.  
```

#### Opcodes

```
  0: 0x009E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik1" with entities [EventEntity, EventEntity], work=42*
  1: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            66 15                f.
00B0: 80 F8 FF FF 7F F8 FF FF  7F 73 68 6B 30 00        .........shk0.  
```

#### Opcodes

```
  0: 0x00AE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=41*
  1: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            66 10                f.
00C0: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 1C 16 80  .........thk1...
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00BE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x00CD [0x1C] WAIT(90* ticks)
  2: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    66 10 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32   f..........thk2
00E0: 1C 17 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00D1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x00E0 [0x1C] WAIT(60* ticks)
  2: 0x00E3 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             66 10 80 F8  FF FF 7F F8 FF FF 7F 64      f..........d
00F0: 69 73 30 00                                       is0.            
```

#### Opcodes

```
  0: 0x00E4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00F3 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F4   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:             66 10 80 F8  FF FF 7F F8 FF FF 7F 69      f..........i
0100: 72 6F 30 1C 18 80 00                              ro0....         
```

#### Opcodes

```
  0: 0x00F4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0103 [0x1C] WAIT(180* ticks)
  2: 0x0106 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0107   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                      66  10 80 F8 FF FF 7F F8 FF         f........
0110: FF 7F 67 6B 72 30 1C 19  80 00                    ..gkr0....      
```

#### Opcodes

```
  0: 0x0107 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0116 [0x1C] WAIT(172* ticks)
  2: 0x0119 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                66 10 80 F8 FF FF            f.....
0120: 7F F8 FF FF 7F 67 6B 72  31 00                    .....gkr1.      
```

#### Opcodes

```
  0: 0x011A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0129 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012A   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                6E F8 FF FF 7F 1A            n.....
0130: 80 99 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x012A [0x6E] EventEntity uses emote 21*
  1: 0x0131 [0x99] Wait for EventEntity animation to complete
  2: 0x0136 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0137  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                      59  06 F8 FF FF 7F 00               Y......  
```

#### Opcodes

```
  0: 0x0137 [0x59] UPDATE_ENTITY_DATA: Check if EventEntity is performing moving action
  1: 0x013D [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            5B 1B                [.
0140: 80 F8 FF FF 7F F8 FF FF  7F 79 6B 65 30 00        .........yke0.  
```

#### Opcodes

```
  0: 0x013E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yke0" with entities [EventEntity, EventEntity], work=2770*
  1: 0x014D [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014E   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                            84 BA                ..
0150: F8 FF FF 7F 1C 80 1D 80  0C 80 1E 80 1C 1F 80 00  ................
```

#### Opcodes

```
  0: 0x014E [0x84] ADJUST_RENDER_FLAGS3_BIT0()
  1: 0x014F [0xBA] SET_ENTITY_POSITION(entity_id=EventEntity, pos_x=-212.419*, pos_z=36.575*, pos_y=-4.125*, direction=39.0°*)
  2: 0x015C [0x1C] WAIT(15* ticks)
  3: 0x015F [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0160   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160: 6E F8 FF FF 7F 1A 80 99  F8 FF FF 7F 00           n............   
```

#### Opcodes

```
  0: 0x0160 [0x6E] EventEntity uses emote 21*
  1: 0x0167 [0x99] Wait for EventEntity animation to complete
  2: 0x016C [0x00] END_REQSTACK()
```
