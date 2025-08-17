# 16999074 - Riftworn Pyxis

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Arrapago Reef (ID: 54) |
| Block Size       | 1432 bytes             |
| Total Events     | 2                      |
| References Count | 33                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [6005](#event-6005)   | 0x0001       |   1275 |            240 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x0003      |           3 |
|       4 | 0x0004      |           4 |
|       5 | 0x0005      |           5 |
|       6 | 0x0006      |           6 |
|       7 | 0x0007      |           7 |
|       8 | 0x0008      |           8 |
|       9 | 0x237B      |        9083 |
|      10 | 0x40000000  |  1073741824 |
|      11 | 0x0009      |           9 |
|      12 | 0x000A      |          10 |
|      13 | 0x2359      |        9049 |
|      14 | 0x237C      |        9084 |
|      15 | 0x000F      |          15 |
|      16 | 0x0010      |          16 |
|      17 | 0x001F      |          31 |
|      18 | 0x237D      |        9085 |
|      19 | 0x235F      |        9055 |
|      20 | 0x2E50      |       11856 |
|      21 | 0x2E51      |       11857 |
|      22 | 0x2E4F      |       11855 |
|      23 | 0x2E5C      |       11868 |
|      24 | 0x2E5A      |       11866 |
|      25 | 0x2E5B      |       11867 |
|      26 | 0x4AC9      |       19145 |
|      27 | 0x4AE6      |       19174 |
|      28 | 0x4AC8      |       19144 |
|      29 | 0x49D8      |       18904 |
|      30 | 0x4819      |       18457 |
|      31 | 0x486E      |       18542 |
|      32 | 0x4D52      |       19794 |

## String References

- **9049**: Obtain this item?
- **9055**: Relinquish all reward items? [Yes, relinquish./On second thought...]
- **9083**: Which item will you obtain? [None of them./[/$0./$1./$2./$3./$4./$5./$6./$7./Relinquish all./Obtain all.]
- **9084**: Obtain the $0? [Yes./No./Obtain as pulse cell.]
- **9085**: One or more of the items you are about to obtain can be converted into pulse cells.

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

### Event 6005

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 1275 bytes |
| Instructions | 240        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 00 80 20 01  03 02 00 00 80 03 04 00   ..... .........
0010: 00 80 03 05 00 00 80 03  06 00 00 80 03 07 00 00  ................
0020: 80 03 08 00 00 80 03 09  00 00 80 03 0A 00 00 80  ................
0030: 03 0B 00 00 80 03 0C 00  00 80 03 0D 00 00 80 03  ................
0040: 06 00 02 10 03 07 00 03  10 03 08 00 04 10 03 09  ................
0050: 00 05 10 03 0A 00 06 10  03 0B 00 07 10 03 0C 00  ................
0060: 08 10 03 0D 00 09 10 03  01 00 00 80 02 06 00 00  ................
0070: 80 00 B1 00 02 07 00 00  80 00 B1 00 02 08 00 00  ................
0080: 80 00 B1 00 02 09 00 00  80 00 B1 00 02 0A 00 00  ................
0090: 80 00 B1 00 02 0B 00 00  80 00 B1 00 02 0C 00 00  ................
00A0: 80 00 B1 00 02 0D 00 00  80 00 B1 00 03 01 00 01  ................
00B0: 80 02 01 00 00 80 00 21  04 03 05 00 00 80 02 06  .......!........
00C0: 00 00 80 00 CD 00 3C 05  00 01 80 01 80 02 07 00  ......<.........
00D0: 00 80 00 DC 00 3C 05 00  02 80 01 80 02 08 00 00  .....<..........
00E0: 80 00 EB 00 3C 05 00 03  80 01 80 02 09 00 00 80  ....<...........
00F0: 00 FA 00 3C 05 00 04 80  01 80 02 0A 00 00 80 00  ...<............
0100: 09 01 3C 05 00 05 80 01  80 02 0B 00 00 80 00 18  ..<.............
0110: 01 3C 05 00 06 80 01 80  02 0C 00 00 80 00 27 01  .<............'.
0120: 3C 05 00 07 80 01 80 02  0D 00 00 80 00 36 01 3C  <............6.<
0130: 05 00 08 80 01 80 03 01  00 00 80 02 06 00 00 80  ................
0140: 01 46 01 0B 01 00 02 07  00 00 80 01 51 01 0B 01  .F..........Q...
0150: 00 02 08 00 00 80 01 5C  01 0B 01 00 02 09 00 00  .......\........
0160: 80 01 67 01 0B 01 00 02  0A 00 00 80 01 72 01 0B  ..g..........r..
0170: 01 00 02 0B 00 00 80 01  7D 01 0B 01 00 02 0C 00  ........}.......
0180: 00 80 01 88 01 0B 01 00  02 0D 00 00 80 01 93 01  ................
0190: 0B 01 00 05 04 00 02 04  00 00 80 02 21 04 03 02  ............!...
01A0: 00 00 80 03 02 10 06 00  03 03 10 07 00 03 04 10  ................
01B0: 08 00 03 05 10 09 00 03  06 10 0A 00 03 07 10 0B  ................
01C0: 00 03 08 10 0C 00 03 09  10 0D 00 1A 26 04 02 0F  ............&...
01D0: 00 00 80 01 DE 01 03 00  17 01 80 01 E3 01 03 00  ................
01E0: 17 00 80 24 09 80 00 80  05 00 25 02 00 10 00 80  ...$......%.....
01F0: 00 FE 01 06 04 00 03 01  10 0A 80 01 D0 02 02 00  ................
0200: 10 01 80 00 13 02 03 03  00 06 00 03 02 00 01 80  ................
0210: 01 D0 02 02 00 10 02 80  00 28 02 03 03 00 07 00  .........(......
0220: 03 02 00 02 80 01 D0 02  02 00 10 03 80 00 3D 02  ..............=.
0230: 03 03 00 08 00 03 02 00  03 80 01 D0 02 02 00 10  ................
0240: 04 80 00 52 02 03 03 00  09 00 03 02 00 04 80 01  ...R............
0250: D0 02 02 00 10 05 80 00  67 02 03 03 00 0A 00 03  ........g.......
0260: 02 00 05 80 01 D0 02 02  00 10 06 80 00 7C 02 03  .............|..
0270: 03 00 0B 00 03 02 00 06  80 01 D0 02 02 00 10 07  ................
0280: 80 00 91 02 03 03 00 0C  00 03 02 00 07 80 01 D0  ................
0290: 02 02 00 10 08 80 00 A6  02 03 03 00 0D 00 03 02  ................
02A0: 00 08 80 01 D0 02 02 00  10 0B 80 00 BB 02 03 03  ................
02B0: 00 00 80 03 02 00 0B 80  01 D0 02 02 00 10 0C 80  ................
02C0: 00 D0 02 03 03 00 00 80  03 02 00 0C 80 01 D0 02  ................
02D0: 02 02 00 08 80 05 6E 03  02 00 10 01 80 04 6B 03  ......n.......k.
02E0: 02 00 10 08 80 05 6B 03  02 03 00 00 80 01 6B 03  ......k.......k.
02F0: 93 03 00 48 0D 80 23 93  00 80 03 02 10 03 00 03  ...H..#.........
0300: 0E 00 00 80 02 02 00 01  80 00 1E 03 02 00 17 00  ................
0310: 80 00 1B 03 3C 0E 00 02  80 01 80 01 25 03 3C 0E  ....<.......%.<.
0320: 00 02 80 01 80 24 0E 80  01 80 0E 00 25 02 00 10  .....$......%...
0330: 00 80 00 40 03 06 04 00  03 01 10 02 00 01 6B 03  ...@..........k.
0340: 02 00 10 01 80 00 4B 03  01 6B 03 02 00 10 02 80  ......K..k......
0350: 00 6B 03 06 04 00 40 00  80 0F 80 01 10 02 00 40  .k....@........@
0360: 10 80 11 80 01 10 01 80  01 6B 03 01 1E 04 02 00  .........k......
0370: 10 0C 80 00 F0 03 02 03  00 00 80 00 ED 03 1A 26  ...............&
0380: 04 02 0F 00 00 80 00 94  03 06 04 00 03 01 10 02  ................
0390: 00 01 ED 03 48 12 80 23  93 06 00 48 0D 80 23 93  ....H..#...H..#.
03A0: 00 80 03 02 10 06 00 24  0E 80 01 80 00 80 25 02  .......$......%.
03B0: 00 10 00 80 00 C2 03 06  04 00 03 01 10 02 00 01  ................
03C0: ED 03 02 00 10 01 80 00  CD 03 01 ED 03 02 00 10  ................
03D0: 02 80 00 ED 03 06 04 00  40 00 80 0F 80 01 10 02  ........@.......
03E0: 00 40 10 80 11 80 01 10  01 80 01 ED 03 01 1E 04  .@..............
03F0: 02 00 10 0B 80 00 1E 04  24 13 80 01 80 00 80 25  ........$......%
0400: 02 00 10 00 80 00 13 04  06 04 00 03 01 10 02 00  ................
0410: 01 1E 04 02 00 10 01 80  00 1E 04 01 1E 04 01 96  ................
0420: 01 42 20 00 21 00 03 0F  00 00 80 02 06 00 14 80  .B .!...........
0430: 80 3B 04 03 0F 00 01 80  01 FB 04 02 06 00 15 80  .;..............
0440: 80 4B 04 03 0F 00 01 80  01 FB 04 02 06 00 16 80  .K..............
0450: 80 5B 04 03 0F 00 01 80  01 FB 04 02 06 00 17 80  .[..............
0460: 80 6B 04 03 0F 00 01 80  01 FB 04 02 06 00 18 80  .k..............
0470: 80 7B 04 03 0F 00 01 80  01 FB 04 02 06 00 19 80  .{..............
0480: 80 8B 04 03 0F 00 01 80  01 FB 04 02 06 00 1A 80  ................
0490: 80 9B 04 03 0F 00 01 80  01 FB 04 02 06 00 1B 80  ................
04A0: 80 AB 04 03 0F 00 01 80  01 FB 04 02 06 00 1C 80  ................
04B0: 80 BB 04 03 0F 00 01 80  01 FB 04 02 06 00 1D 80  ................
04C0: 80 CB 04 03 0F 00 01 80  01 FB 04 02 06 00 1E 80  ................
04D0: 80 DB 04 03 0F 00 01 80  01 FB 04 02 06 00 1F 80  ................
04E0: 80 EB 04 03 0F 00 01 80  01 FB 04 02 06 00 20 80  .............. .
04F0: 80 FB 04 03 0F 00 01 80  01 FB 04 1B              ............    
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x0006 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[2] = 0*
  3: 0x000D [0x03] ExtData[1]->WorkLocal[4] = 0*
  4: 0x0012 [0x03] ExtData[1]->WorkLocal[5] = 0*
  5: 0x0017 [0x03] ExtData[1]->WorkLocal[6] = 0*
  6: 0x001C [0x03] ExtData[1]->WorkLocal[7] = 0*
  7: 0x0021 [0x03] ExtData[1]->WorkLocal[8] = 0*
  8: 0x0026 [0x03] ExtData[1]->WorkLocal[9] = 0*
  9: 0x002B [0x03] ExtData[1]->WorkLocal[10] = 0*
 10: 0x0030 [0x03] ExtData[1]->WorkLocal[11] = 0*
 11: 0x0035 [0x03] ExtData[1]->WorkLocal[12] = 0*
 12: 0x003A [0x03] ExtData[1]->WorkLocal[13] = 0*
 13: 0x003F [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[2]
 14: 0x0044 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[3]
 15: 0x0049 [0x03] ExtData[1]->WorkLocal[8] = Work_Zone[4]
 16: 0x004E [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[5]
 17: 0x0053 [0x03] ExtData[1]->WorkLocal[10] = Work_Zone[6]
 18: 0x0058 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[7]
 19: 0x005D [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[8]
 20: 0x0062 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[9]
 21: 0x0067 [0x03] ExtData[1]->WorkLocal[1] = 0*
 22: 0x006C [0x02] IF !(ExtData[1]->WorkLocal[6] == 0*) GOTO 0x00B1
 23: 0x0074 [0x02] IF !(ExtData[1]->WorkLocal[7] == 0*) GOTO 0x00B1
 24: 0x007C [0x02] IF !(ExtData[1]->WorkLocal[8] == 0*) GOTO 0x00B1
 25: 0x0084 [0x02] IF !(ExtData[1]->WorkLocal[9] == 0*) GOTO 0x00B1
 26: 0x008C [0x02] IF !(ExtData[1]->WorkLocal[10] == 0*) GOTO 0x00B1
 27: 0x0094 [0x02] IF !(ExtData[1]->WorkLocal[11] == 0*) GOTO 0x00B1
 28: 0x009C [0x02] IF !(ExtData[1]->WorkLocal[12] == 0*) GOTO 0x00B1
 29: 0x00A4 [0x02] IF !(ExtData[1]->WorkLocal[13] == 0*) GOTO 0x00B1
 30: 0x00AC [0x03] ExtData[1]->WorkLocal[1] = 1*
 31: 0x00B1 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0421
 32: 0x00B9 [0x03] ExtData[1]->WorkLocal[5] = 0*
 33: 0x00BE [0x02] IF !(ExtData[1]->WorkLocal[6] == 0*) GOTO 0x00CD
 34: 0x00C6 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[5], bit_index_work_offset=1*, condition_work_offset=1*)
 35: 0x00CD [0x02] IF !(ExtData[1]->WorkLocal[7] == 0*) GOTO 0x00DC
 36: 0x00D5 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[5], bit_index_work_offset=2*, condition_work_offset=1*)
 37: 0x00DC [0x02] IF !(ExtData[1]->WorkLocal[8] == 0*) GOTO 0x00EB
 38: 0x00E4 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[5], bit_index_work_offset=3*, condition_work_offset=1*)
 39: 0x00EB [0x02] IF !(ExtData[1]->WorkLocal[9] == 0*) GOTO 0x00FA
 40: 0x00F3 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[5], bit_index_work_offset=4*, condition_work_offset=1*)
 41: 0x00FA [0x02] IF !(ExtData[1]->WorkLocal[10] == 0*) GOTO 0x0109
 42: 0x0102 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[5], bit_index_work_offset=5*, condition_work_offset=1*)
 43: 0x0109 [0x02] IF !(ExtData[1]->WorkLocal[11] == 0*) GOTO 0x0118
 44: 0x0111 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[5], bit_index_work_offset=6*, condition_work_offset=1*)
 45: 0x0118 [0x02] IF !(ExtData[1]->WorkLocal[12] == 0*) GOTO 0x0127
 46: 0x0120 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[5], bit_index_work_offset=7*, condition_work_offset=1*)
 47: 0x0127 [0x02] IF !(ExtData[1]->WorkLocal[13] == 0*) GOTO 0x0136
 48: 0x012F [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[5], bit_index_work_offset=8*, condition_work_offset=1*)
 49: 0x0136 [0x03] ExtData[1]->WorkLocal[1] = 0*
 50: 0x013B [0x02] IF !(ExtData[1]->WorkLocal[6] == 0*) GOTO 0x0146
 51: 0x0143 [0x0B] ExtData[1]->WorkLocal[1]++
 52: 0x0146 [0x02] IF !(ExtData[1]->WorkLocal[7] == 0*) GOTO 0x0151
 53: 0x014E [0x0B] ExtData[1]->WorkLocal[1]++
 54: 0x0151 [0x02] IF !(ExtData[1]->WorkLocal[8] == 0*) GOTO 0x015C
 55: 0x0159 [0x0B] ExtData[1]->WorkLocal[1]++
 56: 0x015C [0x02] IF !(ExtData[1]->WorkLocal[9] == 0*) GOTO 0x0167
 57: 0x0164 [0x0B] ExtData[1]->WorkLocal[1]++
 58: 0x0167 [0x02] IF !(ExtData[1]->WorkLocal[10] == 0*) GOTO 0x0172
 59: 0x016F [0x0B] ExtData[1]->WorkLocal[1]++
 60: 0x0172 [0x02] IF !(ExtData[1]->WorkLocal[11] == 0*) GOTO 0x017D
 61: 0x017A [0x0B] ExtData[1]->WorkLocal[1]++
 62: 0x017D [0x02] IF !(ExtData[1]->WorkLocal[12] == 0*) GOTO 0x0188
 63: 0x0185 [0x0B] ExtData[1]->WorkLocal[1]++
 64: 0x0188 [0x02] IF !(ExtData[1]->WorkLocal[13] == 0*) GOTO 0x0193
 65: 0x0190 [0x0B] ExtData[1]->WorkLocal[1]++
 66: 0x0193 [0x05] ExtData[1]->WorkLocal[4] = 1
 67: 0x0196 [0x02] IF !(ExtData[1]->WorkLocal[4] <= 0*) GOTO 0x0421
 68: 0x019E [0x03] ExtData[1]->WorkLocal[2] = 0*
 69: 0x01A3 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[6]
 70: 0x01A8 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[7]
 71: 0x01AD [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[8]
 72: 0x01B2 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[9]
 73: 0x01B7 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[10]
 74: 0x01BC [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[11]
 75: 0x01C1 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[12]
 76: 0x01C6 [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[13]
 77: 0x01CB [0x1A] CALL_SUBROUTINE(address=0x0426)
 78: 0x01CE [0x02] IF !(ExtData[1]->WorkLocal[15] == 0*) GOTO 0x01DE
 79: 0x01D6 [0x03] Work_Zone_1700[0] = 1*
 80: 0x01DB [0x01] GOTO 0x01E3
 81: 0x01DE [0x03] Work_Zone_1700[0] = 0*

SUBROUTINE_01E3:
 82: 0x01E3 [0x24] CREATE_DIALOG(message_id=9083*, default_option=0*, option_flags=ExtData[1]->WorkLocal[5])
    → "Which item will you obtain? [None of them./[/$0./$1./$2./$3./$4./$5./$6./$7./Relinquish all./Obtain all.]"
 83: 0x01EA [0x25] WAIT_DIALOG_SELECT()
 84: 0x01EB [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01FE
 85: 0x01F3 [0x06] ExtData[1]->WorkLocal[4] = 0
 86: 0x01F6 [0x03] Work_Zone[1] = 1073741824*
 87: 0x01FB [0x01] GOTO 0x02D0
 88: 0x01FE [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0213
 89: 0x0206 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[6]
 90: 0x020B [0x03] ExtData[1]->WorkLocal[2] = 1*
 91: 0x0210 [0x01] GOTO 0x02D0
 92: 0x0213 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0228
 93: 0x021B [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[7]
 94: 0x0220 [0x03] ExtData[1]->WorkLocal[2] = 2*
 95: 0x0225 [0x01] GOTO 0x02D0
 96: 0x0228 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x023D
 97: 0x0230 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[8]
 98: 0x0235 [0x03] ExtData[1]->WorkLocal[2] = 3*
 99: 0x023A [0x01] GOTO 0x02D0
100: 0x023D [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0252
101: 0x0245 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[9]
102: 0x024A [0x03] ExtData[1]->WorkLocal[2] = 4*
103: 0x024F [0x01] GOTO 0x02D0
104: 0x0252 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0267
105: 0x025A [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[10]
106: 0x025F [0x03] ExtData[1]->WorkLocal[2] = 5*
107: 0x0264 [0x01] GOTO 0x02D0
108: 0x0267 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x027C
109: 0x026F [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[11]
110: 0x0274 [0x03] ExtData[1]->WorkLocal[2] = 6*
111: 0x0279 [0x01] GOTO 0x02D0
112: 0x027C [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0291
113: 0x0284 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[12]
114: 0x0289 [0x03] ExtData[1]->WorkLocal[2] = 7*
115: 0x028E [0x01] GOTO 0x02D0
116: 0x0291 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x02A6
117: 0x0299 [0x03] ExtData[1]->WorkLocal[3] = ExtData[1]->WorkLocal[13]
118: 0x029E [0x03] ExtData[1]->WorkLocal[2] = 8*
119: 0x02A3 [0x01] GOTO 0x02D0
120: 0x02A6 [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x02BB
121: 0x02AE [0x03] ExtData[1]->WorkLocal[3] = 0*
122: 0x02B3 [0x03] ExtData[1]->WorkLocal[2] = 9*
123: 0x02B8 [0x01] GOTO 0x02D0
124: 0x02BB [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x02D0
125: 0x02C3 [0x03] ExtData[1]->WorkLocal[3] = 0*
126: 0x02C8 [0x03] ExtData[1]->WorkLocal[2] = 10*
127: 0x02CD [0x01] GOTO 0x02D0

SUBROUTINE_02D0:
128: 0x02D0 [0x02] IF !(ExtData[1]->WorkLocal[2] > 8*) GOTO 0x036E
129: 0x02D8 [0x02] IF !(Work_Zone[0] < 1*) GOTO 0x036B
130: 0x02E0 [0x02] IF !(Work_Zone[0] > 8*) GOTO 0x036B
131: 0x02E8 [0x02] IF !(ExtData[1]->WorkLocal[3] == 0*) GOTO 0x036B
132: 0x02F0 [0x93] DISPLAY_ITEM_INFO(item_id=ExtData[1]->WorkLocal[3])
133: 0x02F3 [0x48] [System] [9049*]:
    → "Obtain this item?"
134: 0x02F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
135: 0x02F7 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
136: 0x02FA [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[3]
137: 0x02FF [0x03] ExtData[1]->WorkLocal[14] = 0*
138: 0x0304 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x031E
139: 0x030C [0x02] IF !(Work_Zone_1700[0] == 0*) GOTO 0x031B
140: 0x0314 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[14], bit_index_work_offset=2*, condition_work_offset=1*)
141: 0x031B [0x01] GOTO 0x0325
142: 0x031E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[14], bit_index_work_offset=2*, condition_work_offset=1*)

SUBROUTINE_0325:
143: 0x0325 [0x24] CREATE_DIALOG(message_id=9084*, default_option=1*, option_flags=ExtData[1]->WorkLocal[14])
    → "Obtain the $0? [Yes./No./Obtain as pulse cell.]"
144: 0x032C [0x25] WAIT_DIALOG_SELECT()
145: 0x032D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0340
146: 0x0335 [0x06] ExtData[1]->WorkLocal[4] = 0
147: 0x0338 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
148: 0x033D [0x01] GOTO 0x036B
149: 0x0340 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x034B
150: 0x0348 [0x01] GOTO 0x036B
151: 0x034B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x036B
152: 0x0353 [0x06] ExtData[1]->WorkLocal[4] = 0
153: 0x0356 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
154: 0x035F [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=1*)
155: 0x0368 [0x01] GOTO 0x036B

SUBROUTINE_036B:
156: 0x036B [0x01] GOTO 0x041E
157: 0x036E [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x03F0
158: 0x0376 [0x02] IF !(ExtData[1]->WorkLocal[3] == 0*) GOTO 0x03ED
159: 0x037E [0x1A] CALL_SUBROUTINE(address=0x0426)
160: 0x0381 [0x02] IF !(ExtData[1]->WorkLocal[15] == 0*) GOTO 0x0394
161: 0x0389 [0x06] ExtData[1]->WorkLocal[4] = 0
162: 0x038C [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
163: 0x0391 [0x01] GOTO 0x03ED
164: 0x0394 [0x48] [System] [9085*]:
    → "One or more of the items you are about to obtain can be converted into pulse cells."
165: 0x0397 [0x23] WAIT_FOR_DIALOG_INTERACTION
166: 0x0398 [0x93] DISPLAY_ITEM_INFO(item_id=ExtData[1]->WorkLocal[6])
167: 0x039B [0x48] [System] [9049*]:
    → "Obtain this item?"
168: 0x039E [0x23] WAIT_FOR_DIALOG_INTERACTION
169: 0x039F [0x93] DISPLAY_ITEM_INFO(item_id=0*)
170: 0x03A2 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[6]
171: 0x03A7 [0x24] CREATE_DIALOG(message_id=9084*, default_option=1*, option_flags=0*)
    → "Obtain the $0? [Yes./No./Obtain as pulse cell.]"
172: 0x03AE [0x25] WAIT_DIALOG_SELECT()
173: 0x03AF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03C2
174: 0x03B7 [0x06] ExtData[1]->WorkLocal[4] = 0
175: 0x03BA [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
176: 0x03BF [0x01] GOTO 0x03ED
177: 0x03C2 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03CD
178: 0x03CA [0x01] GOTO 0x03ED
179: 0x03CD [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x03ED
180: 0x03D5 [0x06] ExtData[1]->WorkLocal[4] = 0
181: 0x03D8 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[2])
182: 0x03E1 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=1*)
183: 0x03EA [0x01] GOTO 0x03ED

SUBROUTINE_03ED:
184: 0x03ED [0x01] GOTO 0x041E
185: 0x03F0 [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x041E
186: 0x03F8 [0x24] CREATE_DIALOG(message_id=9055*, default_option=1*, option_flags=0*)
    → "Relinquish all reward items? [Yes, relinquish./On second thought...]"
187: 0x03FF [0x25] WAIT_DIALOG_SELECT()
188: 0x0400 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0413
189: 0x0408 [0x06] ExtData[1]->WorkLocal[4] = 0
190: 0x040B [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
191: 0x0410 [0x01] GOTO 0x041E
192: 0x0413 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x041E
193: 0x041B [0x01] GOTO 0x041E

SUBROUTINE_041E:
194: 0x041E [0x01] GOTO 0x0196
195: 0x0421 [0x42] SET_CLI_EVENT_CANCEL_DATA()
196: 0x0422 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
197: 0x0424 [0x21] END_EVENT
198: 0x0425 [0x00] END_REQSTACK()

SUBROUTINE_0426:
199: 0x0426 [0x03] ExtData[1]->WorkLocal[15] = 0*
200: 0x042B [0x02] IF !(ExtData[1]->WorkLocal[6] == 11856*) GOTO 0x043B
201: 0x0433 [0x03] ExtData[1]->WorkLocal[15] = 1*
202: 0x0438 [0x01] GOTO 0x04FB
203: 0x043B [0x02] IF !(ExtData[1]->WorkLocal[6] == 11857*) GOTO 0x044B
204: 0x0443 [0x03] ExtData[1]->WorkLocal[15] = 1*
205: 0x0448 [0x01] GOTO 0x04FB
206: 0x044B [0x02] IF !(ExtData[1]->WorkLocal[6] == 11855*) GOTO 0x045B
207: 0x0453 [0x03] ExtData[1]->WorkLocal[15] = 1*
208: 0x0458 [0x01] GOTO 0x04FB
209: 0x045B [0x02] IF !(ExtData[1]->WorkLocal[6] == 11868*) GOTO 0x046B
210: 0x0463 [0x03] ExtData[1]->WorkLocal[15] = 1*
211: 0x0468 [0x01] GOTO 0x04FB
212: 0x046B [0x02] IF !(ExtData[1]->WorkLocal[6] == 11866*) GOTO 0x047B
213: 0x0473 [0x03] ExtData[1]->WorkLocal[15] = 1*
214: 0x0478 [0x01] GOTO 0x04FB
215: 0x047B [0x02] IF !(ExtData[1]->WorkLocal[6] == 11867*) GOTO 0x048B
216: 0x0483 [0x03] ExtData[1]->WorkLocal[15] = 1*
217: 0x0488 [0x01] GOTO 0x04FB
218: 0x048B [0x02] IF !(ExtData[1]->WorkLocal[6] == 19145*) GOTO 0x049B
219: 0x0493 [0x03] ExtData[1]->WorkLocal[15] = 1*
220: 0x0498 [0x01] GOTO 0x04FB
221: 0x049B [0x02] IF !(ExtData[1]->WorkLocal[6] == 19174*) GOTO 0x04AB
222: 0x04A3 [0x03] ExtData[1]->WorkLocal[15] = 1*
223: 0x04A8 [0x01] GOTO 0x04FB
224: 0x04AB [0x02] IF !(ExtData[1]->WorkLocal[6] == 19144*) GOTO 0x04BB
225: 0x04B3 [0x03] ExtData[1]->WorkLocal[15] = 1*
226: 0x04B8 [0x01] GOTO 0x04FB
227: 0x04BB [0x02] IF !(ExtData[1]->WorkLocal[6] == 18904*) GOTO 0x04CB
228: 0x04C3 [0x03] ExtData[1]->WorkLocal[15] = 1*
229: 0x04C8 [0x01] GOTO 0x04FB
230: 0x04CB [0x02] IF !(ExtData[1]->WorkLocal[6] == 18457*) GOTO 0x04DB
231: 0x04D3 [0x03] ExtData[1]->WorkLocal[15] = 1*
232: 0x04D8 [0x01] GOTO 0x04FB
233: 0x04DB [0x02] IF !(ExtData[1]->WorkLocal[6] == 18542*) GOTO 0x04EB
234: 0x04E3 [0x03] ExtData[1]->WorkLocal[15] = 1*
235: 0x04E8 [0x01] GOTO 0x04FB
236: 0x04EB [0x02] IF !(ExtData[1]->WorkLocal[6] == 19794*) GOTO 0x04FB
237: 0x04F3 [0x03] ExtData[1]->WorkLocal[15] = 1*
238: 0x04F8 [0x01] GOTO 0x04FB

SUBROUTINE_04FB:
239: 0x04FB [0x1B] RETURN
```
