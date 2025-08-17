# 17670769 - Maunadolace

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 396 bytes                  |
| Total Events     | 3                          |
| References Count | 17                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |    201 |             47 |
| [334](#event-334)     | 0x00C9       |     20 |             10 |
| [335](#event-335)     | 0x00DD       |     76 |             23 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FE      |         254 |
|       1 | 0x0001      |           1 |
|       2 | 0x203B      |        8251 |
|       3 | 0x0000      |           0 |
|       4 | 0x0007      |           7 |
|       5 | 0x203C      |        8252 |
|       6 | 0x0008      |           8 |
|       7 | 0x203D      |        8253 |
|       8 | 0x0002      |           2 |
|       9 | 0x0009      |           9 |
|      10 | 0x203E      |        8254 |
|      11 | 0x2055      |        8277 |
|      12 | 0x2059      |        8281 |
|      13 | 0x2056      |        8278 |
|      14 | 0x2057      |        8279 |
|      15 | 0x2058      |        8280 |
|      16 | 0x00C9      |         201 |

## String References

- **8251**: Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]
- **8252**: [Requirement/Objective completed]: Obtain all ancient abyssite found in this area.
- **8253**: [Requirement/Objective completed]: Obtain all atma found in this area.
- **8254**: [Requirement/Objective completed]: Complete all quests issued in this area.
- **8277**: I have taken up the task of putting to parchment the deeds of those who have done battle in these parts. This is what I have recorded under your name.
- **8278**: It would seem you've accomplished this task.
- **8279**: Why, I can hardly believe my eyes. You have accomplished anything and everything that could have been expected of you!
- **8280**: You deserve far more than this humble reward, but I fear it is all I have to give. I pray you are not offended.
- **8281**: Our battle for survival is never-ending. Pray do not let down your guard.

## Events

### Event 65535

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0000    |
| Data Size    | 201 bytes |
| Instructions | 1         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00 03 01 10 00 80 43 00  43 01 03 00 00 02 10 03  ......C.C.......
0010: 01 00 03 10 03 02 00 04  10 03 03 00 05 10 03 04  ................
0020: 00 06 10 03 05 00 07 10  03 06 00 08 10 02 01 80  ................
0030: 01 80 00 C8 00 24 02 80  03 80 03 80 25 02 00 10  .....$......%...
0040: 03 80 00 60 00 3E 06 00  04 80 54 00 03 02 10 01  ...`.>....T.....
0050: 80 01 59 00 03 02 10 03  80 48 05 80 23 01 A7 00  ..Y......H..#...
0060: 02 00 10 01 80 00 83 00  3E 06 00 06 80 77 00 03  ........>....w..
0070: 02 10 01 80 01 7C 00 03  02 10 03 80 48 07 80 23  .....|......H..#
0080: 01 A7 00 02 00 10 08 80  00 A6 00 3E 06 00 09 80  ...........>....
0090: 9A 00 03 02 10 01 80 01  9F 00 03 02 10 03 80 48  ...............H
00A0: 0A 80 23 01 A7 00 1B 03  02 10 00 00 03 03 10 01  ..#.............
00B0: 00 03 04 10 02 00 03 05  10 03 00 03 06 10 04 00  ................
00C0: 03 07 10 05 00 01 2D 00  1B                       ......-..       
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0001 [0x03] Work_Zone[1] = 254*
     0x0006 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0008 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x000A [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
     0x000F [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
     0x0014 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
     0x0019 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
     0x001E [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[6]
     0x0023 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[7]
     0x0028 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[8]
     0x002D [0x02] IF !(1* == 1*) GOTO 0x00C8
     0x0035 [0x24] CREATE_DIALOG(message_id=8251*, default_option=0*, option_flags=0*)
    → "Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]"
     0x003C [0x25] WAIT_DIALOG_SELECT()
     0x003D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0060
     0x0045 [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 7*) GOTO 0x0054
     0x004C [0x03] Work_Zone[2] = 1*
     0x0051 [0x01] GOTO 0x0059
     0x0054 [0x03] Work_Zone[2] = 0*
     0x0059 [0x48] [System] [8252*]:
    → "[Requirement/Objective completed]: Obtain all ancient abyssite found in this area."
     0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x005D [0x01] GOTO 0x00A7
     0x0060 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0083
     0x0068 [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 8*) GOTO 0x0077
     0x006F [0x03] Work_Zone[2] = 1*
     0x0074 [0x01] GOTO 0x007C
     0x0077 [0x03] Work_Zone[2] = 0*
     0x007C [0x48] [System] [8253*]:
    → "[Requirement/Objective completed]: Obtain all atma found in this area."
     0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0080 [0x01] GOTO 0x00A7
     0x0083 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00A6
     0x008B [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 9*) GOTO 0x009A
     0x0092 [0x03] Work_Zone[2] = 1*
     0x0097 [0x01] GOTO 0x009F
     0x009A [0x03] Work_Zone[2] = 0*
     0x009F [0x48] [System] [8254*]:
    → "[Requirement/Objective completed]: Complete all quests issued in this area."
     0x00A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00A3 [0x01] GOTO 0x00A7
     0x00A6 [0x1B] RETURN
     0x00A7 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
     0x00AC [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
     0x00B1 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[2]
     0x00B6 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[3]
     0x00BB [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[4]
     0x00C0 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[5]
     0x00C5 [0x01] GOTO 0x002D
     0x00C8 [0x1B] RETURN
```

### Event 334

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 20 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1E F0 FF FF 7F 6F 70           .....op
00D0: 1D 0B 80 23 1A 01 00 1D  0C 80 23 21 00           ...#......#!.   
```

#### Opcodes

```
  0: 0x00C9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00CF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00D0 [0x1D] PRINT_EVENT_MESSAGE(message_id=8277*)
    → "I have taken up the task of putting to parchment the deeds of those who have done battle in these parts. This is what I have recorded under your name."
  4: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00D4 [0x1A] CALL_SUBROUTINE(address=0x0001)
  6: 0x00D7 [0x1D] PRINT_EVENT_MESSAGE(message_id=8281*)
    → "Our battle for survival is never-ending. Pray do not let down your guard."
  7: 0x00DA [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00DB [0x21] END_EVENT
  9: 0x00DC [0x00] END_REQSTACK()
```

### Event 335

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 76 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         20 01 42                .B
00E0: 03 07 00 02 10 1E F0 FF  FF 7F 6F 70 1D 0B 80 23  ..........op...#
00F0: 02 07 00 01 80 80 FF 00  1D 0D 80 23 01 0E 01 02  ...........#....
0100: 07 00 08 80 80 0E 01 1D  0E 80 23 01 0E 01 1D 0F  ..........#.....
0110: 80 23 1D 0C 80 23 45 10  80 F0 FF FF 7F F0 FF FF  .#...#E.........
0120: 7F 71 73 74 63 03 80 21  00                       .qstc..!.       
```

#### Opcodes

```
  0: 0x00DD [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00DF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00E0 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[2]
  3: 0x00E5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00EA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00EB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x00EC [0x1D] PRINT_EVENT_MESSAGE(message_id=8277*)
    → "I have taken up the task of putting to parchment the deeds of those who have done battle in these parts. This is what I have recorded under your name."
  7: 0x00EF [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00F0 [0x02] IF !(ExtData[1]->WorkLocal[7] == 1*) GOTO 0x00FF
  9: 0x00F8 [0x1D] PRINT_EVENT_MESSAGE(message_id=8278*)
    → "It would seem you've accomplished this task."
 10: 0x00FB [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00FC [0x01] GOTO 0x010E
 12: 0x00FF [0x02] IF !(ExtData[1]->WorkLocal[7] == 2*) GOTO 0x010E
 13: 0x0107 [0x1D] PRINT_EVENT_MESSAGE(message_id=8279*)
    → "Why, I can hardly believe my eyes. You have accomplished anything and everything that could have been expected of you!"
 14: 0x010A [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x010B [0x01] GOTO 0x010E

SUBROUTINE_010E:
 16: 0x010E [0x1D] PRINT_EVENT_MESSAGE(message_id=8280*)
    → "You deserve far more than this humble reward, but I fear it is all I have to give. I pray you are not offended."
 17: 0x0111 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0112 [0x1D] PRINT_EVENT_MESSAGE(message_id=8281*)
    → "Our battle for survival is never-ending. Pray do not let down your guard."
 19: 0x0115 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0116 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0127 [0x21] END_EVENT
 22: 0x0128 [0x00] END_REQSTACK()
```
