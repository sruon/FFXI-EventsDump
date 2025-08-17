# 17789076 - Veridical Conflux

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Rabao (ID: 247) |
| Block Size       | 1108 bytes      |
| Total Events     | 5               |
| References Count | 39              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [172](#event-172)     | 0x0001       |    298 |             67 |
| [175](#event-175)     | 0x012B       |    109 |             27 |
| [176](#event-176)     | 0x0198       |     93 |             25 |
| [177](#event-177)     | 0x01F5       |    412 |             78 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x2F44      |       12100 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |
|       6 | 0x0010      |          16 |
|       7 | 0x0018      |          24 |
|       8 | 0x001F      |          31 |
|       9 | 0x40000000  |  1073741824 |
|      10 | 0x2F2D      |       12077 |
|      11 | 0x2F4A      |       12106 |
|      12 | 0x2F22      |       12066 |
|      13 | 0x000B      |          11 |
|      14 | 0x000E      |          14 |
|      15 | 0x2F47      |       12103 |
|      16 | 0x2F36      |       12086 |
|      17 | 0x2F4B      |       12107 |
|      18 | 0x2F35      |       12085 |
|      19 | 0x2F37      |       12087 |
|      20 | 0x2F38      |       12088 |
|      21 | 0x2F45      |       12101 |
|      22 | 0x2F46      |       12102 |
|      23 | 0x2F4C      |       12108 |
|      24 | 0x0032      |          50 |
|      25 | 0x2F55      |       12117 |
|      26 | 0x0008      |           8 |
|      27 | 0x000F      |          15 |
|      28 | 0x0005      |           5 |
|      29 | 0x2F60      |       12128 |
|      30 | 0x0064      |         100 |
|      31 | 0x0065      |         101 |
|      32 | 0x0066      |         102 |
|      33 | 0x0067      |         103 |
|      34 | 0x0068      |         104 |
|      35 | 0x005A      |          90 |
|      36 | 0x00C9      |         201 |
|      37 | 0x002D      |          45 |
|      38 | 0x00C8      |         200 |

## String References

- **12066**: [Apply to proceed/Proceed]? [Definitely!/Not yet.]
- **12077**: You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party.
- **12085**: You are currently number $3 in line to be drawn into this nightmare.
- **12086**: You are currently number $3 in line, with $2 in front of you.
- **12087**: Prepare yourselves! The battlefield is almost ready!
- **12088**: Your number: $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]
- **12100**: Attempt which? (Auto-transport: [off/on]) [None./Sheol A. (Level 119+)/Sheol B. (Level 124+)/Sheol C. (Level 129+)/Sheol: Gaol. (Level 124+)/./././././././././././Toggle auto-transport.]
- **12101**: Only party members present with you in this area will be transported to [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **12102**: Entering [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **12103**: You have chosen not to [apply to/enter] [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **12106**: Applying to enter [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]. You will be unable to participate if you add any more party members. Are you sure?
- **12107**: You are currently applying to enter [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **12108**: Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Automatically create./Close dialogue.]
- **12117**: Designate a value between $0 and $1.
- **12128**: $)$P13.$P106$P10, $P13.$lF$0 [1"/%<$P15{/$~_i/$m$P14F/$3$43308646i]

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

### Event 172

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 298 bytes |
| Instructions | 63        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 07 00 02 10 03  04 00 03 10 03 0B 00 06   B..............
0010: 10 03 0E 00 07 10 03 0F  00 08 10 05 08 00 02 08  ................
0020: 00 00 80 00 BC 00 03 02  00 01 80 03 03 00 01 80  ................
0030: 03 01 00 01 80 03 02 10  0F 00 24 02 80 01 80 07  ..........$.....
0040: 00 25 02 00 10 00 80 00  52 00 03 02 00 00 80 01  .%......R.......
0050: A4 00 02 00 10 03 80 00  62 00 03 02 00 03 80 01  ........b.......
0060: A4 00 02 00 10 04 80 00  72 00 03 02 00 04 80 01  ........r.......
0070: A4 00 02 00 10 05 80 00  82 00 03 02 00 05 80 01  ................
0080: A4 00 02 00 10 06 80 00  9D 00 03 01 10 01 80 40  ...............@
0090: 07 80 08 80 01 10 00 80  21 00 01 A4 00 03 01 10  ........!.......
00A0: 09 80 21 00 03 03 00 01  80 03 01 00 02 00 02 02  ..!.............
00B0: 00 01 80 01 B9 00 06 08  00 01 1E 00 03 06 10 0B  ................
00C0: 00 48 0A 80 03 02 10 01  00 03 04 10 03 00 48 0B  .H............H.
00D0: 80 23 03 03 10 01 80 24  0C 80 01 80 01 80 25 02  .#.....$......%.
00E0: 00 10 01 80 00 10 01 03  01 10 01 80 40 01 80 0D  ............@...
00F0: 80 01 10 01 00 40 0E 80  06 80 01 10 03 00 43 00  .....@........C.
0100: 43 01 02 09 10 01 80 01  0D 01 01 BC 00 01 29 01  C.............).
0110: 03 02 10 01 00 03 03 10  01 80 03 04 10 03 00 48  ...............H
0120: 0F 80 03 01 10 09 80 21  00 21 00                 .......!.!.     
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[2]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[3]
  3: 0x000C [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[6]
  4: 0x0011 [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[7]
  5: 0x0016 [0x03] ExtData[1]->WorkLocal[15] = Work_Zone[8]
  6: 0x001B [0x05] ExtData[1]->WorkLocal[8] = 1
  7: 0x001E [0x02] IF !(ExtData[1]->WorkLocal[8] == 1*) GOTO 0x00BC
  8: 0x0026 [0x03] ExtData[1]->WorkLocal[2] = 0*
  9: 0x002B [0x03] ExtData[1]->WorkLocal[3] = 0*
 10: 0x0030 [0x03] ExtData[1]->WorkLocal[1] = 0*
 11: 0x0035 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[15]
 12: 0x003A [0x24] CREATE_DIALOG(message_id=12100*, default_option=0*, option_flags=ExtData[1]->WorkLocal[7])
    → "Attempt which? (Auto-transport: [off/on]) [None./Sheol A. (Level 119+)/Sheol B. (Level 124+)/Sheol C. (Level 129+)/Sheol: Gaol. (Level 124+)/./././././././././././Toggle auto-transport.]"
 13: 0x0041 [0x25] WAIT_DIALOG_SELECT()
 14: 0x0042 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0052
 15: 0x004A [0x03] ExtData[1]->WorkLocal[2] = 1*
 16: 0x004F [0x01] GOTO 0x00A4
 17: 0x0052 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0062
 18: 0x005A [0x03] ExtData[1]->WorkLocal[2] = 2*
 19: 0x005F [0x01] GOTO 0x00A4
 20: 0x0062 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0072
 21: 0x006A [0x03] ExtData[1]->WorkLocal[2] = 3*
 22: 0x006F [0x01] GOTO 0x00A4
 23: 0x0072 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0082
 24: 0x007A [0x03] ExtData[1]->WorkLocal[2] = 4*
 25: 0x007F [0x01] GOTO 0x00A4
 26: 0x0082 [0x02] IF !(Work_Zone[0] == 16*) GOTO 0x009D
 27: 0x008A [0x03] Work_Zone[1] = 0*
 28: 0x008F [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=1*)
 29: 0x0098 [0x21] END_EVENT
 30: 0x0099 [0x00] END_REQSTACK()

SUBROUTINE_00A4:
 31: 0x00A4 [0x03] ExtData[1]->WorkLocal[3] = 0*
 32: 0x00A9 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[2]
 33: 0x00AE [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x00B9
 34: 0x00B6 [0x06] ExtData[1]->WorkLocal[8] = 0
 35: 0x00B9 [0x01] GOTO 0x001E

SUBROUTINE_00BC:
 36: 0x00BC [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[11]
 37: 0x00C1 [0x48] [System] [12077*]:
    → "You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party."
 38: 0x00C4 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 39: 0x00C9 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 40: 0x00CE [0x48] [System] [12106*]:
    → "Applying to enter [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]. You will be unable to participate if you add any more party members. Are you sure?"
 41: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x00D2 [0x03] Work_Zone[3] = 0*
 43: 0x00D7 [0x24] CREATE_DIALOG(message_id=12066*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Definitely!/Not yet.]"
 44: 0x00DE [0x25] WAIT_DIALOG_SELECT()
 45: 0x00DF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0110
 46: 0x00E7 [0x03] Work_Zone[1] = 0*
 47: 0x00EC [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 48: 0x00F5 [0x40] SET_BIT_WORK_RANGE(start_bit=14*, end_bit=16*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[3])
 49: 0x00FE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 50: 0x0100 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 51: 0x0102 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x010D
 52: 0x010A [0x01] GOTO 0x00BC
 53: 0x010D [0x01] GOTO 0x0129
 54: 0x0110 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 55: 0x0115 [0x03] Work_Zone[3] = 0*
 56: 0x011A [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 57: 0x011F [0x48] [System] [12103*]:
    → "You have chosen not to [apply to/enter] [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
 58: 0x0122 [0x03] Work_Zone[1] = 1073741824*
 59: 0x0127 [0x21] END_EVENT
 60: 0x0128 [0x00] END_REQSTACK()

SUBROUTINE_0129:
 61: 0x0129 [0x21] END_EVENT
 62: 0x012A [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x009A [0x01] GOTO 0x00A4
```

### Event 175

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x012B    |
| Data Size    | 109 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   03 12 00 04 10             .....
0130: 03 04 10 06 10 02 04 10  01 80 02 44 01 48 10 80  ...........D.H..
0140: 23 01 48 01 48 11 80 23  03 04 10 12 00 48 12 80  #.H.H..#.....H..
0150: 23 02 03 10 01 80 00 64  01 48 13 80 03 01 10 09  #......d.H......
0160: 80 01 96 01 03 02 10 00  80 24 14 80 00 80 01 80  .........$......
0170: 25 02 00 10 01 80 00 81  01 03 01 10 00 80 01 96  %...............
0180: 01 02 00 10 00 80 00 91  01 03 01 10 03 80 01 96  ................
0190: 01 03 01 10 09 80 21 00                           ......!.        
```

#### Opcodes

```
  0: 0x012B [0x03] ExtData[1]->WorkLocal[18] = Work_Zone[4]
  1: 0x0130 [0x03] Work_Zone[4] = Work_Zone[6]
  2: 0x0135 [0x02] IF !(Work_Zone[4] <= 0*) GOTO 0x0144
  3: 0x013D [0x48] [System] [12086*]:
    → "You are currently number $3 in line, with $2 in front of you."
  4: 0x0140 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0141 [0x01] GOTO 0x0148
  6: 0x0144 [0x48] [System] [12107*]:
    → "You are currently applying to enter [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
  7: 0x0147 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0148:
  8: 0x0148 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[18]
  9: 0x014D [0x48] [System] [12085*]:
    → "You are currently number $3 in line to be drawn into this nightmare."
 10: 0x0150 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0151 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0164
 12: 0x0159 [0x48] [System] [12087*]:
    → "Prepare yourselves! The battlefield is almost ready!"
 13: 0x015C [0x03] Work_Zone[1] = 1073741824*
 14: 0x0161 [0x01] GOTO 0x0196
 15: 0x0164 [0x03] Work_Zone[2] = 1*
 16: 0x0169 [0x24] CREATE_DIALOG(message_id=12088*, default_option=1*, option_flags=0*)
    → "Your number: $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]"
 17: 0x0170 [0x25] WAIT_DIALOG_SELECT()
 18: 0x0171 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0181
 19: 0x0179 [0x03] Work_Zone[1] = 1*
 20: 0x017E [0x01] GOTO 0x0196
 21: 0x0181 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0191
 22: 0x0189 [0x03] Work_Zone[1] = 2*
 23: 0x018E [0x01] GOTO 0x0196
 24: 0x0191 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_0196:
 25: 0x0196 [0x21] END_EVENT
 26: 0x0197 [0x00] END_REQSTACK()
```

### Event 176

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0198   |
| Data Size    | 93 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                          42 03 0F 00 02 10 03 10          B.......
01A0: 00 04 10 48 15 80 23 03  03 10 00 80 24 0C 80 01  ...H..#.....$...
01B0: 80 01 80 25 02 00 10 01  80 00 EE 01 03 01 10 00  ...%............
01C0: 80 43 00 43 01 02 09 10  01 80 00 E6 01 03 02 10  .C.C............
01D0: 0F 00 03 04 10 10 00 48  16 80 23 1A 24 03 03 01  .......H..#.$...
01E0: 10 03 80 01 EB 01 03 01  10 09 80 01 F3 01 03 01  ................
01F0: 10 09 80 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x0198 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0199 [0x03] ExtData[1]->WorkLocal[15] = Work_Zone[2]
  2: 0x019E [0x03] ExtData[1]->WorkLocal[16] = Work_Zone[4]
  3: 0x01A3 [0x48] [System] [12101*]:
    → "Only party members present with you in this area will be transported to [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
  4: 0x01A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x01A7 [0x03] Work_Zone[3] = 1*
  6: 0x01AC [0x24] CREATE_DIALOG(message_id=12066*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Definitely!/Not yet.]"
  7: 0x01B3 [0x25] WAIT_DIALOG_SELECT()
  8: 0x01B4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01EE
  9: 0x01BC [0x03] Work_Zone[1] = 1*
 10: 0x01C1 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x01C3 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x01C5 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x01E6
 13: 0x01CD [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[15]
 14: 0x01D2 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[16]
 15: 0x01D7 [0x48] [System] [12102*]:
    → "Entering [/Sheol A/Sheol B/Sheol C/Sheol: Gaol][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
 16: 0x01DA [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x01DB [0x1A] CALL_SUBROUTINE(address=0x0324)
 18: 0x01DE [0x03] Work_Zone[1] = 2*
 19: 0x01E3 [0x01] GOTO 0x01EB
 20: 0x01E6 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_01EB:
 21: 0x01EB [0x01] GOTO 0x01F3
 22: 0x01EE [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_01F3:
 23: 0x01F3 [0x21] END_EVENT
 24: 0x01F4 [0x00] END_REQSTACK()
```

### Event 177

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01F5    |
| Data Size    | 412 bytes |
| Instructions | 67        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                03 13 00  02 10 05 0A 00 02 0A 00       ...........
0200: 00 80 00 22 03 24 17 80  01 80 01 80 25 02 00 10  ...".$......%...
0210: 01 80 00 21 02 03 01 10  00 80 43 00 43 01 01 1F  ...!......C.C...
0220: 03 02 00 10 00 80 00 35  02 03 01 10 03 80 43 00  .......5......C.
0230: 43 01 01 1F 03 02 00 10  03 80 00 69 02 03 02 10  C..........i....
0240: 00 80 03 03 10 18 80 48  19 80 71 12 00 80 03 80  .......H..q.....
0250: 71 13 00 00 03 01 10 04  80 40 1A 80 1B 80 01 10  q........@......
0260: 00 00 43 00 43 01 01 1F  03 02 00 10 04 80 00 9D  ..C.C...........
0270: 02 03 02 10 00 80 03 03  10 18 80 48 19 80 71 12  ...........H..q.
0280: 00 80 03 80 71 13 00 00  03 01 10 05 80 40 1A 80  ....q........@..
0290: 1B 80 01 10 00 00 43 00  43 01 01 1F 03 02 00 10  ......C.C.......
02A0: 05 80 00 B1 02 03 01 10  1C 80 43 00 43 01 01 1F  ..........C.C...
02B0: 03 02 00 10 1C 80 00 1C  03 03 02 10 13 00 24 1D  ..............$.
02C0: 80 01 80 01 80 25 02 00  10 01 80 00 D6 02 03 01  .....%..........
02D0: 10 1E 80 01 16 03 02 00  10 00 80 00 E6 02 03 01  ................
02E0: 10 1F 80 01 16 03 02 00  10 03 80 00 F6 02 03 01  ................
02F0: 10 20 80 01 16 03 02 00  10 04 80 00 06 03 03 01  . ..............
0300: 10 21 80 01 16 03 02 00  10 05 80 00 16 03 03 01  .!..............
0310: 10 22 80 01 16 03 06 0A  00 01 1F 03 06 0A 00 01  ."..............
0320: FD 01 21 00 62 00 80 F0  FF FF 7F F0 FF FF 7F 6D  ..!.b..........m
0330: 61 69 6E 01 80 1C 23 80  45 24 80 F0 FF FF 7F F0  ain...#.E$......
0340: FF FF 7F 77 68 6F 31 01  80 55 24 80 F0 FF FF 7F  ...who1..U$.....
0350: F0 FF FF 7F 77 68 6F 31  1C 25 80 45 26 80 F0 FF  ....who1.%.E&...
0360: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 55 26 80 F0  ......fdo1..U&..
0370: FF FF 7F F0 FF FF 7F 66  64 6F 31 45 24 80 F0 FF  .......fdo1E$...
0380: FF 7F F0 FF FF 7F 77 68  69 31 01 80 1C 1B 80 30  ......whi1.....0
0390: 1B                                                .               
```

#### Opcodes

```
  0: 0x01F5 [0x03] ExtData[1]->WorkLocal[19] = Work_Zone[2]
  1: 0x01FA [0x05] ExtData[1]->WorkLocal[10] = 1
  2: 0x01FD [0x02] IF !(ExtData[1]->WorkLocal[10] == 1*) GOTO 0x0322
  3: 0x0205 [0x24] CREATE_DIALOG(message_id=12108*, default_option=0*, option_flags=0*)
    → "Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Automatically create./Close dialogue.]"
  4: 0x020C [0x25] WAIT_DIALOG_SELECT()
  5: 0x020D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0221
  6: 0x0215 [0x03] Work_Zone[1] = 1*
  7: 0x021A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x021C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x021E [0x01] GOTO 0x031F
 10: 0x0221 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0235
 11: 0x0229 [0x03] Work_Zone[1] = 2*
 12: 0x022E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 13: 0x0230 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 14: 0x0232 [0x01] GOTO 0x031F
 15: 0x0235 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0269
 16: 0x023D [0x03] Work_Zone[2] = 1*
 17: 0x0242 [0x03] Work_Zone[3] = 50*
 18: 0x0247 [0x48] [System] [12117*]:
    → "Designate a value between $0 and $1."
 19: 0x024A [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 20: 0x0250 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 21: 0x0254 [0x03] Work_Zone[1] = 3*
 22: 0x0259 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 23: 0x0262 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 24: 0x0264 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 25: 0x0266 [0x01] GOTO 0x031F
 26: 0x0269 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x029D
 27: 0x0271 [0x03] Work_Zone[2] = 1*
 28: 0x0276 [0x03] Work_Zone[3] = 50*
 29: 0x027B [0x48] [System] [12117*]:
    → "Designate a value between $0 and $1."
 30: 0x027E [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 31: 0x0284 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 32: 0x0288 [0x03] Work_Zone[1] = 4*
 33: 0x028D [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 34: 0x0296 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x0298 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x029A [0x01] GOTO 0x031F
 37: 0x029D [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x02B1
 38: 0x02A5 [0x03] Work_Zone[1] = 5*
 39: 0x02AA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 40: 0x02AC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 41: 0x02AE [0x01] GOTO 0x031F
 42: 0x02B1 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x031C
 43: 0x02B9 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[19]
 44: 0x02BE [0x24] CREATE_DIALOG(message_id=12128*, default_option=0*, option_flags=0*)
    → "$)$P13.$P106$P10, $P13.$lF$0 [1"/%<$P15{/$~_i/$m$P14F/$3$43308646i]"
 45: 0x02C5 [0x25] WAIT_DIALOG_SELECT()
 46: 0x02C6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02D6
 47: 0x02CE [0x03] Work_Zone[1] = 100*
 48: 0x02D3 [0x01] GOTO 0x0316
 49: 0x02D6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02E6
 50: 0x02DE [0x03] Work_Zone[1] = 101*
 51: 0x02E3 [0x01] GOTO 0x0316
 52: 0x02E6 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x02F6
 53: 0x02EE [0x03] Work_Zone[1] = 102*
 54: 0x02F3 [0x01] GOTO 0x0316
 55: 0x02F6 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0306
 56: 0x02FE [0x03] Work_Zone[1] = 103*
 57: 0x0303 [0x01] GOTO 0x0316
 58: 0x0306 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0316
 59: 0x030E [0x03] Work_Zone[1] = 104*
 60: 0x0313 [0x01] GOTO 0x0316

SUBROUTINE_0316:
 61: 0x0316 [0x06] ExtData[1]->WorkLocal[10] = 0
 62: 0x0319 [0x01] GOTO 0x031F
 63: 0x031C [0x06] ExtData[1]->WorkLocal[10] = 0

SUBROUTINE_031F:
 64: 0x031F [0x01] GOTO 0x01FD
 65: 0x0322 [0x21] END_EVENT
 66: 0x0323 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0324 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x0335 [0x1C] WAIT(90* ticks)
     0x0338 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0349 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0358 [0x1C] WAIT(45* ticks)
     0x035B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x036C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x037B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x038C [0x1C] WAIT(15* ticks)
     0x038F [0x30] SET_UCOFF_CONTINUE_ZERO()
     0x0390 [0x1B] RETURN
```
