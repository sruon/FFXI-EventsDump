# 17727504 - Fontoumant

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 864 bytes                 |
| Total Events     | 12                        |
| References Count | 31                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [509](#event-509)     | 0x0001       |    176 |             48 |
| [511](#event-511)     | 0x00B1       |     77 |             21 |
| [512](#event-512)     | 0x00FE       |     82 |             20 |
| [515](#event-515)     | 0x0150       |     89 |             17 |
| [561](#event-561)     | 0x01A9       |     36 |             10 |
| [560](#event-560)     | 0x01CD       |     50 |             16 |
| [537](#event-537)     | 0x01FF       |     36 |             10 |
| [558](#event-558)     | 0x0223       |      6 |              4 |
| [608](#event-608)     | 0x0229       |     41 |             13 |
| [609](#event-609)     | 0x0252       |     41 |             13 |
| [610](#event-610)     | 0x027B       |     41 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1D5F      |        7519 |
|       2 | 0x1D60      |        7520 |
|       3 | 0x1D61      |        7521 |
|       4 | 0x1D62      |        7522 |
|       5 | 0x1D63      |        7523 |
|       6 | 0x0000      |           0 |
|       7 | 0x1D66      |        7526 |
|       8 | 0x1D67      |        7527 |
|       9 | 0x1D6F      |        7535 |
|      10 | 0x1D70      |        7536 |
|      11 | 0x1D71      |        7537 |
|      12 | 0x0001      |           1 |
|      13 | 0x1D64      |        7524 |
|      14 | 0x1D7F      |        7551 |
|      15 | 0x1D80      |        7552 |
|      16 | 0x1D81      |        7553 |
|      17 | 0x1D86      |        7558 |
|      18 | 0x1D87      |        7559 |
|      19 | 0x1D88      |        7560 |
|      20 | 0x1D8E      |        7566 |
|      21 | 0x1D8F      |        7567 |
|      22 | 0x00C9      |         201 |
|      23 | 0x1D69      |        7529 |
|      24 | 0x1D6A      |        7530 |
|      25 | 0x1D6B      |        7531 |
|      26 | 0x1D68      |        7528 |
|      27 | 0x1D90      |        7568 |
|      28 | 0x1D6C      |        7532 |
|      29 | 0x1D6D      |        7533 |
|      30 | 0x1D6E      |        7534 |

## String References

- **7519**: Ah, what have we here, a new recruit? I am Fontoumant. Nothing comes in or out the Consortium's warehouses without me knowing about it.
- **7520**: We get shipments from every land here. I can never hire enough workers to handle the load.
- **7521**: Youngsters these days, they lack fortitude! They show up for work once or twice and they disappear. Like seabirds before a gale, they are. Leaving me holding the feathers!
- **7522**: Ah, which reminds me. You wouldn't be needing work, would you? My gil is good, and there's much to be done.
- **7523**: How about it? [I'll work./No, thanks.]
- **7524**: Ach, just like the yearlings I get everyday, you are. Not a strong back in the lot of you!
- **7526**: That's the spirit! There may be some hope for your generation, yet. Here, your first parcel!
- **7527**: Mind you, if you lose it, I'll expect payment for the lost goods. That's my only rule.
- **7528**: Hmm...seems you've a fondness for hauling things already! Clear out your inventory before you take on mine.
- **7529**: I expect you to deliver a parcel before taking another. Everything in the proper order, please.
- **7530**: Wait, you haven't lost the extremely important parcel I entrusted you with, have you?
- **7531**: If you've lost it, you'll have to pay for the loss. Give me 100 gil then and we'll be even.
- **7532**: Fine. Very well, I'll have to go apologize to Regine over at the Magicmart in person. Take more care, next time.
- **7533**: Fine. Very well, I'll have to go apologize to Apstaule over at the auction house in person. Take more care, next time.
- **7534**: Fine. Very well, I'll have to go apologize to Thierride over at the tavern in person. Take more care, next time.
- **7535**: Your first parcel is for Regine's Magicmart.
- **7536**: You'll find it at the end of a passage branching off from the east tunnel.
- **7537**: Give the parcel to the shop owner, Miss Regine, if you would.
- **7551**: This should be easy. Your next parcel is for the auction house.
- **7552**: Walk out that door over there, and it will be right in front of your nose. You can't miss it.
- **7553**: Give the parcel to Apstaule, understood?
- **7558**: Finally! Your third parcel's for the pub.
- **7559**: Go out the door below, turn left, and walk along the waterfront. You'll find the Rusty Anchor there.
- **7560**: Deliver the parcel to a Mr. Thierride. And remember, you're on business!
- **7566**: You did well, <Player>. That should do it for now.
- **7567**: You've done well. Here, take this.
- **7568**: You cannot carry any more gil.

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

### Event 509

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 176 bytes |
| Instructions | 48        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  5B 00 80 F8 FF FF 7F F8   .....op[.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1C 00 80 1D 02  ...tlk0...#.....
0020: 80 23 1C 00 80 1D 03 80  23 1C 00 80 1D 04 80 23  .#......#......#
0030: 5E 69 64 6C 30 24 05 80  06 80 06 80 25 02 00 10  ^idl0$......%...
0040: 06 80 00 84 00 5B 00 80  F8 FF FF 7F F8 FF FF 7F  .....[..........
0050: 74 6C 6B 30 1D 07 80 23  1C 00 80 1D 08 80 23 1C  tlk0...#......#.
0060: 00 80 1D 09 80 23 1C 00  80 1D 0A 80 23 1C 00 80  .....#......#...
0070: 1D 0B 80 23 5E 69 64 6C  30 1C 00 80 03 01 10 06  ...#^idl0.......
0080: 80 01 AF 00 02 00 10 0C  80 00 AF 00 5B 00 80 F8  ............[...
0090: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 0D 80 23 5E  .......tlk0...#^
00A0: 69 64 6C 30 1C 00 80 03  01 10 0C 80 01 AF 00 21  idl0...........!
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7519*)
    → "Ah, what have we here, a new recruit? I am Fontoumant. Nothing comes in or out the Consortium's warehouses without me knowing about it."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1C] WAIT(30* ticks)
  7: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7520*)
    → "We get shipments from every land here. I can never hire enough workers to handle the load."
  8: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0022 [0x1C] WAIT(30* ticks)
 10: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7521*)
    → "Youngsters these days, they lack fortitude! They show up for work once or twice and they disappear. Like seabirds before a gale, they are. Leaving me holding the feathers!"
 11: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0029 [0x1C] WAIT(30* ticks)
 13: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=7522*)
    → "Ah, which reminds me. You wouldn't be needing work, would you? My gil is good, and there's much to be done."
 14: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0030 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 16: 0x0035 [0x24] CREATE_DIALOG(message_id=7523*, default_option=0*, option_flags=0*)
    → "How about it? [I'll work./No, thanks.]"
 17: 0x003C [0x25] WAIT_DIALOG_SELECT()
 18: 0x003D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0084
 19: 0x0045 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
 20: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=7526*)
    → "That's the spirit! There may be some hope for your generation, yet. Here, your first parcel!"
 21: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0058 [0x1C] WAIT(30* ticks)
 23: 0x005B [0x1D] PRINT_EVENT_MESSAGE(message_id=7527*)
    → "Mind you, if you lose it, I'll expect payment for the lost goods. That's my only rule."
 24: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x005F [0x1C] WAIT(30* ticks)
 26: 0x0062 [0x1D] PRINT_EVENT_MESSAGE(message_id=7535*)
    → "Your first parcel is for Regine's Magicmart."
 27: 0x0065 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0066 [0x1C] WAIT(30* ticks)
 29: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=7536*)
    → "You'll find it at the end of a passage branching off from the east tunnel."
 30: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x006D [0x1C] WAIT(30* ticks)
 32: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=7537*)
    → "Give the parcel to the shop owner, Miss Regine, if you would."
 33: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0074 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 35: 0x0079 [0x1C] WAIT(30* ticks)
 36: 0x007C [0x03] Work_Zone[1] = 0*
 37: 0x0081 [0x01] GOTO 0x00AF
 38: 0x0084 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00AF
 39: 0x008C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
 40: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=7524*)
    → "Ach, just like the yearlings I get everyday, you are. Not a strong back in the lot of you!"
 41: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x009F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 43: 0x00A4 [0x1C] WAIT(30* ticks)
 44: 0x00A7 [0x03] Work_Zone[1] = 1*
 45: 0x00AC [0x01] GOTO 0x00AF

SUBROUTINE_00AF:
 46: 0x00AF [0x21] END_EVENT
 47: 0x00B0 [0x00] END_REQSTACK()
```

### Event 511

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 77 bytes |
| Instructions | 21       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    1E F0 FF FF 7F 6F 70  5B 00 80 F8 FF FF 7F F8   .....op[.......
00C0: FF FF 7F 74 6C 6B 30 1D  0E 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
00D0: 1C 00 80 1E 42 80 0E 01  6F 70 5B 00 80 F8 FF FF  ....B...op[.....
00E0: 7F F8 FF FF 7F 74 6C 6B  30 1D 0F 80 23 1C 00 80  .....tlk0...#...
00F0: 1D 10 80 23 5E 69 64 6C  30 1C 00 80 21 00        ...#^idl0...!.  
```

#### Opcodes

```
  0: 0x00B1 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B7 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00B8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7551*)
    → "This should be easy. Your next parcel is for the auction house."
  5: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00CB [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x00D0 [0x1C] WAIT(30* ticks)
  8: 0x00D3 [0x1E] EventEntity looks at Sheridan (ID: 17727554/0x010E8042) and starts talking
  9: 0x00D8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x00D9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 11: 0x00DA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
 12: 0x00E9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7552*)
    → "Walk out that door over there, and it will be right in front of your nose. You can't miss it."
 13: 0x00EC [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00ED [0x1C] WAIT(30* ticks)
 15: 0x00F0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7553*)
    → "Give the parcel to Apstaule, understood?"
 16: 0x00F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00F4 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 18: 0x00F9 [0x1C] WAIT(30* ticks)
 19: 0x00FC [0x21] END_EVENT
 20: 0x00FD [0x00] END_REQSTACK()
```

### Event 512

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FE   |
| Data Size    | 82 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            1E F0                ..
0100: FF FF 7F 6F 70 5B 00 80  F8 FF FF 7F F8 FF FF 7F  ...op[..........
0110: 74 6C 6B 30 1D 11 80 23  5E 69 64 6C 30 1C 00 80  tlk0...#^idl0...
0120: 4A F0 FF FF 7F 0D 80 0E  01 1C 00 80 5B 00 80 F8  J...........[...
0130: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 12 80 23 1C  .......tlk0...#.
0140: 00 80 1D 13 80 23 5E 69  64 6C 30 1C 00 80 21 00  .....#^idl0...!.
```

#### Opcodes

```
  0: 0x00FE [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0103 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0104 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0105 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0114 [0x1D] PRINT_EVENT_MESSAGE(message_id=7558*)
    → "Finally! Your third parcel's for the pub."
  5: 0x0117 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0118 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x011D [0x1C] WAIT(30* ticks)
  8: 0x0120 [0x4A] LocalPlayer looks at Antreneau (ID: 17727501/0x010E800D)
  9: 0x0129 [0x1C] WAIT(30* ticks)
 10: 0x012C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
 11: 0x013B [0x1D] PRINT_EVENT_MESSAGE(message_id=7559*)
    → "Go out the door below, turn left, and walk along the waterfront. You'll find the Rusty Anchor there."
 12: 0x013E [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x013F [0x1C] WAIT(30* ticks)
 14: 0x0142 [0x1D] PRINT_EVENT_MESSAGE(message_id=7560*)
    → "Deliver the parcel to a Mr. Thierride. And remember, you're on business!"
 15: 0x0145 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0146 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 17: 0x014B [0x1C] WAIT(30* ticks)
 18: 0x014E [0x21] END_EVENT
 19: 0x014F [0x00] END_REQSTACK()
```

### Event 515

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0150   |
| Data Size    | 89 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150: 42 1E F0 FF FF 7F 6F 70  5B 00 80 F8 FF FF 7F F8  B.....op[.......
0160: FF FF 7F 74 6C 6B 30 1D  14 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
0170: 1C 00 80 5B 00 80 F8 FF  FF 7F F8 FF FF 7F 70 61  ...[..........pa
0180: 73 30 1D 15 80 23 53 F8  FF FF 7F F8 FF FF 7F 70  s0...#S........p
0190: 61 73 30 45 16 80 F0 FF  FF 7F F0 FF FF 7F 71 73  as0E..........qs
01A0: 74 63 06 80 1C 00 80 21  00                       tc.....!.       
```

#### Opcodes

```
  0: 0x0150 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0151 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0156 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0157 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0158 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  5: 0x0167 [0x1D] PRINT_EVENT_MESSAGE(message_id=7566*)
    → "You did well, <Player>. That should do it for now."
  6: 0x016A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x016B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  8: 0x0170 [0x1C] WAIT(30* ticks)
  9: 0x0173 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=30*
 10: 0x0182 [0x1D] PRINT_EVENT_MESSAGE(message_id=7567*)
    → "You've done well. Here, take this."
 11: 0x0185 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0186 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 13: 0x0193 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 14: 0x01A4 [0x1C] WAIT(30* ticks)
 15: 0x01A7 [0x21] END_EVENT
 16: 0x01A8 [0x00] END_REQSTACK()
```

### Event 561

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A9   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                             1E F0 FF FF 7F 6F 70           .....op
01B0: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  [..........tlk0.
01C0: 14 80 23 5E 69 64 6C 30  1C 00 80 21 00           ..#^idl0...!.   
```

#### Opcodes

```
  0: 0x01A9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x01AE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x01AF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x01B0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x01BF [0x1D] PRINT_EVENT_MESSAGE(message_id=7566*)
    → "You did well, <Player>. That should do it for now."
  5: 0x01C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01C3 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x01C8 [0x1C] WAIT(30* ticks)
  8: 0x01CB [0x21] END_EVENT
  9: 0x01CC [0x00] END_REQSTACK()
```

### Event 560

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01CD   |
| Data Size    | 50 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                         1E F0 FF               ...
01D0: FF 7F 6F 70 5B 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..op[..........t
01E0: 6C 6B 30 1D 17 80 23 1C  00 80 1D 18 80 23 1C 00  lk0...#......#..
01F0: 80 1D 19 80 23 5E 69 64  6C 30 1C 00 80 21 00     ....#^idl0...!. 
```

#### Opcodes

```
  0: 0x01CD [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x01D2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x01D3 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x01D4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x01E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7529*)
    → "I expect you to deliver a parcel before taking another. Everything in the proper order, please."
  5: 0x01E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01E7 [0x1C] WAIT(30* ticks)
  7: 0x01EA [0x1D] PRINT_EVENT_MESSAGE(message_id=7530*)
    → "Wait, you haven't lost the extremely important parcel I entrusted you with, have you?"
  8: 0x01ED [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x01EE [0x1C] WAIT(30* ticks)
 10: 0x01F1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7531*)
    → "If you've lost it, you'll have to pay for the loss. Give me 100 gil then and we'll be even."
 11: 0x01F4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x01F5 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 13: 0x01FA [0x1C] WAIT(30* ticks)
 14: 0x01FD [0x21] END_EVENT
 15: 0x01FE [0x00] END_REQSTACK()
```

### Event 537

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01FF   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                               1E                 .
0200: F0 FF FF 7F 6F 70 5B 00  80 F8 FF FF 7F F8 FF FF  ....op[.........
0210: 7F 74 6C 6B 30 1D 1A 80  23 5E 69 64 6C 30 1C 00  .tlk0...#^idl0..
0220: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x01FF [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0204 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0205 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0206 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0215 [0x1D] PRINT_EVENT_MESSAGE(message_id=7528*)
    → "Hmm...seems you've a fondness for hauling things already! Clear out your inventory before you take on mine."
  5: 0x0218 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0219 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x021E [0x1C] WAIT(30* ticks)
  8: 0x0221 [0x21] END_EVENT
  9: 0x0222 [0x00] END_REQSTACK()
```

### Event 558

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0223  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:          48 1B 80 23 21  00                          H..#!.       
```

#### Opcodes

```
  0: 0x0223 [0x48] [System] [7568*]:
    → "You cannot carry any more gil."
  1: 0x0226 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0227 [0x21] END_EVENT
  3: 0x0228 [0x00] END_REQSTACK()
```

### Event 608

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0229   |
| Data Size    | 41 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                             42 20 01 1E F0 FF FF           B .....
0230: 7F 6F 70 5B 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .op[..........tl
0240: 6B 30 1D 1C 80 23 5E 69  64 6C 30 1C 00 80 20 00  k0...#^idl0... .
0250: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0229 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x022A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x022C [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0231 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0232 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0233 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  6: 0x0242 [0x1D] PRINT_EVENT_MESSAGE(message_id=7532*)
    → "Fine. Very well, I'll have to go apologize to Regine over at the Magicmart in person. Take more care, next time."
  7: 0x0245 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0246 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x024B [0x1C] WAIT(30* ticks)
 10: 0x024E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0250 [0x21] END_EVENT
 12: 0x0251 [0x00] END_REQSTACK()
```

### Event 609

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0252   |
| Data Size    | 41 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:       42 20 01 1E F0 FF  FF 7F 6F 70 5B 00 80 F8    B ......op[...
0260: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 1D 80 23 5E  .......tlk0...#^
0270: 69 64 6C 30 1C 00 80 20  00 21 00                 idl0... .!.     
```

#### Opcodes

```
  0: 0x0252 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0253 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0255 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x025A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x025B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x025C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  6: 0x026B [0x1D] PRINT_EVENT_MESSAGE(message_id=7533*)
    → "Fine. Very well, I'll have to go apologize to Apstaule over at the auction house in person. Take more care, next time."
  7: 0x026E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x026F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x0274 [0x1C] WAIT(30* ticks)
 10: 0x0277 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0279 [0x21] END_EVENT
 12: 0x027A [0x00] END_REQSTACK()
```

### Event 610

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x027B   |
| Data Size    | 41 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                                   42 20 01 1E F0             B ...
0280: FF FF 7F 6F 70 5B 00 80  F8 FF FF 7F F8 FF FF 7F  ...op[..........
0290: 74 6C 6B 30 1D 1E 80 23  5E 69 64 6C 30 1C 00 80  tlk0...#^idl0...
02A0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x027B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x027C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x027E [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0283 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0284 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0285 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  6: 0x0294 [0x1D] PRINT_EVENT_MESSAGE(message_id=7534*)
    → "Fine. Very well, I'll have to go apologize to Thierride over at the tavern in person. Take more care, next time."
  7: 0x0297 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0298 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x029D [0x1C] WAIT(30* ticks)
 10: 0x02A0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x02A2 [0x21] END_EVENT
 12: 0x02A3 [0x00] END_REQSTACK()
```
