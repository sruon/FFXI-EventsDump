# 17736063 - Enigmatic Footprints

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 1244 bytes             |
| Total Events     | 6                      |
| References Count | 37                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [655](#event-655)     | 0x0001       |    353 |             83 |
| [658](#event-658)     | 0x0162       |     94 |             24 |
| [659](#event-659)     | 0x01C0       |     97 |             27 |
| [690](#event-690)     | 0x0221       |    147 |             28 |
| [660](#event-660)     | 0x02B4       |    361 |             69 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0C54      |        3156 |
|       2 | 0x0001      |           1 |
|       3 | 0x0002      |           2 |
|       4 | 0x410B      |       16651 |
|       5 | 0x4138      |       16696 |
|       6 | 0x0018      |          24 |
|       7 | 0x001F      |          31 |
|       8 | 0x0003      |           3 |
|       9 | 0x0004      |           4 |
|      10 | 0x40000000  |  1073741824 |
|      11 | 0x411D      |       16669 |
|      12 | 0x411C      |       16668 |
|      13 | 0x4123      |       16675 |
|      14 | 0x410E      |       16654 |
|      15 | 0x000B      |          11 |
|      16 | 0x4110      |       16656 |
|      17 | 0x4127      |       16679 |
|      18 | 0x4129      |       16681 |
|      19 | 0x4126      |       16678 |
|      20 | 0x4128      |       16680 |
|      21 | 0x412A      |       16682 |
|      22 | 0x410D      |       16653 |
|      23 | 0x410F      |       16655 |
|      24 | 0x4135      |       16693 |
|      25 | 0x410C      |       16652 |
|      26 | 0x413E      |       16702 |
|      27 | 0x0032      |          50 |
|      28 | 0x4147      |       16711 |
|      29 | 0x0008      |           8 |
|      30 | 0x000F      |          15 |
|      31 | 0x0005      |           5 |
|      32 | 0x0006      |           6 |
|      33 | 0x005A      |          90 |
|      34 | 0x00C9      |         201 |
|      35 | 0x002D      |          45 |
|      36 | 0x00C8      |         200 |

## String References

- **16651**: Attempt which? (Auto-transport: [off/on]) [None./$8. (CL: $1)/$3 status./Switch $3 use state. ([off/on])/Toggle auto-transport.]
- **16652**: Instance Setting (Auto-transport: ([off/on]) [Back./$3 status./Switch $3 use state. ([off/on])/Toggle auto-transport.]
- **16653**: Only party members present with you in this area will be transported to $8.
- **16654**: [Apply to proceed/Proceed]? [Definitely!/Not yet.]
- **16655**: Entering $8.
- **16656**: You have chosen not to [apply to/enter] $8.
- **16668**: You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party.
- **16669**: Treasure chest bonuses are now active!
- **16675**: Applying to enter $8. You will be unable to participate if you add any more party members. Are you sure?
- **16678**: You are currently number $3 in line to be drawn into this nightmare.
- **16679**: You are currently number $3 in line, with $2 in front of you.
- **16680**: Prepare yourselves! The battlefield is almost ready!
- **16681**: You are currently applying to enter $8.
- **16682**: Your number: $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]
- **16693**: Your $3 fills with sand.
- **16696**: Enter by :: on //.
- **16702**: Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Testing./Jump./Close dialogue.]
- **16711**: Designate a value between $0 and $1.

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

### Event 655

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 353 bytes |
| Instructions | 67        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 07 00 02 10 03  04 00 03 10 03 12 00 04   B..............
0010: 10 03 0B 00 06 10 03 0E  00 07 10 03 0F 00 08 10  ................
0020: 03 11 00 09 10 05 08 00  03 02 00 00 80 03 03 00  ................
0030: 00 80 03 01 00 00 80 03  02 10 0F 00 03 04 10 01  ................
0040: 80 3E 0E 00 00 80 50 00  03 07 10 02 80 01 55 00  .>....P.......U.
0050: 03 07 10 00 80 3E 0E 00  02 80 64 00 03 08 10 02  .....>....d.....
0060: 80 01 69 00 03 08 10 00  80 3E 0E 00 03 80 70 00  ..i......>....p.
0070: 24 04 80 00 80 07 00 25  02 00 10 02 80 00 9E 00  $......%........
0080: 02 12 00 00 80 00 90 00  03 02 00 02 80 01 9B 00  ................
0090: 03 02 10 12 00 48 05 80  23 21 00 01 F6 00 02 00  .....H..#!......
00A0: 10 03 80 00 B9 00 03 01  10 00 80 40 06 80 07 80  ...........@....
00B0: 01 10 08 80 21 00 01 F6  00 02 00 10 08 80 00 D4  ....!...........
00C0: 00 03 01 10 00 80 40 06  80 07 80 01 10 03 80 21  ......@........!
00D0: 00 01 F6 00 02 00 10 09  80 00 EF 00 03 01 10 00  ................
00E0: 80 40 06 80 07 80 01 10  02 80 21 00 01 F6 00 03  .@........!.....
00F0: 01 10 0A 80 21 00 03 01  00 02 00 02 11 00 00 80  ....!...........
0100: 01 06 01 48 0B 80 03 06  10 0B 00 48 0C 80 03 02  ...H.......H....
0110: 10 0F 00 48 0D 80 23 03  03 10 00 80 24 0E 80 00  ...H..#.....$...
0120: 80 00 80 25 02 00 10 00  80 00 4C 01 03 01 10 00  ...%......L.....
0130: 80 40 00 80 0F 80 01 10  01 00 43 00 43 01 02 09  .@........C.C...
0140: 10 00 80 01 49 01 01 06  01 01 60 01 03 02 10 0F  ....I.....`.....
0150: 00 03 03 10 00 80 48 10  80 03 01 10 0A 80 21 00  ......H.......!.
0160: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[2]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[3]
  3: 0x000C [0x03] ExtData[1]->WorkLocal[18] = Work_Zone[4]
  4: 0x0011 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[6]
  5: 0x0016 [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[7]
  6: 0x001B [0x03] ExtData[1]->WorkLocal[15] = Work_Zone[8]
  7: 0x0020 [0x03] ExtData[1]->WorkLocal[17] = Work_Zone[9]
  8: 0x0025 [0x05] ExtData[1]->WorkLocal[8] = 1
  9: 0x0028 [0x03] ExtData[1]->WorkLocal[2] = 0*
 10: 0x002D [0x03] ExtData[1]->WorkLocal[3] = 0*
 11: 0x0032 [0x03] ExtData[1]->WorkLocal[1] = 0*
 12: 0x0037 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[15]
 13: 0x003C [0x03] Work_Zone[4] = 3156*
 14: 0x0041 [0x3E] IF !(ExtData[1]->WorkLocal[14] bit 0*) GOTO 0x0050
 15: 0x0048 [0x03] Work_Zone[7] = 1*
 16: 0x004D [0x01] GOTO 0x0055
 17: 0x0050 [0x03] Work_Zone[7] = 0*

SUBROUTINE_0055:
 18: 0x0055 [0x3E] IF !(ExtData[1]->WorkLocal[14] bit 1*) GOTO 0x0064
 19: 0x005C [0x03] Work_Zone[8] = 1*
 20: 0x0061 [0x01] GOTO 0x0069
 21: 0x0064 [0x03] Work_Zone[8] = 0*

SUBROUTINE_0069:
 22: 0x0069 [0x3E] IF !(ExtData[1]->WorkLocal[14] bit 2*) GOTO 0x0070
 23: 0x0070 [0x24] CREATE_DIALOG(message_id=16651*, default_option=0*, option_flags=ExtData[1]->WorkLocal[7])
    → "Attempt which? (Auto-transport: [off/on]) [None./$8. (CL: $1)/$3 status./Switch $3 use state. ([off/on])/Toggle auto-transport.]"
 24: 0x0077 [0x25] WAIT_DIALOG_SELECT()
 25: 0x0078 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x009E
 26: 0x0080 [0x02] IF !(ExtData[1]->WorkLocal[18] == 0*) GOTO 0x0090
 27: 0x0088 [0x03] ExtData[1]->WorkLocal[2] = 1*
 28: 0x008D [0x01] GOTO 0x009B
 29: 0x0090 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[18]
 30: 0x0095 [0x48] [System] [16696*]:
    → "Enter by :: on //."
 31: 0x0098 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0099 [0x21] END_EVENT
 33: 0x009A [0x00] END_REQSTACK()

SUBROUTINE_009B:
 34: 0x009B [0x01] GOTO 0x00F6
 35: 0x009E [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00B9
 36: 0x00A6 [0x03] Work_Zone[1] = 0*
 37: 0x00AB [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=3*)
 38: 0x00B4 [0x21] END_EVENT
 39: 0x00B5 [0x00] END_REQSTACK()

SUBROUTINE_00F6:
 40: 0x00F6 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[2]
 41: 0x00FB [0x02] IF !(ExtData[1]->WorkLocal[17] == 0*) GOTO 0x0106
 42: 0x0103 [0x48] [System] [16669*]:
    → "Treasure chest bonuses are now active!"

SUBROUTINE_0106:
 43: 0x0106 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[11]
 44: 0x010B [0x48] [System] [16668*]:
    → "You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party."
 45: 0x010E [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[15]
 46: 0x0113 [0x48] [System] [16675*]:
    → "Applying to enter $8. You will be unable to participate if you add any more party members. Are you sure?"
 47: 0x0116 [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x0117 [0x03] Work_Zone[3] = 0*
 49: 0x011C [0x24] CREATE_DIALOG(message_id=16654*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Definitely!/Not yet.]"
 50: 0x0123 [0x25] WAIT_DIALOG_SELECT()
 51: 0x0124 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x014C
 52: 0x012C [0x03] Work_Zone[1] = 0*
 53: 0x0131 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 54: 0x013A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 55: 0x013C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 56: 0x013E [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x0149
 57: 0x0146 [0x01] GOTO 0x0106
 58: 0x0149 [0x01] GOTO 0x0160
 59: 0x014C [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[15]
 60: 0x0151 [0x03] Work_Zone[3] = 0*
 61: 0x0156 [0x48] [System] [16656*]:
    → "You have chosen not to [apply to/enter] $8."
 62: 0x0159 [0x03] Work_Zone[1] = 1073741824*
 63: 0x015E [0x21] END_EVENT
 64: 0x015F [0x00] END_REQSTACK()

SUBROUTINE_0160:
 65: 0x0160 [0x21] END_EVENT
 66: 0x0161 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00B6 [0x01] GOTO 0x00F6
     0x00D1 [0x01] GOTO 0x00F6
     0x00EC [0x01] GOTO 0x00F6
```

### Event 658

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0162   |
| Data Size    | 94 bytes |
| Instructions | 24       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:       02 04 10 00 80 02  71 01 48 11 80 23 01 75    ......q.H..#.u
0170: 01 48 12 80 23 48 13 80  23 02 03 10 00 80 00 8C  .H..#H..#.......
0180: 01 48 14 80 03 01 10 0A  80 01 BE 01 03 02 10 02  .H..............
0190: 80 24 15 80 02 80 00 80  25 02 00 10 00 80 00 A9  .$......%.......
01A0: 01 03 01 10 02 80 01 BE  01 02 00 10 02 80 00 B9  ................
01B0: 01 03 01 10 03 80 01 BE  01 03 01 10 0A 80 21 00  ..............!.
```

#### Opcodes

```
  0: 0x0162 [0x02] IF !(Work_Zone[4] <= 0*) GOTO 0x0171
  1: 0x016A [0x48] [System] [16679*]:
    → "You are currently number $3 in line, with $2 in front of you."
  2: 0x016D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x016E [0x01] GOTO 0x0175
  4: 0x0171 [0x48] [System] [16681*]:
    → "You are currently applying to enter $8."
  5: 0x0174 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0175:
  6: 0x0175 [0x48] [System] [16678*]:
    → "You are currently number $3 in line to be drawn into this nightmare."
  7: 0x0178 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0179 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x018C
  9: 0x0181 [0x48] [System] [16680*]:
    → "Prepare yourselves! The battlefield is almost ready!"
 10: 0x0184 [0x03] Work_Zone[1] = 1073741824*
 11: 0x0189 [0x01] GOTO 0x01BE
 12: 0x018C [0x03] Work_Zone[2] = 1*
 13: 0x0191 [0x24] CREATE_DIALOG(message_id=16682*, default_option=1*, option_flags=0*)
    → "Your number: $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]"
 14: 0x0198 [0x25] WAIT_DIALOG_SELECT()
 15: 0x0199 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01A9
 16: 0x01A1 [0x03] Work_Zone[1] = 1*
 17: 0x01A6 [0x01] GOTO 0x01BE
 18: 0x01A9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01B9
 19: 0x01B1 [0x03] Work_Zone[1] = 2*
 20: 0x01B6 [0x01] GOTO 0x01BE
 21: 0x01B9 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_01BE:
 22: 0x01BE [0x21] END_EVENT
 23: 0x01BF [0x00] END_REQSTACK()
```

### Event 659

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C0   |
| Data Size    | 97 bytes |
| Instructions | 27       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: 42 03 0F 00 02 10 03 10  00 04 10 48 16 80 23 03  B..........H..#.
01D0: 03 10 02 80 24 0E 80 00  80 00 80 25 02 00 10 00  ....$......%....
01E0: 80 00 1A 02 03 01 10 02  80 43 00 43 01 02 09 10  .........C.C....
01F0: 00 80 00 12 02 03 02 10  0F 00 48 17 80 23 03 04  ..........H..#..
0200: 10 10 00 48 18 80 23 1A  B0 03 03 01 10 03 80 01  ...H..#.........
0210: 17 02 03 01 10 0A 80 01  1F 02 03 01 10 0A 80 21  ...............!
0220: 00                                                .               
```

#### Opcodes

```
  0: 0x01C0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01C1 [0x03] ExtData[1]->WorkLocal[15] = Work_Zone[2]
  2: 0x01C6 [0x03] ExtData[1]->WorkLocal[16] = Work_Zone[4]
  3: 0x01CB [0x48] [System] [16653*]:
    → "Only party members present with you in this area will be transported to $8."
  4: 0x01CE [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x01CF [0x03] Work_Zone[3] = 1*
  6: 0x01D4 [0x24] CREATE_DIALOG(message_id=16654*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Definitely!/Not yet.]"
  7: 0x01DB [0x25] WAIT_DIALOG_SELECT()
  8: 0x01DC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x021A
  9: 0x01E4 [0x03] Work_Zone[1] = 1*
 10: 0x01E9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x01EB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x01ED [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x0212
 13: 0x01F5 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[15]
 14: 0x01FA [0x48] [System] [16655*]:
    → "Entering $8."
 15: 0x01FD [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x01FE [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[16]
 17: 0x0203 [0x48] [System] [16693*]:
    → "Your $3 fills with sand."
 18: 0x0206 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0207 [0x1A] CALL_SUBROUTINE(address=0x03B0)
 20: 0x020A [0x03] Work_Zone[1] = 2*
 21: 0x020F [0x01] GOTO 0x0217
 22: 0x0212 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_0217:
 23: 0x0217 [0x01] GOTO 0x021F
 24: 0x021A [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_021F:
 25: 0x021F [0x21] END_EVENT
 26: 0x0220 [0x00] END_REQSTACK()
```

### Event 690

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0221    |
| Data Size    | 147 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:    03 04 10 01 80 03 0E  00 07 10 3E 0E 00 00 80   ..........>....
0230: 3A 02 03 07 10 02 80 01  3F 02 03 07 10 00 80 3E  :.......?......>
0240: 0E 00 02 80 4E 02 03 08  10 02 80 01 53 02 03 08  ....N.......S...
0250: 10 00 80 3E 0E 00 03 80  5A 02 24 19 80 00 80 07  ...>....Z.$.....
0260: 00 25 02 00 10 02 80 00  7B 02 03 01 10 00 80 40  .%......{......@
0270: 06 80 07 80 01 10 08 80  01 B2 02 02 00 10 03 80  ................
0280: 00 94 02 03 01 10 00 80  40 06 80 07 80 01 10 03  ........@.......
0290: 80 01 B2 02 02 00 10 08  80 00 AD 02 03 01 10 00  ................
02A0: 80 40 06 80 07 80 01 10  02 80 01 B2 02 03 01 10  .@..............
02B0: 0A 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0221 [0x03] Work_Zone[4] = 3156*
  1: 0x0226 [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[7]
  2: 0x022B [0x3E] IF !(ExtData[1]->WorkLocal[14] bit 0*) GOTO 0x023A
  3: 0x0232 [0x03] Work_Zone[7] = 1*
  4: 0x0237 [0x01] GOTO 0x023F
  5: 0x023A [0x03] Work_Zone[7] = 0*

SUBROUTINE_023F:
  6: 0x023F [0x3E] IF !(ExtData[1]->WorkLocal[14] bit 1*) GOTO 0x024E
  7: 0x0246 [0x03] Work_Zone[8] = 1*
  8: 0x024B [0x01] GOTO 0x0253
  9: 0x024E [0x03] Work_Zone[8] = 0*

SUBROUTINE_0253:
 10: 0x0253 [0x3E] IF !(ExtData[1]->WorkLocal[14] bit 2*) GOTO 0x025A
 11: 0x025A [0x24] CREATE_DIALOG(message_id=16652*, default_option=0*, option_flags=ExtData[1]->WorkLocal[7])
    → "Instance Setting (Auto-transport: ([off/on]) [Back./$3 status./Switch $3 use state. ([off/on])/Toggle auto-transport.]"
 12: 0x0261 [0x25] WAIT_DIALOG_SELECT()
 13: 0x0262 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x027B
 14: 0x026A [0x03] Work_Zone[1] = 0*
 15: 0x026F [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=3*)
 16: 0x0278 [0x01] GOTO 0x02B2
 17: 0x027B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0294
 18: 0x0283 [0x03] Work_Zone[1] = 0*
 19: 0x0288 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=2*)
 20: 0x0291 [0x01] GOTO 0x02B2
 21: 0x0294 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x02AD
 22: 0x029C [0x03] Work_Zone[1] = 0*
 23: 0x02A1 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=1*)
 24: 0x02AA [0x01] GOTO 0x02B2
 25: 0x02AD [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_02B2:
 26: 0x02B2 [0x21] END_EVENT
 27: 0x02B3 [0x00] END_REQSTACK()
```

### Event 660

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02B4    |
| Data Size    | 361 bytes |
| Instructions | 58        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:             05 0A 00 02  0A 00 02 80 00 AE 03 24      ...........$
02C0: 1A 80 00 80 00 80 25 02  00 10 00 80 00 DB 02 03  ......%.........
02D0: 01 10 02 80 43 00 43 01  01 AB 03 02 00 10 02 80  ....C.C.........
02E0: 00 EF 02 03 01 10 03 80  43 00 43 01 01 AB 03 02  ........C.C.....
02F0: 00 10 03 80 00 23 03 03  02 10 02 80 03 03 10 1B  .....#..........
0300: 80 48 1C 80 71 12 02 80  03 80 71 13 00 00 03 01  .H..q.....q.....
0310: 10 08 80 40 1D 80 1E 80  01 10 00 00 43 00 43 01  ...@........C.C.
0320: 01 AB 03 02 00 10 08 80  00 57 03 03 02 10 02 80  .........W......
0330: 03 03 10 1B 80 48 1C 80  71 12 02 80 03 80 71 13  .....H..q.....q.
0340: 00 00 03 01 10 09 80 40  1D 80 1E 80 01 10 00 00  .......@........
0350: 43 00 43 01 01 AB 03 02  00 10 09 80 00 6B 03 03  C.C..........k..
0360: 01 10 1F 80 43 00 43 01  01 AB 03 02 00 10 1F 80  ....C.C.........
0370: 00 95 03 48 1C 80 71 12  02 80 03 80 71 13 00 00  ...H..q.....q...
0380: 03 01 10 20 80 40 1D 80  1E 80 01 10 00 00 43 00  ... .@........C.
0390: 43 01 01 AB 03 02 00 10  20 80 00 A8 03 03 01 10  C....... .......
03A0: 02 80 06 0A 00 01 AB 03  06 0A 00 01 B7 02 21 00  ..............!.
03B0: 62 02 80 F0 FF FF 7F F0  FF FF 7F 6D 61 69 6E 00  b..........main.
03C0: 80 1C 21 80 45 22 80 F0  FF FF 7F F0 FF FF 7F 77  ..!.E".........w
03D0: 68 6F 31 00 80 55 22 80  F0 FF FF 7F F0 FF FF 7F  ho1..U".........
03E0: 77 68 6F 31 1C 23 80 45  24 80 F0 FF FF 7F F0 FF  who1.#.E$.......
03F0: FF 7F 66 64 6F 31 00 80  55 24 80 F0 FF FF 7F F0  ..fdo1..U$......
0400: FF FF 7F 66 64 6F 31 45  22 80 F0 FF FF 7F F0 FF  ...fdo1E".......
0410: FF 7F 77 68 69 31 00 80  1C 1E 80 30 1B           ..whi1.....0.   
```

#### Opcodes

```
  0: 0x02B4 [0x05] ExtData[1]->WorkLocal[10] = 1
  1: 0x02B7 [0x02] IF !(ExtData[1]->WorkLocal[10] == 1*) GOTO 0x03AE
  2: 0x02BF [0x24] CREATE_DIALOG(message_id=16702*, default_option=0*, option_flags=0*)
    → "Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Testing./Jump./Close dialogue.]"
  3: 0x02C6 [0x25] WAIT_DIALOG_SELECT()
  4: 0x02C7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02DB
  5: 0x02CF [0x03] Work_Zone[1] = 1*
  6: 0x02D4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x02D6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x02D8 [0x01] GOTO 0x03AB
  9: 0x02DB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02EF
 10: 0x02E3 [0x03] Work_Zone[1] = 2*
 11: 0x02E8 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x02EA [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x02EC [0x01] GOTO 0x03AB
 14: 0x02EF [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0323
 15: 0x02F7 [0x03] Work_Zone[2] = 1*
 16: 0x02FC [0x03] Work_Zone[3] = 50*
 17: 0x0301 [0x48] [System] [16711*]:
    → "Designate a value between $0 and $1."
 18: 0x0304 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 19: 0x030A [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 20: 0x030E [0x03] Work_Zone[1] = 3*
 21: 0x0313 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 22: 0x031C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 23: 0x031E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 24: 0x0320 [0x01] GOTO 0x03AB
 25: 0x0323 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0357
 26: 0x032B [0x03] Work_Zone[2] = 1*
 27: 0x0330 [0x03] Work_Zone[3] = 50*
 28: 0x0335 [0x48] [System] [16711*]:
    → "Designate a value between $0 and $1."
 29: 0x0338 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 30: 0x033E [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 31: 0x0342 [0x03] Work_Zone[1] = 4*
 32: 0x0347 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 33: 0x0350 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 34: 0x0352 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 35: 0x0354 [0x01] GOTO 0x03AB
 36: 0x0357 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x036B
 37: 0x035F [0x03] Work_Zone[1] = 5*
 38: 0x0364 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 39: 0x0366 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 40: 0x0368 [0x01] GOTO 0x03AB
 41: 0x036B [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0395
 42: 0x0373 [0x48] [System] [16711*]:
    → "Designate a value between $0 and $1."
 43: 0x0376 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 44: 0x037C [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 45: 0x0380 [0x03] Work_Zone[1] = 6*
 46: 0x0385 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 47: 0x038E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 48: 0x0390 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 49: 0x0392 [0x01] GOTO 0x03AB
 50: 0x0395 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x03A8
 51: 0x039D [0x03] Work_Zone[1] = 1*
 52: 0x03A2 [0x06] ExtData[1]->WorkLocal[10] = 0
 53: 0x03A5 [0x01] GOTO 0x03AB
 54: 0x03A8 [0x06] ExtData[1]->WorkLocal[10] = 0

SUBROUTINE_03AB:
 55: 0x03AB [0x01] GOTO 0x02B7
 56: 0x03AE [0x21] END_EVENT
 57: 0x03AF [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x03B0 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x03C1 [0x1C] WAIT(90* ticks)
     0x03C4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x03D5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x03E4 [0x1C] WAIT(45* ticks)
     0x03E7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03F8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0407 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0418 [0x1C] WAIT(15* ticks)
     0x041B [0x30] SET_UCOFF_CONTINUE_ZERO()
     0x041C [0x1B] RETURN
```
