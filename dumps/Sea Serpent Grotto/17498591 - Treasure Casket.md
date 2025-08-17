# 17498591 - Treasure Casket

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Sea Serpent Grotto (ID: 176) |
| Block Size       | 1808 bytes                   |
| Total Events     | 5                            |
| References Count | 25                           |

## List of Events

| Event ID            | Entrypoint   |   Size |   Instructions |
|---------------------|--------------|--------|----------------|
| [1036](#event-1036) | 0x0000       |    521 |             97 |
| [1037](#event-1037) | 0x0209       |    521 |             97 |
| [1038](#event-1038) | 0x0412       |    187 |             40 |
| [1060](#event-1060) | 0x04CD       |    443 |             85 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0xFFFFFFFF  |  4294967295 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x0004      |           4 |
|       7 | 0x0005      |           5 |
|       8 | 0x0006      |           6 |
|       9 | 0x0007      |           7 |
|      10 | 0x0008      |           8 |
|      11 | 0x1DBB      |        7611 |
|      12 | 0x1DD5      |        7637 |
|      13 | 0x1DBD      |        7613 |
|      14 | 0x000F      |          15 |
|      15 | 0x0010      |          16 |
|      16 | 0x001F      |          31 |
|      17 | 0x1DBC      |        7612 |
|      18 | 0x1DBE      |        7614 |
|      19 | 0x1DC3      |        7619 |
|      20 | 0x1DC4      |        7620 |
|      21 | 0x1DC5      |        7621 |
|      22 | 0x1DC6      |        7622 |
|      23 | 0x000A      |          10 |
|      24 | 0x270F      |        9999 |

## String References

- **7611**: Which item will you obtain? [None of them./$0./$1./$2./$3./$4./$5./$6./$7.]
- **7612**: Which temporary item will you obtain? [None of them./$0./$1./$2./$3./$4./$5./$6./$7.]
- **7613**: Obtain this item? [Yes./No.]
- **7614**: Obtain this temporary item? [Yes./No.]
- **7619**: The chest is locked.
- **7620**: What will you do? [Leave it be./Attempt to unlock it.]
- **7621**: What will you do? ($0 chances remaining.) [Give up./Enter a combination./Examine the lock.]
- **7622**: It appears that you can enter a two-digit combination between 10 and 99.
- **7637**: Obtain this item?

## Events

### Event 1036

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0000    |
| Data Size    | 521 bytes |
| Instructions | 97        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 20 01 1C 00 80 03 00 00  02 10 03 01 00 03 10 03   ...............
0010: 02 00 04 10 03 03 00 05  10 03 04 00 06 10 03 05  ................
0020: 00 07 10 03 06 00 08 10  03 07 00 09 10 03 08 00  ................
0030: 01 80 03 09 00 02 80 03  0A 00 02 80 03 0B 00 02  ................
0040: 80 03 0C 00 02 80 3D 08  00 02 80 03 80 02 00 00  ......=.........
0050: 02 80 02 61 00 3D 08 00  03 80 03 80 03 02 10 00  ...a.=..........
0060: 00 02 01 00 02 80 02 75  00 3D 08 00 04 80 03 80  .......u.=......
0070: 03 03 10 01 00 02 02 00  02 80 02 89 00 3D 08 00  .............=..
0080: 05 80 03 80 03 04 10 02  00 02 03 00 02 80 02 9D  ................
0090: 00 3D 08 00 06 80 03 80  03 05 10 03 00 02 04 00  .=..............
00A0: 02 80 02 B1 00 3D 08 00  07 80 03 80 03 06 10 04  .....=..........
00B0: 00 02 05 00 02 80 02 C5  00 3D 08 00 08 80 03 80  .........=......
00C0: 03 07 10 05 00 02 06 00  02 80 02 D9 00 3D 08 00  .............=..
00D0: 09 80 03 80 03 08 10 06  00 02 07 00 02 80 02 ED  ................
00E0: 00 3D 08 00 0A 80 03 80  03 09 10 07 00 24 0B 80  .=...........$..
00F0: 02 80 08 00 25 02 00 10  02 80 00 0A 01 03 09 00  ....%...........
0100: 02 80 03 0C 00 02 80 01  B2 01 02 00 10 03 80 00  ................
0110: 1F 01 03 0C 00 00 00 03  09 00 03 80 01 B2 01 02  ................
0120: 00 10 04 80 00 34 01 03  0C 00 01 00 03 09 00 04  .....4..........
0130: 80 01 B2 01 02 00 10 05  80 00 49 01 03 0C 00 02  ..........I.....
0140: 00 03 09 00 05 80 01 B2  01 02 00 10 06 80 00 5E  ...............^
0150: 01 03 0C 00 03 00 03 09  00 06 80 01 B2 01 02 00  ................
0160: 10 07 80 00 73 01 03 0C  00 04 00 03 09 00 07 80  ....s...........
0170: 01 B2 01 02 00 10 08 80  00 88 01 03 0C 00 05 00  ................
0180: 03 09 00 08 80 01 B2 01  02 00 10 09 80 00 9D 01  ................
0190: 03 0C 00 06 00 03 09 00  09 80 01 B2 01 02 00 10  ................
01A0: 0A 80 00 B2 01 03 0C 00  07 00 03 09 00 0A 80 01  ................
01B0: B2 01 02 09 00 02 80 02  06 02 02 0C 00 02 80 02  ................
01C0: 06 02 93 0C 00 48 0C 80  23 93 02 80 24 0D 80 03  .....H..#...$...
01D0: 80 02 80 25 02 00 10 02  80 00 E4 01 03 0A 00 03  ...%............
01E0: 80 01 F4 01 02 00 10 03  80 00 F4 01 03 0A 00 04  ................
01F0: 80 01 F4 01 40 02 80 0E  80 01 10 09 00 40 0F 80  ....@........@..
0200: 10 80 01 10 0A 00 42 21  00                       ......B!.       
```

#### Opcodes

```
  0: 0x0000 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0002 [0x1C] WAIT(60* ticks)
  2: 0x0005 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x000A [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  4: 0x000F [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  5: 0x0014 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  6: 0x0019 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[6]
  7: 0x001E [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[7]
  8: 0x0023 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[8]
  9: 0x0028 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[9]
 10: 0x002D [0x03] ExtData[1]->WorkLocal[8] = 4294967295*
 11: 0x0032 [0x03] ExtData[1]->WorkLocal[9] = 0*
 12: 0x0037 [0x03] ExtData[1]->WorkLocal[10] = 0*
 13: 0x003C [0x03] ExtData[1]->WorkLocal[11] = 0*
 14: 0x0041 [0x03] ExtData[1]->WorkLocal[12] = 0*
 15: 0x0046 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=0*, condition_work_offset=1*)
 16: 0x004D [0x02] IF !(ExtData[1]->WorkLocal[0] <= 0*) GOTO 0x0061
 17: 0x0055 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=1*, condition_work_offset=1*)
 18: 0x005C [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 19: 0x0061 [0x02] IF !(ExtData[1]->WorkLocal[1] <= 0*) GOTO 0x0075
 20: 0x0069 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=2*, condition_work_offset=1*)
 21: 0x0070 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
 22: 0x0075 [0x02] IF !(ExtData[1]->WorkLocal[2] <= 0*) GOTO 0x0089
 23: 0x007D [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=3*, condition_work_offset=1*)
 24: 0x0084 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[2]
 25: 0x0089 [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x009D
 26: 0x0091 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=4*, condition_work_offset=1*)
 27: 0x0098 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[3]
 28: 0x009D [0x02] IF !(ExtData[1]->WorkLocal[4] <= 0*) GOTO 0x00B1
 29: 0x00A5 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=5*, condition_work_offset=1*)
 30: 0x00AC [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[4]
 31: 0x00B1 [0x02] IF !(ExtData[1]->WorkLocal[5] <= 0*) GOTO 0x00C5
 32: 0x00B9 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=6*, condition_work_offset=1*)
 33: 0x00C0 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[5]
 34: 0x00C5 [0x02] IF !(ExtData[1]->WorkLocal[6] <= 0*) GOTO 0x00D9
 35: 0x00CD [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=7*, condition_work_offset=1*)
 36: 0x00D4 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[6]
 37: 0x00D9 [0x02] IF !(ExtData[1]->WorkLocal[7] <= 0*) GOTO 0x00ED
 38: 0x00E1 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=8*, condition_work_offset=1*)
 39: 0x00E8 [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[7]
 40: 0x00ED [0x24] CREATE_DIALOG(message_id=7611*, default_option=0*, option_flags=ExtData[1]->WorkLocal[8])
    → "Which item will you obtain? [None of them./$0./$1./$2./$3./$4./$5./$6./$7.]"
 41: 0x00F4 [0x25] WAIT_DIALOG_SELECT()
 42: 0x00F5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x010A
 43: 0x00FD [0x03] ExtData[1]->WorkLocal[9] = 0*
 44: 0x0102 [0x03] ExtData[1]->WorkLocal[12] = 0*
 45: 0x0107 [0x01] GOTO 0x01B2
 46: 0x010A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x011F
 47: 0x0112 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[0]
 48: 0x0117 [0x03] ExtData[1]->WorkLocal[9] = 1*
 49: 0x011C [0x01] GOTO 0x01B2
 50: 0x011F [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0134
 51: 0x0127 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[1]
 52: 0x012C [0x03] ExtData[1]->WorkLocal[9] = 2*
 53: 0x0131 [0x01] GOTO 0x01B2
 54: 0x0134 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0149
 55: 0x013C [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[2]
 56: 0x0141 [0x03] ExtData[1]->WorkLocal[9] = 3*
 57: 0x0146 [0x01] GOTO 0x01B2
 58: 0x0149 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x015E
 59: 0x0151 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[3]
 60: 0x0156 [0x03] ExtData[1]->WorkLocal[9] = 4*
 61: 0x015B [0x01] GOTO 0x01B2
 62: 0x015E [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0173
 63: 0x0166 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[4]
 64: 0x016B [0x03] ExtData[1]->WorkLocal[9] = 5*
 65: 0x0170 [0x01] GOTO 0x01B2
 66: 0x0173 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0188
 67: 0x017B [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[5]
 68: 0x0180 [0x03] ExtData[1]->WorkLocal[9] = 6*
 69: 0x0185 [0x01] GOTO 0x01B2
 70: 0x0188 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x019D
 71: 0x0190 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[6]
 72: 0x0195 [0x03] ExtData[1]->WorkLocal[9] = 7*
 73: 0x019A [0x01] GOTO 0x01B2
 74: 0x019D [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x01B2
 75: 0x01A5 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[7]
 76: 0x01AA [0x03] ExtData[1]->WorkLocal[9] = 8*
 77: 0x01AF [0x01] GOTO 0x01B2

SUBROUTINE_01B2:
 78: 0x01B2 [0x02] IF !(ExtData[1]->WorkLocal[9] <= 0*) GOTO 0x0206
 79: 0x01BA [0x02] IF !(ExtData[1]->WorkLocal[12] <= 0*) GOTO 0x0206
 80: 0x01C2 [0x93] DISPLAY_ITEM_INFO(item_id=ExtData[1]->WorkLocal[12])
 81: 0x01C5 [0x48] [System] [7637*]:
    → "Obtain this item?"
 82: 0x01C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 83: 0x01C9 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 84: 0x01CC [0x24] CREATE_DIALOG(message_id=7613*, default_option=1*, option_flags=0*)
    → "Obtain this item? [Yes./No.]"
 85: 0x01D3 [0x25] WAIT_DIALOG_SELECT()
 86: 0x01D4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01E4
 87: 0x01DC [0x03] ExtData[1]->WorkLocal[10] = 1*
 88: 0x01E1 [0x01] GOTO 0x01F4
 89: 0x01E4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01F4
 90: 0x01EC [0x03] ExtData[1]->WorkLocal[10] = 2*
 91: 0x01F1 [0x01] GOTO 0x01F4

SUBROUTINE_01F4:
 92: 0x01F4 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[9])
 93: 0x01FD [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[10])
 94: 0x0206 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 95: 0x0207 [0x21] END_EVENT
 96: 0x0208 [0x00] END_REQSTACK()
```

### Event 1037

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0209    |
| Data Size    | 521 bytes |
| Instructions | 97        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                             20 01 1C 00 80 03 00            ......
0210: 00 02 10 03 01 00 03 10  03 02 00 04 10 03 03 00  ................
0220: 05 10 03 04 00 06 10 03  05 00 07 10 03 06 00 08  ................
0230: 10 03 07 00 09 10 03 08  00 01 80 03 09 00 02 80  ................
0240: 03 0A 00 02 80 03 0B 00  02 80 03 0C 00 02 80 3D  ...............=
0250: 08 00 02 80 03 80 02 00  00 02 80 02 6A 02 3D 08  ............j.=.
0260: 00 03 80 03 80 03 02 10  00 00 02 01 00 02 80 02  ................
0270: 7E 02 3D 08 00 04 80 03  80 03 03 10 01 00 02 02  ~.=.............
0280: 00 02 80 02 92 02 3D 08  00 05 80 03 80 03 04 10  ......=.........
0290: 02 00 02 03 00 02 80 02  A6 02 3D 08 00 06 80 03  ..........=.....
02A0: 80 03 05 10 03 00 02 04  00 02 80 02 BA 02 3D 08  ..............=.
02B0: 00 07 80 03 80 03 06 10  04 00 02 05 00 02 80 02  ................
02C0: CE 02 3D 08 00 08 80 03  80 03 07 10 05 00 02 06  ..=.............
02D0: 00 02 80 02 E2 02 3D 08  00 09 80 03 80 03 08 10  ......=.........
02E0: 06 00 02 07 00 02 80 02  F6 02 3D 08 00 0A 80 03  ..........=.....
02F0: 80 03 09 10 07 00 24 11  80 02 80 08 00 25 02 00  ......$......%..
0300: 10 02 80 00 13 03 03 09  00 02 80 03 0C 00 02 80  ................
0310: 01 BB 03 02 00 10 03 80  00 28 03 03 0C 00 00 00  .........(......
0320: 03 09 00 03 80 01 BB 03  02 00 10 04 80 00 3D 03  ..............=.
0330: 03 0C 00 01 00 03 09 00  04 80 01 BB 03 02 00 10  ................
0340: 05 80 00 52 03 03 0C 00  02 00 03 09 00 05 80 01  ...R............
0350: BB 03 02 00 10 06 80 00  67 03 03 0C 00 03 00 03  ........g.......
0360: 09 00 06 80 01 BB 03 02  00 10 07 80 00 7C 03 03  .............|..
0370: 0C 00 04 00 03 09 00 07  80 01 BB 03 02 00 10 08  ................
0380: 80 00 91 03 03 0C 00 05  00 03 09 00 08 80 01 BB  ................
0390: 03 02 00 10 09 80 00 A6  03 03 0C 00 06 00 03 09  ................
03A0: 00 09 80 01 BB 03 02 00  10 0A 80 00 BB 03 03 0C  ................
03B0: 00 07 00 03 09 00 0A 80  01 BB 03 02 09 00 02 80  ................
03C0: 02 0F 04 02 0C 00 02 80  02 0F 04 93 0C 00 48 0C  ..............H.
03D0: 80 23 93 02 80 24 12 80  03 80 02 80 25 02 00 10  .#...$......%...
03E0: 02 80 00 ED 03 03 0A 00  03 80 01 FD 03 02 00 10  ................
03F0: 03 80 00 FD 03 03 0A 00  04 80 01 FD 03 40 02 80  .............@..
0400: 0E 80 01 10 09 00 40 0F  80 10 80 01 10 0A 00 42  ......@........B
0410: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0209 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x020B [0x1C] WAIT(60* ticks)
  2: 0x020E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x0213 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  4: 0x0218 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  5: 0x021D [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  6: 0x0222 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[6]
  7: 0x0227 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[7]
  8: 0x022C [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[8]
  9: 0x0231 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[9]
 10: 0x0236 [0x03] ExtData[1]->WorkLocal[8] = 4294967295*
 11: 0x023B [0x03] ExtData[1]->WorkLocal[9] = 0*
 12: 0x0240 [0x03] ExtData[1]->WorkLocal[10] = 0*
 13: 0x0245 [0x03] ExtData[1]->WorkLocal[11] = 0*
 14: 0x024A [0x03] ExtData[1]->WorkLocal[12] = 0*
 15: 0x024F [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=0*, condition_work_offset=1*)
 16: 0x0256 [0x02] IF !(ExtData[1]->WorkLocal[0] <= 0*) GOTO 0x026A
 17: 0x025E [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=1*, condition_work_offset=1*)
 18: 0x0265 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 19: 0x026A [0x02] IF !(ExtData[1]->WorkLocal[1] <= 0*) GOTO 0x027E
 20: 0x0272 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=2*, condition_work_offset=1*)
 21: 0x0279 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
 22: 0x027E [0x02] IF !(ExtData[1]->WorkLocal[2] <= 0*) GOTO 0x0292
 23: 0x0286 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=3*, condition_work_offset=1*)
 24: 0x028D [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[2]
 25: 0x0292 [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x02A6
 26: 0x029A [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=4*, condition_work_offset=1*)
 27: 0x02A1 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[3]
 28: 0x02A6 [0x02] IF !(ExtData[1]->WorkLocal[4] <= 0*) GOTO 0x02BA
 29: 0x02AE [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=5*, condition_work_offset=1*)
 30: 0x02B5 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[4]
 31: 0x02BA [0x02] IF !(ExtData[1]->WorkLocal[5] <= 0*) GOTO 0x02CE
 32: 0x02C2 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=6*, condition_work_offset=1*)
 33: 0x02C9 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[5]
 34: 0x02CE [0x02] IF !(ExtData[1]->WorkLocal[6] <= 0*) GOTO 0x02E2
 35: 0x02D6 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=7*, condition_work_offset=1*)
 36: 0x02DD [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[6]
 37: 0x02E2 [0x02] IF !(ExtData[1]->WorkLocal[7] <= 0*) GOTO 0x02F6
 38: 0x02EA [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=8*, condition_work_offset=1*)
 39: 0x02F1 [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[7]
 40: 0x02F6 [0x24] CREATE_DIALOG(message_id=7612*, default_option=0*, option_flags=ExtData[1]->WorkLocal[8])
    → "Which temporary item will you obtain? [None of them./$0./$1./$2./$3./$4./$5./$6./$7.]"
 41: 0x02FD [0x25] WAIT_DIALOG_SELECT()
 42: 0x02FE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0313
 43: 0x0306 [0x03] ExtData[1]->WorkLocal[9] = 0*
 44: 0x030B [0x03] ExtData[1]->WorkLocal[12] = 0*
 45: 0x0310 [0x01] GOTO 0x03BB
 46: 0x0313 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0328
 47: 0x031B [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[0]
 48: 0x0320 [0x03] ExtData[1]->WorkLocal[9] = 1*
 49: 0x0325 [0x01] GOTO 0x03BB
 50: 0x0328 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x033D
 51: 0x0330 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[1]
 52: 0x0335 [0x03] ExtData[1]->WorkLocal[9] = 2*
 53: 0x033A [0x01] GOTO 0x03BB
 54: 0x033D [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0352
 55: 0x0345 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[2]
 56: 0x034A [0x03] ExtData[1]->WorkLocal[9] = 3*
 57: 0x034F [0x01] GOTO 0x03BB
 58: 0x0352 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0367
 59: 0x035A [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[3]
 60: 0x035F [0x03] ExtData[1]->WorkLocal[9] = 4*
 61: 0x0364 [0x01] GOTO 0x03BB
 62: 0x0367 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x037C
 63: 0x036F [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[4]
 64: 0x0374 [0x03] ExtData[1]->WorkLocal[9] = 5*
 65: 0x0379 [0x01] GOTO 0x03BB
 66: 0x037C [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0391
 67: 0x0384 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[5]
 68: 0x0389 [0x03] ExtData[1]->WorkLocal[9] = 6*
 69: 0x038E [0x01] GOTO 0x03BB
 70: 0x0391 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x03A6
 71: 0x0399 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[6]
 72: 0x039E [0x03] ExtData[1]->WorkLocal[9] = 7*
 73: 0x03A3 [0x01] GOTO 0x03BB
 74: 0x03A6 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x03BB
 75: 0x03AE [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[7]
 76: 0x03B3 [0x03] ExtData[1]->WorkLocal[9] = 8*
 77: 0x03B8 [0x01] GOTO 0x03BB

SUBROUTINE_03BB:
 78: 0x03BB [0x02] IF !(ExtData[1]->WorkLocal[9] <= 0*) GOTO 0x040F
 79: 0x03C3 [0x02] IF !(ExtData[1]->WorkLocal[12] <= 0*) GOTO 0x040F
 80: 0x03CB [0x93] DISPLAY_ITEM_INFO(item_id=ExtData[1]->WorkLocal[12])
 81: 0x03CE [0x48] [System] [7637*]:
    → "Obtain this item?"
 82: 0x03D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 83: 0x03D2 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 84: 0x03D5 [0x24] CREATE_DIALOG(message_id=7614*, default_option=1*, option_flags=0*)
    → "Obtain this temporary item? [Yes./No.]"
 85: 0x03DC [0x25] WAIT_DIALOG_SELECT()
 86: 0x03DD [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03ED
 87: 0x03E5 [0x03] ExtData[1]->WorkLocal[10] = 1*
 88: 0x03EA [0x01] GOTO 0x03FD
 89: 0x03ED [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03FD
 90: 0x03F5 [0x03] ExtData[1]->WorkLocal[10] = 2*
 91: 0x03FA [0x01] GOTO 0x03FD

SUBROUTINE_03FD:
 92: 0x03FD [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[9])
 93: 0x0406 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[10])
 94: 0x040F [0x42] SET_CLI_EVENT_CANCEL_DATA()
 95: 0x0410 [0x21] END_EVENT
 96: 0x0411 [0x00] END_REQSTACK()
```

### Event 1038

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0412    |
| Data Size    | 187 bytes |
| Instructions | 40        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0410:       03 09 00 02 80 03  0A 00 02 80 03 0B 00 02    ..............
0420: 80 03 0D 00 02 10 20 01  1C 00 80 48 13 80 23 24  ...... ....H..#$
0430: 14 80 02 80 02 80 25 02  00 10 02 80 00 47 04 03  ......%......G..
0440: 0A 00 02 80 01 CA 04 02  00 10 03 80 00 CA 04 03  ................
0450: 0A 00 03 80 03 02 10 0D  00 24 15 80 02 80 02 80  .........$......
0460: 25 02 00 10 02 80 00 71  04 03 09 00 02 80 01 AC  %......q........
0470: 04 02 00 10 03 80 00 9C  04 03 09 00 03 80 48 16  ..............H.
0480: 80 23 71 12 03 80 04 80  71 13 0B 00 02 0B 00 17  .#q.....q.......
0490: 80 03 99 04 03 0B 00 18  80 01 AC 04 02 00 10 04  ................
04A0: 80 00 AC 04 03 09 00 04  80 01 AC 04 40 02 80 09  ............@...
04B0: 80 01 10 09 00 40 0A 80  0E 80 01 10 0A 00 40 0F  .....@........@.
04C0: 80 10 80 01 10 0B 00 01  CA 04 42 21 00           ..........B!.   
```

#### Opcodes

```
  0: 0x0412 [0x03] ExtData[1]->WorkLocal[9] = 0*
  1: 0x0417 [0x03] ExtData[1]->WorkLocal[10] = 0*
  2: 0x041C [0x03] ExtData[1]->WorkLocal[11] = 0*
  3: 0x0421 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[2]
  4: 0x0426 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  5: 0x0428 [0x1C] WAIT(60* ticks)
  6: 0x042B [0x48] [System] [7619*]:
    → "The chest is locked."
  7: 0x042E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x042F [0x24] CREATE_DIALOG(message_id=7620*, default_option=0*, option_flags=0*)
    → "What will you do? [Leave it be./Attempt to unlock it.]"
  9: 0x0436 [0x25] WAIT_DIALOG_SELECT()
 10: 0x0437 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0447
 11: 0x043F [0x03] ExtData[1]->WorkLocal[10] = 0*
 12: 0x0444 [0x01] GOTO 0x04CA
 13: 0x0447 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x04CA
 14: 0x044F [0x03] ExtData[1]->WorkLocal[10] = 1*
 15: 0x0454 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[13]
 16: 0x0459 [0x24] CREATE_DIALOG(message_id=7621*, default_option=0*, option_flags=0*)
    → "What will you do? ($0 chances remaining.) [Give up./Enter a combination./Examine the lock.]"
 17: 0x0460 [0x25] WAIT_DIALOG_SELECT()
 18: 0x0461 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0471
 19: 0x0469 [0x03] ExtData[1]->WorkLocal[9] = 0*
 20: 0x046E [0x01] GOTO 0x04AC
 21: 0x0471 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x049C
 22: 0x0479 [0x03] ExtData[1]->WorkLocal[9] = 1*
 23: 0x047E [0x48] [System] [7622*]:
    → "It appears that you can enter a two-digit combination between 10 and 99."
 24: 0x0481 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0482 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
 26: 0x0488 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=ExtData[1]->WorkLocal[11])
 27: 0x048C [0x02] IF !(ExtData[1]->WorkLocal[11] >= 10*) GOTO 0x0499
 28: 0x0494 [0x03] ExtData[1]->WorkLocal[11] = 9999*
 29: 0x0499 [0x01] GOTO 0x04AC
 30: 0x049C [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x04AC
 31: 0x04A4 [0x03] ExtData[1]->WorkLocal[9] = 2*
 32: 0x04A9 [0x01] GOTO 0x04AC

SUBROUTINE_04AC:
 33: 0x04AC [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[9])
 34: 0x04B5 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[10])
 35: 0x04BE [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[11])
 36: 0x04C7 [0x01] GOTO 0x04CA

SUBROUTINE_04CA:
 37: 0x04CA [0x42] SET_CLI_EVENT_CANCEL_DATA()
 38: 0x04CB [0x21] END_EVENT
 39: 0x04CC [0x00] END_REQSTACK()
```

### Event 1060

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x04CD    |
| Data Size    | 443 bytes |
| Instructions | 85        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04C0:                                         20 01 1C                ..
04D0: 00 80 03 00 00 02 10 03  0E 00 03 10 03 01 00 04  ................
04E0: 10 03 0F 00 05 10 03 02  00 06 10 03 10 00 07 10  ................
04F0: 03 03 00 08 10 03 11 00  09 10 03 08 00 01 80 03  ................
0500: 09 00 02 80 03 0A 00 02  80 03 0B 00 02 80 03 0C  ................
0510: 00 02 80 3D 08 00 02 80  03 80 02 00 00 02 80 02  ...=............
0520: 31 05 3D 08 00 03 80 03  80 03 02 10 00 00 01 36  1.=............6
0530: 05 03 02 10 03 80 02 01  00 02 80 02 4D 05 3D 08  ............M.=.
0540: 00 04 80 03 80 03 03 10  01 00 01 52 05 03 03 10  ...........R....
0550: 03 80 02 02 00 02 80 02  69 05 3D 08 00 05 80 03  ........i.=.....
0560: 80 03 04 10 02 00 01 6E  05 03 04 10 03 80 02 03  .......n........
0570: 00 02 80 02 85 05 3D 08  00 06 80 03 80 03 05 10  ......=.........
0580: 03 00 01 8A 05 03 05 10  03 80 03 06 10 03 80 03  ................
0590: 07 10 03 80 03 08 10 03  80 03 09 10 03 80 24 0B  ..............$.
05A0: 80 02 80 08 00 25 02 00  10 02 80 00 BB 05 03 09  .....%..........
05B0: 00 02 80 03 0C 00 02 80  01 23 06 02 00 10 03 80  .........#......
05C0: 00 D5 05 03 0C 00 00 00  03 09 00 03 80 03 12 00  ................
05D0: 0E 00 01 23 06 02 00 10  04 80 00 EF 05 03 0C 00  ...#............
05E0: 01 00 03 09 00 04 80 03  12 00 0F 00 01 23 06 02  .............#..
05F0: 00 10 05 80 00 09 06 03  0C 00 02 00 03 09 00 05  ................
0600: 80 03 12 00 10 00 01 23  06 02 00 10 06 80 00 23  .......#.......#
0610: 06 03 0C 00 03 00 03 09  00 06 80 03 12 00 11 00  ................
0620: 01 23 06 02 09 00 02 80  02 85 06 02 0C 00 02 80  .#..............
0630: 02 85 06 CC 01 0C 00 12  00 02 80 02 80 48 0C 80  .............H..
0640: 23 CC 01 02 80 02 80 02  80 02 80 24 0D 80 03 80  #..........$....
0650: 02 80 25 02 00 10 02 80  00 63 06 03 0A 00 03 80  ..%......c......
0660: 01 73 06 02 00 10 03 80  00 73 06 03 0A 00 04 80  .s.......s......
0670: 01 73 06 40 02 80 0E 80  01 10 09 00 40 0F 80 10  .s.@........@...
0680: 80 01 10 0A 00 42 21 00                           .....B!.        
```

#### Opcodes

```
  0: 0x04CD [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x04CF [0x1C] WAIT(60* ticks)
  2: 0x04D2 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x04D7 [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[3]
  4: 0x04DC [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[4]
  5: 0x04E1 [0x03] ExtData[1]->WorkLocal[15] = Work_Zone[5]
  6: 0x04E6 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[6]
  7: 0x04EB [0x03] ExtData[1]->WorkLocal[16] = Work_Zone[7]
  8: 0x04F0 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[8]
  9: 0x04F5 [0x03] ExtData[1]->WorkLocal[17] = Work_Zone[9]
 10: 0x04FA [0x03] ExtData[1]->WorkLocal[8] = 4294967295*
 11: 0x04FF [0x03] ExtData[1]->WorkLocal[9] = 0*
 12: 0x0504 [0x03] ExtData[1]->WorkLocal[10] = 0*
 13: 0x0509 [0x03] ExtData[1]->WorkLocal[11] = 0*
 14: 0x050E [0x03] ExtData[1]->WorkLocal[12] = 0*
 15: 0x0513 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=0*, condition_work_offset=1*)
 16: 0x051A [0x02] IF !(ExtData[1]->WorkLocal[0] <= 0*) GOTO 0x0531
 17: 0x0522 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=1*, condition_work_offset=1*)
 18: 0x0529 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 19: 0x052E [0x01] GOTO 0x0536
 20: 0x0531 [0x03] Work_Zone[2] = 1*

SUBROUTINE_0536:
 21: 0x0536 [0x02] IF !(ExtData[1]->WorkLocal[1] <= 0*) GOTO 0x054D
 22: 0x053E [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=2*, condition_work_offset=1*)
 23: 0x0545 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
 24: 0x054A [0x01] GOTO 0x0552
 25: 0x054D [0x03] Work_Zone[3] = 1*

SUBROUTINE_0552:
 26: 0x0552 [0x02] IF !(ExtData[1]->WorkLocal[2] <= 0*) GOTO 0x0569
 27: 0x055A [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=3*, condition_work_offset=1*)
 28: 0x0561 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[2]
 29: 0x0566 [0x01] GOTO 0x056E
 30: 0x0569 [0x03] Work_Zone[4] = 1*

SUBROUTINE_056E:
 31: 0x056E [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x0585
 32: 0x0576 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[8], bit_index_work_offset=4*, condition_work_offset=1*)
 33: 0x057D [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[3]
 34: 0x0582 [0x01] GOTO 0x058A
 35: 0x0585 [0x03] Work_Zone[5] = 1*

SUBROUTINE_058A:
 36: 0x058A [0x03] Work_Zone[6] = 1*
 37: 0x058F [0x03] Work_Zone[7] = 1*
 38: 0x0594 [0x03] Work_Zone[8] = 1*
 39: 0x0599 [0x03] Work_Zone[9] = 1*
 40: 0x059E [0x24] CREATE_DIALOG(message_id=7611*, default_option=0*, option_flags=ExtData[1]->WorkLocal[8])
    → "Which item will you obtain? [None of them./$0./$1./$2./$3./$4./$5./$6./$7.]"
 41: 0x05A5 [0x25] WAIT_DIALOG_SELECT()
 42: 0x05A6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x05BB
 43: 0x05AE [0x03] ExtData[1]->WorkLocal[9] = 0*
 44: 0x05B3 [0x03] ExtData[1]->WorkLocal[12] = 0*
 45: 0x05B8 [0x01] GOTO 0x0623
 46: 0x05BB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x05D5
 47: 0x05C3 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[0]
 48: 0x05C8 [0x03] ExtData[1]->WorkLocal[9] = 1*
 49: 0x05CD [0x03] ExtData[1]->WorkLocal[18] = ExtData[1]->WorkLocal[14]
 50: 0x05D2 [0x01] GOTO 0x0623
 51: 0x05D5 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x05EF
 52: 0x05DD [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[1]
 53: 0x05E2 [0x03] ExtData[1]->WorkLocal[9] = 2*
 54: 0x05E7 [0x03] ExtData[1]->WorkLocal[18] = ExtData[1]->WorkLocal[15]
 55: 0x05EC [0x01] GOTO 0x0623
 56: 0x05EF [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0609
 57: 0x05F7 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[2]
 58: 0x05FC [0x03] ExtData[1]->WorkLocal[9] = 3*
 59: 0x0601 [0x03] ExtData[1]->WorkLocal[18] = ExtData[1]->WorkLocal[16]
 60: 0x0606 [0x01] GOTO 0x0623
 61: 0x0609 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0623
 62: 0x0611 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[3]
 63: 0x0616 [0x03] ExtData[1]->WorkLocal[9] = 4*
 64: 0x061B [0x03] ExtData[1]->WorkLocal[18] = ExtData[1]->WorkLocal[17]
 65: 0x0620 [0x01] GOTO 0x0623

SUBROUTINE_0623:
 66: 0x0623 [0x02] IF !(ExtData[1]->WorkLocal[9] <= 0*) GOTO 0x0685
 67: 0x062B [0x02] IF !(ExtData[1]->WorkLocal[12] <= 0*) GOTO 0x0685
 68: 0x0633 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=ExtData[1]->WorkLocal[12], buffer1=ExtData[1]->WorkLocal[18], buffer2=0*, buffer3=0*)
 69: 0x063D [0x48] [System] [7637*]:
    → "Obtain this item?"
 70: 0x0640 [0x23] WAIT_FOR_DIALOG_INTERACTION
 71: 0x0641 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=0*, buffer1=0*, buffer2=0*, buffer3=0*)
 72: 0x064B [0x24] CREATE_DIALOG(message_id=7613*, default_option=1*, option_flags=0*)
    → "Obtain this item? [Yes./No.]"
 73: 0x0652 [0x25] WAIT_DIALOG_SELECT()
 74: 0x0653 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0663
 75: 0x065B [0x03] ExtData[1]->WorkLocal[10] = 1*
 76: 0x0660 [0x01] GOTO 0x0673
 77: 0x0663 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0673
 78: 0x066B [0x03] ExtData[1]->WorkLocal[10] = 2*
 79: 0x0670 [0x01] GOTO 0x0673

SUBROUTINE_0673:
 80: 0x0673 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[9])
 81: 0x067C [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[10])
 82: 0x0685 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 83: 0x0686 [0x21] END_EVENT
 84: 0x0687 [0x00] END_REQSTACK()
```
