# 17871260 - Diaphanous Transposer

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Kamihr Drifts (ID: 267) |
| Block Size       | 1084 bytes              |
| Total Events     | 5                       |
| References Count | 36                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [68](#event-68)       | 0x0001       |    231 |             55 |
| [71](#event-71)       | 0x00E8       |    109 |             27 |
| [72](#event-72)       | 0x0155       |     93 |             25 |
| [73](#event-73)       | 0x01B2       |    469 |             91 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x223E      |        8766 |
|       3 | 0x0010      |          16 |
|       4 | 0x0018      |          24 |
|       5 | 0x001F      |          31 |
|       6 | 0x40000000  |  1073741824 |
|       7 | 0x224F      |        8783 |
|       8 | 0x2256      |        8790 |
|       9 | 0x2241      |        8769 |
|      10 | 0x000B      |          11 |
|      11 | 0x2243      |        8771 |
|      12 | 0x225A      |        8794 |
|      13 | 0x225C      |        8796 |
|      14 | 0x2259      |        8793 |
|      15 | 0x225B      |        8795 |
|      16 | 0x225D      |        8797 |
|      17 | 0x0002      |           2 |
|      18 | 0x2240      |        8768 |
|      19 | 0x2242      |        8770 |
|      20 | 0x2269      |        8809 |
|      21 | 0x2270      |        8816 |
|      22 | 0x0003      |           3 |
|      23 | 0x0008      |           8 |
|      24 | 0x000F      |          15 |
|      25 | 0x0032      |          50 |
|      26 | 0x2273      |        8819 |
|      27 | 0x0004      |           4 |
|      28 | 0x0005      |           5 |
|      29 | 0x0006      |           6 |
|      30 | 0x0007      |           7 |
|      31 | 0x00C2      |         194 |
|      32 | 0x005A      |          90 |
|      33 | 0x00C9      |         201 |
|      34 | 0x002D      |          45 |
|      35 | 0x00C8      |         200 |

## String References

- **8766**: Attempt which? (Auto-transport: [off/on]) [None./Sortie./././././././././././././././Toggle auto-transport.]
- **8768**: Only party members present with you in this area will be transported to [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **8769**: [Apply to proceed/Proceed]? [Definitely!/Not yet.]
- **8770**: Entering [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **8771**: You have chosen not to [apply to/enter] [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **8783**: You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party.
- **8790**: Applying to enter [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]. You will be unable to participate if you add any more party members. Are you sure?
- **8793**: You are currently number in line to be drawn into this nightmare.
- **8794**: You are currently number in line, with in front of you.
- **8795**: Prepare yourselves! The battlefield is almost ready!
- **8796**: You are currently applying to enter [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **8797**: Your number: . (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]
- **8809**: Debug menu. [Check information./View applicants./Create./Change maximum limit./Clear applications./Automatically create./Check issued tickets./Close dialogue.]
- **8816**: Create [ASSIGN 1 : [standby/make/retry/rest/suspend]/ASSIGN 2 : [standby/make/retry/rest/suspend]/ASSIGN 3 : [standby/make/retry/rest/suspend]/Close menu.]
- **8819**: Designate a value between $0 and $1.

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

### Event 68

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 231 bytes |
| Instructions | 51        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 07 00 02 10 03  04 00 03 10 03 0B 00 06   B..............
0010: 10 03 0E 00 07 10 05 08  00 02 08 00 00 80 00 87  ................
0020: 00 03 02 00 01 80 03 03  00 01 80 03 01 00 01 80  ................
0030: 03 02 10 0F 00 24 02 80  01 80 07 00 25 02 00 10  .....$......%...
0040: 00 80 00 4D 00 03 02 00  00 80 01 6F 00 02 00 10  ...M.......o....
0050: 03 80 00 68 00 03 01 10  01 80 40 04 80 05 80 01  ...h......@.....
0060: 10 00 80 21 00 01 6F 00  03 01 10 06 80 21 00 03  ...!..o......!..
0070: 03 00 01 80 03 01 00 02  00 02 02 00 01 80 01 84  ................
0080: 00 06 08 00 01 19 00 03  06 10 0B 00 48 07 80 03  ............H...
0090: 02 10 01 00 48 08 80 23  03 03 10 01 80 24 09 80  ....H..#.....$..
00A0: 01 80 01 80 25 02 00 10  01 80 00 CD 00 03 01 10  ....%...........
00B0: 01 80 40 01 80 0A 80 01  10 01 00 43 00 43 01 02  ..@........C.C..
00C0: 09 10 01 80 01 CA 00 01  87 00 01 E6 00 03 02 10  ................
00D0: 01 00 03 03 10 01 80 03  04 10 03 00 48 0B 80 03  ............H...
00E0: 01 10 06 80 21 00 21 00                           ....!.!.        
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[2]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[3]
  3: 0x000C [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[6]
  4: 0x0011 [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[7]
  5: 0x0016 [0x05] ExtData[1]->WorkLocal[8] = 1
  6: 0x0019 [0x02] IF !(ExtData[1]->WorkLocal[8] == 1*) GOTO 0x0087
  7: 0x0021 [0x03] ExtData[1]->WorkLocal[2] = 0*
  8: 0x0026 [0x03] ExtData[1]->WorkLocal[3] = 0*
  9: 0x002B [0x03] ExtData[1]->WorkLocal[1] = 0*
 10: 0x0030 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[15]
 11: 0x0035 [0x24] CREATE_DIALOG(message_id=8766*, default_option=0*, option_flags=ExtData[1]->WorkLocal[7])
    → "Attempt which? (Auto-transport: [off/on]) [None./Sortie./././././././././././././././Toggle auto-transport.]"
 12: 0x003C [0x25] WAIT_DIALOG_SELECT()
 13: 0x003D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004D
 14: 0x0045 [0x03] ExtData[1]->WorkLocal[2] = 1*
 15: 0x004A [0x01] GOTO 0x006F
 16: 0x004D [0x02] IF !(Work_Zone[0] == 16*) GOTO 0x0068
 17: 0x0055 [0x03] Work_Zone[1] = 0*
 18: 0x005A [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=1*)
 19: 0x0063 [0x21] END_EVENT
 20: 0x0064 [0x00] END_REQSTACK()

SUBROUTINE_006F:
 21: 0x006F [0x03] ExtData[1]->WorkLocal[3] = 0*
 22: 0x0074 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[2]
 23: 0x0079 [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x0084
 24: 0x0081 [0x06] ExtData[1]->WorkLocal[8] = 0
 25: 0x0084 [0x01] GOTO 0x0019

SUBROUTINE_0087:
 26: 0x0087 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[11]
 27: 0x008C [0x48] [System] [8783*]:
    → "You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party."
 28: 0x008F [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 29: 0x0094 [0x48] [System] [8790*]:
    → "Applying to enter [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]. You will be unable to participate if you add any more party members. Are you sure?"
 30: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x0098 [0x03] Work_Zone[3] = 0*
 32: 0x009D [0x24] CREATE_DIALOG(message_id=8769*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Definitely!/Not yet.]"
 33: 0x00A4 [0x25] WAIT_DIALOG_SELECT()
 34: 0x00A5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CD
 35: 0x00AD [0x03] Work_Zone[1] = 0*
 36: 0x00B2 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 37: 0x00BB [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 38: 0x00BD [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 39: 0x00BF [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x00CA
 40: 0x00C7 [0x01] GOTO 0x0087
 41: 0x00CA [0x01] GOTO 0x00E6
 42: 0x00CD [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 43: 0x00D2 [0x03] Work_Zone[3] = 0*
 44: 0x00D7 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 45: 0x00DC [0x48] [System] [8771*]:
    → "You have chosen not to [apply to/enter] [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
 46: 0x00DF [0x03] Work_Zone[1] = 1073741824*
 47: 0x00E4 [0x21] END_EVENT
 48: 0x00E5 [0x00] END_REQSTACK()

SUBROUTINE_00E6:
 49: 0x00E6 [0x21] END_EVENT
 50: 0x00E7 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0065 [0x01] GOTO 0x006F
```

### Event 71

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E8    |
| Data Size    | 109 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                          03 12 00 04 10 03 04 10          ........
00F0: 06 10 02 04 10 01 80 02  01 01 48 0C 80 23 01 05  ..........H..#..
0100: 01 48 0D 80 23 03 04 10  12 00 48 0E 80 23 02 03  .H..#.....H..#..
0110: 10 01 80 00 21 01 48 0F  80 03 01 10 06 80 01 53  ....!.H........S
0120: 01 03 02 10 00 80 24 10  80 00 80 01 80 25 02 00  ......$......%..
0130: 10 01 80 00 3E 01 03 01  10 00 80 01 53 01 02 00  ....>.......S...
0140: 10 00 80 00 4E 01 03 01  10 11 80 01 53 01 03 01  ....N.......S...
0150: 10 06 80 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x00E8 [0x03] ExtData[1]->WorkLocal[18] = Work_Zone[4]
  1: 0x00ED [0x03] Work_Zone[4] = Work_Zone[6]
  2: 0x00F2 [0x02] IF !(Work_Zone[4] <= 0*) GOTO 0x0101
  3: 0x00FA [0x48] [System] [8794*]:
    → "You are currently number in line, with in front of you."
  4: 0x00FD [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00FE [0x01] GOTO 0x0105
  6: 0x0101 [0x48] [System] [8796*]:
    → "You are currently applying to enter [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
  7: 0x0104 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0105:
  8: 0x0105 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[18]
  9: 0x010A [0x48] [System] [8793*]:
    → "You are currently number in line to be drawn into this nightmare."
 10: 0x010D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x010E [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0121
 12: 0x0116 [0x48] [System] [8795*]:
    → "Prepare yourselves! The battlefield is almost ready!"
 13: 0x0119 [0x03] Work_Zone[1] = 1073741824*
 14: 0x011E [0x01] GOTO 0x0153
 15: 0x0121 [0x03] Work_Zone[2] = 1*
 16: 0x0126 [0x24] CREATE_DIALOG(message_id=8797*, default_option=1*, option_flags=0*)
    → "Your number: . (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]"
 17: 0x012D [0x25] WAIT_DIALOG_SELECT()
 18: 0x012E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x013E
 19: 0x0136 [0x03] Work_Zone[1] = 1*
 20: 0x013B [0x01] GOTO 0x0153
 21: 0x013E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x014E
 22: 0x0146 [0x03] Work_Zone[1] = 2*
 23: 0x014B [0x01] GOTO 0x0153
 24: 0x014E [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_0153:
 25: 0x0153 [0x21] END_EVENT
 26: 0x0154 [0x00] END_REQSTACK()
```

### Event 72

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0155   |
| Data Size    | 93 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                42 03 0F  00 02 10 03 10 00 04 10       B..........
0160: 48 12 80 23 03 03 10 00  80 24 09 80 01 80 01 80  H..#.....$......
0170: 25 02 00 10 01 80 00 AB  01 03 01 10 00 80 43 00  %.............C.
0180: 43 01 02 09 10 01 80 00  A3 01 03 02 10 0F 00 03  C...............
0190: 04 10 10 00 48 13 80 23  1A 1A 03 03 01 10 11 80  ....H..#........
01A0: 01 A8 01 03 01 10 06 80  01 B0 01 03 01 10 06 80  ................
01B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0155 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0156 [0x03] ExtData[1]->WorkLocal[15] = Work_Zone[2]
  2: 0x015B [0x03] ExtData[1]->WorkLocal[16] = Work_Zone[4]
  3: 0x0160 [0x48] [System] [8768*]:
    → "Only party members present with you in this area will be transported to [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
  4: 0x0163 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0164 [0x03] Work_Zone[3] = 1*
  6: 0x0169 [0x24] CREATE_DIALOG(message_id=8769*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Definitely!/Not yet.]"
  7: 0x0170 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0171 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01AB
  9: 0x0179 [0x03] Work_Zone[1] = 1*
 10: 0x017E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x0180 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x0182 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x01A3
 13: 0x018A [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[15]
 14: 0x018F [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[16]
 15: 0x0194 [0x48] [System] [8770*]:
    → "Entering [/Sortie][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
 16: 0x0197 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0198 [0x1A] CALL_SUBROUTINE(address=0x031A)
 18: 0x019B [0x03] Work_Zone[1] = 2*
 19: 0x01A0 [0x01] GOTO 0x01A8
 20: 0x01A3 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_01A8:
 21: 0x01A8 [0x01] GOTO 0x01B0
 22: 0x01AB [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_01B0:
 23: 0x01B0 [0x21] END_EVENT
 24: 0x01B1 [0x00] END_REQSTACK()
```

### Event 73

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01B2    |
| Data Size    | 469 bytes |
| Instructions | 80        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:       03 13 00 02 10 03  14 00 03 10 03 15 00 04    ..............
01C0: 10 05 0A 00 02 0A 00 00  80 00 18 03 24 14 80 01  ............$...
01D0: 80 01 80 25 02 00 10 01  80 00 E8 01 03 01 10 00  ...%............
01E0: 80 43 00 43 01 01 15 03  02 00 10 00 80 00 FC 01  .C.C............
01F0: 03 01 10 11 80 43 00 43  01 01 15 03 02 00 10 11  .....C.C........
0200: 80 00 7F 02 03 02 10 13  00 03 03 10 14 00 03 04  ................
0210: 10 15 00 24 15 80 01 80  01 80 25 02 00 10 01 80  ...$......%.....
0220: 00 2B 02 03 00 00 00 80  01 53 02 02 00 10 00 80  .+.......S......
0230: 00 3B 02 03 00 00 11 80  01 53 02 02 00 10 11 80  .;.......S......
0240: 00 4B 02 03 00 00 16 80  01 53 02 03 00 00 01 80  .K.......S......
0250: 06 0A 00 02 00 00 01 80  02 7C 02 03 01 10 16 80  .........|......
0260: 40 17 80 18 80 01 10 00  00 43 00 43 01 03 13 00  @........C.C....
0270: 02 10 03 14 00 03 10 03  15 00 04 10 01 15 03 02  ................
0280: 00 10 16 80 00 B3 02 03  02 10 00 80 03 03 10 19  ................
0290: 80 48 1A 80 71 12 00 80  11 80 71 13 00 00 03 01  .H..q.....q.....
02A0: 10 1B 80 40 17 80 18 80  01 10 00 00 43 00 43 01  ...@........C.C.
02B0: 01 15 03 02 00 10 1B 80  00 C7 02 03 01 10 1C 80  ................
02C0: 43 00 43 01 01 15 03 02  00 10 1C 80 00 FE 02 03  C.C.............
02D0: 02 10 00 80 03 03 10 19  80 48 1A 80 71 12 00 80  .........H..q...
02E0: 11 80 71 13 00 00 03 01  10 1D 80 40 17 80 18 80  ..q........@....
02F0: 01 10 00 00 43 00 43 01  06 0A 00 01 15 03 02 00  ....C.C.........
0300: 10 1D 80 00 12 03 03 01  10 1E 80 43 00 43 01 01  ...........C.C..
0310: 15 03 06 0A 00 01 C4 01  21 00 CD 1F 80 F8 FF FF  ........!.......
0320: 7F F0 FF FF 7F 73 30 30  30 01 80 1C 20 80 45 21  .....s000... .E!
0330: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 31 01 80 55  .........who1..U
0340: 21 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 31 1C 22  !.........who1."
0350: 80 45 23 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E#.........fdo1
0360: 01 80 55 23 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U#.........fdo
0370: 31 45 21 80 F0 FF FF 7F  F0 FF FF 7F 77 68 69 31  1E!.........whi1
0380: 01 80 1C 18 80 30 1B                              .....0.         
```

#### Opcodes

```
  0: 0x01B2 [0x03] ExtData[1]->WorkLocal[19] = Work_Zone[2]
  1: 0x01B7 [0x03] ExtData[1]->WorkLocal[20] = Work_Zone[3]
  2: 0x01BC [0x03] ExtData[1]->WorkLocal[21] = Work_Zone[4]
  3: 0x01C1 [0x05] ExtData[1]->WorkLocal[10] = 1
  4: 0x01C4 [0x02] IF !(ExtData[1]->WorkLocal[10] == 1*) GOTO 0x0318
  5: 0x01CC [0x24] CREATE_DIALOG(message_id=8809*, default_option=0*, option_flags=0*)
    → "Debug menu. [Check information./View applicants./Create./Change maximum limit./Clear applications./Automatically create./Check issued tickets./Close dialogue.]"
  6: 0x01D3 [0x25] WAIT_DIALOG_SELECT()
  7: 0x01D4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01E8
  8: 0x01DC [0x03] Work_Zone[1] = 1*
  9: 0x01E1 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x01E3 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x01E5 [0x01] GOTO 0x0315
 12: 0x01E8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01FC
 13: 0x01F0 [0x03] Work_Zone[1] = 2*
 14: 0x01F5 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 15: 0x01F7 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 16: 0x01F9 [0x01] GOTO 0x0315
 17: 0x01FC [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x027F
 18: 0x0204 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[19]
 19: 0x0209 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[20]
 20: 0x020E [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[21]
 21: 0x0213 [0x24] CREATE_DIALOG(message_id=8816*, default_option=0*, option_flags=0*)
    → "Create [ASSIGN 1 : [standby/make/retry/rest/suspend]/ASSIGN 2 : [standby/make/retry/rest/suspend]/ASSIGN 3 : [standby/make/retry/rest/suspend]/Close menu.]"
 22: 0x021A [0x25] WAIT_DIALOG_SELECT()
 23: 0x021B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x022B
 24: 0x0223 [0x03] ExtData[1]->WorkLocal[0] = 1*
 25: 0x0228 [0x01] GOTO 0x0253
 26: 0x022B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x023B
 27: 0x0233 [0x03] ExtData[1]->WorkLocal[0] = 2*
 28: 0x0238 [0x01] GOTO 0x0253
 29: 0x023B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x024B
 30: 0x0243 [0x03] ExtData[1]->WorkLocal[0] = 3*
 31: 0x0248 [0x01] GOTO 0x0253
 32: 0x024B [0x03] ExtData[1]->WorkLocal[0] = 0*
 33: 0x0250 [0x06] ExtData[1]->WorkLocal[10] = 0

SUBROUTINE_0253:
 34: 0x0253 [0x02] IF !(ExtData[1]->WorkLocal[0] <= 0*) GOTO 0x027C
 35: 0x025B [0x03] Work_Zone[1] = 3*
 36: 0x0260 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 37: 0x0269 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 38: 0x026B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 39: 0x026D [0x03] ExtData[1]->WorkLocal[19] = Work_Zone[2]
 40: 0x0272 [0x03] ExtData[1]->WorkLocal[20] = Work_Zone[3]
 41: 0x0277 [0x03] ExtData[1]->WorkLocal[21] = Work_Zone[4]
 42: 0x027C [0x01] GOTO 0x0315
 43: 0x027F [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x02B3
 44: 0x0287 [0x03] Work_Zone[2] = 1*
 45: 0x028C [0x03] Work_Zone[3] = 50*
 46: 0x0291 [0x48] [System] [8819*]:
    → "Designate a value between $0 and $1."
 47: 0x0294 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 48: 0x029A [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 49: 0x029E [0x03] Work_Zone[1] = 4*
 50: 0x02A3 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 51: 0x02AC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 52: 0x02AE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 53: 0x02B0 [0x01] GOTO 0x0315
 54: 0x02B3 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x02C7
 55: 0x02BB [0x03] Work_Zone[1] = 5*
 56: 0x02C0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 57: 0x02C2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 58: 0x02C4 [0x01] GOTO 0x0315
 59: 0x02C7 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x02FE
 60: 0x02CF [0x03] Work_Zone[2] = 1*
 61: 0x02D4 [0x03] Work_Zone[3] = 50*
 62: 0x02D9 [0x48] [System] [8819*]:
    → "Designate a value between $0 and $1."
 63: 0x02DC [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 64: 0x02E2 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 65: 0x02E6 [0x03] Work_Zone[1] = 6*
 66: 0x02EB [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 67: 0x02F4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 68: 0x02F6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 69: 0x02F8 [0x06] ExtData[1]->WorkLocal[10] = 0
 70: 0x02FB [0x01] GOTO 0x0315
 71: 0x02FE [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0312
 72: 0x0306 [0x03] Work_Zone[1] = 7*
 73: 0x030B [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 74: 0x030D [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 75: 0x030F [0x01] GOTO 0x0315
 76: 0x0312 [0x06] ExtData[1]->WorkLocal[10] = 0

SUBROUTINE_0315:
 77: 0x0315 [0x01] GOTO 0x01C4
 78: 0x0318 [0x21] END_EVENT
 79: 0x0319 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x031A [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "s000" with entities [EventEntity, LocalPlayer], work=[194*, 0*]
     0x032B [0x1C] WAIT(90* ticks)
     0x032E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x033F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x034E [0x1C] WAIT(45* ticks)
     0x0351 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0362 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0371 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0382 [0x1C] WAIT(15* ticks)
     0x0385 [0x30] SET_UCOFF_CONTINUE_ZERO()
     0x0386 [0x1B] RETURN
```
