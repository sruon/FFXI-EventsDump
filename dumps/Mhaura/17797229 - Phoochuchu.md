# 17797229 - Phoochuchu

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 476 bytes        |
| Total Events     | 5                |
| References Count | 17               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [300](#event-300)     | 0x0001       |      6 |              4 |
| [301](#event-301)     | 0x0007       |    108 |             18 |
| [302](#event-302)     | 0x0073       |     56 |             10 |
| [303](#event-303)     | 0x00AB       |    199 |             32 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D53      |        7507 |
|       1 | 0x1D54      |        7508 |
|       2 | 0x0031      |          49 |
|       3 | 0x1D55      |        7509 |
|       4 | 0x1D56      |        7510 |
|       5 | 0x1D57      |        7511 |
|       6 | 0x1D5A      |        7514 |
|       7 | 0x1D5B      |        7515 |
|       8 | 0x1D58      |        7512 |
|       9 | 0x1D59      |        7513 |
|      10 | 0x0000      |           0 |
|      11 | 0x000A      |          10 |
|      12 | 0x0014      |          20 |
|      13 | 0x001E      |          30 |
|      14 | 0x0028      |          40 |
|      15 | 0x0032      |          50 |
|      16 | 0x003C      |          60 |

## String References

- **7507**: I got no business with a flea like you. Get outta my face before I decide to messy-wess you up.
- **7508**: You're <Player>, right? Ha ha ha! I knew it! Just like Gilgamesh described. Lemme tell you what I gotty-wot so far.
- **7509**: The creepy-weep that stole our helmet isn't from any large syndicate. He isn't even very famous among other pirates. He's just a simple thiefy-weef trying to pull off a big job for a big profit.
- **7510**: According to the owner of that inn, he traveled numerous timey-wimes between here and Selbina, and would sometimes talk about his plans after a few too many drinky-winks. But then one day, he just disappeared.
- **7511**: After looking at Norg's nautical loggy-wogs, I learned that the time he disappeared matches the time he must have entered our headquarters. But where he went from therey-where, I don't know.
- **7512**: Wa-wa-wait! There's something else.
- **7513**: One of our men in Bastok is piecing together all the information we've gathered so far. He's hiding out in a run-down old housey-wouse in the Mines District (J-6). He should be able to give you something juicy-wuicy.
- **7514**: I thought that this might have been the work of some large groupy-woop, but when I heard that it was just one guy...boy, was I surprisey-wised!
- **7515**: I can understand wanting to makey-wake it big overnight, but he should have thought a little bitty-wit longer before deciding to take us on!

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

### Event 300

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 21 00                               ...#!.         
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7507*)
    → "I got no business with a flea like you. Get outta my face before I decide to messy-wess you up."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

### Event 301

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0007    |
| Data Size    | 108 bytes |
| Instructions | 18        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      42  1A E4 00 1D 01 80 23 66         B......#f
0010: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 03  ..........tlk0..
0020: 80 23 1D 04 80 23 66 02  80 F8 FF FF 7F F8 FF FF  .#...#f.........
0030: 7F 74 6C 6B 31 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  .tlk1S........tl
0040: 6B 31 66 02 80 F8 FF FF  7F F8 FF FF 7F 74 68 6B  k1f..........thk
0050: 31 1D 05 80 23 66 02 80  F8 FF FF 7F F8 FF FF 7F  1...#f..........
0060: 74 68 6B 32 53 F8 FF FF  7F F8 FF FF 7F 74 68 6B  thk2S........thk
0070: 32 21 00                                          2!.             
```

#### Opcodes

```
  0: 0x0007 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0008 [0x1A] CALL_SUBROUTINE(address=0x00E4)
  2: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=7508*)
    → "You're <Player>, right? Ha ha ha! I knew it! Just like Gilgamesh described. Lemme tell you what I gotty-wot so far."
  3: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  5: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7509*)
    → "The creepy-weep that stole our helmet isn't from any large syndicate. He isn't even very famous among other pirates. He's just a simple thiefy-weef trying to pull off a big job for a big profit."
  6: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7510*)
    → "According to the owner of that inn, he traveled numerous timey-wimes between here and Selbina, and would sometimes talk about his plans after a few too many drinky-winks. But then one day, he just disappeared."
  8: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0026 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
 10: 0x0035 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 11: 0x0042 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=49*
 12: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=7511*)
    → "After looking at Norg's nautical loggy-wogs, I learned that the time he disappeared matches the time he must have entered our headquarters. But where he went from therey-where, I don't know."
 13: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0055 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=49*
 15: 0x0064 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 16: 0x0071 [0x21] END_EVENT
 17: 0x0072 [0x00] END_REQSTACK()
