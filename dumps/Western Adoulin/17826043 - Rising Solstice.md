# 17826043 - Rising Solstice

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 548 bytes                 |
| Total Events     | 12                        |
| References Count | 28                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [502](#event-502)        | 0x0001       |     47 |             11 |
| [580](#event-580)        | 0x0030       |     47 |             11 |
| [2](#event-2)            | 0x005F       |      1 |              1 |
| [65535.1](#event-655351) | 0x0060       |     24 |              3 |
| [2550](#event-2550)      | 0x0078       |     61 |             19 |
| [2551](#event-2551)      | 0x00B5       |     43 |              9 |
| [2552](#event-2552)      | 0x00E0       |     78 |             20 |
| [150](#event-150)        | 0x012E       |     58 |             15 |
| [159](#event-159)        | 0x0168       |      7 |              2 |
| [182](#event-182)        | 0x016F       |      1 |              1 |
| [181](#event-181)        | 0x0170       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x2622      |        9762 |
|       2 | 0x2623      |        9763 |
|       3 | 0x0041      |          65 |
|       4 | 0x2624      |        9764 |
|       5 | 0x2625      |        9765 |
|       6 | 0x0008      |           8 |
|       7 | 0x000A      |          10 |
|       8 | 0x0156      |         342 |
|       9 | 0x0140      |         320 |
|      10 | 0x00EF      |         239 |
|      11 | 0x0000      |           0 |
|      12 | 0x0001      |           1 |
|      13 | 0x1F0E      |        7950 |
|      14 | 0x1F0F      |        7951 |
|      15 | 0x1F10      |        7952 |
|      16 | 0x1F11      |        7953 |
|      17 | 0x1F12      |        7954 |
|      18 | 0x1F13      |        7955 |
|      19 | 0x1F35      |        7989 |
|      20 | 0x1F36      |        7990 |
|      21 | 0x1F37      |        7991 |
|      22 | 0x1F38      |        7992 |
|      23 | 0x1F39      |        7993 |
|      24 | 0x00C9      |         201 |
|      25 | 0x22F5      |        8949 |
|      26 | 0x22F6      |        8950 |
|      27 | 0x22F7      |        8951 |

## String References

- **7950**: Whaddya want?
- **7951**: I don't have time for louses like y...
- **7952**: Wait a minute. You seem like you have time on your hands. Why don't I give you some wholesome work? None of this stirring-up-trouble-in-the-jungle stuff.
- **7953**: The guard on duty today fell asleep before his patrol, that laggard. Take this paper with his route on it and fill in for him. You've got nothing better to do, right?
- **7954**: Follow those instructions to the letter. They shouldn't be hard to figure out, even for an outsider like you.
- **7955**: I thought I sent you out on patrol! Are you purposefully trying to scare our people? Now go!
- **7989**: Finally finished, huh? ...No one was troubled by anything? Good.
- **7990**: Speaking of trouble, everyone in the Peacekeepers' Coalition makes ridding our city of it their number one priority! There's no room for those who can't follow this mantra. That's why we'll be punishing the person you replaced today.
- **7991**: Patrolling the streets is not our only tactic. We also look out upon Adoulin from guard towers and the city walls. If we see any fires of discontent, we snuff them out!
- **7992**: Should monsters somehow breach Jorius Yett, we'll be there to stop them, too.
- **7993**: See, we have enough problems without having to deal with pioneers. Watch your step around this town, or we might just have to deal with you.
- **8949**: Have you heard? Some beasts from the jungles ran off with Arciela! The whole castle's as flustered as a flock of heartwings in heat.
- **8950**: You...knew that already? And you want me to keep mum?
- **8951**: Now that you mention it, I think I was told to keep my mouth shut by...oh great Goddess, my wagging tongue's done it again! My back can't tolerate any more lashes!
- **9762**: Not another foreigner... Well, you're here, so I guess I have to "welcome" you to Adoulin.
- **9763**: I'd prefer it if you got the hell out of my face and never came back. The coalition leaders, however, want you to become a pioneer. Better get on it and register then.
- **9764**: Pioneers, adventurers, whatever you call yourselves...you're all Velkk scat to me.
- **9765**: Just don't cause any trouble here in Western Adoulin and things won't get...messy.

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

### Event 502

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 66  ...tlk0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 21 00  ..........tlk1!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9762*)
    → "Not another foreigner... Well, you're here, so I guess I have to "welcome" you to Adoulin."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9763*)
    → "I'd prefer it if you got the hell out of my face and never came back. The coalition leaders, however, want you to become a pioneer. Better get on it and register then."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=60*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 580

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 66  03 80 F8 FF FF 7F F8 FF  .....opf........
0040: FF 7F 74 6C 62 30 1D 04  80 23 1D 05 80 23 66 03  ..tlb0...#...#f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 62 31 21 00     .........tlb1!. 
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  4: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=9764*)
    → "Pioneers, adventurers, whatever you call yourselves...you're all Velkk scat to me."
  5: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=9765*)
    → "Just don't cause any trouble here in Western Adoulin and things won't get...messy."
  7: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
  9: 0x005D [0x21] END_EVENT
 10: 0x005E [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               00                 .
```

#### Opcodes

```
  0: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: B6 0B 06 80 07 80 08 80  08 80 09 80 08 80 0A 80  ................
0070: 0B 80 0B 80 C0 0C 80 00                           ........        
```

#### Opcodes

```
  0: 0x0060 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=10*, head=342*, body=342*, hands=320*, legs=342*, feet=239*, main=0*, sub=0*)
  1: 0x0074 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0077 [0x00] END_REQSTACK()
```

### Event 2550

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 61 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          1E F0 FF FF 7F 42 6F 70          .....Bop
0080: 66 03 80 F8 FF FF 7F F8  FF FF 7F 74 6C 62 30 1D  f..........tlb0.
0090: 0D 80 23 1D 0E 80 23 1D  0F 80 23 1D 10 80 23 1D  ..#...#...#...#.
00A0: 11 80 23 66 03 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
00B0: 62 31 2E 21 00                                    b1.!.           
```

#### Opcodes

```
  0: 0x0078 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x007E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x007F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0080 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  5: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=7950*)
    → "Whaddya want?"
  6: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=7951*)
    → "I don't have time for louses like y..."
  8: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=7952*)
    → "Wait a minute. You seem like you have time on your hands. Why don't I give you some wholesome work? None of this stirring-up-trouble-in-the-jungle stuff."
 10: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=7953*)
    → "The guard on duty today fell asleep before his patrol, that laggard. Take this paper with his route on it and fill in for him. You've got nothing better to do, right?"
 12: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x009F [0x1D] PRINT_EVENT_MESSAGE(message_id=7954*)
    → "Follow those instructions to the letter. They shouldn't be hard to figure out, even for an outsider like you."
 14: 0x00A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00A3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
 16: 0x00B2 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 17: 0x00B3 [0x21] END_EVENT
 18: 0x00B4 [0x00] END_REQSTACK()
```

### Event 2551

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                1E F0 FF  FF 7F 6F 70 66 03 80 F8       .....opf...
00C0: FF FF 7F F8 FF FF 7F 74  6C 62 30 1D 12 80 23 66  .......tlb0...#f
00D0: 03 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 31 21 00  ..........tlb1!.
```

#### Opcodes

```
  0: 0x00B5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00BA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00BC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  4: 0x00CB [0x1D] PRINT_EVENT_MESSAGE(message_id=7955*)
    → "I thought I sent you out on patrol! Are you purposefully trying to scare our people? Now go!"
  5: 0x00CE [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00CF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
  7: 0x00DE [0x21] END_EVENT
  8: 0x00DF [0x00] END_REQSTACK()
```

### Event 2552

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 78 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 1E F0 FF FF 7F 42 6F 70  66 03 80 F8 FF FF 7F F8  .....Bopf.......
00F0: FF FF 7F 74 6C 62 30 1D  13 80 23 1D 14 80 23 1D  ...tlb0...#...#.
0100: 15 80 23 1D 16 80 23 1D  17 80 23 45 18 80 F8 FF  ..#...#...#E....
0110: FF 7F F8 FF FF 7F 71 73  74 63 0B 80 66 03 80 F8  ......qstc..f...
0120: FF FF 7F F8 FF FF 7F 74  6C 62 31 2E 21 00        .......tlb1.!.  
```

#### Opcodes

```
  0: 0x00E0 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00E5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00E6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00E7 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00E8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  5: 0x00F7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7989*)
    → "Finally finished, huh? ...No one was troubled by anything? Good."
  6: 0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00FB [0x1D] PRINT_EVENT_MESSAGE(message_id=7990*)
    → "Speaking of trouble, everyone in the Peacekeepers' Coalition makes ridding our city of it their number one priority! There's no room for those who can't follow this mantra. That's why we'll be punishing the person you replaced today."
  8: 0x00FE [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00FF [0x1D] PRINT_EVENT_MESSAGE(message_id=7991*)
    → "Patrolling the streets is not our only tactic. We also look out upon Adoulin from guard towers and the city walls. If we see any fires of discontent, we snuff them out!"
 10: 0x0102 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=7992*)
    → "Should monsters somehow breach Jorius Yett, we'll be there to stop them, too."
 12: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0107 [0x1D] PRINT_EVENT_MESSAGE(message_id=7993*)
    → "See, we have enough problems without having to deal with pioneers. Watch your step around this town, or we might just have to deal with you."
 14: 0x010A [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x010B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 16: 0x011C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
 17: 0x012B [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 18: 0x012C [0x21] END_EVENT
 19: 0x012D [0x00] END_REQSTACK()
```

### Event 150

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012E   |
| Data Size    | 58 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                            1E F0                ..
0130: FF FF 7F 6F 70 66 00 80  F8 FF FF 7F F8 FF FF 7F  ...opf..........
0140: 61 6E 67 30 1D 19 80 23  5E 69 64 6C 30 1D 1A 80  ang0...#^idl0...
0150: 23 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  #f..........tlk0
0160: 1D 1B 80 23 20 00 21 00                           ...# .!.        
```

#### Opcodes

```
  0: 0x012E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0133 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0134 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0135 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=60*
  4: 0x0144 [0x1D] PRINT_EVENT_MESSAGE(message_id=8949*)
    → "Have you heard? Some beasts from the jungles ran off with Arciela! The whole castle's as flustered as a flock of heartwings in heat."
  5: 0x0147 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0148 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x014D [0x1D] PRINT_EVENT_MESSAGE(message_id=8950*)
    → "You...knew that already? And you want me to keep mum?"
  8: 0x0150 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0151 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
 10: 0x0160 [0x1D] PRINT_EVENT_MESSAGE(message_id=8951*)
    → "Now that you mention it, I think I was told to keep my mouth shut by...oh great Goddess, my wagging tongue's done it again! My back can't tolerate any more lashes!"
 11: 0x0163 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0164 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0166 [0x21] END_EVENT
 14: 0x0167 [0x00] END_REQSTACK()
```

### Event 159

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0168  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0168 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x016E [0x00] END_REQSTACK()
```

### Event 182

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x016F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                               00                 .
```

#### Opcodes

```
  0: 0x016F [0x00] END_REQSTACK()
```

### Event 181

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0170  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170: 00                                                .               
```

#### Opcodes

```
  0: 0x0170 [0x00] END_REQSTACK()
```
