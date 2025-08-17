# 17568181 - Rojaireaut

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ordelle's Caves (ID: 193) |
| Block Size       | 788 bytes                 |
| Total Events     | 6                         |
| References Count | 27                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [50](#event-50)       | 0x0001       |     46 |             11 |
| [51](#event-51)       | 0x002F       |    205 |             46 |
| [52](#event-52)       | 0x00FC       |    139 |             24 |
| [53](#event-53)       | 0x0187       |    195 |             35 |
| [54](#event-54)       | 0x024A       |     51 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x1D14      |        7444 |
|       2 | 0x1D0C      |        7436 |
|       3 | 0x1D0D      |        7437 |
|       4 | 0x1D0E      |        7438 |
|       5 | 0x1D0F      |        7439 |
|       6 | 0x1D10      |        7440 |
|       7 | 0x1D11      |        7441 |
|       8 | 0x1D12      |        7442 |
|       9 | 0x0001      |           1 |
|      10 | 0x0000      |           0 |
|      11 | 0x1D15      |        7445 |
|      12 | 0x00C8      |         200 |
|      13 | 0x003C      |          60 |
|      14 | 0x01F3      |         499 |
|      15 | 0x005A      |          90 |
|      16 | 0x0015      |          21 |
|      17 | 0x1D13      |        7443 |
|      18 | 0x001E      |          30 |
|      19 | 0x1D18      |        7448 |
|      20 | 0x1D19      |        7449 |
|      21 | 0x40000000  |  1073741824 |
|      22 | 0x1D16      |        7446 |
|      23 | 0x000E      |          14 |
|      24 | 0x0002      |           2 |
|      25 | 0x01D8      |         472 |
|      26 | 0x1D17      |        7447 |

## String References

- **7436**: Well, it's about time you showed up! You're here for the V.E.R.M.I.N. extermination operation, yes?
- **7437**: I'll get straight to the point. We want you to find and defeat the fiend that has been wreaking havoc down here, then take the evidence of its extermination to Norejaie in San d'Oria.
- **7438**: In order to lure the creature into the open, we have prepared this special ointment that must be applied to your skin.
- **7439**: Lest you think me unhelpful, I will share with you what I know: sightings have been reported from the area around G-9.
- **7440**: The effect of the ointment lasts for about a day. If it wears off early, or you want the effect removed, just come back here and talk to me.
- **7441**: There may be some...unexpected side effects. But we won't let a little discomfort bother us now, will we?
- **7442**: Apply the ointment? [Slap it on./Did you say, "side effects"...?]
- **7443**: Come now, you call yourself an adventurer?
- **7444**: I have no time for your idle chatter.
- **7445**: Now, close your eyes for a moment. This won't hurt a bit...
- **7446**: You wish the effect removed? Well then, close your eyes. This will be relatively painless...
- **7447**: What's that you have there? 6 from the fiend? That should be proof enough for Norejaie. Take it back to her in San d'Oria.
- **7448**: Hmmm? Perhaps you forgot something?
- **7449**: What do you desire? [Nothing./To have the ointment removed./To reconfirm where I'm going.]

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

### Event 50

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 46 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F   B.....opf......
0010: F8 FF FF 7F 74 6C 6B 30  1D 01 80 23 66 00 80 F8  ....tlk0...#f...
0020: FF FF 7F F8 FF FF 7F 74  6C 6B 31 20 00 21 00     .......tlk1 .!. 
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  5: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7444*)
    → "I have no time for your idle chatter."
  6: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  8: 0x002B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x002D [0x21] END_EVENT
 10: 0x002E [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x002F    |
| Data Size    | 205 bytes |
| Instructions | 46        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               1E                 .
0030: F0 FF FF 7F 6F 70 66 00  80 F8 FF FF 7F F8 FF FF  ....opf.........
0040: 7F 74 6C 6B 30 1D 02 80  23 1D 03 80 23 1D 04 80  .tlk0...#...#...
0050: 23 1D 05 80 23 1D 06 80  23 1D 07 80 23 24 08 80  #...#...#...#$..
0060: 09 80 0A 80 25 02 00 10  0A 80 00 C0 00 42 43 00  ....%........BC.
0070: 43 01 1D 0B 80 23 03 01  10 09 80 66 00 80 F8 FF  C....#.....f....
0080: FF 7F F8 FF FF 7F 74 6C  6B 31 45 0C 80 F0 FF FF  ......tlk1E.....
0090: 7F F0 FF FF 7F 66 64 6F  31 0A 80 1C 0D 80 73 0E  .....fdo1.....s.
00A0: 80 B5 11 0C 01 F0 FF FF  7F 1C 0F 80 45 0C 80 F0  ............E...
00B0: FF FF 7F F0 FF FF 7F 66  64 69 31 0A 80 01 F8 00  .......fdi1.....
00C0: 02 00 10 09 80 00 F8 00  42 43 00 43 01 66 10 80  ........BC.C.f..
00D0: F8 FF FF 7F F8 FF FF 7F  64 69 73 30 1D 11 80 23  ........dis0...#
00E0: 53 F8 FF FF 7F F8 FF FF  7F 64 69 73 30 5E 69 64  S........dis0^id
00F0: 6C 30 1C 12 80 01 F8 00  20 00 21 00              l0...... .!.    
```

#### Opcodes

```
  0: 0x002F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0035 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0036 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  4: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=7436*)
    → "Well, it's about time you showed up! You're here for the V.E.R.M.I.N. extermination operation, yes?"
  5: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=7437*)
    → "I'll get straight to the point. We want you to find and defeat the fiend that has been wreaking havoc down here, then take the evidence of its extermination to Norejaie in San d'Oria."
  7: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7438*)
    → "In order to lure the creature into the open, we have prepared this special ointment that must be applied to your skin."
  9: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=7439*)
    → "Lest you think me unhelpful, I will share with you what I know: sightings have been reported from the area around G-9."
 11: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=7440*)
    → "The effect of the ointment lasts for about a day. If it wears off early, or you want the effect removed, just come back here and talk to me."
 13: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=7441*)
    → "There may be some...unexpected side effects. But we won't let a little discomfort bother us now, will we?"
 15: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x005D [0x24] CREATE_DIALOG(message_id=7442*, default_option=1*, option_flags=0*)
    → "Apply the ointment? [Slap it on./Did you say, "side effects"...?]"
 17: 0x0064 [0x25] WAIT_DIALOG_SELECT()
 18: 0x0065 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C0
 19: 0x006D [0x42] SET_CLI_EVENT_CANCEL_DATA()
 20: 0x006E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 21: 0x0070 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 22: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=7445*)
    → "Now, close your eyes for a moment. This won't hurt a bit..."
 23: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0076 [0x03] Work_Zone[1] = 1*
 25: 0x007B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
 26: 0x008A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x009B [0x1C] WAIT(60* ticks)
 28: 0x009E [0x73] Rojaireaut (ID: 17568181/0x010C11B5) casts magic 499* on LocalPlayer
 29: 0x00A9 [0x1C] WAIT(90* ticks)
 30: 0x00AC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x00BD [0x01] GOTO 0x00F8
 32: 0x00C0 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00F8
 33: 0x00C8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 34: 0x00C9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x00CB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x00CD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=21*
 37: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=7443*)
    → "Come now, you call yourself an adventurer?"
 38: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x00E0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
 40: 0x00ED [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 41: 0x00F2 [0x1C] WAIT(30* ticks)
 42: 0x00F5 [0x01] GOTO 0x00F8

SUBROUTINE_00F8:
 43: 0x00F8 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 44: 0x00FA [0x21] END_EVENT
 45: 0x00FB [0x00] END_REQSTACK()
```

### Event 52

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00FC    |
| Data Size    | 139 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      43 00 43 01              C.C.
0100: 42 1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8  B.....opf.......
0110: FF FF 7F 74 6C 6B 30 1D  0B 80 23 66 00 80 F8 FF  ...tlk0...#f....
0120: FF 7F F8 FF FF 7F 74 6C  6B 31 45 0C 80 F0 FF FF  ......tlk1E.....
0130: 7F F0 FF FF 7F 66 64 6F  31 0A 80 1C 0D 80 73 0E  .....fdo1.....s.
0140: 80 B5 11 0C 01 F0 FF FF  7F 1C 0F 80 45 0C 80 F0  ............E...
0150: FF FF 7F F0 FF FF 7F 66  64 69 31 0A 80 66 00 80  .......fdi1..f..
0160: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 05 80 23  ........tlk0...#
0170: 1D 06 80 23 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
0180: 6C 6B 31 20 00 21 00                              lk1 .!.         
```

#### Opcodes

```
  0: 0x00FC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  1: 0x00FE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  2: 0x0100 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0101 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0106 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0107 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0108 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  7: 0x0117 [0x1D] PRINT_EVENT_MESSAGE(message_id=7445*)
    → "Now, close your eyes for a moment. This won't hurt a bit..."
  8: 0x011A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x011B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
 10: 0x012A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x013B [0x1C] WAIT(60* ticks)
 12: 0x013E [0x73] Rojaireaut (ID: 17568181/0x010C11B5) casts magic 499* on LocalPlayer
 13: 0x0149 [0x1C] WAIT(90* ticks)
 14: 0x014C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x015D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
 16: 0x016C [0x1D] PRINT_EVENT_MESSAGE(message_id=7439*)
    → "Lest you think me unhelpful, I will share with you what I know: sightings have been reported from the area around G-9."
 17: 0x016F [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0170 [0x1D] PRINT_EVENT_MESSAGE(message_id=7440*)
    → "The effect of the ointment lasts for about a day. If it wears off early, or you want the effect removed, just come back here and talk to me."
 19: 0x0173 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0174 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
 21: 0x0183 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 22: 0x0185 [0x21] END_EVENT
 23: 0x0186 [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0187    |
| Data Size    | 195 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                      43  00 43 01 42 1E F0 FF FF         C.C.B....
0190: 7F 6F 70 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
01A0: 6B 30 1D 13 80 23 24 14  80 0A 80 0A 80 25 02 00  k0...#$......%..
01B0: 10 0A 80 00 CD 01 66 00  80 F8 FF FF 7F F8 FF FF  ......f.........
01C0: 7F 74 6C 6B 31 03 01 10  15 80 01 46 02 02 00 10  .tlk1......F....
01D0: 09 80 00 23 02 1D 16 80  23 66 00 80 F8 FF FF 7F  ...#....#f......
01E0: F8 FF FF 7F 74 6C 6B 31  45 0C 80 F0 FF FF 7F F0  ....tlk1E.......
01F0: FF FF 7F 66 64 6F 31 0A  80 1C 0D 80 73 17 80 B5  ...fdo1.....s...
0200: 11 0C 01 F0 FF FF 7F 1C  0F 80 45 0C 80 F0 FF FF  ..........E.....
0210: 7F F0 FF FF 7F 66 64 69  31 0A 80 03 01 10 0A 80  .....fdi1.......
0220: 01 46 02 02 00 10 18 80  00 46 02 1D 05 80 23 66  .F.......F....#f
0230: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 03 01  ..........tlk1..
0240: 10 15 80 01 46 02 20 00  21 00                    ....F. .!.      
```

#### Opcodes

```
  0: 0x0187 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  1: 0x0189 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  2: 0x018B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x018C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0191 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0192 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0193 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  7: 0x01A2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7448*)
    → "Hmmm? Perhaps you forgot something?"
  8: 0x01A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x01A6 [0x24] CREATE_DIALOG(message_id=7449*, default_option=0*, option_flags=0*)
    → "What do you desire? [Nothing./To have the ointment removed./To reconfirm where I'm going.]"
 10: 0x01AD [0x25] WAIT_DIALOG_SELECT()
 11: 0x01AE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01CD
 12: 0x01B6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
 13: 0x01C5 [0x03] Work_Zone[1] = 1073741824*
 14: 0x01CA [0x01] GOTO 0x0246
 15: 0x01CD [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0223
 16: 0x01D5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7446*)
    → "You wish the effect removed? Well then, close your eyes. This will be relatively painless..."
 17: 0x01D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x01D9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
 19: 0x01E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x01F9 [0x1C] WAIT(60* ticks)
 21: 0x01FC [0x73] Rojaireaut (ID: 17568181/0x010C11B5) casts magic 14* on LocalPlayer
 22: 0x0207 [0x1C] WAIT(90* ticks)
 23: 0x020A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x021B [0x03] Work_Zone[1] = 0*
 25: 0x0220 [0x01] GOTO 0x0246
 26: 0x0223 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0246
 27: 0x022B [0x1D] PRINT_EVENT_MESSAGE(message_id=7439*)
    → "Lest you think me unhelpful, I will share with you what I know: sightings have been reported from the area around G-9."
 28: 0x022E [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x022F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
 30: 0x023E [0x03] Work_Zone[1] = 1073741824*
 31: 0x0243 [0x01] GOTO 0x0246

SUBROUTINE_0246:
 32: 0x0246 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x0248 [0x21] END_EVENT
 34: 0x0249 [0x00] END_REQSTACK()
```

### Event 54

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024A   |
| Data Size    | 51 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                42 1E F0 FF FF 7F            B.....
0250: 6F 70 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  opf..........tlk
0260: 30 03 02 10 19 80 1D 1A  80 23 66 00 80 F8 FF FF  0........#f.....
0270: 7F F8 FF FF 7F 74 6C 6B  31 20 00 21 00           .....tlk1 .!.   
```

#### Opcodes

```
  0: 0x024A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x024B [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0250 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0251 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0252 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  5: 0x0261 [0x03] Work_Zone[2] = 472*
  6: 0x0266 [0x1D] PRINT_EVENT_MESSAGE(message_id=7447*)
    → "What's that you have there? 6 from the fiend? That should be proof enough for Norejaie. Take it back to her in San d'Oria."
  7: 0x0269 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x026A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  9: 0x0279 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x027B [0x21] END_EVENT
 11: 0x027C [0x00] END_REQSTACK()
```
