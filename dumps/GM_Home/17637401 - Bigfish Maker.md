# 17637401 - Bigfish Maker

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 1412 bytes        |
| Total Events     | 2                 |
| References Count | 79                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [49](#event-49)       | 0x0001       |   1068 |            231 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D16      |        7446 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x1D18      |        7448 |
|       4 | 0x0137      |         311 |
|       5 | 0x1D17      |        7447 |
|       6 | 0x40000000  |  1073741824 |
|       7 | 0x0002      |           2 |
|       8 | 0x0138      |         312 |
|       9 | 0x0003      |           3 |
|      10 | 0x0139      |         313 |
|      11 | 0x0004      |           4 |
|      12 | 0x013A      |         314 |
|      13 | 0x1D13      |        7443 |
|      14 | 0x0010      |          16 |
|      15 | 0x0017      |          23 |
|      16 | 0x1D14      |        7444 |
|      17 | 0x0018      |          24 |
|      18 | 0x001E      |          30 |
|      19 | 0x0005      |           5 |
|      20 | 0x1D15      |        7445 |
|      21 | 0x001F      |          31 |
|      22 | 0x1C71      |        7281 |
|      23 | 0x0006      |           6 |
|      24 | 0x0007      |           7 |
|      25 | 0x1180      |        4480 |
|      26 | 0x117F      |        4479 |
|      27 | 0x1177      |        4471 |
|      28 | 0x117E      |        4478 |
|      29 | 0x10D0      |        4304 |
|      30 | 0x117A      |        4474 |
|      31 | 0x117B      |        4475 |
|      32 | 0x117C      |        4476 |
|      33 | 0x1400      |        5120 |
|      34 | 0x10D1      |        4305 |
|      35 | 0x1407      |        5127 |
|      36 | 0x1175      |        4469 |
|      37 | 0x10D2      |        4306 |
|      38 | 0x116E      |        4462 |
|      39 | 0x10D3      |        4307 |
|      40 | 0x117D      |        4477 |
|      41 | 0x1166      |        4454 |
|      42 | 0x116F      |        4463 |
|      43 | 0x10DC      |        4316 |
|      44 | 0x10D4      |        4308 |
|      45 | 0x10DF      |        4319 |
|      46 | 0x10D5      |        4309 |
|      47 | 0x1409      |        5129 |
|      48 | 0x1410      |        5136 |
|      49 | 0x15A4      |        5540 |
|      50 | 0x1557      |        5463 |
|      51 | 0x15A1      |        5537 |
|      52 | 0x1563      |        5475 |
|      53 | 0x1415      |        5141 |
|      54 | 0x154A      |        5450 |
|      55 | 0x16B7      |        5815 |
|      56 | 0x154B      |        5451 |
|      57 | 0x140F      |        5135 |
|      58 | 0x155E      |        5470 |
|      59 | 0x16B5      |        5813 |
|      60 | 0x154F      |        5455 |
|      61 | 0x1556      |        5462 |
|      62 | 0x155B      |        5467 |
|      63 | 0x140D      |        5133 |
|      64 | 0x1414      |        5140 |
|      65 | 0x1411      |        5137 |
|      66 | 0x16B6      |        5814 |
|      67 | 0x140E      |        5134 |
|      68 | 0x155F      |        5471 |
|      69 | 0x1564      |        5476 |
|      70 | 0x155C      |        5468 |
|      71 | 0x15A2      |        5538 |
|      72 | 0x15A3      |        5539 |
|      73 | 0x1743      |        5955 |
|      74 | 0x176B      |        5995 |
|      75 | 0x173F      |        5951 |
|      76 | 0x176D      |        5997 |
|      77 | 0x159E      |        5534 |
|      78 | 0x1959      |        6489 |

## String References

- **7281**: Select one [$0i$0j./$1i$1j./$2$3041793/$3i$3j./$4i$4j./$5i$5j./$6i$6j./$7i$7j./Next.]
- **7443**: Size? [Random (default)./Largest./Smallest.]
- **7444**: Weight? [Adjusted random (default)./Adjusted largest (with respect to size)./Adjusted smallest (with respect to size)./Completely random./Largest (regardless of size)./Smallest (regardless of size).]
- **7445**: Is it ranking registerable? [Yes (default)./No.]
- **7446**: What d'ya want? [A big fish!/An effect test!(1)./An effect test!(2)./An effect test!(3)./An effect test!(4)./Nothing!]
- **7447**: Check it out...
- **7448**: Server or client? [Server./Client.]

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

### Event 49

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 1068 bytes |
| Instructions | 197        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 14   $......%.......
0010: 00 01 0F 01 02 00 10 02  80 00 51 00 24 03 80 01  ..........Q.$...
0020: 80 01 80 25 02 00 10 01  80 00 38 00 03 01 10 01  ...%......8.....
0030: 80 43 00 43 01 01 43 00  73 04 80 F0 FF FF 7F F0  .C.C..C.s.......
0040: FF FF 7F 1D 05 80 23 03  01 10 06 80 21 00 01 0F  ......#.....!...
0050: 01 02 00 10 07 80 00 8E  00 24 03 80 01 80 01 80  .........$......
0060: 25 02 00 10 01 80 00 75  00 03 01 10 02 80 43 00  %......u......C.
0070: 43 01 01 80 00 73 08 80  F0 FF FF 7F F0 FF FF 7F  C....s..........
0080: 1D 05 80 23 03 01 10 06  80 21 00 01 0F 01 02 00  ...#.....!......
0090: 10 09 80 00 CB 00 24 03  80 01 80 01 80 25 02 00  ......$......%..
00A0: 10 01 80 00 B2 00 03 01  10 07 80 43 00 43 01 01  ...........C.C..
00B0: BD 00 73 0A 80 F0 FF FF  7F F0 FF FF 7F 1D 05 80  ..s.............
00C0: 23 03 01 10 06 80 21 00  01 0F 01 02 00 10 0B 80  #.....!.........
00D0: 00 08 01 24 03 80 01 80  01 80 25 02 00 10 01 80  ...$......%.....
00E0: 00 EF 00 03 01 10 09 80  43 00 43 01 01 FA 00 73  ........C.C....s
00F0: 0C 80 F0 FF FF 7F F0 FF  FF 7F 1D 05 80 23 03 01  .............#..
0100: 10 06 80 21 00 01 0F 01  03 01 10 06 80 21 00 1A  ...!.........!..
0110: 16 02 03 00 00 01 10 24  0D 80 01 80 01 80 25 02  .......$......%.
0120: 00 10 01 80 00 33 01 40  0E 80 0F 80 01 10 01 80  .....3.@........
0130: 01 64 01 02 00 10 02 80  00 47 01 40 0E 80 0F 80  .d.......G.@....
0140: 01 10 02 80 01 64 01 02  00 10 07 80 00 5B 01 40  .....d.......[.@
0150: 0E 80 0F 80 01 10 07 80  01 64 01 40 0E 80 0F 80  .........d.@....
0160: 01 10 01 80 24 10 80 01  80 01 80 25 02 00 10 01  ....$......%....
0170: 80 00 80 01 40 11 80 12  80 01 10 01 80 01 E4 01  ....@...........
0180: 02 00 10 02 80 00 94 01  40 11 80 12 80 01 10 02  ........@.......
0190: 80 01 E4 01 02 00 10 07  80 00 A8 01 40 11 80 12  ............@...
01A0: 80 01 10 07 80 01 E4 01  02 00 10 09 80 00 BC 01  ................
01B0: 40 11 80 12 80 01 10 09  80 01 E4 01 02 00 10 0B  @...............
01C0: 80 00 D0 01 40 11 80 12  80 01 10 0B 80 01 E4 01  ....@...........
01D0: 02 00 10 13 80 00 E4 01  40 11 80 12 80 01 10 13  ........@.......
01E0: 80 01 E4 01 24 14 80 01  80 01 80 25 02 00 10 01  ....$......%....
01F0: 80 00 00 02 40 15 80 15  80 01 10 01 80 01 14 02  ....@...........
0200: 02 00 10 02 80 00 14 02  40 15 80 15 80 01 10 02  ........@.......
0210: 80 01 14 02 21 00 1A 0E  03 1A 82 02 02 01 10 01  ....!...........
0220: 80 01 25 02 1B 1A 37 03  1A 82 02 02 01 10 01 80  ..%...7.........
0230: 01 34 02 1B 1A 60 03 1A  82 02 02 01 10 01 80 01  .4...`..........
0240: 43 02 1B 1A 89 03 1A 82  02 02 01 10 01 80 01 52  C..............R
0250: 02 1B 1A B2 03 1A 82 02  02 01 10 01 80 01 61 02  ..............a.
0260: 1B 1A DB 03 1A 82 02 02  01 10 01 80 01 70 02 1B  .............p..
0270: 1A 04 04 1A 82 02 02 01  10 01 80 01 7F 02 1B 01  ................
0280: 16 02 06 01 10 24 16 80  01 80 01 80 25 02 00 10  .....$......%...
0290: 01 80 00 9D 02 03 01 10  02 10 01 0D 03 02 00 10  ................
02A0: 02 80 00 AD 02 03 01 10  03 10 01 0D 03 02 00 10  ................
02B0: 07 80 00 BD 02 03 01 10  04 10 01 0D 03 02 00 10  ................
02C0: 09 80 00 CD 02 03 01 10  05 10 01 0D 03 02 00 10  ................
02D0: 0B 80 00 DD 02 03 01 10  06 10 01 0D 03 02 00 10  ................
02E0: 13 80 00 ED 02 03 01 10  07 10 01 0D 03 02 00 10  ................
02F0: 17 80 00 FD 02 03 01 10  08 10 01 0D 03 02 00 10  ................
0300: 18 80 00 0D 03 03 01 10  09 10 01 0D 03 1B 03 02  ................
0310: 10 19 80 03 03 10 1A 80  03 04 10 1B 80 03 05 10  ................
0320: 1C 80 03 06 10 1D 80 03  07 10 1E 80 03 08 10 1F  ................
0330: 80 03 09 10 20 80 1B 03  02 10 21 80 03 03 10 22  .... .....!...."
0340: 80 03 04 10 23 80 03 05  10 24 80 03 06 10 25 80  ....#....$....%.
0350: 03 07 10 26 80 03 08 10  27 80 03 09 10 28 80 1B  ...&....'....(..
0360: 03 02 10 29 80 03 03 10  2A 80 03 04 10 2B 80 03  ...)....*....+..
0370: 05 10 2C 80 03 06 10 2D  80 03 07 10 2E 80 03 08  ..,....-........
0380: 10 2F 80 03 09 10 30 80  1B 03 02 10 31 80 03 03  ./....0.....1...
0390: 10 32 80 03 04 10 33 80  03 05 10 34 80 03 06 10  .2....3....4....
03A0: 35 80 03 07 10 36 80 03  08 10 37 80 03 09 10 38  5....6....7....8
03B0: 80 1B 03 02 10 39 80 03  03 10 3A 80 03 04 10 3B  .....9....:....;
03C0: 80 03 05 10 3C 80 03 06  10 3D 80 03 07 10 3E 80  ....<....=....>.
03D0: 03 08 10 3F 80 03 09 10  40 80 1B 03 02 10 41 80  ...?....@.....A.
03E0: 03 03 10 42 80 03 04 10  43 80 03 05 10 44 80 03  ...B....C....D..
03F0: 06 10 45 80 03 07 10 46  80 03 08 10 47 80 03 09  ..E....F....G...
0400: 10 48 80 1B 03 02 10 49  80 03 03 10 4A 80 03 04  .H.....I....J...
0410: 10 4B 80 03 05 10 4C 80  03 06 10 4D 80 03 07 10  .K....L....M....
0420: 4E 80 03 08 10 01 80 03  09 10 01 80 1B           N............   
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7446*, default_option=0*, option_flags=0*)
    → "What d'ya want? [A big fish!/An effect test!(1)./An effect test!(2)./An effect test!(3)./An effect test!(4)./Nothing!]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0014
  3: 0x0011 [0x01] GOTO 0x010F
  4: 0x0014 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0051
  5: 0x001C [0x24] CREATE_DIALOG(message_id=7448*, default_option=0*, option_flags=0*)
    → "Server or client? [Server./Client.]"
  6: 0x0023 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0024 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0038
  8: 0x002C [0x03] Work_Zone[1] = 0*
  9: 0x0031 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0033 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0035 [0x01] GOTO 0x0043
 12: 0x0038 [0x73] LocalPlayer casts magic 311* on LocalPlayer

SUBROUTINE_0043:
 13: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=7447*)
    → "Check it out..."
 14: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0047 [0x03] Work_Zone[1] = 1073741824*
 16: 0x004C [0x21] END_EVENT
 17: 0x004D [0x00] END_REQSTACK()

SUBROUTINE_0080:
 18: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=7447*)
    → "Check it out..."
 19: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0084 [0x03] Work_Zone[1] = 1073741824*
 21: 0x0089 [0x21] END_EVENT
 22: 0x008A [0x00] END_REQSTACK()

SUBROUTINE_00BD:
 23: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=7447*)
    → "Check it out..."
 24: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x00C1 [0x03] Work_Zone[1] = 1073741824*
 26: 0x00C6 [0x21] END_EVENT
 27: 0x00C7 [0x00] END_REQSTACK()

SUBROUTINE_00FA:
 28: 0x00FA [0x1D] PRINT_EVENT_MESSAGE(message_id=7447*)
    → "Check it out..."
 29: 0x00FD [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x00FE [0x03] Work_Zone[1] = 1073741824*
 31: 0x0103 [0x21] END_EVENT
 32: 0x0104 [0x00] END_REQSTACK()

SUBROUTINE_010F:
 33: 0x010F [0x1A] CALL_SUBROUTINE(address=0x0216)
 34: 0x0112 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[1]
 35: 0x0117 [0x24] CREATE_DIALOG(message_id=7443*, default_option=0*, option_flags=0*)
    → "Size? [Random (default)./Largest./Smallest.]"
 36: 0x011E [0x25] WAIT_DIALOG_SELECT()
 37: 0x011F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0133
 38: 0x0127 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=Work_Zone[1], source=0*)
 39: 0x0130 [0x01] GOTO 0x0164
 40: 0x0133 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0147
 41: 0x013B [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=Work_Zone[1], source=1*)
 42: 0x0144 [0x01] GOTO 0x0164
 43: 0x0147 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x015B
 44: 0x014F [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=Work_Zone[1], source=2*)
 45: 0x0158 [0x01] GOTO 0x0164
 46: 0x015B [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=Work_Zone[1], source=0*)

SUBROUTINE_0164:
 47: 0x0164 [0x24] CREATE_DIALOG(message_id=7444*, default_option=0*, option_flags=0*)
    → "Weight? [Adjusted random (default)./Adjusted largest (with respect to size)./Adjusted smallest (with respect to size)./Completely random./Largest (regardless of size)./Smallest (regardless of size).]"
 48: 0x016B [0x25] WAIT_DIALOG_SELECT()
 49: 0x016C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0180
 50: 0x0174 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=30*, target=Work_Zone[1], source=0*)
 51: 0x017D [0x01] GOTO 0x01E4
 52: 0x0180 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0194
 53: 0x0188 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=30*, target=Work_Zone[1], source=1*)
 54: 0x0191 [0x01] GOTO 0x01E4
 55: 0x0194 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x01A8
 56: 0x019C [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=30*, target=Work_Zone[1], source=2*)
 57: 0x01A5 [0x01] GOTO 0x01E4
 58: 0x01A8 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x01BC
 59: 0x01B0 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=30*, target=Work_Zone[1], source=3*)
 60: 0x01B9 [0x01] GOTO 0x01E4
 61: 0x01BC [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x01D0
 62: 0x01C4 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=30*, target=Work_Zone[1], source=4*)
 63: 0x01CD [0x01] GOTO 0x01E4
 64: 0x01D0 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x01E4
 65: 0x01D8 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=30*, target=Work_Zone[1], source=5*)
 66: 0x01E1 [0x01] GOTO 0x01E4

SUBROUTINE_01E4:
 67: 0x01E4 [0x24] CREATE_DIALOG(message_id=7445*, default_option=0*, option_flags=0*)
    → "Is it ranking registerable? [Yes (default)./No.]"
 68: 0x01EB [0x25] WAIT_DIALOG_SELECT()
 69: 0x01EC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0200
 70: 0x01F4 [0x40] SET_BIT_WORK_RANGE(start_bit=31*, end_bit=31*, target=Work_Zone[1], source=0*)
 71: 0x01FD [0x01] GOTO 0x0214
 72: 0x0200 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0214
 73: 0x0208 [0x40] SET_BIT_WORK_RANGE(start_bit=31*, end_bit=31*, target=Work_Zone[1], source=1*)
 74: 0x0211 [0x01] GOTO 0x0214

SUBROUTINE_0214:
 75: 0x0214 [0x21] END_EVENT
 76: 0x0215 [0x00] END_REQSTACK()

SUBROUTINE_0216:
 77: 0x0216 [0x1A] CALL_SUBROUTINE(address=0x030E)
 78: 0x0219 [0x1A] CALL_SUBROUTINE(address=0x0282)
 79: 0x021C [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0225
 80: 0x0224 [0x1B] RETURN
 81: 0x0225 [0x1A] CALL_SUBROUTINE(address=0x0337)
 82: 0x0228 [0x1A] CALL_SUBROUTINE(address=0x0282)
 83: 0x022B [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0234
 84: 0x0233 [0x1B] RETURN
 85: 0x0234 [0x1A] CALL_SUBROUTINE(address=0x0360)
 86: 0x0237 [0x1A] CALL_SUBROUTINE(address=0x0282)
 87: 0x023A [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0243
 88: 0x0242 [0x1B] RETURN
 89: 0x0243 [0x1A] CALL_SUBROUTINE(address=0x0389)
 90: 0x0246 [0x1A] CALL_SUBROUTINE(address=0x0282)
 91: 0x0249 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0252
 92: 0x0251 [0x1B] RETURN
 93: 0x0252 [0x1A] CALL_SUBROUTINE(address=0x03B2)
 94: 0x0255 [0x1A] CALL_SUBROUTINE(address=0x0282)
 95: 0x0258 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0261
 96: 0x0260 [0x1B] RETURN
 97: 0x0261 [0x1A] CALL_SUBROUTINE(address=0x03DB)
 98: 0x0264 [0x1A] CALL_SUBROUTINE(address=0x0282)
 99: 0x0267 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0270
100: 0x026F [0x1B] RETURN
101: 0x0270 [0x1A] CALL_SUBROUTINE(address=0x0404)
102: 0x0273 [0x1A] CALL_SUBROUTINE(address=0x0282)
103: 0x0276 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x027F
104: 0x027E [0x1B] RETURN
105: 0x027F [0x01] GOTO 0x0216

SUBROUTINE_0282:
106: 0x0282 [0x06] Work_Zone[1] = 0
107: 0x0285 [0x24] CREATE_DIALOG(message_id=7281*, default_option=0*, option_flags=0*)
    → "Select one [$0i$0j./$1i$1j./$2$3041793/$3i$3j./$4i$4j./$5i$5j./$6i$6j./$7i$7j./Next.]"
108: 0x028C [0x25] WAIT_DIALOG_SELECT()
109: 0x028D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x029D
110: 0x0295 [0x03] Work_Zone[1] = Work_Zone[2]
111: 0x029A [0x01] GOTO 0x030D
112: 0x029D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02AD
113: 0x02A5 [0x03] Work_Zone[1] = Work_Zone[3]
114: 0x02AA [0x01] GOTO 0x030D
115: 0x02AD [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x02BD
116: 0x02B5 [0x03] Work_Zone[1] = Work_Zone[4]
117: 0x02BA [0x01] GOTO 0x030D
118: 0x02BD [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x02CD
119: 0x02C5 [0x03] Work_Zone[1] = Work_Zone[5]
120: 0x02CA [0x01] GOTO 0x030D
121: 0x02CD [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x02DD
122: 0x02D5 [0x03] Work_Zone[1] = Work_Zone[6]
123: 0x02DA [0x01] GOTO 0x030D
124: 0x02DD [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x02ED
125: 0x02E5 [0x03] Work_Zone[1] = Work_Zone[7]
126: 0x02EA [0x01] GOTO 0x030D
127: 0x02ED [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x02FD
128: 0x02F5 [0x03] Work_Zone[1] = Work_Zone[8]
129: 0x02FA [0x01] GOTO 0x030D
130: 0x02FD [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x030D
131: 0x0305 [0x03] Work_Zone[1] = Work_Zone[9]
132: 0x030A [0x01] GOTO 0x030D

SUBROUTINE_030D:
133: 0x030D [0x1B] RETURN

SUBROUTINE_030E:
134: 0x030E [0x03] Work_Zone[2] = 4480*
135: 0x0313 [0x03] Work_Zone[3] = 4479*
136: 0x0318 [0x03] Work_Zone[4] = 4471*
137: 0x031D [0x03] Work_Zone[5] = 4478*
138: 0x0322 [0x03] Work_Zone[6] = 4304*
139: 0x0327 [0x03] Work_Zone[7] = 4474*
140: 0x032C [0x03] Work_Zone[8] = 4475*
141: 0x0331 [0x03] Work_Zone[9] = 4476*
142: 0x0336 [0x1B] RETURN

SUBROUTINE_0337:
143: 0x0337 [0x03] Work_Zone[2] = 5120*
144: 0x033C [0x03] Work_Zone[3] = 4305*
145: 0x0341 [0x03] Work_Zone[4] = 5127*
146: 0x0346 [0x03] Work_Zone[5] = 4469*
147: 0x034B [0x03] Work_Zone[6] = 4306*
148: 0x0350 [0x03] Work_Zone[7] = 4462*
149: 0x0355 [0x03] Work_Zone[8] = 4307*
150: 0x035A [0x03] Work_Zone[9] = 4477*
151: 0x035F [0x1B] RETURN

SUBROUTINE_0360:
152: 0x0360 [0x03] Work_Zone[2] = 4454*
153: 0x0365 [0x03] Work_Zone[3] = 4463*
154: 0x036A [0x03] Work_Zone[4] = 4316*
155: 0x036F [0x03] Work_Zone[5] = 4308*
156: 0x0374 [0x03] Work_Zone[6] = 4319*
157: 0x0379 [0x03] Work_Zone[7] = 4309*
158: 0x037E [0x03] Work_Zone[8] = 5129*
159: 0x0383 [0x03] Work_Zone[9] = 5136*
160: 0x0388 [0x1B] RETURN

SUBROUTINE_0389:
161: 0x0389 [0x03] Work_Zone[2] = 5540*
162: 0x038E [0x03] Work_Zone[3] = 5463*
163: 0x0393 [0x03] Work_Zone[4] = 5537*
164: 0x0398 [0x03] Work_Zone[5] = 5475*
165: 0x039D [0x03] Work_Zone[6] = 5141*
166: 0x03A2 [0x03] Work_Zone[7] = 5450*
167: 0x03A7 [0x03] Work_Zone[8] = 5815*
168: 0x03AC [0x03] Work_Zone[9] = 5451*
169: 0x03B1 [0x1B] RETURN

SUBROUTINE_03B2:
170: 0x03B2 [0x03] Work_Zone[2] = 5135*
171: 0x03B7 [0x03] Work_Zone[3] = 5470*
172: 0x03BC [0x03] Work_Zone[4] = 5813*
173: 0x03C1 [0x03] Work_Zone[5] = 5455*
174: 0x03C6 [0x03] Work_Zone[6] = 5462*
175: 0x03CB [0x03] Work_Zone[7] = 5467*
176: 0x03D0 [0x03] Work_Zone[8] = 5133*
177: 0x03D5 [0x03] Work_Zone[9] = 5140*
178: 0x03DA [0x1B] RETURN

SUBROUTINE_03DB:
179: 0x03DB [0x03] Work_Zone[2] = 5137*
180: 0x03E0 [0x03] Work_Zone[3] = 5814*
181: 0x03E5 [0x03] Work_Zone[4] = 5134*
182: 0x03EA [0x03] Work_Zone[5] = 5471*
183: 0x03EF [0x03] Work_Zone[6] = 5476*
184: 0x03F4 [0x03] Work_Zone[7] = 5468*
185: 0x03F9 [0x03] Work_Zone[8] = 5538*
186: 0x03FE [0x03] Work_Zone[9] = 5539*
187: 0x0403 [0x1B] RETURN

SUBROUTINE_0404:
188: 0x0404 [0x03] Work_Zone[2] = 5955*
189: 0x0409 [0x03] Work_Zone[3] = 5995*
190: 0x040E [0x03] Work_Zone[4] = 5951*
191: 0x0413 [0x03] Work_Zone[5] = 5997*
192: 0x0418 [0x03] Work_Zone[6] = 5534*
193: 0x041D [0x03] Work_Zone[7] = 6489*
194: 0x0422 [0x03] Work_Zone[8] = 0*
195: 0x0427 [0x03] Work_Zone[9] = 0*
196: 0x042C [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x004E [0x01] GOTO 0x010F
# Dead code (unreachable instructions):
     0x008B [0x01] GOTO 0x010F
# Dead code (unreachable instructions):
     0x00C8 [0x01] GOTO 0x010F
# Dead code (unreachable instructions):
     0x0105 [0x01] GOTO 0x010F
```
