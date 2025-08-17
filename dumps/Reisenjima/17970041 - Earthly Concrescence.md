# 17970041 - Earthly Concrescence

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Reisenjima (ID: 291) |
| Block Size       | 1004 bytes           |
| Total Events     | 9                    |
| References Count | 38                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [16](#event-16)       | 0x0001       |    352 |             79 |
| [19](#event-19)       | 0x0161       |    104 |             26 |
| [20](#event-20)       | 0x01C9       |    103 |             28 |
| [21](#event-21)       | 0x0230       |    233 |             51 |
| [34](#event-34)       | 0x0319       |      1 |              1 |
| [41](#event-41)       | 0x031A       |      1 |              1 |
| [43](#event-43)       | 0x031B       |      1 |              1 |
| [53](#event-53)       | 0x031C       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0007      |           7 |
|       2 | 0x0008      |           8 |
|       3 | 0x000F      |          15 |
|       4 | 0x1F78      |        8056 |
|       5 | 0x0001      |           1 |
|       6 | 0x0012      |          18 |
|       7 | 0x0002      |           2 |
|       8 | 0x0003      |           3 |
|       9 | 0x0006      |           6 |
|      10 | 0x0004      |           4 |
|      11 | 0x0005      |           5 |
|      12 | 0x0018      |          24 |
|      13 | 0x001F      |          31 |
|      14 | 0x0064      |         100 |
|      15 | 0x40000000  |  1073741824 |
|      16 | 0xFFFFFFFF  |  4294967295 |
|      17 | 0x1F89      |        8073 |
|      18 | 0x1F8E      |        8078 |
|      19 | 0x1F8F      |        8079 |
|      20 | 0x1F7C      |        8060 |
|      21 | 0x000B      |          11 |
|      22 | 0x1F7E      |        8062 |
|      23 | 0x1F93      |        8083 |
|      24 | 0x1F95      |        8085 |
|      25 | 0x1F92      |        8082 |
|      26 | 0x1F94      |        8084 |
|      27 | 0x1F96      |        8086 |
|      28 | 0x1F7A      |        8058 |
|      29 | 0x1F7B      |        8059 |
|      30 | 0x1F7D      |        8061 |
|      31 | 0x1FA1      |        8097 |
|      32 | 0x0032      |          50 |
|      33 | 0x1FAA      |        8106 |
|      34 | 0x00A8      |         168 |
|      35 | 0x00A0      |         160 |
|      36 | 0x00C8      |         200 |
|      37 | 0x003C      |          60 |

## String References

- **8056**: Attempt which? (Auto-transport: [off/on]) [None./Omen. (Content level: $1)/Nii's Last Stand./Dance of the Tengu (Zhuu Buxu)./Dance of the Tengu (Reikuu)./Toggle auto-transport.]
- **8058**: Only party members present with you in this area will be transported to [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)].
- **8059**: You have selected to enter [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)].
- **8060**: [Apply to proceed/Proceed]? [Most certainly!/Not yet.]
- **8061**: Entering [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)].
- **8062**: You have chosen not to [apply to/enter] [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)].
- **8073**: You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party.
- **8078**: Applying to enter [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)]. You will be unable to participate if you add any more party members. Are you sure?
- **8079**: Applying to enter [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)].
- **8082**: You are currently number $3 in line for the [earthly concrescence/aspirants' grounds/babbling brook].
- **8083**: You are currently number $3 in line, with $2 in front of you.
- **8084**: Prepare yourselves! The battlefield is almost ready!
- **8085**: You are currently applying to enter [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)].
- **8086**: Your number: $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]
- **8097**: Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Close dialogue.]
- **8106**: Designate a value between $0 and $1.

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

### Event 16

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 352 bytes |
| Instructions | 75        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 07 00 02 10 03  04 00 03 10 41 00 80 01   B..........A...
0010: 80 06 10 0F 00 41 02 80  03 80 06 10 10 00 03 0E  .....A..........
0020: 00 07 10 05 08 00 03 02  00 00 80 03 03 00 00 80  ................
0030: 03 01 00 00 80 24 04 80  00 80 07 00 25 02 00 10  .....$......%...
0040: 05 80 00 55 00 03 02 00  05 80 03 11 00 06 80 05  ...U............
0050: 12 00 01 BF 00 02 00 10  07 80 00 6D 00 03 02 00  ...........m....
0060: 07 80 03 11 00 05 80 06  12 00 01 BF 00 02 00 10  ................
0070: 08 80 00 85 00 03 02 00  08 80 03 11 00 09 80 05  ................
0080: 12 00 01 BF 00 02 00 10  0A 80 00 9D 00 03 02 00  ................
0090: 0A 80 03 11 00 09 80 05  12 00 01 BF 00 02 00 10  ................
00A0: 0B 80 00 B8 00 03 01 10  00 80 40 0C 80 0D 80 01  ..........@.....
00B0: 10 0E 80 21 00 01 BF 00  03 01 10 0F 80 21 00 03  ...!.........!..
00C0: 01 00 02 00 02 12 00 00  80 01 E9 00 03 0B 00 11  ................
00D0: 00 02 11 00 09 80 02 E1  00 08 0B 00 10 00 01 E6  ................
00E0: 00 08 0B 00 0F 00 01 EE  00 03 0B 00 10 80 03 06  ................
00F0: 10 0B 00 02 06 10 00 80  04 FE 00 48 11 80 03 02  ...........H....
0100: 10 01 00 02 0F 00 05 80  02 12 01 48 12 80 23 01  ...........H..#.
0110: 16 01 48 13 80 23 03 03  10 00 80 24 14 80 00 80  ..H..#.....$....
0120: 00 80 25 02 00 10 00 80  00 4B 01 03 01 10 00 80  ..%......K......
0130: 40 00 80 15 80 01 10 01  00 43 00 43 01 02 09 10  @........C.C....
0140: 00 80 01 48 01 01 EE 00  01 5F 01 03 02 10 01 00  ...H....._......
0150: 03 03 10 00 80 48 16 80  03 01 10 0F 80 21 00 21  .....H.......!.!
0160: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[2]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[3]
  3: 0x000C [0x41] ExtData[1]->WorkLocal[15] = Work_Zone[6] (bits 0*-7*)
  4: 0x0015 [0x41] ExtData[1]->WorkLocal[16] = Work_Zone[6] (bits 8*-15*)
  5: 0x001E [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[7]
  6: 0x0023 [0x05] ExtData[1]->WorkLocal[8] = 1
  7: 0x0026 [0x03] ExtData[1]->WorkLocal[2] = 0*
  8: 0x002B [0x03] ExtData[1]->WorkLocal[3] = 0*
  9: 0x0030 [0x03] ExtData[1]->WorkLocal[1] = 0*
 10: 0x0035 [0x24] CREATE_DIALOG(message_id=8056*, default_option=0*, option_flags=ExtData[1]->WorkLocal[7])
    → "Attempt which? (Auto-transport: [off/on]) [None./Omen. (Content level: $1)/Nii's Last Stand./Dance of the Tengu (Zhuu Buxu)./Dance of the Tengu (Reikuu)./Toggle auto-transport.]"
 11: 0x003C [0x25] WAIT_DIALOG_SELECT()
 12: 0x003D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0055
 13: 0x0045 [0x03] ExtData[1]->WorkLocal[2] = 1*
 14: 0x004A [0x03] ExtData[1]->WorkLocal[17] = 18*
 15: 0x004F [0x05] ExtData[1]->WorkLocal[18] = 1
 16: 0x0052 [0x01] GOTO 0x00BF
 17: 0x0055 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x006D
 18: 0x005D [0x03] ExtData[1]->WorkLocal[2] = 2*
 19: 0x0062 [0x03] ExtData[1]->WorkLocal[17] = 1*
 20: 0x0067 [0x06] ExtData[1]->WorkLocal[18] = 0
 21: 0x006A [0x01] GOTO 0x00BF
 22: 0x006D [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0085
 23: 0x0075 [0x03] ExtData[1]->WorkLocal[2] = 3*
 24: 0x007A [0x03] ExtData[1]->WorkLocal[17] = 6*
 25: 0x007F [0x05] ExtData[1]->WorkLocal[18] = 1
 26: 0x0082 [0x01] GOTO 0x00BF
 27: 0x0085 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x009D
 28: 0x008D [0x03] ExtData[1]->WorkLocal[2] = 4*
 29: 0x0092 [0x03] ExtData[1]->WorkLocal[17] = 6*
 30: 0x0097 [0x05] ExtData[1]->WorkLocal[18] = 1
 31: 0x009A [0x01] GOTO 0x00BF
 32: 0x009D [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x00B8
 33: 0x00A5 [0x03] Work_Zone[1] = 0*
 34: 0x00AA [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=100*)
 35: 0x00B3 [0x21] END_EVENT
 36: 0x00B4 [0x00] END_REQSTACK()

SUBROUTINE_00BF:
 37: 0x00BF [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[2]
 38: 0x00C4 [0x02] IF !(ExtData[1]->WorkLocal[18] == 0*) GOTO 0x00E9
 39: 0x00CC [0x03] ExtData[1]->WorkLocal[11] = ExtData[1]->WorkLocal[17]
 40: 0x00D1 [0x02] IF !(ExtData[1]->WorkLocal[17] <= 6*) GOTO 0x00E1
 41: 0x00D9 [0x08] ExtData[1]->WorkLocal[11] -= ExtData[1]->WorkLocal[16]
 42: 0x00DE [0x01] GOTO 0x00E6
 43: 0x00E1 [0x08] ExtData[1]->WorkLocal[11] -= ExtData[1]->WorkLocal[15]

SUBROUTINE_00E6:
 44: 0x00E6 [0x01] GOTO 0x00EE
 45: 0x00E9 [0x03] ExtData[1]->WorkLocal[11] = 4294967295*

SUBROUTINE_00EE:
 46: 0x00EE [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[11]
 47: 0x00F3 [0x02] IF !(Work_Zone[6] < 0*) GOTO 0x00FE
 48: 0x00FB [0x48] [System] [8073*]:
    → "You will be able to call forth up to $4 alter ego[/s] given the current number of players in your party."
 49: 0x00FE [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 50: 0x0103 [0x02] IF !(ExtData[1]->WorkLocal[15] <= 1*) GOTO 0x0112
 51: 0x010B [0x48] [System] [8078*]:
    → "Applying to enter [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)]. You will be unable to participate if you add any more party members. Are you sure?"
 52: 0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x010F [0x01] GOTO 0x0116
 54: 0x0112 [0x48] [System] [8079*]:
    → "Applying to enter [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)]."
 55: 0x0115 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0116:
 56: 0x0116 [0x03] Work_Zone[3] = 0*
 57: 0x011B [0x24] CREATE_DIALOG(message_id=8060*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Most certainly!/Not yet.]"
 58: 0x0122 [0x25] WAIT_DIALOG_SELECT()
 59: 0x0123 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x014B
 60: 0x012B [0x03] Work_Zone[1] = 0*
 61: 0x0130 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 62: 0x0139 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 63: 0x013B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 64: 0x013D [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x0148
 65: 0x0145 [0x01] GOTO 0x00EE
 66: 0x0148 [0x01] GOTO 0x015F
 67: 0x014B [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 68: 0x0150 [0x03] Work_Zone[3] = 0*
 69: 0x0155 [0x48] [System] [8062*]:
    → "You have chosen not to [apply to/enter] [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)]."
 70: 0x0158 [0x03] Work_Zone[1] = 1073741824*
 71: 0x015D [0x21] END_EVENT
 72: 0x015E [0x00] END_REQSTACK()

SUBROUTINE_015F:
 73: 0x015F [0x21] END_EVENT
 74: 0x0160 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00B5 [0x01] GOTO 0x00BF
```

### Event 19

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0161    |
| Data Size    | 104 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:    03 13 00 03 10 03 03  10 06 10 02 04 10 00 80   ...............
0170: 02 7A 01 48 17 80 23 01  7E 01 48 18 80 23 48 19  .z.H..#.~.H..#H.
0180: 80 23 02 13 00 00 80 00  95 01 48 1A 80 03 01 10  .#........H.....
0190: 0F 80 01 C7 01 03 02 10  05 80 24 1B 80 05 80 00  ..........$.....
01A0: 80 25 02 00 10 00 80 00  B2 01 03 01 10 05 80 01  .%..............
01B0: C7 01 02 00 10 05 80 00  C2 01 03 01 10 07 80 01  ................
01C0: C7 01 03 01 10 0F 80 21  00                       .......!.       
```

#### Opcodes

```
  0: 0x0161 [0x03] ExtData[1]->WorkLocal[19] = Work_Zone[3]
  1: 0x0166 [0x03] Work_Zone[3] = Work_Zone[6]
  2: 0x016B [0x02] IF !(Work_Zone[4] <= 0*) GOTO 0x017A
  3: 0x0173 [0x48] [System] [8083*]:
    → "You are currently number $3 in line, with $2 in front of you."
  4: 0x0176 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0177 [0x01] GOTO 0x017E
  6: 0x017A [0x48] [System] [8085*]:
    → "You are currently applying to enter [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)]."
  7: 0x017D [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_017E:
  8: 0x017E [0x48] [System] [8082*]:
    → "You are currently number $3 in line for the [earthly concrescence/aspirants' grounds/babbling brook]."
  9: 0x0181 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0182 [0x02] IF !(ExtData[1]->WorkLocal[19] == 0*) GOTO 0x0195
 11: 0x018A [0x48] [System] [8084*]:
    → "Prepare yourselves! The battlefield is almost ready!"
 12: 0x018D [0x03] Work_Zone[1] = 1073741824*
 13: 0x0192 [0x01] GOTO 0x01C7
 14: 0x0195 [0x03] Work_Zone[2] = 1*
 15: 0x019A [0x24] CREATE_DIALOG(message_id=8086*, default_option=1*, option_flags=0*)
    → "Your number: $3. (Auto-transport: [off/on]) [Remove your name./Toggle auto-transport./Close dialogue.]"
 16: 0x01A1 [0x25] WAIT_DIALOG_SELECT()
 17: 0x01A2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01B2
 18: 0x01AA [0x03] Work_Zone[1] = 1*
 19: 0x01AF [0x01] GOTO 0x01C7
 20: 0x01B2 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01C2
 21: 0x01BA [0x03] Work_Zone[1] = 2*
 22: 0x01BF [0x01] GOTO 0x01C7
 23: 0x01C2 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_01C7:
 24: 0x01C7 [0x21] END_EVENT
 25: 0x01C8 [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01C9    |
| Data Size    | 103 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                             42 03 01 00 02 10 03           B......
01D0: 0F 00 03 10 02 0F 00 05  80 02 E3 01 48 1C 80 23  ............H..#
01E0: 01 E7 01 48 1D 80 23 03  03 10 05 80 24 14 80 00  ...H..#.....$...
01F0: 80 00 80 25 02 00 10 00  80 00 29 02 03 01 10 05  ...%......).....
0200: 80 43 00 43 01 02 09 10  00 80 00 21 02 03 02 10  .C.C.......!....
0210: 01 00 48 1E 80 23 1A EF  02 03 01 10 07 80 01 26  ..H..#.........&
0220: 02 03 01 10 0F 80 01 2E  02 03 01 10 0F 80 21 00  ..............!.
```

#### Opcodes

```
  0: 0x01C9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01CA [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
  2: 0x01CF [0x03] ExtData[1]->WorkLocal[15] = Work_Zone[3]
  3: 0x01D4 [0x02] IF !(ExtData[1]->WorkLocal[15] <= 1*) GOTO 0x01E3
  4: 0x01DC [0x48] [System] [8058*]:
    → "Only party members present with you in this area will be transported to [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)]."
  5: 0x01DF [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01E0 [0x01] GOTO 0x01E7
  7: 0x01E3 [0x48] [System] [8059*]:
    → "You have selected to enter [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)]."
  8: 0x01E6 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_01E7:
  9: 0x01E7 [0x03] Work_Zone[3] = 1*
 10: 0x01EC [0x24] CREATE_DIALOG(message_id=8060*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Most certainly!/Not yet.]"
 11: 0x01F3 [0x25] WAIT_DIALOG_SELECT()
 12: 0x01F4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0229
 13: 0x01FC [0x03] Work_Zone[1] = 1*
 14: 0x0201 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 15: 0x0203 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 16: 0x0205 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x0221
 17: 0x020D [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 18: 0x0212 [0x48] [System] [8061*]:
    → "Entering [/Omen/Nii's Last Stand/Dance of the Tengu (Zhuu Buxu)/Dance of the Tengu (Reikuu)]."
 19: 0x0215 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0216 [0x1A] CALL_SUBROUTINE(address=0x02EF)
 21: 0x0219 [0x03] Work_Zone[1] = 2*
 22: 0x021E [0x01] GOTO 0x0226
 23: 0x0221 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_0226:
 24: 0x0226 [0x01] GOTO 0x022E
 25: 0x0229 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_022E:
 26: 0x022E [0x21] END_EVENT
 27: 0x022F [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0230    |
| Data Size    | 233 bytes |
| Instructions | 45        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230: 05 0A 00 02 0A 00 05 80  00 ED 02 24 1F 80 00 80  ...........$....
0240: 00 80 25 02 00 10 00 80  00 57 02 03 01 10 05 80  ..%......W......
0250: 43 00 43 01 01 EA 02 02  00 10 05 80 00 6B 02 03  C.C..........k..
0260: 01 10 07 80 43 00 43 01  01 EA 02 02 00 10 07 80  ....C.C.........
0270: 00 9F 02 03 02 10 05 80  03 03 10 20 80 48 21 80  ........... .H!.
0280: 71 12 05 80 07 80 71 13  00 00 03 01 10 08 80 40  q.....q........@
0290: 02 80 03 80 01 10 00 00  43 00 43 01 01 EA 02 02  ........C.C.....
02A0: 00 10 08 80 00 D3 02 03  02 10 05 80 03 03 10 20  ............... 
02B0: 80 48 21 80 71 12 05 80  07 80 71 13 00 00 03 01  .H!.q.....q.....
02C0: 10 0A 80 40 02 80 03 80  01 10 00 00 43 00 43 01  ...@........C.C.
02D0: 01 EA 02 02 00 10 0A 80  00 E7 02 03 01 10 0B 80  ................
02E0: 43 00 43 01 01 EA 02 06  0A 00 01 33 02 21 00 D0  C.C........3.!..
02F0: 22 80 F0 FF FF 7F F0 FF  FF 7F 6D 61 69 6E 00 80  ".........main..
0300: 1C 23 80 45 24 80 F0 FF  FF 7F F0 FF FF 7F 66 64  .#.E$.........fd
0310: 6F 31 00 80 1C 25 80 30  1B                       o1...%.0.       
```

#### Opcodes

```
  0: 0x0230 [0x05] ExtData[1]->WorkLocal[10] = 1
  1: 0x0233 [0x02] IF !(ExtData[1]->WorkLocal[10] == 1*) GOTO 0x02ED
  2: 0x023B [0x24] CREATE_DIALOG(message_id=8097*, default_option=0*, option_flags=0*)
    → "Debug menu. [Check information./View applicants./Applicant parameters./Change maximum limit./Clear applications./Close dialogue.]"
  3: 0x0242 [0x25] WAIT_DIALOG_SELECT()
  4: 0x0243 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0257
  5: 0x024B [0x03] Work_Zone[1] = 1*
  6: 0x0250 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x0252 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x0254 [0x01] GOTO 0x02EA
  9: 0x0257 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x026B
 10: 0x025F [0x03] Work_Zone[1] = 2*
 11: 0x0264 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x0266 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x0268 [0x01] GOTO 0x02EA
 14: 0x026B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x029F
 15: 0x0273 [0x03] Work_Zone[2] = 1*
 16: 0x0278 [0x03] Work_Zone[3] = 50*
 17: 0x027D [0x48] [System] [8106*]:
    → "Designate a value between $0 and $1."
 18: 0x0280 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 19: 0x0286 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 20: 0x028A [0x03] Work_Zone[1] = 3*
 21: 0x028F [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 22: 0x0298 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 23: 0x029A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 24: 0x029C [0x01] GOTO 0x02EA
 25: 0x029F [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x02D3
 26: 0x02A7 [0x03] Work_Zone[2] = 1*
 27: 0x02AC [0x03] Work_Zone[3] = 50*
 28: 0x02B1 [0x48] [System] [8106*]:
    → "Designate a value between $0 and $1."
 29: 0x02B4 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 30: 0x02BA [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[0])
 31: 0x02BE [0x03] Work_Zone[1] = 4*
 32: 0x02C3 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 33: 0x02CC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 34: 0x02CE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 35: 0x02D0 [0x01] GOTO 0x02EA
 36: 0x02D3 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x02E7
 37: 0x02DB [0x03] Work_Zone[1] = 5*
 38: 0x02E0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 39: 0x02E2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 40: 0x02E4 [0x01] GOTO 0x02EA
 41: 0x02E7 [0x06] ExtData[1]->WorkLocal[10] = 0

SUBROUTINE_02EA:
 42: 0x02EA [0x01] GOTO 0x0233
 43: 0x02ED [0x21] END_EVENT
 44: 0x02EE [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x02EF [0xD0] LOAD_SCHEDULED_TASK_ALT5: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[168*, 0*]
     0x0300 [0x1C] WAIT(160* ticks)
     0x0303 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0314 [0x1C] WAIT(60* ticks)
     0x0317 [0x30] SET_UCOFF_CONTINUE_ZERO()
     0x0318 [0x1B] RETURN
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0319  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0310:                             00                             .      
```

#### Opcodes

```
  0: 0x0319 [0x00] END_REQSTACK()
```

### Event 41

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x031A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0310:                                00                           .     
```

#### Opcodes

```
  0: 0x031A [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x031B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0310:                                   00                         .    
```

#### Opcodes

```
  0: 0x031B [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x031C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0310:                                      00                       .   
```

#### Opcodes

```
  0: 0x031C [0x00] END_REQSTACK()
```
