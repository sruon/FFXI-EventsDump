# 16962145 - Event Master

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 716 bytes                   |
| Total Events     | 2                           |
| References Count | 22                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [501](#event-501)     | 0x0001       |    603 |            120 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x270F      |        9999 |
|       2 | 0x1FD9      |        8153 |
|       3 | 0x0000      |           0 |
|       4 | 0x40000000  |  1073741824 |
|       5 | 0x1FD7      |        8151 |
|       6 | 0x0002      |           2 |
|       7 | 0x0008      |           8 |
|       8 | 0x000F      |          15 |
|       9 | 0x000C      |          12 |
|      10 | 0x0006      |           6 |
|      11 | 0x000A      |          10 |
|      12 | 0x0005      |           5 |
|      13 | 0x0003      |           3 |
|      14 | 0x0004      |           4 |
|      15 | 0x1FDA      |        8154 |
|      16 | 0x0638      |        1592 |
|      17 | 0x0639      |        1593 |
|      18 | 0x1FDB      |        8155 |
|      19 | 0x01F0      |         496 |
|      20 | 0x0010      |          16 |
|      21 | 0x0017      |          23 |

## String References

- **8151**: Current area score: $0 (Rank $1) Enter a number between 0 and 63. (0 to cancel).
- **8153**: Do something? [Nope./Reset fame./Quest 01 (Fame rank: $0/Quest 02 (Fame rank: $1/Quest 03 (Fame rank: $2/Quest 04 (Fame rank: $3/Quest 05 (Fame rank: $4/Quest 06 (Fame rank: $5/Quest 07 (Fame rank: $6/Quest 08 (Fame rank: $7/Quest 09 (Fame rank: $8/Quest 10 (Fame rank: $9/Toggle AP check (currently [on/off]).]
- **8154**: Do something? (Quest ). [Nope./Set to incomplete./Progress report./Obtain key item./Set to complete./Set times completed.]
- **8155**: GjI7i$6226530i . . . . . . .

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
| Data Size    | 603 bytes |
| Instructions | 119       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 04 00 02 10 03 05  00 03 10 03 02 17 04 10   ...............
0010: 05 00 00 02 00 00 00 80  00 0A 01 1A 0B 02 03 02  ................
0020: 00 01 80 24 02 80 03 80  03 80 25 02 00 10 03 80  ...$......%.....
0030: 00 3E 00 06 00 00 03 01  10 04 80 01 8E 00 02 00  .>..............
0040: 10 00 80 00 71 00 03 02  10 04 00 03 03 10 05 00  ....q...........
0050: 48 05 80 03 01 10 03 80  71 12 00 80 06 80 71 13  H.......q.....q.
0060: 01 00 40 07 80 08 80 01  10 01 00 06 00 00 01 8E  ..@.............
0070: 00 02 00 10 09 80 00 84  00 03 01 10 0A 80 06 00  ................
0080: 00 01 8E 00 03 02 00 00  10 08 02 00 06 80 02 02  ................
0090: 00 0B 80 03 07 01 03 03  00 03 80 02 02 00 0A 80  ................
00A0: 01 AA 00 3C 03 00 0C 80  00 80 02 02 00 00 80 80  ...<............
00B0: BC 00 3C 03 00 0D 80 00  80 01 F2 00 02 02 00 06  ..<.............
00C0: 80 80 CE 00 3C 03 00 0D  80 00 80 01 F2 00 02 02  ....<...........
00D0: 00 0E 80 80 E0 00 3C 03  00 0D 80 00 80 01 F2 00  ......<.........
00E0: 02 02 00 07 80 80 F2 00  3C 03 00 0D 80 00 80 01  ........<.......
00F0: F2 00 3C 03 00 06 80 00  80 03 17 17 02 00 0B 17  ..<.............
0100: 17 1A 0C 01 06 00 00 01  13 00 21 00 24 0F 80 03  ..........!.$...
0110: 80 03 00 25 02 00 10 03  80 00 24 01 03 01 10 04  ...%......$.....
0120: 80 01 09 02 02 00 10 00  80 00 3D 01 03 01 10 00  ..........=.....
0130: 80 40 07 80 08 80 01 10  02 00 01 09 02 02 00 10  .@..............
0140: 06 80 00 56 01 03 01 10  06 80 40 07 80 08 80 01  ...V......@.....
0150: 10 02 00 01 09 02 02 00  10 0D 80 00 B7 01 03 01  ................
0160: 10 0D 80 40 07 80 08 80  01 10 02 00 02 02 00 0D  ...@............
0170: 80 80 B4 01 03 02 10 10  80 03 03 10 11 80 24 12  ..............$.
0180: 80 03 80 13 80 25 02 00  10 03 80 00 96 01 03 01  .....%..........
0190: 10 04 80 01 B1 01 02 00  10 00 80 00 A1 01 01 B1  ................
01A0: 01 02 00 10 06 80 00 AC  01 01 B1 01 03 01 10 04  ................
01B0: 80 01 B4 01 01 09 02 02  00 10 0E 80 00 D0 01 03  ................
01C0: 01 10 0E 80 40 07 80 08  80 01 10 02 00 01 09 02  ....@...........
01D0: 02 00 10 0C 80 00 09 02  03 01 10 0C 80 40 07 80  .............@..
01E0: 08 80 01 10 02 00 71 12  00 80 00 80 71 13 06 00  ......q.....q...
01F0: 02 06 00 0C 80 02 FD 01  03 06 00 0C 80 40 14 80  .............@..
0200: 15 80 01 10 06 00 01 09  02 1B 1B 03 02 10 03 80  ................
0210: 03 03 10 03 80 03 04 10  03 80 03 05 10 00 80 03  ................
0220: 06 10 00 80 03 07 10 06  80 03 08 10 06 80 03 09  ................
0230: 10 0D 80 03 00 17 0D 80  03 01 17 0E 80 0B 02 10  ................
0240: 0B 03 10 0B 04 10 0B 05  10 0B 06 10 0B 07 10 0B  ................
0250: 08 10 0B 09 10 0B 00 17  0B 01 17 1B              ............    
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[3]
  2: 0x000B [0x03] Work_Zone_1700[2] = Work_Zone[4]
  3: 0x0010 [0x05] ExtData[1]->WorkLocal[0] = 1
  4: 0x0013 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x010A
  5: 0x001B [0x1A] CALL_SUBROUTINE(address=0x020B)
  6: 0x001E [0x03] ExtData[1]->WorkLocal[2] = 9999*
  7: 0x0023 [0x24] CREATE_DIALOG(message_id=8153*, default_option=0*, option_flags=0*)
    → "Do something? [Nope./Reset fame./Quest 01 (Fame rank: $0/Quest 02 (Fame rank: $1/Quest 03 (Fame rank: $2/Quest 04 (Fame rank: $3/Quest 05 (Fame rank: $4/Quest 06 (Fame rank: $5/Quest 07 (Fame rank: $6/Quest 08 (Fame rank: $7/Quest 09 (Fame rank: $8/Quest 10 (Fame rank: $9/Toggle AP check (currently [on/off]).]"
  8: 0x002A [0x25] WAIT_DIALOG_SELECT()
  9: 0x002B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003E
 10: 0x0033 [0x06] ExtData[1]->WorkLocal[0] = 0
 11: 0x0036 [0x03] Work_Zone[1] = 1073741824*
 12: 0x003B [0x01] GOTO 0x008E
 13: 0x003E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0071
 14: 0x0046 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[4]
 15: 0x004B [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[5]
 16: 0x0050 [0x48] [System] [8151*]:
    → "Current area score: $0 (Rank $1) Enter a number between 0 and 63. (0 to cancel)."
 17: 0x0053 [0x03] Work_Zone[1] = 0*
 18: 0x0058 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 19: 0x005E [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[1])
 20: 0x0062 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 21: 0x006B [0x06] ExtData[1]->WorkLocal[0] = 0
 22: 0x006E [0x01] GOTO 0x008E
 23: 0x0071 [0x02] IF !(Work_Zone[0] == 12*) GOTO 0x0084
 24: 0x0079 [0x03] Work_Zone[1] = 6*
 25: 0x007E [0x06] ExtData[1]->WorkLocal[0] = 0
 26: 0x0081 [0x01] GOTO 0x008E
 27: 0x0084 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[0]
 28: 0x0089 [0x08] ExtData[1]->WorkLocal[2] -= 2*

SUBROUTINE_008E:
 29: 0x008E [0x02] IF !(ExtData[1]->WorkLocal[2] >= 10*) GOTO 0x0107
 30: 0x0096 [0x03] ExtData[1]->WorkLocal[3] = 0*
 31: 0x009B [0x02] IF !(ExtData[1]->WorkLocal[2] == 6*) GOTO 0x00AA
 32: 0x00A3 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=5*, condition_work_offset=1*)
 33: 0x00AA [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00BC
 34: 0x00B2 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=3*, condition_work_offset=1*)
 35: 0x00B9 [0x01] GOTO 0x00F2
 36: 0x00BC [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x00CE
 37: 0x00C4 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=3*, condition_work_offset=1*)
 38: 0x00CB [0x01] GOTO 0x00F2
 39: 0x00CE [0x02] IF !(ExtData[1]->WorkLocal[2] == 4*) GOTO 0x00E0
 40: 0x00D6 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=3*, condition_work_offset=1*)
 41: 0x00DD [0x01] GOTO 0x00F2
 42: 0x00E0 [0x02] IF !(ExtData[1]->WorkLocal[2] == 8*) GOTO 0x00F2
 43: 0x00E8 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=3*, condition_work_offset=1*)
 44: 0x00EF [0x01] GOTO 0x00F2

SUBROUTINE_00F2:
 45: 0x00F2 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=2*, condition_work_offset=1*)
 46: 0x00F9 [0x03] Work_Zone_1700[23] = ExtData[1]->WorkLocal[2]
 47: 0x00FE [0x0B] Work_Zone_1700[23]++
 48: 0x0101 [0x1A] CALL_SUBROUTINE(address=0x010C)
 49: 0x0104 [0x06] ExtData[1]->WorkLocal[0] = 0
 50: 0x0107 [0x01] GOTO 0x0013
 51: 0x010A [0x21] END_EVENT
 52: 0x010B [0x00] END_REQSTACK()

SUBROUTINE_010C:
 53: 0x010C [0x24] CREATE_DIALOG(message_id=8154*, default_option=0*, option_flags=ExtData[1]->WorkLocal[3])
    → "Do something? (Quest ). [Nope./Set to incomplete./Progress report./Obtain key item./Set to complete./Set times completed.]"
 54: 0x0113 [0x25] WAIT_DIALOG_SELECT()
 55: 0x0114 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0124
 56: 0x011C [0x03] Work_Zone[1] = 1073741824*
 57: 0x0121 [0x01] GOTO 0x0209
 58: 0x0124 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x013D
 59: 0x012C [0x03] Work_Zone[1] = 1*
 60: 0x0131 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 61: 0x013A [0x01] GOTO 0x0209
 62: 0x013D [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0156
 63: 0x0145 [0x03] Work_Zone[1] = 2*
 64: 0x014A [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 65: 0x0153 [0x01] GOTO 0x0209
 66: 0x0156 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x01B7
 67: 0x015E [0x03] Work_Zone[1] = 3*
 68: 0x0163 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 69: 0x016C [0x02] IF !(ExtData[1]->WorkLocal[2] == 3*) GOTO 0x01B4
 70: 0x0174 [0x03] Work_Zone[2] = 1592*
 71: 0x0179 [0x03] Work_Zone[3] = 1593*
 72: 0x017E [0x24] CREATE_DIALOG(message_id=8155*, default_option=0*, option_flags=496*)
    → "GjI7i$6226530i . . . . . . ."
 73: 0x0185 [0x25] WAIT_DIALOG_SELECT()
 74: 0x0186 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0196
 75: 0x018E [0x03] Work_Zone[1] = 1073741824*
 76: 0x0193 [0x01] GOTO 0x01B1
 77: 0x0196 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01A1
 78: 0x019E [0x01] GOTO 0x01B1
 79: 0x01A1 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x01AC
 80: 0x01A9 [0x01] GOTO 0x01B1
 81: 0x01AC [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_01B1:
 82: 0x01B1 [0x01] GOTO 0x01B4

SUBROUTINE_01B4:
 83: 0x01B4 [0x01] GOTO 0x0209
 84: 0x01B7 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x01D0
 85: 0x01BF [0x03] Work_Zone[1] = 4*
 86: 0x01C4 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 87: 0x01CD [0x01] GOTO 0x0209
 88: 0x01D0 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0209
 89: 0x01D8 [0x03] Work_Zone[1] = 5*
 90: 0x01DD [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
 91: 0x01E6 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 1*])
 92: 0x01EC [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[6])
 93: 0x01F0 [0x02] IF !(ExtData[1]->WorkLocal[6] <= 5*) GOTO 0x01FD
 94: 0x01F8 [0x03] ExtData[1]->WorkLocal[6] = 5*
 95: 0x01FD [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 96: 0x0206 [0x01] GOTO 0x0209

SUBROUTINE_0209:
 97: 0x0209 [0x1B] RETURN

SUBROUTINE_020B:
 98: 0x020B [0x03] Work_Zone[2] = 0*
 99: 0x0210 [0x03] Work_Zone[3] = 0*
100: 0x0215 [0x03] Work_Zone[4] = 0*
101: 0x021A [0x03] Work_Zone[5] = 1*
102: 0x021F [0x03] Work_Zone[6] = 1*
103: 0x0224 [0x03] Work_Zone[7] = 2*
104: 0x0229 [0x03] Work_Zone[8] = 2*
105: 0x022E [0x03] Work_Zone[9] = 3*
106: 0x0233 [0x03] Work_Zone_1700[0] = 3*
107: 0x0238 [0x03] Work_Zone_1700[1] = 4*
108: 0x023D [0x0B] Work_Zone[2]++
109: 0x0240 [0x0B] Work_Zone[3]++
110: 0x0243 [0x0B] Work_Zone[4]++
111: 0x0246 [0x0B] Work_Zone[5]++
112: 0x0249 [0x0B] Work_Zone[6]++
113: 0x024C [0x0B] Work_Zone[7]++
114: 0x024F [0x0B] Work_Zone[8]++
115: 0x0252 [0x0B] Work_Zone[9]++
116: 0x0255 [0x0B] Work_Zone_1700[0]++
117: 0x0258 [0x0B] Work_Zone_1700[1]++
118: 0x025B [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x020A [0x1B] RETURN
```
