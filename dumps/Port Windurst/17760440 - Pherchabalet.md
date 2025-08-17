# 17760440 - Pherchabalet

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 416 bytes               |
| Total Events     | 2                       |
| References Count | 25                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [553](#event-553)     | 0x0001       |    291 |             82 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x31E3      |       12771 |
|       2 | 0x31F1      |       12785 |
|       3 | 0x0078      |         120 |
|       4 | 0x31F2      |       12786 |
|       5 | 0x31E4      |       12772 |
|       6 | 0x31E5      |       12773 |
|       7 | 0x0001      |           1 |
|       8 | 0x31E6      |       12774 |
|       9 | 0xFFFFFFFF  |  4294967295 |
|      10 | 0xFFFFFFFE  |  4294967294 |
|      11 | 0x31F0      |       12784 |
|      12 | 0x31E7      |       12775 |
|      13 | 0x0004      |           4 |
|      14 | 0x0003      |           3 |
|      15 | 0x31E8      |       12776 |
|      16 | 0x31E9      |       12777 |
|      17 | 0x0002      |           2 |
|      18 | 0x31EA      |       12778 |
|      19 | 0x31EB      |       12779 |
|      20 | 0x31EC      |       12780 |
|      21 | 0x31ED      |       12781 |
|      22 | 0x31EE      |       12782 |
|      23 | 0x31EF      |       12783 |
|      24 | 0x40000000  |  1073741824 |

## String References

- **12771**: Here you can learn the fate and fortune of an adventuring duo.
- **12772**: For a mere 120 gil, I will divine what today will bring for you and %0.
- **12773**: Pay 120 gil for a fortune telling? [Pay up./I make my own fortune.]
- **12774**: Now, let us see what the winds portend...
- **12775**: Adventuring with %0 today will [bring you great fortune!/be highly profitable./bring fair fortune./be mutually advantageous./bring misfortune./be perilous./be disastrous!]
- **12776**: Good fortune fills your cup to overflowing. Be sure to share it with those less blessed by fate.
- **12777**: Stand together and you have little to fear. With your combined strength, you can overcome any obstacle.
- **12778**: Do not let your good fortune blind you to danger. Pitfalls aplenty await the unwary traveler.
- **12779**: Happiness is a state of mind. You can find laughter in even the most desperate of situations.
- **12780**: The day ahead will be filled with trials and tribulations, but in time the path before you will run smooth once more.
- **12781**: There may be clashes of opinion today, but approach each other with an open mind and all will be well.
- **12782**: You must rely on each others' strengths to overcome the difficulties you will face today. Don't let petty squabbles bring your downfall.
- **12783**: Please accept this modest gift in celebration of your good fortune.
- **12784**: Either you or %0 has already heard fate's fickle will today. You may only have your fortune told once every Vana'dielian day.
- **12785**: Form a party with the person you wish to check your fortune with, and then speak with me for a reading of your fate.
- **12786**: You need 120 gil to have your fortune told.

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

### Event 553

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 291 bytes |
| Instructions | 82        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 02 05  10 00 80 00 1D 01 1D 01   ...............
0010: 80 23 02 03 10 00 80 00  21 00 1D 02 80 23 01 1A  .#......!....#..
0020: 01 02 04 10 00 80 00 16  01 02 02 10 03 80 03 38  ...............8
0030: 00 1D 04 80 23 01 13 01  1D 05 80 23 24 06 80 07  ....#......#$...
0040: 80 00 80 25 02 00 10 00  80 00 03 01 1D 08 80 23  ...%...........#
0050: 42 03 01 10 03 10 43 00  43 01 02 03 10 09 80 00  B.....C.C.......
0060: 64 00 21 00 02 03 10 0A  80 00 72 00 1D 0B 80 23  d.!.......r....#
0070: 21 00 1D 0C 80 23 02 03  10 0D 80 03 C2 00 13 00  !....#..........
0080: 00 0E 80 02 00 00 00 80  80 92 00 1D 0F 80 23 01  ..............#.
0090: BF 00 02 00 00 07 80 80  A1 00 1D 10 80 23 01 BF  .............#..
00A0: 00 02 00 00 11 80 80 B0  00 1D 12 80 23 01 BF 00  ............#...
00B0: 02 00 00 0E 80 80 BF 00  1D 13 80 23 01 BF 00 01  ...........#....
00C0: F4 00 13 00 00 11 80 02  00 00 00 80 80 D6 00 1D  ................
00D0: 14 80 23 01 F4 00 02 00  00 07 80 80 E5 00 1D 15  ..#.............
00E0: 80 23 01 F4 00 02 00 00  11 80 80 F4 00 1D 16 80  .#..............
00F0: 23 01 F4 00 02 03 10 11  80 03 00 01 1D 17 80 23  #..............#
0100: 01 13 01 02 00 10 07 80  00 13 01 03 01 10 18 80  ................
0110: 01 13 01 01 1A 01 1D 0B  80 23 01 22 01 42 1D 17  .........#.".B..
0120: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x02] IF !(Work_Zone[5] == 0*) GOTO 0x011D
  2: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=12771*)
    → "Here you can learn the fate and fortune of an adventuring duo."
  3: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0012 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0021
  5: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=12785*)
    → "Form a party with the person you wish to check your fortune with, and then speak with me for a reading of your fate."
  6: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001E [0x01] GOTO 0x011A
  8: 0x0021 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0116
  9: 0x0029 [0x02] IF !(Work_Zone[2] >= 120*) GOTO 0x0038
 10: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=12786*)
    → "You need 120 gil to have your fortune told."
 11: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0035 [0x01] GOTO 0x0113
 13: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=12772*)
    → "For a mere 120 gil, I will divine what today will bring for you and %0."
 14: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x003C [0x24] CREATE_DIALOG(message_id=12773*, default_option=1*, option_flags=0*)
    → "Pay 120 gil for a fortune telling? [Pay up./I make my own fortune.]"
 16: 0x0043 [0x25] WAIT_DIALOG_SELECT()
 17: 0x0044 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0103
 18: 0x004C [0x1D] PRINT_EVENT_MESSAGE(message_id=12774*)
    → "Now, let us see what the winds portend..."
 19: 0x004F [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0050 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 21: 0x0051 [0x03] Work_Zone[1] = Work_Zone[3]
 22: 0x0056 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 23: 0x0058 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 24: 0x005A [0x02] IF !(Work_Zone[3] == 4294967295*) GOTO 0x0064
 25: 0x0062 [0x21] END_EVENT
 26: 0x0063 [0x00] END_REQSTACK()
 27: 0x0064 [0x02] IF !(Work_Zone[3] == 4294967294*) GOTO 0x0072
 28: 0x006C [0x1D] PRINT_EVENT_MESSAGE(message_id=12784*)
    → "Either you or %0 has already heard fate's fickle will today. You may only have your fortune told once every Vana'dielian day."
 29: 0x006F [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0070 [0x21] END_EVENT
 31: 0x0071 [0x00] END_REQSTACK()
 32: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=12775*)
    → "Adventuring with %0 today will [bring you great fortune!/be highly profitable./bring fair fortune./be mutually advantageous./bring misfortune./be perilous./be disastrous!]"
 33: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0076 [0x02] IF !(Work_Zone[3] >= 4*) GOTO 0x00C2
 35: 0x007E [0x13] ExtData[1]->WorkLocal[0] = rand() % 3*
 36: 0x0083 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0092
 37: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=12776*)
    → "Good fortune fills your cup to overflowing. Be sure to share it with those less blessed by fate."
 38: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x008F [0x01] GOTO 0x00BF
 40: 0x0092 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x00A1
 41: 0x009A [0x1D] PRINT_EVENT_MESSAGE(message_id=12777*)
    → "Stand together and you have little to fear. With your combined strength, you can overcome any obstacle."
 42: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x009E [0x01] GOTO 0x00BF
 44: 0x00A1 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x00B0
 45: 0x00A9 [0x1D] PRINT_EVENT_MESSAGE(message_id=12778*)
    → "Do not let your good fortune blind you to danger. Pitfalls aplenty await the unwary traveler."
 46: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x00AD [0x01] GOTO 0x00BF
 48: 0x00B0 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x00BF
 49: 0x00B8 [0x1D] PRINT_EVENT_MESSAGE(message_id=12779*)
    → "Happiness is a state of mind. You can find laughter in even the most desperate of situations."
 50: 0x00BB [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x00BC [0x01] GOTO 0x00BF

SUBROUTINE_00BF:
 52: 0x00BF [0x01] GOTO 0x00F4
 53: 0x00C2 [0x13] ExtData[1]->WorkLocal[0] = rand() % 2*
 54: 0x00C7 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x00D6
 55: 0x00CF [0x1D] PRINT_EVENT_MESSAGE(message_id=12780*)
    → "The day ahead will be filled with trials and tribulations, but in time the path before you will run smooth once more."
 56: 0x00D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x00D3 [0x01] GOTO 0x00F4
 58: 0x00D6 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x00E5
 59: 0x00DE [0x1D] PRINT_EVENT_MESSAGE(message_id=12781*)
    → "There may be clashes of opinion today, but approach each other with an open mind and all will be well."
 60: 0x00E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 61: 0x00E2 [0x01] GOTO 0x00F4
 62: 0x00E5 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x00F4
 63: 0x00ED [0x1D] PRINT_EVENT_MESSAGE(message_id=12782*)
    → "You must rely on each others' strengths to overcome the difficulties you will face today. Don't let petty squabbles bring your downfall."
 64: 0x00F0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x00F1 [0x01] GOTO 0x00F4

SUBROUTINE_00F4:
 66: 0x00F4 [0x02] IF !(Work_Zone[3] >= 2*) GOTO 0x0100
 67: 0x00FC [0x1D] PRINT_EVENT_MESSAGE(message_id=12783*)
    → "Please accept this modest gift in celebration of your good fortune."
 68: 0x00FF [0x23] WAIT_FOR_DIALOG_INTERACTION
 69: 0x0100 [0x01] GOTO 0x0113
 70: 0x0103 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0113
 71: 0x010B [0x03] Work_Zone[1] = 1073741824*
 72: 0x0110 [0x01] GOTO 0x0113

SUBROUTINE_0113:
 73: 0x0113 [0x01] GOTO 0x011A
 74: 0x0116 [0x1D] PRINT_EVENT_MESSAGE(message_id=12784*)
    → "Either you or %0 has already heard fate's fickle will today. You may only have your fortune told once every Vana'dielian day."
 75: 0x0119 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_011A:
 76: 0x011A [0x01] GOTO 0x0122
 77: 0x011D [0x42] SET_CLI_EVENT_CANCEL_DATA()
 78: 0x011E [0x1D] PRINT_EVENT_MESSAGE(message_id=12783*)
    → "Please accept this modest gift in celebration of your good fortune."
 79: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0122:
 80: 0x0122 [0x21] END_EVENT
 81: 0x0123 [0x00] END_REQSTACK()
```
