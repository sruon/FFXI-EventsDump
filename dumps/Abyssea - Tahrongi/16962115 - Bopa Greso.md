# 16962115 - Bopa Greso

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 1228 bytes                  |
| Total Events     | 7                           |
| References Count | 28                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [366](#event-366)     | 0x0001       |     60 |             12 |
| [367](#event-367)     | 0x003D       |    514 |             74 |
| [368](#event-368)     | 0x023F       |     56 |             10 |
| [369](#event-369)     | 0x0277       |    163 |             23 |
| [370](#event-370)     | 0x031A       |     13 |              7 |
| [371](#event-371)     | 0x0327       |    263 |             39 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F3B      |        7995 |
|       1 | 0x0167      |         359 |
|       2 | 0x1F3C      |        7996 |
|       3 | 0x1F3E      |        7998 |
|       4 | 0x1F3F      |        7999 |
|       5 | 0x0001      |           1 |
|       6 | 0x0000      |           0 |
|       7 | 0x1F40      |        8000 |
|       8 | 0x1F41      |        8001 |
|       9 | 0x1F42      |        8002 |
|      10 | 0x1F43      |        8003 |
|      11 | 0x0166      |         358 |
|      12 | 0x1F44      |        8004 |
|      13 | 0x1F45      |        8005 |
|      14 | 0x1F46      |        8006 |
|      15 | 0x1F47      |        8007 |
|      16 | 0x0169      |         361 |
|      17 | 0x1F48      |        8008 |
|      18 | 0x1F49      |        8009 |
|      19 | 0x1F4A      |        8010 |
|      20 | 0x1F4F      |        8015 |
|      21 | 0x1F50      |        8016 |
|      22 | 0x00C9      |         201 |
|      23 | 0x1F51      |        8017 |
|      24 | 0x1F52      |        8018 |
|      25 | 0x1F53      |        8019 |
|      26 | 0x1F54      |        8020 |
|      27 | 0x1F55      |        8021 |

## String References

- **7995**: "Get your act together! We must band together to surrrvive!" "Do you have a death wish?" Sheesh! That mercenary captain won't stop yappin' her trrrap.
- **7996**: She just doesn't get it. It's times like these a girrrl's gotta watch out for herself. We've got enough to worry 'bout without dealin' with everrryone's whimperings.
- **7998**: You've got the looks of someone who's been around the block. Someone who's looked danger in the eye and lived to tell the tale. Am I rrright?
- **7999**: Am I rrright? [You're rrright./Dead wrrrong.]
- **8000**: Oh, is that so? Then you'd best get out of here, and quickly. This ain't the place for no shelterrred little [prince/princess].
- **8001**: Heh, I knew it. My gut instincts haven't failed me yet. Tell me, does the name Nanaa Mihgo mean anything to you?
- **8003**: We followed her to Heavens Tower when those nasty buggers burst through the city walls, but after we teleported out here, she was nowherrre t' be found.
- **8005**: Slap these up on the signposts around the canyon, let the boss know we're safe and sound, and our merry little band'll be back together in no time flat!
- **8006**: We were gonna do it ourselves, but hey, why brrreak a sweat when you've got someone to do it for ya?
- **8007**: No, don't arrrgue--we insist. Unless you'd care to part with that spiffy garb you're wearin', of course...
- **8009**: Anyhow, you'll find four signposts scattered through the canyon. Slap one of these on each of 'em, and rrreport to us when the job is done.
- **8015**: You did good, kid. It's only a matter of time before we're rrreunited with the boss now.
- **8017**: You there! It's about time you showed up!
- **8019**: That's right, it's one of the $5 that you posted for us.
- **8021**: Yep, someone's going to have to get back out there and do the job all over again.

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

### Event 366

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 5B 01 80 F8   .....op...#[...
0010: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 02 80 23 5B  .......tlk0...#[
0020: 01 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 32 53 F8  ..........tlk2S.
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 32 21 00           .......tlk2!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7995*)
    → ""Get your act together! We must band together to surrrvive!" "Do you have a death wish?" Sheesh! That mercenary captain won't stop yappin' her trrrap."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7996*)
    → "She just doesn't get it. It's times like these a girrrl's gotta watch out for herself. We've got enough to worry 'bout without dealin' with everrryone's whimperings."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=359*
  9: 0x002E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 10: 0x003B [0x21] END_EVENT
 11: 0x003C [0x00] END_REQSTACK()
```

### Event 367

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x003D    |
| Data Size    | 514 bytes |
| Instructions | 73        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         42 1E F0               B..
0040: FF FF 7F 4A F0 FF FF 7F  F8 FF FF 7F 4A 44 D2 02  ...J........JD..
0050: 01 F0 FF FF 7F 6F 70 6F  76 44 D2 02 01 1D 03 80  .....opovD......
0060: 23 24 04 80 05 80 06 80  25 02 00 10 06 80 00 79  #$......%......y
0070: 00 03 01 10 06 80 01 8F  00 02 00 10 05 80 00 8F  ................
0080: 00 1D 07 80 23 03 01 10  05 80 21 00 01 8F 00 5B  ....#.....!....[
0090: 01 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 08  ..........tlk0..
00A0: 80 23 5B 01 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#[..........tlk
00B0: 32 53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 32 4A F0  2S........tlk2J.
00C0: FF FF 7F 44 D2 02 01 5B  01 80 44 D2 02 01 44 D2  ...D...[..D...D.
00D0: 02 01 74 6C 6B 30 2B 44  D2 02 01 09 80 23 5B 01  ..tlk0+D.....#[.
00E0: 80 44 D2 02 01 44 D2 02  01 74 6C 6B 32 53 44 D2  .D...D...tlk2SD.
00F0: 02 01 44 D2 02 01 74 6C  6B 32 4A F0 FF FF 7F F8  ..D...tlk2J.....
0100: FF FF 7F 5B 01 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ...[..........tl
0110: 6B 30 1D 0A 80 23 5B 01  80 F8 FF FF 7F F8 FF FF  k0...#[.........
0120: 7F 74 6C 6B 32 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  .tlk2S........tl
0130: 6B 32 4A F0 FF FF 7F 44  D2 02 01 7C 00 44 D2 02  k2J....D...|.D..
0140: 01 5B 0B 80 44 D2 02 01  44 D2 02 01 67 75 74 30  .[..D...D...gut0
0150: 2B 44 D2 02 01 0C 80 23  53 44 D2 02 01 44 D2 02  +D.....#SD...D..
0160: 01 67 75 74 30 7C 01 44  D2 02 01 4A F0 FF FF 7F  .gut0|.D...J....
0170: F8 FF FF 7F 5B 01 80 F8  FF FF 7F F8 FF FF 7F 74  ....[..........t
0180: 6C 6B 30 1D 0D 80 23 1D  0E 80 23 1D 0F 80 23 5B  lk0...#...#...#[
0190: 01 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 32 53 F8  ..........tlk2S.
01A0: FF FF 7F F8 FF FF 7F 74  6C 6B 32 4A F0 FF FF 7F  .......tlk2J....
01B0: 44 D2 02 01 5B 10 80 44  D2 02 01 44 D2 02 01 70  D...[..D...D...p
01C0: 6F 69 30 2B 44 D2 02 01  11 80 23 53 F8 FF FF 7F  oi0+D.....#S....
01D0: F8 FF FF 7F 74 6C 6B 32  53 44 D2 02 01 44 D2 02  ....tlk2SD...D..
01E0: 01 70 6F 69 30 4A F0 FF  FF 7F F8 FF FF 7F 5B 01  .poi0J........[.
01F0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 12 80  .........tlk0...
0200: 23 5B 01 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 32  #[..........tlk2
0210: 4A F0 FF FF 7F 44 D2 02  01 5B 10 80 44 D2 02 01  J....D...[..D...
0220: 44 D2 02 01 77 61 76 30  2B 44 D2 02 01 13 80 23  D...wav0+D.....#
0230: 53 44 D2 02 01 44 D2 02  01 77 61 76 30 21 00     SD...D...wav0!. 
```

#### Opcodes

```
  0: 0x003D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x003E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0043 [0x4A] LocalPlayer looks at EventEntity
  3: 0x004C [0x4A] Cha Lebagta (ID: 16962116/0x0102D244) looks at LocalPlayer
  4: 0x0055 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0056 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0057 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0058 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Cha Lebagta (ID: 16962116/0x0102D244) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=7998*)
    → "You've got the looks of someone who's been around the block. Someone who's looked danger in the eye and lived to tell the tale. Am I rrright?"
  9: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0061 [0x24] CREATE_DIALOG(message_id=7999*, default_option=1*, option_flags=0*)
    → "Am I rrright? [You're rrright./Dead wrrrong.]"
 11: 0x0068 [0x25] WAIT_DIALOG_SELECT()
 12: 0x0069 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0079
 13: 0x0071 [0x03] Work_Zone[1] = 0*
 14: 0x0076 [0x01] GOTO 0x008F
 15: 0x0079 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x008F
 16: 0x0081 [0x1D] PRINT_EVENT_MESSAGE(message_id=8000*)
    → "Oh, is that so? Then you'd best get out of here, and quickly. This ain't the place for no shelterrred little [prince/princess]."
 17: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0085 [0x03] Work_Zone[1] = 1*
 19: 0x008A [0x21] END_EVENT
 20: 0x008B [0x00] END_REQSTACK()

SUBROUTINE_008F:
 21: 0x008F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
 22: 0x009E [0x1D] PRINT_EVENT_MESSAGE(message_id=8001*)
    → "Heh, I knew it. My gut instincts haven't failed me yet. Tell me, does the name Nanaa Mihgo mean anything to you?"
 23: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x00A2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=359*
 25: 0x00B1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 26: 0x00BE [0x4A] LocalPlayer looks at Cha Lebagta (ID: 16962116/0x0102D244)
 27: 0x00C7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=359*
 28: 0x00D6 [0x2B] Cha Lebagta (ID: 16962116/0x0102D244) [8002*]:
    → "The cat burglar? Chieftainness o' cutpurrrses and pickpocket nonparrreil? Made somethin' of a name for herself back in Windurst. Well, what would ya think if we told ya she was our boss?"
 29: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x00DE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=359*
 31: 0x00ED [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)]
 32: 0x00FA [0x4A] LocalPlayer looks at EventEntity
 33: 0x0103 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
 34: 0x0112 [0x1D] PRINT_EVENT_MESSAGE(message_id=8003*)
    → "We followed her to Heavens Tower when those nasty buggers burst through the city walls, but after we teleported out here, she was nowherrre t' be found."
 35: 0x0115 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x0116 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=359*
 37: 0x0125 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 38: 0x0132 [0x4A] LocalPlayer looks at Cha Lebagta (ID: 16962116/0x0102D244)
 39: 0x013B [0x7C] Cha Lebagta (ID: 16962116/0x0102D244)->Render.Flags2 |= 0x00
 40: 0x0141 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gut0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=358*
 41: 0x0150 [0x2B] Cha Lebagta (ID: 16962116/0x0102D244) [8004*]:
    → "That's why we came up with these beauties!"
 42: 0x0157 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x0158 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gut0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)]
 44: 0x0165 [0x7C] Cha Lebagta (ID: 16962116/0x0102D244)->Render.Flags2 |= 0x01
 45: 0x016B [0x4A] LocalPlayer looks at EventEntity
 46: 0x0174 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
 47: 0x0183 [0x1D] PRINT_EVENT_MESSAGE(message_id=8005*)
    → "Slap these up on the signposts around the canyon, let the boss know we're safe and sound, and our merry little band'll be back together in no time flat!"
 48: 0x0186 [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x0187 [0x1D] PRINT_EVENT_MESSAGE(message_id=8006*)
    → "We were gonna do it ourselves, but hey, why brrreak a sweat when you've got someone to do it for ya?"
 50: 0x018A [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x018B [0x1D] PRINT_EVENT_MESSAGE(message_id=8007*)
    → "No, don't arrrgue--we insist. Unless you'd care to part with that spiffy garb you're wearin', of course..."
 52: 0x018E [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x018F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=359*
 54: 0x019E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 55: 0x01AB [0x4A] LocalPlayer looks at Cha Lebagta (ID: 16962116/0x0102D244)
 56: 0x01B4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=361*
 57: 0x01C3 [0x2B] Cha Lebagta (ID: 16962116/0x0102D244) [8008*]:
    → "Just think of it as a favor you'll be doin' all the surrrvivors in these parts. After all, if there's anyone who can teach 'em a thing or two about stayin' safe in the face of danger, it's the boss. She may help herself to some o' their possessions in the prrrocess, but hey, that's business."
 58: 0x01CA [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x01CB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 60: 0x01D8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)]
 61: 0x01E5 [0x4A] LocalPlayer looks at EventEntity
 62: 0x01EE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
 63: 0x01FD [0x1D] PRINT_EVENT_MESSAGE(message_id=8009*)
    → "Anyhow, you'll find four signposts scattered through the canyon. Slap one of these on each of 'em, and rrreport to us when the job is done."
 64: 0x0200 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x0201 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=359*
 66: 0x0210 [0x4A] LocalPlayer looks at Cha Lebagta (ID: 16962116/0x0102D244)
 67: 0x0219 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wav0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=361*
 68: 0x0228 [0x2B] Cha Lebagta (ID: 16962116/0x0102D244) [8010*]:
    → "Now get crrrackin'!"
 69: 0x022F [0x23] WAIT_FOR_DIALOG_INTERACTION
 70: 0x0230 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wav0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)]
 71: 0x023D [0x21] END_EVENT
 72: 0x023E [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x008C [0x01] GOTO 0x008F
```

### Event 368

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x023F   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                                               1E                 .
0240: F0 FF FF 7F 6F 70 5B 01  80 F8 FF FF 7F F8 FF FF  ....op[.........
0250: 7F 74 6C 6B 30 1D 12 80  23 5B 01 80 F8 FF FF 7F  .tlk0...#[......
0260: F8 FF FF 7F 74 6C 6B 32  53 F8 FF FF 7F F8 FF FF  ....tlk2S.......
0270: 7F 74 6C 6B 32 21 00                              .tlk2!.         
```

#### Opcodes

```
  0: 0x023F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0244 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0245 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0246 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
  4: 0x0255 [0x1D] PRINT_EVENT_MESSAGE(message_id=8009*)
    → "Anyhow, you'll find four signposts scattered through the canyon. Slap one of these on each of 'em, and rrreport to us when the job is done."
  5: 0x0258 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0259 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=359*
  7: 0x0268 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
  8: 0x0275 [0x21] END_EVENT
  9: 0x0276 [0x00] END_REQSTACK()
```

### Event 369

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0277    |
| Data Size    | 163 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                      42  1E F0 FF FF 7F 4A F0 FF         B.....J..
0280: FF 7F F8 FF FF 7F 4A 44  D2 02 01 F0 FF FF 7F 6F  ......JD.......o
0290: 70 6F 76 44 D2 02 01 03  02 10 8B 7F 5B 01 80 F8  povD........[...
02A0: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 14 80 23 5B  .......tlk0...#[
02B0: 01 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 32 53 F8  ..........tlk2S.
02C0: FF FF 7F F8 FF FF 7F 74  6C 6B 32 4A F0 FF FF 7F  .......tlk2J....
02D0: 44 D2 02 01 5B 01 80 44  D2 02 01 44 D2 02 01 74  D...[..D...D...t
02E0: 6C 6B 30 2B 44 D2 02 01  15 80 23 5B 01 80 44 D2  lk0+D.....#[..D.
02F0: 02 01 44 D2 02 01 74 6C  6B 32 53 44 D2 02 01 44  ..D...tlk2SD...D
0300: D2 02 01 74 6C 6B 32 45  16 80 F0 FF FF 7F F0 FF  ...tlk2E........
0310: FF 7F 71 73 74 63 06 80  21 00                    ..qstc..!.      
```

#### Opcodes

```
  0: 0x0277 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0278 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x027D [0x4A] LocalPlayer looks at EventEntity
  3: 0x0286 [0x4A] Cha Lebagta (ID: 16962116/0x0102D244) looks at LocalPlayer
  4: 0x028F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0290 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0291 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0292 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Cha Lebagta (ID: 16962116/0x0102D244) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x0297 [0x03] Work_Zone[2] = (LocalPlayer->Render.Flags01 >> 25) & 1
  9: 0x029C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
 10: 0x02AB [0x1D] PRINT_EVENT_MESSAGE(message_id=8015*)
    → "You did good, kid. It's only a matter of time before we're rrreunited with the boss now."
 11: 0x02AE [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x02AF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=359*
 13: 0x02BE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 14: 0x02CB [0x4A] LocalPlayer looks at Cha Lebagta (ID: 16962116/0x0102D244)
 15: 0x02D4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=359*
 16: 0x02E3 [0x2B] Cha Lebagta (ID: 16962116/0x0102D244) [8016*]:
    → "We'd make you an honorary member of our band, but that would mean havin' to split the prrrofits. No hard feelings, 'kay?"
 17: 0x02EA [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x02EB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=359*
 19: 0x02FA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)]
 20: 0x0307 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0318 [0x21] END_EVENT
 22: 0x0319 [0x00] END_REQSTACK()
```

### Event 370

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x031A   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0310:                                1E F0 FF FF 7F 6F            .....o
0320: 70 1D 14 80 23 21 00                              p...#!.         
```

#### Opcodes

```
  0: 0x031A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x031F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0320 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0321 [0x1D] PRINT_EVENT_MESSAGE(message_id=8015*)
    → "You did good, kid. It's only a matter of time before we're rrreunited with the boss now."
  4: 0x0324 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0325 [0x21] END_EVENT
  6: 0x0326 [0x00] END_REQSTACK()
```

### Event 371

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0327    |
| Data Size    | 263 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0320:                      42  1E F0 FF FF 7F 4A F0 FF         B.....J..
0330: FF 7F F8 FF FF 7F 4A 44  D2 02 01 F0 FF FF 7F 6F  ......JD.......o
0340: 70 6F 76 44 D2 02 01 1D  17 80 23 4A F0 FF FF 7F  povD......#J....
0350: 44 D2 02 01 5B 10 80 44  D2 02 01 44 D2 02 01 70  D...[..D...D...p
0360: 6F 69 30 2B 44 D2 02 01  18 80 23 53 44 D2 02 01  oi0+D.....#SD...
0370: 44 D2 02 01 70 6F 69 30  4A F0 FF FF 7F F8 FF FF  D...poi0J.......
0380: 7F 5B 01 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .[..........tlk0
0390: 1D 19 80 23 5B 01 80 F8  FF FF 7F F8 FF FF 7F 74  ...#[..........t
03A0: 6C 6B 32 53 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 32  lk2S........tlk2
03B0: 5B 01 80 44 D2 02 01 44  D2 02 01 74 6C 6B 30 4A  [..D...D...tlk0J
03C0: F0 FF FF 7F 44 D2 02 01  2B 44 D2 02 01 1A 80 23  ....D...+D.....#
03D0: 5B 01 80 44 D2 02 01 44  D2 02 01 74 6C 6B 32 53  [..D...D...tlk2S
03E0: 44 D2 02 01 44 D2 02 01  74 6C 6B 32 4A F0 FF FF  D...D...tlk2J...
03F0: 7F F8 FF FF 7F 5B 01 80  F8 FF FF 7F F8 FF FF 7F  .....[..........
0400: 74 6C 6B 30 1D 1B 80 23  1D 0E 80 23 1D 12 80 23  tlk0...#...#...#
0410: 5B 01 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 32 53  [..........tlk2S
0420: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 32 21 00        ........tlk2!.  
```

#### Opcodes

```
  0: 0x0327 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0328 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x032D [0x4A] LocalPlayer looks at EventEntity
  3: 0x0336 [0x4A] Cha Lebagta (ID: 16962116/0x0102D244) looks at LocalPlayer
  4: 0x033F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0340 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0341 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0342 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Cha Lebagta (ID: 16962116/0x0102D244) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x0347 [0x1D] PRINT_EVENT_MESSAGE(message_id=8017*)
    → "You there! It's about time you showed up!"
  9: 0x034A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x034B [0x4A] LocalPlayer looks at Cha Lebagta (ID: 16962116/0x0102D244)
 11: 0x0354 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=361*
 12: 0x0363 [0x2B] Cha Lebagta (ID: 16962116/0x0102D244) [8018*]:
    → "Tell me: does this look familiarrr to you?"
 13: 0x036A [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x036B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)]
 15: 0x0378 [0x4A] LocalPlayer looks at EventEntity
 16: 0x0381 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
 17: 0x0390 [0x1D] PRINT_EVENT_MESSAGE(message_id=8019*)
    → "That's right, it's one of the $5 that you posted for us."
 18: 0x0393 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0394 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=359*
 20: 0x03A3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 21: 0x03B0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=359*
 22: 0x03BF [0x4A] LocalPlayer looks at Cha Lebagta (ID: 16962116/0x0102D244)
 23: 0x03C8 [0x2B] Cha Lebagta (ID: 16962116/0x0102D244) [8020*]:
    → "I dunno if a gust o' wind got it, or if you're just a sorry poster-putter-upper, but one thing's for sure...it ain't gonna do us any good lyin' on the grrround here."
 24: 0x03CF [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x03D0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)], work=359*
 26: 0x03DF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [Cha Lebagta (ID: 16962116/0x0102D244), Cha Lebagta (ID: 16962116/0x0102D244)]
 27: 0x03EC [0x4A] LocalPlayer looks at EventEntity
 28: 0x03F5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
 29: 0x0404 [0x1D] PRINT_EVENT_MESSAGE(message_id=8021*)
    → "Yep, someone's going to have to get back out there and do the job all over again."
 30: 0x0407 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x0408 [0x1D] PRINT_EVENT_MESSAGE(message_id=8006*)
    → "We were gonna do it ourselves, but hey, why brrreak a sweat when you've got someone to do it for ya?"
 32: 0x040B [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x040C [0x1D] PRINT_EVENT_MESSAGE(message_id=8009*)
    → "Anyhow, you'll find four signposts scattered through the canyon. Slap one of these on each of 'em, and rrreport to us when the job is done."
 34: 0x040F [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x0410 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=359*
 36: 0x041F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
 37: 0x042C [0x21] END_EVENT
 38: 0x042D [0x00] END_REQSTACK()
```
