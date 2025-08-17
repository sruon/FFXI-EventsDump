# 17801237 - Thali Mhobrum

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 584 bytes        |
| Total Events     | 26               |
| References Count | 6                |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0037       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0045       |     22 |              3 |
| [65535.6](#event-655356)   | 0x005B       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0069       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0079       |     20 |              3 |
| [65535.9](#event-655359)   | 0x008D       |     22 |              3 |
| [65535.10](#event-6553510) | 0x00A3       |     20 |              3 |
| [65535.11](#event-6553511) | 0x00B7       |     22 |              3 |
| [65535.12](#event-6553512) | 0x00CD       |     20 |              3 |
| [65535.13](#event-6553513) | 0x00E1       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00F1       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00FF       |     16 |              2 |
| [65535.16](#event-6553516) | 0x010F       |     14 |              2 |
| [65535.17](#event-6553517) | 0x011D       |     16 |              2 |
| [65535.18](#event-6553518) | 0x012D       |     14 |              2 |
| [65535.19](#event-6553519) | 0x013B       |     28 |              4 |
| [65535.20](#event-6553520) | 0x0157       |     26 |              4 |
| [65535.21](#event-6553521) | 0x0171       |      9 |              3 |
| [190](#event-190)          | 0x017A       |     29 |             10 |
| [163](#event-163)          | 0x0197       |     29 |             10 |
| [299](#event-299)          | 0x01B4       |      1 |              1 |
| [301](#event-301)          | 0x01B5       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0166      |         358 |
|       1 | 0x001E      |          30 |
|       2 | 0x016C      |         364 |
|       3 | 0x0168      |         360 |
|       4 | 0x2736      |       10038 |
|       5 | 0x2882      |       10370 |

## String References

- **10038**: When it comes to knife-throwing, there isn't a soul that can match the skill of our chieftainness. I advise staying on herrr good side.
- **10370**: When it comes to knife-throwing, there isn't a soul that can match the skill of our chieftainness. And with a stench like that, she could probably hit you with her eyes closed.

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=358*
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
0020:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 74 6C 6B 32 00                              ..tlk2.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=358*
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
0040: 74 6C 6B 32 00                                    tlk2.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                81 00 F8  FF FF 7F 5B 00 80 F8 FF       ......[....
0050: FF 7F F8 FF FF 7F 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x0045 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=358*
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   53 F8 FF FF 7F             S....
0060: F8 FF FF 7F 74 68 6B 31  00                       ....thk1.       
```

#### Opcodes

```
  0: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             5B 00 80 F8 FF FF 7F           [......
0070: F8 FF FF 7F 74 68 6B 32  00                       ....thk2.       
```

#### Opcodes

```
  0: 0x0069 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=358*
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             53 F8 FF FF 7F F8 FF           S......
0080: FF 7F 74 68 6B 32 81 01  F8 FF FF 7F 00           ..thk2.......   
```

#### Opcodes

```
  0: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0086 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         81 00 F8               ...
0090: FF FF 7F 5B 00 80 F8 FF  FF 7F F8 FF FF 7F 73 69  ...[..........si
00A0: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x008D [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0093 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sis0" with entities [EventEntity, EventEntity], work=358*
  2: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          53 F8 FF FF 7F  F8 FF FF 7F 73 69 73 30     S........sis0
00B0: 81 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x00A3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sis0" with entities [EventEntity, EventEntity]
  1: 0x00B0 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      7C  00 F8 FF FF 7F 5B 00 80         |.....[..
00C0: F8 FF FF 7F F8 FF FF 7F  67 75 74 30 00           ........gut0.   
```

#### Opcodes

```
  0: 0x00B7 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x00BD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gut0" with entities [EventEntity, EventEntity], work=358*
  2: 0x00CC [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CD   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         53 F8 FF               S..
00D0: FF 7F F8 FF FF 7F 67 75  74 30 7C 01 F8 FF FF 7F  ......gut0|.....
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00CD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gut0" with entities [EventEntity, EventEntity]
  1: 0x00DA [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    5B 02 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 30   [..........poi0
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=364*
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    53 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 30 00      S........poi0. 
```

#### Opcodes

```
  0: 0x00F1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x00FE [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               5B                 [
0100: 03 80 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 31 00     ..........poi1. 
```

#### Opcodes

```
  0: 0x00FF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=360*
  1: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               53                 S
0110: F8 FF FF 7F F8 FF FF 7F  70 6F 69 31 00           ........poi1.   
```

#### Opcodes

```
  0: 0x010F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
  1: 0x011C [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         5B 03 80               [..
0120: F8 FF FF 7F F8 FF FF 7F  70 6F 69 33 00           ........poi3.   
```

#### Opcodes

```
  0: 0x011D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi3" with entities [EventEntity, EventEntity], work=360*
  1: 0x012C [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         53 F8 FF               S..
0130: FF 7F F8 FF FF 7F 70 6F  69 33 00                 ......poi3.     
```

#### Opcodes

```
  0: 0x012D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi3" with entities [EventEntity, EventEntity]
  1: 0x013A [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013B   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   7C 00 F8 FF FF             |....
0140: 7F 81 00 F8 FF FF 7F 5B  02 80 F8 FF FF 7F F8 FF  .......[........
0150: FF 7F 61 6E 67 30 00                              ..ang0.         
```

#### Opcodes

```
  0: 0x013B [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0141 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  2: 0x0147 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=364*
  3: 0x0156 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0157   |
| Data Size    | 26 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0160: 61 6E 67 30 7C 01 F8 FF  FF 7F 81 01 F8 FF FF 7F  ang0|...........
0170: 00                                                .               
```

#### Opcodes

```
  0: 0x0157 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
  1: 0x0164 [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x016A [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  3: 0x0170 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0171  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0171 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0176 [0x1C] WAIT(30* ticks)
  2: 0x0179 [0x00] END_REQSTACK()
```

### Event 190

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017A   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                1E F0 FF FF 7F 6F            .....o
0180: 70 29 08 15 A0 0F 01 01  1D 04 80 23 29 08 15 A0  p).........#)...
0190: 0F 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x017A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x017F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0180 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0181 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Thali Mhobrum (ID: 17801237/0x010FA015), tag_num=0x01)
  4: 0x0188 [0x1D] PRINT_EVENT_MESSAGE(message_id=10038*)
    → "When it comes to knife-throwing, there isn't a soul that can match the skill of our chieftainness. I advise staying on herrr good side."
  5: 0x018B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x018C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Thali Mhobrum (ID: 17801237/0x010FA015), tag_num=0x02)
  7: 0x0193 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0195 [0x21] END_EVENT
  9: 0x0196 [0x00] END_REQSTACK()
```

### Event 163

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0197   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                      1E  F0 FF FF 7F 6F 70 29 08         .....op).
01A0: 15 A0 0F 01 01 1D 05 80  23 29 08 15 A0 0F 01 02  ........#)......
01B0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0197 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x019C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x019D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x019E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Thali Mhobrum (ID: 17801237/0x010FA015), tag_num=0x01)
  4: 0x01A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=10370*)
    → "When it comes to knife-throwing, there isn't a soul that can match the skill of our chieftainness. And with a stench like that, she could probably hit you with her eyes closed."
  5: 0x01A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01A9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Thali Mhobrum (ID: 17801237/0x010FA015), tag_num=0x02)
  7: 0x01B0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x01B2 [0x21] END_EVENT
  9: 0x01B3 [0x00] END_REQSTACK()
```

### Event 299

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:             00                                        .           
```

#### Opcodes

```
  0: 0x01B4 [0x00] END_REQSTACK()
```

### Event 301

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                00                                      .          
```

#### Opcodes

```
  0: 0x01B5 [0x00] END_REQSTACK()
```
