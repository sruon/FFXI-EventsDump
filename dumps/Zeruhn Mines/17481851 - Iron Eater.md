# 17481851 - Iron Eater

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Zeruhn Mines (ID: 172) |
| Block Size       | 668 bytes              |
| Total Events     | 30                     |
| References Count | 29                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [200](#event-200)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     26 |              7 |
| [65535.2](#event-655352)   | 0x001C       |     14 |              4 |
| [202](#event-202)          | 0x002A       |      1 |              1 |
| [231](#event-231)          | 0x002B       |      7 |              2 |
| [65535.3](#event-655353)   | 0x0032       |     15 |              5 |
| [65535.4](#event-655354)   | 0x0041       |     15 |              5 |
| [65535.5](#event-655355)   | 0x0050       |     15 |              5 |
| [65535.6](#event-655356)   | 0x005F       |     16 |              2 |
| [65535.7](#event-655357)   | 0x006F       |     14 |              2 |
| [65535.8](#event-655358)   | 0x007D       |     16 |              2 |
| [65535.9](#event-655359)   | 0x008D       |     14 |              2 |
| [65535.10](#event-6553510) | 0x009B       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00AB       |     14 |              2 |
| [65535.12](#event-6553512) | 0x00B9       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00C9       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00D7       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00E7       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00F5       |     16 |              4 |
| [65535.17](#event-6553517) | 0x0105       |     16 |              4 |
| [65535.18](#event-6553518) | 0x0115       |     16 |              4 |
| [65535.19](#event-6553519) | 0x0125       |     16 |              4 |
| [65535.20](#event-6553520) | 0x0135       |     16 |              4 |
| [65535.21](#event-6553521) | 0x0145       |     16 |              4 |
| [65535.22](#event-6553522) | 0x0155       |     16 |              4 |
| [65535.23](#event-6553523) | 0x0165       |     16 |              4 |
| [65535.24](#event-6553524) | 0x0175       |     16 |              4 |
| [65535.25](#event-6553525) | 0x0185       |     16 |              4 |
| [65535.26](#event-6553526) | 0x0195       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFEF643  |  4294899267 |
|       2 | 0xECED      |       60653 |
|       3 | 0x0000      |           0 |
|       4 | 0x0911      |        2321 |
|       5 | 0xFFFEDCDE  |  4294892766 |
|       6 | 0xE999      |       59801 |
|       7 | 0x0022      |          34 |
|       8 | 0x0E17      |        3607 |
|       9 | 0xFFFE06A4  |  4294837924 |
|      10 | 0x245C      |        9308 |
|      11 | 0x0BA7      |        2983 |
|      12 | 0xFFFDF8A0  |  4294834336 |
|      13 | 0x2527      |        9511 |
|      14 | 0x071E      |        1822 |
|      15 | 0xFFFDD9D9  |  4294826457 |
|      16 | 0x2615      |        9749 |
|      17 | 0x0045      |          69 |
|      18 | 0x0083      |         131 |
|      19 | 0x0015      |          21 |
|      20 | 0x003C      |          60 |
|      21 | 0x0007      |           7 |
|      22 | 0x0006      |           6 |
|      23 | 0x000B      |          11 |
|      24 | 0x000E      |          14 |
|      25 | 0x0004      |           4 |
|      26 | 0x0013      |          19 |
|      27 | 0x000C      |          12 |
|      28 | 0x001D      |          29 |

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

### Event 200

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
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 32 00 80 37  01 80 02 80 03 80 04 80    ".2..7........
0010: 1F 00 05 80 06 80 07 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-68.029*, z=60.653*, y=0.000*, direction=204.0°*
  3: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=-74.530*, Z=59.801*, Y=0.034*
  4: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      32 00 80 1F              2...
0020: 00 01 80 02 80 03 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x001C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001F [0x1F] MOVE_ENTITY: EventEntity moves to X=-68.029*, Z=60.653*, Y=0.000*
  2: 0x0027 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0029 [0x00] END_REQSTACK()
```

### Event 202

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                00                           .     
```

#### Opcodes

```
  0: 0x002A [0x00] END_REQSTACK()
```

### Event 231

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   92 01 F8 FF FF             .....
0030: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x002B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       32 00 80 1F 00 08  80 09 80 0A 80 1F 01 6F    2............o
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0032 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0035 [0x1F] MOVE_ENTITY: EventEntity moves to X=3.607*, Z=-129.372*, Y=9.308*
  2: 0x003D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    32 00 80 1F 00 0B 80  0C 80 0D 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0041 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.983*, Z=-132.960*, Y=9.511*
  2: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 00 80 1F 00 0E 80 0F  80 10 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.822*, Z=-140.839*, Y=9.749*
  2: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               66                 f
0060: 11 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00     ..........tlk0. 
```

#### Opcodes

```
  0: 0x005F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  1: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               53                 S
0070: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 00           ........tlk0.   
```

#### Opcodes

```
  0: 0x006F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         66 11 80               f..
0080: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x007D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=69*
  1: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         53 F8 FF               S..
0090: FF 7F F8 FF FF 7F 74 6C  6B 31 00                 ......tlk1.     
```

#### Opcodes

```
  0: 0x008D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   66 12 80 F8 FF             f....
00A0: FF 7F F8 FF FF 7F 70 61  73 30 00                 ......pas0.     
```

#### Opcodes

```
  0: 0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=131*
  1: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   53 F8 FF FF 7F             S....
00B0: F8 FF FF 7F 70 61 73 30  00                       ....pas0.       
```

#### Opcodes

```
  0: 0x00AB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             66 11 80 F8 FF FF 7F           f......
00C0: F8 FF FF 7F 74 68 6B 31  00                       ....thk1.       
```

#### Opcodes

```
  0: 0x00B9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=69*
  1: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             53 F8 FF FF 7F F8 FF           S......
00D0: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x00C9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x00D6 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      66  11 80 F8 FF FF 7F F8 FF         f........
00E0: FF 7F 74 68 6B 32 00                              ..thk2.         
```

#### Opcodes

```
  0: 0x00D7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=69*
  1: 0x00E6 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00F0: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x00E7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                6E F8 FF  FF 7F 13 80 99 F8 FF FF       n..........
0100: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x00F5 [0x6E] EventEntity uses emote 21*
  1: 0x00FC [0x99] Wait for EventEntity animation to complete
  2: 0x0101 [0x1C] WAIT(60* ticks)
  3: 0x0104 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0105   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                6E F8 FF  FF 7F 15 80 99 F8 FF FF       n..........
0110: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0105 [0x6E] EventEntity uses emote 7*
  1: 0x010C [0x99] Wait for EventEntity animation to complete
  2: 0x0111 [0x1C] WAIT(60* ticks)
  3: 0x0114 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0115   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                6E F8 FF  FF 7F 16 80 99 F8 FF FF       n..........
0120: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0115 [0x6E] EventEntity uses emote 6*
  1: 0x011C [0x99] Wait for EventEntity animation to complete
  2: 0x0121 [0x1C] WAIT(60* ticks)
  3: 0x0124 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0125   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                6E F8 FF  FF 7F 17 80 99 F8 FF FF       n..........
0130: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0125 [0x6E] EventEntity uses emote 11*
  1: 0x012C [0x99] Wait for EventEntity animation to complete
  2: 0x0131 [0x1C] WAIT(60* ticks)
  3: 0x0134 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0135   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                6E F8 FF  FF 7F 18 80 99 F8 FF FF       n..........
0140: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0135 [0x6E] EventEntity uses emote 14*
  1: 0x013C [0x99] Wait for EventEntity animation to complete
  2: 0x0141 [0x1C] WAIT(60* ticks)
  3: 0x0144 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0145   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                6E F8 FF  FF 7F 19 80 99 F8 FF FF       n..........
0150: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0145 [0x6E] EventEntity uses emote 4*
  1: 0x014C [0x99] Wait for EventEntity animation to complete
  2: 0x0151 [0x1C] WAIT(60* ticks)
  3: 0x0154 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0155   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                6E F8 FF  FF 7F 1A 80 99 F8 FF FF       n..........
0160: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0155 [0x6E] EventEntity uses emote 19*
  1: 0x015C [0x99] Wait for EventEntity animation to complete
  2: 0x0161 [0x1C] WAIT(60* ticks)
  3: 0x0164 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0165   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                6E F8 FF  FF 7F 1B 80 99 F8 FF FF       n..........
0170: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0165 [0x6E] EventEntity uses emote 12*
  1: 0x016C [0x99] Wait for EventEntity animation to complete
  2: 0x0171 [0x1C] WAIT(60* ticks)
  3: 0x0174 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0175   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                6E F8 FF  FF 7F 1B 80 99 F8 FF FF       n..........
0180: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0175 [0x6E] EventEntity uses emote 12*
  1: 0x017C [0x99] Wait for EventEntity animation to complete
  2: 0x0181 [0x1C] WAIT(60* ticks)
  3: 0x0184 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0185   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                6E F8 FF  FF 7F 1C 80 99 F8 FF FF       n..........
0190: 7F 1C 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0185 [0x6E] EventEntity uses emote 29*
  1: 0x018C [0x99] Wait for EventEntity animation to complete
  2: 0x0191 [0x1C] WAIT(60* ticks)
  3: 0x0194 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0195  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                5E 69 64  6C 30 1C 14 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x0195 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x019A [0x1C] WAIT(60* ticks)
  2: 0x019D [0x00] END_REQSTACK()
```