```

### Event 302

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          1A E4 00 66 02  80 F8 FF FF 7F F8 FF FF     ...f.........
0080: 7F 74 68 6B 31 1D 06 80  23 66 02 80 F8 FF FF 7F  .thk1...#f......
0090: F8 FF FF 7F 74 68 6B 32  53 F8 FF FF 7F F8 FF FF  ....thk2S.......
00A0: 7F 74 68 6B 32 1D 07 80  23 21 00                 .thk2...#!.     
```

#### Opcodes

```
  0: 0x0073 [0x1A] CALL_SUBROUTINE(address=0x00E4)
  1: 0x0076 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=49*
  2: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=7514*)
    → "I thought that this might have been the work of some large groupy-woop, but when I heard that it was just one guy...boy, was I surprisey-wised!"
  3: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0089 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=49*
  5: 0x0098 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  6: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7515*)
    → "I can understand wanting to makey-wake it big overnight, but he should have thought a little bitty-wit longer before deciding to take us on!"
  7: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00A9 [0x21] END_EVENT
  9: 0x00AA [0x00] END_REQSTACK()
```

### Event 303

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00AB    |
| Data Size    | 199 bytes |
| Instructions | 16        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   42 1A E4 00 66             B...f
00B0: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 08  ..........tlk0..
00C0: 80 23 1D 09 80 23 66 02  80 F8 FF FF 7F F8 FF FF  .#...#f.........
00D0: 7F 74 6C 6B 31 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  .tlk1S........tl
00E0: 6B 31 21 00 86 00 F8 FF  FF 7F 1E F0 FF FF 7F 6F  k1!............o
00F0: 70 1B 66 0A 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  p.f..........tlk
0100: 30 1B 66 0A 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  0.f..........tlk
0110: 31 1B 66 0B 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  1.f..........tlk
0120: 30 1B 66 0C 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  0.f..........tlk
0130: 30 1B 66 0D 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  0.f..........tlk
0140: 30 1B 66 0E 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  0.f..........tlk
0150: 30 1B 66 0F 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  0.f..........tlk
0160: 30 1B 66 10 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  0.f..........tlk
0170: 30 1B                                             0.              
```

#### Opcodes

```
  0: 0x00AB [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00AC [0x1A] CALL_SUBROUTINE(address=0x00E4)
  2: 0x00AF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  3: 0x00BE [0x1D] PRINT_EVENT_MESSAGE(message_id=7512*)
    → "Wa-wa-wait! There's something else."
  4: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7513*)
    → "One of our men in Bastok is piecing together all the information we've gathered so far. He's hiding out in a run-down old housey-wouse in the Mines District (J-6). He should be able to give you something juicy-wuicy."
  6: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00C6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  8: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  9: 0x00E2 [0x21] END_EVENT
 10: 0x00E3 [0x00] END_REQSTACK()

SUBROUTINE_00E4:
 11: 0x00E4 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
 12: 0x00EA [0x1E] EventEntity looks at LocalPlayer and starts talking
 13: 0x00EF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 14: 0x00F0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 15: 0x00F1 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00F2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
     0x0101 [0x1B] RETURN
     0x0102 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
     0x0111 [0x1B] RETURN
     0x0112 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
     0x0121 [0x1B] RETURN
     0x0122 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
     0x0131 [0x1B] RETURN
     0x0132 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
     0x0141 [0x1B] RETURN
     0x0142 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
     0x0151 [0x1B] RETURN
     0x0152 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
     0x0161 [0x1B] RETURN
     0x0162 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
     0x0171 [0x1B] RETURN
```
