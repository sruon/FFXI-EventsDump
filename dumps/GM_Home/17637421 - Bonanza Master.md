# 17637421 - Bonanza Master

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 416 bytes         |
| Total Events     | 2                 |
| References Count | 12                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [81](#event-81)       | 0x0001       |    340 |             89 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1DB1      |        7601 |
|       2 | 0x0001      |           1 |
|       3 | 0x1DB2      |        7602 |
|       4 | 0x0002      |           2 |
|       5 | 0x1DB3      |        7603 |
|       6 | 0x0003      |           3 |
|       7 | 0x1DB4      |        7604 |
|       8 | 0x0004      |           4 |
|       9 | 0x1DB5      |        7605 |
|      10 | 0x0005      |           5 |
|      11 | 0x1DB6      |        7606 |

## String References

- **7601**: Pick a prize rank. [Rank 1 (5 digits): $14$13$12$11$10/Rank 2 (4 digits): $18$17$16$15/Rank 3 (3 digits): $21$20$19/Rank 4 (2 digits): $23$22/Rank 5 (1 digits): $24/Do nothing.]
- **7602**: The rank $0 numbers are $5$4$3$2$1!
- **7603**: The rank $0 numbers are $5$4$3$2$1!
- **7604**: The rank $0 numbers are $5$4$3$2$1!
- **7605**: The rank $0 numbers are $5$4$3$2$1!
- **7606**: The rank $0 number is $5$4$3$2$1!

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

### Event 81

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 340 bytes |
| Instructions | 89        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 06 02 10 06 03 10  06 04 10 06 05 10 06 06   B..............
0010: 10 06 07 10 06 08 10 06  09 10 06 00 17 06 01 17  ................
0020: 06 02 17 06 03 17 06 04  17 06 05 17 06 06 17 06  ................
0030: 07 17 06 08 17 06 09 17  06 0A 17 06 0B 17 06 0C  ................
0040: 17 06 0D 17 06 0E 17 06  0F 17 06 10 17 06 00 00  ................
0050: 02 00 00 00 80 00 53 01  24 01 80 00 80 00 80 25  ......S.$......%
0060: 02 00 10 00 80 00 99 00  03 01 10 00 10 43 00 43  .............C.C
0070: 01 02 02 10 02 80 00 96  00 03 02 17 03 10 03 03  ................
0080: 17 04 10 03 04 17 05 10  03 05 17 06 10 03 06 17  ................
0090: 07 10 1D 03 80 23 01 50  01 02 00 10 02 80 00 CD  .....#.P........
00A0: 00 03 01 10 00 10 43 00  43 01 02 02 10 04 80 00  ......C.C.......
00B0: CA 00 03 07 17 03 10 03  08 17 04 10 03 09 17 05  ................
00C0: 10 03 0A 17 06 10 1D 05  80 23 01 50 01 02 00 10  .........#.P....
00D0: 04 80 00 FC 00 03 01 10  00 10 43 00 43 01 02 02  ..........C.C...
00E0: 10 06 80 00 F9 00 03 0B  17 03 10 03 0C 17 04 10  ................
00F0: 03 0D 17 05 10 1D 07 80  23 01 50 01 02 00 10 06  ........#.P.....
0100: 80 00 26 01 03 01 10 00  10 43 00 43 01 02 02 10  ..&......C.C....
0110: 08 80 00 23 01 03 0E 17  03 10 03 0F 17 04 10 1D  ...#............
0120: 09 80 23 01 50 01 02 00  10 08 80 00 4B 01 03 01  ..#.P.......K...
0130: 10 00 10 43 00 43 01 02  02 10 0A 80 00 48 01 03  ...C.C.......H..
0140: 10 17 03 10 1D 0B 80 23  01 50 01 03 00 00 02 80  .......#.P......
0150: 01 50 00 21 00                                    .P.!.           
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x06] Work_Zone[2] = 0
  2: 0x0005 [0x06] Work_Zone[3] = 0
  3: 0x0008 [0x06] Work_Zone[4] = 0
  4: 0x000B [0x06] Work_Zone[5] = 0
  5: 0x000E [0x06] Work_Zone[6] = 0
  6: 0x0011 [0x06] Work_Zone[7] = 0
  7: 0x0014 [0x06] Work_Zone[8] = 0
  8: 0x0017 [0x06] Work_Zone[9] = 0
  9: 0x001A [0x06] Work_Zone_1700[0] = 0
 10: 0x001D [0x06] Work_Zone_1700[1] = 0
 11: 0x0020 [0x06] Work_Zone_1700[2] = 0
 12: 0x0023 [0x06] Work_Zone_1700[3] = 0
 13: 0x0026 [0x06] Work_Zone_1700[4] = 0
 14: 0x0029 [0x06] Work_Zone_1700[5] = 0
 15: 0x002C [0x06] Work_Zone_1700[6] = 0
 16: 0x002F [0x06] Work_Zone_1700[7] = 0
 17: 0x0032 [0x06] Work_Zone_1700[8] = 0
 18: 0x0035 [0x06] Work_Zone_1700[9] = 0
 19: 0x0038 [0x06] Work_Zone_1700[10] = 0
 20: 0x003B [0x06] Work_Zone_1700[11] = 0
 21: 0x003E [0x06] Work_Zone_1700[12] = 0
 22: 0x0041 [0x06] Work_Zone_1700[13] = 0
 23: 0x0044 [0x06] Work_Zone_1700[14] = 0
 24: 0x0047 [0x06] Work_Zone_1700[15] = 0
 25: 0x004A [0x06] Work_Zone_1700[16] = 0
 26: 0x004D [0x06] ExtData[1]->WorkLocal[0] = 0
 27: 0x0050 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0153
 28: 0x0058 [0x24] CREATE_DIALOG(message_id=7601*, default_option=0*, option_flags=0*)
    → "Pick a prize rank. [Rank 1 (5 digits): $14$13$12$11$10/Rank 2 (4 digits): $18$17$16$15/Rank 3 (3 digits): $21$20$19/Rank 4 (2 digits): $23$22/Rank 5 (1 digits): $24/Do nothing.]"
 29: 0x005F [0x25] WAIT_DIALOG_SELECT()
 30: 0x0060 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0099
 31: 0x0068 [0x03] Work_Zone[1] = Work_Zone[0]
 32: 0x006D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 33: 0x006F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 34: 0x0071 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0096
 35: 0x0079 [0x03] Work_Zone_1700[2] = Work_Zone[3]
 36: 0x007E [0x03] Work_Zone_1700[3] = Work_Zone[4]
 37: 0x0083 [0x03] Work_Zone_1700[4] = Work_Zone[5]
 38: 0x0088 [0x03] Work_Zone_1700[5] = Work_Zone[6]
 39: 0x008D [0x03] Work_Zone_1700[6] = Work_Zone[7]
 40: 0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=7602*)
    → "The rank $0 numbers are $5$4$3$2$1!"
 41: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x0096 [0x01] GOTO 0x0150
 43: 0x0099 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00CD
 44: 0x00A1 [0x03] Work_Zone[1] = Work_Zone[0]
 45: 0x00A6 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 46: 0x00A8 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 47: 0x00AA [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x00CA
 48: 0x00B2 [0x03] Work_Zone_1700[7] = Work_Zone[3]
 49: 0x00B7 [0x03] Work_Zone_1700[8] = Work_Zone[4]
 50: 0x00BC [0x03] Work_Zone_1700[9] = Work_Zone[5]
 51: 0x00C1 [0x03] Work_Zone_1700[10] = Work_Zone[6]
 52: 0x00C6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7603*)
    → "The rank $0 numbers are $5$4$3$2$1!"
 53: 0x00C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x00CA [0x01] GOTO 0x0150
 55: 0x00CD [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00FC
 56: 0x00D5 [0x03] Work_Zone[1] = Work_Zone[0]
 57: 0x00DA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 58: 0x00DC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 59: 0x00DE [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x00F9
 60: 0x00E6 [0x03] Work_Zone_1700[11] = Work_Zone[3]
 61: 0x00EB [0x03] Work_Zone_1700[12] = Work_Zone[4]
 62: 0x00F0 [0x03] Work_Zone_1700[13] = Work_Zone[5]
 63: 0x00F5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7604*)
    → "The rank $0 numbers are $5$4$3$2$1!"
 64: 0x00F8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x00F9 [0x01] GOTO 0x0150
 66: 0x00FC [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0126
 67: 0x0104 [0x03] Work_Zone[1] = Work_Zone[0]
 68: 0x0109 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 69: 0x010B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 70: 0x010D [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0123
 71: 0x0115 [0x03] Work_Zone_1700[14] = Work_Zone[3]
 72: 0x011A [0x03] Work_Zone_1700[15] = Work_Zone[4]
 73: 0x011F [0x1D] PRINT_EVENT_MESSAGE(message_id=7605*)
    → "The rank $0 numbers are $5$4$3$2$1!"
 74: 0x0122 [0x23] WAIT_FOR_DIALOG_INTERACTION
 75: 0x0123 [0x01] GOTO 0x0150
 76: 0x0126 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x014B
 77: 0x012E [0x03] Work_Zone[1] = Work_Zone[0]
 78: 0x0133 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 79: 0x0135 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 80: 0x0137 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x0148
 81: 0x013F [0x03] Work_Zone_1700[16] = Work_Zone[3]
 82: 0x0144 [0x1D] PRINT_EVENT_MESSAGE(message_id=7606*)
    → "The rank $0 number is $5$4$3$2$1!"
 83: 0x0147 [0x23] WAIT_FOR_DIALOG_INTERACTION
 84: 0x0148 [0x01] GOTO 0x0150
 85: 0x014B [0x03] ExtData[1]->WorkLocal[0] = 1*

SUBROUTINE_0150:
 86: 0x0150 [0x01] GOTO 0x0050
 87: 0x0153 [0x21] END_EVENT
 88: 0x0154 [0x00] END_REQSTACK()
```
