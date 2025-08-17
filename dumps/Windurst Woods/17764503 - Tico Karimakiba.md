# 17764503 - Tico Karimakiba

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 584 bytes                |
| Total Events     | 22                       |
| References Count | 18                       |

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
| [65535.9](#event-655359)   | 0x008D       |     16 |              2 |
| [65535.10](#event-6553510) | 0x009D       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00AB       |      9 |              3 |
| [361](#event-361)          | 0x00B4       |    120 |             25 |
| [65535.12](#event-6553512) | 0x012C       |     23 |              7 |
| [65535.13](#event-6553513) | 0x0143       |     19 |              5 |
| [65535.14](#event-6553514) | 0x0156       |     19 |              5 |
| [65535.15](#event-6553515) | 0x0169       |      5 |              3 |
| [65535.16](#event-6553516) | 0x016E       |      5 |              3 |
| [65535.17](#event-6553517) | 0x0173       |      5 |              3 |
| [65535.18](#event-6553518) | 0x0178       |      5 |              3 |
| [65535.19](#event-6553519) | 0x017D       |      5 |              3 |
| [65535.20](#event-6553520) | 0x0182       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x0008      |           8 |
|       3 | 0x2070      |        8304 |
|       4 | 0x0001      |           1 |
|       5 | 0x0000      |           0 |
|       6 | 0xFFFFFFFC  |  4294967292 |
|       7 | 0x0002      |           2 |
|       8 | 0x206E      |        8302 |
|       9 | 0x206F      |        8303 |
|      10 | 0x2071      |        8305 |
|      11 | 0x2072      |        8306 |
|      12 | 0x2073      |        8307 |
|      13 | 0x2074      |        8308 |
|      14 | 0x2075      |        8309 |
|      15 | 0x2076      |        8310 |
|      16 | 0x2077      |        8311 |
|      17 | 0x2078      |        8312 |

## String References

- **8302**: Hey! What do you want? Don't tell me...
- **8303**: You heard that I have a monster correlation chart and came to beg me to show it to you, rrright?
- **8304**: Look at the tattered diagram? [Yes./No.]
- **8305**: Oh, so you're just trying to flirt with me, huh? Well, sorry there, but I'm not interrrested in men or women. The only thing that makes my heart leap are the tracks and droppings of my next hunting game, thank you.
- **8306**: I knew it! Alrrright then. I don't mind showing it to you. Besides, I'm a topnotch hunter, so I don't need it anyway.
- **8307**: I was given this parchment a few years ago by a scrrruffy old Elvaan man. I helped him out when I found him lost in the woods, and this was his way of paying me back.
- **8308**: To tell you the truth, I wasn't that interested in it, so I didn't pay much attention to his explanation and have forrrgotten most of what he said.
- **8309**: It was something about how the different types of monsters eat each other in order to surrrvive, so I guess he was trying to tell me to referrr to this pattern when I go hunting.
- **8310**: But whenever I spot a monster, I become totally obsessed by the thought of the hunt and forrrget all about his advice and this chart.
- **8311**: Maybe it's enough to just keep this knowledge locked away in the back of your mind somewhere, in case you ever need it. But if you want to know more, then you'll just have to go and track down that old guy.
- **8312**: You're welcome to have another gander at this chart whenever you want to. It's a pain to explain it to everyone who asks, but maybe it is some kind of fate... Actually, I've found that I enjoy helping people out.

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
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
0030: FF 7F 64 69 73 30 00                              ..dis0.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=50*
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
0040: 64 69 73 30 00                                    dis0.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
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
0040:                81 00 F8  FF FF 7F 66 00 80 F8 FF       ......f....
0050: FF 7F F8 FF FF 7F 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x0045 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=50*
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
0060:                             66 00 80 F8 FF FF 7F           f......
0070: F8 FF FF 7F 74 68 6B 32  00                       ....thk2.       
```

#### Opcodes

```
  0: 0x0069 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=50*
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
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         66 02 80               f..
0090: F8 FF FF 7F F8 FF FF 7F  75 72 65 30 00           ........ure0.   
```

#### Opcodes

```
  0: 0x008D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ure0" with entities [EventEntity, EventEntity], work=8*
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         53 F8 FF               S..
00A0: FF 7F F8 FF FF 7F 75 72  65 30 00                 ......ure0.     
```

#### Opcodes

```
  0: 0x009D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ure0" with entities [EventEntity, EventEntity]
  1: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AB  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   5E 69 64 6C 30             ^idl0
00B0: 1C 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00AB [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00B0 [0x1C] WAIT(30* ticks)
  2: 0x00B3 [0x00] END_REQSTACK()
```

### Event 361

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00B4    |
| Data Size    | 120 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             1E F0 FF FF  7F 6F 70 29 0B 97 10 0F      .....op)....
00C0: 01 0D 24 03 80 04 80 05  80 25 02 00 10 05 80 00  ..$......%......
00D0: 11 01 03 01 10 04 80 29  0B 97 10 0F 01 0F 8D 06  .......)........
00E0: 80 07 80 29 0B 97 10 0F  01 10 29 0B 97 10 0F 01  ...)......).....
00F0: 11 29 0B 97 10 0F 01 12  29 0B 97 10 0F 01 13 29  .)......)......)
0100: 0B 97 10 0F 01 14 8A 29  0B 97 10 0F 01 15 01 28  .......).......(
0110: 01 02 00 10 04 80 00 28  01 03 01 10 07 80 29 0B  .......(......).
0120: 97 10 0F 01 0E 01 28 01  20 00 21 00              ......(. .!.    
```

#### Opcodes

```
  0: 0x00B4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00BB [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x0D)
  4: 0x00C2 [0x24] CREATE_DIALOG(message_id=8304*, default_option=1*, option_flags=0*)
    → "Look at the tattered diagram? [Yes./No.]"
  5: 0x00C9 [0x25] WAIT_DIALOG_SELECT()
  6: 0x00CA [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0111
  7: 0x00D2 [0x03] Work_Zone[1] = 1*
  8: 0x00D7 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x0F)
  9: 0x00DE [0x8D] OPEN_MAP_WITH_PROPERTIES(map_id=4294967292*, properties=2*)
 10: 0x00E3 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x10)
 11: 0x00EA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x11)
 12: 0x00F1 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x12)
 13: 0x00F8 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x13)
 14: 0x00FF [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x14)
 15: 0x0106 [0x8A] CLOSE_MAP()
 16: 0x0107 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x15)
 17: 0x010E [0x01] GOTO 0x0128
 18: 0x0111 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0128
 19: 0x0119 [0x03] Work_Zone[1] = 2*
 20: 0x011E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x0E)
 21: 0x0125 [0x01] GOTO 0x0128

SUBROUTINE_0128:
 22: 0x0128 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 23: 0x012A [0x21] END_EVENT
 24: 0x012B [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012C   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                      29 08 97 10              )...
0130: 0F 01 01 1D 08 80 23 1D  09 80 23 29 08 97 10 0F  ......#...#)....
0140: 01 02 00                                          ...             
```

#### Opcodes

```
  0: 0x012C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x01)
  1: 0x0133 [0x1D] PRINT_EVENT_MESSAGE(message_id=8302*)
    → "Hey! What do you want? Don't tell me..."
  2: 0x0136 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0137 [0x1D] PRINT_EVENT_MESSAGE(message_id=8303*)
    → "You heard that I have a monster correlation chart and came to beg me to show it to you, rrright?"
  4: 0x013A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x013B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x02)
  6: 0x0142 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0143   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:          29 08 97 10 0F  01 03 1D 0A 80 23 29 08     ).........#).
0150: 97 10 0F 01 04 00                                 ......          
```

#### Opcodes

```
  0: 0x0143 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x03)
  1: 0x014A [0x1D] PRINT_EVENT_MESSAGE(message_id=8305*)
    → "Oh, so you're just trying to flirt with me, huh? Well, sorry there, but I'm not interrrested in men or women. The only thing that makes my heart leap are the tracks and droppings of my next hunting game, thank you."
  2: 0x014D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x014E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x04)
  4: 0x0155 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   29 08  97 10 0F 01 03 1D 0B 80        ).........
0160: 23 29 08 97 10 0F 01 04  00                       #).......       
```

#### Opcodes

```
  0: 0x0156 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x03)
  1: 0x015D [0x1D] PRINT_EVENT_MESSAGE(message_id=8306*)
    → "I knew it! Alrrright then. I don't mind showing it to you. Besides, I'm a topnotch hunter, so I don't need it anyway."
  2: 0x0160 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0161 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x04)
  4: 0x0168 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0169  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                             1D 0C 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0169 [0x1D] PRINT_EVENT_MESSAGE(message_id=8307*)
    → "I was given this parchment a few years ago by a scrrruffy old Elvaan man. I helped him out when I found him lost in the woods, and this was his way of paying me back."
  1: 0x016C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x016D [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x016E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                            1D 0D                ..
0170: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x016E [0x1D] PRINT_EVENT_MESSAGE(message_id=8308*)
    → "To tell you the truth, I wasn't that interested in it, so I didn't pay much attention to his explanation and have forrrgotten most of what he said."
  1: 0x0171 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0172 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0173  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:          1D 0E 80 23 00                              ...#.        
```

#### Opcodes

```
  0: 0x0173 [0x1D] PRINT_EVENT_MESSAGE(message_id=8309*)
    → "It was something about how the different types of monsters eat each other in order to surrrvive, so I guess he was trying to tell me to referrr to this pattern when I go hunting."
  1: 0x0176 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0177 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0178  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                          1D 0F 80 23 00                   ...#.   
```

#### Opcodes

```
  0: 0x0178 [0x1D] PRINT_EVENT_MESSAGE(message_id=8310*)
    → "But whenever I spot a monster, I become totally obsessed by the thought of the hunt and forrrget all about his advice and this chart."
  1: 0x017B [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x017C [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x017D  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                         1D 10 80               ...
0180: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x017D [0x1D] PRINT_EVENT_MESSAGE(message_id=8311*)
    → "Maybe it's enough to just keep this knowledge locked away in the back of your mind somewhere, in case you ever need it. But if you want to know more, then you'll just have to go and track down that old guy."
  1: 0x0180 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0181 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0182   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:       29 08 97 10 0F 01  01 1D 11 80 23 29 08 97    ).........#)..
0190: 10 0F 01 02 00                                    .....           
```

#### Opcodes

```
  0: 0x0182 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x01)
  1: 0x0189 [0x1D] PRINT_EVENT_MESSAGE(message_id=8312*)
    → "You're welcome to have another gander at this chart whenever you want to. It's a pain to explain it to everyone who asks, but maybe it is some kind of fate... Actually, I've found that I enjoy helping people out."
  2: 0x018C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x018D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tico Karimakiba (ID: 17764503/0x010F1097), tag_num=0x02)
  4: 0x0194 [0x00] END_REQSTACK()
```
