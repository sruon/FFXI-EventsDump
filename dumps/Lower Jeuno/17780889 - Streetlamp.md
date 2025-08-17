# 17780889 - Streetlamp

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 624 bytes             |
| Total Events     | 2                     |
| References Count | 21                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [128](#event-128)     | 0x0001       |    514 |             81 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1C64      |        7268 |
|       2 | 0x0000      |           0 |
|       3 | 0x40000000  |  1073741824 |
|       4 | 0x0091      |         145 |
|       5 | 0x0002      |           2 |
|       6 | 0x0003      |           3 |
|       7 | 0x0004      |           4 |
|       8 | 0x0005      |           5 |
|       9 | 0x0006      |           6 |
|      10 | 0x0007      |           7 |
|      11 | 0x0008      |           8 |
|      12 | 0x0009      |           9 |
|      13 | 0x000A      |          10 |
|      14 | 0x000B      |          11 |
|      15 | 0x00B4      |         180 |
|      16 | 0x1C69      |        7273 |
|      17 | 0x1C6C      |        7276 |
|      18 | 0x1C6D      |        7277 |
|      19 | 0x1C6A      |        7274 |
|      20 | 0x1C6B      |        7275 |

## String References

- **7268**: Light the lamp? [Yes./No.]
- **7273**: The lamp is already lit.
- **7274**: The lamp is lit.
- **7275**: You examine the lamp. It seems that it must be lit manually.
- **7276**: It is too early to light it. You must wait until nine o'clock.
- **7277**: You have failed to light all the lamps in time.

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

### Event 128

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 514 bytes |
| Instructions | 81        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 03 00 00 02  10 03 01 00 03 10 02 00    .B............
0010: 00 00 80 80 B6 01 06 01  10 24 01 80 02 80 02 80  .........$......
0020: 25 02 00 10 02 80 00 B3  01 03 01 10 00 80 46 01  %.............F.
0030: 43 00 43 01 03 02 00 09  10 02 02 00 00 80 00 49  C.C............I
0040: 00 03 01 10 03 80 01 AE  01 02 01 00 02 80 80 65  ...............e
0050: 00 45 04 80 F0 FF FF 7F  F0 FF FF 7F 63 6C 30 30  .E..........cl00
0060: 02 80 01 99 01 02 01 00  00 80 80 81 00 45 04 80  .............E..
0070: F0 FF FF 7F F0 FF FF 7F  63 6C 30 31 02 80 01 99  ........cl01....
0080: 01 02 01 00 05 80 80 9D  00 45 04 80 F0 FF FF 7F  .........E......
0090: F0 FF FF 7F 63 6C 30 32  02 80 01 99 01 02 01 00  ....cl02........
00A0: 06 80 80 B9 00 45 04 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
00B0: 63 6C 30 33 02 80 01 99  01 02 01 00 07 80 80 D5  cl03............
00C0: 00 45 04 80 F0 FF FF 7F  F0 FF FF 7F 63 6C 30 34  .E..........cl04
00D0: 02 80 01 99 01 02 01 00  08 80 80 F1 00 45 04 80  .............E..
00E0: F0 FF FF 7F F0 FF FF 7F  63 6C 30 35 02 80 01 99  ........cl05....
00F0: 01 02 01 00 09 80 80 0D  01 45 04 80 F0 FF FF 7F  .........E......
0100: F0 FF FF 7F 63 6C 30 36  02 80 01 99 01 02 01 00  ....cl06........
0110: 0A 80 80 29 01 45 04 80  F0 FF FF 7F F0 FF FF 7F  ...).E..........
0120: 63 6C 30 37 02 80 01 99  01 02 01 00 0B 80 80 45  cl07...........E
0130: 01 45 04 80 F0 FF FF 7F  F0 FF FF 7F 63 6C 30 38  .E..........cl08
0140: 02 80 01 99 01 02 01 00  0C 80 80 61 01 45 04 80  ...........a.E..
0150: F0 FF FF 7F F0 FF FF 7F  63 6C 30 39 02 80 01 99  ........cl09....
0160: 01 02 01 00 0D 80 80 7D  01 45 04 80 F0 FF FF 7F  .......}.E......
0170: F0 FF FF 7F 63 6C 31 30  02 80 01 99 01 02 01 00  ....cl10........
0180: 0E 80 80 99 01 45 04 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0190: 63 6C 31 31 02 80 01 99  01 45 04 80 F0 FF FF 7F  cl11.....E......
01A0: F0 FF FF 7F 73 65 6C 74  02 80 4C 1C 0F 80 46 00  ....selt..L...F.
01B0: 01 B3 01 01 01 02 02 00  00 05 80 80 C5 01 48 10  ..............H.
01C0: 80 23 01 01 02 02 00 00  07 80 80 D4 01 48 11 80  .#...........H..
01D0: 23 01 01 02 02 00 00 06  80 80 E3 01 48 12 80 23  #...........H..#
01E0: 01 01 02 02 00 00 08 80  80 F2 01 48 13 80 23 01  ...........H..#.
01F0: 01 02 02 00 00 09 80 80  01 02 48 14 80 23 01 01  ..........H..#..
0200: 02 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x0009 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  4: 0x000E [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x01B6
  5: 0x0016 [0x06] Work_Zone[1] = 0
  6: 0x0019 [0x24] CREATE_DIALOG(message_id=7268*, default_option=0*, option_flags=0*)
    → "Light the lamp? [Yes./No.]"
  7: 0x0020 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0021 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01B3
  9: 0x0029 [0x03] Work_Zone[1] = 1*
 10: 0x002E [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0030 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x0032 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x0034 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[9]
 14: 0x0039 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x0049
 15: 0x0041 [0x03] Work_Zone[1] = 1073741824*
 16: 0x0046 [0x01] GOTO 0x01AE
 17: 0x0049 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0065
 18: 0x0051 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl00" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 19: 0x0062 [0x01] GOTO 0x0199
 20: 0x0065 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0081
 21: 0x006D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl01" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 22: 0x007E [0x01] GOTO 0x0199
 23: 0x0081 [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x009D
 24: 0x0089 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl02" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 25: 0x009A [0x01] GOTO 0x0199
 26: 0x009D [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x00B9
 27: 0x00A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl03" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 28: 0x00B6 [0x01] GOTO 0x0199
 29: 0x00B9 [0x02] IF !(ExtData[1]->WorkLocal[1] == 4*) GOTO 0x00D5
 30: 0x00C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl04" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 31: 0x00D2 [0x01] GOTO 0x0199
 32: 0x00D5 [0x02] IF !(ExtData[1]->WorkLocal[1] == 5*) GOTO 0x00F1
 33: 0x00DD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl05" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 34: 0x00EE [0x01] GOTO 0x0199
 35: 0x00F1 [0x02] IF !(ExtData[1]->WorkLocal[1] == 6*) GOTO 0x010D
 36: 0x00F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl06" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 37: 0x010A [0x01] GOTO 0x0199
 38: 0x010D [0x02] IF !(ExtData[1]->WorkLocal[1] == 7*) GOTO 0x0129
 39: 0x0115 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl07" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 40: 0x0126 [0x01] GOTO 0x0199
 41: 0x0129 [0x02] IF !(ExtData[1]->WorkLocal[1] == 8*) GOTO 0x0145
 42: 0x0131 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl08" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 43: 0x0142 [0x01] GOTO 0x0199
 44: 0x0145 [0x02] IF !(ExtData[1]->WorkLocal[1] == 9*) GOTO 0x0161
 45: 0x014D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl09" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 46: 0x015E [0x01] GOTO 0x0199
 47: 0x0161 [0x02] IF !(ExtData[1]->WorkLocal[1] == 10*) GOTO 0x017D
 48: 0x0169 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl10" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 49: 0x017A [0x01] GOTO 0x0199
 50: 0x017D [0x02] IF !(ExtData[1]->WorkLocal[1] == 11*) GOTO 0x0199
 51: 0x0185 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cl11" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 52: 0x0196 [0x01] GOTO 0x0199

SUBROUTINE_0199:
 53: 0x0199 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "selt" with entities [LocalPlayer, LocalPlayer], work=[145*, 0*]
 54: 0x01AA [0x4C] EventEntity->StatusEvent = 8 // Open door
 55: 0x01AB [0x1C] WAIT(180* ticks)

SUBROUTINE_01AE:
 56: 0x01AE [0x46] CAMERA_CONTROL: Restore default settings
 57: 0x01B0 [0x01] GOTO 0x01B3

SUBROUTINE_01B3:
 58: 0x01B3 [0x01] GOTO 0x0201
 59: 0x01B6 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x01C5
 60: 0x01BE [0x48] [System] [7273*]:
    → "The lamp is already lit."
 61: 0x01C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x01C2 [0x01] GOTO 0x0201
 63: 0x01C5 [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x01D4
 64: 0x01CD [0x48] [System] [7276*]:
    → "It is too early to light it. You must wait until nine o'clock."
 65: 0x01D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x01D1 [0x01] GOTO 0x0201
 67: 0x01D4 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x01E3
 68: 0x01DC [0x48] [System] [7277*]:
    → "You have failed to light all the lamps in time."
 69: 0x01DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 70: 0x01E0 [0x01] GOTO 0x0201
 71: 0x01E3 [0x02] IF !(ExtData[1]->WorkLocal[0] == 5*) GOTO 0x01F2
 72: 0x01EB [0x48] [System] [7274*]:
    → "The lamp is lit."
 73: 0x01EE [0x23] WAIT_FOR_DIALOG_INTERACTION
 74: 0x01EF [0x01] GOTO 0x0201
 75: 0x01F2 [0x02] IF !(ExtData[1]->WorkLocal[0] == 6*) GOTO 0x0201
 76: 0x01FA [0x48] [System] [7275*]:
    → "You examine the lamp. It seems that it must be lit manually."
 77: 0x01FD [0x23] WAIT_FOR_DIALOG_INTERACTION
 78: 0x01FE [0x01] GOTO 0x0201

SUBROUTINE_0201:
 79: 0x0201 [0x21] END_EVENT
 80: 0x0202 [0x00] END_REQSTACK()
```
