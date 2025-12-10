# 17195770 - Moogle Meeting

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 1132 bytes                  |
| Total Events     | 6                           |
| References Count | 39                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [228](#event-228)     | 0x0001       |    313 |             70 |
| [231](#event-231)     | 0x013A       |    109 |             27 |
| [232](#event-232)     | 0x01A7       |     93 |             25 |
| [233](#event-233)     | 0x0204       |    412 |             78 |
| [225](#event-225)     | 0x03A0       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x315D      |       12637 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |
|       6 | 0x0010      |          16 |
|       7 | 0x0018      |          24 |
|       8 | 0x001F      |          31 |
|       9 | 0x40000000  |  1073741824 |
|      10 | 0x3129      |       12585 |
|      11 | 0x3163      |       12643 |
|      12 | 0x311E      |       12574 |
|      13 | 0x000B      |          11 |
|      14 | 0x000E      |          14 |
|      15 | 0x3160      |       12640 |
|      16 | 0x3167      |       12647 |
|      17 | 0x3164      |       12644 |
|      18 | 0x3166      |       12646 |
|      19 | 0x3130      |       12592 |
|      20 | 0x3131      |       12593 |
|      21 | 0x315E      |       12638 |
|      22 | 0x315F      |       12639 |
|      23 | 0x313D      |       12605 |
|      24 | 0x0032      |          50 |
|      25 | 0x3146      |       12614 |
|      26 | 0x0008      |           8 |
|      27 | 0x000F      |          15 |
|      28 | 0x0005      |           5 |
|      29 | 0x3151      |       12625 |
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

- **12574**: [Apply to proceed/Proceed]? [Definitely!/Not yet.]
- **12585**: You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party.
- **12592**: Prepare yourselves! The battlefield is almost ready!
- **12593**: Your number: $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]
- **12605**: Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Automatically create./Close dialogue.]
- **12614**: Designate a value between $0 and $1.
- **12625**: $)$P13.$P106$P10, $P13.$lF$0 [1"/%<$P15{/$~_i/$m$P14F/$3$43308646i]
- **12637**: Enter which? (Auto-transport: [Off/On].) [Never mind./Moglesse Oblige./././././././././././././././Toggle auto-transport.]
- **12638**: Only party members present with you in this area will be transported to [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **12639**: Entering [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **12640**: You have chosen not to [apply to/enter] [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **12643**: Applying to enter [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]. You will be unable to participate if you add any more party members. Are you sure?
- **12644**: You are currently applying to enter [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy].
- **12646**: Your registration number for entering this nightmare is $3.
- **12647**: IDs up through $3 have been registered, and ID $2 is currently ready.

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

### Event 228

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 313 bytes |
| Instructions | 66        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 07 00 02 10 03  04 00 03 10 03 0C 00 05   B..............
0010: 10 03 0B 00 06 10 03 0F  00 07 10 03 10 00 08 10  ................
0020: 05 08 00 02 08 00 00 80  00 C1 00 03 02 00 01 80  ................
0030: 03 03 00 01 80 03 01 00  01 80 03 02 10 10 00 24  ...............$
0040: 02 80 01 80 07 00 25 02  00 10 00 80 00 57 00 03  ......%......W..
0050: 02 00 00 80 01 A9 00 02  00 10 03 80 00 67 00 03  .............g..
0060: 02 00 03 80 01 A9 00 02  00 10 04 80 00 77 00 03  .............w..
0070: 02 00 04 80 01 A9 00 02  00 10 05 80 00 87 00 03  ................
0080: 02 00 05 80 01 A9 00 02  00 10 06 80 00 A2 00 03  ................
0090: 01 10 01 80 40 07 80 08  80 01 10 00 80 21 00 01  ....@........!..
00A0: A9 00 03 01 10 09 80 21  00 03 03 00 01 80 03 01  .......!........
00B0: 00 02 00 02 02 00 01 80  01 BE 00 06 08 00 01 23  ...............#
00C0: 00 3E 0C 00 01 00 CB 00  01 D3 00 03 06 10 0B 00  .>..............
00D0: 48 0A 80 03 02 10 01 00  03 04 10 03 00 48 0B 80  H............H..
00E0: 23 03 03 10 01 80 24 0C  80 01 80 01 80 25 02 00  #.....$......%..
00F0: 10 01 80 00 1F 01 03 01  10 01 80 40 01 80 0D 80  ...........@....
0100: 01 10 01 00 40 0E 80 06  80 01 10 03 00 43 00 43  ....@........C.C
0110: 01 02 09 10 01 80 01 1C  01 01 C1 00 01 38 01 03  .............8..
0120: 02 10 01 00 03 03 10 01  80 03 04 10 03 00 48 0F  ..............H.
0130: 80 03 01 10 09 80 21 00  21 00                    ......!.!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[2]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[3]
  3: 0x000C [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[5]
  4: 0x0011 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[6]
  5: 0x0016 [0x03] ExtData[1]->WorkLocal[15] = Work_Zone[7]
  6: 0x001B [0x03] ExtData[1]->WorkLocal[16] = Work_Zone[8]
  7: 0x0020 [0x05] ExtData[1]->WorkLocal[8] = 1
  8: 0x0023 [0x02] IF !(ExtData[1]->WorkLocal[8] == 1*) GOTO 0x00C1
  9: 0x002B [0x03] ExtData[1]->WorkLocal[2] = 0*
 10: 0x0030 [0x03] ExtData[1]->WorkLocal[3] = 0*
 11: 0x0035 [0x03] ExtData[1]->WorkLocal[1] = 0*
 12: 0x003A [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[16]
 13: 0x003F [0x24] CREATE_DIALOG(message_id=12637*, default_option=0*, option_flags=ExtData[1]->WorkLocal[7])
    → "Enter which? (Auto-transport: [Off/On].) [Never mind./Moglesse Oblige./././././././././././././././Toggle auto-transport.]"
 14: 0x0046 [0x25] WAIT_DIALOG_SELECT()
 15: 0x0047 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0057
 16: 0x004F [0x03] ExtData[1]->WorkLocal[2] = 1*
 17: 0x0054 [0x01] GOTO 0x00A9
 18: 0x0057 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0067
 19: 0x005F [0x03] ExtData[1]->WorkLocal[2] = 2*
 20: 0x0064 [0x01] GOTO 0x00A9
 21: 0x0067 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0077
 22: 0x006F [0x03] ExtData[1]->WorkLocal[2] = 3*
 23: 0x0074 [0x01] GOTO 0x00A9
 24: 0x0077 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0087
 25: 0x007F [0x03] ExtData[1]->WorkLocal[2] = 4*
 26: 0x0084 [0x01] GOTO 0x00A9
 27: 0x0087 [0x02] IF !(Work_Zone[0] == 16*) GOTO 0x00A2
 28: 0x008F [0x03] Work_Zone[1] = 0*
 29: 0x0094 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=1*)
 30: 0x009D [0x21] END_EVENT
 31: 0x009E [0x00] END_REQSTACK()

SUBROUTINE_00A9:
 32: 0x00A9 [0x03] ExtData[1]->WorkLocal[3] = 0*
 33: 0x00AE [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[2]
 34: 0x00B3 [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x00BE
 35: 0x00BB [0x06] ExtData[1]->WorkLocal[8] = 0
 36: 0x00BE [0x01] GOTO 0x0023

SUBROUTINE_00C1:
 37: 0x00C1 [0x3E] IF !(ExtData[1]->WorkLocal[12] bit ExtData[1]->WorkLocal[1]) GOTO 0x00CB
 38: 0x00C8 [0x01] GOTO 0x00D3
 39: 0x00CB [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[11]
 40: 0x00D0 [0x48] [System] [12585*]:
    → "You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party."

SUBROUTINE_00D3:
 41: 0x00D3 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 42: 0x00D8 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 43: 0x00DD [0x48] [System] [12643*]:
    → "Applying to enter [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]. You will be unable to participate if you add any more party members. Are you sure?"
 44: 0x00E0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x00E1 [0x03] Work_Zone[3] = 0*
 46: 0x00E6 [0x24] CREATE_DIALOG(message_id=12574*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Definitely!/Not yet.]"
 47: 0x00ED [0x25] WAIT_DIALOG_SELECT()
 48: 0x00EE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x011F
 49: 0x00F6 [0x03] Work_Zone[1] = 0*
 50: 0x00FB [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 51: 0x0104 [0x40] SET_BIT_WORK_RANGE(start_bit=14*, end_bit=16*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[3])
 52: 0x010D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 53: 0x010F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 54: 0x0111 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x011C
 55: 0x0119 [0x01] GOTO 0x00C1
 56: 0x011C [0x01] GOTO 0x0138
 57: 0x011F [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 58: 0x0124 [0x03] Work_Zone[3] = 0*
 59: 0x0129 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 60: 0x012E [0x48] [System] [12640*]:
    → "You have chosen not to [apply to/enter] [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
 61: 0x0131 [0x03] Work_Zone[1] = 1073741824*
 62: 0x0136 [0x21] END_EVENT
 63: 0x0137 [0x00] END_REQSTACK()

SUBROUTINE_0138:
 64: 0x0138 [0x21] END_EVENT
 65: 0x0139 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x009F [0x01] GOTO 0x00A9
```

### Event 231

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x013A    |
| Data Size    | 109 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                03 13 00 04 10 03            ......
0140: 04 10 06 10 02 04 10 01  80 02 53 01 48 10 80 23  ..........S.H..#
0150: 01 57 01 48 11 80 23 03  04 10 13 00 48 12 80 23  .W.H..#.....H..#
0160: 02 03 10 01 80 00 73 01  48 13 80 03 01 10 09 80  ......s.H.......
0170: 01 A5 01 03 02 10 00 80  24 14 80 00 80 01 80 25  ........$......%
0180: 02 00 10 01 80 00 90 01  03 01 10 00 80 01 A5 01  ................
0190: 02 00 10 00 80 00 A0 01  03 01 10 03 80 01 A5 01  ................
01A0: 03 01 10 09 80 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x013A [0x03] ExtData[1]->WorkLocal[19] = Work_Zone[4]
  1: 0x013F [0x03] Work_Zone[4] = Work_Zone[6]
  2: 0x0144 [0x02] IF !(Work_Zone[4] <= 0*) GOTO 0x0153
  3: 0x014C [0x48] [System] [12647*]:
    → "IDs up through $3 have been registered, and ID $2 is currently ready."
  4: 0x014F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0150 [0x01] GOTO 0x0157
  6: 0x0153 [0x48] [System] [12644*]:
    → "You are currently applying to enter [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
  7: 0x0156 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0157:
  8: 0x0157 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[19]
  9: 0x015C [0x48] [System] [12646*]:
    → "Your registration number for entering this nightmare is $3."
 10: 0x015F [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0160 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0173
 12: 0x0168 [0x48] [System] [12592*]:
    → "Prepare yourselves! The battlefield is almost ready!"
 13: 0x016B [0x03] Work_Zone[1] = 1073741824*
 14: 0x0170 [0x01] GOTO 0x01A5
 15: 0x0173 [0x03] Work_Zone[2] = 1*
 16: 0x0178 [0x24] CREATE_DIALOG(message_id=12593*, default_option=1*, option_flags=0*)
    → "Your number: $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]"
 17: 0x017F [0x25] WAIT_DIALOG_SELECT()
 18: 0x0180 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0190
 19: 0x0188 [0x03] Work_Zone[1] = 1*
 20: 0x018D [0x01] GOTO 0x01A5
 21: 0x0190 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01A0
 22: 0x0198 [0x03] Work_Zone[1] = 2*
 23: 0x019D [0x01] GOTO 0x01A5
 24: 0x01A0 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_01A5:
 25: 0x01A5 [0x21] END_EVENT
 26: 0x01A6 [0x00] END_REQSTACK()
```

### Event 232

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A7   |
| Data Size    | 93 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                      42  03 10 00 02 10 03 11 00         B........
01B0: 04 10 48 15 80 23 03 03  10 00 80 24 0C 80 01 80  ..H..#.....$....
01C0: 01 80 25 02 00 10 01 80  00 FD 01 03 01 10 00 80  ..%.............
01D0: 43 00 43 01 02 09 10 01  80 00 F5 01 03 02 10 10  C.C.............
01E0: 00 03 04 10 11 00 48 16  80 23 1A 33 03 03 01 10  ......H..#.3....
01F0: 03 80 01 FA 01 03 01 10  09 80 01 02 02 03 01 10  ................
0200: 09 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x01A7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01A8 [0x03] ExtData[1]->WorkLocal[16] = Work_Zone[2]
  2: 0x01AD [0x03] ExtData[1]->WorkLocal[17] = Work_Zone[4]
  3: 0x01B2 [0x48] [System] [12638*]:
    → "Only party members present with you in this area will be transported to [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
  4: 0x01B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x01B6 [0x03] Work_Zone[3] = 1*
  6: 0x01BB [0x24] CREATE_DIALOG(message_id=12574*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Definitely!/Not yet.]"
  7: 0x01C2 [0x25] WAIT_DIALOG_SELECT()
  8: 0x01C3 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01FD
  9: 0x01CB [0x03] Work_Zone[1] = 1*
 10: 0x01D0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x01D2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x01D4 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x01F5
 13: 0x01DC [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[16]
 14: 0x01E1 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[17]
 15: 0x01E6 [0x48] [System] [12639*]:
    → "Entering [/Moglesse Oblige][/: Very Difficult/: Difficult/: Normal/: Easy/: Very Easy]."
 16: 0x01E9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x01EA [0x1A] CALL_SUBROUTINE(address=0x0333)
 18: 0x01ED [0x03] Work_Zone[1] = 2*
 19: 0x01F2 [0x01] GOTO 0x01FA
 20: 0x01F5 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_01FA:
 21: 0x01FA [0x01] GOTO 0x0202
 22: 0x01FD [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_0202:
 23: 0x0202 [0x21] END_EVENT
 24: 0x0203 [0x00] END_REQSTACK()
```

### Event 233

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0204    |
| Data Size    | 412 bytes |
| Instructions | 67        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:             03 14 00 02  10 05 0A 00 02 0A 00 00      ............
0210: 80 00 31 03 24 17 80 01  80 01 80 25 02 00 10 01  ..1.$......%....
0220: 80 00 30 02 03 01 10 00  80 43 00 43 01 01 2E 03  ..0......C.C....
0230: 02 00 10 00 80 00 44 02  03 01 10 03 80 43 00 43  ......D......C.C
0240: 01 01 2E 03 02 00 10 03  80 00 78 02 03 02 10 00  ..........x.....
0250: 80 03 03 10 18 80 48 19  80 71 12 00 80 03 80 71  ......H..q.....q
0260: 13 00 00 03 01 10 04 80  40 1A 80 1B 80 01 10 00  ........@.......
0270: 00 43 00 43 01 01 2E 03  02 00 10 04 80 00 AC 02  .C.C............
0280: 03 02 10 00 80 03 03 10  18 80 48 19 80 71 12 00  ..........H..q..
0290: 80 03 80 71 13 00 00 03  01 10 05 80 40 1A 80 1B  ...q........@...
02A0: 80 01 10 00 00 43 00 43  01 01 2E 03 02 00 10 05  .....C.C........
02B0: 80 00 C0 02 03 01 10 1C  80 43 00 43 01 01 2E 03  .........C.C....
02C0: 02 00 10 1C 80 00 2B 03  03 02 10 14 00 24 1D 80  ......+......$..
02D0: 01 80 01 80 25 02 00 10  01 80 00 E5 02 03 01 10  ....%...........
02E0: 1E 80 01 25 03 02 00 10  00 80 00 F5 02 03 01 10  ...%............
02F0: 1F 80 01 25 03 02 00 10  03 80 00 05 03 03 01 10  ...%............
0300: 20 80 01 25 03 02 00 10  04 80 00 15 03 03 01 10   ..%............
0310: 21 80 01 25 03 02 00 10  05 80 00 25 03 03 01 10  !..%.......%....
0320: 22 80 01 25 03 06 0A 00  01 2E 03 06 0A 00 01 0C  "..%............
0330: 02 21 00 62 00 80 F0 FF  FF 7F F0 FF FF 7F 6D 61  .!.b..........ma
0340: 69 6E 01 80 1C 23 80 45  24 80 F0 FF FF 7F F0 FF  in...#.E$.......
0350: FF 7F 77 68 6F 31 01 80  55 24 80 F0 FF FF 7F F0  ..who1..U$......
0360: FF FF 7F 77 68 6F 31 1C  25 80 45 26 80 F0 FF FF  ...who1.%.E&....
0370: 7F F0 FF FF 7F 66 64 6F  31 01 80 55 26 80 F0 FF  .....fdo1..U&...
0380: FF 7F F0 FF FF 7F 66 64  6F 31 45 24 80 F0 FF FF  ......fdo1E$....
0390: 7F F0 FF FF 7F 77 68 69  31 01 80 1C 1B 80 30 1B  .....whi1.....0.
```

#### Opcodes

```
  0: 0x0204 [0x03] ExtData[1]->WorkLocal[20] = Work_Zone[2]
  1: 0x0209 [0x05] ExtData[1]->WorkLocal[10] = 1
  2: 0x020C [0x02] IF !(ExtData[1]->WorkLocal[10] == 1*) GOTO 0x0331
  3: 0x0214 [0x24] CREATE_DIALOG(message_id=12605*, default_option=0*, option_flags=0*)
    → "Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Automatically create./Close dialogue.]"
  4: 0x021B [0x25] WAIT_DIALOG_SELECT()
  5: 0x021C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0230
  6: 0x0224 [0x03] Work_Zone[1] = 1*
  7: 0x0229 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x022B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x022D [0x01] GOTO 0x032E
 10: 0x0230 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0244
 11: 0x0238 [0x03] Work_Zone[1] = 2*
 12: 0x023D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 13: 0x023F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 14: 0x0241 [0x01] GOTO 0x032E
 15: 0x0244 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0278
 16: 0x024C [0x03] Work_Zone[2] = 1*
 17: 0x0251 [0x03] Work_Zone[3] = 50*
 18: 0x0256 [0x48] [System] [12614*]:
    → "Designate a value between $0 and $1."
 19: 0x0259 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 20: 0x025F [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 21: 0x0263 [0x03] Work_Zone[1] = 3*
 22: 0x0268 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 23: 0x0271 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 24: 0x0273 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 25: 0x0275 [0x01] GOTO 0x032E
 26: 0x0278 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x02AC
 27: 0x0280 [0x03] Work_Zone[2] = 1*
 28: 0x0285 [0x03] Work_Zone[3] = 50*
 29: 0x028A [0x48] [System] [12614*]:
    → "Designate a value between $0 and $1."
 30: 0x028D [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 31: 0x0293 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 32: 0x0297 [0x03] Work_Zone[1] = 4*
 33: 0x029C [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 34: 0x02A5 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x02A7 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x02A9 [0x01] GOTO 0x032E
 37: 0x02AC [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x02C0
 38: 0x02B4 [0x03] Work_Zone[1] = 5*
 39: 0x02B9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 40: 0x02BB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 41: 0x02BD [0x01] GOTO 0x032E
 42: 0x02C0 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x032B
 43: 0x02C8 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[20]
 44: 0x02CD [0x24] CREATE_DIALOG(message_id=12625*, default_option=0*, option_flags=0*)
    → "$)$P13.$P106$P10, $P13.$lF$0 [1"/%<$P15{/$~_i/$m$P14F/$3$43308646i]"
 45: 0x02D4 [0x25] WAIT_DIALOG_SELECT()
 46: 0x02D5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02E5
 47: 0x02DD [0x03] Work_Zone[1] = 100*
 48: 0x02E2 [0x01] GOTO 0x0325
 49: 0x02E5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02F5
 50: 0x02ED [0x03] Work_Zone[1] = 101*
 51: 0x02F2 [0x01] GOTO 0x0325
 52: 0x02F5 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0305
 53: 0x02FD [0x03] Work_Zone[1] = 102*
 54: 0x0302 [0x01] GOTO 0x0325
 55: 0x0305 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0315
 56: 0x030D [0x03] Work_Zone[1] = 103*
 57: 0x0312 [0x01] GOTO 0x0325
 58: 0x0315 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0325
 59: 0x031D [0x03] Work_Zone[1] = 104*
 60: 0x0322 [0x01] GOTO 0x0325

SUBROUTINE_0325:
 61: 0x0325 [0x06] ExtData[1]->WorkLocal[10] = 0
 62: 0x0328 [0x01] GOTO 0x032E
 63: 0x032B [0x06] ExtData[1]->WorkLocal[10] = 0

SUBROUTINE_032E:
 64: 0x032E [0x01] GOTO 0x020C
 65: 0x0331 [0x21] END_EVENT
 66: 0x0332 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0333 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x0344 [0x1C] WAIT(90* ticks)
     0x0347 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0358 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0367 [0x1C] WAIT(45* ticks)
     0x036A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x037B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x038A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x039B [0x1C] WAIT(15* ticks)
     0x039E [0x30] SET_UCOFF_CONTINUE_ZERO()
     0x039F [0x1B] RETURN
```

### Event 225

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A0  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x03A0 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x03A6 [0x00] END_REQSTACK()
```
