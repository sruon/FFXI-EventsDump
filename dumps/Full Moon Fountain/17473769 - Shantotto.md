# 17473769 - Shantotto

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 540 bytes                    |
| Total Events     | 19                           |
| References Count | 23                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     37 |              5 |
| [65535.2](#event-655352)   | 0x0026       |     51 |             13 |
| [65535.3](#event-655353)   | 0x0059       |     25 |              3 |
| [65535.4](#event-655354)   | 0x0072       |     10 |              2 |
| [65535.5](#event-655355)   | 0x007C       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0086       |      2 |              2 |
| [64](#event-64)            | 0x0088       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0089       |     23 |              5 |
| [65535.8](#event-655358)   | 0x00A0       |     14 |              4 |
| [65535.9](#event-655359)   | 0x00AE       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00BE       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00CE       |     19 |              3 |
| [65535.12](#event-6553512) | 0x00E1       |     19 |              3 |
| [65535.13](#event-6553513) | 0x00F4       |     16 |              2 |
| [65535.14](#event-6553514) | 0x0104       |     19 |              3 |
| [65535.15](#event-6553515) | 0x0117       |     19 |              3 |
| [65535.16](#event-6553516) | 0x012A       |     36 |              6 |
| [65535.17](#event-6553517) | 0x014E       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0AC7      |        2759 |
|       1 | 0x0046      |          70 |
|       2 | 0x005A      |          90 |
|       3 | 0x0000      |           0 |
|       4 | 0x02BC      |         700 |
|       5 | 0x0941      |        2369 |
|       6 | 0x0080      |         128 |
|       7 | 0x000E      |          14 |
|       8 | 0xFFFF12AE  |  4294906542 |
|       9 | 0xE7D6      |       59350 |
|      10 | 0x24F4      |        9460 |
|      11 | 0x000F      |          15 |
|      12 | 0xFFFF12F8  |  4294906616 |
|      13 | 0xED4E      |       60750 |
|      14 | 0x24CA      |        9418 |
|      15 | 0x0AC8      |        2760 |
|      16 | 0x0043      |          67 |
|      17 | 0x003C      |          60 |
|      18 | 0x006F      |         111 |
|      19 | 0x0061      |          97 |
|      20 | 0x0AD9      |        2777 |
|      21 | 0x00D2      |         210 |
|      22 | 0x0050      |          80 |

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
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 62 6F 68 30   [..........boh0
0010: 6C F8 FF FF 7F 01 80 02  80 1C 02 80 6C F8 FF FF  l...........l...
0020: 7F 03 80 04 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "boh0" with entities [EventEntity, EventEntity], work=2759*
  1: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=70*, fade_time=90*)
  2: 0x0019 [0x1C] WAIT(90* ticks)
  3: 0x001C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=700*)
  4: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 51 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   B7 01  01 00 F8 FF FF 7F B4 13        ..........
0030: 00 00 53 68 61 6E 74 6F  74 74 6F 00 00 00 00 00  ..Shantotto.....
0040: 00 00 B5 00 00 00 B6 00  05 80 22 00 92 01 F8 FF  ..........".....
0050: FF 7F 94 01 F8 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x0026 [0xB7] ENTITY_DATA_HANDLER: Set Unknown NPC (ID: 4294443009/0xFFF80001) name from 0x7FFF (monstrosity: 0x13B4)
  1: 0x0030 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0031 [0x00] END_REQSTACK()
     0x0032 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler 0x00000000 with entities [Unknown NPC (ID: 1953390952/0x746E6168), Unknown NPC (ID: 1869902959/0x6F74746F)]
     0x003F [0x00] END_REQSTACK()
     0x0040 [0x00] END_REQSTACK()
     0x0041 [0x00] END_REQSTACK()
     0x0042 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
     0x0046 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2369*)
     0x004A [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
     0x004C [0x92] EventEntity->Render.Flags3 ^= 0x01
     0x0052 [0x94] EventEntity->Render.Flags3 ^= 0x01
     0x0058 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             B4 13 00 00 50 72 65           ....Pre
0060: 76 4E 61 6D 65 00 00 00  00 00 00 00 00 B5 00 00  vName...........
0070: 00 00                                             ..              
```

#### Opcodes

```
  0: 0x0059 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="PrevName")
  1: 0x006D [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       6C F8 FF FF 7F 06  80 03 80 00                l.........    
```

#### Opcodes

```
  0: 0x0072 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  1: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      6C F8 FF FF              l...
0080: 7F 03 80 03 80 00                                 ......          
```

#### Opcodes

```
  0: 0x007C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0086  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   84 00                                 ..        
```

#### Opcodes

```
  0: 0x0086 [0x84] ADJUST_RENDER_FLAGS3_BIT0()
  1: 0x0087 [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0088  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          00                               .       
```

#### Opcodes

```
  0: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             32 07 80 1F 00 08 80           2......
0090: 09 80 0A 80 1F 01 4A F8  FF FF 7F E8 A0 0A 01 00  ......J.........
```

#### Opcodes

```
  0: 0x0089 [0x32] ExtData[1]->MainSpeed = 14* * 0.1
  1: 0x008C [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.754*, Z=59.350*, Y=9.460*
  2: 0x0094 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0096 [0x4A] EventEntity looks at Shantotto (ID: 17473768/0x010AA0E8)
  4: 0x009F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A0   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 32 0B 80 1F 00 0C 80 0D  80 0E 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x00A0 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x00A3 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.680*, Z=60.750*, Y=9.418*
  2: 0x00AB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            5B 0F                [.
00B0: 80 F8 FF FF 7F F8 FF FF  7F 6F 68 68 30 00        .........ohh0.  
```

#### Opcodes

```
  0: 0x00AE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ohh0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            5B 0F                [.
00C0: 80 F8 FF FF 7F F8 FF FF  7F 6F 68 68 31 00        .........ohh1.  
```

#### Opcodes

```
  0: 0x00BE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ohh1" with entities [EventEntity, EventEntity], work=2760*
  1: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            5B 00                [.
00D0: 80 F8 FF FF 7F F8 FF FF  7F 62 72 69 30 1C 10 80  .........bri0...
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00CE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bri0" with entities [EventEntity, EventEntity], work=2759*
  1: 0x00DD [0x1C] WAIT(67* ticks)
  2: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 62 72 69 31   [..........bri1
00F0: 1C 11 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00E1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bri1" with entities [EventEntity, EventEntity], work=2759*
  1: 0x00F0 [0x1C] WAIT(60* ticks)
  2: 0x00F3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:             5B 00 80 F8  FF FF 7F F8 FF FF 7F 62      [..........b
0100: 72 69 6C 00                                       ril.            
```

#### Opcodes

```
  0: 0x00F4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bril" with entities [EventEntity, EventEntity], work=2759*
  1: 0x0103 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0104   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             5B 00 80 F8  FF FF 7F F8 FF FF 7F 79      [..........y
0110: 67 6F 30 1C 12 80 00                              go0....         
```

#### Opcodes

```
  0: 0x0104 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ygo0" with entities [EventEntity, EventEntity], work=2759*
  1: 0x0113 [0x1C] WAIT(111* ticks)
  2: 0x0116 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0117   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0120: FF 7F 79 65 73 30 1C 13  80 00                    ..yes0....      
```

#### Opcodes

```
  0: 0x0117 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes0" with entities [EventEntity, EventEntity], work=2759*
  1: 0x0126 [0x1C] WAIT(97* ticks)
  2: 0x0129 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012A   |
| Data Size    | 36 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                7B F8 FF FF 7F 81            {.....
0130: 00 F8 FF FF 7F 5B 14 80  F8 FF FF 7F F8 FF FF 7F  .....[..........
0140: 69 6E 6F 30 1C 15 80 81  01 F8 FF FF 7F 00        ino0..........  
```

#### Opcodes

```
  0: 0x012A [0x7B] EventEntity stops talking
  1: 0x012F [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  2: 0x0135 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=2777*
  3: 0x0144 [0x1C] WAIT(210* ticks)
  4: 0x0147 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  5: 0x014D [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014E   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                            5B 14                [.
0150: 80 F8 FF FF 7F F8 FF FF  7F 69 6E 6F 31 1C 16 80  .........ino1...
0160: 00                                                .               
```

#### Opcodes

```
  0: 0x014E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino1" with entities [EventEntity, EventEntity], work=2777*
  1: 0x015D [0x1C] WAIT(80* ticks)
  2: 0x0160 [0x00] END_REQSTACK()
```
