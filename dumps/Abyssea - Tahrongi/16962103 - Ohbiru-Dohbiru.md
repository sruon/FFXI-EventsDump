# 16962103 - Ohbiru-Dohbiru

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 524 bytes                   |
| Total Events     | 7                           |
| References Count | 23                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [344](#event-344)     | 0x0001       |     17 |              9 |
| [345](#event-345)     | 0x0012       |    158 |             34 |
| [346](#event-346)     | 0x00B0       |     13 |              7 |
| [347](#event-347)     | 0x00BD       |     72 |             18 |
| [348](#event-348)     | 0x0105       |     64 |             14 |
| [349](#event-349)     | 0x0145       |     60 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F11      |        7953 |
|       1 | 0x1F12      |        7954 |
|       2 | 0x1F13      |        7955 |
|       3 | 0x1F14      |        7956 |
|       4 | 0x0000      |           0 |
|       5 | 0x0150      |         336 |
|       6 | 0x1F15      |        7957 |
|       7 | 0x001E      |          30 |
|       8 | 0x0001      |           1 |
|       9 | 0x0024      |          36 |
|      10 | 0x1F16      |        7958 |
|      11 | 0x005A      |          90 |
|      12 | 0x1F17      |        7959 |
|      13 | 0x0028      |          40 |
|      14 | 0x1F18      |        7960 |
|      15 | 0x1F1A      |        7962 |
|      16 | 0x1F24      |        7972 |
|      17 | 0x1F25      |        7973 |
|      18 | 0x1F26      |        7974 |
|      19 | 0x1F27      |        7975 |
|      20 | 0x1F28      |        7976 |
|      21 | 0x1F2A      |        7978 |
|      22 | 0x1F2B      |        7979 |

## String References

- **7953**: Minister Rukususu, Leepe-Hoppe, Doctor Yoran-Oran... I do hope they're all right...
- **7954**: Kerutoto? She's sleeping blissfully as always, no doubt.
- **7955**: Hail there! Have you perchance caught sight of a garishly pink-colored fiend in these parts?
- **7956**: Seen a pink fiend? [I have not./I have!]
- **7957**: Well, drat! Wherever did it scamper off to? At this rate, I'll never finish my research!
- **7958**: You have? What luck! This could just be the breakthrough in my research I've been waiting for!
- **7959**: What research, you say? Why, my study of the Abyssean ecosystem, of course! It started out as a hobby, but recently I'm convinced that it just might be the key to our survival.
- **7960**: Perhaps you've noticed that there are all sorts of curious new creatures sprouting out of the ground these days. One in particular has caught my fancy--a pinkish thing that bears a striking resemblance to the mandragora we know so well.
- **7962**: If you'd be willing to help me procure one, speak to Kenapa-Keppa outside. Nothing would thrill him more than to be able to fill you in on the details!
- **7972**: Splendid, splendid work! I truly can't thank you enough. Could I ask you to round me up a sandworm or two while you're at it? But I jest!
- **7973**: But of course! Since you've been such a dutiful assistant, why don't I enlighten you as to my latest findings?
- **7974**: My experiments have shown that when battling the beasts that roam the canyon here, it'd behoove you to formulate a proper plan of attack!
- **7975**: They each have their weaknesses, you see. Send a particularly unpleasant attack or spell their way, and you just might stop them in their tracks, or scare them into forgetting some of their most potent abilities.
- **7976**: You might also want to experiment with killing them in all many of creative ways. Me? A sadist? Of course not! I'm just saying, my research suggests that doing so might prove fruitful!
- **7978**: I don't know quite how to say this my friend, but you know that splendid specimen you caught for us? Well, while I was writing up my latest lab report, it seems to have--er, how shall I say this?--ah, escaped.
- **7979**: You wouldn't possibly be in the mood for tracking another one down for me, would you? Just think, it's not for me...it's for science!

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

### Event 344

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
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7953*)
    → "Minister Rukususu, Leepe-Hoppe, Doctor Yoran-Oran... I do hope they're all right..."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=7954*)
    → "Kerutoto? She's sleeping blissfully as always, no doubt."
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x21] END_EVENT
  8: 0x0011 [0x00] END_REQSTACK()
```

### Event 345

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0012    |
| Data Size    | 158 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       42 1E F0 FF FF 7F  6F 70 1D 02 80 23 24 03    B.....op...#$.
0020: 80 04 80 04 80 25 02 00  10 04 80 00 59 00 5B 05  .....%......Y.[.
0030: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 1D 06 80  .........thk1...
0040: 23 53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 5E 69  #S........thk1^i
0050: 64 6C 30 1C 07 80 01 77  00 02 00 10 08 80 00 77  dl0....w.......w
0060: 00 6E F8 FF FF 7F 09 80  99 F8 FF FF 7F 1D 0A 80  .n..............
0070: 23 1C 0B 80 01 77 00 1D  0C 80 23 66 0D 80 F8 FF  #....w....#f....
0080: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 0E 80 23 1D 0F  ......tlk0...#..
0090: 80 23 66 0D 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#f..........tlk
00A0: 31 53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 21 00  1S........tlk1!.
```

#### Opcodes

```
  0: 0x0012 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0013 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0019 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=7955*)
    → "Hail there! Have you perchance caught sight of a garishly pink-colored fiend in these parts?"
  5: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001E [0x24] CREATE_DIALOG(message_id=7956*, default_option=0*, option_flags=0*)
    → "Seen a pink fiend? [I have not./I have!]"
  7: 0x0025 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0026 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0059
  9: 0x002E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=336*
 10: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=7957*)
    → "Well, drat! Wherever did it scamper off to? At this rate, I'll never finish my research!"
 11: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0041 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
 13: 0x004E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 14: 0x0053 [0x1C] WAIT(30* ticks)
 15: 0x0056 [0x01] GOTO 0x0077
 16: 0x0059 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0077
 17: 0x0061 [0x6E] EventEntity uses emote 36*
 18: 0x0068 [0x99] Wait for EventEntity animation to complete
 19: 0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=7958*)
    → "You have? What luck! This could just be the breakthrough in my research I've been waiting for!"
 20: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0071 [0x1C] WAIT(90* ticks)
 22: 0x0074 [0x01] GOTO 0x0077

SUBROUTINE_0077:
 23: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=7959*)
    → "What research, you say? Why, my study of the Abyssean ecosystem, of course! It started out as a hobby, but recently I'm convinced that it just might be the key to our survival."
 24: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x007B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 26: 0x008A [0x1D] PRINT_EVENT_MESSAGE(message_id=7960*)
    → "Perhaps you've noticed that there are all sorts of curious new creatures sprouting out of the ground these days. One in particular has caught my fancy--a pinkish thing that bears a striking resemblance to the mandragora we know so well."
 27: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x008E [0x1D] PRINT_EVENT_MESSAGE(message_id=7962*)
    → "If you'd be willing to help me procure one, speak to Kenapa-Keppa outside. Nothing would thrill him more than to be able to fill you in on the details!"
 29: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0092 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 31: 0x00A1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 32: 0x00AE [0x21] END_EVENT
 33: 0x00AF [0x00] END_REQSTACK()
```

### Event 346

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 1E F0 FF FF 7F 6F 70 1D  0F 80 23 21 00           .....op...#!.   
```

#### Opcodes

```
  0: 0x00B0 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B6 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7962*)
    → "If you'd be willing to help me procure one, speak to Kenapa-Keppa outside. Nothing would thrill him more than to be able to fill you in on the details!"
  4: 0x00BA [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00BB [0x21] END_EVENT
  6: 0x00BC [0x00] END_REQSTACK()
```

### Event 347

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BD   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                         1E F0 FF               ...
00C0: FF 7F 6F 70 1D 10 80 23  66 0D 80 F8 FF FF 7F F8  ..op...#f.......
00D0: FF FF 7F 74 6C 6B 30 1D  11 80 23 1D 12 80 23 1D  ...tlk0...#...#.
00E0: 13 80 23 1D 14 80 23 66  0D 80 F8 FF FF 7F F8 FF  ..#...#f........
00F0: FF 7F 74 6C 6B 31 53 F8  FF FF 7F F8 FF FF 7F 74  ..tlk1S........t
0100: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x00BD [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00C3 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00C4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7972*)
    → "Splendid, splendid work! I truly can't thank you enough. Could I ask you to round me up a sandworm or two while you're at it? But I jest!"
  4: 0x00C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00C8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  6: 0x00D7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7973*)
    → "But of course! Since you've been such a dutiful assistant, why don't I enlighten you as to my latest findings?"
  7: 0x00DA [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00DB [0x1D] PRINT_EVENT_MESSAGE(message_id=7974*)
    → "My experiments have shown that when battling the beasts that roam the canyon here, it'd behoove you to formulate a proper plan of attack!"
  9: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00DF [0x1D] PRINT_EVENT_MESSAGE(message_id=7975*)
    → "They each have their weaknesses, you see. Send a particularly unpleasant attack or spell their way, and you just might stop them in their tracks, or scare them into forgetting some of their most potent abilities."
 11: 0x00E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7976*)
    → "You might also want to experiment with killing them in all many of creative ways. Me? A sadist? Of course not! I'm just saying, my research suggests that doing so might prove fruitful!"
 13: 0x00E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00E7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 15: 0x00F6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 16: 0x0103 [0x21] END_EVENT
 17: 0x0104 [0x00] END_REQSTACK()
```

### Event 348

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0105   |
| Data Size    | 64 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                1E F0 FF  FF 7F 6F 70 66 0D 80 F8       .....opf...
0110: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 12 80 23 1D  .......tlk0...#.
0120: 13 80 23 1D 14 80 23 66  0D 80 F8 FF FF 7F F8 FF  ..#...#f........
0130: FF 7F 74 6C 6B 31 53 F8  FF FF 7F F8 FF FF 7F 74  ..tlk1S........t
0140: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x0105 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x010A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x010B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x010C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x011B [0x1D] PRINT_EVENT_MESSAGE(message_id=7974*)
    → "My experiments have shown that when battling the beasts that roam the canyon here, it'd behoove you to formulate a proper plan of attack!"
  5: 0x011E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x011F [0x1D] PRINT_EVENT_MESSAGE(message_id=7975*)
    → "They each have their weaknesses, you see. Send a particularly unpleasant attack or spell their way, and you just might stop them in their tracks, or scare them into forgetting some of their most potent abilities."
  7: 0x0122 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0123 [0x1D] PRINT_EVENT_MESSAGE(message_id=7976*)
    → "You might also want to experiment with killing them in all many of creative ways. Me? A sadist? Of course not! I'm just saying, my research suggests that doing so might prove fruitful!"
  9: 0x0126 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0127 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 11: 0x0136 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 12: 0x0143 [0x21] END_EVENT
 13: 0x0144 [0x00] END_REQSTACK()
```

### Event 349

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0145   |
| Data Size    | 60 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                1E F0 FF  FF 7F 6F 70 1D 15 80 23       .....op...#
0150: 66 0D 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0160: 16 80 23 66 0D 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0170: 6B 31 53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 21  k1S........tlk1!
0180: 00                                                .               
```

#### Opcodes

```
  0: 0x0145 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x014A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x014B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x014C [0x1D] PRINT_EVENT_MESSAGE(message_id=7978*)
    → "I don't know quite how to say this my friend, but you know that splendid specimen you caught for us? Well, while I was writing up my latest lab report, it seems to have--er, how shall I say this?--ah, escaped."
  4: 0x014F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0150 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  6: 0x015F [0x1D] PRINT_EVENT_MESSAGE(message_id=7979*)
    → "You wouldn't possibly be in the mood for tracking another one down for me, would you? Just think, it's not for me...it's for science!"
  7: 0x0162 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0163 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  9: 0x0172 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 10: 0x017F [0x21] END_EVENT
 11: 0x0180 [0x00] END_REQSTACK()
```
