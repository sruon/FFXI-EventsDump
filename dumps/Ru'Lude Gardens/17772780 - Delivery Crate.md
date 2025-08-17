# 17772780 - Delivery Crate

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 1136 bytes                |
| Total Events     | 20                        |
| References Count | 23                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |    101 |             21 |
| [10134](#event-10134)    | 0x0065       |    828 |            156 |
| [10163](#event-10163)    | 0x03A1       |      1 |              1 |
| [10164](#event-10164)    | 0x03A2       |      1 |              1 |
| [10165](#event-10165)    | 0x03A3       |      1 |              1 |
| [10166](#event-10166)    | 0x03A4       |      1 |              1 |
| [10167](#event-10167)    | 0x03A5       |      1 |              1 |
| [10168](#event-10168)    | 0x03A6       |      1 |              1 |
| [65535.1](#event-655351) | 0x03A7       |      1 |              1 |
| [65535.2](#event-655352) | 0x03A8       |      1 |              1 |
| [65535.3](#event-655353) | 0x03A9       |      1 |              1 |
| [65535.4](#event-655354) | 0x03AA       |      1 |              1 |
| [65535.5](#event-655355) | 0x03AB       |      1 |              1 |
| [65535.6](#event-655356) | 0x03AC       |      1 |              1 |
| [10169](#event-10169)    | 0x03AD       |      1 |              1 |
| [10170](#event-10170)    | 0x03AE       |      1 |              1 |
| [10171](#event-10171)    | 0x03AF       |      1 |              1 |
| [10172](#event-10172)    | 0x03B0       |      1 |              1 |
| [10173](#event-10173)    | 0x03B1       |      1 |              1 |
| [10174](#event-10174)    | 0x03B2       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x38E2      |       14562 |
|       3 | 0x38E5      |       14565 |
|       4 | 0x0007      |           7 |
|       5 | 0x0066      |         102 |
|       6 | 0x0008      |           8 |
|       7 | 0x0017      |          23 |
|       8 | 0x40000000  |  1073741824 |
|       9 | 0x0065      |         101 |
|      10 | 0xFFFFFFFF  |  4294967295 |
|      11 | 0x000F      |          15 |
|      12 | 0x0010      |          16 |
|      13 | 0x001F      |          31 |
|      14 | 0x0002      |           2 |
|      15 | 0x0003      |           3 |
|      16 | 0x0004      |           4 |
|      17 | 0x0067      |         103 |
|      18 | 0x0005      |           5 |
|      19 | 0x0006      |           6 |
|      20 | 0x0009      |           9 |
|      21 | 0x38E3      |       14563 |
|      22 | 0x38E4      |       14564 |

## String References

- **14562**: Deposit $2 $0$0 for Trial $0?
- **14563**: Deposit $2 $0 for which of the following trials?
- **14564**: Which trial? [Trial $0 ($10 remaining)./Trial $1 ($11 remaining)./Trial $2 ($12 remaining)./Trial $3 ($13 remaining)./Trial $4 ($14 remaining)./Trial $5 ($15 remaining)./Trial $6 ($16 remaining)./Trial $7 ($17 remaining)./Trial $8 ($18 remaining)./Trial $9 ($19 remaining)./Cancel.]
- **14565**: Deposit $2 $0$0 ? [Yes./No.]

## Events

### Event 65535

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0000    |
| Data Size    | 101 bytes |
| Instructions | 21        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 03 04 00 00 80 03 05 00  00 80 03 06 00 00 80 03  ................
0010: 07 00 00 80 03 08 00 00  80 03 09 00 00 80 03 0A  ................
0020: 00 00 80 03 0B 00 00 80  03 0C 00 00 80 03 0D 00  ................
0030: 00 80 03 0E 00 00 80 03  0F 00 00 80 03 10 00 00  ................
0040: 80 03 11 00 00 80 03 12  00 00 80 03 13 00 00 80  ................
0050: 03 14 00 00 80 03 15 00  00 80 03 16 00 00 80 03  ................
0060: 17 00 00 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0000 [0x03] ExtData[1]->WorkLocal[4] = 0*
  1: 0x0005 [0x03] ExtData[1]->WorkLocal[5] = 0*
  2: 0x000A [0x03] ExtData[1]->WorkLocal[6] = 0*
  3: 0x000F [0x03] ExtData[1]->WorkLocal[7] = 0*
  4: 0x0014 [0x03] ExtData[1]->WorkLocal[8] = 0*
  5: 0x0019 [0x03] ExtData[1]->WorkLocal[9] = 0*
  6: 0x001E [0x03] ExtData[1]->WorkLocal[10] = 0*
  7: 0x0023 [0x03] ExtData[1]->WorkLocal[11] = 0*
  8: 0x0028 [0x03] ExtData[1]->WorkLocal[12] = 0*
  9: 0x002D [0x03] ExtData[1]->WorkLocal[13] = 0*
 10: 0x0032 [0x03] ExtData[1]->WorkLocal[14] = 0*
 11: 0x0037 [0x03] ExtData[1]->WorkLocal[15] = 0*
 12: 0x003C [0x03] ExtData[1]->WorkLocal[16] = 0*
 13: 0x0041 [0x03] ExtData[1]->WorkLocal[17] = 0*
 14: 0x0046 [0x03] ExtData[1]->WorkLocal[18] = 0*
 15: 0x004B [0x03] ExtData[1]->WorkLocal[19] = 0*
 16: 0x0050 [0x03] ExtData[1]->WorkLocal[20] = 0*
 17: 0x0055 [0x03] ExtData[1]->WorkLocal[21] = 0*
 18: 0x005A [0x03] ExtData[1]->WorkLocal[22] = 0*
 19: 0x005F [0x03] ExtData[1]->WorkLocal[23] = 0*
 20: 0x0064 [0x00] END_REQSTACK()
```

### Event 10134

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0065    |
| Data Size    | 828 bytes |
| Instructions | 156       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                42 03 00  00 02 10 03 01 00 03 10       B..........
0070: 03 02 00 04 10 03 04 00  05 10 02 02 00 01 80 02  ................
0080: 88 00 1A D6 00 01 8B 00  1A 8D 00 21 00 03 02 10  ...........!....
0090: 04 00 03 03 10 00 00 03  04 10 01 00 48 02 80 23  ............H..#
00A0: 24 03 80 01 80 00 80 25  02 00 10 00 80 00 C5 00  $......%........
00B0: 40 00 80 04 80 01 10 05  80 40 06 80 07 80 01 10  @........@......
00C0: 04 00 01 D5 00 02 00 10  01 80 00 D5 00 03 01 10  ................
00D0: 08 80 01 D5 00 1B 03 01  10 09 80 43 00 43 01 02  ...........C.C..
00E0: 09 10 0A 80 00 ED 00 03  01 10 08 80 1B 03 18 00  ................
00F0: 08 10 3E 18 00 00 80 FC  00 01 0E 01 41 00 80 0B  ..>.........A...
0100: 80 02 10 04 00 41 0C 80  0D 80 02 10 0E 00 3E 18  .....A........>.
0110: 00 01 80 18 01 01 2A 01  41 00 80 0B 80 03 10 05  ......*.A.......
0120: 00 41 0C 80 0D 80 03 10  0F 00 3E 18 00 0E 80 34  .A........>....4
0130: 01 01 46 01 41 00 80 0B  80 04 10 06 00 41 0C 80  ..F.A........A..
0140: 0D 80 04 10 10 00 3E 18  00 0F 80 50 01 01 62 01  ......>....P..b.
0150: 41 00 80 0B 80 05 10 07  00 41 0C 80 0D 80 05 10  A........A......
0160: 11 00 3E 18 00 10 80 6C  01 01 7E 01 41 00 80 0B  ..>....l..~.A...
0170: 80 06 10 08 00 41 0C 80  0D 80 06 10 12 00 03 01  .....A..........
0180: 10 11 80 43 00 43 01 02  09 10 0A 80 00 95 01 03  ...C.C..........
0190: 01 10 08 80 1B 10 08 10  12 80 0E 18 00 08 10 3E  ...............>
01A0: 18 00 12 80 A9 01 01 BB  01 41 00 80 0B 80 02 10  .........A......
01B0: 09 00 41 0C 80 0D 80 02  10 13 00 3E 18 00 13 80  ..A........>....
01C0: C5 01 01 D7 01 41 00 80  0B 80 03 10 0A 00 41 0C  .....A........A.
01D0: 80 0D 80 03 10 14 00 3E  18 00 04 80 E1 01 01 F3  .......>........
01E0: 01 41 00 80 0B 80 04 10  0B 00 41 0C 80 0D 80 04  .A........A.....
01F0: 10 15 00 3E 18 00 06 80  FD 01 01 0F 02 41 00 80  ...>.........A..
0200: 0B 80 05 10 0C 00 41 0C  80 0D 80 05 10 16 00 3E  ......A........>
0210: 18 00 14 80 19 02 01 2B  02 41 00 80 0B 80 06 10  .......+.A......
0220: 0D 00 41 0C 80 0D 80 06  10 17 00 03 02 10 00 00  ..A.............
0230: 03 04 10 01 00 48 15 80  23 06 19 00 02 19 00 00  .....H..#.......
0240: 80 00 A0 03 03 02 10 04  00 03 03 10 05 00 03 04  ................
0250: 10 06 00 03 05 10 07 00  03 06 10 08 00 03 07 10  ................
0260: 09 00 03 08 10 0A 00 03  09 10 0B 00 03 00 17 0C  ................
0270: 00 03 01 17 0D 00 03 02  17 0E 00 03 03 17 0F 00  ................
0280: 03 04 17 10 00 03 05 17  11 00 03 06 17 12 00 03  ................
0290: 07 17 13 00 03 08 17 14  00 03 09 17 15 00 03 0A  ................
02A0: 17 16 00 03 0B 17 17 00  24 16 80 00 80 18 00 25  ........$......%
02B0: 02 00 10 00 80 00 C0 02  03 03 00 04 00 01 56 03  ..............V.
02C0: 02 00 10 01 80 00 D0 02  03 03 00 05 00 01 56 03  ..............V.
02D0: 02 00 10 0E 80 00 E0 02  03 03 00 06 00 01 56 03  ..............V.
02E0: 02 00 10 0F 80 00 F0 02  03 03 00 07 00 01 56 03  ..............V.
02F0: 02 00 10 10 80 00 00 03  03 03 00 08 00 01 56 03  ..............V.
0300: 02 00 10 12 80 00 10 03  03 03 00 09 00 01 56 03  ..............V.
0310: 02 00 10 13 80 00 20 03  03 03 00 0A 00 01 56 03  ...... .......V.
0320: 02 00 10 04 80 00 30 03  03 03 00 0B 00 01 56 03  ......0.......V.
0330: 02 00 10 06 80 00 40 03  03 03 00 0C 00 01 56 03  ......@.......V.
0340: 02 00 10 14 80 00 50 03  03 03 00 0D 00 01 56 03  ......P.......V.
0350: 03 01 10 08 80 1B 03 02  10 03 00 03 03 10 00 00  ................
0360: 03 04 10 01 00 24 03 80  01 80 00 80 25 02 00 10  .....$......%...
0370: 00 80 00 8D 03 40 00 80  04 80 01 10 05 80 40 06  .....@........@.
0380: 80 07 80 01 10 03 00 05  19 00 01 9D 03 02 00 10  ................
0390: 01 80 00 9D 03 03 01 10  08 80 01 9D 03 01 3C 02  ..............<.
03A0: 1B                                                .               
```

#### Opcodes

```
  0: 0x0065 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0066 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  2: 0x006B [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  3: 0x0070 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  4: 0x0075 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[5]
  5: 0x007A [0x02] IF !(ExtData[1]->WorkLocal[2] <= 1*) GOTO 0x0088
  6: 0x0082 [0x1A] CALL_SUBROUTINE(address=0x00D6)
  7: 0x0085 [0x01] GOTO 0x008B
  8: 0x0088 [0x1A] CALL_SUBROUTINE(address=0x008D)

SUBROUTINE_008B:
  9: 0x008B [0x21] END_EVENT
 10: 0x008C [0x00] END_REQSTACK()

SUBROUTINE_008D:
 11: 0x008D [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[4]
 12: 0x0092 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
 13: 0x0097 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[1]
 14: 0x009C [0x48] [System] [14562*]:
    → "Deposit $2 $0$0 for Trial $0?"
 15: 0x009F [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x00A0 [0x24] CREATE_DIALOG(message_id=14565*, default_option=1*, option_flags=0*)
    → "Deposit $2 $0$0 ? [Yes./No.]"
 17: 0x00A7 [0x25] WAIT_DIALOG_SELECT()
 18: 0x00A8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C5
 19: 0x00B0 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=102*)
 20: 0x00B9 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=23*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[4])
 21: 0x00C2 [0x01] GOTO 0x00D5
 22: 0x00C5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00D5
 23: 0x00CD [0x03] Work_Zone[1] = 1073741824*
 24: 0x00D2 [0x01] GOTO 0x00D5

SUBROUTINE_00D5:
 25: 0x00D5 [0x1B] RETURN

SUBROUTINE_00D6:
 26: 0x00D6 [0x03] Work_Zone[1] = 101*
 27: 0x00DB [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 28: 0x00DD [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 29: 0x00DF [0x02] IF !(Work_Zone[9] == 4294967295*) GOTO 0x00ED
 30: 0x00E7 [0x03] Work_Zone[1] = 1073741824*
 31: 0x00EC [0x1B] RETURN
 32: 0x00ED [0x03] ExtData[1]->WorkLocal[24] = Work_Zone[8]
 33: 0x00F2 [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 0*) GOTO 0x00FC
 34: 0x00F9 [0x01] GOTO 0x010E
 35: 0x00FC [0x41] ExtData[1]->WorkLocal[4] = Work_Zone[2] (bits 0*-15*)
 36: 0x0105 [0x41] ExtData[1]->WorkLocal[14] = Work_Zone[2] (bits 16*-31*)

SUBROUTINE_010E:
 37: 0x010E [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 1*) GOTO 0x0118
 38: 0x0115 [0x01] GOTO 0x012A
 39: 0x0118 [0x41] ExtData[1]->WorkLocal[5] = Work_Zone[3] (bits 0*-15*)
 40: 0x0121 [0x41] ExtData[1]->WorkLocal[15] = Work_Zone[3] (bits 16*-31*)

SUBROUTINE_012A:
 41: 0x012A [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 2*) GOTO 0x0134
 42: 0x0131 [0x01] GOTO 0x0146
 43: 0x0134 [0x41] ExtData[1]->WorkLocal[6] = Work_Zone[4] (bits 0*-15*)
 44: 0x013D [0x41] ExtData[1]->WorkLocal[16] = Work_Zone[4] (bits 16*-31*)

SUBROUTINE_0146:
 45: 0x0146 [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 3*) GOTO 0x0150
 46: 0x014D [0x01] GOTO 0x0162
 47: 0x0150 [0x41] ExtData[1]->WorkLocal[7] = Work_Zone[5] (bits 0*-15*)
 48: 0x0159 [0x41] ExtData[1]->WorkLocal[17] = Work_Zone[5] (bits 16*-31*)

SUBROUTINE_0162:
 49: 0x0162 [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 4*) GOTO 0x016C
 50: 0x0169 [0x01] GOTO 0x017E
 51: 0x016C [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[6] (bits 0*-15*)
 52: 0x0175 [0x41] ExtData[1]->WorkLocal[18] = Work_Zone[6] (bits 16*-31*)

SUBROUTINE_017E:
 53: 0x017E [0x03] Work_Zone[1] = 103*
 54: 0x0183 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 55: 0x0185 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 56: 0x0187 [0x02] IF !(Work_Zone[9] == 4294967295*) GOTO 0x0195
 57: 0x018F [0x03] Work_Zone[1] = 1073741824*
 58: 0x0194 [0x1B] RETURN
 59: 0x0195 [0x10] Work_Zone[8] <<= 5*
 60: 0x019A [0x0E] ExtData[1]->WorkLocal[24] |= Work_Zone[8]
 61: 0x019F [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 5*) GOTO 0x01A9
 62: 0x01A6 [0x01] GOTO 0x01BB
 63: 0x01A9 [0x41] ExtData[1]->WorkLocal[9] = Work_Zone[2] (bits 0*-15*)
 64: 0x01B2 [0x41] ExtData[1]->WorkLocal[19] = Work_Zone[2] (bits 16*-31*)

SUBROUTINE_01BB:
 65: 0x01BB [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 6*) GOTO 0x01C5
 66: 0x01C2 [0x01] GOTO 0x01D7
 67: 0x01C5 [0x41] ExtData[1]->WorkLocal[10] = Work_Zone[3] (bits 0*-15*)
 68: 0x01CE [0x41] ExtData[1]->WorkLocal[20] = Work_Zone[3] (bits 16*-31*)

SUBROUTINE_01D7:
 69: 0x01D7 [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 7*) GOTO 0x01E1
 70: 0x01DE [0x01] GOTO 0x01F3
 71: 0x01E1 [0x41] ExtData[1]->WorkLocal[11] = Work_Zone[4] (bits 0*-15*)
 72: 0x01EA [0x41] ExtData[1]->WorkLocal[21] = Work_Zone[4] (bits 16*-31*)

SUBROUTINE_01F3:
 73: 0x01F3 [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 8*) GOTO 0x01FD
 74: 0x01FA [0x01] GOTO 0x020F
 75: 0x01FD [0x41] ExtData[1]->WorkLocal[12] = Work_Zone[5] (bits 0*-15*)
 76: 0x0206 [0x41] ExtData[1]->WorkLocal[22] = Work_Zone[5] (bits 16*-31*)

SUBROUTINE_020F:
 77: 0x020F [0x3E] IF !(ExtData[1]->WorkLocal[24] bit 9*) GOTO 0x0219
 78: 0x0216 [0x01] GOTO 0x022B
 79: 0x0219 [0x41] ExtData[1]->WorkLocal[13] = Work_Zone[6] (bits 0*-15*)
 80: 0x0222 [0x41] ExtData[1]->WorkLocal[23] = Work_Zone[6] (bits 16*-31*)

SUBROUTINE_022B:
 81: 0x022B [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 82: 0x0230 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[1]
 83: 0x0235 [0x48] [System] [14563*]:
    → "Deposit $2 $0 for which of the following trials?"
 84: 0x0238 [0x23] WAIT_FOR_DIALOG_INTERACTION
 85: 0x0239 [0x06] ExtData[1]->WorkLocal[25] = 0

SUBROUTINE_023C:
 86: 0x023C [0x02] IF !(ExtData[1]->WorkLocal[25] == 0*) GOTO 0x03A0
 87: 0x0244 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[4]
 88: 0x0249 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[5]
 89: 0x024E [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[6]
 90: 0x0253 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[7]
 91: 0x0258 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[8]
 92: 0x025D [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[9]
 93: 0x0262 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[10]
 94: 0x0267 [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[11]
 95: 0x026C [0x03] Work_Zone_1700[0] = ExtData[1]->WorkLocal[12]
 96: 0x0271 [0x03] Work_Zone_1700[1] = ExtData[1]->WorkLocal[13]
 97: 0x0276 [0x03] Work_Zone_1700[2] = ExtData[1]->WorkLocal[14]
 98: 0x027B [0x03] Work_Zone_1700[3] = ExtData[1]->WorkLocal[15]
 99: 0x0280 [0x03] Work_Zone_1700[4] = ExtData[1]->WorkLocal[16]
100: 0x0285 [0x03] Work_Zone_1700[5] = ExtData[1]->WorkLocal[17]
101: 0x028A [0x03] Work_Zone_1700[6] = ExtData[1]->WorkLocal[18]
102: 0x028F [0x03] Work_Zone_1700[7] = ExtData[1]->WorkLocal[19]
103: 0x0294 [0x03] Work_Zone_1700[8] = ExtData[1]->WorkLocal[20]
104: 0x0299 [0x03] Work_Zone_1700[9] = ExtData[1]->WorkLocal[21]
105: 0x029E [0x03] Work_Zone_1700[10] = ExtData[1]->WorkLocal[22]
106: 0x02A3 [0x03] Work_Zone_1700[11] = ExtData[1]->WorkLocal[23]
107: 0x02A8 [0x24] CREATE_DIALOG(message_id=14564*, default_option=0*, option_flags=ExtData[1]->WorkLocal[24])
    → "Which trial? [Trial $0 ($10 remaining)./Trial $1 ($11 remaining)./Trial $2 ($12 remaining)./Trial $3 ($13 remaining)./Trial $4 ($14 remaining)./Trial $5 ($15 remaining)./Trial $6 ($16 remaining)./Trial $7 ($17 remaining)./Trial $8 ($18 remaining)./Trial $9 ($19 remaining)./Cancel.]"
108: 0x02AF [0x25] WAIT_DIALOG_SELECT()
109: 0x02B0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02C0
110: 0x02B8 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[4]
111: 0x02BD [0x01] GOTO 0x0356
112: 0x02C0 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02D0
113: 0x02C8 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[5]
114: 0x02CD [0x01] GOTO 0x0356
115: 0x02D0 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x02E0
116: 0x02D8 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[6]
117: 0x02DD [0x01] GOTO 0x0356
118: 0x02E0 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x02F0
119: 0x02E8 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[7]
120: 0x02ED [0x01] GOTO 0x0356
121: 0x02F0 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0300
122: 0x02F8 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[8]
123: 0x02FD [0x01] GOTO 0x0356
124: 0x0300 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0310
125: 0x0308 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[9]
126: 0x030D [0x01] GOTO 0x0356
127: 0x0310 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0320
128: 0x0318 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[10]
129: 0x031D [0x01] GOTO 0x0356
130: 0x0320 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0330
131: 0x0328 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[11]
132: 0x032D [0x01] GOTO 0x0356
133: 0x0330 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x0340
134: 0x0338 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[12]
135: 0x033D [0x01] GOTO 0x0356
136: 0x0340 [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x0350
137: 0x0348 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[13]
138: 0x034D [0x01] GOTO 0x0356
139: 0x0350 [0x03] Work_Zone[1] = 1073741824*
140: 0x0355 [0x1B] RETURN

SUBROUTINE_0356:
141: 0x0356 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[3]
142: 0x035B [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
143: 0x0360 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[1]
144: 0x0365 [0x24] CREATE_DIALOG(message_id=14565*, default_option=1*, option_flags=0*)
    → "Deposit $2 $0$0 ? [Yes./No.]"
145: 0x036C [0x25] WAIT_DIALOG_SELECT()
146: 0x036D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x038D
147: 0x0375 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=102*)
148: 0x037E [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=23*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[3])
149: 0x0387 [0x05] ExtData[1]->WorkLocal[25] = 1
150: 0x038A [0x01] GOTO 0x039D
151: 0x038D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x039D
152: 0x0395 [0x03] Work_Zone[1] = 1073741824*
153: 0x039A [0x01] GOTO 0x039D

SUBROUTINE_039D:
154: 0x039D [0x01] GOTO 0x023C
155: 0x03A0 [0x1B] RETURN
```

### Event 10163

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:    00                                              .              
```

#### Opcodes

```
  0: 0x03A1 [0x00] END_REQSTACK()
```

### Event 10164

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:       00                                            .             
```

#### Opcodes

```
  0: 0x03A2 [0x00] END_REQSTACK()
```

### Event 10165

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:          00                                          .            
```

#### Opcodes

```
  0: 0x03A3 [0x00] END_REQSTACK()
```

### Event 10166

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:             00                                        .           
```

#### Opcodes

```
  0: 0x03A4 [0x00] END_REQSTACK()
```

### Event 10167

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                00                                      .          
```

#### Opcodes

```
  0: 0x03A5 [0x00] END_REQSTACK()
```

### Event 10168

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                   00                                    .         
```

#### Opcodes

```
  0: 0x03A6 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                      00                                  .        
```

#### Opcodes

```
  0: 0x03A7 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                          00                               .       
```

#### Opcodes

```
  0: 0x03A8 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03A9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                             00                             .      
```

#### Opcodes

```
  0: 0x03A9 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03AA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                                00                           .     
```

#### Opcodes

```
  0: 0x03AA [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03AB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                                   00                         .    
```

#### Opcodes

```
  0: 0x03AB [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03AC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                                      00                       .   
```

#### Opcodes

```
  0: 0x03AC [0x00] END_REQSTACK()
```

### Event 10169

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03AD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                                         00                     .  
```

#### Opcodes

```
  0: 0x03AD [0x00] END_REQSTACK()
```

### Event 10170

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03AE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                                            00                   . 
```

#### Opcodes

```
  0: 0x03AE [0x00] END_REQSTACK()
```

### Event 10171

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03AF  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                                               00                 .
```

#### Opcodes

```
  0: 0x03AF [0x00] END_REQSTACK()
```

### Event 10172

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03B0  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0: 00                                                .               
```

#### Opcodes

```
  0: 0x03B0 [0x00] END_REQSTACK()
```

### Event 10173

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03B1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:    00                                              .              
```

#### Opcodes

```
  0: 0x03B1 [0x00] END_REQSTACK()
```

### Event 10174

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03B2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:       00                                            .             
```

#### Opcodes

```
  0: 0x03B2 [0x00] END_REQSTACK()
```
