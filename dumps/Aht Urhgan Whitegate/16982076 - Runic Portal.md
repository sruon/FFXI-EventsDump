# 16982076 - Runic Portal

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 4152 bytes                    |
| Total Events     | 8                             |
| References Count | 33                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [101](#event-101)     | 0x0001       |   2008 |            250 |
| [120](#event-120)     | 0x07D9       |    309 |             39 |
| [121](#event-121)     | 0x090E       |    309 |             39 |
| [122](#event-122)     | 0x0A43       |    309 |             39 |
| [123](#event-123)     | 0x0B78       |    309 |             39 |
| [124](#event-124)     | 0x0CAD       |    309 |             39 |
| [125](#event-125)     | 0x0DE2       |    416 |             63 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x007E      |         126 |
|       2 | 0x0001      |           1 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |
|       6 | 0x0005      |           5 |
|       7 | 0x0006      |           6 |
|       8 | 0x1214      |        4628 |
|       9 | 0x030E      |         782 |
|      10 | 0x1200      |        4608 |
|      11 | 0x1201      |        4609 |
|      12 | 0x1213      |        4627 |
|      13 | 0x00C8      |         200 |
|      14 | 0x003C      |          60 |
|      15 | 0x0013      |          19 |
|      16 | 0x00D9      |         217 |
|      17 | 0x012C      |         300 |
|      18 | 0x00C9      |         201 |
|      19 | 0x0096      |         150 |
|      20 | 0x001E      |          30 |
|      21 | 0x1206      |        4614 |
|      22 | 0x120C      |        4620 |
|      23 | 0x1207      |        4615 |
|      24 | 0x1208      |        4616 |
|      25 | 0x1209      |        4617 |
|      26 | 0x120A      |        4618 |
|      27 | 0x120B      |        4619 |
|      28 | 0x0064      |         100 |
|      29 | 0x1202      |        4610 |
|      30 | 0x1203      |        4611 |
|      31 | 0x1204      |        4612 |
|      32 | 0x03E8      |        1000 |

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

### Event 101

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 2008 bytes |
| Instructions | 244        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 01 00 00 80  03 00 00 01 80 3E 03 10    ...........>..
0010: 02 80 1B 00 3D 00 00 02  80 02 80 3E 03 10 03 80  ....=......>....
0020: 29 00 3D 00 00 03 80 02  80 3E 03 10 04 80 37 00  ).=......>....7.
0030: 3D 00 00 04 80 02 80 3E  03 10 05 80 45 00 3D 00  =......>....E.=.
0040: 00 05 80 02 80 3E 03 10  06 80 53 00 3D 00 00 06  .....>....S.=...
0050: 80 02 80 3E 03 10 07 80  61 00 3D 00 00 07 80 02  ...>....a.=.....
0060: 80 02 00 00 01 80 00 6F  00 48 08 80 23 21 00 02  .......o.H..#!..
0070: 06 10 02 80 00 7A 00 01  C6 00 02 07 10 00 80 00  .....z..........
0080: 85 00 01 C6 00 02 08 10  02 80 00 C6 00 03 02 10  ................
0090: 09 80 48 0A 80 23 24 0B  80 00 80 00 80 25 02 00  ..H..#$......%..
00A0: 10 00 80 00 AB 00 21 00  01 C6 00 02 00 10 02 80  ......!.........
00B0: 00 B6 00 01 C6 00 02 00  10 03 80 00 C6 00 03 07  ................
00C0: 10 00 80 01 C6 00 24 0C  80 00 80 00 00 25 02 00  ......$......%..
00D0: 10 00 80 00 D9 00 01 D5  07 02 00 10 02 80 00 03  ................
00E0: 02 1A 17 0F 02 01 00 02  80 00 EE 00 21 00 42 46  ............!.BF
00F0: 01 07 01 00 02 80 03 01  10 01 00 45 0D 80 F0 FF  ...........E....
0100: FF 7F F0 FF FF 7F 66 64  6F 31 00 80 1C 0E 80 38  ......fdo1.....8
0110: 0F 80 29 01 F0 FF FF 7F  05 45 10 80 F0 FF FF 7F  ..)......E......
0120: F0 FF FF 7F 7A 35 30 61  00 80 2D F8 FF FF 7F F8  ....z50a..-.....
0130: FF FF 7F 31 70 62 32 45  0D 80 F0 FF FF 7F F0 FF  ...1pb2E........
0140: FF 7F 66 64 69 31 00 80  1C 11 80 29 10 F0 FF FF  ..fdi1.....)....
0150: 7F 06 29 10 F0 FF FF 7F  18 45 0D 80 F0 FF FF 7F  ..)......E......
0160: F0 FF FF 7F 62 6C 6F 6E  00 80 45 12 80 F0 FF FF  ....blon..E.....
0170: 7F F0 FF FF 7F 62 6C 6F  6E 00 80 45 0D 80 F0 FF  .....blon..E....
0180: FF 7F F0 FF FF 7F 6F 76  6C 31 00 80 45 10 80 F0  ......ovl1..E...
0190: FF FF 7F F0 FF FF 7F 7A  35 30 62 00 80 27 01 F0  .......z50b..'..
01A0: FF FF 7F 04 1C 13 80 45  12 80 F8 FF FF 7F F8 FF  .......E........
01B0: FF 7F 77 68 6F 31 00 80  55 12 80 F8 FF FF 7F F8  ..who1..U.......
01C0: FF FF 7F 77 68 6F 31 45  0D 80 F8 FF FF 7F F8 FF  ...who1E........
01D0: FF 7F 66 64 6F 30 00 80  1C 14 80 30 45 12 80 F8  ..fdo0.....0E...
01E0: FF FF 7F F8 FF FF 7F 77  68 69 31 00 80 45 0D 80  .......whi1..E..
01F0: F0 FF FF 7F F0 FF FF 7F  62 6C 6F 66 00 80 46 00  ........blof..F.
0200: 01 D5 07 02 00 10 03 80  00 2D 03 1A 17 0F 02 01  .........-......
0210: 00 02 80 00 18 02 21 00  42 46 01 07 01 00 03 80  ......!.BF......
0220: 03 01 10 01 00 45 0D 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0230: 66 64 6F 31 00 80 1C 0E  80 38 0F 80 29 01 F0 FF  fdo1.....8..)...
0240: FF 7F 05 45 10 80 F0 FF  FF 7F F0 FF FF 7F 7A 35  ...E..........z5
0250: 30 61 00 80 2D F8 FF FF  7F F8 FF FF 7F 31 70 62  0a..-........1pb
0260: 32 45 0D 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  2E..........fdi1
0270: 00 80 1C 11 80 29 10 F0  FF FF 7F 06 29 10 F0 FF  .....)......)...
0280: FF 7F 18 45 0D 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  ...E..........bl
0290: 6F 6E 00 80 45 12 80 F0  FF FF 7F F0 FF FF 7F 62  on..E..........b
02A0: 6C 6F 6E 00 80 45 0D 80  F0 FF FF 7F F0 FF FF 7F  lon..E..........
02B0: 6F 76 6C 31 00 80 45 10  80 F0 FF FF 7F F0 FF FF  ovl1..E.........
02C0: 7F 7A 35 30 62 00 80 27  01 F0 FF FF 7F 04 1C 13  .z50b..'........
02D0: 80 45 12 80 F8 FF FF 7F  F8 FF FF 7F 77 68 6F 31  .E..........who1
02E0: 00 80 55 12 80 F8 FF FF  7F F8 FF FF 7F 77 68 6F  ..U..........who
02F0: 31 45 0D 80 F8 FF FF 7F  F8 FF FF 7F 66 64 6F 30  1E..........fdo0
0300: 00 80 1C 14 80 30 45 12  80 F8 FF FF 7F F8 FF FF  .....0E.........
0310: 7F 77 68 69 31 00 80 45  0D 80 F0 FF FF 7F F0 FF  .whi1..E........
0320: FF 7F 62 6C 6F 66 00 80  46 00 01 D5 07 02 00 10  ..blof..F.......
0330: 04 80 00 57 04 1A 17 0F  02 01 00 02 80 00 42 03  ...W..........B.
0340: 21 00 42 46 01 07 01 00  04 80 03 01 10 01 00 45  !.BF...........E
0350: 0D 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 00 80  ..........fdo1..
0360: 1C 0E 80 38 0F 80 29 01  F0 FF FF 7F 05 45 10 80  ...8..)......E..
0370: F0 FF FF 7F F0 FF FF 7F  7A 35 30 61 00 80 2D F8  ........z50a..-.
0380: FF FF 7F F8 FF FF 7F 31  70 62 32 45 0D 80 F0 FF  .......1pb2E....
0390: FF 7F F0 FF FF 7F 66 64  69 31 00 80 1C 11 80 29  ......fdi1.....)
03A0: 10 F0 FF FF 7F 06 29 10  F0 FF FF 7F 18 45 0D 80  ......)......E..
03B0: F0 FF FF 7F F0 FF FF 7F  62 6C 6F 6E 00 80 45 12  ........blon..E.
03C0: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 00 80 45  .........blon..E
03D0: 0D 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 00 80  ..........ovl1..
03E0: 45 10 80 F0 FF FF 7F F0  FF FF 7F 7A 35 30 62 00  E..........z50b.
03F0: 80 27 01 F0 FF FF 7F 04  1C 13 80 45 12 80 F8 FF  .'.........E....
0400: FF 7F F8 FF FF 7F 77 68  6F 31 00 80 55 12 80 F8  ......who1..U...
0410: FF FF 7F F8 FF FF 7F 77  68 6F 31 45 0D 80 F8 FF  .......who1E....
0420: FF 7F F8 FF FF 7F 66 64  6F 30 00 80 1C 14 80 30  ......fdo0.....0
0430: 45 12 80 F8 FF FF 7F F8  FF FF 7F 77 68 69 31 00  E..........whi1.
0440: 80 45 0D 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 66  .E..........blof
0450: 00 80 46 00 01 D5 07 02  00 10 05 80 00 81 05 1A  ..F.............
0460: 17 0F 02 01 00 02 80 00  6C 04 21 00 42 46 01 07  ........l.!.BF..
0470: 01 00 05 80 03 01 10 01  00 45 0D 80 F0 FF FF 7F  .........E......
0480: F0 FF FF 7F 66 64 6F 31  00 80 1C 0E 80 38 0F 80  ....fdo1.....8..
0490: 29 01 F0 FF FF 7F 05 45  10 80 F0 FF FF 7F F0 FF  )......E........
04A0: FF 7F 7A 35 30 61 00 80  2D F8 FF FF 7F F8 FF FF  ..z50a..-.......
04B0: 7F 31 70 62 32 45 0D 80  F0 FF FF 7F F0 FF FF 7F  .1pb2E..........
04C0: 66 64 69 31 00 80 1C 11  80 29 10 F0 FF FF 7F 06  fdi1.....)......
04D0: 29 10 F0 FF FF 7F 18 45  0D 80 F0 FF FF 7F F0 FF  )......E........
04E0: FF 7F 62 6C 6F 6E 00 80  45 12 80 F0 FF FF 7F F0  ..blon..E.......
04F0: FF FF 7F 62 6C 6F 6E 00  80 45 0D 80 F0 FF FF 7F  ...blon..E......
0500: F0 FF FF 7F 6F 76 6C 31  00 80 45 10 80 F0 FF FF  ....ovl1..E.....
0510: 7F F0 FF FF 7F 7A 35 30  62 00 80 27 01 F0 FF FF  .....z50b..'....
0520: 7F 04 1C 13 80 45 12 80  F8 FF FF 7F F8 FF FF 7F  .....E..........
0530: 77 68 6F 31 00 80 55 12  80 F8 FF FF 7F F8 FF FF  who1..U.........
0540: 7F 77 68 6F 31 45 0D 80  F8 FF FF 7F F8 FF FF 7F  .who1E..........
0550: 66 64 6F 30 00 80 1C 14  80 30 45 12 80 F8 FF FF  fdo0.....0E.....
0560: 7F F8 FF FF 7F 77 68 69  31 00 80 45 0D 80 F0 FF  .....whi1..E....
0570: FF 7F F0 FF FF 7F 62 6C  6F 66 00 80 46 00 01 D5  ......blof..F...
0580: 07 02 00 10 06 80 00 AB  06 1A 17 0F 02 01 00 02  ................
0590: 80 00 96 05 21 00 42 46  01 07 01 00 06 80 03 01  ....!.BF........
05A0: 10 01 00 45 0D 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
05B0: 6F 31 00 80 1C 0E 80 38  0F 80 29 01 F0 FF FF 7F  o1.....8..).....
05C0: 05 45 10 80 F0 FF FF 7F  F0 FF FF 7F 7A 35 30 61  .E..........z50a
05D0: 00 80 2D F8 FF FF 7F F8  FF FF 7F 31 70 62 32 45  ..-........1pb2E
05E0: 0D 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 00 80  ..........fdi1..
05F0: 1C 11 80 29 10 F0 FF FF  7F 06 29 10 F0 FF FF 7F  ...)......).....
0600: 18 45 0D 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
0610: 00 80 45 12 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
0620: 6E 00 80 45 0D 80 F0 FF  FF 7F F0 FF FF 7F 6F 76  n..E..........ov
0630: 6C 31 00 80 45 10 80 F0  FF FF 7F F0 FF FF 7F 7A  l1..E..........z
0640: 35 30 62 00 80 27 01 F0  FF FF 7F 04 1C 13 80 45  50b..'.........E
0650: 12 80 F8 FF FF 7F F8 FF  FF 7F 77 68 6F 31 00 80  ..........who1..
0660: 55 12 80 F8 FF FF 7F F8  FF FF 7F 77 68 6F 31 45  U..........who1E
0670: 0D 80 F8 FF FF 7F F8 FF  FF 7F 66 64 6F 30 00 80  ..........fdo0..
0680: 1C 14 80 30 45 12 80 F8  FF FF 7F F8 FF FF 7F 77  ...0E..........w
0690: 68 69 31 00 80 45 0D 80  F0 FF FF 7F F0 FF FF 7F  hi1..E..........
06A0: 62 6C 6F 66 00 80 46 00  01 D5 07 02 00 10 07 80  blof..F.........
06B0: 00 D5 07 1A 17 0F 02 01  00 02 80 00 C0 06 21 00  ..............!.
06C0: 42 46 01 07 01 00 07 80  03 01 10 01 00 45 0D 80  BF...........E..
06D0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 00 80 1C 0E  ........fdo1....
06E0: 80 38 0F 80 29 01 F0 FF  FF 7F 05 45 10 80 F0 FF  .8..)......E....
06F0: FF 7F F0 FF FF 7F 7A 35  30 61 00 80 2D F8 FF FF  ......z50a..-...
0700: 7F F8 FF FF 7F 31 70 62  32 45 0D 80 F0 FF FF 7F  .....1pb2E......
0710: F0 FF FF 7F 66 64 69 31  00 80 1C 11 80 29 10 F0  ....fdi1.....)..
0720: FF FF 7F 06 29 10 F0 FF  FF 7F 18 45 0D 80 F0 FF  ....)......E....
0730: FF 7F F0 FF FF 7F 62 6C  6F 6E 00 80 45 12 80 F0  ......blon..E...
0740: FF FF 7F F0 FF FF 7F 62  6C 6F 6E 00 80 45 0D 80  .......blon..E..
0750: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 00 80 45 10  ........ovl1..E.
0760: 80 F0 FF FF 7F F0 FF FF  7F 7A 35 30 62 00 80 27  .........z50b..'
0770: 01 F0 FF FF 7F 04 1C 13  80 45 12 80 F8 FF FF 7F  .........E......
0780: F8 FF FF 7F 77 68 6F 31  00 80 55 12 80 F8 FF FF  ....who1..U.....
0790: 7F F8 FF FF 7F 77 68 6F  31 45 0D 80 F8 FF FF 7F  .....who1E......
07A0: F8 FF FF 7F 66 64 6F 30  00 80 1C 14 80 30 45 12  ....fdo0.....0E.
07B0: 80 F8 FF FF 7F F8 FF FF  7F 77 68 69 31 00 80 45  .........whi1..E
07C0: 0D 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 66 00 80  ..........blof..
07D0: 46 00 01 D5 07 20 00 21  00                       F.... .!.       
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[1] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[0] = 126*
  3: 0x000D [0x3E] IF !(Work_Zone[3] bit 1*) GOTO 0x001B
  4: 0x0014 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=1*, condition_work_offset=1*)
  5: 0x001B [0x3E] IF !(Work_Zone[3] bit 2*) GOTO 0x0029
  6: 0x0022 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=2*, condition_work_offset=1*)
  7: 0x0029 [0x3E] IF !(Work_Zone[3] bit 3*) GOTO 0x0037
  8: 0x0030 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=3*, condition_work_offset=1*)
  9: 0x0037 [0x3E] IF !(Work_Zone[3] bit 4*) GOTO 0x0045
 10: 0x003E [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=4*, condition_work_offset=1*)
 11: 0x0045 [0x3E] IF !(Work_Zone[3] bit 5*) GOTO 0x0053
 12: 0x004C [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=5*, condition_work_offset=1*)
 13: 0x0053 [0x3E] IF !(Work_Zone[3] bit 6*) GOTO 0x0061
 14: 0x005A [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=6*, condition_work_offset=1*)
 15: 0x0061 [0x02] IF !(ExtData[1]->WorkLocal[0] == 126*) GOTO 0x006F
 16: 0x0069 [0x48] [System] [4628*]:
    → "You must use the runic portal at each staging point in order to open the route to the Chamber of Passage.\u007F1\u0000\u0007"
 17: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x006D [0x21] END_EVENT
 19: 0x006E [0x00] END_REQSTACK()
 20: 0x006F [0x02] IF !(Work_Zone[6] == 1*) GOTO 0x007A
 21: 0x0077 [0x01] GOTO 0x00C6
 22: 0x007A [0x02] IF !(Work_Zone[7] == 0*) GOTO 0x0085
 23: 0x0082 [0x01] GOTO 0x00C6
 24: 0x0085 [0x02] IF !(Work_Zone[8] == 1*) GOTO 0x00C6
 25: 0x008D [0x03] Work_Zone[2] = 782*
 26: 0x0092 [0x48] [System] [4608*]:
    → "You may access the portal using \u0001\u00056\u0002\u0000\u0000\u0000 or Imperial Standing credits.\u007F1\u0000\u0007"
 27: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0096 [0x24] CREATE_DIALOG(message_id=4609*, default_option=0*, option_flags=0*)
    → "Which will it be?\u0007\u000BUse neither.\u0007Use Imperial Standing.\u0007Use \u0001\u00056\u0002\u0000\u0000\u0000.\u007F1\u0000\u0007"
 29: 0x009D [0x25] WAIT_DIALOG_SELECT()
 30: 0x009E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00AB
 31: 0x00A6 [0x21] END_EVENT
 32: 0x00A7 [0x00] END_REQSTACK()

