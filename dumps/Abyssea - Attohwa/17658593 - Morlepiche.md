# 17658593 - Morlepiche

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 328 bytes                   |
| Total Events     | 4                           |
| References Count | 14                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [308](#event-308)     | 0x0001       |     43 |              9 |
| [309](#event-309)     | 0x002C       |    134 |             28 |
| [310](#event-310)     | 0x00B2       |     62 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x1F67      |        8039 |
|       2 | 0x1F68      |        8040 |
|       3 | 0x1F69      |        8041 |
|       4 | 0x0003      |           3 |
|       5 | 0x1F6B      |        8043 |
|       6 | 0x1F6A      |        8042 |
|       7 | 0x0000      |           0 |
|       8 | 0x1F6C      |        8044 |
|       9 | 0x1F6D      |        8045 |
|      10 | 0x1F6E      |        8046 |
|      11 | 0x00C9      |         201 |
|      12 | 0x1F6F      |        8047 |
|      13 | 0x1F70      |        8048 |

## String References

- **8039**: ...Five, six. Curses! Is this all that remains!? If those supplies don't arrive soon, we're as good as done for!
- **8040**: What is this? Do my eyes deceive me!?
- **8041**: Our supplies! I thought for sure we had lost them for good. You have no idea what this means to us, friend.
- **8042**: Still, this will not sustain us forever. If you encounter any more of the waylaid supplies, promise that you will deliver them here to me.
- **8043**: ...Yes, this should be all of them. Excellent! This should keep this outpost in good trim for the foreseeable future.
- **8044**: What's that you say? You've heard we were looking for a few good [men/women]?
- **8045**: Ahaha! For a labyrinth of crags and craters, word certainly travels fast in this chasm. Of course, we'd be honored to welcome you to our ranks.
- **8046**: Currently, our most pressing need is in maintaining our defenses against the hordes. Speak with the resistance sapper over there to learn how you can do your part.
- **8047**: I, for one, have no intention of laying down my life in this barren wasteland. No, there are too many people depending on me, too many things I still must accomplish...
- **8048**: Surely it is the same for you, friend? That is why we must band together, and drive back the fiends at all costs!

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

### Event 308

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 68 6B 31 1D  01 80 23 66 00 80 F8 FF  ...thk1...#f....
0020: FF 7F F8 FF FF 7F 74 68  6B 32 21 00              ......thk2!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8039*)
    → "...Five, six. Curses! Is this all that remains!? If those supplies don't arrive soon, we're as good as done for!"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  7: 0x002A [0x21] END_EVENT
  8: 0x002B [0x00] END_REQSTACK()
```

### Event 309

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x002C    |
| Data Size    | 134 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      42 1E F0 FF              B...
0030: FF 7F 6F 70 1D 02 80 23  1D 03 80 23 66 00 80 F8  ..op...#...#f...
0040: FF FF 7F F8 FF FF 7F 74  77 61 30 02 03 10 04 80  .......twa0.....
0050: 04 5A 00 1D 05 80 23 01  5E 00 1D 06 80 23 66 00  .Z....#.^....#f.
0060: 80 F8 FF FF 7F F8 FF FF  7F 74 77 61 31 02 04 10  .........twa1...
0070: 07 80 00 B0 00 1D 08 80  23 66 00 80 F8 FF FF 7F  ........#f......
0080: F8 FF FF 7F 74 77 61 30  1D 09 80 23 1D 0A 80 23  ....twa0...#...#
0090: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 77 61 31 45  f..........twa1E
00A0: 0B 80 F0 FF FF 7F F0 FF  FF 7F 71 73 74 63 07 80  ..........qstc..
00B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x002C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0033 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=8040*)
    → "What is this? Do my eyes deceive me!?"
  5: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=8041*)
    → "Our supplies! I thought for sure we had lost them for good. You have no idea what this means to us, friend."
  7: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x003C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [EventEntity, EventEntity], work=29*
  9: 0x004B [0x02] IF !(Work_Zone[3] < 3*) GOTO 0x005A
 10: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=8043*)
    → "...Yes, this should be all of them. Excellent! This should keep this outpost in good trim for the foreseeable future."
 11: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0057 [0x01] GOTO 0x005E
 13: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=8042*)
    → "Still, this will not sustain us forever. If you encounter any more of the waylaid supplies, promise that you will deliver them here to me."
 14: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_005E:
 15: 0x005E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa1" with entities [EventEntity, EventEntity], work=29*
 16: 0x006D [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x00B0
 17: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=8044*)
    → "What's that you say? You've heard we were looking for a few good [men/women]?"
 18: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0079 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [EventEntity, EventEntity], work=29*
 20: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=8045*)
    → "Ahaha! For a labyrinth of crags and craters, word certainly travels fast in this chasm. Of course, we'd be honored to welcome you to our ranks."
 21: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=8046*)
    → "Currently, our most pressing need is in maintaining our defenses against the hordes. Speak with the resistance sapper over there to learn how you can do your part."
 23: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0090 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa1" with entities [EventEntity, EventEntity], work=29*
 25: 0x009F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 26: 0x00B0 [0x21] END_EVENT
 27: 0x00B1 [0x00] END_REQSTACK()
```

### Event 310

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 62 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F    .....opf......
00C0: F8 FF FF 7F 74 77 61 30  02 03 10 04 80 04 DB 00  ....twa0........
00D0: 1D 0C 80 23 1D 0D 80 23  01 DF 00 1D 06 80 23 66  ...#...#......#f
00E0: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 77 61 31 21 00  ..........twa1!.
```

#### Opcodes

```
  0: 0x00B2 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B8 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00B9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [EventEntity, EventEntity], work=29*
  4: 0x00C8 [0x02] IF !(Work_Zone[3] < 3*) GOTO 0x00DB
  5: 0x00D0 [0x1D] PRINT_EVENT_MESSAGE(message_id=8047*)
    → "I, for one, have no intention of laying down my life in this barren wasteland. No, there are too many people depending on me, too many things I still must accomplish..."
  6: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00D4 [0x1D] PRINT_EVENT_MESSAGE(message_id=8048*)
    → "Surely it is the same for you, friend? That is why we must band together, and drive back the fiends at all costs!"
  8: 0x00D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00D8 [0x01] GOTO 0x00DF
 10: 0x00DB [0x1D] PRINT_EVENT_MESSAGE(message_id=8042*)
    → "Still, this will not sustain us forever. If you encounter any more of the waylaid supplies, promise that you will deliver them here to me."
 11: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00DF:
 12: 0x00DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa1" with entities [EventEntity, EventEntity], work=29*
 13: 0x00EE [0x21] END_EVENT
 14: 0x00EF [0x00] END_REQSTACK()
```
