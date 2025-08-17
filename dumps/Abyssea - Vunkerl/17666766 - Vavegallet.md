# 17666766 - Vavegallet

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Vunkerl (ID: 217) |
| Block Size       | 388 bytes                   |
| Total Events     | 4                           |
| References Count | 19                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |    201 |             47 |
| [1089](#event-1089)   | 0x00C9       |     22 |             10 |
| [1090](#event-1090)   | 0x00DF       |     24 |              6 |
| [1091](#event-1091)   | 0x00F7       |     32 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FE      |         254 |
|       1 | 0x0001      |           1 |
|       2 | 0x1F8E      |        8078 |
|       3 | 0x0000      |           0 |
|       4 | 0x0007      |           7 |
|       5 | 0x1F8F      |        8079 |
|       6 | 0x0008      |           8 |
|       7 | 0x1F90      |        8080 |
|       8 | 0x0002      |           2 |
|       9 | 0x0009      |           9 |
|      10 | 0x1F91      |        8081 |
|      11 | 0x2110      |        8464 |
|      12 | 0x2111      |        8465 |
|      13 | 0x2112      |        8466 |
|      14 | 0x2113      |        8467 |
|      15 | 0x00C9      |         201 |
|      16 | 0x2114      |        8468 |
|      17 | 0x2115      |        8469 |
|      18 | 0x2116      |        8470 |

## String References

- **8078**: Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]
- **8079**: [Requirement/Objective completed]: Obtain all ancient abyssite found in this area.
- **8080**: [Requirement/Objective completed]: Obtain all atma found in this area.
- **8081**: [Requirement/Objective completed]: Complete all quests issued in this area.
- **8464**: Greetings. I'm in charge of keeping the records of your exploits, and presenting you with rewards commensurate with your deeds.
- **8465**: Your achievements in this area thus far are as follows:
- **8466**: Come back any time for an evaluation of your exploits.
- **8467**: It seems you've completed an objective. Well done. Take this as a token of thanks for your efforts.
- **8468**: Amazing! You've completed every single objective in this area!
- **8469**: Why, this is an accomplishment the likes of which I've never seen. Would that you had wings, that you could take your place in the sky as the sun whose warmth and radiance we have gone so long without!
- **8470**: Ah, forgive me for getting carried away with myself. Your accomplishments moved me like I've not been moved in some while. Please, continue to stand by our side!

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
     0x0035 [0x24] CREATE_DIALOG(message_id=8078*, default_option=0*, option_flags=0*)
    → "Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]"
     0x003C [0x25] WAIT_DIALOG_SELECT()
     0x003D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0060
     0x0045 [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 7*) GOTO 0x0054
     0x004C [0x03] Work_Zone[2] = 1*
     0x0051 [0x01] GOTO 0x0059
     0x0054 [0x03] Work_Zone[2] = 0*
     0x0059 [0x48] [System] [8079*]:
    → "[Requirement/Objective completed]: Obtain all ancient abyssite found in this area."
     0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x005D [0x01] GOTO 0x00A7
     0x0060 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0083
     0x0068 [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 8*) GOTO 0x0077
     0x006F [0x03] Work_Zone[2] = 1*
     0x0074 [0x01] GOTO 0x007C
     0x0077 [0x03] Work_Zone[2] = 0*
     0x007C [0x48] [System] [8080*]:
    → "[Requirement/Objective completed]: Obtain all atma found in this area."
     0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0080 [0x01] GOTO 0x00A7
     0x0083 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00A6
     0x008B [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 9*) GOTO 0x009A
     0x0092 [0x03] Work_Zone[2] = 1*
     0x0097 [0x01] GOTO 0x009F
     0x009A [0x03] Work_Zone[2] = 0*
     0x009F [0x48] [System] [8081*]:
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

### Event 1089

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 22 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1E F0 FF FF 7F 1D 0B           .......
00D0: 80 23 1D 0C 80 23 1A 01  00 1D 0D 80 23 21 00     .#...#......#!. 
```

#### Opcodes

```
  0: 0x00C9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CE [0x1D] PRINT_EVENT_MESSAGE(message_id=8464*)
    → "Greetings. I'm in charge of keeping the records of your exploits, and presenting you with rewards commensurate with your deeds."
  2: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00D2 [0x1D] PRINT_EVENT_MESSAGE(message_id=8465*)
    → "Your achievements in this area thus far are as follows:"
  4: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00D6 [0x1A] CALL_SUBROUTINE(address=0x0001)
  6: 0x00D9 [0x1D] PRINT_EVENT_MESSAGE(message_id=8466*)
    → "Come back any time for an evaluation of your exploits."
  7: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00DD [0x21] END_EVENT
  9: 0x00DE [0x00] END_REQSTACK()
```

### Event 1090

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DF   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               42                 B
00E0: 1D 0E 80 23 45 0F 80 F0  FF FF 7F F0 FF FF 7F 71  ...#E..........q
00F0: 73 74 63 03 80 21 00                              stc..!.         
```

#### Opcodes

```
  0: 0x00DF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00E0 [0x1D] PRINT_EVENT_MESSAGE(message_id=8467*)
    → "It seems you've completed an objective. Well done. Take this as a token of thanks for your efforts."
  2: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00E4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  4: 0x00F5 [0x21] END_EVENT
  5: 0x00F6 [0x00] END_REQSTACK()
```

### Event 1091

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F7   |
| Data Size    | 32 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      42  1D 10 80 23 1D 11 80 23         B...#...#
0100: 1D 12 80 23 45 0F 80 F0  FF FF 7F F0 FF FF 7F 71  ...#E..........q
0110: 73 74 63 03 80 21 00                              stc..!.         
```

#### Opcodes

```
  0: 0x00F7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00F8 [0x1D] PRINT_EVENT_MESSAGE(message_id=8468*)
    → "Amazing! You've completed every single objective in this area!"
  2: 0x00FB [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00FC [0x1D] PRINT_EVENT_MESSAGE(message_id=8469*)
    → "Why, this is an accomplishment the likes of which I've never seen. Would that you had wings, that you could take your place in the sky as the sun whose warmth and radiance we have gone so long without!"
  4: 0x00FF [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0100 [0x1D] PRINT_EVENT_MESSAGE(message_id=8470*)
    → "Ah, forgive me for getting carried away with myself. Your accomplishments moved me like I've not been moved in some while. Please, continue to stand by our side!"
  6: 0x0103 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0104 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x0115 [0x21] END_EVENT
  9: 0x0116 [0x00] END_REQSTACK()
```
