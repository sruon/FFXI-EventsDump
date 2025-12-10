# 17248786 - Achieve Master

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 484 bytes                   |
| Total Events     | 2                           |
| References Count | 14                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [83](#event-83)       | 0x0001       |    403 |             85 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0006      |           6 |
|       2 | 0x3073      |       12403 |
|       3 | 0x0007      |           7 |
|       4 | 0x0001      |           1 |
|       5 | 0x0005      |           5 |
|       6 | 0x0002      |           2 |
|       7 | 0x0010      |          16 |
|       8 | 0x001F      |          31 |
|       9 | 0x0003      |           3 |
|      10 | 0x0004      |           4 |
|      11 | 0x40000000  |  1073741824 |
|      12 | 0x3074      |       12404 |
|      13 | 0x0017      |          23 |

## String References

- **12403**: Top o' the menu to ya. [Autopilot (Currently: [ON/OFF])/Cutscene...change! (Currently: No. $1)/Cutscene Status Modification./Group: $3./Get me outta here.]
- **12404**: Status No. $1: [Closed/Open/Spare] [Closed./Open./Spare./Return to top.]

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

### Event 83

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 403 bytes |
| Instructions | 85        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A 74 01 05 01 00 02  01 00 00 80 01 CB 00 1A   .t.............
0010: 84 01 02 05 00 00 80 00  22 00 03 08 00 01 80 01  ........".......
0020: 27 00 03 08 00 00 80 24  02 80 03 00 08 00 25 02  '......$......%.
0030: 00 10 00 80 00 50 00 03  01 10 00 80 40 00 80 03  .....P......@...
0040: 80 01 10 04 80 03 03 00  00 10 06 01 00 01 C8 00  ................
0050: 02 00 10 04 80 00 83 00  71 12 04 80 05 80 71 13  ........q.....q.
0060: 06 00 40 00 80 03 80 01  10 06 80 40 07 80 08 80  ..@........@....
0070: 01 10 06 00 03 03 00 00  10 43 00 43 01 1A 74 01  .........C.C..t.
0080: 01 C8 00 02 00 10 06 80  00 96 00 03 03 00 00 10  ................
0090: 1A CD 00 01 C8 00 02 00  10 09 80 00 C0 00 71 12  ..............q.
00A0: 04 80 06 80 71 13 06 00  40 00 80 03 80 01 10 0A  ....q...@.......
00B0: 80 40 07 80 08 80 01 10  06 00 06 01 00 01 C8 00  .@..............
00C0: 03 01 10 0B 80 06 01 00  01 07 00 21 00 05 02 00  ...........!....
00D0: 02 02 00 00 80 01 73 01  1A 84 01 24 0C 80 04 00  ......s....$....
00E0: 00 80 25 02 00 10 00 80  00 11 01 03 01 10 00 80  ..%.............
00F0: 40 00 80 03 80 01 10 09  80 40 07 80 0D 80 01 10  @........@......
0100: 00 80 03 04 00 00 10 43  00 43 01 1A 74 01 01 70  .......C.C..t..p
0110: 01 02 00 10 04 80 00 3F  01 03 01 10 00 80 40 00  .......?......@.
0120: 80 03 80 01 10 09 80 40  07 80 0D 80 01 10 04 80  .......@........
0130: 03 04 00 00 10 43 00 43  01 1A 74 01 01 70 01 02  .....C.C..t..p..
0140: 00 10 06 80 00 6D 01 03  01 10 00 80 40 00 80 03  .....m......@...
0150: 80 01 10 09 80 40 07 80  0D 80 01 10 06 80 03 04  .....@..........
0160: 00 00 10 43 00 43 01 1A  74 01 01 70 01 06 02 00  ...C.C..t..p....
0170: 01 D0 00 1B 03 05 00 02  10 03 06 00 03 10 03 07  ................
0180: 00 04 10 1B 03 02 10 05  00 03 03 10 06 00 03 04  ................
0190: 10 07 00 1B                                       ....            
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x0174)
  1: 0x0004 [0x05] ExtData[1]->WorkLocal[1] = 1
  2: 0x0007 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00CB
  3: 0x000F [0x1A] CALL_SUBROUTINE(address=0x0184)
  4: 0x0012 [0x02] IF !(ExtData[1]->WorkLocal[5] == 0*) GOTO 0x0022
  5: 0x001A [0x03] ExtData[1]->WorkLocal[8] = 6*
  6: 0x001F [0x01] GOTO 0x0027
  7: 0x0022 [0x03] ExtData[1]->WorkLocal[8] = 0*

