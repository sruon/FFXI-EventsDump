# 17494622 - Lewenhart

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 364 bytes                            |
| Total Events     | 2                                    |
| References Count | 8                                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [501](#event-501)     | 0x0001       |    307 |             82 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1EEE      |        7918 |
|       2 | 0x0000      |           0 |
|       3 | 0x1EEF      |        7919 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x103A      |        4154 |
|       7 | 0x1EF0      |        7920 |

## String References

- **7918**: Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest.
- **7919**: The lives and dreams that are shattered on the battlefield... And the burden of sorrow that is inherited by loved ones left behind... It is of this that we bards sing, lest the lessons they teach us be forgotten for all time.
- **7920**: $0...! Thank you kindly, friend. With this offering, those who have been laid to rest here may finally know true peace.

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

### Event 501

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 307 bytes |
| Instructions | 82        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 20 01 42 1E  F0 FF FF 7F 03 01 00 03    .B .B.........
0010: 10 03 02 00 04 10 03 03  00 05 10 02 02 10 00 80  ................
0020: 00 2A 00 1D 01 80 23 01  30 01 02 03 00 02 80 80  .*....#.0.......
0030: 39 00 1D 01 80 23 01 30  01 02 03 00 00 80 80 AD  9....#.0........
0040: 00 02 01 00 02 80 80 50  00 1D 01 80 23 01 AA 00  .......P....#...
0050: 02 01 00 00 80 80 6E 00  02 02 00 00 80 00 67 00  ......n.......g.
0060: 1D 03 80 23 01 6B 00 1D  01 80 23 01 AA 00 02 01  ...#.k....#.....
0070: 00 04 80 80 8C 00 02 02  00 00 80 00 85 00 1D 03  ................
0080: 80 23 01 89 00 1D 01 80  23 01 AA 00 02 01 00 05  .#......#.......
0090: 80 80 AA 00 02 02 00 00  80 00 A3 00 1D 03 80 23  ...............#
00A0: 01 A7 00 1D 01 80 23 01  AA 00 01 30 01 02 03 00  ......#....0....
00B0: 04 80 80 30 01 02 01 00  02 80 80 C4 00 1D 01 80  ...0............
00C0: 23 01 2D 01 02 01 00 00  80 80 E7 00 02 02 00 04  #.-.............
00D0: 80 00 E0 00 03 02 10 06  80 1D 07 80 23 01 E4 00  ............#...
00E0: 1D 01 80 23 01 2D 01 02  01 00 04 80 80 0A 01 02  ...#.-..........
00F0: 02 00 04 80 00 03 01 03  02 10 06 80 1D 07 80 23  ...............#
0100: 01 07 01 1D 01 80 23 01  2D 01 02 01 00 05 80 80  ......#.-.......
0110: 2D 01 02 02 00 04 80 00  26 01 03 02 10 06 80 1D  -.......&.......
0120: 07 80 23 01 2A 01 1D 01  80 23 01 2D 01 01 30 01  ..#.*....#.-..0.
0130: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0006 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0007 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x000C [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  6: 0x0011 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  7: 0x0016 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  8: 0x001B [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x002A
  9: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 10: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0027 [0x01] GOTO 0x0130
 12: 0x002A [0x02] IF !(ExtData[1]->WorkLocal[3] == 0*) GOTO 0x0039
 13: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 14: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0036 [0x01] GOTO 0x0130
 16: 0x0039 [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x00AD
 17: 0x0041 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0050
 18: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 19: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x004D [0x01] GOTO 0x00AA
 21: 0x0050 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x006E
 22: 0x0058 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x0067
 23: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=7919*)
    → "The lives and dreams that are shattered on the battlefield... And the burden of sorrow that is inherited by loved ones left behind... It is of this that we bards sing, lest the lessons they teach us be forgotten for all time."
 24: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0064 [0x01] GOTO 0x006B
 26: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 27: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_006B:
 28: 0x006B [0x01] GOTO 0x00AA
 29: 0x006E [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x008C
 30: 0x0076 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x0085
 31: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=7919*)
    → "The lives and dreams that are shattered on the battlefield... And the burden of sorrow that is inherited by loved ones left behind... It is of this that we bards sing, lest the lessons they teach us be forgotten for all time."
 32: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0082 [0x01] GOTO 0x0089
 34: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 35: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0089:
 36: 0x0089 [0x01] GOTO 0x00AA
 37: 0x008C [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x00AA
 38: 0x0094 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00A3
 39: 0x009C [0x1D] PRINT_EVENT_MESSAGE(message_id=7919*)
    → "The lives and dreams that are shattered on the battlefield... And the burden of sorrow that is inherited by loved ones left behind... It is of this that we bards sing, lest the lessons they teach us be forgotten for all time."
 40: 0x009F [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x00A0 [0x01] GOTO 0x00A7
 42: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 43: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00A7:
 44: 0x00A7 [0x01] GOTO 0x00AA

SUBROUTINE_00AA:
 45: 0x00AA [0x01] GOTO 0x0130
 46: 0x00AD [0x02] IF !(ExtData[1]->WorkLocal[3] == 2*) GOTO 0x0130
 47: 0x00B5 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00C4
 48: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 49: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x00C1 [0x01] GOTO 0x012D
 51: 0x00C4 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x00E7
 52: 0x00CC [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x00E0
 53: 0x00D4 [0x03] Work_Zone[2] = 4154*
 54: 0x00D9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7920*)
    → "$0...! Thank you kindly, friend. With this offering, those who have been laid to rest here may finally know true peace."
 55: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x00DD [0x01] GOTO 0x00E4
 57: 0x00E0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 58: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00E4:
 59: 0x00E4 [0x01] GOTO 0x012D
 60: 0x00E7 [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x010A
 61: 0x00EF [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x0103
 62: 0x00F7 [0x03] Work_Zone[2] = 4154*
 63: 0x00FC [0x1D] PRINT_EVENT_MESSAGE(message_id=7920*)
    → "$0...! Thank you kindly, friend. With this offering, those who have been laid to rest here may finally know true peace."
 64: 0x00FF [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x0100 [0x01] GOTO 0x0107
 66: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 67: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0107:
 68: 0x0107 [0x01] GOTO 0x012D
 69: 0x010A [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x012D
 70: 0x0112 [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x0126
 71: 0x011A [0x03] Work_Zone[2] = 4154*
 72: 0x011F [0x1D] PRINT_EVENT_MESSAGE(message_id=7920*)
    → "$0...! Thank you kindly, friend. With this offering, those who have been laid to rest here may finally know true peace."
 73: 0x0122 [0x23] WAIT_FOR_DIALOG_INTERACTION
 74: 0x0123 [0x01] GOTO 0x012A
 75: 0x0126 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "Never-ending is the cycle of torment and death. Ruthless is its grasp on even those poor souls whose only wish is for eternal rest."
 76: 0x0129 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_012A:
 77: 0x012A [0x01] GOTO 0x012D

SUBROUTINE_012D:
 78: 0x012D [0x01] GOTO 0x0130

SUBROUTINE_0130:
 79: 0x0130 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 80: 0x0132 [0x21] END_EVENT
 81: 0x0133 [0x00] END_REQSTACK()
```
