# 17588760 - Ahko Mhalijikhari

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Maze of Shakhrami (ID: 198) |
| Block Size       | 788 bytes                   |
| Total Events     | 6                           |
| References Count | 27                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [61](#event-61)       | 0x0001       |     46 |             11 |
| [62](#event-62)       | 0x002F       |    205 |             46 |
| [63](#event-63)       | 0x00FC       |    139 |             24 |
| [64](#event-64)       | 0x0187       |    195 |             35 |
| [65](#event-65)       | 0x024A       |     51 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003B      |          59 |
|       1 | 0x1C90      |        7312 |
|       2 | 0x1C88      |        7304 |
|       3 | 0x1C89      |        7305 |
|       4 | 0x1C8A      |        7306 |
|       5 | 0x1C8B      |        7307 |
|       6 | 0x1C8C      |        7308 |
|       7 | 0x1C8D      |        7309 |
|       8 | 0x1C8E      |        7310 |
|       9 | 0x0001      |           1 |
|      10 | 0x0000      |           0 |
|      11 | 0x1C91      |        7313 |
|      12 | 0x00C8      |         200 |
|      13 | 0x003C      |          60 |
|      14 | 0x01F3      |         499 |
|      15 | 0x005A      |          90 |
|      16 | 0x0034      |          52 |
|      17 | 0x1C8F      |        7311 |
|      18 | 0x001E      |          30 |
|      19 | 0x1C94      |        7316 |
|      20 | 0x1C95      |        7317 |
|      21 | 0x40000000  |  1073741824 |
|      22 | 0x1C92      |        7314 |
|      23 | 0x000E      |          14 |
|      24 | 0x0002      |           2 |
|      25 | 0x01DA      |         474 |
|      26 | 0x1C93      |        7315 |

## String References

- **7304**: Ah, you're here at last! Rrready and rrraring to perform your V.E.R.M.I.N. assignment?
- **7305**: Okay, here's the deal. Find and defeat the creatures that've been rrrunning amok down here, and then take the proof of their demise to Lumomo in Windurst.
- **7306**: We've prrrepared this special ointment to rub on your skin that will lure the creatures out of hiding.
- **7307**: Those buggerrrs have been spotted mostly around I-10. Shouldn't be too hard for you to get to.
- **7308**: The effect of the ointment lasts for about a day. If it wears off, or you want the effect rrremoved, just come back here and talk with me.
- **7309**: The ointment may have some interrresting...side effects. Rrready, tiger?
- **7310**: Apply the ointment? [Slap it on./Not rrright now...]
- **7311**: Oh? Lost your nerrrve? Talk to me if you change your mind.
- **7312**: Move along, adventurrrer.
- **7313**: Rrright, here we go! Close your eyes...
- **7314**: You want the effect rrremoved? Okay, just close your eyes...
- **7315**: How...lovely. A chunk of $3. Well, take it back to Lumomo. I'm sure she'll apprrreciate your efforts.
- **7316**: What do you want?
- **7317**: What do you desire? [Nothing./To have the ointment removed./To reconfirm where I'm going.]

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

### Event 61

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
  4: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  5: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7312*)
    → "Move along, adventurrrer."
  6: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  8: 0x002B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x002D [0x21] END_EVENT
 10: 0x002E [0x00] END_REQSTACK()
```

### Event 62

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
00A0: 80 18 62 0C 01 F0 FF FF  7F 1C 0F 80 45 0C 80 F0  ..b.........E...
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
  3: 0x0036 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  4: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=7304*)
    → "Ah, you're here at last! Rrready and rrraring to perform your V.E.R.M.I.N. assignment?"
  5: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=7305*)
    → "Okay, here's the deal. Find and defeat the creatures that've been rrrunning amok down here, and then take the proof of their demise to Lumomo in Windurst."
  7: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7306*)
    → "We've prrrepared this special ointment to rub on your skin that will lure the creatures out of hiding."
  9: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=7307*)
    → "Those buggerrrs have been spotted mostly around I-10. Shouldn't be too hard for you to get to."
 11: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=7308*)
    → "The effect of the ointment lasts for about a day. If it wears off, or you want the effect rrremoved, just come back here and talk with me."
 13: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=7309*)
    → "The ointment may have some interrresting...side effects. Rrready, tiger?"
 15: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x005D [0x24] CREATE_DIALOG(message_id=7310*, default_option=1*, option_flags=0*)
    → "Apply the ointment? [Slap it on./Not rrright now...]"
 17: 0x0064 [0x25] WAIT_DIALOG_SELECT()
 18: 0x0065 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C0
 19: 0x006D [0x42] SET_CLI_EVENT_CANCEL_DATA()
 20: 0x006E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 21: 0x0070 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 22: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=7313*)
    → "Rrright, here we go! Close your eyes..."
 23: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0076 [0x03] Work_Zone[1] = 1*
 25: 0x007B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 26: 0x008A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x009B [0x1C] WAIT(60* ticks)
 28: 0x009E [0x73] Ahko Mhalijikhari (ID: 17588760/0x010C6218) casts magic 499* on LocalPlayer
 29: 0x00A9 [0x1C] WAIT(90* ticks)
 30: 0x00AC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x00BD [0x01] GOTO 0x00F8
 32: 0x00C0 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00F8
 33: 0x00C8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 34: 0x00C9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x00CB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x00CD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=52*
 37: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=7311*)
    → "Oh? Lost your nerrrve? Talk to me if you change your mind."
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

### Event 63

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
0140: 80 18 62 0C 01 F0 FF FF  7F 1C 0F 80 45 0C 80 F0  ..b.........E...
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
  6: 0x0108 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  7: 0x0117 [0x1D] PRINT_EVENT_MESSAGE(message_id=7313*)
    → "Rrright, here we go! Close your eyes..."
  8: 0x011A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x011B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 10: 0x012A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x013B [0x1C] WAIT(60* ticks)
 12: 0x013E [0x73] Ahko Mhalijikhari (ID: 17588760/0x010C6218) casts magic 499* on LocalPlayer
 13: 0x0149 [0x1C] WAIT(90* ticks)
 14: 0x014C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x015D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
 16: 0x016C [0x1D] PRINT_EVENT_MESSAGE(message_id=7307*)
    → "Those buggerrrs have been spotted mostly around I-10. Shouldn't be too hard for you to get to."
 17: 0x016F [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0170 [0x1D] PRINT_EVENT_MESSAGE(message_id=7308*)
    → "The effect of the ointment lasts for about a day. If it wears off, or you want the effect rrremoved, just come back here and talk with me."
 19: 0x0173 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0174 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 21: 0x0183 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 22: 0x0185 [0x21] END_EVENT
 23: 0x0186 [0x00] END_REQSTACK()
```

### Event 64

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
01F0: FF FF 7F 66 64 6F 31 0A  80 1C 0D 80 73 17 80 18  ...fdo1.....s...
0200: 62 0C 01 F0 FF FF 7F 1C  0F 80 45 0C 80 F0 FF FF  b.........E.....
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
  6: 0x0193 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  7: 0x01A2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7316*)
    → "What do you want?"
  8: 0x01A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x01A6 [0x24] CREATE_DIALOG(message_id=7317*, default_option=0*, option_flags=0*)
    → "What do you desire? [Nothing./To have the ointment removed./To reconfirm where I'm going.]"
 10: 0x01AD [0x25] WAIT_DIALOG_SELECT()
 11: 0x01AE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01CD
 12: 0x01B6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 13: 0x01C5 [0x03] Work_Zone[1] = 1073741824*
 14: 0x01CA [0x01] GOTO 0x0246
 15: 0x01CD [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0223
 16: 0x01D5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7314*)
    → "You want the effect rrremoved? Okay, just close your eyes..."
 17: 0x01D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x01D9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 19: 0x01E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x01F9 [0x1C] WAIT(60* ticks)
 21: 0x01FC [0x73] Ahko Mhalijikhari (ID: 17588760/0x010C6218) casts magic 14* on LocalPlayer
 22: 0x0207 [0x1C] WAIT(90* ticks)
 23: 0x020A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x021B [0x03] Work_Zone[1] = 0*
 25: 0x0220 [0x01] GOTO 0x0246
 26: 0x0223 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0246
 27: 0x022B [0x1D] PRINT_EVENT_MESSAGE(message_id=7307*)
    → "Those buggerrrs have been spotted mostly around I-10. Shouldn't be too hard for you to get to."
 28: 0x022E [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x022F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 30: 0x023E [0x03] Work_Zone[1] = 1073741824*
 31: 0x0243 [0x01] GOTO 0x0246

SUBROUTINE_0246:
 32: 0x0246 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x0248 [0x21] END_EVENT
 34: 0x0249 [0x00] END_REQSTACK()
```

### Event 65

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
  4: 0x0252 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  5: 0x0261 [0x03] Work_Zone[2] = 474*
  6: 0x0266 [0x1D] PRINT_EVENT_MESSAGE(message_id=7315*)
    → "How...lovely. A chunk of $3. Well, take it back to Lumomo. I'm sure she'll apprrreciate your efforts."
  7: 0x0269 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x026A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  9: 0x0279 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x027B [0x21] END_EVENT
 11: 0x027C [0x00] END_REQSTACK()
```