SUBROUTINE_0027:
  8: 0x0027 [0x24] CREATE_DIALOG(message_id=12403*, default_option=ExtData[1]->WorkLocal[3], option_flags=ExtData[1]->WorkLocal[8])
    → "Top o' the menu to ya. [Autopilot (Currently: [ON/OFF])/Cutscene...change! (Currently: No. $1)/Cutscene Status Modification./Group: $3./Get me outta here.]"
  9: 0x002E [0x25] WAIT_DIALOG_SELECT()
 10: 0x002F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0050
 11: 0x0037 [0x03] Work_Zone[1] = 0*
 12: 0x003C [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=1*)
 13: 0x0045 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[0]
 14: 0x004A [0x06] ExtData[1]->WorkLocal[1] = 0
 15: 0x004D [0x01] GOTO 0x00C8
 16: 0x0050 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0083
 17: 0x0058 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 5*])
 18: 0x005E [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[6])
 19: 0x0062 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=2*)
 20: 0x006B [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 21: 0x0074 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[0]
 22: 0x0079 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 23: 0x007B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 24: 0x007D [0x1A] CALL_SUBROUTINE(address=0x0174)
 25: 0x0080 [0x01] GOTO 0x00C8
 26: 0x0083 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0096
 27: 0x008B [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[0]
 28: 0x0090 [0x1A] CALL_SUBROUTINE(address=0x00CD)
 29: 0x0093 [0x01] GOTO 0x00C8
 30: 0x0096 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x00C0
 31: 0x009E [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 32: 0x00A4 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[6])
 33: 0x00A8 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=4*)
 34: 0x00B1 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 35: 0x00BA [0x06] ExtData[1]->WorkLocal[1] = 0
 36: 0x00BD [0x01] GOTO 0x00C8
 37: 0x00C0 [0x03] Work_Zone[1] = 1073741824*
 38: 0x00C5 [0x06] ExtData[1]->WorkLocal[1] = 0

SUBROUTINE_00C8:
 39: 0x00C8 [0x01] GOTO 0x0007
 40: 0x00CB [0x21] END_EVENT
 41: 0x00CC [0x00] END_REQSTACK()

SUBROUTINE_00CD:
 42: 0x00CD [0x05] ExtData[1]->WorkLocal[2] = 1

SUBROUTINE_00D0:
 43: 0x00D0 [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x0173
 44: 0x00D8 [0x1A] CALL_SUBROUTINE(address=0x0184)
 45: 0x00DB [0x24] CREATE_DIALOG(message_id=12404*, default_option=ExtData[1]->WorkLocal[4], option_flags=0*)
    → "Status No. $1: [Closed/Open/Spare] [Closed./Open./Spare./Return to top.]"
 46: 0x00E2 [0x25] WAIT_DIALOG_SELECT()
 47: 0x00E3 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0111
 48: 0x00EB [0x03] Work_Zone[1] = 0*
 49: 0x00F0 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=3*)
 50: 0x00F9 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=Work_Zone[1], source=0*)
 51: 0x0102 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[0]
 52: 0x0107 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 53: 0x0109 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 54: 0x010B [0x1A] CALL_SUBROUTINE(address=0x0174)
 55: 0x010E [0x01] GOTO 0x0170
 56: 0x0111 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x013F
 57: 0x0119 [0x03] Work_Zone[1] = 0*
 58: 0x011E [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=3*)
 59: 0x0127 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=Work_Zone[1], source=1*)
 60: 0x0130 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[0]
 61: 0x0135 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 62: 0x0137 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 63: 0x0139 [0x1A] CALL_SUBROUTINE(address=0x0174)
 64: 0x013C [0x01] GOTO 0x0170
 65: 0x013F [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x016D
 66: 0x0147 [0x03] Work_Zone[1] = 0*
 67: 0x014C [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=3*)
 68: 0x0155 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=Work_Zone[1], source=2*)
 69: 0x015E [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[0]
 70: 0x0163 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 71: 0x0165 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 72: 0x0167 [0x1A] CALL_SUBROUTINE(address=0x0174)
 73: 0x016A [0x01] GOTO 0x0170
 74: 0x016D [0x06] ExtData[1]->WorkLocal[2] = 0

SUBROUTINE_0170:
 75: 0x0170 [0x01] GOTO 0x00D0
 76: 0x0173 [0x1B] RETURN

SUBROUTINE_0174:
 77: 0x0174 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[2]
 78: 0x0179 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[3]
 79: 0x017E [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[4]
 80: 0x0183 [0x1B] RETURN

SUBROUTINE_0184:
 81: 0x0184 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[5]
 82: 0x0189 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[6]
 83: 0x018E [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[7]
 84: 0x0193 [0x1B] RETURN
```
