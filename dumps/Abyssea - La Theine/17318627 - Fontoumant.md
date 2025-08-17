# 17318627 - Fontoumant

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Abyssea - La Theine (ID: 132) |
| Block Size       | 464 bytes                     |
| Total Events     | 6                             |
| References Count | 22                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [178](#event-178)     | 0x0001       |     28 |              8 |
| [179](#event-179)     | 0x001D       |     36 |             12 |
| [180](#event-180)     | 0x0041       |     51 |             12 |
| [181](#event-181)     | 0x0074       |    192 |             62 |
| [182](#event-182)     | 0x0134       |     28 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1F1A      |        7962 |
|       2 | 0x1F26      |        7974 |
|       3 | 0x1F23      |        7971 |
|       4 | 0x1F25      |        7973 |
|       5 | 0x1F27      |        7975 |
|       6 | 0x00F0      |         240 |
|       7 | 0x00C9      |         201 |
|       8 | 0x0000      |           0 |
|       9 | 0x1F1B      |        7963 |
|      10 | 0x1F1C      |        7964 |
|      11 | 0x1F1D      |        7965 |
|      12 | 0x1F1E      |        7966 |
|      13 | 0x1F1F      |        7967 |
|      14 | 0x1F20      |        7968 |
|      15 | 0x0001      |           1 |
|      16 | 0x1F22      |        7970 |
|      17 | 0x0A30      |        2608 |
|      18 | 0x1F24      |        7972 |
|      19 | 0x1F21      |        7969 |
|      20 | 0x1F29      |        7977 |
|      21 | 0x1F28      |        7976 |

## String References

- **7962**: Hm? An outsider, are we? I've no time to waste on one who's yet to earn my trust. Begone with you.
- **7963**: Ah, you must be the newcomer folk've been bending my ears about. I am Fontoumant. Before this evil engulfed us, I had a respected post overseeing the Consortium's warehouses.
- **7964**: But that and more were taken away from me, and I have those Abyssean fiends to thank for it.
- **7965**: My smoldering desire to exact revenge upon the vile creatures is all that drives me now. I spend my days devising ways to exterminate them, and painfully. Such is my joy.
- **7966**: I had a suspicion that the creatures' appearance was connected to the increase in seismic activity, and the research I subsequently conducted lent credence to this theory.
- **7967**: The fiends surge out from fissures--wounds on the earth's surface--that have opened up in ravines after tremors, I'm sure of it. I've a mind to delve deeper into this, but I require the assistance of one with a stout heart and a strong back.
- **7968**: Assist with the research? [I'm at your disposal!/I've prior, less dangerous engagements.]
- **7969**: Ach, just like the yearlings I get every day, you are. Away with you until you're willing to assist my research!
- **7970**: That's the spirit! There may be some hope for your generation yet. Now, let us dispense with the pleasantries as every moment spent in idleness could mean another score of demons being spawned into our midst.
- **7971**: I have created anti-Abyssean grenades, and I would have you test them out at three newly opened fissures. The first is a stone's throw away from this encampment, and the second and third are located in the ravine west of here.
- **7972**: In short, you are to take the grenades and cast one into each fissure. Remarkably straightforward, wouldn't you say so?
- **7973**: The findings will avail us only if the experiment is conducted periodically, however, so I would thank you for your continued assistance. Now, off you go then!
- **7974**: Hm? Forgotten the fissure locations, have you? The first is a stone's throw away from this encampment, and the second and third are located in the ravine west of here.
- **7975**: Ah, you're back. I trust the task posed no difficulties. Take this as recompense for your troubles, and seek me here whenever you wish to assist further in my research.
- **7976**: Ah, it's you again. Very kind of you to show, but I've yet to finish readying another set of grenades. Return here in a while, if you would.
- **7977**: Ah, it's you again. The research continues to yield useful data, in no small part thanks to you. I've just finished readying a new set of grenades. Might I prevail upon you to assist me again?

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

### Event 178

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  5B 00 80 F8 FF FF 7F F8   .....op[.......
0010: FF FF 7F 74 68 6B 30 1D  01 80 23 21 00           ...thk0...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7962*)
    → "Hm? An outsider, are we? I've no time to waste on one who's yet to earn my trust. Begone with you."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x21] END_EVENT
  7: 0x001C [0x00] END_REQSTACK()
```

### Event 179

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 36 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         1E F0 FF               ...
0020: FF 7F 6F 70 5B 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..op[..........t
0030: 6C 6B 30 1D 02 80 23 1D  03 80 23 1D 04 80 23 21  lk0...#...#...#!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x001D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0023 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0024 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=7974*)
    → "Hm? Forgotten the fissure locations, have you? The first is a stone's throw away from this encampment, and the second and third are located in the ravine west of here."
  5: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=7971*)
    → "I have created anti-Abyssean grenades, and I would have you test them out at three newly opened fissures. The first is a stone's throw away from this encampment, and the second and third are located in the ravine west of here."
  7: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=7973*)
    → "The findings will avail us only if the experiment is conducted periodically, however, so I would thank you for your continued assistance. Now, off you go then!"
  9: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x003F [0x21] END_EVENT
 11: 0x0040 [0x00] END_REQSTACK()
```

### Event 180

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 51 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    20 01 42 1E F0 FF FF  7F 6F 70 1D 05 80 23 5B    .B.....op...#[
0050: 00 80 F8 FF FF 7F F8 FF  FF 7F 70 61 73 30 1C 06  ..........pas0..
0060: 80 45 07 80 F0 FF FF 7F  F0 FF FF 7F 71 73 74 63  .E..........qstc
0070: 08 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0041 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0043 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=7975*)
    → "Ah, you're back. I trust the task posed no difficulties. Take this as recompense for your troubles, and seek me here whenever you wish to assist further in my research."
  6: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=30*
  8: 0x005E [0x1C] WAIT(240* ticks)
  9: 0x0061 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x0072 [0x21] END_EVENT
 11: 0x0073 [0x00] END_REQSTACK()
```

### Event 181

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0074    |
| Data Size    | 192 bytes |
| Instructions | 62        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             20 01 42 03  00 00 09 10 06 01 10 1E       .B.........
0080: F0 FF FF 7F 6F 70 5B 00  80 F8 FF FF 7F F8 FF FF  ....op[.........
0090: 7F 74 6C 6B 30 02 00 00  08 80 00 F1 00 1D 09 80  .tlk0...........
00A0: 23 1D 0A 80 23 1D 0B 80  23 1D 0C 80 23 1D 0D 80  #...#...#...#...
00B0: 23 24 0E 80 0F 80 08 80  25 02 00 10 08 80 00 DF  #$......%.......
00C0: 00 42 1D 10 80 23 03 02  10 11 80 1D 03 80 23 1D  .B...#........#.
00D0: 12 80 23 1D 04 80 23 03  01 10 0F 80 01 EE 00 02  ..#...#.........
00E0: 00 10 0F 80 00 EE 00 1D  13 80 23 01 EE 00 01 32  ..........#....2
00F0: 01 1D 14 80 23 24 0E 80  0F 80 08 80 25 02 00 10  ....#$......%...
0100: 08 80 00 23 01 42 1D 10  80 23 03 02 10 11 80 1D  ...#.B...#......
0110: 03 80 23 1D 12 80 23 1D  04 80 23 03 01 10 0F 80  ..#...#...#.....
0120: 01 32 01 02 00 10 0F 80  00 32 01 1D 13 80 23 01  .2.......2....#.
0130: 32 01 21 00                                       2.!.            
```

#### Opcodes

```
  0: 0x0074 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0076 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0077 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[9]
  3: 0x007C [0x06] Work_Zone[1] = 0
  4: 0x007F [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0084 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0085 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0086 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  8: 0x0095 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x00F1
  9: 0x009D [0x1D] PRINT_EVENT_MESSAGE(message_id=7963*)
    → "Ah, you must be the newcomer folk've been bending my ears about. I am Fontoumant. Before this evil engulfed us, I had a respected post overseeing the Consortium's warehouses."
 10: 0x00A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7964*)
    → "But that and more were taken away from me, and I have those Abyssean fiends to thank for it."
 12: 0x00A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7965*)
    → "My smoldering desire to exact revenge upon the vile creatures is all that drives me now. I spend my days devising ways to exterminate them, and painfully. Such is my joy."
 14: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00A9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7966*)
    → "I had a suspicion that the creatures' appearance was connected to the increase in seismic activity, and the research I subsequently conducted lent credence to this theory."
 16: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00AD [0x1D] PRINT_EVENT_MESSAGE(message_id=7967*)
    → "The fiends surge out from fissures--wounds on the earth's surface--that have opened up in ravines after tremors, I'm sure of it. I've a mind to delve deeper into this, but I require the assistance of one with a stout heart and a strong back."
 18: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00B1 [0x24] CREATE_DIALOG(message_id=7968*, default_option=1*, option_flags=0*)
    → "Assist with the research? [I'm at your disposal!/I've prior, less dangerous engagements.]"
 20: 0x00B8 [0x25] WAIT_DIALOG_SELECT()
 21: 0x00B9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00DF
 22: 0x00C1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 23: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7970*)
    → "That's the spirit! There may be some hope for your generation yet. Now, let us dispense with the pleasantries as every moment spent in idleness could mean another score of demons being spawned into our midst."
 24: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x00C6 [0x03] Work_Zone[2] = 2608*
 26: 0x00CB [0x1D] PRINT_EVENT_MESSAGE(message_id=7971*)
    → "I have created anti-Abyssean grenades, and I would have you test them out at three newly opened fissures. The first is a stone's throw away from this encampment, and the second and third are located in the ravine west of here."
 27: 0x00CE [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x00CF [0x1D] PRINT_EVENT_MESSAGE(message_id=7972*)
    → "In short, you are to take the grenades and cast one into each fissure. Remarkably straightforward, wouldn't you say so?"
 29: 0x00D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x00D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7973*)
    → "The findings will avail us only if the experiment is conducted periodically, however, so I would thank you for your continued assistance. Now, off you go then!"
 31: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x00D7 [0x03] Work_Zone[1] = 1*
 33: 0x00DC [0x01] GOTO 0x00EE
 34: 0x00DF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00EE
 35: 0x00E7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7969*)
    → "Ach, just like the yearlings I get every day, you are. Away with you until you're willing to assist my research!"
 36: 0x00EA [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x00EB [0x01] GOTO 0x00EE

SUBROUTINE_00EE:
 38: 0x00EE [0x01] GOTO 0x0132
 39: 0x00F1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7977*)
    → "Ah, it's you again. The research continues to yield useful data, in no small part thanks to you. I've just finished readying a new set of grenades. Might I prevail upon you to assist me again?"
 40: 0x00F4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x00F5 [0x24] CREATE_DIALOG(message_id=7968*, default_option=1*, option_flags=0*)
    → "Assist with the research? [I'm at your disposal!/I've prior, less dangerous engagements.]"
 42: 0x00FC [0x25] WAIT_DIALOG_SELECT()
 43: 0x00FD [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0123
 44: 0x0105 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 45: 0x0106 [0x1D] PRINT_EVENT_MESSAGE(message_id=7970*)
    → "That's the spirit! There may be some hope for your generation yet. Now, let us dispense with the pleasantries as every moment spent in idleness could mean another score of demons being spawned into our midst."
 46: 0x0109 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x010A [0x03] Work_Zone[2] = 2608*
 48: 0x010F [0x1D] PRINT_EVENT_MESSAGE(message_id=7971*)
    → "I have created anti-Abyssean grenades, and I would have you test them out at three newly opened fissures. The first is a stone's throw away from this encampment, and the second and third are located in the ravine west of here."
 49: 0x0112 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x0113 [0x1D] PRINT_EVENT_MESSAGE(message_id=7972*)
    → "In short, you are to take the grenades and cast one into each fissure. Remarkably straightforward, wouldn't you say so?"
 51: 0x0116 [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x0117 [0x1D] PRINT_EVENT_MESSAGE(message_id=7973*)
    → "The findings will avail us only if the experiment is conducted periodically, however, so I would thank you for your continued assistance. Now, off you go then!"
 53: 0x011A [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x011B [0x03] Work_Zone[1] = 1*
 55: 0x0120 [0x01] GOTO 0x0132
 56: 0x0123 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0132
 57: 0x012B [0x1D] PRINT_EVENT_MESSAGE(message_id=7969*)
    → "Ach, just like the yearlings I get every day, you are. Away with you until you're willing to assist my research!"
 58: 0x012E [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x012F [0x01] GOTO 0x0132

SUBROUTINE_0132:
 60: 0x0132 [0x21] END_EVENT
 61: 0x0133 [0x00] END_REQSTACK()
```

### Event 182

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0134   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:             1E F0 FF FF  7F 6F 70 5B 00 80 F8 FF      .....op[....
0140: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 15 80 23 21 00  ......tlk0...#!.
```

#### Opcodes

```
  0: 0x0134 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0139 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x013A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x013B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x014A [0x1D] PRINT_EVENT_MESSAGE(message_id=7976*)
    → "Ah, it's you again. Very kind of you to show, but I've yet to finish readying another set of grenades. Return here in a while, if you would."
  5: 0x014D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x014E [0x21] END_EVENT
  7: 0x014F [0x00] END_REQSTACK()
```
