# 17797271 - Ambuscade Tome

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 1144 bytes       |
| Total Events     | 5                |
| References Count | 35               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [374](#event-374)     | 0x0001       |    435 |             94 |
| [377](#event-377)     | 0x01B4       |     95 |             25 |
| [378](#event-378)     | 0x0213       |     83 |             23 |
| [379](#event-379)     | 0x0266       |    352 |             67 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x1F9A      |        8090 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |
|       6 | 0x0018      |          24 |
|       7 | 0x001F      |          31 |
|       8 | 0x40000000  |  1073741824 |
|       9 | 0x000F      |          15 |
|      10 | 0x000A      |          10 |
|      11 | 0x0005      |           5 |
|      12 | 0x1F9B      |        8091 |
|      13 | 0x000B      |          11 |
|      14 | 0x1FAA      |        8106 |
|      15 | 0x1FAF      |        8111 |
|      16 | 0x1F9D      |        8093 |
|      17 | 0x1F9F      |        8095 |
|      18 | 0x1FB3      |        8115 |
|      19 | 0x1FB5      |        8117 |
|      20 | 0x1FB2      |        8114 |
|      21 | 0x1FB4      |        8116 |
|      22 | 0x1FB6      |        8118 |
|      23 | 0x1F9C      |        8092 |
|      24 | 0x1F9E      |        8094 |
|      25 | 0x1FC1      |        8129 |
|      26 | 0x0032      |          50 |
|      27 | 0x1FCA      |        8138 |
|      28 | 0x0008      |           8 |
|      29 | 0x0011      |          17 |
|      30 | 0x0006      |           6 |
|      31 | 0x005A      |          90 |
|      32 | 0x00C9      |         201 |
|      33 | 0x002D      |          45 |
|      34 | 0x00C8      |         200 |

## String References

- **8090**: Pick your poison. (Auto-transport: [off/on]) [No Ambuscade for now./Intense Ambuscade./Regular Ambuscade./Light Ambuscade./Toggle auto-transport.]
- **8091**: Select a difficulty level. [Go back./Very difficult. (Level: ???)/Difficult. (Level: $10)/Normal. (Level: $11)/Easy. (Level: $12)/Very easy. (Level: $13)]
- **8092**: Only party members present with you in this area will be transported to the [/Very Difficult Intense Ambuscade/Difficult Intense Ambuscade/Normal Intense Ambuscade/Easy Intense Ambuscade/Very Easy Intense Ambuscade/Very Difficult Ambuscade/Difficult Ambuscade/Normal Ambuscade/Easy Ambuscade/Very Easy Ambuscade/Light Ambuscade].
- **8093**: [Apply to proceed/Proceed]? [Most certainly!/Not yet.]
- **8094**: Entering the [/Very Difficult Intense Ambuscade/Difficult Intense Ambuscade/Normal Intense Ambuscade/Easy Intense Ambuscade/Very Easy Intense Ambuscade/Very Difficult Ambuscade/Difficult Ambuscade/Normal Ambuscade/Easy Ambuscade/Very Easy Ambuscade/Light Ambuscade].
- **8095**: You have chosen not to [apply to /]enter the [/Very Difficult Intense Ambuscade/Difficult Intense Ambuscade/Normal Intense Ambuscade/Easy Intense Ambuscade/Very Easy Intense Ambuscade/Very Difficult Ambuscade/Difficult Ambuscade/Normal Ambuscade/Easy Ambuscade/Very Easy Ambuscade/Light Ambuscade].
- **8106**: You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party.
- **8111**: Applying to enter [/a Very Difficult Intense Ambuscade/a Difficult Intense Ambuscade/a Normal Intense Ambuscade/an Easy Intense Ambuscade/a Very Easy Intense Ambuscade/a Very Difficult Ambuscade/a Difficult Ambuscade/a Normal Ambuscade/an Easy Ambuscade/a Very Easy Ambuscade/a Light Ambuscade]. You will be unable to participate if you add any more party members. Are you sure?
- **8114**: Your name is inscribed in page $3 of the Ambuscade tome.
- **8115**: Names are inscribed up through page $3 of the Ambuscade tome. Page $2 beams with a fierce light.
- **8116**: Prepare yourselves! The battlefield is almost ready!
- **8117**: You are currently applying to enter [/a Very Difficult Intense Ambuscade/a Difficult Intense Ambuscade/a Normal Intense Ambuscade/an Easy Intense Ambuscade/a Very Easy Intense Ambuscade/a Very Difficult Ambuscade/a Difficult Ambuscade/a Normal Ambuscade/an Easy Ambuscade/a Very Easy Ambuscade/a Light Ambuscade].
- **8118**: You are on page $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]
- **8129**: Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Dummy Entrance People./Close dialogue.]
- **8138**: Designate a value between $0 and $1.

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

### Event 374

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 435 bytes |
| Instructions | 90        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 07 00 02 10 03  05 00 03 10 03 06 00 04   B..............
0010: 10 03 0B 00 06 10 03 0E  00 07 10 05 08 00 02 08  ................
0020: 00 00 80 00 58 01 03 02  00 01 80 03 03 00 01 80  ....X...........
0030: 03 01 00 01 80 03 04 00  01 80 24 02 80 01 80 07  ..........$.....
0040: 00 25 02 00 10 00 80 00  57 00 03 02 00 00 80 03  .%......W.......
0050: 04 00 05 00 01 A3 00 02  00 10 03 80 00 6C 00 03  .............l..
0060: 02 00 03 80 03 04 00 06  00 01 A3 00 02 00 10 04  ................
0070: 80 00 81 00 03 02 00 04  80 03 03 00 00 80 01 A3  ................
0080: 00 02 00 10 05 80 00 9C  00 03 01 10 01 80 40 06  ..............@.
0090: 80 07 80 01 10 00 80 21  00 01 A3 00 03 01 10 08  .......!........
00A0: 80 21 00 03 02 17 04 00  03 03 17 04 00 03 04 17  .!..............
00B0: 04 00 03 05 17 04 00 07  02 17 09 80 07 03 17 0A  ................
00C0: 80 07 04 17 0B 80 07 05  17 01 80 02 03 00 01 80  ................
00D0: 00 30 01 24 0C 80 01 80  01 80 25 02 00 10 00 80  .0.$......%.....
00E0: 00 EB 00 03 03 00 00 80  01 30 01 02 00 10 03 80  .........0......
00F0: 00 FB 00 03 03 00 03 80  01 30 01 02 00 10 04 80  .........0......
0100: 00 0B 01 03 03 00 04 80  01 30 01 02 00 10 05 80  .........0......
0110: 00 1B 01 03 03 00 05 80  01 30 01 02 00 10 0B 80  .........0......
0120: 00 2B 01 03 03 00 0B 80  01 30 01 03 02 00 01 80  .+.......0......
0130: 03 01 00 02 00 0C 01 00  14 01 00 0B 80 07 01 00  ................
0140: 03 00 02 01 00 00 80 04  55 01 02 01 00 0D 80 05  ........U.......
0150: 55 01 06 08 00 01 1E 00  03 06 10 0B 00 48 0E 80  U............H..
0160: 03 02 10 01 00 48 0F 80  23 03 03 10 01 80 24 10  .....H..#.....$.
0170: 80 01 80 01 80 25 02 00  10 01 80 00 9E 01 03 01  .....%..........
0180: 10 01 80 40 01 80 0D 80  01 10 01 00 43 00 43 01  ...@........C.C.
0190: 02 09 10 01 80 01 9B 01  01 58 01 01 B2 01 03 02  .........X......
01A0: 10 01 00 03 03 10 01 80  48 11 80 03 01 10 08 80  ........H.......
01B0: 21 00 21 00                                       !.!.            
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[2]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[3]
  3: 0x000C [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[4]
  4: 0x0011 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[6]
  5: 0x0016 [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[7]
  6: 0x001B [0x05] ExtData[1]->WorkLocal[8] = 1
  7: 0x001E [0x02] IF !(ExtData[1]->WorkLocal[8] == 1*) GOTO 0x0158
  8: 0x0026 [0x03] ExtData[1]->WorkLocal[2] = 0*
  9: 0x002B [0x03] ExtData[1]->WorkLocal[3] = 0*
 10: 0x0030 [0x03] ExtData[1]->WorkLocal[1] = 0*
 11: 0x0035 [0x03] ExtData[1]->WorkLocal[4] = 0*
 12: 0x003A [0x24] CREATE_DIALOG(message_id=8090*, default_option=0*, option_flags=ExtData[1]->WorkLocal[7])
    → "Pick your poison. (Auto-transport: [off/on]) [No Ambuscade for now./Intense Ambuscade./Regular Ambuscade./Light Ambuscade./Toggle auto-transport.]"
 13: 0x0041 [0x25] WAIT_DIALOG_SELECT()
 14: 0x0042 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0057
 15: 0x004A [0x03] ExtData[1]->WorkLocal[2] = 1*
 16: 0x004F [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->WorkLocal[5]
 17: 0x0054 [0x01] GOTO 0x00A3
 18: 0x0057 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x006C
 19: 0x005F [0x03] ExtData[1]->WorkLocal[2] = 2*
 20: 0x0064 [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->WorkLocal[6]
 21: 0x0069 [0x01] GOTO 0x00A3
 22: 0x006C [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0081
 23: 0x0074 [0x03] ExtData[1]->WorkLocal[2] = 3*
 24: 0x0079 [0x03] ExtData[1]->WorkLocal[3] = 1*
 25: 0x007E [0x01] GOTO 0x00A3
 26: 0x0081 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x009C
 27: 0x0089 [0x03] Work_Zone[1] = 0*
 28: 0x008E [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=1*)
 29: 0x0097 [0x21] END_EVENT
 30: 0x0098 [0x00] END_REQSTACK()

SUBROUTINE_00A3:
 31: 0x00A3 [0x03] Work_Zone_1700[2] = ExtData[1]->WorkLocal[4]
 32: 0x00A8 [0x03] Work_Zone_1700[3] = ExtData[1]->WorkLocal[4]
 33: 0x00AD [0x03] Work_Zone_1700[4] = ExtData[1]->WorkLocal[4]
 34: 0x00B2 [0x03] Work_Zone_1700[5] = ExtData[1]->WorkLocal[4]
 35: 0x00B7 [0x07] Work_Zone_1700[2] += 15*
 36: 0x00BC [0x07] Work_Zone_1700[3] += 10*
 37: 0x00C1 [0x07] Work_Zone_1700[4] += 5*
 38: 0x00C6 [0x07] Work_Zone_1700[5] += 0*
 39: 0x00CB [0x02] IF !(ExtData[1]->WorkLocal[3] == 0*) GOTO 0x0130
 40: 0x00D3 [0x24] CREATE_DIALOG(message_id=8091*, default_option=0*, option_flags=0*)
    → "Select a difficulty level. [Go back./Very difficult. (Level: ???)/Difficult. (Level: $10)/Normal. (Level: $11)/Easy. (Level: $12)/Very easy. (Level: $13)]"
 41: 0x00DA [0x25] WAIT_DIALOG_SELECT()
 42: 0x00DB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00EB
 43: 0x00E3 [0x03] ExtData[1]->WorkLocal[3] = 1*
 44: 0x00E8 [0x01] GOTO 0x0130
 45: 0x00EB [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00FB
 46: 0x00F3 [0x03] ExtData[1]->WorkLocal[3] = 2*
 47: 0x00F8 [0x01] GOTO 0x0130
 48: 0x00FB [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x010B
 49: 0x0103 [0x03] ExtData[1]->WorkLocal[3] = 3*
 50: 0x0108 [0x01] GOTO 0x0130
 51: 0x010B [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x011B
 52: 0x0113 [0x03] ExtData[1]->WorkLocal[3] = 4*
 53: 0x0118 [0x01] GOTO 0x0130
 54: 0x011B [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x012B
 55: 0x0123 [0x03] ExtData[1]->WorkLocal[3] = 5*
 56: 0x0128 [0x01] GOTO 0x0130
 57: 0x012B [0x03] ExtData[1]->WorkLocal[2] = 0*

SUBROUTINE_0130:
 58: 0x0130 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[2]
 59: 0x0135 [0x0C] ExtData[1]->WorkLocal[1]--
 60: 0x0138 [0x14] ExtData[1]->WorkLocal[1] *= 5*
 61: 0x013D [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[3]
 62: 0x0142 [0x02] IF !(ExtData[1]->WorkLocal[1] < 1*) GOTO 0x0155
 63: 0x014A [0x02] IF !(ExtData[1]->WorkLocal[1] > 11*) GOTO 0x0155
 64: 0x0152 [0x06] ExtData[1]->WorkLocal[8] = 0
 65: 0x0155 [0x01] GOTO 0x001E

SUBROUTINE_0158:
 66: 0x0158 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[11]
 67: 0x015D [0x48] [System] [8106*]:
    → "You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party."
 68: 0x0160 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 69: 0x0165 [0x48] [System] [8111*]:
    → "Applying to enter [/a Very Difficult Intense Ambuscade/a Difficult Intense Ambuscade/a Normal Intense Ambuscade/an Easy Intense Ambuscade/a Very Easy Intense Ambuscade/a Very Difficult Ambuscade/a Difficult Ambuscade/a Normal Ambuscade/an Easy Ambuscade/a Very Easy Ambuscade/a Light Ambuscade]. You will be unable to participate if you add any more party members. Are you sure?"
 70: 0x0168 [0x23] WAIT_FOR_DIALOG_INTERACTION
 71: 0x0169 [0x03] Work_Zone[3] = 0*
 72: 0x016E [0x24] CREATE_DIALOG(message_id=8093*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Most certainly!/Not yet.]"
 73: 0x0175 [0x25] WAIT_DIALOG_SELECT()
 74: 0x0176 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x019E
 75: 0x017E [0x03] Work_Zone[1] = 0*
 76: 0x0183 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 77: 0x018C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 78: 0x018E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 79: 0x0190 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x019B
 80: 0x0198 [0x01] GOTO 0x0158
 81: 0x019B [0x01] GOTO 0x01B2
 82: 0x019E [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 83: 0x01A3 [0x03] Work_Zone[3] = 0*
 84: 0x01A8 [0x48] [System] [8095*]:
    → "You have chosen not to [apply to /]enter the [/Very Difficult Intense Ambuscade/Difficult Intense Ambuscade/Normal Intense Ambuscade/Easy Intense Ambuscade/Very Easy Intense Ambuscade/Very Difficult Ambuscade/Difficult Ambuscade/Normal Ambuscade/Easy Ambuscade/Very Easy Ambuscade/Light Ambuscade]."
 85: 0x01AB [0x03] Work_Zone[1] = 1073741824*
 86: 0x01B0 [0x21] END_EVENT
 87: 0x01B1 [0x00] END_REQSTACK()

SUBROUTINE_01B2:
 88: 0x01B2 [0x21] END_EVENT
 89: 0x01B3 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0099 [0x01] GOTO 0x00A3
```

### Event 377

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B4   |
| Data Size    | 95 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:             02 04 10 01  80 02 C3 01 48 12 80 23      ........H..#
01C0: 01 C7 01 48 13 80 23 48  14 80 23 02 03 10 01 80  ...H..#H..#.....
01D0: 00 DF 01 48 15 80 23 03  01 10 08 80 01 11 02 03  ...H..#.........
01E0: 02 10 00 80 24 16 80 00  80 01 80 25 02 00 10 01  ....$......%....
01F0: 80 00 FC 01 03 01 10 00  80 01 11 02 02 00 10 00  ................
0200: 80 00 0C 02 03 01 10 03  80 01 11 02 03 01 10 08  ................
0210: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x01B4 [0x02] IF !(Work_Zone[4] <= 0*) GOTO 0x01C3
  1: 0x01BC [0x48] [System] [8115*]:
    → "Names are inscribed up through page $3 of the Ambuscade tome. Page $2 beams with a fierce light."
  2: 0x01BF [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01C0 [0x01] GOTO 0x01C7
  4: 0x01C3 [0x48] [System] [8117*]:
    → "You are currently applying to enter [/a Very Difficult Intense Ambuscade/a Difficult Intense Ambuscade/a Normal Intense Ambuscade/an Easy Intense Ambuscade/a Very Easy Intense Ambuscade/a Very Difficult Ambuscade/a Difficult Ambuscade/a Normal Ambuscade/an Easy Ambuscade/a Very Easy Ambuscade/a Light Ambuscade]."
  5: 0x01C6 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_01C7:
  6: 0x01C7 [0x48] [System] [8114*]:
    → "Your name is inscribed in page $3 of the Ambuscade tome."
  7: 0x01CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x01CB [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x01DF
  9: 0x01D3 [0x48] [System] [8116*]:
    → "Prepare yourselves! The battlefield is almost ready!"
 10: 0x01D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x01D7 [0x03] Work_Zone[1] = 1073741824*
 12: 0x01DC [0x01] GOTO 0x0211
 13: 0x01DF [0x03] Work_Zone[2] = 1*
 14: 0x01E4 [0x24] CREATE_DIALOG(message_id=8118*, default_option=1*, option_flags=0*)
    → "You are on page $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]"
 15: 0x01EB [0x25] WAIT_DIALOG_SELECT()
 16: 0x01EC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01FC
 17: 0x01F4 [0x03] Work_Zone[1] = 1*
 18: 0x01F9 [0x01] GOTO 0x0211
 19: 0x01FC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x020C
 20: 0x0204 [0x03] Work_Zone[1] = 2*
 21: 0x0209 [0x01] GOTO 0x0211
 22: 0x020C [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_0211:
 23: 0x0211 [0x21] END_EVENT
 24: 0x0212 [0x00] END_REQSTACK()
```

### Event 378

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0213   |
| Data Size    | 83 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:          42 03 01 00 02  10 48 17 80 23 03 03 10     B.....H..#...
0220: 00 80 24 10 80 01 80 01  80 25 02 00 10 01 80 00  ..$......%......
0230: 5F 02 03 01 10 00 80 43  00 43 01 02 09 10 01 80  _......C.C......
0240: 00 57 02 03 02 10 01 00  48 18 80 23 1A 59 03 03  .W......H..#.Y..
0250: 01 10 03 80 01 5C 02 03  01 10 08 80 01 64 02 03  .....\.......d..
0260: 01 10 08 80 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x0213 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0214 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
  2: 0x0219 [0x48] [System] [8092*]:
    → "Only party members present with you in this area will be transported to the [/Very Difficult Intense Ambuscade/Difficult Intense Ambuscade/Normal Intense Ambuscade/Easy Intense Ambuscade/Very Easy Intense Ambuscade/Very Difficult Ambuscade/Difficult Ambuscade/Normal Ambuscade/Easy Ambuscade/Very Easy Ambuscade/Light Ambuscade]."
  3: 0x021C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x021D [0x03] Work_Zone[3] = 1*
  5: 0x0222 [0x24] CREATE_DIALOG(message_id=8093*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Most certainly!/Not yet.]"
  6: 0x0229 [0x25] WAIT_DIALOG_SELECT()
  7: 0x022A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x025F
  8: 0x0232 [0x03] Work_Zone[1] = 1*
  9: 0x0237 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0239 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x023B [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x0257
 12: 0x0243 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 13: 0x0248 [0x48] [System] [8094*]:
    → "Entering the [/Very Difficult Intense Ambuscade/Difficult Intense Ambuscade/Normal Intense Ambuscade/Easy Intense Ambuscade/Very Easy Intense Ambuscade/Very Difficult Ambuscade/Difficult Ambuscade/Normal Ambuscade/Easy Ambuscade/Very Easy Ambuscade/Light Ambuscade]."
 14: 0x024B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x024C [0x1A] CALL_SUBROUTINE(address=0x0359)
 16: 0x024F [0x03] Work_Zone[1] = 2*
 17: 0x0254 [0x01] GOTO 0x025C
 18: 0x0257 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_025C:
 19: 0x025C [0x01] GOTO 0x0264
 20: 0x025F [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_0264:
 21: 0x0264 [0x21] END_EVENT
 22: 0x0265 [0x00] END_REQSTACK()
```

### Event 379

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0266    |
| Data Size    | 352 bytes |
| Instructions | 56        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                   05 0A  00 02 0A 00 00 80 00 57        .........W
0270: 03 24 19 80 01 80 01 80  25 02 00 10 01 80 00 8D  .$......%.......
0280: 02 03 01 10 00 80 43 00  43 01 01 54 03 02 00 10  ......C.C..T....
0290: 00 80 00 A1 02 03 01 10  03 80 43 00 43 01 01 54  ..........C.C..T
02A0: 03 02 00 10 03 80 00 D5  02 03 02 10 00 80 03 03  ................
02B0: 10 1A 80 48 1B 80 71 12  00 80 03 80 71 13 00 00  ...H..q.....q...
02C0: 03 01 10 04 80 40 1C 80  09 80 01 10 00 00 43 00  .....@........C.
02D0: 43 01 01 54 03 02 00 10  04 80 00 09 03 03 02 10  C..T............
02E0: 00 80 03 03 10 1A 80 48  1B 80 71 12 00 80 03 80  .......H..q.....
02F0: 71 13 00 00 03 01 10 05  80 40 1C 80 09 80 01 10  q........@......
0300: 00 00 43 00 43 01 01 54  03 02 00 10 05 80 00 1D  ..C.C..T........
0310: 03 03 01 10 0B 80 43 00  43 01 01 54 03 02 00 10  ......C.C..T....
0320: 0B 80 00 51 03 03 02 10  01 80 03 03 10 1D 80 48  ...Q...........H
0330: 1B 80 71 12 00 80 03 80  71 13 00 00 03 01 10 1E  ..q.....q.......
0340: 80 40 1C 80 09 80 01 10  00 00 43 00 43 01 01 54  .@........C.C..T
0350: 03 06 0A 00 01 69 02 21  00 62 00 80 F0 FF FF 7F  .....i.!.b......
0360: F0 FF FF 7F 6D 61 69 6E  01 80 1C 1F 80 45 20 80  ....main.....E .
0370: F0 FF FF 7F F0 FF FF 7F  77 68 6F 31 01 80 55 20  ........who1..U 
0380: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 31 1C 21 80  .........who1.!.
0390: 45 22 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 01  E".........fdo1.
03A0: 80 55 22 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .U".........fdo1
03B0: 45 20 80 F0 FF FF 7F F0  FF FF 7F 77 68 69 31 01  E .........whi1.
03C0: 80 1C 09 80 30 1B                                 ....0.          
```

#### Opcodes

```
  0: 0x0266 [0x05] ExtData[1]->WorkLocal[10] = 1
  1: 0x0269 [0x02] IF !(ExtData[1]->WorkLocal[10] == 1*) GOTO 0x0357
  2: 0x0271 [0x24] CREATE_DIALOG(message_id=8129*, default_option=0*, option_flags=0*)
    → "Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Dummy Entrance People./Close dialogue.]"
  3: 0x0278 [0x25] WAIT_DIALOG_SELECT()
  4: 0x0279 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x028D
  5: 0x0281 [0x03] Work_Zone[1] = 1*
  6: 0x0286 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x0288 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x028A [0x01] GOTO 0x0354
  9: 0x028D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02A1
 10: 0x0295 [0x03] Work_Zone[1] = 2*
 11: 0x029A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x029C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x029E [0x01] GOTO 0x0354
 14: 0x02A1 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x02D5
 15: 0x02A9 [0x03] Work_Zone[2] = 1*
 16: 0x02AE [0x03] Work_Zone[3] = 50*
 17: 0x02B3 [0x48] [System] [8138*]:
    → "Designate a value between $0 and $1."
 18: 0x02B6 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 19: 0x02BC [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 20: 0x02C0 [0x03] Work_Zone[1] = 3*
 21: 0x02C5 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 22: 0x02CE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 23: 0x02D0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 24: 0x02D2 [0x01] GOTO 0x0354
 25: 0x02D5 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0309
 26: 0x02DD [0x03] Work_Zone[2] = 1*
 27: 0x02E2 [0x03] Work_Zone[3] = 50*
 28: 0x02E7 [0x48] [System] [8138*]:
    → "Designate a value between $0 and $1."
 29: 0x02EA [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 30: 0x02F0 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 31: 0x02F4 [0x03] Work_Zone[1] = 4*
 32: 0x02F9 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 33: 0x0302 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 34: 0x0304 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 35: 0x0306 [0x01] GOTO 0x0354
 36: 0x0309 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x031D
 37: 0x0311 [0x03] Work_Zone[1] = 5*
 38: 0x0316 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 39: 0x0318 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 40: 0x031A [0x01] GOTO 0x0354
 41: 0x031D [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0351
 42: 0x0325 [0x03] Work_Zone[2] = 0*
 43: 0x032A [0x03] Work_Zone[3] = 17*
 44: 0x032F [0x48] [System] [8138*]:
    → "Designate a value between $0 and $1."
 45: 0x0332 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 46: 0x0338 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 47: 0x033C [0x03] Work_Zone[1] = 6*
 48: 0x0341 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 49: 0x034A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 50: 0x034C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 51: 0x034E [0x01] GOTO 0x0354
 52: 0x0351 [0x06] ExtData[1]->WorkLocal[10] = 0

SUBROUTINE_0354:
 53: 0x0354 [0x01] GOTO 0x0269
 54: 0x0357 [0x21] END_EVENT
 55: 0x0358 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0359 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x036A [0x1C] WAIT(90* ticks)
     0x036D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x037E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x038D [0x1C] WAIT(45* ticks)
     0x0390 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03A1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x03B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x03C1 [0x1C] WAIT(15* ticks)
     0x03C4 [0x30] SET_UCOFF_CONTINUE_ZERO()
     0x03C5 [0x1B] RETURN
```
