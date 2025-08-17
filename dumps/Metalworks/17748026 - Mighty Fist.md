# 17748026 - Mighty Fist

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 424 bytes            |
| Total Events     | 7                    |
| References Count | 24                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [560](#event-560)     | 0x0001       |     30 |              8 |
| [561](#event-561)     | 0x001F       |     43 |             13 |
| [565](#event-565)     | 0x004A       |     44 |             12 |
| [566](#event-566)     | 0x0076       |     59 |             10 |
| [752](#event-752)     | 0x00B1       |     91 |             23 |
| [754](#event-754)     | 0x010C       |     16 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1EDA      |        7898 |
|       1 | 0x0037      |          55 |
|       2 | 0x1EDB      |        7899 |
|       3 | 0x1EDC      |        7900 |
|       4 | 0x1EDD      |        7901 |
|       5 | 0x1EDE      |        7902 |
|       6 | 0x1EDF      |        7903 |
|       7 | 0x008A      |         138 |
|       8 | 0x0285      |         645 |
|       9 | 0x1F51      |        8017 |
|      10 | 0x1F52      |        8018 |
|      11 | 0x1F53      |        8019 |
|      12 | 0x1F54      |        8020 |
|      13 | 0x00C9      |         201 |
|      14 | 0x0000      |           0 |
|      15 | 0x00EB      |         235 |
|      16 | 0x2175      |        8565 |
|      17 | 0x2176      |        8566 |
|      18 | 0x2177      |        8567 |
|      19 | 0x2178      |        8568 |
|      20 | 0x2179      |        8569 |
|      21 | 0x217A      |        8570 |
|      22 | 0x217B      |        8571 |
|      23 | 0x217C      |        8572 |

## String References

- **7898**: To be honest, it's not always easy working with Humes, but you get used to it. You have to.
- **7899**: You've got to be flexible, you know? You gotta keep up with the times. Otherwise you'll end up in the mines with the rest of the old, hard-headed Galka.
- **7900**: This is the Darksteel Forge. You must've heard of darksteel before.
- **7901**: Darksteel is an alloy harder yet more flexible than regular steel. What's more, it neither stains nor rusts. The only drawback is that it's a little heavy.
- **7902**: Its formula was a Galkan secret for a long time, but lately we've decided to teach Humes how to make it, too.
- **7903**: Knowing Humes, though, they would've figured it out eventually, and come up with something better.
- **8017**: You've become quite an experienced adventurer, I hear. I feel I can trust you.
- **8018**: I need you to go on an errand for me. Our supply of $6 is running low. Bring us two of them.
- **8019**: The Zeruhn Mines haven't been yielding much of it lately. You may have better luck in the Gusgen Mines.
- **8020**: Thank you. Here is your payment. If you find any more, bring them here.
- **8565**: What? You say Raibaht is searching for the book $3?
- **8566**: I see he's finally come to his senses. I've been trying to get him to ask Chief Cid to pour more money into the darksteel program.
- **8567**: Well, knowing Raibaht, he probably had to think and re-think it, but he still hasn't made up his mind. Hopefully, seeing $3 will help to push him in the right direction.
- **8568**: The problem is, $3 was donated to a library somewhere before I was appointed to this position.
- **8569**: And on top of that, there's no record of the donation anywhere. I guess I can't complain. That was back in the day when mythril was the material of choice, cermet was getting all the funding, and darksteel...well, darksteel was about as popular as rusty buckets...
- **8570**: ...and worth about the same, too.
- **8571**: I will write a letter to the library holding the document. You will need to take this letter and show it to the proprietor of the library.
- **8572**: Excellent! You've retrieved our copy of $3! Quickly, take it to Raibaht.

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

### Event 560

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 5B 01 80 F8 FF FF   ........#[.....
0010: 7F F8 FF FF 7F 74 6C 6B  30 1D 02 80 23 21 00     .....tlk0...#!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7898*)
    → "To be honest, it's not always easy working with Humes, but you get used to it. You have to."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=55*
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=7899*)
    → "You've got to be flexible, you know? You gotta keep up with the times. Otherwise you'll end up in the mines with the rest of the old, hard-headed Galka."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```

### Event 561

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 43 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1E                 .
0020: F0 FF FF 7F 1D 03 80 23  5B 01 80 F8 FF FF 7F F8  .......#[.......
0030: FF FF 7F 74 6C 6B 30 1D  04 80 23 1D 05 80 23 5E  ...tlk0...#...#^
0040: 69 64 6C 30 1D 06 80 23  21 00                    idl0...#!.      
```

#### Opcodes

```
  0: 0x001F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7900*)
    → "This is the Darksteel Forge. You must've heard of darksteel before."
  2: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0028 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=55*
  4: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=7901*)
    → "Darksteel is an alloy harder yet more flexible than regular steel. What's more, it neither stains nor rusts. The only drawback is that it's a little heavy."
  5: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=7902*)
    → "Its formula was a Galkan secret for a long time, but lately we've decided to teach Humes how to make it, too."
  7: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x003F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=7903*)
    → "Knowing Humes, though, they would've figured it out eventually, and come up with something better."
 10: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0048 [0x21] END_EVENT
 12: 0x0049 [0x00] END_REQSTACK()
```

### Event 565

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 44 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                03 09 10 07 80 03            ......
0050: 08 10 08 80 1E F0 FF FF  7F 1D 09 80 23 5B 01 80  ............#[..
0060: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 0A 80 23  ........tlk0...#
0070: 1D 0B 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x004A [0x03] Work_Zone[9] = 138*
  1: 0x004F [0x03] Work_Zone[8] = 645*
  2: 0x0054 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=8017*)
    → "You've become quite an experienced adventurer, I hear. I feel I can trust you."
  4: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x005D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=55*
  6: 0x006C [0x1D] PRINT_EVENT_MESSAGE(message_id=8018*)
    → "I need you to go on an errand for me. Our supply of $6 is running low. Bring us two of them."
  7: 0x006F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=8019*)
    → "The Zeruhn Mines haven't been yielding much of it lately. You may have better luck in the Gusgen Mines."
  9: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0074 [0x21] END_EVENT
 11: 0x0075 [0x00] END_REQSTACK()
```

### Event 566

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 59 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   20 01  42 1E F0 FF FF 7F 5B 01         .B.....[.
0080: 80 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 1D 0C 80  .........pas0...
0090: 23 53 F8 FF FF 7F F8 FF  FF 7F 70 61 73 30 45 0D  #S........pas0E.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 71 73 74 63 0E 80 21  .........qstc..!
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x0076 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0078 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0079 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x007E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=55*
  4: 0x008D [0x1D] PRINT_EVENT_MESSAGE(message_id=8020*)
    → "Thank you. Here is your payment. If you find any more, bring them here."
  5: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0091 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  7: 0x009E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
  8: 0x00AF [0x21] END_EVENT
  9: 0x00B0 [0x00] END_REQSTACK()
```

### Event 752

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 91 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    42 03 09 10 0F 80 1E  F0 FF FF 7F 1D 10 80 23   B.............#
00C0: 5B 01 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  [..........tlk0.
00D0: 11 80 23 1D 12 80 23 5E  69 64 6C 30 1D 13 80 23  ..#...#^idl0...#
00E0: 5B 01 80 F8 FF FF 7F F8  FF FF 7F 74 68 61 31 1D  [..........tha1.
00F0: 14 80 23 1D 15 80 23 5B  01 80 F8 FF FF 7F F8 FF  ..#...#[........
0100: FF 7F 74 68 61 32 1D 16  80 23 21 00              ..tha2...#!.    
```

#### Opcodes

```
  0: 0x00B1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00B2 [0x03] Work_Zone[9] = 235*
  2: 0x00B7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00BC [0x1D] PRINT_EVENT_MESSAGE(message_id=8565*)
    → "What? You say Raibaht is searching for the book $3?"
  4: 0x00BF [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00C0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=55*
  6: 0x00CF [0x1D] PRINT_EVENT_MESSAGE(message_id=8566*)
    → "I see he's finally come to his senses. I've been trying to get him to ask Chief Cid to pour more money into the darksteel program."
  7: 0x00D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8567*)
    → "Well, knowing Raibaht, he probably had to think and re-think it, but he still hasn't made up his mind. Hopefully, seeing $3 will help to push him in the right direction."
  9: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00D7 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 11: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=8568*)
    → "The problem is, $3 was donated to a library somewhere before I was appointed to this position."
 12: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00E0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tha1" with entities [EventEntity, EventEntity], work=55*
 14: 0x00EF [0x1D] PRINT_EVENT_MESSAGE(message_id=8569*)
    → "And on top of that, there's no record of the donation anywhere. I guess I can't complain. That was back in the day when mythril was the material of choice, cermet was getting all the funding, and darksteel...well, darksteel was about as popular as rusty buckets..."
 15: 0x00F2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x00F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8570*)
    → "...and worth about the same, too."
 17: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x00F7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tha2" with entities [EventEntity, EventEntity], work=55*
 19: 0x0106 [0x1D] PRINT_EVENT_MESSAGE(message_id=8571*)
    → "I will write a letter to the library holding the document. You will need to take this letter and show it to the proprietor of the library."
 20: 0x0109 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x010A [0x21] END_EVENT
 22: 0x010B [0x00] END_REQSTACK()
```

### Event 754

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010C   |
| Data Size    | 16 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      03 09 10 0F              ....
0110: 80 1E F0 FF FF 7F 1D 17  80 23 21 00              .........#!.    
```

#### Opcodes

```
  0: 0x010C [0x03] Work_Zone[9] = 235*
  1: 0x0111 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0116 [0x1D] PRINT_EVENT_MESSAGE(message_id=8572*)
    → "Excellent! You've retrieved our copy of $3! Quickly, take it to Raibaht."
  3: 0x0119 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x011A [0x21] END_EVENT
  5: 0x011B [0x00] END_REQSTACK()
```
