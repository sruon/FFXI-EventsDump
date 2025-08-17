# 16962097 - Piketo-Puketo

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 492 bytes                   |
| Total Events     | 7                           |
| References Count | 22                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [322](#event-322)     | 0x0001       |     13 |              7 |
| [323](#event-323)     | 0x000E       |    129 |             31 |
| [324](#event-324)     | 0x008F       |     59 |             18 |
| [325](#event-325)     | 0x00CA       |    112 |             23 |
| [326](#event-326)     | 0x013A       |     28 |             11 |
| [327](#event-327)     | 0x0156       |     18 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1EDF      |        7903 |
|       1 | 0x1EE0      |        7904 |
|       2 | 0x0031      |          49 |
|       3 | 0x1EE1      |        7905 |
|       4 | 0x1EE2      |        7906 |
|       5 | 0x001E      |          30 |
|       6 | 0x0028      |          40 |
|       7 | 0x1EE3      |        7907 |
|       8 | 0x1EE4      |        7908 |
|       9 | 0x1EE5      |        7909 |
|      10 | 0x1EE6      |        7910 |
|      11 | 0x1EE7      |        7911 |
|      12 | 0x0000      |           0 |
|      13 | 0x1EF0      |        7920 |
|      14 | 0x0015      |          21 |
|      15 | 0x1EEC      |        7916 |
|      16 | 0x0078      |         120 |
|      17 | 0x1EED      |        7917 |
|      18 | 0x1EEE      |        7918 |
|      19 | 0x1EF1      |        7921 |
|      20 | 0x00C9      |         201 |
|      21 | 0x1EEF      |        7919 |

## String References

- **7903**: These gustatorily challenged boors will know my genius when I save them from famine! Bow down before my whisk and colander, fools! Ahahahahahahaaa!
- **7904**: You there! I command you to assist me!
- **7905**: Who are you to issue commands, you say? Why, only the ladle-bearing messiah whose soup of sustenance will save this miserable realm from starvation. Yes, that's right--in a land ruled by famine, the purveyor of provisions is king! A god, even!
- **7906**: Perhaps you have seen the scattered trees that speckle this otherwise barren, cactus-ridden wasteland. These trees once burgeoned with edible fruit, but no more!
- **7907**: And so who does it fall to, to take this lemon of a situation and make a scrumptious souffl<Player>i out of it? Why, none other than Piketo-Puketo, culinarian of culinarians, and his $3!
- **7908**: Those Rhinostery poseurs claim it to be their invention, but they're full of more hot air than an oven baking one of my famed rolanberry tarts. Ahem! In any event, one shot into its roots and any tree should readily return to full fruit-bearing glory.
- **7909**: You'll find a number of trees bearing their roots on the path leading to the Meriphataud Mountains. Take your pick of them! For it is not the ingredients that make the dish, but the skill of the chef who prepares them!
- **7910**: But not all will partake from Piketo-Puketo's table of plenty! Called my rolanberry tarts too tart, did you? My macarons too mushy? Oh yes, I remember you all! You will beg for forgiveness, or starve wishing the goddess had blessed you with a proper palate!
- **7911**: Now go forth and do my bidding, apprentice!
- **7916**: What's this? $6?
- **7917**: Bwahahaha! I knew I was a genius! Now, to fire up the oven and prepare the manna that will deliver our people from starvation...or at least those whose palate I deem worthy!
- **7918**: Don't ask me why, but my discerning nose tells me I'll be asking a similar favor of you in the none-too-distant future. If you've any semblance of good taste, you'll continue to serve me well.
- **7919**: My loyal minion returns, and not a moment too soon! It seems the world can't get enough of my gustatory delights. Here's your $3. You already know what to do with it, so chop chop!
- **7920**: What are you dawdling around here for? The world awaits victuals from my heavenly oven! To the trees lining the path to Meriphataud with you!
- **7921**: Such a dutiful [lad/lass] you are! Have no fear--I will see to it that you survive the great famine. Let it not be said that the mighty Piketo-Puketo does not smile upon the cultured and refined! Bwahahaha!

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

### Event 322

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7903*)
    → "These gustatorily challenged boors will know my genius when I save them from famine! Bow down before my whisk and colander, fools! Ahahahahahahaaa!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 323

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000E    |
| Data Size    | 129 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            42 1E                B.
0010: F0 FF FF 7F 6F 70 1D 01  80 23 66 02 80 F8 FF FF  ....op...#f.....
0020: 7F F8 FF FF 7F 74 6C 6B  30 1D 03 80 23 1D 04 80  .....tlk0...#...
0030: 23 53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69  #S........tlk0^i
0040: 64 6C 30 1C 05 80 66 06  80 F8 FF FF 7F F8 FF FF  dl0...f.........
0050: 7F 70 61 73 30 1D 07 80  23 53 F8 FF FF 7F F8 FF  .pas0...#S......
0060: FF 7F 70 61 73 30 66 02  80 F8 FF FF 7F F8 FF FF  ..pas0f.........
0070: 7F 74 6C 6B 30 1D 08 80  23 1D 09 80 23 5E 69 64  .tlk0...#...#^id
0080: 6C 30 1C 05 80 1D 0A 80  23 1D 0B 80 23 21 00     l0......#...#!. 
```

#### Opcodes

```
  0: 0x000E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0014 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0015 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=7904*)
    → "You there! I command you to assist me!"
  5: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  7: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7905*)
    → "Who are you to issue commands, you say? Why, only the ladle-bearing messiah whose soup of sustenance will save this miserable realm from starvation. Yes, that's right--in a land ruled by famine, the purveyor of provisions is king! A god, even!"
  8: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=7906*)
    → "Perhaps you have seen the scattered trees that speckle this otherwise barren, cactus-ridden wasteland. These trees once burgeoned with edible fruit, but no more!"
 10: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0031 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 12: 0x003E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 13: 0x0043 [0x1C] WAIT(30* ticks)
 14: 0x0046 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=40*
 15: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=7907*)
    → "And so who does it fall to, to take this lemon of a situation and make a scrumptious souffl<Player>i out of it? Why, none other than Piketo-Puketo, culinarian of culinarians, and his $3!"
 16: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0059 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 18: 0x0066 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
 19: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=7908*)
    → "Those Rhinostery poseurs claim it to be their invention, but they're full of more hot air than an oven baking one of my famed rolanberry tarts. Ahem! In any event, one shot into its roots and any tree should readily return to full fruit-bearing glory."
 20: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0079 [0x1D] PRINT_EVENT_MESSAGE(message_id=7909*)
    → "You'll find a number of trees bearing their roots on the path leading to the Meriphataud Mountains. Take your pick of them! For it is not the ingredients that make the dish, but the skill of the chef who prepares them!"
 22: 0x007C [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x007D [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 24: 0x0082 [0x1C] WAIT(30* ticks)
 25: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=7910*)
    → "But not all will partake from Piketo-Puketo's table of plenty! Called my rolanberry tarts too tart, did you? My macarons too mushy? Oh yes, I remember you all! You will beg for forgiveness, or starve wishing the goddess had blessed you with a proper palate!"
 26: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0089 [0x1D] PRINT_EVENT_MESSAGE(message_id=7911*)
    → "Now go forth and do my bidding, apprentice!"
 28: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x008D [0x21] END_EVENT
 30: 0x008E [0x00] END_REQSTACK()
```

### Event 324

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 59 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               1E                 .
0090: F0 FF FF 7F 6F 70 02 04  10 0C 80 00 C4 00 66 02  ....op........f.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 09 80  .........tlk0...
00B0: 23 5E 69 64 6C 30 1C 05  80 1D 0A 80 23 1D 0B 80  #^idl0......#...
00C0: 23 01 C8 00 1D 0D 80 23  21 00                    #......#!.      
```

#### Opcodes

```
  0: 0x008F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0094 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0095 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0096 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x00C4
  4: 0x009E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  5: 0x00AD [0x1D] PRINT_EVENT_MESSAGE(message_id=7909*)
    → "You'll find a number of trees bearing their roots on the path leading to the Meriphataud Mountains. Take your pick of them! For it is not the ingredients that make the dish, but the skill of the chef who prepares them!"
  6: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00B1 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  8: 0x00B6 [0x1C] WAIT(30* ticks)
  9: 0x00B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7910*)
    → "But not all will partake from Piketo-Puketo's table of plenty! Called my rolanberry tarts too tart, did you? My macarons too mushy? Oh yes, I remember you all! You will beg for forgiveness, or starve wishing the goddess had blessed you with a proper palate!"
 10: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=7911*)
    → "Now go forth and do my bidding, apprentice!"
 12: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00C1 [0x01] GOTO 0x00C8
 14: 0x00C4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7920*)
    → "What are you dawdling around here for? The world awaits victuals from my heavenly oven! To the trees lining the path to Meriphataud with you!"
 15: 0x00C7 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00C8:
 16: 0x00C8 [0x21] END_EVENT
 17: 0x00C9 [0x00] END_REQSTACK()
```

### Event 325

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00CA    |
| Data Size    | 112 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                42 1E F0 FF FF 7F            B.....
00D0: 6F 70 02 04 10 0C 80 00  23 01 6E F8 FF FF 7F 0E  op......#.n.....
00E0: 80 99 F8 FF FF 7F 1D 0F  80 23 1C 10 80 66 06 80  .........#...f..
00F0: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 1D 11 80 23  ........thk1...#
0100: 66 06 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 32 53  f..........thk2S
0110: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 1D 12 80 23  ........thk2...#
0120: 01 27 01 1D 13 80 23 45  14 80 F0 FF FF 7F F0 FF  .'....#E........
0130: FF 7F 71 73 74 63 0C 80  21 00                    ..qstc..!.      
```

#### Opcodes

```
  0: 0x00CA [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00CB [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00D0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00D1 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00D2 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0123
  5: 0x00DA [0x6E] EventEntity uses emote 21*
  6: 0x00E1 [0x99] Wait for EventEntity animation to complete
  7: 0x00E6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7916*)
    → "What's this? $6?"
  8: 0x00E9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00EA [0x1C] WAIT(120* ticks)
 10: 0x00ED [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
 11: 0x00FC [0x1D] PRINT_EVENT_MESSAGE(message_id=7917*)
    → "Bwahahaha! I knew I was a genius! Now, to fire up the oven and prepare the manna that will deliver our people from starvation...or at least those whose palate I deem worthy!"
 12: 0x00FF [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0100 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
 14: 0x010F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 15: 0x011C [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Don't ask me why, but my discerning nose tells me I'll be asking a similar favor of you in the none-too-distant future. If you've any semblance of good taste, you'll continue to serve me well."
 16: 0x011F [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0120 [0x01] GOTO 0x0127
 18: 0x0123 [0x1D] PRINT_EVENT_MESSAGE(message_id=7921*)
    → "Such a dutiful [lad/lass] you are! Have no fear--I will see to it that you survive the great famine. Let it not be said that the mighty Piketo-Puketo does not smile upon the cultured and refined! Bwahahaha!"
 19: 0x0126 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0127:
 20: 0x0127 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0138 [0x21] END_EVENT
 22: 0x0139 [0x00] END_REQSTACK()
```

### Event 326

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013A   |
| Data Size    | 28 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                1E F0 FF FF 7F 6F            .....o
0140: 70 02 04 10 0C 80 00 50  01 1D 12 80 23 01 54 01  p......P....#.T.
0150: 1D 13 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x013A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x013F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0140 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0141 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0150
  4: 0x0149 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Don't ask me why, but my discerning nose tells me I'll be asking a similar favor of you in the none-too-distant future. If you've any semblance of good taste, you'll continue to serve me well."
  5: 0x014C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x014D [0x01] GOTO 0x0154
  7: 0x0150 [0x1D] PRINT_EVENT_MESSAGE(message_id=7921*)
    → "Such a dutiful [lad/lass] you are! Have no fear--I will see to it that you survive the great famine. Let it not be said that the mighty Piketo-Puketo does not smile upon the cultured and refined! Bwahahaha!"
  8: 0x0153 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0154:
  9: 0x0154 [0x21] END_EVENT
 10: 0x0155 [0x00] END_REQSTACK()
```

### Event 327

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 18 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   42 1E  F0 FF FF 7F 6F 70 1D 15        B.....op..
0160: 80 23 1D 0D 80 23 21 00                           .#...#!.        
```

#### Opcodes

```
  0: 0x0156 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0157 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x015C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x015D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x015E [0x1D] PRINT_EVENT_MESSAGE(message_id=7919*)
    → "My loyal minion returns, and not a moment too soon! It seems the world can't get enough of my gustatory delights. Here's your $3. You already know what to do with it, so chop chop!"
  5: 0x0161 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0162 [0x1D] PRINT_EVENT_MESSAGE(message_id=7920*)
    → "What are you dawdling around here for? The world awaits victuals from my heavenly oven! To the trees lining the path to Meriphataud with you!"
  7: 0x0165 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0166 [0x21] END_EVENT
  9: 0x0167 [0x00] END_REQSTACK()
```
