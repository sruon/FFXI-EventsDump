# 17780965 - Yoran-Oran

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 496 bytes             |
| Total Events     | 17                    |
| References Count | 30                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     35 |              5 |
| [10100](#event-10100)      | 0x0024       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0025       |     30 |              8 |
| [65535.3](#event-655353)   | 0x0043       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0051       |     14 |              4 |
| [65535.5](#event-655355)   | 0x005F       |     16 |              2 |
| [65535.6](#event-655356)   | 0x006F       |     29 |              3 |
| [65535.7](#event-655357)   | 0x008C       |     16 |              2 |
| [65535.8](#event-655358)   | 0x009C       |     29 |              3 |
| [65535.9](#event-655359)   | 0x00B9       |     21 |              5 |
| [65535.10](#event-6553510) | 0x00CE       |     19 |              3 |
| [65535.11](#event-6553511) | 0x00E1       |     19 |              3 |
| [10101](#event-10101)      | 0x00F4       |      1 |              1 |
| [65535.12](#event-6553512) | 0x00F5       |     15 |              5 |
| [65535.13](#event-6553513) | 0x0104       |     15 |              5 |
| [65535.14](#event-6553514) | 0x0113       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x000D      |          13 |
|       2 | 0x0013      |          19 |
|       3 | 0x0017      |          23 |
|       4 | 0x0000      |           0 |
|       5 | 0x0037      |          55 |
|       6 | 0x4570      |       17776 |
|       7 | 0xFFFF2E5C  |  4294913628 |
|       8 | 0x0F3B      |        3899 |
|       9 | 0x001E      |          30 |
|      10 | 0x01F4      |         500 |
|      11 | 0x0032      |          50 |
|      12 | 0x4E66      |       20070 |
|      13 | 0xFFFF2338  |  4294910776 |
|      14 | 0x0F1D      |        3869 |
|      15 | 0x0007      |           7 |
|      16 | 0x4726      |       18214 |
|      17 | 0xFFFF3333  |  4294914867 |
|      18 | 0x0028      |          40 |
|      19 | 0x0031      |          49 |
|      20 | 0x000F      |          15 |
|      21 | 0x0AD2      |        2770 |
|      22 | 0x008C      |         140 |
|      23 | 0x005C      |          92 |
|      24 | 0x003C      |          60 |
|      25 | 0x460E      |       17934 |
|      26 | 0xFFFF2F33  |  4294913843 |
|      27 | 0x0023      |          35 |
|      28 | 0x4E47      |       20039 |
|      29 | 0xFFFF2325  |  4294910757 |

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
0000:    22 00 B6 0B 00 80 01  80 02 80 03 80 03 80 03   "..............
0010: 80 03 80 04 80 04 80 92  01 F8 FF FF 7F 94 01 F8  ................
0020: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=13*, head=19*, body=23*, hands=23*, legs=23*, feet=23*, main=0*, sub=0*)
  2: 0x0017 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x001D [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0023 [0x00] END_REQSTACK()
```

### Event 10100

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
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 05 80  1F 00 06 80 07 80 08 80       2..........
0030: 1F 01 6F 7B F8 FF FF 7F  1C 09 80 4B F8 FF FF 7F  ..o{.......K....
0040: 0A 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 55* * 0.1
  1: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.776*, Z=-53.668*, Y=3.899*
  2: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0033 [0x7B] EventEntity stops talking
  5: 0x0038 [0x1C] WAIT(30* ticks)
  6: 0x003B [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=2.7°*)
  7: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          32 0B 80 1F 00  0C 80 0D 80 0E 80 1F 01     2............
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0043 [0x32] ExtData[1]->MainSpeed = 50* * 0.1
  1: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=20.070*, Z=-56.520*, Y=3.869*
  2: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    32 0F 80 1F 00 10 80  11 80 08 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0051 [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  1: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=18.214*, Z=-52.429*, Y=3.899*
  2: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.5

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
0060: 12 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00     ..........tlk0. 
```

#### Opcodes

```
  0: 0x005F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               66                 f
0070: 12 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
0080: FF FF 7F F8 FF FF 7F 74  6C 6B 31 00              .......tlk1.    
```

#### Opcodes

```
  0: 0x006F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x007E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      66 13 80 F8              f...
0090: FF FF 7F F8 FF FF 7F 74  6C 6B 30 00              .......tlk0.    
```

#### Opcodes

```
  0: 0x008C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  1: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      66 13 80 F8              f...
00A0: FF FF 7F F8 FF FF 7F 74  6C 6B 31 53 F8 FF FF 7F  .......tlk1S....
00B0: F8 FF FF 7F 74 6C 6B 31  00                       ....tlk1.       
```

#### Opcodes

```
  0: 0x009C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  1: 0x00AB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             6E F8 FF FF 7F 0F 80           n......
00C0: 99 F8 FF FF 7F 99 F8 FF  FF 7F 1C 14 80 00        ..............  
```

#### Opcodes

```
  0: 0x00B9 [0x6E] EventEntity uses emote 7*
  1: 0x00C0 [0x99] Wait for EventEntity animation to complete
  2: 0x00C5 [0x99] Wait for EventEntity animation to complete
  3: 0x00CA [0x1C] WAIT(15* ticks)
  4: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            5B 15                [.
00D0: 80 F8 FF FF 7F F8 FF FF  7F 7A 74 75 30 1C 16 80  .........ztu0...
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00CE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ztu0" with entities [EventEntity, EventEntity], work=2770*
  1: 0x00DD [0x1C] WAIT(140* ticks)
  2: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    5B 15 80 F8 FF FF 7F  F8 FF FF 7F 7A 74 75 31   [..........ztu1
00F0: 1C 17 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00E1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ztu1" with entities [EventEntity, EventEntity], work=2770*
  1: 0x00F0 [0x1C] WAIT(92* ticks)
  2: 0x00F3 [0x00] END_REQSTACK()
```

### Event 10101

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:             00                                        .           
```

#### Opcodes

```
  0: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                32 18 80  1F 00 19 80 1A 80 08 80       2..........
0100: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x00F5 [0x32] ExtData[1]->MainSpeed = 60* * 0.1
  1: 0x00F8 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.934*, Z=-53.453*, Y=3.899*
  2: 0x0100 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0102 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0103 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0104   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             32 1B 80 1F  00 1C 80 1D 80 0E 80 1F      2...........
0110: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0104 [0x32] ExtData[1]->MainSpeed = 35* * 0.1
  1: 0x0107 [0x1F] MOVE_ENTITY: EventEntity moves to X=20.039*, Z=-56.539*, Y=3.869*
  2: 0x010F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0111 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0112 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0113   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          32 14 80 1F 00  10 80 11 80 08 80 1F 01     2............
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0113 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x0116 [0x1F] MOVE_ENTITY: EventEntity moves to X=18.214*, Z=-52.429*, Y=3.899*
  2: 0x011E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0120 [0x00] END_REQSTACK()
```
