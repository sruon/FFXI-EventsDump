# 17473771 - Yoran-Oran

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 488 bytes                    |
| Total Events     | 16                           |
| References Count | 27                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     35 |              5 |
| [63](#event-63)            | 0x0024       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0025       |     23 |              5 |
| [65535.3](#event-655353)   | 0x003C       |     16 |              2 |
| [65535.4](#event-655354)   | 0x004C       |     16 |              2 |
| [65535.5](#event-655355)   | 0x005C       |     20 |              6 |
| [64](#event-64)            | 0x0070       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0071       |     14 |              4 |
| [65535.7](#event-655357)   | 0x007F       |     14 |              4 |
| [65535.8](#event-655358)   | 0x008D       |     14 |              4 |
| [65535.9](#event-655359)   | 0x009B       |     19 |              3 |
| [65535.10](#event-6553510) | 0x00AE       |     19 |              3 |
| [65535.11](#event-6553511) | 0x00C1       |     13 |              3 |
| [65535.12](#event-6553512) | 0x00CE       |     48 |              8 |
| [65535.13](#event-6553513) | 0x00FE       |     43 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x000D      |          13 |
|       2 | 0x0013      |          19 |
|       3 | 0x0017      |          23 |
|       4 | 0x0000      |           0 |
|       5 | 0x001E      |          30 |
|       6 | 0xFFFF12B2  |  4294906546 |
|       7 | 0xC724      |       50980 |
|       8 | 0x2640      |        9792 |
|       9 | 0x0031      |          49 |
|      10 | 0x000A      |          10 |
|      11 | 0xFFFF133D  |  4294906685 |
|      12 | 0xCB02      |       51970 |
|      13 | 0xFFFF15A0  |  4294907296 |
|      14 | 0xE060      |       57440 |
|      15 | 0x24D6      |        9430 |
|      16 | 0xEDE4      |       60900 |
|      17 | 0x24C0      |        9408 |
|      18 | 0x0028      |          40 |
|      19 | 0x9C40      |       40000 |
|      20 | 0x25E7      |        9703 |
|      21 | 0x00AC      |         172 |
|      22 | 0x003C      |          60 |
|      23 | 0x0015      |          21 |
|      24 | 0x0AD2      |        2770 |
|      25 | 0x008C      |         140 |
|      26 | 0x005C      |          92 |

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

### Event 63

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
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 05 80  1F 00 06 80 07 80 08 80       2..........
0030: 1F 01 4A F8 FF FF 7F E8  A0 0A 01 00              ..J.........    
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.750*, Z=50.980*, Y=9.792*
  2: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0032 [0x4A] EventEntity looks at Shantotto (ID: 17473768/0x010AA0E8)
  4: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      66 09 80 F8              f...
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 30 00              .......tlk0.    
```

#### Opcodes

```
  0: 0x003C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  1: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      66 09 80 F8              f...
0050: FF FF 7F F8 FF FF 7F 74  6C 6B 31 00              .......tlk1.    
```

#### Opcodes

```
  0: 0x004C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      7B F8 FF FF              {...
0060: 7F 32 0A 80 1F 00 0B 80  0C 80 08 80 1F 01 6F 00  .2............o.
```

#### Opcodes

```
  0: 0x005C [0x7B] EventEntity stops talking
  1: 0x0061 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  2: 0x0064 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.611*, Z=51.970*, Y=9.792*
  3: 0x006C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x006E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x006F [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0070  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    32 01 80 1F 00 0D 80  0E 80 0F 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0071 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.000*, Z=57.440*, Y=9.430*
  2: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               32                 2
0080: 01 80 1F 00 0D 80 10 80  11 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x007F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.000*, Z=60.900*, Y=9.408*
  2: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         32 12 80               2..
0090: 1F 00 0D 80 13 80 14 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x008D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0090 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.000*, Z=40.000*, Y=9.703*
  2: 0x0098 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   66 12 80 F8 FF             f....
00A0: FF 7F F8 FF FF 7F 67 6B  72 30 1C 15 80 00        ......gkr0....  
```

#### Opcodes

```
  0: 0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00AA [0x1C] WAIT(172* ticks)
  2: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            66 12                f.
00B0: 80 F8 FF FF 7F F8 FF FF  7F 67 6B 72 31 1C 16 80  .........gkr1...
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr1" with entities [EventEntity, EventEntity], work=40*
  1: 0x00BD [0x1C] WAIT(60* ticks)
  2: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    6E F8 FF FF 7F 17 80  99 F8 FF FF 7F 00         n............  
```

#### Opcodes

```
  0: 0x00C1 [0x6E] EventEntity uses emote 21*
  1: 0x00C8 [0x99] Wait for EventEntity animation to complete
  2: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 48 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            7B F8                {.
00D0: FF FF 7F 81 00 F8 FF FF  7F 7C 00 F8 FF FF 7F 5B  .........|.....[
00E0: 18 80 F8 FF FF 7F F8 FF  FF 7F 7A 74 75 30 1C 19  ..........ztu0..
00F0: 80 81 01 F8 FF FF 7F 7C  01 F8 FF FF 7F 00        .......|......  
```

#### Opcodes

```
  0: 0x00CE [0x7B] EventEntity stops talking
  1: 0x00D3 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  2: 0x00D9 [0x7C] EventEntity->Render.Flags2 |= 0x00
  3: 0x00DF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ztu0" with entities [EventEntity, EventEntity], work=2770*
  4: 0x00EE [0x1C] WAIT(140* ticks)
  5: 0x00F1 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  6: 0x00F7 [0x7C] EventEntity->Render.Flags2 |= 0x01
  7: 0x00FD [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FE   |
| Data Size    | 43 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            81 00                ..
0100: F8 FF FF 7F 7C 00 F8 FF  FF 7F 5B 18 80 F8 FF FF  ....|.....[.....
0110: 7F F8 FF FF 7F 7A 74 75  31 1C 1A 80 81 01 F8 FF  .....ztu1.......
0120: FF 7F 7C 01 F8 FF FF 7F  00                       ..|......       
```

#### Opcodes

```
  0: 0x00FE [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0104 [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x010A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ztu1" with entities [EventEntity, EventEntity], work=2770*
  3: 0x0119 [0x1C] WAIT(92* ticks)
  4: 0x011C [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  5: 0x0122 [0x7C] EventEntity->Render.Flags2 |= 0x01
  6: 0x0128 [0x00] END_REQSTACK()
```
