# 17723629 - Emeige AMAN

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 484 bytes                     |
| Total Events     | 3                             |
| References Count | 26                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [739](#event-739)     | 0x0001       |    227 |             80 |
| [995](#event-995)     | 0x00E4       |    121 |             39 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x335A      |       13146 |
|       2 | 0x335B      |       13147 |
|       3 | 0x335C      |       13148 |
|       4 | 0x335D      |       13149 |
|       5 | 0x335E      |       13150 |
|       6 | 0x335F      |       13151 |
|       7 | 0x3360      |       13152 |
|       8 | 0x3361      |       13153 |
|       9 | 0x3362      |       13154 |
|      10 | 0x3364      |       13156 |
|      11 | 0x0002      |           2 |
|      12 | 0x40000000  |  1073741824 |
|      13 | 0x000A      |          10 |
|      14 | 0x336C      |       13164 |
|      15 | 0x336A      |       13162 |
|      16 | 0x336B      |       13163 |
|      17 | 0x3363      |       13155 |
|      18 | 0x3365      |       13157 |
|      19 | 0x0078      |         120 |
|      20 | 0x0000      |           0 |
|      21 | 0x000D      |          13 |
|      22 | 0x3366      |       13158 |
|      23 | 0x3368      |       13160 |
|      24 | 0x3369      |       13161 |
|      25 | 0x3367      |       13159 |

## String References

- **13146**: Good day, [sir/ma'am]. I am with the Adventurers' Mutual Aid Network (AMAN) and am now taking applications for new mentors.
- **13147**: What is a mentor, you ask? Well, in short, a mentor is an experienced adventurer who is willing to offer some of their time to help out their less traveled companions.
- **13148**: If this sounds like the job for you, then feel free to sign up today.
- **13149**: To become a mentor, you must have completed the Records of Eminence objective $0.
- **13150**: Accepting $0 requires that you have over 180 hours of play time...
- **13151**: ...and have completed the Records of Eminence objective $2.
- **13152**: Please note that registering and serving as a mentor, as well as utilizing the services of the Mentor Program, are to be done at the player's own discretion.
- **13153**: SQUARE ENIX will not be held responsible for the actions and/or comments of any mentors. No benefits of any kind will be provided to those who choose to participate in the Mentor Program.
- **13154**: When you agree to participate in the Mentor Program, you are acknowledging that you have read and understood the above terms.
- **13155**: I am sorry, but you do not meet the requirements necessary to accept the Records of Eminence objective $0.
- **13156**: Please speak to me again once you have accepted $0. I will then judge whether or not you meet the requirements.
- **13157**: You have accepted $0, yes? Then let me check my materials here...
- **13158**: Congratulations! You are qualified to be a mentor!
- **13159**: My materials here say that you don't meet the requirements. Keep at it!
- **13160**: Would you like to serve as a mentor? [Yes./No.]
- **13161**: You are now a registered mentor.
- **13162**: You can enable "Mentor Status" by using the command /mentor on. You can disable the status by using /mentor off.
- **13163**: Mentor status can also be switched on and off in the "Config" menu found within the "Help Desk."
- **13164**: You are already a registered mentor.

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

### Event 739

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 227 bytes |
| Instructions | 80        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 03 01  00 03 10 03 02 00 04 10   ...............
0010: 03 03 00 05 10 1E F0 FF  FF 7F 02 00 00 00 80 80  ................
0020: 61 00 1D 01 80 23 1D 02  80 23 1D 03 80 23 03 02  a....#...#...#..
0030: 10 01 00 1D 04 80 23 1D  05 80 23 03 03 10 02 00  ......#...#.....
0040: 03 04 10 03 00 1D 06 80  23 48 07 80 23 48 08 80  ........#H..#H..
0050: 23 48 09 80 23 1D 0A 80  23 03 01 10 00 80 01 E2  #H..#...#.......
0060: 00 02 00 00 0B 80 80 8A  00 1D 01 80 23 1D 02 80  ............#...
0070: 23 1D 03 80 23 03 02 10  01 00 1D 04 80 23 1D 0A  #...#........#..
0080: 80 23 03 01 10 0C 80 01  E2 00 02 00 00 0D 80 80  .#..............
0090: A6 00 1D 0E 80 23 48 0F  80 23 48 10 80 23 03 01  .....#H..#H..#..
00A0: 10 0C 80 01 E2 00 1D 01  80 23 1D 02 80 23 1D 03  .........#...#..
00B0: 80 23 03 02 10 01 00 1D  04 80 23 1D 05 80 23 03  .#........#...#.
00C0: 03 10 02 00 03 04 10 03  00 1D 06 80 23 48 07 80  ............#H..
00D0: 23 48 08 80 23 48 09 80  23 1D 11 80 23 03 01 10  #H..#H..#...#...
00E0: 0C 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x000B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  3: 0x0010 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  4: 0x0015 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x001A [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0061
  6: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=13146*)
    → "Good day, [sir/ma'am]. I am with the Adventurers' Mutual Aid Network (AMAN) and am now taking applications for new mentors."
  7: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=13147*)
    → "What is a mentor, you ask? Well, in short, a mentor is an experienced adventurer who is willing to offer some of their time to help out their less traveled companions."
  9: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=13148*)
    → "If this sounds like the job for you, then feel free to sign up today."
 11: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x002E [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 13: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=13149*)
    → "To become a mentor, you must have completed the Records of Eminence objective $0."
 14: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=13150*)
    → "Accepting $0 requires that you have over 180 hours of play time..."
 16: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x003B [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
 18: 0x0040 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 19: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=13151*)
    → "...and have completed the Records of Eminence objective $2."
 20: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0049 [0x48] [System] [13152*]:
    → "Please note that registering and serving as a mentor, as well as utilizing the services of the Mentor Program, are to be done at the player's own discretion."
 22: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x004D [0x48] [System] [13153*]:
    → "SQUARE ENIX will not be held responsible for the actions and/or comments of any mentors. No benefits of any kind will be provided to those who choose to participate in the Mentor Program."
 24: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0051 [0x48] [System] [13154*]:
    → "When you agree to participate in the Mentor Program, you are acknowledging that you have read and understood the above terms."
 26: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=13156*)
    → "Please speak to me again once you have accepted $0. I will then judge whether or not you meet the requirements."
 28: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0059 [0x03] Work_Zone[1] = 1*
 30: 0x005E [0x01] GOTO 0x00E2
 31: 0x0061 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x008A
 32: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=13146*)
    → "Good day, [sir/ma'am]. I am with the Adventurers' Mutual Aid Network (AMAN) and am now taking applications for new mentors."
 33: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=13147*)
    → "What is a mentor, you ask? Well, in short, a mentor is an experienced adventurer who is willing to offer some of their time to help out their less traveled companions."
 35: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x0071 [0x1D] PRINT_EVENT_MESSAGE(message_id=13148*)
    → "If this sounds like the job for you, then feel free to sign up today."
 37: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x0075 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 39: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=13149*)
    → "To become a mentor, you must have completed the Records of Eminence objective $0."
 40: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=13156*)
    → "Please speak to me again once you have accepted $0. I will then judge whether or not you meet the requirements."
 42: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x0082 [0x03] Work_Zone[1] = 1073741824*
 44: 0x0087 [0x01] GOTO 0x00E2
 45: 0x008A [0x02] IF !(ExtData[1]->WorkLocal[0] == 10*) GOTO 0x00A6
 46: 0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=13164*)
    → "You are already a registered mentor."
 47: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x0096 [0x48] [System] [13162*]:
    → "You can enable "Mentor Status" by using the command /mentor on. You can disable the status by using /mentor off."
 49: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x009A [0x48] [System] [13163*]:
    → "Mentor status can also be switched on and off in the "Config" menu found within the "Help Desk.""
 51: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x009E [0x03] Work_Zone[1] = 1073741824*
 53: 0x00A3 [0x01] GOTO 0x00E2
 54: 0x00A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=13146*)
    → "Good day, [sir/ma'am]. I am with the Adventurers' Mutual Aid Network (AMAN) and am now taking applications for new mentors."
 55: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=13147*)
    → "What is a mentor, you ask? Well, in short, a mentor is an experienced adventurer who is willing to offer some of their time to help out their less traveled companions."
 57: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x00AE [0x1D] PRINT_EVENT_MESSAGE(message_id=13148*)
    → "If this sounds like the job for you, then feel free to sign up today."
 59: 0x00B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x00B2 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 61: 0x00B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=13149*)
    → "To become a mentor, you must have completed the Records of Eminence objective $0."
 62: 0x00BA [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x00BB [0x1D] PRINT_EVENT_MESSAGE(message_id=13150*)
    → "Accepting $0 requires that you have over 180 hours of play time..."
 64: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x00BF [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
 66: 0x00C4 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 67: 0x00C9 [0x1D] PRINT_EVENT_MESSAGE(message_id=13151*)
    → "...and have completed the Records of Eminence objective $2."
 68: 0x00CC [0x23] WAIT_FOR_DIALOG_INTERACTION
 69: 0x00CD [0x48] [System] [13152*]:
    → "Please note that registering and serving as a mentor, as well as utilizing the services of the Mentor Program, are to be done at the player's own discretion."
 70: 0x00D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 71: 0x00D1 [0x48] [System] [13153*]:
    → "SQUARE ENIX will not be held responsible for the actions and/or comments of any mentors. No benefits of any kind will be provided to those who choose to participate in the Mentor Program."
 72: 0x00D4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 73: 0x00D5 [0x48] [System] [13154*]:
    → "When you agree to participate in the Mentor Program, you are acknowledging that you have read and understood the above terms."
 74: 0x00D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 75: 0x00D9 [0x1D] PRINT_EVENT_MESSAGE(message_id=13155*)
    → "I am sorry, but you do not meet the requirements necessary to accept the Records of Eminence objective $0."
 76: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION
 77: 0x00DD [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_00E2:
 78: 0x00E2 [0x21] END_EVENT
 79: 0x00E3 [0x00] END_REQSTACK()
```

### Event 995

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E4    |
| Data Size    | 121 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             03 01 00 02  10 03 04 00 03 10 1E F0      ............
00F0: FF FF 7F 1D 01 80 23 1D  12 80 23 42 1C 13 80 02  ......#...#B....
0100: 04 00 14 80 01 52 01 6E  F8 FF FF 7F 15 80 99 F8  .....R.n........
0110: FF FF 7F 1D 16 80 23 1C  00 80 48 07 80 23 48 08  ......#...H..#H.
0120: 80 23 48 09 80 23 24 17  80 14 80 14 80 25 02 00  .#H..#$......%..
0130: 10 14 80 00 4A 01 1D 18  80 23 1D 0F 80 23 1D 10  ....J....#...#..
0140: 80 23 03 01 10 00 80 01  4F 01 03 01 10 0C 80 01  .#......O.......
0150: 5B 01 1D 19 80 23 03 01  10 0C 80 21 00           [....#.....!.   
```

#### Opcodes

```
  0: 0x00E4 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
  1: 0x00E9 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[3]
  2: 0x00EE [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=13146*)
    → "Good day, [sir/ma'am]. I am with the Adventurers' Mutual Aid Network (AMAN) and am now taking applications for new mentors."
  4: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00F7 [0x1D] PRINT_EVENT_MESSAGE(message_id=13157*)
    → "You have accepted $0, yes? Then let me check my materials here..."
  6: 0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00FB [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x00FC [0x1C] WAIT(120* ticks)
  9: 0x00FF [0x02] IF !(ExtData[1]->WorkLocal[4] == 0*) GOTO 0x0152
 10: 0x0107 [0x6E] EventEntity uses emote 13*
 11: 0x010E [0x99] Wait for EventEntity animation to complete
 12: 0x0113 [0x1D] PRINT_EVENT_MESSAGE(message_id=13158*)
    → "Congratulations! You are qualified to be a mentor!"
 13: 0x0116 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0117 [0x1C] WAIT(1* ticks)
 15: 0x011A [0x48] [System] [13152*]:
    → "Please note that registering and serving as a mentor, as well as utilizing the services of the Mentor Program, are to be done at the player's own discretion."
 16: 0x011D [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x011E [0x48] [System] [13153*]:
    → "SQUARE ENIX will not be held responsible for the actions and/or comments of any mentors. No benefits of any kind will be provided to those who choose to participate in the Mentor Program."
 18: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0122 [0x48] [System] [13154*]:
    → "When you agree to participate in the Mentor Program, you are acknowledging that you have read and understood the above terms."
 20: 0x0125 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0126 [0x24] CREATE_DIALOG(message_id=13160*, default_option=0*, option_flags=0*)
    → "Would you like to serve as a mentor? [Yes./No.]"
 22: 0x012D [0x25] WAIT_DIALOG_SELECT()
 23: 0x012E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x014A
 24: 0x0136 [0x1D] PRINT_EVENT_MESSAGE(message_id=13161*)
    → "You are now a registered mentor."
 25: 0x0139 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x013A [0x1D] PRINT_EVENT_MESSAGE(message_id=13162*)
    → "You can enable "Mentor Status" by using the command /mentor on. You can disable the status by using /mentor off."
 27: 0x013D [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x013E [0x1D] PRINT_EVENT_MESSAGE(message_id=13163*)
    → "Mentor status can also be switched on and off in the "Config" menu found within the "Help Desk.""
 29: 0x0141 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0142 [0x03] Work_Zone[1] = 1*
 31: 0x0147 [0x01] GOTO 0x014F
 32: 0x014A [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_014F:
 33: 0x014F [0x01] GOTO 0x015B
 34: 0x0152 [0x1D] PRINT_EVENT_MESSAGE(message_id=13159*)
    → "My materials here say that you don't meet the requirements. Keep at it!"
 35: 0x0155 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x0156 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_015B:
 37: 0x015B [0x21] END_EVENT
 38: 0x015C [0x00] END_REQSTACK()
```
