# 17772698 - Francmage

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 524 bytes                 |
| Total Events     | 26                        |
| References Count | 14                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x005B       |     16 |              2 |
| [65535.8](#event-655358)   | 0x006B       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0079       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0089       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0097       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00A7       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00B5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00C5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00D3       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00E3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00F1       |     12 |              3 |
| [10008](#event-10008)      | 0x00FD       |     12 |              3 |
| [65535.18](#event-6553518) | 0x0109       |     14 |              4 |
| [65535.19](#event-6553519) | 0x0117       |     14 |              4 |
| [65535.20](#event-6553520) | 0x0125       |     19 |              5 |
| [65535.21](#event-6553521) | 0x0138       |      5 |              3 |
| [65535.22](#event-6553522) | 0x013D       |      5 |              3 |
| [65535.23](#event-6553523) | 0x0142       |      5 |              3 |
| [65535.24](#event-6553524) | 0x0147       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x0000      |           0 |
|       2 | 0x58EE      |       22766 |
|       3 | 0xFFFFFA24  |  4294965796 |
|       4 | 0x0B87      |        2951 |
|       5 | 0x000D      |          13 |
|       6 | 0x89D8      |       35288 |
|       7 | 0xFFFFF449  |  4294964297 |
|       8 | 0x791A      |       31002 |
|       9 | 0x1AA2      |        6818 |
|      10 | 0x1AA6      |        6822 |
|      11 | 0x1AAC      |        6828 |
|      12 | 0x1AB0      |        6832 |
|      13 | 0x1AB2      |        6834 |

## String References

- **6818**: You called for me, Your Majesty?
- **6822**: Oh, yes, that. Those Bastoker Humes are causing no end of trouble--saying they want to investigate here, there, and the other place...
- **6828**: As you command, my lord. I would give the very blood that runs in my veins if it were to further the cause of our kingdom. You can rely on me.
- **6832**: I understand, Your Grace.
- **6834**: Yes, sire! My life for the Kingdom!

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00      S........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               66                 f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 00     ..........tlk1. 
```

#### Opcodes

```
  0: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         66 00 80               f..
0040: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 00           ........thk1.   
```

#### Opcodes

```
  0: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         53 F8 FF               S..
0050: FF 7F F8 FF FF 7F 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   66 00 80 F8 FF             f....
0060: FF 7F F8 FF FF 7F 74 68  6B 32 00                 ......thk2.     
```

#### Opcodes

```
  0: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   53 F8 FF FF 7F             S....
0070: F8 FF FF 7F 74 68 6B 32  00                       ....thk2.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             66 00 80 F8 FF FF 7F           f......
0080: F8 FF FF 7F 73 68 61 30  00                       ....sha0.       
```

#### Opcodes

```
  0: 0x0079 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             53 F8 FF FF 7F F8 FF           S......
0090: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x0089 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      66  00 80 F8 FF FF 7F F8 FF         f........
00A0: FF 7F 73 68 61 31 00                              ..sha1.         
```

#### Opcodes

```
  0: 0x0097 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00B0: 73 68 61 31 00                                    sha1.           
```

#### Opcodes

```
  0: 0x00A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
00C0: 73 69 72 30 00                                    sir0.           
```

#### Opcodes

```
  0: 0x00B5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir0" with entities [EventEntity, EventEntity], work=29*
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                53 F8 FF  FF 7F F8 FF FF 7F 73 69       S........si
00D0: 72 30 00                                          r0.             
```

#### Opcodes

```
  0: 0x00C5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sir0" with entities [EventEntity, EventEntity]
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 73 69     f..........si
00E0: 72 31 00                                          r1.             
```

#### Opcodes

```
  0: 0x00D3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir1" with entities [EventEntity, EventEntity], work=29*
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          53 F8 FF FF 7F  F8 FF FF 7F 73 69 72 31     S........sir1
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sir1" with entities [EventEntity, EventEntity]
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    37 01 80 02 80 03 80  04 80 22 00 00            7........"..   
```

#### Opcodes

```
  0: 0x00F1 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=22.766*, y=-1.500*, direction=259.4°*
  1: 0x00FA [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x00FC [0x00] END_REQSTACK()
```

### Event 10008

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FD   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         37 01 80               7..
0100: 02 80 03 80 04 80 22 00  00                       ......"..       
```

#### Opcodes

```
  0: 0x00FD [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=22.766*, y=-1.500*, direction=259.4°*
  1: 0x0106 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0108 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0109   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                             32 05 80 1F 00 01 80           2......
0110: 06 80 07 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0109 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x010C [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=35.288*, Y=-2.999*
  2: 0x0114 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0116 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0117   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      32  05 80 1F 00 01 80 08 80         2........
0120: 07 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0117 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x011A [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=31.002*, Y=-2.999*
  2: 0x0122 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0124 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0125   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                29 08 9A  30 0F 01 09 1D 09 80 23       )..0......#
0130: 29 08 9A 30 0F 01 0A 00                           )..0....        
```

#### Opcodes

```
  0: 0x0125 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Francmage (ID: 17772698/0x010F309A), tag_num=0x09)
  1: 0x012C [0x1D] PRINT_EVENT_MESSAGE(message_id=6818*)
    → "You called for me, Your Majesty?"
  2: 0x012F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0130 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Francmage (ID: 17772698/0x010F309A), tag_num=0x0A)
  4: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0138  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          1D 0A 80 23 00                   ...#.   
```

#### Opcodes

```
  0: 0x0138 [0x1D] PRINT_EVENT_MESSAGE(message_id=6822*)
    → "Oh, yes, that. Those Bastoker Humes are causing no end of trouble--saying they want to investigate here, there, and the other place..."
  1: 0x013B [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x013C [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013D  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         1D 0B 80               ...
0140: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x013D [0x1D] PRINT_EVENT_MESSAGE(message_id=6828*)
    → "As you command, my lord. I would give the very blood that runs in my veins if it were to further the cause of our kingdom. You can rely on me."
  1: 0x0140 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0141 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0142  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       1D 0C 80 23 00                                ...#.         
```

#### Opcodes

```
  0: 0x0142 [0x1D] PRINT_EVENT_MESSAGE(message_id=6832*)
    → "I understand, Your Grace."
  1: 0x0145 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0146 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0147   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                      29  08 9A 30 0F 01 0B 1D 0D         )..0.....
0150: 80 23 29 08 9A 30 0F 01  0C 00                    .#)..0....      
```

#### Opcodes

```
  0: 0x0147 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Francmage (ID: 17772698/0x010F309A), tag_num=0x0B)
  1: 0x014E [0x1D] PRINT_EVENT_MESSAGE(message_id=6834*)
    → "Yes, sire! My life for the Kingdom!"
  2: 0x0151 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0152 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Francmage (ID: 17772698/0x010F309A), tag_num=0x0C)
  4: 0x0159 [0x00] END_REQSTACK()
```
