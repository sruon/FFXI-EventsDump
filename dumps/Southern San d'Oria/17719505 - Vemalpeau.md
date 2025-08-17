# 17719505 - Vemalpeau

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 312 bytes                     |
| Total Events     | 10                            |
| References Count | 12                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     17 |              9 |
| [7](#event-7)            | 0x0012       |     17 |              9 |
| [5](#event-5)            | 0x0023       |     84 |             18 |
| [4](#event-4)            | 0x0077       |     13 |              7 |
| [3](#event-3)            | 0x0084       |     13 |              7 |
| [6](#event-6)            | 0x0091       |      1 |              1 |
| [2](#event-2)            | 0x0092       |     13 |              7 |
| [65535.1](#event-655351) | 0x009F       |     19 |              3 |
| [65535.2](#event-655352) | 0x00B2       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x23BC      |        9148 |
|       1 | 0x23BD      |        9149 |
|       2 | 0x23BE      |        9150 |
|       3 | 0x23BF      |        9151 |
|       4 | 0x0014      |          20 |
|       5 | 0x23C9      |        9161 |
|       6 | 0x23CA      |        9162 |
|       7 | 0x23CB      |        9163 |
|       8 | 0x23CC      |        9164 |
|       9 | 0x23CD      |        9165 |
|      10 | 0x23E6      |        9190 |
|      11 | 0x003C      |          60 |

## String References

- **9148**: What do you want? I'm waiting for someone. Each time the door opens, I turn to look! Begone!
- **9149**: This is no concern of yours. Leave at once!
- **9150**: What are you here for? You ask about my son? Please, just go!
- **9151**: I know all about the intrigue of the knights! I heard that something was amiss right when my son disappeared. I know they had something to do with it!
- **9161**: Why, you would offer this to me!? It's the paintbrush Chusarlaud always wanted. How did you know?
- **9162**: In youth he wanted to be a painter. But, when his mother fell ill we lost the means, and he decided to become a knight. All on his own...
- **9163**: I just couldn't ask him to quit, even though I wanted him to. He was our pride. How could such a thing happen to him?
- **9164**: He has gone missing for nearly a year, but there is still a chance he lives. We've kept his room upstairs the way it's always been. Go see for yourself if you want to.
- **9165**: Come to think of it, often he would read a letter from his commanding officer. Once I snatched it while he was away, but the paper was blank.
- **9190**: It broke my heart to learn about him, but now I know the truth. You'll always have my gratitude.

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

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 17 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 1D 01 80 23   .....op...#...#
0010: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=9148*)
    → "What do you want? I'm waiting for someone. Each time the door opens, I turn to look! Begone!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=9149*)
    → "This is no concern of yours. Leave at once!"
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x21] END_EVENT
  8: 0x0011 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 17 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       1E F0 FF FF 7F 6F  70 1D 02 80 23 1D 03 80    .....op...#...
0020: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0012 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0017 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0018 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=9150*)
    → "What are you here for? You ask about my son? Please, just go!"
  4: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=9151*)
    → "I know all about the intrigue of the knights! I heard that something was amiss right when my son disappeared. I know they had something to do with it!"
  6: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0021 [0x21] END_EVENT
  8: 0x0022 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 84 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          42 1E F0 FF FF  7F 6F 70 66 04 80 F8 FF     B.....opf....
0030: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 05 80 23 66 04  ......tlk0...#f.
0040: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 1D 06 80  .........thk1...
0050: 23 1D 07 80 23 66 04 80  F8 FF FF 7F F8 FF FF 7F  #...#f..........
0060: 74 68 6B 32 1D 08 80 23  53 F8 FF FF 7F F8 FF FF  thk2...#S.......
0070: 7F 74 68 6B 32 21 00                              .thk2!.         
```

#### Opcodes

```
  0: 0x0023 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0024 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0029 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x002A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x003A [0x1D] PRINT_EVENT_MESSAGE(message_id=9161*)
    → "Why, you would offer this to me!? It's the paintbrush Chusarlaud always wanted. How did you know?"
  6: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x003E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  8: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=9162*)
    → "In youth he wanted to be a painter. But, when his mother fell ill we lost the means, and he decided to become a knight. All on his own..."
  9: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=9163*)
    → "I just couldn't ask him to quit, even though I wanted him to. He was our pride. How could such a thing happen to him?"
 11: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0055 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
 13: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=9164*)
    → "He has gone missing for nearly a year, but there is still a chance he lives. We've kept his room upstairs the way it's always been. Go see for yourself if you want to."
 14: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0068 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 16: 0x0075 [0x21] END_EVENT
 17: 0x0076 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      1E  F0 FF FF 7F 6F 70 1D 08         .....op..
0080: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0077 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=9164*)
    → "He has gone missing for nearly a year, but there is still a chance he lives. We've kept his room upstairs the way it's always been. Go see for yourself if you want to."
  4: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0082 [0x21] END_EVENT
  6: 0x0083 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             1E F0 FF FF  7F 6F 70 1D 09 80 23 21      .....op...#!
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0084 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0089 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x008A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=9165*)
    → "Come to think of it, often he would read a letter from his commanding officer. Once I snatched it while he was away, but the paper was blank."
  4: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x008F [0x21] END_EVENT
  6: 0x0090 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0091  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    00                                              .              
```

#### Opcodes

```
  0: 0x0091 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       1E F0 FF FF 7F 6F  70 1D 0A 80 23 21 00       .....op...#!. 
```

#### Opcodes

```
  0: 0x0092 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0097 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0098 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0099 [0x1D] PRINT_EVENT_MESSAGE(message_id=9190*)
    → "It broke my heart to learn about him, but now I know the truth. You'll always have my gratitude."
  4: 0x009C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x009D [0x21] END_EVENT
  6: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               66                 f
00A0: 04 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 1C 0B  ..........thk1..
00B0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x009F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x00AE [0x1C] WAIT(60* ticks)
  2: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       66 04 80 F8 FF FF  7F F8 FF FF 7F 74 68 6B    f..........thk
00C0: 32 53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     2S........thk2. 
```

#### Opcodes

```
  0: 0x00B2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  1: 0x00C1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x00CE [0x00] END_REQSTACK()
```
