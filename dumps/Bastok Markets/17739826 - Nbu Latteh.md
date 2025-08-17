# 17739826 - Nbu Latteh

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Bastok Markets (ID: 235) |
| Block Size       | 480 bytes                |
| Total Events     | 10                       |
| References Count | 23                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [127](#event-127)     | 0x0001       |     30 |              8 |
| [230](#event-230)     | 0x001F       |     88 |             20 |
| [231](#event-231)     | 0x0077       |     21 |              5 |
| [233](#event-233)     | 0x008C       |     61 |             11 |
| [234](#event-234)     | 0x00C9       |     60 |             10 |
| [235](#event-235)     | 0x0105       |     47 |             15 |
| [675](#event-675)     | 0x0134       |      7 |              2 |
| [676](#event-676)     | 0x013B       |      7 |              2 |
| [678](#event-678)     | 0x0142       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D7C      |        7548 |
|       1 | 0x0032      |          50 |
|       2 | 0x1D7D      |        7549 |
|       3 | 0x1000      |        4096 |
|       4 | 0x348E      |       13454 |
|       5 | 0x1DAB      |        7595 |
|       6 | 0x1DAC      |        7596 |
|       7 | 0x1DAD      |        7597 |
|       8 | 0x000A      |          10 |
|       9 | 0x1DAE      |        7598 |
|      10 | 0x1DAF      |        7599 |
|      11 | 0x0034      |          52 |
|      12 | 0x1DB0      |        7600 |
|      13 | 0x1DB2      |        7602 |
|      14 | 0x1DB3      |        7603 |
|      15 | 0x00C9      |         201 |
|      16 | 0x0000      |           0 |
|      17 | 0x1DB4      |        7604 |
|      18 | 0x1DB5      |        7605 |
|      19 | 0x1DB6      |        7606 |
|      20 | 0x1DB7      |        7607 |
|      21 | 0x1DB8      |        7608 |
|      22 | 0x1DB9      |        7609 |

## String References

- **7548**: It's either poorly-guarded poor houses, or well-guarded well-to-do houses... How am I supposed to work under these conditions?
- **7549**: What kind of work do I do? I could tell you, but then I'd have to kill you! Hah hah hah. Just kidding.
- **7595**: Ah! An adventurrrer! Good, good! I need your help!
- **7596**: I want to give $6 to my daughter as a present, but I could only get my paws on $7.
- **7597**: Could you make it into $6 and give it to my daughter? Of course, I'm not asking you to do it for nothing. I have enough to pay you.
- **7598**: I'd do it myself, if it weren't for that guard over there. I think she's got me marrrked. Anyway, here's the $7.
- **7599**: Why is the guard watching me? Oh, it's nothing for you to worry about. By the way, my place is in the Mines District, in the lower level housing area. There aren't that many Mithra around, so it shouldn't be too harrrd to find.
- **7600**: Damned guard! I've got to make a living, too! Come on, look the other way!
- **7602**: So, did you do it? What's that? A letter from my daughter? Oh, how sweet!
- **7603**: Be patient, my little kitten--Mom's gonna work hard for you! Oh, wait...I should give you this first. Thanks again!
- **7604**: Wait... You've read this, haven't you? That's not very commendable, you know? Still, I should pay you for your work.
- **7605**: Oh, hi! I've been looking for you! I need you to do something for me again. You're a good person and I trust you, so I'm going to tell you this...
- **7606**: I recently got some information about a treasure! It's supposed to be buried under one of the signposts on the Konschtat Highlands.
- **7607**: I'd go myself, but I got this other thing I have to take care of first...
- **7608**: But I wouldn't want anyone else to take it before I do, so I thought of asking you, my trusty sidekick! If whatever's buried there is worth anything, I'll be happy to buy it off you.
- **7609**: So, could you go get it and bring it to my house? Have a chat with my daughter and wait if I'm not there. I'll try to shake that guard off my tail before then.

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

### Event 127

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 66 01 80 F8 FF FF   ........#f.....
0010: 7F F8 FF FF 7F 74 6C 6B  30 1D 02 80 23 21 00     .....tlk0...#!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7548*)
    → "It's either poorly-guarded poor houses, or well-guarded well-to-do houses... How am I supposed to work under these conditions?"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=7549*)
    → "What kind of work do I do? I could tell you, but then I'd have to kill you! Hah hah hah. Just kidding."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```

### Event 230

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 88 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               03                 .
0020: 09 10 03 80 03 08 10 04  80 1E F0 FF FF 7F 1D 05  ................
0030: 80 23 66 01 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#f..........tlk
0040: 30 1D 06 80 23 1D 07 80  23 5E 69 64 6C 30 1C 08  0...#...#^idl0..
0050: 80 66 01 80 F8 FF FF 7F  F8 FF FF 7F 70 61 73 30  .f..........pas0
0060: 1D 09 80 23 1D 0A 80 23  53 F8 FF FF 7F F8 FF FF  ...#...#S.......
0070: 7F 70 61 73 30 21 00                              .pas0!.         
```

#### Opcodes

```
  0: 0x001F [0x03] Work_Zone[9] = 4096*
  1: 0x0024 [0x03] Work_Zone[8] = 13454*
  2: 0x0029 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7595*)
    → "Ah! An adventurrrer! Good, good! I need your help!"
  4: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0032 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  6: 0x0041 [0x1D] PRINT_EVENT_MESSAGE(message_id=7596*)
    → "I want to give $6 to my daughter as a present, but I could only get my paws on $7."
  7: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=7597*)
    → "Could you make it into $6 and give it to my daughter? Of course, I'm not asking you to do it for nothing. I have enough to pay you."
  9: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0049 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 11: 0x004E [0x1C] WAIT(10* ticks)
 12: 0x0051 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=50*
 13: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=7598*)
    → "I'd do it myself, if it weren't for that guard over there. I think she's got me marrrked. Anyway, here's the $7."
 14: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=7599*)
    → "Why is the guard watching me? Oh, it's nothing for you to worry about. By the way, my place is in the Mines District, in the lower level housing area. There aren't that many Mithra around, so it shouldn't be too harrrd to find."
 16: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0068 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 18: 0x0075 [0x21] END_EVENT
 19: 0x0076 [0x00] END_REQSTACK()
```

### Event 231

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      66  0B 80 F8 FF FF 7F F8 FF         f........
0080: FF 7F 64 69 73 30 1D 0C  80 23 21 00              ..dis0...#!.    
```

#### Opcodes

```
  0: 0x0077 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=52*
  1: 0x0086 [0x1D] PRINT_EVENT_MESSAGE(message_id=7600*)
    → "Damned guard! I've got to make a living, too! Come on, look the other way!"
  2: 0x0089 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x008A [0x21] END_EVENT
  4: 0x008B [0x00] END_REQSTACK()
```

### Event 233

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 61 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      42 1E F0 FF              B...
0090: FF 7F 1D 0D 80 23 66 01  80 F8 FF FF 7F F8 FF FF  .....#f.........
00A0: 7F 70 61 73 30 1D 0E 80  23 53 F8 FF FF 7F F8 FF  .pas0...#S......
00B0: FF 7F 70 61 73 30 45 0F  80 F0 FF FF 7F F0 FF FF  ..pas0E.........
00C0: 7F 71 73 74 63 10 80 21  00                       .qstc..!.       
```

#### Opcodes

```
  0: 0x008C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x008D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=7602*)
    → "So, did you do it? What's that? A letter from my daughter? Oh, how sweet!"
  3: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0096 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=50*
  5: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7603*)
    → "Be patient, my little kitten--Mom's gonna work hard for you! Oh, wait...I should give you this first. Thanks again!"
  6: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00A9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  8: 0x00B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  9: 0x00C7 [0x21] END_EVENT
 10: 0x00C8 [0x00] END_REQSTACK()
```

### Event 234

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 60 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1E F0 FF FF 7F 1D 0D           .......
00D0: 80 23 66 01 80 F8 FF FF  7F F8 FF FF 7F 70 61 73  .#f..........pas
00E0: 30 1D 11 80 23 53 F8 FF  FF 7F F8 FF FF 7F 70 61  0...#S........pa
00F0: 73 30 45 0F 80 F0 FF FF  7F F0 FF FF 7F 71 73 74  s0E..........qst
0100: 63 10 80 21 00                                    c..!.           
```

#### Opcodes

```
  0: 0x00C9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CE [0x1D] PRINT_EVENT_MESSAGE(message_id=7602*)
    → "So, did you do it? What's that? A letter from my daughter? Oh, how sweet!"
  2: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00D2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=50*
  4: 0x00E1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7604*)
    → "Wait... You've read this, haven't you? That's not very commendable, you know? Still, I should pay you for your work."
  5: 0x00E4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00E5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  7: 0x00F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x0103 [0x21] END_EVENT
  9: 0x0104 [0x00] END_REQSTACK()
```

### Event 235

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0105   |
| Data Size    | 47 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                1E F0 FF  FF 7F 1D 12 80 23 66 01       ........#f.
0110: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 13 80  .........tlk0...
0120: 23 1D 14 80 23 1D 15 80  23 5E 69 64 6C 30 1D 16  #...#...#^idl0..
0130: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0105 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x010A [0x1D] PRINT_EVENT_MESSAGE(message_id=7605*)
    → "Oh, hi! I've been looking for you! I need you to do something for me again. You're a good person and I trust you, so I'm going to tell you this..."
  2: 0x010D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x010E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x011D [0x1D] PRINT_EVENT_MESSAGE(message_id=7606*)
    → "I recently got some information about a treasure! It's supposed to be buried under one of the signposts on the Konschtat Highlands."
  5: 0x0120 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0121 [0x1D] PRINT_EVENT_MESSAGE(message_id=7607*)
    → "I'd go myself, but I got this other thing I have to take care of first..."
  7: 0x0124 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0125 [0x1D] PRINT_EVENT_MESSAGE(message_id=7608*)
    → "But I wouldn't want anyone else to take it before I do, so I thought of asking you, my trusty sidekick! If whatever's buried there is worth anything, I'll be happy to buy it off you."
  9: 0x0128 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0129 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 11: 0x012E [0x1D] PRINT_EVENT_MESSAGE(message_id=7609*)
    → "So, could you go get it and bring it to my house? Have a chat with my daughter and wait if I'm not there. I'll try to shake that guard off my tail before then."
 12: 0x0131 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0132 [0x21] END_EVENT
 14: 0x0133 [0x00] END_REQSTACK()
```

### Event 675

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0134  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0134 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x013A [0x00] END_REQSTACK()
```

### Event 676

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   92 01 F8 FF FF             .....
0140: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x013B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0141 [0x00] END_REQSTACK()
```

### Event 678

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0142  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0142 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0148 [0x00] END_REQSTACK()
```
