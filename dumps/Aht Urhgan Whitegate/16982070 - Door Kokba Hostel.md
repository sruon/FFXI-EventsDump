# 16982070 - Door Kokba Hostel

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 2776 bytes                    |
| Total Events     | 5                             |
| References Count | 71                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [76](#event-76)       | 0x0001       |     17 |              7 |
| [77](#event-77)       | 0x0012       |     27 |              9 |
| [80](#event-80)       | 0x002D       |    425 |             90 |
| [70](#event-70)       | 0x01D6       |   1986 |            423 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0E10      |        3600 |
|       1 | 0x25FF      |        9727 |
|       2 | 0x0384      |         900 |
|       3 | 0x003C      |          60 |
|       4 | 0x2600      |        9728 |
|       5 | 0x25DE      |        9694 |
|       6 | 0x25E6      |        9702 |
|       7 | 0x0010      |          16 |
|       8 | 0x001F      |          31 |
|       9 | 0x0001      |           1 |
|      10 | 0x0000      |           0 |
|      11 | 0x0003      |           3 |
|      12 | 0x0004      |           4 |
|      13 | 0x0007      |           7 |
|      14 | 0x0008      |           8 |
|      15 | 0x000B      |          11 |
|      16 | 0x000C      |          12 |
|      17 | 0x000F      |          15 |
|      18 | 0x25E7      |        9703 |
|      19 | 0x25E9      |        9705 |
|      20 | 0x0002      |           2 |
|      21 | 0x25EA      |        9706 |
|      22 | 0x25EB      |        9707 |
|      23 | 0x25EC      |        9708 |
|      24 | 0xFFFFFFFF  |  4294967295 |
|      25 | 0x25FC      |        9724 |
|      26 | 0x25EE      |        9710 |
|      27 | 0x25EF      |        9711 |
|      28 | 0x25F0      |        9712 |
|      29 | 0x25FE      |        9726 |
|      30 | 0x25F1      |        9713 |
|      31 | 0x2607      |        9735 |
|      32 | 0x25DB      |        9691 |
|      33 | 0x25F2      |        9714 |
|      34 | 0x25F3      |        9715 |
|      35 | 0x0005      |           5 |
|      36 | 0x25DC      |        9692 |
|      37 | 0x0020      |          32 |
|      38 | 0x000D      |          13 |
|      39 | 0x002C      |          44 |
|      40 | 0x0006      |           6 |
|      41 | 0x0009      |           9 |
|      42 | 0x000A      |          10 |
|      43 | 0x2A300     |      172800 |
|      44 | 0x25F5      |        9717 |
|      45 | 0x15180     |       86400 |
|      46 | 0x000E      |          14 |
|      47 | 0x25F7      |        9719 |
|      48 | 0x25F8      |        9720 |
|      49 | 0x25F9      |        9721 |
|      50 | 0x01F2      |         498 |
|      51 | 0x25FA      |        9722 |
|      52 | 0xFFFFFFFE  |  4294967294 |
|      53 | 0x00E9      |         233 |
|      54 | 0x25FD      |        9725 |
|      55 | 0x25F6      |        9718 |
|      56 | 0xA8C0      |       43200 |
|      57 | 0x2601      |        9729 |
|      58 | 0x2602      |        9730 |
|      59 | 0x25DD      |        9693 |
|      60 | 0x2603      |        9731 |
|      61 | 0x2604      |        9732 |
|      62 | 0x2605      |        9733 |
|      63 | 0x2606      |        9734 |
|      64 | 0x00C8      |         200 |
|      65 | 0x2977D     |      169853 |
|      66 | 0xFFFF064A  |  4294903370 |
|      67 | 0xFFFFE890  |  4294961296 |
|      68 | 0xFFFFFFFD  |  4294967293 |
|      69 | 0x006C      |         108 |
|      70 | 0x260B      |        9739 |

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

### Event 76

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 17 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 03 10 02 10 07  03 10 00 80 48 01 80 23   B..........H..#
0010: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] Work_Zone[3] = Work_Zone[2]
  2: 0x0007 [0x07] Work_Zone[3] += 3600*
  3: 0x000C [0x48] [System] [9727*]:
    → "The reception period for the \u00072\u007F+\u0000\u00073 to \u00072\u007F+\u0001\u00073 time slot has ended!\u0007You can now begin the process of setting options and creating a password.\u007F1\u0000\u0007"
  4: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0010 [0x21] END_EVENT
  6: 0x0011 [0x00] END_REQSTACK()
```

### Event 77

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       42 03 03 10 02 10  07 03 10 00 80 03 04 10    B.............
0020: 02 80 15 04 10 03 80 48  04 80 23 21 00           .......H..#!.   
```

#### Opcodes

```
  0: 0x0012 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0013 [0x03] Work_Zone[3] = Work_Zone[2]
  2: 0x0018 [0x07] Work_Zone[3] += 3600*
  3: 0x001D [0x03] Work_Zone[4] = 900*
  4: 0x0022 [0x15] Work_Zone[4] /= 60*
  5: 0x0027 [0x48] [System] [9728*]:
    → "The reception period for the \u00072\u007F+\u0000\u00073 to \u00072\u007F+\u0001\u00073 time slot has ended!\u0007Next time, please try to arrive 
\u0002 \u007F\u0012\u0001[minute/minutes] before the reservation begins.\u007F1\u0000\u0007"
  6: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002B [0x21] END_EVENT
  8: 0x002C [0x00] END_REQSTACK()
```

### Event 80

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x002D    |
| Data Size    | 425 bytes |
| Instructions | 83        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         48 05 80               H..
0030: 23 48 06 80 23 06 01 10  40 07 80 08 80 01 10 09  #H..#...@.......
0040: 80 06 03 00 41 0A 80 0B  80 28 10 08 00 40 0A 80  ....A....(...@..
0050: 0B 80 01 10 08 00 41 0C  80 0D 80 28 10 08 00 40  ......A....(...@
0060: 0C 80 0D 80 01 10 08 00  41 0E 80 0F 80 28 10 08  ........A....(..
0070: 00 40 0E 80 0F 80 01 10  08 00 41 10 80 11 80 28  .@........A....(
0080: 10 08 00 40 10 80 11 80  01 10 08 00 41 0A 80 0B  ...@........A...
0090: 80 01 10 02 10 41 0C 80  0D 80 01 10 03 10 41 0E  .....A........A.
00A0: 80 0F 80 01 10 04 10 41  10 80 11 80 01 10 05 10  .......A........
00B0: 24 12 80 03 00 0A 80 25  03 03 00 00 10 02 00 10  $......%........
00C0: 0A 80 00 C8 00 01 82 01  03 08 00 00 10 0C 08 00  ................
00D0: 14 08 00 0C 80 03 09 00  08 00 07 09 00 0B 80 41  ...............A
00E0: 08 00 09 00 01 10 04 00  0B 04 00 02 03 00 09 80  ................
00F0: 80 09 01 24 13 80 04 00  0A 80 25 02 00 10 0A 80  ...$......%.....
0100: 00 06 01 01 06 01 01 63  01 02 03 00 14 80 80 27  .......c.......'
0110: 01 24 15 80 04 00 0A 80  25 02 00 10 0A 80 00 24  .$......%......$
0120: 01 01 24 01 01 63 01 02  03 00 0B 80 80 45 01 24  ..$..c.......E.$
0130: 16 80 04 00 0A 80 25 02  00 10 0A 80 00 42 01 01  ......%......B..
0140: 42 01 01 63 01 02 03 00  0C 80 80 63 01 24 17 80  B..c.......c.$..
0150: 04 00 0A 80 25 02 00 10  0A 80 00 60 01 01 60 01  ....%......`..`.
0160: 01 63 01 02 00 10 0A 80  80 6E 01 01 7F 01 03 0A  .c.......n......
0170: 00 00 10 0C 0A 00 40 08  00 09 00 01 10 0A 00 01  ......@.........
0180: 8C 00 43 00 43 01 02 02  10 18 80 00 95 01 48 19  ..C.C.........H.
0190: 80 23 01 D4 01 48 1A 80  23 2E 71 00 71 01 71 02  .#...H..#.q.q.q.
01A0: 02 02 10 0C 80 80 AF 01  48 1B 80 23 01 D4 01 02  ........H..#....
01B0: 02 10 0B 80 80 C1 01 48  1C 80 23 01 99 01 01 D4  .......H..#.....
01C0: 01 02 02 10 18 80 80 D0  01 48 19 80 23 01 D4 01  .........H..#...
01D0: 48 1C 80 23 21 00                                 H..#!.          
```

#### Opcodes

```
  0: 0x002D [0x48] [System] [9694*]:
    → "You can now begin the process of setting options and creating a password.\u007F1\u0000\u0007"
  1: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0031 [0x48] [System] [9702*]:
    → "You have the option of selecting your attendants...\u007F1\u0000\u0007"
  3: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0035 [0x06] Work_Zone[1] = 0
  5: 0x0038 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=1*)
  6: 0x0041 [0x06] ExtData[1]->WorkLocal[3] = 0
  7: 0x0044 [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[40] (bits 0*-3*)
  8: 0x004D [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[8])
  9: 0x0056 [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[40] (bits 4*-7*)
 10: 0x005F [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[8])
 11: 0x0068 [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[40] (bits 8*-11*)
 12: 0x0071 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[8])
 13: 0x007A [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[40] (bits 12*-15*)
 14: 0x0083 [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[8])
 15: 0x008C [0x41] Work_Zone[2] = Work_Zone[1] (bits 0*-3*)
 16: 0x0095 [0x41] Work_Zone[3] = Work_Zone[1] (bits 4*-7*)
 17: 0x009E [0x41] Work_Zone[4] = Work_Zone[1] (bits 8*-11*)
 18: 0x00A7 [0x41] Work_Zone[5] = Work_Zone[1] (bits 12*-15*)
 19: 0x00B0 [0x24] CREATE_DIALOG(message_id=9703*, default_option=ExtData[1]->WorkLocal[3], option_flags=0*)
    → "Select an attendant to change.\u0007\u000BThis is fine.\u0007Attendant 1 (Type \u000C\u0000[A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/P/Q/R/S/T/U/V/W/X/Y/Z])\u0007Attendant 2 (Type \u000C\u0001[A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/P/Q/R/S/T/U/V/W/X/Y/Z])\u0007Attendant 3 (Type \u000C\u0002[A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/P/Q/R/S/T/U/V/W/X/Y/Z])\u0007Attendant 4 (Type \u000C\u0003[A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/P/Q/R/S/T/U/V/W/X/Y/Z])\u007F1\u0000\u0007"
 20: 0x00B7 [0x25] WAIT_DIALOG_SELECT()
 21: 0x00B8 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[0]
 22: 0x00BD [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C8
 23: 0x00C5 [0x01] GOTO 0x0182
 24: 0x00C8 [0x03] ExtData[1]->WorkLocal[8] = Work_Zone[0]
 25: 0x00CD [0x0C] ExtData[1]->WorkLocal[8]--
 26: 0x00D0 [0x14] ExtData[1]->WorkLocal[8] *= 4*
 27: 0x00D5 [0x03] ExtData[1]->WorkLocal[9] = ExtData[1]->WorkLocal[8]
 28: 0x00DA [0x07] ExtData[1]->WorkLocal[9] += 3*
 29: 0x00DF [0x41] ExtData[1]->WorkLocal[4] = Work_Zone[1] (bits ExtData[1]->WorkLocal[8]-ExtData[1]->WorkLocal[9])
 30: 0x00E8 [0x0B] ExtData[1]->WorkLocal[4]++
 31: 0x00EB [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x0109
 32: 0x00F3 [0x24] CREATE_DIALOG(message_id=9705*, default_option=ExtData[1]->WorkLocal[4], option_flags=0*)
    → "Which do you choose for Attendant 1?\u0007\u000BNo change.\u0007A. Hume male\u0007B. Hume female\u0007C. Elvaan male\u0007D. Elvaan female\u0007E. Tarutaru male\u0007F. Tarutaru female\u0007G. Mithra\u0007H. Galka\u0007I. Hume male Casual\u0007J. Hume female Casual\u0007K. Beautiful Quartet (Hume female)\u0007L. Cutey Cats (Mithra)\u0007M. Party Animals (Hume female)\u0007N. Notorious Gals (Mithra)\u0007O. White Angels (Hume female)\u0007P. Al Zahbi Rumblers (Hume male)\u007F1\u0000\u0007"
 33: 0x00FA [0x25] WAIT_DIALOG_SELECT()
 34: 0x00FB [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0106
 35: 0x0103 [0x01] GOTO 0x0106

SUBROUTINE_0106:
 36: 0x0106 [0x01] GOTO 0x0163
 37: 0x0109 [0x02] IF !(ExtData[1]->WorkLocal[3] == 2*) GOTO 0x0127
 38: 0x0111 [0x24] CREATE_DIALOG(message_id=9706*, default_option=ExtData[1]->WorkLocal[4], option_flags=0*)
    → "Which do you choose for Attendant 2?\u0007\u000BNo change.\u0007A. Hume male\u0007B. Hume female\u0007C. Elvaan male\u0007D. Elvaan female\u0007E. Tarutaru male\u0007F. Tarutaru female\u0007G. Mithra\u0007H. Galka\u0007I. Elvaan male Casual\u0007J. Elvaan female Casual\u0007K. Beautiful Quartet (Hume female)\u0007L. Cutey Cats (Mithra)\u0007M. Party Animals (Hume female)\u0007N. Notorious Gals (Mithra)\u0007O. White Angels (Hume female)\u0007P. Al Zahbi Rumblers (Hume male)\u007F1\u0000\u0007"
 39: 0x0118 [0x25] WAIT_DIALOG_SELECT()
 40: 0x0119 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0124
 41: 0x0121 [0x01] GOTO 0x0124

SUBROUTINE_0124:
 42: 0x0124 [0x01] GOTO 0x0163
 43: 0x0127 [0x02] IF !(ExtData[1]->WorkLocal[3] == 3*) GOTO 0x0145
 44: 0x012F [0x24] CREATE_DIALOG(message_id=9707*, default_option=ExtData[1]->WorkLocal[4], option_flags=0*)
    → "Which do you choose for Attendant 3?\u0007\u000BNo change.\u0007A. Hume male\u0007B. Hume female\u0007C. Elvaan male\u0007D. Elvaan female\u0007E. Tarutaru male\u0007F. Tarutaru female\u0007G. Mithra\u0007H. Galka\u0007I. Tarutaru male Casual\u0007J. Tarutaru female Casual\u0007K. Beautiful Quartet (Hume female)\u0007L. Cutey Cats (Mithra)\u0007M. Party Animals (Hume female)\u0007N. Notorious Gals (Mithra)\u0007O. White Angels (Mithra)\u0007P. Al Zahbi Rumblers (Elvaan)\u007F1\u0000\u0007"
 45: 0x0136 [0x25] WAIT_DIALOG_SELECT()
 46: 0x0137 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0142
 47: 0x013F [0x01] GOTO 0x0142

SUBROUTINE_0142:
 48: 0x0142 [0x01] GOTO 0x0163
 49: 0x0145 [0x02] IF !(ExtData[1]->WorkLocal[3] == 4*) GOTO 0x0163
 50: 0x014D [0x24] CREATE_DIALOG(message_id=9708*, default_option=ExtData[1]->WorkLocal[4], option_flags=0*)
    → "Which do you choose for Attendant 4?\u0007\u000BNo change.\u0007A. Hume male\u0007B. Hume female\u0007C. Elvaan male\u0007D. Elvaan female\u0007E. Tarutaru male\u0007F. Tarutaru female\u0007G. Mithra\u0007H. Galka\u0007I. Galka Casual\u0007J. Mithra female Casual\u0007K. Beautiful Quartet (Hume female)\u0007L. Cutey Cats (Mithra)\u0007M. Party Animals (Hume female)\u0007N. Notorious Gals (Mithra)\u0007O. White Angels (Mithra)\u0007P. Al Zahbi Rumblers (Galka)\u007F1\u0000\u0007"
 51: 0x0154 [0x25] WAIT_DIALOG_SELECT()
 52: 0x0155 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0160
 53: 0x015D [0x01] GOTO 0x0160

SUBROUTINE_0160:
 54: 0x0160 [0x01] GOTO 0x0163

SUBROUTINE_0163:
 55: 0x0163 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x016E
 56: 0x016B [0x01] GOTO 0x017F
 57: 0x016E [0x03] ExtData[1]->WorkLocal[10] = Work_Zone[0]
 58: 0x0173 [0x0C] ExtData[1]->WorkLocal[10]--
 59: 0x0176 [0x40] SET_BIT_WORK_RANGE(start_bit=ExtData[1]->WorkLocal[8], end_bit=ExtData[1]->WorkLocal[9], target=Work_Zone[1], source=ExtData[1]->WorkLocal[10])

SUBROUTINE_017F:
 60: 0x017F [0x01] GOTO 0x008C

SUBROUTINE_0182:
 61: 0x0182 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 62: 0x0184 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 63: 0x0186 [0x02] IF !(Work_Zone[2] == 4294967295*) GOTO 0x0195
 64: 0x018E [0x48] [System] [9724*]:
    → "There appears to have been some trouble with the reservation system.\u007F1\u0000\u0007"
 65: 0x0191 [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x0192 [0x01] GOTO 0x01D4
 67: 0x0195 [0x48] [System] [9710*]:
    → "Create a password.\u007F1\u0000\u0007"
 68: 0x0198 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0199:
 69: 0x0199 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 70: 0x019A [0x71] USER_INPUT_HANDLER: Open password input dialog (sends packet 0x60)
 71: 0x019C [0x71] USER_INPUT_HANDLER: Check if player has input or exited
 72: 0x019E [0x71] USER_INPUT_HANDLER: Check if server responded
 73: 0x01A0 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x01AF
 74: 0x01A8 [0x48] [System] [9711*]:
    → "The password has been set to \u00072\u001C\u0000.\u00073\u0007All options have been set. You can now enter the hostel.\u007F1\u0000\u0007"
 75: 0x01AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 76: 0x01AC [0x01] GOTO 0x01D4
 77: 0x01AF [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x01C1
 78: 0x01B7 [0x48] [System] [9712*]:
    → "That password is invalid.\u007F1\u0000\u0007"
 79: 0x01BA [0x23] WAIT_FOR_DIALOG_INTERACTION
 80: 0x01BB [0x01] GOTO 0x0199

SUBROUTINE_01D4:
 81: 0x01D4 [0x21] END_EVENT
 82: 0x01D5 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x01BE [0x01] GOTO 0x01D4
```

### Event 70

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x01D6     |
| Data Size    | 1986 bytes |
| Instructions | 356        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                   03 00  00 02 10 03 05 00 03 10        ..........
01E0: 03 06 00 04 10 03 0D 00  05 10 03 0E 00 06 10 02  ................
01F0: 0E 00 0A 80 01 0B 02 83  08 00 02 08 00 0E 00 05  ................
0200: 0B 02 03 06 10 0E 00 48  1D 80 23 03 28 10 08 10  .......H..#.(...
0210: 3E 09 10 0A 80 1A 02 05  0F 00 02 00 00 0C 80 80  >...............
0220: 29 02 48 1E 80 23 01 46  08 02 00 00 14 80 80 38  ).H..#.F.......8
0230: 02 48 1F 80 23 01 46 08  06 03 00 2E 24 20 80 03  .H..#.F.....$ ..
0240: 00 0A 80 25 03 03 00 00  10 02 00 10 09 80 00 A3  ...%............
0250: 02 02 00 00 09 80 80 8B  02 42 48 21 80 23 71 00  .........BH!.#q.
0260: 71 01 71 02 02 02 10 14  80 80 75 02 1A 4B 08 01  q.q.......u..K..
0270: 46 08 01 88 02 02 02 10  09 80 80 84 02 48 22 80  F............H".
0280: 23 01 88 02 48 19 80 23  01 A0 02 02 00 00 23 80  #...H..#......#.
0290: 80 9C 02 1A 4B 08 01 46  08 01 A0 02 48 24 80 23  ....K..F....H$.#
02A0: 01 33 08 02 00 10 14 80  00 60 07 06 07 00 03 04  .3.......`......
02B0: 00 0A 80 83 0A 00 15 0A  00 00 80 0B 0A 00 14 0A  ................
02C0: 00 00 80 06 02 10 06 03  10 06 04 10 06 05 10 06  ................
02D0: 06 10 06 07 10 06 08 10  06 09 10 06 00 17 06 01  ................
02E0: 17 06 02 17 06 03 17 06  04 17 06 05 17 06 06 17  ................
02F0: 06 07 17 06 08 17 06 09  17 06 0A 17 06 0B 17 06  ................
0300: 0C 17 06 0D 17 06 0E 17  06 0F 17 06 02 00 02 07  ................
0310: 00 0A 80 80 25 03 3C 02  00 0A 80 09 80 03 0B 00  ....%.<.........
0320: 0A 80 01 5C 03 02 07 00  09 80 80 35 03 03 0B 00  ...\.......5....
0330: 10 80 01 5C 03 02 07 00  14 80 80 45 03 03 0B 00  ...\.......E....
0340: 25 80 01 5C 03 02 07 00  0B 80 80 5C 03 3C 02 00  %..\.......\.<..
0350: 26 80 09 80 03 0B 00 27  80 01 5C 03 06 0C 00 02  &......'..\.....
0360: 0C 00 0F 80 05 4C 05 02  0C 00 0A 80 80 77 03 03  .....L.......w..
0370: 02 10 0A 00 01 27 04 02  0C 00 09 80 80 87 03 03  .....'..........
0380: 03 10 0A 00 01 27 04 02  0C 00 14 80 80 97 03 03  .....'..........
0390: 04 10 0A 00 01 27 04 02  0C 00 0B 80 80 A7 03 03  .....'..........
03A0: 05 10 0A 00 01 27 04 02  0C 00 0C 80 80 B7 03 03  .....'..........
03B0: 06 10 0A 00 01 27 04 02  0C 00 23 80 80 C7 03 03  .....'....#.....
03C0: 07 10 0A 00 01 27 04 02  0C 00 28 80 80 D7 03 03  .....'....(.....
03D0: 08 10 0A 00 01 27 04 02  0C 00 0D 80 80 E7 03 03  .....'..........
03E0: 09 10 0A 00 01 27 04 02  0C 00 0E 80 80 F7 03 03  .....'..........
03F0: 00 17 0A 00 01 27 04 02  0C 00 29 80 80 07 04 03  .....'....).....
0400: 01 17 0A 00 01 27 04 02  0C 00 2A 80 80 17 04 03  .....'....*.....
0410: 02 17 0A 00 01 27 04 02  0C 00 0F 80 80 27 04 03  .....'.......'..
0420: 03 17 0A 00 01 27 04 06  09 00 02 0B 00 25 80 04  .....'.......%..
0430: 4B 04 03 08 00 0B 00 08  08 00 25 80 3E 06 00 08  K.........%.>...
0440: 00 48 04 03 09 00 14 80  01 57 04 3E 05 00 0B 00  .H.......W.>....
0450: 57 04 03 09 00 14 80 02  09 00 14 80 01 7E 04 03  W............~..
0460: 08 00 0A 00 08 08 00 2B  80 02 08 00 0D 00 05 79  .......+.......y
0470: 04 03 09 00 0A 80 01 7E  04 03 09 00 09 80 02 0C  .......~........
0480: 00 0A 80 80 8E 04 03 04  17 09 00 01 3E 05 02 0C  ............>...
0490: 00 09 80 80 9E 04 03 05  17 09 00 01 3E 05 02 0C  ............>...
04A0: 00 14 80 80 AE 04 03 06  17 09 00 01 3E 05 02 0C  ............>...
04B0: 00 0B 80 80 BE 04 03 07  17 09 00 01 3E 05 02 0C  ............>...
04C0: 00 0C 80 80 CE 04 03 08  17 09 00 01 3E 05 02 0C  ............>...
04D0: 00 23 80 80 DE 04 03 09  17 09 00 01 3E 05 02 0C  .#..........>...
04E0: 00 28 80 80 EE 04 03 0A  17 09 00 01 3E 05 02 0C  .(..........>...
04F0: 00 0D 80 80 FE 04 03 0B  17 09 00 01 3E 05 02 0C  ............>...
0500: 00 0E 80 80 0E 05 03 0C  17 09 00 01 3E 05 02 0C  ............>...
0510: 00 29 80 80 1E 05 03 0D  17 09 00 01 3E 05 02 0C  .)..........>...
0520: 00 2A 80 80 2E 05 03 0E  17 09 00 01 3E 05 02 0C  .*..........>...
0530: 00 0F 80 80 3E 05 03 0F  17 09 00 01 3E 05 07 0A  ....>.......>...
0540: 00 00 80 0B 0B 00 0B 0C  00 01 5F 03 24 2C 80 04  .........._.$,..
0550: 00 02 00 25 03 04 00 00  10 02 00 10 0A 80 00 74  ...%...........t
0560: 05 03 04 00 26 80 0C 07  00 08 0A 00 2D 80 01 C3  ....&.......-...
0570: 02 01 5D 07 02 00 10 26  80 00 8A 05 03 04 00 0A  ..]....&........
0580: 80 0B 07 00 01 C3 02 01  5D 07 02 00 10 2E 80 00  ........].......
0590: 95 05 01 5D 07 02 00 10  09 80 80 AA 05 03 08 00  ...]............
05A0: 02 10 03 09 00 04 17 01  91 06 02 00 10 14 80 80  ................
05B0: BF 05 03 08 00 03 10 03  09 00 05 17 01 91 06 02  ................
05C0: 00 10 0B 80 80 D4 05 03  08 00 04 10 03 09 00 06  ................
05D0: 17 01 91 06 02 00 10 0C  80 80 E9 05 03 08 00 05  ................
05E0: 10 03 09 00 07 17 01 91  06 02 00 10 23 80 80 FE  ............#...
05F0: 05 03 08 00 06 10 03 09  00 08 17 01 91 06 02 00  ................
0600: 10 28 80 80 13 06 03 08  00 07 10 03 09 00 09 17  .(..............
0610: 01 91 06 02 00 10 0D 80  80 28 06 03 08 00 08 10  .........(......
0620: 03 09 00 0A 17 01 91 06  02 00 10 0E 80 80 3D 06  ..............=.
0630: 03 08 00 09 10 03 09 00  0B 17 01 91 06 02 00 10  ................
0640: 29 80 80 52 06 03 08 00  00 17 03 09 00 0C 17 01  )..R............
0650: 91 06 02 00 10 2A 80 80  67 06 03 08 00 01 17 03  .....*..g.......
0660: 09 00 0D 17 01 91 06 02  00 10 0F 80 80 7C 06 03  .............|..
0670: 08 00 02 17 03 09 00 0E  17 01 91 06 02 00 10 10  ................
0680: 80 80 91 06 03 08 00 03  17 03 09 00 0F 17 01 91  ................
0690: 06 03 1E 17 08 00 03 1F  17 1E 17 07 1F 17 00 80  ................
06A0: 02 1E 17 0E 00 00 B4 06  03 06 10 1E 17 48 1D 80  .............H..
06B0: 23 01 55 07 02 09 00 0A  80 80 C3 06 48 2F 80 23  #.U.........H/.#
06C0: 01 55 07 02 09 00 09 80  80 46 07 02 0E 00 0A 80  .U.......F......
06D0: 01 DF 06 03 06 10 0E 00  48 30 80 23 01 43 07 24  ........H0.#.C.$
06E0: 31 80 09 80 0A 80 25 02  00 10 0A 80 00 43 07 03  1.....%......C..
06F0: 02 10 32 80 24 33 80 09  80 0A 80 25 02 00 10 0A  ..2.$3.....%....
0700: 80 00 40 07 42 03 01 10  1E 17 43 00 43 01 02 02  ..@.B.....C.C...
0710: 10 18 80 80 1D 07 48 19  80 23 01 3A 07 02 02 10  ......H..#.:....
0720: 34 80 80 2C 07 48 35 80  23 01 3A 07 03 03 10 02  4..,.H5.#.:.....
0730: 80 15 03 10 03 80 48 36  80 23 01 46 08 01 40 07  ......H6.#.F..@.
0740: 01 43 07 01 55 07 02 09  00 14 80 80 55 07 48 37  .C..U.......U.H7
0750: 80 23 01 55 07 08 0A 00  38 80 01 C3 02 01 33 08  .#.U....8.....3.
0760: 02 00 10 0B 80 00 09 08  02 0E 00 0A 80 01 7C 07  ..............|.
0770: 03 06 10 0E 00 48 30 80  23 01 06 08 02 0F 00 0A  .....H0.#.......
0780: 80 00 02 08 83 02 10 15  02 10 00 80 14 02 10 00  ................
0790: 80 24 39 80 09 80 0A 80  25 02 00 10 0A 80 00 FF  .$9.....%.......
07A0: 07 03 02 10 32 80 24 3A  80 09 80 0A 80 25 02 00  ....2.$:.....%..
07B0: 10 0A 80 00 FC 07 42 03  01 10 34 80 43 00 43 01  ......B...4.C.C.
07C0: 02 02 10 18 80 80 CF 07  48 19 80 23 01 F9 07 02  ........H..#....
07D0: 02 10 34 80 80 DE 07 48  35 80 23 01 F9 07 83 02  ..4....H5.#.....
07E0: 10 15 02 10 00 80 14 02  10 00 80 03 03 10 02 10  ................
07F0: 07 03 10 00 80 48 01 80  23 01 FC 07 01 FF 07 01  .....H..#.......
0800: 06 08 48 3B 80 23 01 33  08 02 00 10 0C 80 00 33  ..H;.#.3.......3
0810: 08 48 3C 80 23 03 02 10  02 80 15 02 10 03 80 48  .H<.#..........H
0820: 3D 80 23 48 3E 80 23 03  02 10 32 80 48 3F 80 23  =.#H>.#...2.H?.#
0830: 01 33 08 02 03 00 0A 80  01 46 08 02 03 00 0B 80  .3.......F......
0840: 01 46 08 01 3B 02 06 01  10 21 00 03 01 10 18 80  .F..;....!......
0850: 20 01 46 01 42 45 40 80  F8 FF FF 7F F8 FF FF 7F   .F.BE@.........
0860: 66 64 6F 31 0A 80 55 40  80 F8 FF FF 7F F8 FF FF  fdo1..U@........
0870: 7F 66 64 6F 31 38 0B 80  94 01 F0 FF FF 7F 97 0A  .fdo18..........
0880: 80 09 80 27 03 B2 21 03  01 0A 27 03 B3 21 03 01  ...'..!...'..!..
0890: 08 27 03 B4 21 03 01 08  27 03 B5 21 03 01 08 80  .'..!...'..!....
08A0: B2 21 03 01 80 B3 21 03  01 80 B4 21 03 01 80 B5  .!....!....!....
08B0: 21 03 01 06 10 00 47 00  41 80 42 80 43 80 0A 80  !.....G.A.B.C...
08C0: 47 01 02 02 10 44 80 80  D1 08 48 19 80 23 01 5E  G....D....H..#.^
08D0: 09 02 02 10 34 80 80 E0  08 48 35 80 23 01 5E 09  ....4....H5.#.^.
08E0: 03 10 00 02 10 29 03 F0  FF FF 7F F1 27 04 B2 21  .....)......'..!
08F0: 03 01 03 27 04 B3 21 03  01 03 27 04 B4 21 03 01  ...'..!...'..!..
0900: 03 27 04 B5 21 03 01 03  1C 09 80 45 45 80 F0 FF  .'..!......EE...
0910: FF 7F F0 FF FF 7F 62 61  63 6B 0A 80 4C 45 40 80  ......back..LE@.
0920: F8 FF FF 7F F8 FF FF 7F  66 64 69 31 0A 80 55 40  ........fdi1..U@
0930: 80 F8 FF FF 7F F8 FF FF  7F 66 64 69 31 32 26 80  .........fdi12&.
0940: 28 05 B2 21 03 01 04 27  03 F0 FF FF 7F F2 1C 40  (..!...'.......@
0950: 80 4D 02 10 00 09 80 00  5E 09 48 46 80 23 45 40  .M......^.HF.#E@
0960: 80 F8 FF FF 7F F8 FF FF  7F 66 64 6F 32 0A 80 55  .........fdo2..U
0970: 40 80 F8 FF FF 7F F8 FF  FF 7F 66 64 6F 32 2A 03  @.........fdo2*.
0980: F0 FF FF 7F 46 00 45 40  80 F8 FF FF 7F F8 FF FF  ....F.E@........
0990: 7F 66 64 69 31 0A 80 1B                           .fdi1...        
```

#### Opcodes

```
  0: 0x01D6 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x01DB [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[3]
  2: 0x01E0 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[4]
  3: 0x01E5 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[5]
  4: 0x01EA [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[6]
  5: 0x01EF [0x02] IF !(ExtData[1]->WorkLocal[14] == 0*) GOTO 0x020B
  6: 0x01F7 [0x83] ExtData[1]->WorkLocal[8] = GetGameTime()
  7: 0x01FA [0x02] IF !(ExtData[1]->WorkLocal[8] > ExtData[1]->WorkLocal[14]) GOTO 0x020B
  8: 0x0202 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[14]
  9: 0x0207 [0x48] [System] [9726*]:
    → "A reservation under the name of \u00072\u0008\u00073 has been made for \u00072\u007F+\u0004.\u00073\u007F1\u0000\u0007"
 10: 0x020A [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x020B [0x03] Work_Zone[40] = Work_Zone[8]
 12: 0x0210 [0x3E] IF !(Work_Zone[9] bit 0*) GOTO 0x021A
 13: 0x0217 [0x05] ExtData[1]->WorkLocal[15] = 1
 14: 0x021A [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x0229
 15: 0x0222 [0x48] [System] [9713*]:
    → "The password should now be set to \u00072\u001C\u0000.\u00073\u007F1\u0000\u0007"
 16: 0x0225 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0226 [0x01] GOTO 0x0846
 18: 0x0229 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0238
 19: 0x0231 [0x48] [System] [9735*]:
    → "This gate appears to be for entry only...\u007F1\u0000\u0007"
 20: 0x0234 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0235 [0x01] GOTO 0x0846
 22: 0x0238 [0x06] ExtData[1]->WorkLocal[3] = 0

SUBROUTINE_023B:
 23: 0x023B [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 24: 0x023C [0x24] CREATE_DIALOG(message_id=9691*, default_option=ExtData[1]->WorkLocal[3], option_flags=0*)
    → "Welcome to the Kokba Hostel.\u0007\u000BLeave.\u0007Enter.\u0007Reservations.\u0007Reserve the hostel from now.\u0007Information.\u007F1\u0000\u0007"
 25: 0x0243 [0x25] WAIT_DIALOG_SELECT()
 26: 0x0244 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[0]
 27: 0x0249 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02A3
 28: 0x0251 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x028B
 29: 0x0259 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 30: 0x025A [0x48] [System] [9714*]:
    → "A password is required.\u007F1\u0000\u0007"
 31: 0x025D [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x025E [0x71] USER_INPUT_HANDLER: Open password input dialog (sends packet 0x60)
 33: 0x0260 [0x71] USER_INPUT_HANDLER: Check if player has input or exited
 34: 0x0262 [0x71] USER_INPUT_HANDLER: Check if server responded
 35: 0x0264 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0275
 36: 0x026C [0x1A] CALL_SUBROUTINE(address=0x084B)
 37: 0x026F [0x01] GOTO 0x0846

SUBROUTINE_0288:
 38: 0x0288 [0x01] GOTO 0x02A0
 39: 0x028B [0x02] IF !(ExtData[1]->WorkLocal[0] == 5*) GOTO 0x029C
 40: 0x0293 [0x1A] CALL_SUBROUTINE(address=0x084B)
 41: 0x0296 [0x01] GOTO 0x0846

SUBROUTINE_02A0:
 42: 0x02A0 [0x01] GOTO 0x0833
 43: 0x02A3 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0760
 44: 0x02AB [0x06] ExtData[1]->WorkLocal[7] = 0
 45: 0x02AE [0x03] ExtData[1]->WorkLocal[4] = 0*
 46: 0x02B3 [0x83] ExtData[1]->WorkLocal[10] = GetGameTime()
 47: 0x02B6 [0x15] ExtData[1]->WorkLocal[10] /= 3600*
 48: 0x02BB [0x0B] ExtData[1]->WorkLocal[10]++
 49: 0x02BE [0x14] ExtData[1]->WorkLocal[10] *= 3600*

SUBROUTINE_02C3:
 50: 0x02C3 [0x06] Work_Zone[2] = 0
 51: 0x02C6 [0x06] Work_Zone[3] = 0
 52: 0x02C9 [0x06] Work_Zone[4] = 0
 53: 0x02CC [0x06] Work_Zone[5] = 0
 54: 0x02CF [0x06] Work_Zone[6] = 0
 55: 0x02D2 [0x06] Work_Zone[7] = 0
 56: 0x02D5 [0x06] Work_Zone[8] = 0
 57: 0x02D8 [0x06] Work_Zone[9] = 0
 58: 0x02DB [0x06] Work_Zone_1700[0] = 0
 59: 0x02DE [0x06] Work_Zone_1700[1] = 0
 60: 0x02E1 [0x06] Work_Zone_1700[2] = 0
 61: 0x02E4 [0x06] Work_Zone_1700[3] = 0
 62: 0x02E7 [0x06] Work_Zone_1700[4] = 0
 63: 0x02EA [0x06] Work_Zone_1700[5] = 0
 64: 0x02ED [0x06] Work_Zone_1700[6] = 0
 65: 0x02F0 [0x06] Work_Zone_1700[7] = 0
 66: 0x02F3 [0x06] Work_Zone_1700[8] = 0
 67: 0x02F6 [0x06] Work_Zone_1700[9] = 0
 68: 0x02F9 [0x06] Work_Zone_1700[10] = 0
 69: 0x02FC [0x06] Work_Zone_1700[11] = 0
 70: 0x02FF [0x06] Work_Zone_1700[12] = 0
 71: 0x0302 [0x06] Work_Zone_1700[13] = 0
 72: 0x0305 [0x06] Work_Zone_1700[14] = 0
 73: 0x0308 [0x06] Work_Zone_1700[15] = 0
 74: 0x030B [0x06] ExtData[1]->WorkLocal[2] = 0
 75: 0x030E [0x02] IF !(ExtData[1]->WorkLocal[7] == 0*) GOTO 0x0325
 76: 0x0316 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=0*, condition_work_offset=1*)
 77: 0x031D [0x03] ExtData[1]->WorkLocal[11] = 0*
 78: 0x0322 [0x01] GOTO 0x035C
 79: 0x0325 [0x02] IF !(ExtData[1]->WorkLocal[7] == 1*) GOTO 0x0335
 80: 0x032D [0x03] ExtData[1]->WorkLocal[11] = 12*
 81: 0x0332 [0x01] GOTO 0x035C
 82: 0x0335 [0x02] IF !(ExtData[1]->WorkLocal[7] == 2*) GOTO 0x0345
 83: 0x033D [0x03] ExtData[1]->WorkLocal[11] = 32*
 84: 0x0342 [0x01] GOTO 0x035C
 85: 0x0345 [0x02] IF !(ExtData[1]->WorkLocal[7] == 3*) GOTO 0x035C
 86: 0x034D [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=13*, condition_work_offset=1*)
 87: 0x0354 [0x03] ExtData[1]->WorkLocal[11] = 44*
 88: 0x0359 [0x01] GOTO 0x035C

SUBROUTINE_035C:
 89: 0x035C [0x06] ExtData[1]->WorkLocal[12] = 0

SUBROUTINE_035F:
 90: 0x035F [0x02] IF !(ExtData[1]->WorkLocal[12] > 11*) GOTO 0x054C
 91: 0x0367 [0x02] IF !(ExtData[1]->WorkLocal[12] == 0*) GOTO 0x0377
 92: 0x036F [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[10]
 93: 0x0374 [0x01] GOTO 0x0427
 94: 0x0377 [0x02] IF !(ExtData[1]->WorkLocal[12] == 1*) GOTO 0x0387
 95: 0x037F [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[10]
 96: 0x0384 [0x01] GOTO 0x0427
 97: 0x0387 [0x02] IF !(ExtData[1]->WorkLocal[12] == 2*) GOTO 0x0397
 98: 0x038F [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[10]
 99: 0x0394 [0x01] GOTO 0x0427
100: 0x0397 [0x02] IF !(ExtData[1]->WorkLocal[12] == 3*) GOTO 0x03A7
101: 0x039F [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[10]
102: 0x03A4 [0x01] GOTO 0x0427
103: 0x03A7 [0x02] IF !(ExtData[1]->WorkLocal[12] == 4*) GOTO 0x03B7
104: 0x03AF [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[10]
105: 0x03B4 [0x01] GOTO 0x0427
106: 0x03B7 [0x02] IF !(ExtData[1]->WorkLocal[12] == 5*) GOTO 0x03C7
107: 0x03BF [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[10]
108: 0x03C4 [0x01] GOTO 0x0427
109: 0x03C7 [0x02] IF !(ExtData[1]->WorkLocal[12] == 6*) GOTO 0x03D7
110: 0x03CF [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[10]
111: 0x03D4 [0x01] GOTO 0x0427
112: 0x03D7 [0x02] IF !(ExtData[1]->WorkLocal[12] == 7*) GOTO 0x03E7
113: 0x03DF [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[10]
114: 0x03E4 [0x01] GOTO 0x0427
115: 0x03E7 [0x02] IF !(ExtData[1]->WorkLocal[12] == 8*) GOTO 0x03F7
116: 0x03EF [0x03] Work_Zone_1700[0] = ExtData[1]->WorkLocal[10]
117: 0x03F4 [0x01] GOTO 0x0427
118: 0x03F7 [0x02] IF !(ExtData[1]->WorkLocal[12] == 9*) GOTO 0x0407
119: 0x03FF [0x03] Work_Zone_1700[1] = ExtData[1]->WorkLocal[10]
120: 0x0404 [0x01] GOTO 0x0427
121: 0x0407 [0x02] IF !(ExtData[1]->WorkLocal[12] == 10*) GOTO 0x0417
122: 0x040F [0x03] Work_Zone_1700[2] = ExtData[1]->WorkLocal[10]
123: 0x0414 [0x01] GOTO 0x0427
124: 0x0417 [0x02] IF !(ExtData[1]->WorkLocal[12] == 11*) GOTO 0x0427
125: 0x041F [0x03] Work_Zone_1700[3] = ExtData[1]->WorkLocal[10]
126: 0x0424 [0x01] GOTO 0x0427

SUBROUTINE_0427:
127: 0x0427 [0x06] ExtData[1]->WorkLocal[9] = 0
128: 0x042A [0x02] IF !(ExtData[1]->WorkLocal[11] < 32*) GOTO 0x044B
129: 0x0432 [0x03] ExtData[1]->WorkLocal[8] = ExtData[1]->WorkLocal[11]
130: 0x0437 [0x08] ExtData[1]->WorkLocal[8] -= 32*
131: 0x043C [0x3E] IF !(ExtData[1]->WorkLocal[6] bit ExtData[1]->WorkLocal[8]) GOTO 0x0448
132: 0x0443 [0x03] ExtData[1]->WorkLocal[9] = 2*
133: 0x0448 [0x01] GOTO 0x0457
134: 0x044B [0x3E] IF !(ExtData[1]->WorkLocal[5] bit ExtData[1]->WorkLocal[11]) GOTO 0x0457
135: 0x0452 [0x03] ExtData[1]->WorkLocal[9] = 2*

SUBROUTINE_0457:
136: 0x0457 [0x02] IF !(ExtData[1]->WorkLocal[9] == 2*) GOTO 0x047E
137: 0x045F [0x03] ExtData[1]->WorkLocal[8] = ExtData[1]->WorkLocal[10]
138: 0x0464 [0x08] ExtData[1]->WorkLocal[8] -= 172800*
139: 0x0469 [0x02] IF !(ExtData[1]->WorkLocal[8] > ExtData[1]->WorkLocal[13]) GOTO 0x0479
140: 0x0471 [0x03] ExtData[1]->WorkLocal[9] = 0*
141: 0x0476 [0x01] GOTO 0x047E
142: 0x0479 [0x03] ExtData[1]->WorkLocal[9] = 1*

SUBROUTINE_047E:
143: 0x047E [0x02] IF !(ExtData[1]->WorkLocal[12] == 0*) GOTO 0x048E
144: 0x0486 [0x03] Work_Zone_1700[4] = ExtData[1]->WorkLocal[9]
145: 0x048B [0x01] GOTO 0x053E
146: 0x048E [0x02] IF !(ExtData[1]->WorkLocal[12] == 1*) GOTO 0x049E
147: 0x0496 [0x03] Work_Zone_1700[5] = ExtData[1]->WorkLocal[9]
148: 0x049B [0x01] GOTO 0x053E
149: 0x049E [0x02] IF !(ExtData[1]->WorkLocal[12] == 2*) GOTO 0x04AE
150: 0x04A6 [0x03] Work_Zone_1700[6] = ExtData[1]->WorkLocal[9]
151: 0x04AB [0x01] GOTO 0x053E
152: 0x04AE [0x02] IF !(ExtData[1]->WorkLocal[12] == 3*) GOTO 0x04BE
153: 0x04B6 [0x03] Work_Zone_1700[7] = ExtData[1]->WorkLocal[9]
154: 0x04BB [0x01] GOTO 0x053E
155: 0x04BE [0x02] IF !(ExtData[1]->WorkLocal[12] == 4*) GOTO 0x04CE
156: 0x04C6 [0x03] Work_Zone_1700[8] = ExtData[1]->WorkLocal[9]
157: 0x04CB [0x01] GOTO 0x053E
158: 0x04CE [0x02] IF !(ExtData[1]->WorkLocal[12] == 5*) GOTO 0x04DE
159: 0x04D6 [0x03] Work_Zone_1700[9] = ExtData[1]->WorkLocal[9]
160: 0x04DB [0x01] GOTO 0x053E
161: 0x04DE [0x02] IF !(ExtData[1]->WorkLocal[12] == 6*) GOTO 0x04EE
162: 0x04E6 [0x03] Work_Zone_1700[10] = ExtData[1]->WorkLocal[9]
163: 0x04EB [0x01] GOTO 0x053E
164: 0x04EE [0x02] IF !(ExtData[1]->WorkLocal[12] == 7*) GOTO 0x04FE
165: 0x04F6 [0x03] Work_Zone_1700[11] = ExtData[1]->WorkLocal[9]
166: 0x04FB [0x01] GOTO 0x053E
167: 0x04FE [0x02] IF !(ExtData[1]->WorkLocal[12] == 8*) GOTO 0x050E
168: 0x0506 [0x03] Work_Zone_1700[12] = ExtData[1]->WorkLocal[9]
169: 0x050B [0x01] GOTO 0x053E
170: 0x050E [0x02] IF !(ExtData[1]->WorkLocal[12] == 9*) GOTO 0x051E
171: 0x0516 [0x03] Work_Zone_1700[13] = ExtData[1]->WorkLocal[9]
172: 0x051B [0x01] GOTO 0x053E
173: 0x051E [0x02] IF !(ExtData[1]->WorkLocal[12] == 10*) GOTO 0x052E
174: 0x0526 [0x03] Work_Zone_1700[14] = ExtData[1]->WorkLocal[9]
175: 0x052B [0x01] GOTO 0x053E
176: 0x052E [0x02] IF !(ExtData[1]->WorkLocal[12] == 11*) GOTO 0x053E
177: 0x0536 [0x03] Work_Zone_1700[15] = ExtData[1]->WorkLocal[9]
178: 0x053B [0x01] GOTO 0x053E

SUBROUTINE_053E:
179: 0x053E [0x07] ExtData[1]->WorkLocal[10] += 3600*
180: 0x0543 [0x0B] ExtData[1]->WorkLocal[11]++
181: 0x0546 [0x0B] ExtData[1]->WorkLocal[12]++
182: 0x0549 [0x01] GOTO 0x035F
183: 0x054C [0x24] CREATE_DIALOG(message_id=9717*, default_option=ExtData[1]->WorkLocal[4], option_flags=ExtData[1]->WorkLocal[2])
    → "Kokba Hostel reservations.\u0007\u000BPrevious page.\u0007\u007F+\u0000 (\u000C\u000C[?/-/x])\u0007\u007F+\u0001 (\u000C[?/-/x])\u0007\u007F+\u0002 (\u000C\u000E[?/-/x])\u0007\u007F+\u0003 (\u000C\u000F[?/-/x])\u0007\u007F+\u0004 (\u000C\u0010[?/-/x])\u0007\u007F+\u0005 (\u000C\u0011[?/-/x])\u0007\u007F+\u0006 (\u000C\u0012[?/-/x])\u0007\u007F+\u0007 (\u000C\u0013[?/-/x])\u0007\u007F+\u0008 (\u000C\u0014[?/-/x])\u0007\u007F+	 (\u000C\u0015[?/-/x])\u0007\u007F+
 (\u000C\u0016[?/-/x])\u0007\u007F+\u000B (\u000C\u0017[?/-/x])\u0007Next page.\u0007Return to main menu.\u007F1\u0000\u0007"
184: 0x0553 [0x25] WAIT_DIALOG_SELECT()
185: 0x0554 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[0]
186: 0x0559 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0574
187: 0x0561 [0x03] ExtData[1]->WorkLocal[4] = 13*
188: 0x0566 [0x0C] ExtData[1]->WorkLocal[7]--
189: 0x0569 [0x08] ExtData[1]->WorkLocal[10] -= 86400*
190: 0x056E [0x01] GOTO 0x02C3

SUBROUTINE_0691:
191: 0x0691 [0x03] Work_Zone_1700[30] = ExtData[1]->WorkLocal[8]
192: 0x0696 [0x03] Work_Zone_1700[31] = Work_Zone_1700[30]
193: 0x069B [0x07] Work_Zone_1700[31] += 3600*
194: 0x06A0 [0x02] IF !(Work_Zone_1700[30] == ExtData[1]->WorkLocal[14]) GOTO 0x06B4
195: 0x06A8 [0x03] Work_Zone[6] = Work_Zone_1700[30]
196: 0x06AD [0x48] [System] [9726*]:
    → "A reservation under the name of \u00072\u0008\u00073 has been made for \u00072\u007F+\u0004.\u00073\u007F1\u0000\u0007"
197: 0x06B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
198: 0x06B1 [0x01] GOTO 0x0755
199: 0x06B4 [0x02] IF !(ExtData[1]->WorkLocal[9] == 0*) GOTO 0x06C3
200: 0x06BC [0x48] [System] [9719*]:
    → "The reservation for the \u00072\u007F+&\u00073 to \u00072\u007F+'\u00073 time slot has been lost.\u007F1\u0000\u0007"
201: 0x06BF [0x23] WAIT_FOR_DIALOG_INTERACTION
202: 0x06C0 [0x01] GOTO 0x0755
203: 0x06C3 [0x02] IF !(ExtData[1]->WorkLocal[9] == 1*) GOTO 0x0746
204: 0x06CB [0x02] IF !(ExtData[1]->WorkLocal[14] == 0*) GOTO 0x06DF
205: 0x06D3 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[14]
206: 0x06D8 [0x48] [System] [9720*]:
    → "A reservation under the name of \u00072\u0008\u00073 has already been made for \u00072\u007F+\u0004.\u00073\u007F1\u0000\u0007"
207: 0x06DB [0x23] WAIT_FOR_DIALOG_INTERACTION
208: 0x06DC [0x01] GOTO 0x0743
209: 0x06DF [0x24] CREATE_DIALOG(message_id=9721*, default_option=1*, option_flags=0*)
    → "Reserve from \u007F+&?\u0007\u000BYes.\u0007No.\u007F1\u0000\u0007"
210: 0x06E6 [0x25] WAIT_DIALOG_SELECT()
211: 0x06E7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0743
212: 0x06EF [0x03] Work_Zone[2] = 498*
213: 0x06F4 [0x24] CREATE_DIALOG(message_id=9722*, default_option=1*, option_flags=0*)
    → "The reservation fee is 
\u0000 gil.\u0007\u000BPay the fee.\u0007Forget it.\u007F1\u0000\u0007"
214: 0x06FB [0x25] WAIT_DIALOG_SELECT()
215: 0x06FC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0740
216: 0x0704 [0x42] SET_CLI_EVENT_CANCEL_DATA()
217: 0x0705 [0x03] Work_Zone[1] = Work_Zone_1700[30]
218: 0x070A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
219: 0x070C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
220: 0x070E [0x02] IF !(Work_Zone[2] == 4294967295*) GOTO 0x071D
221: 0x0716 [0x48] [System] [9724*]:
    → "There appears to have been some trouble with the reservation system.\u007F1\u0000\u0007"
222: 0x0719 [0x23] WAIT_FOR_DIALOG_INTERACTION
223: 0x071A [0x01] GOTO 0x073A
224: 0x071D [0x02] IF !(Work_Zone[2] == 4294967294*) GOTO 0x072C
225: 0x0725 [0x48] [System] [233*]:
    → "You do not have enough gil.\u007F1\u0000\u0007"
226: 0x0728 [0x23] WAIT_FOR_DIALOG_INTERACTION
227: 0x0729 [0x01] GOTO 0x073A
228: 0x072C [0x03] Work_Zone[3] = 900*
229: 0x0731 [0x15] Work_Zone[3] /= 60*
230: 0x0736 [0x48] [System] [9725*]:
    → "You have successfully made a reservation from \u00072\u007F+&\u00073!\u0007The hostel reception will be available from 
\u0001 \u007F\u0012\u0001[minute/minutes] before the reservation.\u007F1\u0000\u0007"
231: 0x0739 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_073A:
232: 0x073A [0x01] GOTO 0x0846

SUBROUTINE_0740:
233: 0x0740 [0x01] GOTO 0x0743

SUBROUTINE_0743:
234: 0x0743 [0x01] GOTO 0x0755
235: 0x0746 [0x02] IF !(ExtData[1]->WorkLocal[9] == 2*) GOTO 0x0755
236: 0x074E [0x48] [System] [9718*]:
    → "The time slot from \u00072\u007F+&\u00073 to \u00072\u007F+'\u00073 is already reserved.\u007F1\u0000\u0007"
237: 0x0751 [0x23] WAIT_FOR_DIALOG_INTERACTION
238: 0x0752 [0x01] GOTO 0x0755

SUBROUTINE_0755:
239: 0x0755 [0x08] ExtData[1]->WorkLocal[10] -= 43200*
240: 0x075A [0x01] GOTO 0x02C3

SUBROUTINE_075D:
241: 0x075D [0x01] GOTO 0x0833
242: 0x0760 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0809
243: 0x0768 [0x02] IF !(ExtData[1]->WorkLocal[14] == 0*) GOTO 0x077C
244: 0x0770 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[14]
245: 0x0775 [0x48] [System] [9720*]:
    → "A reservation under the name of \u00072\u0008\u00073 has already been made for \u00072\u007F+\u0004.\u00073\u007F1\u0000\u0007"
246: 0x0778 [0x23] WAIT_FOR_DIALOG_INTERACTION
247: 0x0779 [0x01] GOTO 0x0806
248: 0x077C [0x02] IF !(ExtData[1]->WorkLocal[15] == 0*) GOTO 0x0802
249: 0x0784 [0x83] Work_Zone[2] = GetGameTime()
250: 0x0787 [0x15] Work_Zone[2] /= 3600*
251: 0x078C [0x14] Work_Zone[2] *= 3600*
252: 0x0791 [0x24] CREATE_DIALOG(message_id=9729*, default_option=1*, option_flags=0*)
    → "Reserve the current time slot?\u0007\u000BYes.\u0007No.\u007F1\u0000\u0007"
253: 0x0798 [0x25] WAIT_DIALOG_SELECT()
254: 0x0799 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x07FF
255: 0x07A1 [0x03] Work_Zone[2] = 498*
256: 0x07A6 [0x24] CREATE_DIALOG(message_id=9730*, default_option=1*, option_flags=0*)
    → "The reservation fee is 
\u0000 gil.\u0007\u000BPay the fee.\u0007Forget it.\u007F1\u0000\u0007"
257: 0x07AD [0x25] WAIT_DIALOG_SELECT()
258: 0x07AE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x07FC
259: 0x07B6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
260: 0x07B7 [0x03] Work_Zone[1] = 4294967294*
261: 0x07BC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
262: 0x07BE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
263: 0x07C0 [0x02] IF !(Work_Zone[2] == 4294967295*) GOTO 0x07CF
264: 0x07C8 [0x48] [System] [9724*]:
    → "There appears to have been some trouble with the reservation system.\u007F1\u0000\u0007"
265: 0x07CB [0x23] WAIT_FOR_DIALOG_INTERACTION
266: 0x07CC [0x01] GOTO 0x07F9
267: 0x07CF [0x02] IF !(Work_Zone[2] == 4294967294*) GOTO 0x07DE
268: 0x07D7 [0x48] [System] [233*]:
    → "You do not have enough gil.\u007F1\u0000\u0007"
269: 0x07DA [0x23] WAIT_FOR_DIALOG_INTERACTION
270: 0x07DB [0x01] GOTO 0x07F9
271: 0x07DE [0x83] Work_Zone[2] = GetGameTime()
272: 0x07E1 [0x15] Work_Zone[2] /= 3600*
273: 0x07E6 [0x14] Work_Zone[2] *= 3600*
274: 0x07EB [0x03] Work_Zone[3] = Work_Zone[2]
275: 0x07F0 [0x07] Work_Zone[3] += 3600*
276: 0x07F5 [0x48] [System] [9727*]:
    → "The reception period for the \u00072\u007F+\u0000\u00073 to \u00072\u007F+\u0001\u00073 time slot has ended!\u0007You can now begin the process of setting options and creating a password.\u007F1\u0000\u0007"
277: 0x07F8 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_07F9:
278: 0x07F9 [0x01] GOTO 0x07FC

SUBROUTINE_07FC:
279: 0x07FC [0x01] GOTO 0x07FF

SUBROUTINE_07FF:
280: 0x07FF [0x01] GOTO 0x0806
281: 0x0802 [0x48] [System] [9693*]:
    → "The hostel is currently occupied.\u007F1\u0000\u0007"
282: 0x0805 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0806:
283: 0x0806 [0x01] GOTO 0x0833
284: 0x0809 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0833
285: 0x0811 [0x48] [System] [9731*]:
    → "The Kokba Hostel is a room that can be reserved for private functions in time slots of one hour (Earth time). Customers may make reservations for up to two days in advance, but can only have one active reservation at a time.\u007F1\u0000\u0007"
286: 0x0814 [0x23] WAIT_FOR_DIALOG_INTERACTION
287: 0x0815 [0x03] Work_Zone[2] = 900*
288: 0x081A [0x15] Work_Zone[2] /= 60*
289: 0x081F [0x48] [System] [9732*]:
    → "The hostel reception will be available 
\u0000 \u007F\u0012\u0000[minute/minutes] before a reservation begins. If you have not confirmed your reservation before the end of the reception period, your time slot will become available for other customers to reserve. Should another customer reserve your time slot, your reservation will be canceled.\u007F1\u0000\u0007"
290: 0x0822 [0x23] WAIT_FOR_DIALOG_INTERACTION
291: 0x0823 [0x48] [System] [9733*]:
    → "The hostel will become available for your private use after the reception period ends. You will be asked to create a password before entering the hostel. Only customers who know the correct password will be able to enter during the reserved time slot.\u007F1\u0000\u0007"
292: 0x0826 [0x23] WAIT_FOR_DIALOG_INTERACTION
293: 0x0827 [0x03] Work_Zone[2] = 498*
294: 0x082C [0x48] [System] [9734*]:
    → "After confirming the reservation, other customers will be charged a one-time fee of 
\u0000 gil upon entry. Please be aware that no refunds will be made in the case of a cancellation.\u007F1\u0000\u0007"
295: 0x082F [0x23] WAIT_FOR_DIALOG_INTERACTION
296: 0x0830 [0x01] GOTO 0x0833

SUBROUTINE_0833:
297: 0x0833 [0x02] IF !(ExtData[1]->WorkLocal[3] == 0*) GOTO 0x0846
298: 0x083B [0x02] IF !(ExtData[1]->WorkLocal[3] == 3*) GOTO 0x0846
299: 0x0843 [0x01] GOTO 0x023B

SUBROUTINE_0846:
300: 0x0846 [0x06] Work_Zone[1] = 0
301: 0x0849 [0x21] END_EVENT
302: 0x084A [0x00] END_REQSTACK()

SUBROUTINE_084B:
303: 0x084B [0x03] Work_Zone[1] = 4294967295*
304: 0x0850 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
305: 0x0852 [0x46] CAMERA_CONTROL: Disable user control
306: 0x0854 [0x42] SET_CLI_EVENT_CANCEL_DATA()
307: 0x0855 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
308: 0x0866 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
309: 0x0875 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
310: 0x0878 [0x94] LocalPlayer->Render.Flags3 ^= 0x01
311: 0x087E [0x97] SAVE_SET_WIND_VALUES(wind_base=0x800A, wind_width=0x8009)
312: 0x0883 [0x27] REQ_SET(priority=0x03, entity_id=Attendant (ID: 16982450/0x010321B2), tag_num=0x0A)
313: 0x088A [0x27] REQ_SET(priority=0x03, entity_id=Attendant (ID: 16982451/0x010321B3), tag_num=0x08)
314: 0x0891 [0x27] REQ_SET(priority=0x03, entity_id=Attendant (ID: 16982452/0x010321B4), tag_num=0x08)
315: 0x0898 [0x27] REQ_SET(priority=0x03, entity_id=Attendant (ID: 16982453/0x010321B5), tag_num=0x08)
316: 0x089F [0x80] LOAD_WAIT(entity=Attendant (ID: 16982450/0x010321B2))
317: 0x08A4 [0x80] LOAD_WAIT(entity=Attendant (ID: 16982451/0x010321B3))
318: 0x08A9 [0x80] LOAD_WAIT(entity=Attendant (ID: 16982452/0x010321B4))
319: 0x08AE [0x80] LOAD_WAIT(entity=Attendant (ID: 16982453/0x010321B5))
320: 0x08B3 [0x06] ExtData[1]->WorkLocal[16] = 0
321: 0x08B6 [0x47] UPDATE_PLAYER_POS(169.853*, -63.926*, -6.000*, yaw=0.0°*)
322: 0x08C0 [0x47] WAIT_PLAYER_POS_UPDATE
323: 0x08C2 [0x02] IF !(Work_Zone[2] == 4294967293*) GOTO 0x08D1
324: 0x08CA [0x48] [System] [9724*]:
    → "There appears to have been some trouble with the reservation system.\u007F1\u0000\u0007"
325: 0x08CD [0x23] WAIT_FOR_DIALOG_INTERACTION
326: 0x08CE [0x01] GOTO 0x095E
327: 0x08D1 [0x02] IF !(Work_Zone[2] == 4294967294*) GOTO 0x08E0
328: 0x08D9 [0x48] [System] [233*]:
    → "You do not have enough gil.\u007F1\u0000\u0007"
329: 0x08DC [0x23] WAIT_FOR_DIALOG_INTERACTION
330: 0x08DD [0x01] GOTO 0x095E
331: 0x08E0 [0x03] ExtData[1]->WorkLocal[16] = Work_Zone[2]
332: 0x08E5 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0xF1)
333: 0x08EC [0x27] REQ_SET(priority=0x04, entity_id=Attendant (ID: 16982450/0x010321B2), tag_num=0x03)
334: 0x08F3 [0x27] REQ_SET(priority=0x04, entity_id=Attendant (ID: 16982451/0x010321B3), tag_num=0x03)
335: 0x08FA [0x27] REQ_SET(priority=0x04, entity_id=Attendant (ID: 16982452/0x010321B4), tag_num=0x03)
336: 0x0901 [0x27] REQ_SET(priority=0x04, entity_id=Attendant (ID: 16982453/0x010321B5), tag_num=0x03)
337: 0x0908 [0x1C] WAIT(1* ticks)
338: 0x090B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "back" with entities [LocalPlayer, LocalPlayer], work=[108*, 0*]
339: 0x091C [0x4C] EventEntity->StatusEvent = 8 // Open door
340: 0x091D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
341: 0x092E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [EventEntity, EventEntity], work=200*
342: 0x093D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
343: 0x0940 [0x28] REQ_SET_WITH_CONDITIONS(priority=0x05, target_entity=Attendant (ID: 16982450/0x010321B2), tag_num=0x04)
344: 0x0947 [0x27] REQ_SET(priority=0x03, entity_id=LocalPlayer, tag_num=0xF2)
345: 0x094E [0x1C] WAIT(200* ticks)
346: 0x0951 [0x4D] EventEntity->StatusEvent = 9 // Close door
347: 0x0952 [0x02] IF !(ExtData[1]->WorkLocal[16] == 1*) GOTO 0x095E
348: 0x095A [0x48] [System] [9739*]:
    → "You have received a party pack of temporary items! These items can only be used within the hostel.\u0000\u0007"
349: 0x095D [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_095E:
350: 0x095E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [EventEntity, EventEntity], work=[200*, 0*]
351: 0x096F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [EventEntity, EventEntity], work=200*
352: 0x097E [0x2A] GET_REQ_LEVEL(level=3, entity_id=LocalPlayer)
353: 0x0984 [0x46] CAMERA_CONTROL: Restore default settings
354: 0x0986 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
355: 0x0997 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0272 [0x01] GOTO 0x0288
# Dead code (unreachable instructions):
     0x0299 [0x01] GOTO 0x02A0
# Dead code (unreachable instructions):
     0x0571 [0x01] GOTO 0x075D
     0x0587 [0x01] GOTO 0x075D
# Dead code (unreachable instructions):
     0x073D [0x01] GOTO 0x0740
```