SUBROUTINE_00C6:
 33: 0x00C6 [0x24] CREATE_DIALOG(message_id=4627*, default_option=0*, option_flags=ExtData[1]->WorkLocal[0])
    → "Choose your destination.\u0007\u000BI've changed my mind.\u0007Azouph Isle (Leujaoam Sanctum).\u0007Dvucca Isle (Periqia).\u0007Mamool Ja staging point.\u0007Halvung (Lebros Caverns).\u0007Ilrusi Atoll staging point.\u0007Nyzul Isle staging point.\u007F1\u0000\u0007"
 34: 0x00CD [0x25] WAIT_DIALOG_SELECT()
 35: 0x00CE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00D9
 36: 0x00D6 [0x01] GOTO 0x07D5
 37: 0x00D9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0203
 38: 0x00E1 [0x1A] CALL_SUBROUTINE(address=0x0F17)
 39: 0x00E4 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x00EE
 40: 0x00EC [0x21] END_EVENT
 41: 0x00ED [0x00] END_REQSTACK()
 42: 0x00EE [0x42] SET_CLI_EVENT_CANCEL_DATA()
 43: 0x00EF [0x46] CAMERA_CONTROL: Disable user control
 44: 0x00F1 [0x07] ExtData[1]->WorkLocal[1] += 1*
 45: 0x00F6 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[1]
 46: 0x00FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 47: 0x010C [0x1C] WAIT(60* ticks)
 48: 0x010F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 49: 0x0112 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 50: 0x0119 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 51: 0x012A [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 52: 0x0137 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 53: 0x0148 [0x1C] WAIT(300* ticks)
 54: 0x014B [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 55: 0x0152 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
 56: 0x0159 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x016A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 58: 0x017B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 59: 0x018C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 60: 0x019D [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 61: 0x01A4 [0x1C] WAIT(150* ticks)
 62: 0x01A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 63: 0x01B8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 64: 0x01C7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 65: 0x01D8 [0x1C] WAIT(30* ticks)
 66: 0x01DB [0x30] SET_UCOFF_CONTINUE_ZERO()
 67: 0x01DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 68: 0x01ED [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 69: 0x01FE [0x46] CAMERA_CONTROL: Restore default settings
 70: 0x0200 [0x01] GOTO 0x07D5
 71: 0x0203 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x032D
 72: 0x020B [0x1A] CALL_SUBROUTINE(address=0x0F17)
 73: 0x020E [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0218
 74: 0x0216 [0x21] END_EVENT
 75: 0x0217 [0x00] END_REQSTACK()
 76: 0x0218 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 77: 0x0219 [0x46] CAMERA_CONTROL: Disable user control
 78: 0x021B [0x07] ExtData[1]->WorkLocal[1] += 2*
 79: 0x0220 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[1]
 80: 0x0225 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 81: 0x0236 [0x1C] WAIT(60* ticks)
 82: 0x0239 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 83: 0x023C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 84: 0x0243 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 85: 0x0254 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 86: 0x0261 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 87: 0x0272 [0x1C] WAIT(300* ticks)
 88: 0x0275 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 89: 0x027C [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
 90: 0x0283 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 91: 0x0294 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 92: 0x02A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 93: 0x02B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 94: 0x02C7 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 95: 0x02CE [0x1C] WAIT(150* ticks)
 96: 0x02D1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 97: 0x02E2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 98: 0x02F1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 99: 0x0302 [0x1C] WAIT(30* ticks)
100: 0x0305 [0x30] SET_UCOFF_CONTINUE_ZERO()
101: 0x0306 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
102: 0x0317 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
103: 0x0328 [0x46] CAMERA_CONTROL: Restore default settings
104: 0x032A [0x01] GOTO 0x07D5
105: 0x032D [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0457
106: 0x0335 [0x1A] CALL_SUBROUTINE(address=0x0F17)
107: 0x0338 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0342
108: 0x0340 [0x21] END_EVENT
109: 0x0341 [0x00] END_REQSTACK()
110: 0x0342 [0x42] SET_CLI_EVENT_CANCEL_DATA()
111: 0x0343 [0x46] CAMERA_CONTROL: Disable user control
112: 0x0345 [0x07] ExtData[1]->WorkLocal[1] += 3*
113: 0x034A [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[1]
114: 0x034F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
115: 0x0360 [0x1C] WAIT(60* ticks)
116: 0x0363 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
117: 0x0366 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
118: 0x036D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
119: 0x037E [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
120: 0x038B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
121: 0x039C [0x1C] WAIT(300* ticks)
122: 0x039F [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
123: 0x03A6 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
124: 0x03AD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
125: 0x03BE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
126: 0x03CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
127: 0x03E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
128: 0x03F1 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
129: 0x03F8 [0x1C] WAIT(150* ticks)
130: 0x03FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
131: 0x040C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
132: 0x041B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
133: 0x042C [0x1C] WAIT(30* ticks)
134: 0x042F [0x30] SET_UCOFF_CONTINUE_ZERO()
135: 0x0430 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
136: 0x0441 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
137: 0x0452 [0x46] CAMERA_CONTROL: Restore default settings
138: 0x0454 [0x01] GOTO 0x07D5
139: 0x0457 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0581
140: 0x045F [0x1A] CALL_SUBROUTINE(address=0x0F17)
141: 0x0462 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x046C
142: 0x046A [0x21] END_EVENT
143: 0x046B [0x00] END_REQSTACK()
144: 0x046C [0x42] SET_CLI_EVENT_CANCEL_DATA()
145: 0x046D [0x46] CAMERA_CONTROL: Disable user control
146: 0x046F [0x07] ExtData[1]->WorkLocal[1] += 4*
147: 0x0474 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[1]
148: 0x0479 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
149: 0x048A [0x1C] WAIT(60* ticks)
150: 0x048D [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
151: 0x0490 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
152: 0x0497 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
153: 0x04A8 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
154: 0x04B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
155: 0x04C6 [0x1C] WAIT(300* ticks)
156: 0x04C9 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
157: 0x04D0 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
158: 0x04D7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
159: 0x04E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
160: 0x04F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
161: 0x050A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
162: 0x051B [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
163: 0x0522 [0x1C] WAIT(150* ticks)
164: 0x0525 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
165: 0x0536 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
166: 0x0545 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
167: 0x0556 [0x1C] WAIT(30* ticks)
168: 0x0559 [0x30] SET_UCOFF_CONTINUE_ZERO()
169: 0x055A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
170: 0x056B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
171: 0x057C [0x46] CAMERA_CONTROL: Restore default settings
172: 0x057E [0x01] GOTO 0x07D5
173: 0x0581 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x06AB
174: 0x0589 [0x1A] CALL_SUBROUTINE(address=0x0F17)
175: 0x058C [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0596
176: 0x0594 [0x21] END_EVENT
177: 0x0595 [0x00] END_REQSTACK()
178: 0x0596 [0x42] SET_CLI_EVENT_CANCEL_DATA()
179: 0x0597 [0x46] CAMERA_CONTROL: Disable user control
180: 0x0599 [0x07] ExtData[1]->WorkLocal[1] += 5*
181: 0x059E [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[1]
182: 0x05A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
183: 0x05B4 [0x1C] WAIT(60* ticks)
184: 0x05B7 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
185: 0x05BA [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
186: 0x05C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
187: 0x05D2 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
188: 0x05DF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
189: 0x05F0 [0x1C] WAIT(300* ticks)
190: 0x05F3 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
191: 0x05FA [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
192: 0x0601 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
193: 0x0612 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
194: 0x0623 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
195: 0x0634 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
196: 0x0645 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
197: 0x064C [0x1C] WAIT(150* ticks)
198: 0x064F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
199: 0x0660 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
200: 0x066F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
201: 0x0680 [0x1C] WAIT(30* ticks)
202: 0x0683 [0x30] SET_UCOFF_CONTINUE_ZERO()
203: 0x0684 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
204: 0x0695 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
205: 0x06A6 [0x46] CAMERA_CONTROL: Restore default settings
206: 0x06A8 [0x01] GOTO 0x07D5
207: 0x06AB [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x07D5
208: 0x06B3 [0x1A] CALL_SUBROUTINE(address=0x0F17)
209: 0x06B6 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x06C0
210: 0x06BE [0x21] END_EVENT
211: 0x06BF [0x00] END_REQSTACK()
212: 0x06C0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
213: 0x06C1 [0x46] CAMERA_CONTROL: Disable user control
214: 0x06C3 [0x07] ExtData[1]->WorkLocal[1] += 6*
215: 0x06C8 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[1]
216: 0x06CD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
217: 0x06DE [0x1C] WAIT(60* ticks)
218: 0x06E1 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
219: 0x06E4 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
220: 0x06EB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
221: 0x06FC [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
222: 0x0709 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
223: 0x071A [0x1C] WAIT(300* ticks)
224: 0x071D [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
225: 0x0724 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
226: 0x072B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
227: 0x073C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
228: 0x074D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
229: 0x075E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
230: 0x076F [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
231: 0x0776 [0x1C] WAIT(150* ticks)
232: 0x0779 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
233: 0x078A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
234: 0x0799 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
235: 0x07AA [0x1C] WAIT(30* ticks)
236: 0x07AD [0x30] SET_UCOFF_CONTINUE_ZERO()
237: 0x07AE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
238: 0x07BF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
239: 0x07D0 [0x46] CAMERA_CONTROL: Restore default settings
240: 0x07D2 [0x01] GOTO 0x07D5

SUBROUTINE_07D5:
241: 0x07D5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
242: 0x07D7 [0x21] END_EVENT
243: 0x07D8 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00A8 [0x01] GOTO 0x00C6
```

### Event 120

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x07D9    |
| Data Size    | 309 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
07D0:                             20 01 48 15 80 23 24            .H..#$
07E0: 16 80 02 80 00 80 25 02  00 10 00 80 00 FF 08 42  ......%........B
07F0: 46 01 03 01 10 02 80 45  0D 80 F0 FF FF 7F F0 FF  F......E........
0800: FF 7F 66 64 6F 31 00 80  1C 0E 80 38 0F 80 29 01  ..fdo1.....8..).
0810: F0 FF FF 7F 05 45 10 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0820: 7A 35 30 61 00 80 2D F8  FF FF 7F F8 FF FF 7F 31  z50a..-........1
0830: 70 62 32 45 0D 80 F0 FF  FF 7F F0 FF FF 7F 66 64  pb2E..........fd
0840: 69 31 00 80 1C 11 80 29  10 F0 FF FF 7F 06 29 10  i1.....)......).
0850: F0 FF FF 7F 18 45 0D 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0860: 62 6C 6F 6E 00 80 45 12  80 F0 FF FF 7F F0 FF FF  blon..E.........
0870: 7F 62 6C 6F 6E 00 80 45  0D 80 F0 FF FF 7F F0 FF  .blon..E........
0880: FF 7F 6F 76 6C 31 00 80  45 10 80 F0 FF FF 7F F0  ..ovl1..E.......
0890: FF FF 7F 7A 35 30 62 00  80 27 01 F0 FF FF 7F 04  ...z50b..'......
08A0: 1C 13 80 45 12 80 F8 FF  FF 7F F8 FF FF 7F 77 68  ...E..........wh
08B0: 6F 31 00 80 55 12 80 F8  FF FF 7F F8 FF FF 7F 77  o1..U..........w
08C0: 68 6F 31 45 0D 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ho1E..........fd
08D0: 6F 30 00 80 1C 14 80 30  45 12 80 F8 FF FF 7F F8  o0.....0E.......
08E0: FF FF 7F 77 68 69 31 00  80 45 0D 80 F0 FF FF 7F  ...whi1..E......
08F0: F0 FF FF 7F 62 6C 6F 66  00 80 46 00 01 0A 09 02  ....blof..F.....
0900: 00 10 02 80 00 0A 09 01  0A 09 20 00 21 00        .......... .!.  
```

#### Opcodes

```
  0: 0x07D9 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x07DB [0x48] [System] [4614*]:
    → "You will now be transported to the staging point on Azouph Isle for participation in Assault (Leujaoam Sanctum).\u007F1\u0000\u0007"
  2: 0x07DE [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x07DF [0x24] CREATE_DIALOG(message_id=4620*, default_option=1*, option_flags=0*)
    → "Are you ready?\u0007\u000BYes.\u0007Not yet.\u007F1\u0000\u0007"
  4: 0x07E6 [0x25] WAIT_DIALOG_SELECT()
  5: 0x07E7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x08FF
  6: 0x07EF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x07F0 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x07F2 [0x03] Work_Zone[1] = 1*
  9: 0x07F7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0808 [0x1C] WAIT(60* ticks)
 11: 0x080B [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x080E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0815 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 14: 0x0826 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 15: 0x0833 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0844 [0x1C] WAIT(300* ticks)
 17: 0x0847 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 18: 0x084E [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
 19: 0x0855 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0866 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0877 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0888 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 23: 0x0899 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 24: 0x08A0 [0x1C] WAIT(150* ticks)
 25: 0x08A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 26: 0x08B4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 27: 0x08C3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x08D4 [0x1C] WAIT(30* ticks)
 29: 0x08D7 [0x30] SET_UCOFF_CONTINUE_ZERO()
 30: 0x08D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 31: 0x08E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x08FA [0x46] CAMERA_CONTROL: Restore default settings
 33: 0x08FC [0x01] GOTO 0x090A
 34: 0x08FF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x090A
 35: 0x0907 [0x01] GOTO 0x090A

SUBROUTINE_090A:
 36: 0x090A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 37: 0x090C [0x21] END_EVENT
 38: 0x090D [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x090E    |
| Data Size    | 309 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0900:                                            20 01                 .
0910: 48 17 80 23 24 16 80 02  80 00 80 25 02 00 10 00  H..#$......%....
0920: 80 00 34 0A 42 46 01 03  01 10 02 80 45 0D 80 F0  ..4.BF......E...
0930: FF FF 7F F0 FF FF 7F 66  64 6F 31 00 80 1C 0E 80  .......fdo1.....
0940: 38 0F 80 29 01 F0 FF FF  7F 05 45 10 80 F0 FF FF  8..)......E.....
0950: 7F F0 FF FF 7F 7A 35 30  61 00 80 2D F8 FF FF 7F  .....z50a..-....
0960: F8 FF FF 7F 31 70 62 32  45 0D 80 F0 FF FF 7F F0  ....1pb2E.......
0970: FF FF 7F 66 64 69 31 00  80 1C 11 80 29 10 F0 FF  ...fdi1.....)...
0980: FF 7F 06 29 10 F0 FF FF  7F 18 45 0D 80 F0 FF FF  ...)......E.....
0990: 7F F0 FF FF 7F 62 6C 6F  6E 00 80 45 12 80 F0 FF  .....blon..E....
09A0: FF 7F F0 FF FF 7F 62 6C  6F 6E 00 80 45 0D 80 F0  ......blon..E...
09B0: FF FF 7F F0 FF FF 7F 6F  76 6C 31 00 80 45 10 80  .......ovl1..E..
09C0: F0 FF FF 7F F0 FF FF 7F  7A 35 30 62 00 80 27 01  ........z50b..'.
09D0: F0 FF FF 7F 04 1C 13 80  45 12 80 F8 FF FF 7F F8  ........E.......
09E0: FF FF 7F 77 68 6F 31 00  80 55 12 80 F8 FF FF 7F  ...who1..U......
09F0: F8 FF FF 7F 77 68 6F 31  45 0D 80 F8 FF FF 7F F8  ....who1E.......
0A00: FF FF 7F 66 64 6F 30 00  80 1C 14 80 30 45 12 80  ...fdo0.....0E..
0A10: F8 FF FF 7F F8 FF FF 7F  77 68 69 31 00 80 45 0D  ........whi1..E.
0A20: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 66 00 80 46  .........blof..F
0A30: 00 01 3F 0A 02 00 10 02  80 00 3F 0A 01 3F 0A 20  ..?.......?..?. 
0A40: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x090E [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0910 [0x48] [System] [4615*]:
    → "You will now be transported to the Mamool Ja staging point for participation in Assault (Mamool Ja Training Grounds).\u007F1\u0000\u0007"
  2: 0x0913 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0914 [0x24] CREATE_DIALOG(message_id=4620*, default_option=1*, option_flags=0*)
    → "Are you ready?\u0007\u000BYes.\u0007Not yet.\u007F1\u0000\u0007"
  4: 0x091B [0x25] WAIT_DIALOG_SELECT()
  5: 0x091C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0A34
  6: 0x0924 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0925 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0927 [0x03] Work_Zone[1] = 1*
  9: 0x092C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x093D [0x1C] WAIT(60* ticks)
 11: 0x0940 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0943 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x094A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 14: 0x095B [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 15: 0x0968 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0979 [0x1C] WAIT(300* ticks)
 17: 0x097C [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 18: 0x0983 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
 19: 0x098A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x099B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x09AC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x09BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 23: 0x09CE [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 24: 0x09D5 [0x1C] WAIT(150* ticks)
 25: 0x09D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 26: 0x09E9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 27: 0x09F8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x0A09 [0x1C] WAIT(30* ticks)
 29: 0x0A0C [0x30] SET_UCOFF_CONTINUE_ZERO()
 30: 0x0A0D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 31: 0x0A1E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x0A2F [0x46] CAMERA_CONTROL: Restore default settings
 33: 0x0A31 [0x01] GOTO 0x0A3F
 34: 0x0A34 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0A3F
 35: 0x0A3C [0x01] GOTO 0x0A3F

SUBROUTINE_0A3F:
 36: 0x0A3F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 37: 0x0A41 [0x21] END_EVENT
 38: 0x0A42 [0x00] END_REQSTACK()
```

### Event 122

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0A43    |
| Data Size    | 309 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0A40:          20 01 48 18 80  23 24 16 80 02 80 00 80      .H..#$......
0A50: 25 02 00 10 00 80 00 69  0B 42 46 01 03 01 10 02  %......i.BF.....
0A60: 80 45 0D 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0A70: 00 80 1C 0E 80 38 0F 80  29 01 F0 FF FF 7F 05 45  .....8..)......E
0A80: 10 80 F0 FF FF 7F F0 FF  FF 7F 7A 35 30 61 00 80  ..........z50a..
0A90: 2D F8 FF FF 7F F8 FF FF  7F 31 70 62 32 45 0D 80  -........1pb2E..
0AA0: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 00 80 1C 11  ........fdi1....
0AB0: 80 29 10 F0 FF FF 7F 06  29 10 F0 FF FF 7F 18 45  .)......)......E
0AC0: 0D 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 00 80  ..........blon..
0AD0: 45 12 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 00  E..........blon.
0AE0: 80 45 0D 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  .E..........ovl1
0AF0: 00 80 45 10 80 F0 FF FF  7F F0 FF FF 7F 7A 35 30  ..E..........z50
0B00: 62 00 80 27 01 F0 FF FF  7F 04 1C 13 80 45 12 80  b..'.........E..
0B10: F8 FF FF 7F F8 FF FF 7F  77 68 6F 31 00 80 55 12  ........who1..U.
0B20: 80 F8 FF FF 7F F8 FF FF  7F 77 68 6F 31 45 0D 80  .........who1E..
0B30: F8 FF FF 7F F8 FF FF 7F  66 64 6F 30 00 80 1C 14  ........fdo0....
0B40: 80 30 45 12 80 F8 FF FF  7F F8 FF FF 7F 77 68 69  .0E..........whi
0B50: 31 00 80 45 0D 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  1..E..........bl
0B60: 6F 66 00 80 46 00 01 74  0B 02 00 10 02 80 00 74  of..F..t.......t
0B70: 0B 01 74 0B 20 00 21 00                           ..t. .!.        
```

#### Opcodes

```
  0: 0x0A43 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0A45 [0x48] [System] [4616*]:
    → "You will now be transported to the staging point in Halvung for participation in Assault (Lebros Caverns).\u007F1\u0000\u0007"
  2: 0x0A48 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0A49 [0x24] CREATE_DIALOG(message_id=4620*, default_option=1*, option_flags=0*)
    → "Are you ready?\u0007\u000BYes.\u0007Not yet.\u007F1\u0000\u0007"
  4: 0x0A50 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0A51 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0B69
  6: 0x0A59 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0A5A [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0A5C [0x03] Work_Zone[1] = 1*
  9: 0x0A61 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0A72 [0x1C] WAIT(60* ticks)
 11: 0x0A75 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0A78 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0A7F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 14: 0x0A90 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 15: 0x0A9D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0AAE [0x1C] WAIT(300* ticks)
 17: 0x0AB1 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 18: 0x0AB8 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
 19: 0x0ABF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0AD0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0AE1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0AF2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 23: 0x0B03 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 24: 0x0B0A [0x1C] WAIT(150* ticks)
 25: 0x0B0D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 26: 0x0B1E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 27: 0x0B2D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x0B3E [0x1C] WAIT(30* ticks)
 29: 0x0B41 [0x30] SET_UCOFF_CONTINUE_ZERO()
 30: 0x0B42 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 31: 0x0B53 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x0B64 [0x46] CAMERA_CONTROL: Restore default settings
 33: 0x0B66 [0x01] GOTO 0x0B74
 34: 0x0B69 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0B74
 35: 0x0B71 [0x01] GOTO 0x0B74

SUBROUTINE_0B74:
 36: 0x0B74 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 37: 0x0B76 [0x21] END_EVENT
 38: 0x0B77 [0x00] END_REQSTACK()
```

### Event 123

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0B78    |
| Data Size    | 309 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0B70:                          20 01 48 19 80 23 24 16           .H..#$.
0B80: 80 02 80 00 80 25 02 00  10 00 80 00 9E 0C 42 46  .....%........BF
0B90: 01 03 01 10 02 80 45 0D  80 F0 FF FF 7F F0 FF FF  ......E.........
0BA0: 7F 66 64 6F 31 00 80 1C  0E 80 38 0F 80 29 01 F0  .fdo1.....8..)..
0BB0: FF FF 7F 05 45 10 80 F0  FF FF 7F F0 FF FF 7F 7A  ....E..........z
0BC0: 35 30 61 00 80 2D F8 FF  FF 7F F8 FF FF 7F 31 70  50a..-........1p
0BD0: 62 32 45 0D 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  b2E..........fdi
0BE0: 31 00 80 1C 11 80 29 10  F0 FF FF 7F 06 29 10 F0  1.....)......)..
0BF0: FF FF 7F 18 45 0D 80 F0  FF FF 7F F0 FF FF 7F 62  ....E..........b
0C00: 6C 6F 6E 00 80 45 12 80  F0 FF FF 7F F0 FF FF 7F  lon..E..........
0C10: 62 6C 6F 6E 00 80 45 0D  80 F0 FF FF 7F F0 FF FF  blon..E.........
0C20: 7F 6F 76 6C 31 00 80 45  10 80 F0 FF FF 7F F0 FF  .ovl1..E........
0C30: FF 7F 7A 35 30 62 00 80  27 01 F0 FF FF 7F 04 1C  ..z50b..'.......
0C40: 13 80 45 12 80 F8 FF FF  7F F8 FF FF 7F 77 68 6F  ..E..........who
0C50: 31 00 80 55 12 80 F8 FF  FF 7F F8 FF FF 7F 77 68  1..U..........wh
0C60: 6F 31 45 0D 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  o1E..........fdo
0C70: 30 00 80 1C 14 80 30 45  12 80 F8 FF FF 7F F8 FF  0.....0E........
0C80: FF 7F 77 68 69 31 00 80  45 0D 80 F0 FF FF 7F F0  ..whi1..E.......
0C90: FF FF 7F 62 6C 6F 66 00  80 46 00 01 A9 0C 02 00  ...blof..F......
0CA0: 10 02 80 00 A9 0C 01 A9  0C 20 00 21 00           ......... .!.   
```

#### Opcodes

```
  0: 0x0B78 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0B7A [0x48] [System] [4617*]:
    → "You will now be transported to the staging point on Dvucca Isle for participation in Assault (Periqia).\u007F1\u0000\u0007"
  2: 0x0B7D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0B7E [0x24] CREATE_DIALOG(message_id=4620*, default_option=1*, option_flags=0*)
    → "Are you ready?\u0007\u000BYes.\u0007Not yet.\u007F1\u0000\u0007"
  4: 0x0B85 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0B86 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0C9E
  6: 0x0B8E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0B8F [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0B91 [0x03] Work_Zone[1] = 1*
  9: 0x0B96 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0BA7 [0x1C] WAIT(60* ticks)
 11: 0x0BAA [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0BAD [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0BB4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 14: 0x0BC5 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 15: 0x0BD2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0BE3 [0x1C] WAIT(300* ticks)
 17: 0x0BE6 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 18: 0x0BED [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
 19: 0x0BF4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0C05 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0C16 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0C27 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 23: 0x0C38 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 24: 0x0C3F [0x1C] WAIT(150* ticks)
 25: 0x0C42 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 26: 0x0C53 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 27: 0x0C62 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x0C73 [0x1C] WAIT(30* ticks)
 29: 0x0C76 [0x30] SET_UCOFF_CONTINUE_ZERO()
 30: 0x0C77 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 31: 0x0C88 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x0C99 [0x46] CAMERA_CONTROL: Restore default settings
 33: 0x0C9B [0x01] GOTO 0x0CA9
 34: 0x0C9E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0CA9
 35: 0x0CA6 [0x01] GOTO 0x0CA9

SUBROUTINE_0CA9:
 36: 0x0CA9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 37: 0x0CAB [0x21] END_EVENT
 38: 0x0CAC [0x00] END_REQSTACK()
```

### Event 124

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0CAD    |
| Data Size    | 309 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0CA0:                                         20 01 48                .H
0CB0: 1A 80 23 24 16 80 02 80  00 80 25 02 00 10 00 80  ..#$......%.....
0CC0: 00 D3 0D 42 46 01 03 01  10 02 80 45 0D 80 F0 FF  ...BF......E....
0CD0: FF 7F F0 FF FF 7F 66 64  6F 31 00 80 1C 0E 80 38  ......fdo1.....8
0CE0: 0F 80 29 01 F0 FF FF 7F  05 45 10 80 F0 FF FF 7F  ..)......E......
0CF0: F0 FF FF 7F 7A 35 30 61  00 80 2D F8 FF FF 7F F8  ....z50a..-.....
0D00: FF FF 7F 31 70 62 32 45  0D 80 F0 FF FF 7F F0 FF  ...1pb2E........
0D10: FF 7F 66 64 69 31 00 80  1C 11 80 29 10 F0 FF FF  ..fdi1.....)....
0D20: 7F 06 29 10 F0 FF FF 7F  18 45 0D 80 F0 FF FF 7F  ..)......E......
0D30: F0 FF FF 7F 62 6C 6F 6E  00 80 45 12 80 F0 FF FF  ....blon..E.....
0D40: 7F F0 FF FF 7F 62 6C 6F  6E 00 80 45 0D 80 F0 FF  .....blon..E....
0D50: FF 7F F0 FF FF 7F 6F 76  6C 31 00 80 45 10 80 F0  ......ovl1..E...
0D60: FF FF 7F F0 FF FF 7F 7A  35 30 62 00 80 27 01 F0  .......z50b..'..
0D70: FF FF 7F 04 1C 13 80 45  12 80 F8 FF FF 7F F8 FF  .......E........
0D80: FF 7F 77 68 6F 31 00 80  55 12 80 F8 FF FF 7F F8  ..who1..U.......
0D90: FF FF 7F 77 68 6F 31 45  0D 80 F8 FF FF 7F F8 FF  ...who1E........
0DA0: FF 7F 66 64 6F 30 00 80  1C 14 80 30 45 12 80 F8  ..fdo0.....0E...
0DB0: FF FF 7F F8 FF FF 7F 77  68 69 31 00 80 45 0D 80  .......whi1..E..
0DC0: F0 FF FF 7F F0 FF FF 7F  62 6C 6F 66 00 80 46 00  ........blof..F.
0DD0: 01 DE 0D 02 00 10 02 80  00 DE 0D 01 DE 0D 20 00  .............. .
0DE0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0CAD [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0CAF [0x48] [System] [4618*]:
    → "You will now be transported to the staging point on the Ilrusi Atoll for participation in Assault.\u007F1\u0000\u0007"
  2: 0x0CB2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0CB3 [0x24] CREATE_DIALOG(message_id=4620*, default_option=1*, option_flags=0*)
    → "Are you ready?\u0007\u000BYes.\u0007Not yet.\u007F1\u0000\u0007"
  4: 0x0CBA [0x25] WAIT_DIALOG_SELECT()
  5: 0x0CBB [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0DD3
  6: 0x0CC3 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0CC4 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0CC6 [0x03] Work_Zone[1] = 1*
  9: 0x0CCB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0CDC [0x1C] WAIT(60* ticks)
 11: 0x0CDF [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0CE2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0CE9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 14: 0x0CFA [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 15: 0x0D07 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0D18 [0x1C] WAIT(300* ticks)
 17: 0x0D1B [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 18: 0x0D22 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
 19: 0x0D29 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0D3A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0D4B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0D5C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 23: 0x0D6D [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 24: 0x0D74 [0x1C] WAIT(150* ticks)
 25: 0x0D77 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 26: 0x0D88 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 27: 0x0D97 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x0DA8 [0x1C] WAIT(30* ticks)
 29: 0x0DAB [0x30] SET_UCOFF_CONTINUE_ZERO()
 30: 0x0DAC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 31: 0x0DBD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x0DCE [0x46] CAMERA_CONTROL: Restore default settings
 33: 0x0DD0 [0x01] GOTO 0x0DDE
 34: 0x0DD3 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0DDE
 35: 0x0DDB [0x01] GOTO 0x0DDE

SUBROUTINE_0DDE:
 36: 0x0DDE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 37: 0x0DE0 [0x21] END_EVENT
 38: 0x0DE1 [0x00] END_REQSTACK()
```

### Event 125

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0DE2    |
| Data Size    | 416 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0DE0:       20 01 48 1B 80 23  24 16 80 02 80 00 80 25     .H..#$......%
0DF0: 02 00 10 00 80 00 08 0F  42 46 01 03 01 10 02 80  ........BF......
0E00: 45 0D 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 00  E..........fdo1.
0E10: 80 1C 0E 80 38 0F 80 29  01 F0 FF FF 7F 05 45 10  ....8..)......E.
0E20: 80 F0 FF FF 7F F0 FF FF  7F 7A 35 30 61 00 80 2D  .........z50a..-
0E30: F8 FF FF 7F F8 FF FF 7F  31 70 62 32 45 0D 80 F0  ........1pb2E...
0E40: FF FF 7F F0 FF FF 7F 66  64 69 31 00 80 1C 11 80  .......fdi1.....
0E50: 29 10 F0 FF FF 7F 06 29  10 F0 FF FF 7F 18 45 0D  )......)......E.
0E60: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 00 80 45  .........blon..E
0E70: 12 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 00 80  ..........blon..
0E80: 45 0D 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 00  E..........ovl1.
0E90: 80 45 10 80 F0 FF FF 7F  F0 FF FF 7F 7A 35 30 62  .E..........z50b
0EA0: 00 80 27 01 F0 FF FF 7F  04 1C 13 80 45 12 80 F8  ..'.........E...
0EB0: FF FF 7F F8 FF FF 7F 77  68 6F 31 00 80 55 12 80  .......who1..U..
0EC0: F8 FF FF 7F F8 FF FF 7F  77 68 6F 31 45 0D 80 F8  ........who1E...
0ED0: FF FF 7F F8 FF FF 7F 66  64 6F 30 00 80 1C 14 80  .......fdo0.....
0EE0: 30 45 12 80 F8 FF FF 7F  F8 FF FF 7F 77 68 69 31  0E..........whi1
0EF0: 00 80 45 0D 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
0F00: 66 00 80 46 00 01 13 0F  02 00 10 02 80 00 13 0F  f..F............
0F10: 01 13 0F 20 00 21 00 03  01 00 00 80 02 07 10 00  ... .!..........
0F20: 80 00 2C 0F 03 01 00 1C  80 01 81 0F 02 06 10 02  ..,.............
0F30: 80 00 37 0F 01 81 0F 03  02 10 05 10 03 03 10 0D  ..7.............
0F40: 80 48 1D 80 23 24 1E 80  00 80 00 80 25 02 00 10  .H..#$......%...
0F50: 00 80 00 5D 0F 03 01 00  02 80 01 81 0F 02 00 10  ...]............
0F60: 02 80 00 81 0F 02 05 10  0D 80 03 79 0F 48 1F 80  ...........y.H..
0F70: 23 03 01 00 02 80 01 7E  0F 03 01 00 20 80 01 81  #......~.... ...
0F80: 0F 1B                                             ..              
```

#### Opcodes

```
  0: 0x0DE2 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0DE4 [0x48] [System] [4619*]:
    → "You will now be transported to the staging point on Nyzul Isle for participation in Assault.\u007F1\u0000\u0007"
  2: 0x0DE7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0DE8 [0x24] CREATE_DIALOG(message_id=4620*, default_option=1*, option_flags=0*)
    → "Are you ready?\u0007\u000BYes.\u0007Not yet.\u007F1\u0000\u0007"
  4: 0x0DEF [0x25] WAIT_DIALOG_SELECT()
  5: 0x0DF0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0F08
  6: 0x0DF8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0DF9 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0DFB [0x03] Work_Zone[1] = 1*
  9: 0x0E00 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0E11 [0x1C] WAIT(60* ticks)
 11: 0x0E14 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0E17 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0E1E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 14: 0x0E2F [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1pb2" with entities [EventEntity, EventEntity]
 15: 0x0E3C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0E4D [0x1C] WAIT(300* ticks)
 17: 0x0E50 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 18: 0x0E57 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x18)
 19: 0x0E5E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0E6F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x0E80 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0E91 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z50b" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 23: 0x0EA2 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 24: 0x0EA9 [0x1C] WAIT(150* ticks)
 25: 0x0EAC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 26: 0x0EBD [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 27: 0x0ECC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x0EDD [0x1C] WAIT(30* ticks)
 29: 0x0EE0 [0x30] SET_UCOFF_CONTINUE_ZERO()
 30: 0x0EE1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 31: 0x0EF2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x0F03 [0x46] CAMERA_CONTROL: Restore default settings
 33: 0x0F05 [0x01] GOTO 0x0F13
 34: 0x0F08 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0F13
 35: 0x0F10 [0x01] GOTO 0x0F13

SUBROUTINE_0F13:
 36: 0x0F13 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 37: 0x0F15 [0x21] END_EVENT
 38: 0x0F16 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0F17 [0x03] ExtData[1]->WorkLocal[1] = 0*
     0x0F1C [0x02] IF !(Work_Zone[7] == 0*) GOTO 0x0F2C
     0x0F24 [0x03] ExtData[1]->WorkLocal[1] = 100*
     0x0F29 [0x01] GOTO 0x0F81
     0x0F2C [0x02] IF !(Work_Zone[6] == 1*) GOTO 0x0F37
     0x0F34 [0x01] GOTO 0x0F81
     0x0F37 [0x03] Work_Zone[2] = Work_Zone[5]
     0x0F3C [0x03] Work_Zone[3] = 200*
     0x0F41 [0x48] [System] [4610*]:
    → "You currently have 
\u0000 \u007F\u0012\u0000[credit/credits] of Imperial Standing..\u0007It will cost 
\u0001 \u007F\u0012\u0001[credit/credits] to travel to your destination. Proceed?\u007F1\u0000\u0007"
     0x0F44 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0F45 [0x24] CREATE_DIALOG(message_id=4611*, default_option=0*, option_flags=0*)
    → "Spend Imperial Standing?\u0007\u000BNo, cancel.\u0007Yes, proceed.\u007F1\u0000\u0007"
     0x0F4C [0x25] WAIT_DIALOG_SELECT()
     0x0F4D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0F5D
     0x0F55 [0x03] ExtData[1]->WorkLocal[1] = 1*
     0x0F5A [0x01] GOTO 0x0F81
     0x0F5D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0F81
     0x0F65 [0x02] IF !(Work_Zone[5] >= 200*) GOTO 0x0F79
     0x0F6D [0x48] [System] [4612*]:
    → "You do not possess sufficient Imperial Standing.\u0000\u0007"
     0x0F70 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0F71 [0x03] ExtData[1]->WorkLocal[1] = 1*
     0x0F76 [0x01] GOTO 0x0F7E
     0x0F79 [0x03] ExtData[1]->WorkLocal[1] = 1000*
     0x0F7E [0x01] GOTO 0x0F81
     0x0F81 [0x1B] RETURN
```
