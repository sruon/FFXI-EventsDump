# 17752262 - Gantineux

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 468 bytes                 |
| Total Events     | 7                         |
| References Count | 18                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10018](#event-10018) | 0x0001       |     11 |              5 |
| [10019](#event-10019) | 0x000C       |    173 |             31 |
| [10020](#event-10020) | 0x00B9       |     11 |              5 |
| [10021](#event-10021) | 0x00C4       |     82 |             18 |
| [10022](#event-10022) | 0x0116       |     43 |              9 |
| [10023](#event-10023) | 0x0141       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x240A      |        9226 |
|       1 | 0x00AF      |         175 |
|       2 | 0x0014      |          20 |
|       3 | 0x240B      |        9227 |
|       4 | 0x240C      |        9228 |
|       5 | 0x240D      |        9229 |
|       6 | 0x240E      |        9230 |
|       7 | 0x240F      |        9231 |
|       8 | 0x2410      |        9232 |
|       9 | 0x2411      |        9233 |
|      10 | 0x2412      |        9234 |
|      11 | 0x2413      |        9235 |
|      12 | 0x2414      |        9236 |
|      13 | 0x2415      |        9237 |
|      14 | 0x2416      |        9238 |
|      15 | 0x2417      |        9239 |
|      16 | 0x2418      |        9240 |
|      17 | 0x2419      |        9241 |

## String References

- **9226**: I am a friar of the San d'Oria Cathedral, come to Windurst as part of a pilgrimage.
- **9227**: Now that my devotions at the Crag of Mea in the Tahrongi Canyon are complete, I have orders from the cathedral to research the union between the magical arts of Windurst and miracles born of faith.
- **9228**: I debated on how to best proceed, but finally settled on the field of putting troubled spirits to rest.
- **9229**: After hours of painstaking research, I was able to create an item that could be said to stand at the pinnacle of white magic!
- **9230**: Behold my creation! Please take this $3 and journey to the Eldieme Necropolis, a veritable city of restless souls.
- **9231**: In the Necropolis, you will find a brazier with a flame that wavers from time to time. If you hold this $3 aloft in that place, it should bring the spirits into a state of tranquility. Please return and inform me of the outcome.
- **9232**: Why not go there myself, you ask? I am on a pilgrimage, and must not travel north of Jeuno.
- **9233**: Furthermore, I am but a simple scholar. It would be impossible for me to enter a place such as the Eldieme Necropolis.
- **9234**: Please give peace to the spirits of the Eldieme Necropolis.
- **9235**: Ah, you're back! And the result? Oh, I see...I was so sure it would work...
- **9236**: In any case, I must thank you for your assistance. I would like to reward you immediately, but I do not possess anything of value...
- **9237**: Please take this letter of introduction to Eperdur of the San d'Oria Cathedral.
- **9238**: May Paradise open its gates to you.
- **9239**: Please take this letter of introduction to Eperdur of the San d'Oria Cathedral.
- **9240**: A communication from the cathedral arrived to encourage me in my ongoing research.
- **9241**: The Gates of Paradise are yet distant, I fear.

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

### Event 10018

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=9226*)
    → "I am a friar of the San d'Oria Cathedral, come to Windurst as part of a pilgrimage."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 10019

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000C    |
| Data Size    | 173 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      03 09 10 01              ....
0010: 80 1E F0 FF FF 7F 1D 00  80 23 6F 70 5B 02 80 F8  .........#op[...
0020: FF FF 7F F8 FF FF 7F 74  68 6B 31 1D 03 80 23 1D  .......thk1...#.
0030: 04 80 23 53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31  ..#S........thk1
0040: 5B 02 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 32 1D  [..........thk2.
0050: 05 80 23 2C F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32  ..#,........thk2
0060: 5B 02 80 F8 FF FF 7F F8  FF FF 7F 70 61 73 30 1D  [..........pas0.
0070: 06 80 23 1D 07 80 23 53  F8 FF FF 7F F8 FF FF 7F  ..#...#S........
0080: 70 61 73 30 5B 02 80 F8  FF FF 7F F8 FF FF 7F 74  pas0[..........t
0090: 6C 6B 30 1D 08 80 23 53  F8 FF FF 7F F8 FF FF 7F  lk0...#S........
00A0: 74 6C 6B 30 5B 02 80 F8  FF FF 7F F8 FF FF 7F 74  tlk0[..........t
00B0: 6C 6B 31 1D 09 80 23 21  00                       lk1...#!.       
```

#### Opcodes

```
  0: 0x000C [0x03] Work_Zone[9] = 175*
  1: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=9226*)
    → "I am a friar of the San d'Oria Cathedral, come to Windurst as part of a pilgrimage."
  3: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x001B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x001C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  7: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=9227*)
    → "Now that my devotions at the Crag of Mea in the Tahrongi Canyon are complete, I have orders from the cathedral to research the union between the magical arts of Windurst and miracles born of faith."
  8: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=9228*)
    → "I debated on how to best proceed, but finally settled on the field of putting troubled spirits to rest."
 10: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0033 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
 12: 0x0040 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
 13: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=9229*)
    → "After hours of painstaking research, I was able to create an item that could be said to stand at the pinnacle of white magic!"
 14: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0053 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "thk2" with entities [EventEntity, EventEntity]
 16: 0x0060 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 17: 0x006F [0x1D] PRINT_EVENT_MESSAGE(message_id=9230*)
    → "Behold my creation! Please take this $3 and journey to the Eldieme Necropolis, a veritable city of restless souls."
 18: 0x0072 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=9231*)
    → "In the Necropolis, you will find a brazier with a flame that wavers from time to time. If you hold this $3 aloft in that place, it should bring the spirits into a state of tranquility. Please return and inform me of the outcome."
 20: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0077 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 22: 0x0084 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 23: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=9232*)
    → "Why not go there myself, you ask? I am on a pilgrimage, and must not travel north of Jeuno."
 24: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0097 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 26: 0x00A4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 27: 0x00B3 [0x1D] PRINT_EVENT_MESSAGE(message_id=9233*)
    → "Furthermore, I am but a simple scholar. It would be impossible for me to enter a place such as the Eldieme Necropolis."
 28: 0x00B6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x00B7 [0x21] END_EVENT
 30: 0x00B8 [0x00] END_REQSTACK()
```

### Event 10020

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             1E F0 FF FF 7F 1D 0A           .......
00C0: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x00B9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00BE [0x1D] PRINT_EVENT_MESSAGE(message_id=9234*)
    → "Please give peace to the spirits of the Eldieme Necropolis."
  2: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00C2 [0x21] END_EVENT
  4: 0x00C3 [0x00] END_REQSTACK()
```

### Event 10021

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C4   |
| Data Size    | 82 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:             42 1E F0 FF  FF 7F 1D 0B 80 23 6F 70      B........#op
00D0: 5B 02 80 F8 FF FF 7F F8  FF FF 7F 70 61 73 30 1D  [..........pas0.
00E0: 0C 80 23 1D 0D 80 23 53  F8 FF FF 7F F8 FF FF 7F  ..#...#S........
00F0: 70 61 73 30 5B 02 80 F8  FF FF 7F F8 FF FF 7F 69  pas0[..........i
0100: 6E 6F 30 1D 0E 80 23 53  F8 FF FF 7F F8 FF FF 7F  no0...#S........
0110: 69 6E 6F 30 21 00                                 ino0!.          
```

#### Opcodes

```
  0: 0x00C4 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00C5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00CA [0x1D] PRINT_EVENT_MESSAGE(message_id=9235*)
    → "Ah, you're back! And the result? Oh, I see...I was so sure it would work..."
  3: 0x00CD [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00CE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00CF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x00D0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
  7: 0x00DF [0x1D] PRINT_EVENT_MESSAGE(message_id=9236*)
    → "In any case, I must thank you for your assistance. I would like to reward you immediately, but I do not possess anything of value..."
  8: 0x00E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=9237*)
    → "Please take this letter of introduction to Eperdur of the San d'Oria Cathedral."
 10: 0x00E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00E7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 12: 0x00F4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
 13: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=9238*)
    → "May Paradise open its gates to you."
 14: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0107 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
 16: 0x0114 [0x21] END_EVENT
 17: 0x0115 [0x00] END_REQSTACK()
```

### Event 10022

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   1E F0  FF FF 7F 1D 0F 80 23 5B        ........#[
0120: 02 80 F8 FF FF 7F F8 FF  FF 7F 69 6E 6F 30 1D 0E  ..........ino0..
0130: 80 23 53 F8 FF FF 7F F8  FF FF 7F 69 6E 6F 30 21  .#S........ino0!
0140: 00                                                .               
```

#### Opcodes

```
  0: 0x0116 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x011B [0x1D] PRINT_EVENT_MESSAGE(message_id=9239*)
    → "Please take this letter of introduction to Eperdur of the San d'Oria Cathedral."
  2: 0x011E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x011F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
  4: 0x012E [0x1D] PRINT_EVENT_MESSAGE(message_id=9238*)
    → "May Paradise open its gates to you."
  5: 0x0131 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0132 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
  7: 0x013F [0x21] END_EVENT
  8: 0x0140 [0x00] END_REQSTACK()
```

### Event 10023

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0141   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:    1E F0 FF FF 7F 1D 10  80 23 5B 02 80 F8 FF FF   ........#[.....
0150: 7F F8 FF FF 7F 74 6C 6B  30 1D 11 80 23 21 00     .....tlk0...#!. 
```

#### Opcodes

```
  0: 0x0141 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0146 [0x1D] PRINT_EVENT_MESSAGE(message_id=9240*)
    → "A communication from the cathedral arrived to encourage me in my ongoing research."
  2: 0x0149 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x014A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0159 [0x1D] PRINT_EVENT_MESSAGE(message_id=9241*)
    → "The Gates of Paradise are yet distant, I fear."
  5: 0x015C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x015D [0x21] END_EVENT
  7: 0x015E [0x00] END_REQSTACK()
```
