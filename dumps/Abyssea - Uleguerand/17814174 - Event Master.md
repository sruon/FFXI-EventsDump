# 17814174 - Event Master

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 604 bytes                      |
| Total Events     | 2                              |
| References Count | 21                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [400](#event-400)     | 0x0001       |    495 |            101 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x270F      |        9999 |
|       2 | 0x2036      |        8246 |
|       3 | 0x0000      |           0 |
|       4 | 0x40000000  |  1073741824 |
|       5 | 0x2034      |        8244 |
|       6 | 0x0002      |           2 |
|       7 | 0x0007      |           7 |
|       8 | 0x0008      |           8 |
|       9 | 0x000F      |          15 |
|      10 | 0x000C      |          12 |
|      11 | 0x0006      |           6 |
|      12 | 0x000A      |          10 |
|      13 | 0x002C      |          44 |
|      14 | 0x0009      |           9 |
|      15 | 0x2037      |        8247 |
|      16 | 0x0003      |           3 |
|      17 | 0x0004      |           4 |
|      18 | 0x0005      |           5 |
|      19 | 0x0010      |          16 |
|      20 | 0x0017      |          23 |

## String References

- **8244**: Fame value for this area: $0 Input a value from 0 - 63. (Cancel: 0)
- **8246**: What will you do? [Nothing./Set fame./Quest 01 (Fame: $0)/Quest 02 (Fame: $1)/Quest 03 (Fame: $2)/Quest 04 (Fame: $3)/Quest 05 (Fame: $4)/Quest 06 (Fame: $5)/Quest 07 (Fame: $6)/Quest 08 (Fame: $7)/Quest 09 (Fame: $8)/Quest 10 (Fame: $9)/AP (elapsed time) check (Currently: [Seeing/Not seeing])]
- **8247**: What will yo do? (Quest ) [Nothing./Set quest eligibility./Quest progress./Obtain key item./Complete quest./Set times completed.]

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

### Event 400

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 495 bytes |
| Instructions | 100       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 04 00 02 10 03 05  00 03 10 03 02 17 04 10   ...............
0010: 05 00 00 02 00 00 00 80  00 D0 00 1A 9F 01 03 02  ................
0020: 00 01 80 24 02 80 03 80  03 80 25 02 00 10 03 80  ...$......%.....
0030: 00 3E 00 06 00 00 03 01  10 04 80 01 97 00 02 00  .>..............
0040: 10 00 80 00 7A 00 03 02  10 04 00 03 03 10 05 00  ....z...........
0050: 48 05 80 03 01 10 03 80  71 12 00 80 06 80 71 13  H.......q.....q.
0060: 01 00 40 03 80 07 80 01  10 03 80 40 08 80 09 80  ..@........@....
0070: 01 10 01 00 06 00 00 01  97 00 02 00 10 0A 80 00  ................
0080: 8D 00 03 01 10 0B 80 06  00 00 01 97 00 03 02 00  ................
0090: 00 10 08 02 00 06 80 02  02 00 0C 80 03 CD 00 02  ................
00A0: 02 00 08 80 80 AF 00 03  03 00 0D 80 01 BF 00 02  ................
00B0: 02 00 0E 80 80 BF 00 03  03 00 0D 80 01 BF 00 03  ................
00C0: 17 17 02 00 0B 17 17 1A  D2 00 06 00 00 01 13 00  ................
00D0: 21 00 24 0F 80 03 80 03  00 25 02 00 10 03 80 00  !.$......%......
00E0: EA 00 03 01 10 04 80 01  9D 01 02 00 10 00 80 00  ................
00F0: 03 01 03 01 10 00 80 40  08 80 09 80 01 10 02 00  .......@........
0100: 01 9D 01 02 00 10 06 80  00 1C 01 03 01 10 06 80  ................
0110: 40 08 80 09 80 01 10 02  00 01 9D 01 02 00 10 10  @...............
0120: 80 00 4B 01 03 01 10 10  80 40 08 80 09 80 01 10  ..K......@......
0130: 02 00 02 02 00 08 80 80  3D 01 01 48 01 02 02 00  ........=..H....
0140: 0E 80 80 48 01 01 48 01  01 9D 01 02 00 10 11 80  ...H..H.........
0150: 00 64 01 03 01 10 11 80  40 08 80 09 80 01 10 02  .d......@.......
0160: 00 01 9D 01 02 00 10 12  80 00 9D 01 03 01 10 12  ................
0170: 80 40 08 80 09 80 01 10  02 00 71 12 00 80 00 80  .@........q.....
0180: 71 13 06 00 02 06 00 12  80 02 91 01 03 06 00 12  q...............
0190: 80 40 13 80 14 80 01 10  06 00 01 9D 01 1B 1B 03  .@..............
01A0: 02 10 03 80 03 03 10 03  80 03 04 10 03 80 03 05  ................
01B0: 10 10 80 03 06 10 10 80  03 07 10 00 80 03 08 10  ................
01C0: 11 80 03 09 10 06 80 03  00 17 03 80 03 01 17 00  ................
01D0: 80 0B 02 10 0B 03 10 0B  04 10 0B 05 10 0B 06 10  ................
01E0: 0B 07 10 0B 08 10 0B 09  10 0B 00 17 0B 01 17 1B  ................
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[3]
  2: 0x000B [0x03] Work_Zone_1700[2] = Work_Zone[4]
  3: 0x0010 [0x05] ExtData[1]->WorkLocal[0] = 1
  4: 0x0013 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x00D0
  5: 0x001B [0x1A] CALL_SUBROUTINE(address=0x019F)
  6: 0x001E [0x03] ExtData[1]->WorkLocal[2] = 9999*
  7: 0x0023 [0x24] CREATE_DIALOG(message_id=8246*, default_option=0*, option_flags=0*)
    → "What will you do? [Nothing./Set fame./Quest 01 (Fame: $0)/Quest 02 (Fame: $1)/Quest 03 (Fame: $2)/Quest 04 (Fame: $3)/Quest 05 (Fame: $4)/Quest 06 (Fame: $5)/Quest 07 (Fame: $6)/Quest 08 (Fame: $7)/Quest 09 (Fame: $8)/Quest 10 (Fame: $9)/AP (elapsed time) check (Currently: [Seeing/Not seeing])]"
  8: 0x002A [0x25] WAIT_DIALOG_SELECT()
  9: 0x002B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003E
 10: 0x0033 [0x06] ExtData[1]->WorkLocal[0] = 0
 11: 0x0036 [0x03] Work_Zone[1] = 1073741824*
 12: 0x003B [0x01] GOTO 0x0097
 13: 0x003E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x007A
 14: 0x0046 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[4]
 15: 0x004B [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[5]
 16: 0x0050 [0x48] [System] [8244*]:
    → "Fame value for this area: $0 Input a value from 0 - 63. (Cancel: 0)"
 17: 0x0053 [0x03] Work_Zone[1] = 0*
 18: 0x0058 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 19: 0x005E [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[1])
 20: 0x0062 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=0*)
 21: 0x006B [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 22: 0x0074 [0x06] ExtData[1]->WorkLocal[0] = 0
 23: 0x0077 [0x01] GOTO 0x0097
 24: 0x007A [0x02] IF !(Work_Zone[0] == 12*) GOTO 0x008D
 25: 0x0082 [0x03] Work_Zone[1] = 6*
 26: 0x0087 [0x06] ExtData[1]->WorkLocal[0] = 0
 27: 0x008A [0x01] GOTO 0x0097
 28: 0x008D [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[0]
 29: 0x0092 [0x08] ExtData[1]->WorkLocal[2] -= 2*

SUBROUTINE_0097:
 30: 0x0097 [0x02] IF !(ExtData[1]->WorkLocal[2] >= 10*) GOTO 0x00CD
 31: 0x009F [0x02] IF !(ExtData[1]->WorkLocal[2] == 8*) GOTO 0x00AF
 32: 0x00A7 [0x03] ExtData[1]->WorkLocal[3] = 44*
 33: 0x00AC [0x01] GOTO 0x00BF
 34: 0x00AF [0x02] IF !(ExtData[1]->WorkLocal[2] == 9*) GOTO 0x00BF
 35: 0x00B7 [0x03] ExtData[1]->WorkLocal[3] = 44*
 36: 0x00BC [0x01] GOTO 0x00BF

SUBROUTINE_00BF:
 37: 0x00BF [0x03] Work_Zone_1700[23] = ExtData[1]->WorkLocal[2]
 38: 0x00C4 [0x0B] Work_Zone_1700[23]++
 39: 0x00C7 [0x1A] CALL_SUBROUTINE(address=0x00D2)
 40: 0x00CA [0x06] ExtData[1]->WorkLocal[0] = 0
 41: 0x00CD [0x01] GOTO 0x0013
 42: 0x00D0 [0x21] END_EVENT
 43: 0x00D1 [0x00] END_REQSTACK()

SUBROUTINE_00D2:
 44: 0x00D2 [0x24] CREATE_DIALOG(message_id=8247*, default_option=0*, option_flags=ExtData[1]->WorkLocal[3])
    → "What will yo do? (Quest ) [Nothing./Set quest eligibility./Quest progress./Obtain key item./Complete quest./Set times completed.]"
 45: 0x00D9 [0x25] WAIT_DIALOG_SELECT()
 46: 0x00DA [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00EA
 47: 0x00E2 [0x03] Work_Zone[1] = 1073741824*
 48: 0x00E7 [0x01] GOTO 0x019D
 49: 0x00EA [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0103
 50: 0x00F2 [0x03] Work_Zone[1] = 1*
 51: 0x00F7 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 52: 0x0100 [0x01] GOTO 0x019D
 53: 0x0103 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x011C
 54: 0x010B [0x03] Work_Zone[1] = 2*
 55: 0x0110 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 56: 0x0119 [0x01] GOTO 0x019D
 57: 0x011C [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x014B
 58: 0x0124 [0x03] Work_Zone[1] = 3*
 59: 0x0129 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 60: 0x0132 [0x02] IF !(ExtData[1]->WorkLocal[2] == 8*) GOTO 0x013D
 61: 0x013A [0x01] GOTO 0x0148
 62: 0x013D [0x02] IF !(ExtData[1]->WorkLocal[2] == 9*) GOTO 0x0148
 63: 0x0145 [0x01] GOTO 0x0148

SUBROUTINE_0148:
 64: 0x0148 [0x01] GOTO 0x019D
 65: 0x014B [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0164
 66: 0x0153 [0x03] Work_Zone[1] = 4*
 67: 0x0158 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 68: 0x0161 [0x01] GOTO 0x019D
 69: 0x0164 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x019D
 70: 0x016C [0x03] Work_Zone[1] = 5*
 71: 0x0171 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 72: 0x017A [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 1*])
 73: 0x0180 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[6])
 74: 0x0184 [0x02] IF !(ExtData[1]->WorkLocal[6] <= 5*) GOTO 0x0191
 75: 0x018C [0x03] ExtData[1]->WorkLocal[6] = 5*
 76: 0x0191 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 77: 0x019A [0x01] GOTO 0x019D

SUBROUTINE_019D:
 78: 0x019D [0x1B] RETURN

SUBROUTINE_019F:
 79: 0x019F [0x03] Work_Zone[2] = 0*
 80: 0x01A4 [0x03] Work_Zone[3] = 0*
 81: 0x01A9 [0x03] Work_Zone[4] = 0*
 82: 0x01AE [0x03] Work_Zone[5] = 3*
 83: 0x01B3 [0x03] Work_Zone[6] = 3*
 84: 0x01B8 [0x03] Work_Zone[7] = 1*
 85: 0x01BD [0x03] Work_Zone[8] = 4*
 86: 0x01C2 [0x03] Work_Zone[9] = 2*
 87: 0x01C7 [0x03] Work_Zone_1700[0] = 0*
 88: 0x01CC [0x03] Work_Zone_1700[1] = 1*
 89: 0x01D1 [0x0B] Work_Zone[2]++
 90: 0x01D4 [0x0B] Work_Zone[3]++
 91: 0x01D7 [0x0B] Work_Zone[4]++
 92: 0x01DA [0x0B] Work_Zone[5]++
 93: 0x01DD [0x0B] Work_Zone[6]++
 94: 0x01E0 [0x0B] Work_Zone[7]++
 95: 0x01E3 [0x0B] Work_Zone[8]++
 96: 0x01E6 [0x0B] Work_Zone[9]++
 97: 0x01E9 [0x0B] Work_Zone_1700[0]++
 98: 0x01EC [0x0B] Work_Zone_1700[1]++
 99: 0x01EF [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x019E [0x1B] RETURN
```
