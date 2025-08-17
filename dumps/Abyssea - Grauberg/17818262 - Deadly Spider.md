# 17818262 - Deadly Spider

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Grauberg (ID: 254) |
| Block Size       | 464 bytes                    |
| Total Events     | 3                            |
| References Count | 19                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |    201 |             47 |
| [280](#event-280)     | 0x00C9       |     66 |             12 |
| [281](#event-281)     | 0x010B       |     90 |             22 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FE      |         254 |
|       1 | 0x0001      |           1 |
|       2 | 0x208D      |        8333 |
|       3 | 0x0000      |           0 |
|       4 | 0x0007      |           7 |
|       5 | 0x208E      |        8334 |
|       6 | 0x0008      |           8 |
|       7 | 0x208F      |        8335 |
|       8 | 0x0002      |           2 |
|       9 | 0x0009      |           9 |
|      10 | 0x2090      |        8336 |
|      11 | 0x001E      |          30 |
|      12 | 0x003C      |          60 |
|      13 | 0x205D      |        8285 |
|      14 | 0x2061      |        8289 |
|      15 | 0x205E      |        8286 |
|      16 | 0x205F      |        8287 |
|      17 | 0x2060      |        8288 |
|      18 | 0x00C9      |         201 |

## String References

- **8285**: G'day, mate. Come to check on your progress for this area, have ya? Well then, treat yerself to a good eyeful:
- **8286**: Looks like you've completed this objective. You can give yerself a pat on the back for that.
- **8287**: Crikey, you've completed all objectives in the area! That's something to write home about, I reckon!
- **8288**: Here's a little reward for ya, mate, just to show our appreciation.
- **8289**: Stay sharp out there, eh? Else you'll end up bein' tucker for them Abyssean nasties.
- **8333**: Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]
- **8334**: [Requirement/Objective completed]: Obtain all ancient abyssite found in this area.
- **8335**: [Requirement/Objective completed]: Obtain all atma found in this area.
- **8336**: [Requirement/Objective completed]: Complete all quests issued in this area.

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
     0x0035 [0x24] CREATE_DIALOG(message_id=8333*, default_option=0*, option_flags=0*)
    → "Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]"
     0x003C [0x25] WAIT_DIALOG_SELECT()
     0x003D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0060
     0x0045 [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 7*) GOTO 0x0054
     0x004C [0x03] Work_Zone[2] = 1*
     0x0051 [0x01] GOTO 0x0059
     0x0054 [0x03] Work_Zone[2] = 0*
     0x0059 [0x48] [System] [8334*]:
    → "[Requirement/Objective completed]: Obtain all ancient abyssite found in this area."
     0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x005D [0x01] GOTO 0x00A7
     0x0060 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0083
     0x0068 [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 8*) GOTO 0x0077
     0x006F [0x03] Work_Zone[2] = 1*
     0x0074 [0x01] GOTO 0x007C
     0x0077 [0x03] Work_Zone[2] = 0*
     0x007C [0x48] [System] [8335*]:
    → "[Requirement/Objective completed]: Obtain all atma found in this area."
     0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0080 [0x01] GOTO 0x00A7
     0x0083 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00A6
     0x008B [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 9*) GOTO 0x009A
     0x0092 [0x03] Work_Zone[2] = 1*
     0x0097 [0x01] GOTO 0x009F
     0x009A [0x03] Work_Zone[2] = 0*
     0x009F [0x48] [System] [8336*]:
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

### Event 280

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 66 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1E F0 FF FF 7F 1C 0B           .......
00D0: 80 66 0C 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .f..........tlk0
00E0: 1D 0D 80 23 66 0C 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
00F0: 6C 6B 31 1A 01 00 66 0C  80 F8 FF FF 7F F8 FF FF  lk1...f.........
0100: 7F 74 6C 6B 30 1D 0E 80  23 21 00                 .tlk0...#!.     
```

#### Opcodes

```
  0: 0x00C9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CE [0x1C] WAIT(30* ticks)
  2: 0x00D1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  3: 0x00E0 [0x1D] PRINT_EVENT_MESSAGE(message_id=8285*)
    → "G'day, mate. Come to check on your progress for this area, have ya? Well then, treat yerself to a good eyeful:"
  4: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00E4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=60*
  6: 0x00F3 [0x1A] CALL_SUBROUTINE(address=0x0001)
  7: 0x00F6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  8: 0x0105 [0x1D] PRINT_EVENT_MESSAGE(message_id=8289*)
    → "Stay sharp out there, eh? Else you'll end up bein' tucker for them Abyssean nasties."
  9: 0x0108 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0109 [0x21] END_EVENT
 11: 0x010A [0x00] END_REQSTACK()
```

### Event 281

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010B   |
| Data Size    | 90 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   42 03 07 00 02             B....
0110: 10 1E F0 FF FF 7F 1C 0B  80 66 0C 80 F8 FF FF 7F  .........f......
0120: F8 FF FF 7F 74 6C 6B 30  1D 0D 80 23 02 07 00 01  ....tlk0...#....
0130: 80 80 3B 01 1D 0F 80 23  01 4A 01 02 07 00 08 80  ..;....#.J......
0140: 80 4A 01 1D 10 80 23 01  4A 01 1D 11 80 23 1D 0E  .J....#.J....#..
0150: 80 23 45 12 80 F0 FF FF  7F F0 FF FF 7F 71 73 74  .#E..........qst
0160: 63 03 80 21 00                                    c..!.           
```

#### Opcodes

```
  0: 0x010B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x010C [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[2]
  2: 0x0111 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0116 [0x1C] WAIT(30* ticks)
  4: 0x0119 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  5: 0x0128 [0x1D] PRINT_EVENT_MESSAGE(message_id=8285*)
    → "G'day, mate. Come to check on your progress for this area, have ya? Well then, treat yerself to a good eyeful:"
  6: 0x012B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x012C [0x02] IF !(ExtData[1]->WorkLocal[7] == 1*) GOTO 0x013B
  8: 0x0134 [0x1D] PRINT_EVENT_MESSAGE(message_id=8286*)
    → "Looks like you've completed this objective. You can give yerself a pat on the back for that."
  9: 0x0137 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0138 [0x01] GOTO 0x014A
 11: 0x013B [0x02] IF !(ExtData[1]->WorkLocal[7] == 2*) GOTO 0x014A
 12: 0x0143 [0x1D] PRINT_EVENT_MESSAGE(message_id=8287*)
    → "Crikey, you've completed all objectives in the area! That's something to write home about, I reckon!"
 13: 0x0146 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0147 [0x01] GOTO 0x014A

SUBROUTINE_014A:
 15: 0x014A [0x1D] PRINT_EVENT_MESSAGE(message_id=8288*)
    → "Here's a little reward for ya, mate, just to show our appreciation."
 16: 0x014D [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x014E [0x1D] PRINT_EVENT_MESSAGE(message_id=8289*)
    → "Stay sharp out there, eh? Else you'll end up bein' tucker for them Abyssean nasties."
 18: 0x0151 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0152 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 20: 0x0163 [0x21] END_EVENT
 21: 0x0164 [0x00] END_REQSTACK()
```
