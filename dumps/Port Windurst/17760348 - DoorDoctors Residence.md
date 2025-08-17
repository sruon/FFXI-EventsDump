# 17760348 - DoorDoctors Residence

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 7460 bytes              |
| Total Events     | 7                       |
| References Count | 61                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |   2787 |            364 |
| [386](#event-386)        | 0x0AE4       |      1 |              1 |
| [390](#event-390)        | 0x0AE5       |      1 |              1 |
| [65535.2](#event-655352) | 0x0AE6       |   4380 |            549 |
| [432](#event-432)        | 0x1C02       |      1 |              1 |
| [433](#event-433)        | 0x1C03       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x000C      |          12 |
|       3 | 0x0813      |        2067 |
|       4 | 0x0078      |         120 |
|       5 | 0x007F      |         127 |
|       6 | 0x0014      |          20 |
|       7 | 0x0064      |         100 |
|       8 | 0x008B      |         139 |
|       9 | 0x00C8      |         200 |
|      10 | 0x0F76      |        3958 |
|      11 | 0x0F78      |        3960 |
|      12 | 0x0F84      |        3972 |
|      13 | 0x0F85      |        3973 |
|      14 | 0x0F88      |        3976 |
|      15 | 0x0F87      |        3975 |
|      16 | 0x003C      |          60 |
|      17 | 0x012C      |         300 |
|      18 | 0x061F      |        1567 |
|      19 | 0x0400      |        1024 |
|      20 | 0x0F7E      |        3966 |
|      21 | 0x0F7F      |        3967 |
|      22 | 0x0F80      |        3968 |
|      23 | 0x0F81      |        3969 |
|      24 | 0x0008      |           8 |
|      25 | 0x0F8F      |        3983 |
|      26 | 0x001E      |          30 |
|      27 | 0x007B      |         123 |
|      28 | 0x0003      |           3 |
|      29 | 0x0F8C      |        3980 |
|      30 | 0x000A      |          10 |
|      31 | 0x0032      |          50 |
|      32 | 0x0097      |         151 |
|      33 | 0x0096      |         150 |
|      34 | 0x0013      |          19 |
|      35 | 0x0F95      |        3989 |
|      36 | 0x0F96      |        3990 |
|      37 | 0x0F97      |        3991 |
|      38 | 0x0F98      |        3992 |
|      39 | 0x07D0      |        2000 |
|      40 | 0x0F9B      |        3995 |
|      41 | 0x0FA2      |        4002 |
|      42 | 0x03E8      |        1000 |
|      43 | 0x00A1      |         161 |
|      44 | 0x0FB3      |        4019 |
|      45 | 0x0FB5      |        4021 |
|      46 | 0x0FB8      |        4024 |
|      47 | 0x0FB9      |        4025 |
|      48 | 0x0C03      |        3075 |
|      49 | 0x0FBA      |        4026 |
|      50 | 0x000F      |          15 |
|      51 | 0x0FBE      |        4030 |
|      52 | 0x085E      |        2142 |
|      53 | 0x0FC2      |        4034 |
|      54 | 0x0FC3      |        4035 |
|      55 | 0x0FC5      |        4037 |
|      56 | 0x000D      |          13 |
|      57 | 0x0FCA      |        4042 |
|      58 | 0x0FD0      |        4048 |
|      59 | 0x0C29      |        3113 |
|      60 | 0x0FE0      |        4064 |

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

### Event 65535.1

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 2787 bytes |
| Instructions | 364        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 00 80 02 00  00 01 80 00 11 00 01 1F   ...............
0010: 00 77 02 80 01 80 4E 01  A4 00 0F 01 38 03 80 29  .w....N.....8..)
0020: 08 F0 FF FF 7F 0A 29 0B  F0 FF FF 7F 41 5C 00 04  ......).....A\..
0030: 80 5C 01 04 80 5D 05 80  06 80 1C 07 80 4E 00 52  .\...].......N.R
0040: 00 0F 01 4E 00 53 00 0F  01 4E 00 54 00 0F 01 4E  ...N.S...N.T...N
0050: 00 56 00 0F 01 4E 00 57  00 0F 01 4E 00 55 00 0F  .V...N.W...N.U..
0060: 01 80 52 00 0F 01 80 53  00 0F 01 80 54 00 0F 01  ..R....S....T...
0070: 80 56 00 0F 01 80 57 00  0F 01 80 55 00 0F 01 2C  .V....W....U...,
0080: 55 00 0F 01 55 00 0F 01  77 6F 66 34 02 00 00 01  U...U...wof4....
0090: 80 00 EA 00 45 08 80 09  00 0F 01 09 00 0F 01 73  ....E..........s
00A0: 30 35 35 01 80 45 09 80  F0 FF FF 7F F0 FF FF 7F  055..E..........
00B0: 66 64 69 31 01 80 2B 52  00 0F 01 0A 80 23 4A F0  fdi1..+R.....#J.
00C0: FF FF 7F 52 00 0F 01 52  08 80 09 00 0F 01 09 00  ...R...R........
00D0: 0F 01 73 30 35 35 45 08  80 09 00 0F 01 09 00 0F  ..s055E.........
00E0: 01 73 30 35 33 01 80 01  0C 01 45 08 80 09 00 0F  .s053.....E.....
00F0: 01 09 00 0F 01 73 30 35  33 01 80 45 09 80 F0 FF  .....s053..E....
0100: FF 7F F0 FF FF 7F 66 64  69 31 01 80 27 0B 52 00  ......fdi1..'.R.
0110: 0F 01 97 27 0B 53 00 0F  01 46 27 0B 54 00 0F 01  ...'.S...F'.T...
0120: 3A 27 0B 56 00 0F 01 39  27 0B 57 00 0F 01 3F 27  :'.V...9'.W...?'
0130: 0B 55 00 0F 01 54 2A 0B  52 00 0F 01 2A 0B 53 00  .U...T*.R...*.S.
0140: 0F 01 2A 0B 54 00 0F 01  2A 0B 56 00 0F 01 2A 0B  ..*.T...*.V...*.
0150: 57 00 0F 01 2A 0B 55 00  0F 01 55 08 80 09 00 0F  W...*.U...U.....
0160: 01 09 00 0F 01 73 30 35  33 45 08 80 09 00 0F 01  .....s053E......
0170: 09 00 0F 01 73 31 30 34  01 80 02 00 00 01 80 00  ....s104........
0180: A6 01 29 0B 52 00 0F 01  9B 4A 52 00 0F 01 55 00  ..).R....JR...U.
0190: 0F 01 45 08 80 09 00 0F  01 09 00 0F 01 73 30 35  ..E..........s05
01A0: 34 01 80 01 AF 01 4A 52  00 0F 01 55 00 0F 01 2B  4.....JR...U...+
01B0: 52 00 0F 01 0B 80 23 27  08 54 00 0F 01 05 27 08  R.....#'.T....'.
01C0: 53 00 0F 01 09 27 08 56  00 0F 01 03 27 08 57 00  S....'.V....'.W.
01D0: 0F 01 05 2B 53 00 0F 01  0C 80 23 2B 54 00 0F 01  ...+S.....#+T...
01E0: 0D 80 23 2B 56 00 0F 01  0E 80 23 2B 57 00 0F 01  ..#+V.....#+W...
01F0: 0F 80 23 2A 08 54 00 0F  01 2A 08 53 00 0F 01 2A  ..#*.T...*.S...*
0200: 08 56 00 0F 01 2A 08 57  00 0F 01 29 08 54 00 0F  .V...*.W...).T..
0210: 01 06 29 08 53 00 0F 01  0A 29 08 57 00 0F 01 04  ..).S....).W....
0220: 29 08 56 00 0F 01 04 45  09 80 F0 FF FF 7F F0 FF  ).V....E........
0230: FF 7F 66 64 6F 31 01 80  1C 10 80 29 0B F0 FF FF  ..fdo1.....)....
0240: 7F 42 29 0B 52 00 0F 01  96 29 0B 54 00 0F 01 39  .B).R....).T...9
0250: 29 0B 57 00 0F 01 3E 29  0B 56 00 0F 01 38 29 0B  ).W...>).V...8).
0260: 55 00 0F 01 53 29 0B 53  00 0F 01 45 4E 00 5A 00  U...S).S...EN.Z.
0270: 0F 01 1C 10 80 45 08 80  09 00 0F 01 09 00 0F 01  .....E..........
0280: 73 30 35 36 01 80 45 09  80 F0 FF FF 7F F0 FF FF  s056..E.........
0290: 7F 66 64 69 31 01 80 1C  11 80 45 09 80 F0 FF FF  .fdi1.....E.....
02A0: 7F F0 FF FF 7F 66 64 6F  31 01 80 55 08 80 09 00  .....fdo1..U....
02B0: 0F 01 09 00 0F 01 73 30  35 36 1C 10 80 45 08 80  ......s056...E..
02C0: 09 00 0F 01 09 00 0F 01  73 30 35 37 01 80 45 09  ........s057..E.
02D0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 01 80 29  .........fdi1..)
02E0: 0B 52 00 0F 01 9D 4A 52  00 0F 01 54 00 0F 01 29  .R....JR...T...)
02F0: 0B 52 00 0F 01 9E 4A 53  00 0F 01 54 00 0F 01 52  .R....JS...T...R
0300: 08 80 09 00 0F 01 09 00  0F 01 73 30 35 37 45 08  ..........s057E.
0310: 80 09 00 0F 01 09 00 0F  01 73 30 35 38 01 80 29  .........s058..)
0320: 0B 54 00 0F 01 3E 29 0B  52 00 0F 01 9F 29 0B 5A  .T...>).R....).Z
0330: 00 0F 01 26 45 08 80 09  00 0F 01 09 00 0F 01 73  ...&E..........s
0340: 30 35 39 01 80 4A 57 00  0F 01 52 00 0F 01 29 0B  059..JW...R...).
0350: 57 00 0F 01 44 80 5A 00  0F 01 4B 57 00 0F 01 12  W...D.Z...KW....
0360: 80 4A 52 00 0F 01 5A 00  0F 01 4A 54 00 0F 01 5A  .JR...Z...JT...Z
0370: 00 0F 01 4A 53 00 0F 01  5A 00 0F 01 4A 56 00 0F  ...JS...Z...JV..
0380: 01 5A 00 0F 01 27 0B 5A  00 0F 01 29 45 09 80 F0  .Z...'.Z...)E...
0390: FF FF 7F F0 FF FF 7F 66  64 6F 31 01 80 1C 10 80  .......fdo1.....
03A0: 27 0B 55 00 0F 01 55 27  0B 54 00 0F 01 3B 27 0B  '.U...U'.T...;'.
03B0: 53 00 0F 01 47 2A 0B 54  00 0F 01 2A 0B 53 00 0F  S...G*.T...*.S..
03C0: 01 1C 10 80 45 08 80 09  00 0F 01 09 00 0F 01 73  ....E..........s
03D0: 30 36 30 01 80 45 09 80  F0 FF FF 7F F0 FF FF 7F  060..E..........
03E0: 66 64 69 31 01 80 1C 09  80 2A 0B 55 00 0F 01 4A  fdi1.....*.U...J
03F0: 52 00 0F 01 5A 00 0F 01  4A 54 00 0F 01 5A 00 0F  R...Z...JT...Z..
0400: 01 4A 53 00 0F 01 5A 00  0F 01 4A 56 00 0F 01 5A  .JS...Z...JV...Z
0410: 00 0F 01 4B 52 00 0F 01  13 80 6F 76 52 00 0F 01  ...KR.....ovR...
0420: 5D 01 80 04 80 2C 52 00  0F 01 52 00 0F 01 77 6F  ]....,R...R...wo
0430: 6E 34 29 08 52 00 0F 01  1C 29 08 52 00 0F 01 1D  n4).R....).R....
0440: 45 08 80 09 00 0F 01 09  00 0F 01 73 30 36 31 01  E..........s061.
0450: 80 27 0B 57 00 0F 01 40  1C 10 80 27 0B 56 00 0F  .'.W...@...'.V..
0460: 01 3A 55 08 80 09 00 0F  01 09 00 0F 01 73 30 36  .:U..........s06
0470: 31 2B 52 00 0F 01 14 80  23 4A 53 00 0F 01 52 00  1+R.....#JS...R.
0480: 0F 01 2B 52 00 0F 01 15  80 23 2B 52 00 0F 01 16  ..+R.....#+R....
0490: 80 23 2B 52 00 0F 01 17  80 23 29 08 52 00 0F 01  .#+R.....#).R...
04A0: 1E 29 08 52 00 0F 01 1F  2A 0B 57 00 0F 01 2A 0B  .).R....*.W...*.
04B0: 56 00 0F 01 2A 0B 5A 00  0F 01 29 0B 5A 00 0F 01  V...*.Z...).Z...
04C0: 27 62 18 80 5A 00 0F 01  5A 00 0F 01 6D 61 69 6E  'b..Z...Z...main
04D0: 01 80 45 08 80 F0 FF FF  7F F0 FF FF 7F 73 31 30  ..E..........s10
04E0: 37 01 80 2B 5A 00 0F 01  19 80 23 29 08 52 00 0F  7..+Z.....#).R..
04F0: 01 0E 29 08 54 00 0F 01  07 29 08 53 00 0F 01 0B  ..).T....).S....
0500: 29 08 57 00 0F 01 07 29  08 56 00 0F 01 06 1C 07  ).W....).V......
0510: 80 4A 52 00 0F 01 F0 FF  FF 7F 1C 1A 80 29 0B 52  .JR..........).R
0520: 00 0F 01 A1 62 18 80 5A  00 0F 01 5A 00 0F 01 73  ....b..Z...Z...s
0530: 74 6F 6E 01 80 27 0B 52  00 0F 01 98 27 0B 53 00  ton..'.R....'.S.
0540: 0F 01 48 27 0B 54 00 0F  01 3C 27 0B 56 00 0F 01  ..H'.T...<'.V...
0550: 3B 27 0B 57 00 0F 01 41  27 0B 55 00 0F 01 56 1C  ;'.W...A'.U...V.
0560: 1A 80 4A F0 FF FF 7F 52  00 0F 01 1C 1A 80 4A F0  ..J....R......J.
0570: FF FF 7F 52 00 0F 01 02  00 00 01 80 00 8F 05 1C  ...R............
0580: 1A 80 27 0B F0 FF FF 7F  43 1C 1A 80 01 8F 05 45  ..'.....C......E
0590: 09 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 01 80  ..........fdo1..
05A0: 1C 10 80 5C 00 1B 80 5C  01 1B 80 1C 07 80 5D 05  ...\...\......].
05B0: 80 04 80 2A 0B 52 00 0F  01 2A 0B 53 00 0F 01 2A  ...*.R...*.S...*
05C0: 0B 54 00 0F 01 2A 0B 56  00 0F 01 2A 0B 57 00 0F  .T...*.V...*.W..
05D0: 01 2A 0B 55 00 0F 01 02  00 00 01 80 00 E8 05 2A  .*.U...........*
05E0: 0B F0 FF FF 7F 01 E8 05  29 0B 52 00 0F 01 99 29  ........).R....)
05F0: 0B 53 00 0F 01 49 29 0B  54 00 0F 01 3D 29 0B 56  .S...I).T...=).V
0600: 00 0F 01 3C 29 0B 57 00  0F 01 42 29 0B 55 00 0F  ...<).W...B).U..
0610: 01 57 29 0B F0 FF FF 7F  44 29 0B 5A 00 0F 01 2A  .W).....D).Z...*
0620: 29 0B 5A 00 0F 01 28 29  0B 5A 00 0F 01 13 29 0B  ).Z...().Z....).
0630: 5A 00 0F 01 14 4E 00 59  00 0F 01 45 08 80 09 00  Z....N.Y...E....
0640: 0F 01 09 00 0F 01 73 30  36 32 01 80 45 09 80 F0  ......s062..E...
0650: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 55 08 80  .......fdi1..U..
0660: 09 00 0F 01 09 00 0F 01  73 30 36 32 45 08 80 09  ........s062E...
0670: 00 0F 01 09 00 0F 01 73  30 36 33 01 80 29 0B 52  .......s063..).R
0680: 00 0F 01 9A 4A 52 00 0F  01 53 00 0F 01 29 0B 52  ....JR...S...).R
0690: 00 0F 01 A2 02 09 10 18  80 00 B0 06 45 08 80 09  ............E...
06A0: 00 0F 01 09 00 0F 01 73  31 30 38 01 80 01 C1 06  .......s108.....
06B0: 45 08 80 09 00 0F 01 09  00 0F 01 73 30 36 35 01  E..........s065.
06C0: 80 4A 52 00 0F 01 F0 FF  FF 7F 29 0B 52 00 0F 01  .JR.......).R...
06D0: A3 62 1C 80 59 00 0F 01  59 00 0F 01 6D 61 69 6E  .b..Y...Y...main
06E0: 01 80 4A 52 00 0F 01 55  00 0F 01 4A 56 00 0F 01  ..JR...U...JV...
06F0: 55 00 0F 01 4A 57 00 0F  01 55 00 0F 01 4A 54 00  U...JW...U...JT.
0700: 0F 01 55 00 0F 01 4A 53  00 0F 01 55 00 0F 01 29  ..U...JS...U...)
0710: 0B 55 00 0F 01 5C 4E 01  59 00 0F 01 45 08 80 09  .U...\N.Y...E...
0720: 00 0F 01 09 00 0F 01 73  30 36 34 01 80 27 0B 55  .......s064..'.U
0730: 00 0F 01 58 4A 52 00 0F  01 55 00 0F 01 4A 56 00  ...XJR...U...JV.
0740: 0F 01 55 00 0F 01 4A 57  00 0F 01 55 00 0F 01 4A  ..U...JW...U...J
0750: 54 00 0F 01 55 00 0F 01  4A 53 00 0F 01 55 00 0F  T...U...JS...U..
0760: 01 1C 1A 80 4A 52 00 0F  01 55 00 0F 01 4A 56 00  ....JR...U...JV.
0770: 0F 01 55 00 0F 01 4A 57  00 0F 01 55 00 0F 01 4A  ..U...JW...U...J
0780: 54 00 0F 01 55 00 0F 01  4A 53 00 0F 01 55 00 0F  T...U...JS...U..
0790: 01 1C 1A 80 4A 52 00 0F  01 55 00 0F 01 4A 56 00  ....JR...U...JV.
07A0: 0F 01 55 00 0F 01 4A 57  00 0F 01 55 00 0F 01 4A  ..U...JW...U...J
07B0: 54 00 0F 01 55 00 0F 01  4A 53 00 0F 01 55 00 0F  T...U...JS...U..
07C0: 01 1C 1A 80 4A 52 00 0F  01 55 00 0F 01 4A 56 00  ....JR...U...JV.
07D0: 0F 01 55 00 0F 01 4A 57  00 0F 01 55 00 0F 01 4A  ..U...JW...U...J
07E0: 54 00 0F 01 55 00 0F 01  4A 53 00 0F 01 55 00 0F  T...U...JS...U..
07F0: 01 4A 52 00 0F 01 55 00  0F 01 4A 56 00 0F 01 55  .JR...U...JV...U
0800: 00 0F 01 4A 57 00 0F 01  55 00 0F 01 4A 54 00 0F  ...JW...U...JT..
0810: 01 55 00 0F 01 4A 53 00  0F 01 55 00 0F 01 2A 0B  .U...JS...U...*.
0820: 55 00 0F 01 55 08 80 09  00 0F 01 09 00 0F 01 73  U...U..........s
0830: 30 36 34 4A 52 00 0F 01  5A 00 0F 01 4A 56 00 0F  064JR...Z...JV..
0840: 01 5A 00 0F 01 4A 57 00  0F 01 5A 00 0F 01 4A 54  .Z...JW...Z...JT
0850: 00 0F 01 5A 00 0F 01 4A  53 00 0F 01 5A 00 0F 01  ...Z...JS...Z...
0860: 29 0B 5A 00 0F 01 15 4A  55 00 0F 01 5A 00 0F 01  ).Z....JU...Z...
0870: 1C 07 80 29 08 52 00 0F  01 0E 29 08 54 00 0F 01  ...).R....).T...
0880: 07 29 08 53 00 0F 01 0B  29 08 57 00 0F 01 07 29  .).S....).W....)
0890: 08 56 00 0F 01 06 29 0B  5A 00 0F 01 16 4A 5A 00  .V....).Z....JZ.
08A0: 0F 01 52 00 0F 01 45 08  80 09 00 0F 01 09 00 0F  ..R...E.........
08B0: 01 73 31 30 35 01 80 2B  5A 00 0F 01 1D 80 23 29  .s105..+Z.....#)
08C0: 08 52 00 0F 01 0E 27 0B  55 00 0F 01 59 29 0B 5A  .R....'.U...Y).Z
08D0: 00 0F 01 2D 29 08 52 00  0F 01 0F 52 08 80 09 00  ...-).R....R....
08E0: 0F 01 09 00 0F 01 73 31  30 35 45 08 80 09 00 0F  ......s105E.....
08F0: 01 09 00 0F 01 73 30 36  37 01 80 27 0B F0 FF FF  .....s067..'....
0900: 7F 45 27 0B 57 00 0F 01  43 27 0B 56 00 0F 01 3D  .E'.W...C'.V...=
0910: 27 0B 54 00 0F 01 4A 27  0B 53 00 0F 01 42 29 0A  '.T...J'.S...B).
0920: 59 00 0F 01 04 02 00 00  01 80 00 30 09 01 3E 09  Y..........0..>.
0930: 29 0A 59 00 0F 01 05 27  08 5A 00 0F 01 2C 27 0B  ).Y....'.Z...,'.
0940: 52 00 0F 01 91 1C 1A 80  02 00 00 01 80 00 64 09  R.............d.
0950: 1C 10 80 29 0A 59 00 0F  01 05 27 08 5A 00 0F 01  ...).Y....'.Z...
0960: 2B 01 64 09 1C 07 80 45  09 80 F0 FF FF 7F F0 FF  +.d....E........
0970: FF 7F 66 64 6F 31 01 80  55 08 80 09 00 0F 01 09  ..fdo1..U.......
0980: 00 0F 01 73 30 36 37 2A  0B 52 00 0F 01 2A 0B 57  ...s067*.R...*.W
0990: 00 0F 01 2A 0B 56 00 0F  01 2A 0B 53 00 0F 01 2A  ...*.V...*.S...*
09A0: 0B 54 00 0F 01 2A 0B F0  FF FF 7F 2A 0B 55 00 0F  .T...*.....*.U..
09B0: 01 02 00 00 01 80 00 C2  09 2A 08 5A 00 0F 01 01  .........*.Z....
09C0: C8 09 2A 08 5A 00 0F 01  1C 10 80 45 08 80 09 00  ..*.Z......E....
09D0: 0F 01 09 00 0F 01 73 30  36 36 01 80 27 0B 55 00  ......s066..'.U.
09E0: 0F 01 5A 1C 1A 80 45 09  80 F0 FF FF 7F F0 FF FF  ..Z...E.........
09F0: 7F 66 64 69 31 01 80 2A  0B 55 00 0F 01 2A 08 5A  .fdi1..*.U...*.Z
0A00: 00 0F 01 1C 1A 80 7B 55  00 0F 01 4A F0 FF FF 7F  ......{U...J....
0A10: 55 00 0F 01 29 0B 55 00  0F 01 5D 45 08 80 09 00  U...).U...]E....
0A20: 0F 01 09 00 0F 01 73 30  36 38 01 80 4B 55 00 0F  ......s068..KU..
0A30: 01 13 80 1C 1A 80 27 08  55 00 0F 01 11 1C 1E 80  ......'.U.......
0A40: 2C 55 00 0F 01 55 00 0F  01 77 6F 6E 34 2A 08 55  ,U...U...won4*.U
0A50: 00 0F 01 29 0B 55 00 0F  01 5E 29 08 55 00 0F 01  ...).U...^).U...
0A60: 12 45 08 80 09 00 0F 01  09 00 0F 01 73 30 34 39  .E..........s049
0A70: 01 80 2C 55 00 0F 01 55  00 0F 01 77 6F 66 34 27  ..,U...U...wof4'
0A80: 0B 55 00 0F 01 4C 1C 1F  80 4A F0 FF FF 7F 55 00  .U...L...J....U.
0A90: 0F 01 1C 1F 80 4A F0 FF  FF 7F 55 00 0F 01 1C 1F  .....J....U.....
0AA0: 80 4A F0 FF FF 7F 55 00  0F 01 45 09 80 F0 FF FF  .J....U...E.....
0AB0: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 10 80 7B 5A  .....fdo1.....{Z
0AC0: 00 0F 01 5C 00 20 80 5C  01 20 80 1C 21 80 02 00  ...\. .\. ..!...
0AD0: 00 01 80 00 D9 0A 01 E3  0A 4E 00 A4 00 0F 01 38  .........N.....8
0AE0: 22 80 78 00                                       ".x.            
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = 1*
  1: 0x0006 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0011
  2: 0x000E [0x01] GOTO 0x001F
  3: 0x0011 [0x77] SET_EVENT_TIME_WEATHER(hour=12*, weather=0*)
  4: 0x0016 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Unnamed NPC (ID: 17760420/0x010F00A4)
  5: 0x001C [0x38] SET_CLIENT_EVENT_MODE(mode=2067*)

SUBROUTINE_001F:
  6: 0x001F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x0A)
  7: 0x0026 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x41)
  8: 0x002D [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 120*
  9: 0x0031 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 120*
 10: 0x0035 [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=20*)
 11: 0x003A [0x1C] WAIT(100* ticks)
 12: 0x003D [0x4E] SET_ENTITY_HIDE_FLAG: Show Kohlo-Lakolo (ID: 17760338/0x010F0052)
 13: 0x0043 [0x4E] SET_ENTITY_HIDE_FLAG: Show Papo-Hopo (ID: 17760339/0x010F0053)
 14: 0x0049 [0x4E] SET_ENTITY_HIDE_FLAG: Show Gomada-Vulmada (ID: 17760340/0x010F0054)
 15: 0x004F [0x4E] SET_ENTITY_HIDE_FLAG: Show Yafa Yaa (ID: 17760342/0x010F0056)
 16: 0x0055 [0x4E] SET_ENTITY_HIDE_FLAG: Show Pyo Nzon (ID: 17760343/0x010F0057)
 17: 0x005B [0x4E] SET_ENTITY_HIDE_FLAG: Show Pichichi (ID: 17760341/0x010F0055)
 18: 0x0061 [0x80] LOAD_WAIT(entity=Kohlo-Lakolo (ID: 17760338/0x010F0052))
 19: 0x0066 [0x80] LOAD_WAIT(entity=Papo-Hopo (ID: 17760339/0x010F0053))
 20: 0x006B [0x80] LOAD_WAIT(entity=Gomada-Vulmada (ID: 17760340/0x010F0054))
 21: 0x0070 [0x80] LOAD_WAIT(entity=Yafa Yaa (ID: 17760342/0x010F0056))
 22: 0x0075 [0x80] LOAD_WAIT(entity=Pyo Nzon (ID: 17760343/0x010F0057))
 23: 0x007A [0x80] LOAD_WAIT(entity=Pichichi (ID: 17760341/0x010F0055))
 24: 0x007F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "wof4" with entities [Pichichi (ID: 17760341/0x010F0055), Pichichi (ID: 17760341/0x010F0055)]
 25: 0x008C [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x00EA
 26: 0x0094 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s055" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 27: 0x00A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x00B6 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3958*]:
    → "Ahoy! Ahoy!"
 29: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x00BE [0x4A] LocalPlayer looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
 31: 0x00C7 [0x52] END_LOAD_SCHEDULER: End scheduler "s055" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
 32: 0x00D6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s053" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 33: 0x00E7 [0x01] GOTO 0x010C
 34: 0x00EA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s053" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 35: 0x00FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]

SUBROUTINE_010C:
 36: 0x010C [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x97)
 37: 0x0113 [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x46)
 38: 0x011A [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x3A)
 39: 0x0121 [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x39)
 40: 0x0128 [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x3F)
 41: 0x012F [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x54)
 42: 0x0136 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
 43: 0x013C [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
 44: 0x0142 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
 45: 0x0148 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
 46: 0x014E [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
 47: 0x0154 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
 48: 0x015A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s053" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
 49: 0x0169 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s104" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 50: 0x017A [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x01A6
 51: 0x0182 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x9B)
 52: 0x0189 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
 53: 0x0192 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s054" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 54: 0x01A3 [0x01] GOTO 0x01AF
 55: 0x01A6 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)

SUBROUTINE_01AF:
 56: 0x01AF [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3960*]:
    → "Star Onion Brigade, attentio`n! "Operation Onion" will now begin!"
 57: 0x01B6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x01B7 [0x27] REQ_SET(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x05)
 59: 0x01BE [0x27] REQ_SET(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x09)
 60: 0x01C5 [0x27] REQ_SET(priority=0x08, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x03)
 61: 0x01CC [0x27] REQ_SET(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x05)
 62: 0x01D3 [0x2B] Papo-Hopo (ID: 17760339/0x010F0053) [3972*]:
    → "Yippee!"
 63: 0x01DA [0x23] WAIT_FOR_DIALOG_INTERACTION
 64: 0x01DB [0x2B] Gomada-Vulmada (ID: 17760340/0x010F0054) [3973*]:
    → "Hi-ho Silver!"
 65: 0x01E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x01E3 [0x2B] Yafa Yaa (ID: 17760342/0x010F0056) [3976*]:
    → "Meow!"
 67: 0x01EA [0x23] WAIT_FOR_DIALOG_INTERACTION
 68: 0x01EB [0x2B] Pyo Nzon (ID: 17760343/0x010F0057) [3975*]:
    → "Herrre we go again!"
 69: 0x01F2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 70: 0x01F3 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
 71: 0x01F9 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
 72: 0x01FF [0x2A] GET_REQ_LEVEL(level=8, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
 73: 0x0205 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
 74: 0x020B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x06)
 75: 0x0212 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x0A)
 76: 0x0219 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x04)
 77: 0x0220 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x04)
 78: 0x0227 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 79: 0x0238 [0x1C] WAIT(60* ticks)
 80: 0x023B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x42)
 81: 0x0242 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x96)
 82: 0x0249 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x39)
 83: 0x0250 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x3E)
 84: 0x0257 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x38)
 85: 0x025E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x53)
 86: 0x0265 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x45)
 87: 0x026C [0x4E] SET_ENTITY_HIDE_FLAG: Show Nanaa Mihgo (ID: 17760346/0x010F005A)
 88: 0x0272 [0x1C] WAIT(60* ticks)
 89: 0x0275 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s056" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 90: 0x0286 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 91: 0x0297 [0x1C] WAIT(300* ticks)
 92: 0x029A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 93: 0x02AB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s056" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
 94: 0x02BA [0x1C] WAIT(60* ticks)
 95: 0x02BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s057" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 96: 0x02CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 97: 0x02DF [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x9D)
 98: 0x02E6 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Gomada-Vulmada (ID: 17760340/0x010F0054)
 99: 0x02EF [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x9E)
100: 0x02F6 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Gomada-Vulmada (ID: 17760340/0x010F0054)
101: 0x02FF [0x52] END_LOAD_SCHEDULER: End scheduler "s057" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
102: 0x030E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s058" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
103: 0x031F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x3E)
104: 0x0326 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x9F)
105: 0x032D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x26)
106: 0x0334 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s059" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
107: 0x0345 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
108: 0x034E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x44)
109: 0x0355 [0x80] LOAD_WAIT(entity=Nanaa Mihgo (ID: 17760346/0x010F005A))
110: 0x035A [0x4B] UPDATE_ENTITY_YAW(entity=Pyo Nzon (ID: 17760343/0x010F0057), yaw=8.6°*)
111: 0x0361 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
112: 0x036A [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
113: 0x0373 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
114: 0x037C [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
115: 0x0385 [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x29)
116: 0x038C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
117: 0x039D [0x1C] WAIT(60* ticks)
118: 0x03A0 [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x55)
119: 0x03A7 [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x3B)
120: 0x03AE [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x47)
121: 0x03B5 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
122: 0x03BB [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
123: 0x03C1 [0x1C] WAIT(60* ticks)
124: 0x03C4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s060" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
125: 0x03D5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
126: 0x03E6 [0x1C] WAIT(200* ticks)
127: 0x03E9 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
128: 0x03EF [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
129: 0x03F8 [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
130: 0x0401 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
131: 0x040A [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
132: 0x0413 [0x4B] UPDATE_ENTITY_YAW(entity=Kohlo-Lakolo (ID: 17760338/0x010F0052), yaw=5.6°*)
133: 0x041A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
134: 0x041B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Kohlo-Lakolo (ID: 17760338/0x010F0052) Render.Flags0 and Render.Flags3 conditions are met
135: 0x0420 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=120*)
136: 0x0425 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "won4" with entities [Kohlo-Lakolo (ID: 17760338/0x010F0052), Kohlo-Lakolo (ID: 17760338/0x010F0052)]
137: 0x0432 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x1C)
138: 0x0439 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x1D)
139: 0x0440 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s061" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
140: 0x0451 [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x40)
141: 0x0458 [0x1C] WAIT(60* ticks)
142: 0x045B [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x3A)
143: 0x0462 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s061" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
144: 0x0471 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3966*]:
    → "Wait till you see the whites of her eyes, then let her have it with our onion stinky-bombs!!!"
145: 0x0478 [0x23] WAIT_FOR_DIALOG_INTERACTION
146: 0x0479 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
147: 0x0482 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3967*]:
    → "Three!"
148: 0x0489 [0x23] WAIT_FOR_DIALOG_INTERACTION
149: 0x048A [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3968*]:
    → "Two!"
150: 0x0491 [0x23] WAIT_FOR_DIALOG_INTERACTION
151: 0x0492 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3969*]:
    → "One!"
152: 0x0499 [0x23] WAIT_FOR_DIALOG_INTERACTION
153: 0x049A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x1E)
154: 0x04A1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x1F)
155: 0x04A8 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
156: 0x04AE [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
157: 0x04B4 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A))
158: 0x04BA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x27)
159: 0x04C1 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Nanaa Mihgo (ID: 17760346/0x010F005A), Nanaa Mihgo (ID: 17760346/0x010F005A)], work=[8*, 0*]
160: 0x04D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s107" with entities [LocalPlayer, LocalPlayer], work=[139*, 0*]
161: 0x04E3 [0x2B] Nanaa Mihgo (ID: 17760346/0x010F005A) [3983*]:
    → "Grrrowl!!!"
162: 0x04EA [0x23] WAIT_FOR_DIALOG_INTERACTION
163: 0x04EB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x0E)
164: 0x04F2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x07)
165: 0x04F9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x0B)
166: 0x0500 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x07)
167: 0x0507 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x06)
168: 0x050E [0x1C] WAIT(100* ticks)
169: 0x0511 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at LocalPlayer
170: 0x051A [0x1C] WAIT(30* ticks)
171: 0x051D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0xA1)
172: 0x0524 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "ston" with entities [Nanaa Mihgo (ID: 17760346/0x010F005A), Nanaa Mihgo (ID: 17760346/0x010F005A)], work=[8*, 0*]
173: 0x0535 [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x98)
174: 0x053C [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x48)
175: 0x0543 [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x3C)
176: 0x054A [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x3B)
177: 0x0551 [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x41)
178: 0x0558 [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x56)
179: 0x055F [0x1C] WAIT(30* ticks)
180: 0x0562 [0x4A] LocalPlayer looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
181: 0x056B [0x1C] WAIT(30* ticks)
182: 0x056E [0x4A] LocalPlayer looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
183: 0x0577 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x058F
184: 0x057F [0x1C] WAIT(30* ticks)
185: 0x0582 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x43)
186: 0x0589 [0x1C] WAIT(30* ticks)
187: 0x058C [0x01] GOTO 0x058F

SUBROUTINE_058F:
188: 0x058F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
189: 0x05A0 [0x1C] WAIT(60* ticks)
190: 0x05A3 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 123*
191: 0x05A7 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 123*
192: 0x05AB [0x1C] WAIT(100* ticks)
193: 0x05AE [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=120*)
194: 0x05B3 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
195: 0x05B9 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
196: 0x05BF [0x2A] GET_REQ_LEVEL(level=11, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
197: 0x05C5 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
198: 0x05CB [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
199: 0x05D1 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
200: 0x05D7 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x05E8
201: 0x05DF [0x2A] GET_REQ_LEVEL(level=11, entity_id=LocalPlayer)
202: 0x05E5 [0x01] GOTO 0x05E8

SUBROUTINE_05E8:
203: 0x05E8 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x99)
204: 0x05EF [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x49)
205: 0x05F6 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x3D)
206: 0x05FD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x3C)
207: 0x0604 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x42)
208: 0x060B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x57)
209: 0x0612 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x44)
210: 0x0619 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x2A)
211: 0x0620 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x28)
212: 0x0627 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x13)
213: 0x062E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x14)
214: 0x0635 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17760345/0x010F0059)
215: 0x063B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s062" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
216: 0x064C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
217: 0x065D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s062" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
218: 0x066C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s063" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
219: 0x067D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x9A)
220: 0x0684 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Papo-Hopo (ID: 17760339/0x010F0053)
221: 0x068D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0xA2)
222: 0x0694 [0x02] IF !(Work_Zone[9] == 8*) GOTO 0x06B0
223: 0x069C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s108" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
224: 0x06AD [0x01] GOTO 0x06C1
225: 0x06B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s065" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]

SUBROUTINE_06C1:
226: 0x06C1 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at LocalPlayer
227: 0x06CA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0xA3)
228: 0x06D1 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Unnamed NPC (ID: 17760345/0x010F0059), Unnamed NPC (ID: 17760345/0x010F0059)], work=[3*, 0*]
229: 0x06E2 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
230: 0x06EB [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Pichichi (ID: 17760341/0x010F0055)
231: 0x06F4 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Pichichi (ID: 17760341/0x010F0055)
232: 0x06FD [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Pichichi (ID: 17760341/0x010F0055)
233: 0x0706 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Pichichi (ID: 17760341/0x010F0055)
234: 0x070F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x5C)
235: 0x0716 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Unnamed NPC (ID: 17760345/0x010F0059)
236: 0x071C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s064" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
237: 0x072D [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x58)
238: 0x0734 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
239: 0x073D [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Pichichi (ID: 17760341/0x010F0055)
240: 0x0746 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Pichichi (ID: 17760341/0x010F0055)
241: 0x074F [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Pichichi (ID: 17760341/0x010F0055)
242: 0x0758 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Pichichi (ID: 17760341/0x010F0055)
243: 0x0761 [0x1C] WAIT(30* ticks)
244: 0x0764 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
245: 0x076D [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Pichichi (ID: 17760341/0x010F0055)
246: 0x0776 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Pichichi (ID: 17760341/0x010F0055)
247: 0x077F [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Pichichi (ID: 17760341/0x010F0055)
248: 0x0788 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Pichichi (ID: 17760341/0x010F0055)
249: 0x0791 [0x1C] WAIT(30* ticks)
250: 0x0794 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
251: 0x079D [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Pichichi (ID: 17760341/0x010F0055)
252: 0x07A6 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Pichichi (ID: 17760341/0x010F0055)
253: 0x07AF [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Pichichi (ID: 17760341/0x010F0055)
254: 0x07B8 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Pichichi (ID: 17760341/0x010F0055)
255: 0x07C1 [0x1C] WAIT(30* ticks)
256: 0x07C4 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
257: 0x07CD [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Pichichi (ID: 17760341/0x010F0055)
258: 0x07D6 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Pichichi (ID: 17760341/0x010F0055)
259: 0x07DF [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Pichichi (ID: 17760341/0x010F0055)
260: 0x07E8 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Pichichi (ID: 17760341/0x010F0055)
261: 0x07F1 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
262: 0x07FA [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Pichichi (ID: 17760341/0x010F0055)
263: 0x0803 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Pichichi (ID: 17760341/0x010F0055)
264: 0x080C [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Pichichi (ID: 17760341/0x010F0055)
265: 0x0815 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Pichichi (ID: 17760341/0x010F0055)
266: 0x081E [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
267: 0x0824 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s064" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
268: 0x0833 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
269: 0x083C [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
270: 0x0845 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
271: 0x084E [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
272: 0x0857 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
273: 0x0860 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x15)
274: 0x0867 [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
275: 0x0870 [0x1C] WAIT(100* ticks)
276: 0x0873 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x0E)
277: 0x087A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x07)
278: 0x0881 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x0B)
279: 0x0888 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x07)
280: 0x088F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x06)
281: 0x0896 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x16)
282: 0x089D [0x4A] Nanaa Mihgo (ID: 17760346/0x010F005A) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
283: 0x08A6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s105" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
284: 0x08B7 [0x2B] Nanaa Mihgo (ID: 17760346/0x010F005A) [3980*]:
    → "<cough> <cough> Grrr... Pe-ew! Wh-what hit me?"
285: 0x08BE [0x23] WAIT_FOR_DIALOG_INTERACTION
286: 0x08BF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x0E)
287: 0x08C6 [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x59)
288: 0x08CD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x2D)
289: 0x08D4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x0F)
290: 0x08DB [0x52] END_LOAD_SCHEDULER: End scheduler "s105" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
291: 0x08EA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s067" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
292: 0x08FB [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x45)
293: 0x0902 [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x43)
294: 0x0909 [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x3D)
295: 0x0910 [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x4A)
296: 0x0917 [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x42)
297: 0x091E [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Unnamed NPC (ID: 17760345/0x010F0059), tag_num=0x04)
298: 0x0925 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0930
299: 0x092D [0x01] GOTO 0x093E
300: 0x0930 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Unnamed NPC (ID: 17760345/0x010F0059), tag_num=0x05)
301: 0x0937 [0x27] REQ_SET(priority=0x08, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x2C)

SUBROUTINE_093E:
302: 0x093E [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x91)
303: 0x0945 [0x1C] WAIT(30* ticks)
304: 0x0948 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0964
305: 0x0950 [0x1C] WAIT(60* ticks)
306: 0x0953 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Unnamed NPC (ID: 17760345/0x010F0059), tag_num=0x05)
307: 0x095A [0x27] REQ_SET(priority=0x08, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x2B)
308: 0x0961 [0x01] GOTO 0x0964

SUBROUTINE_0964:
309: 0x0964 [0x1C] WAIT(100* ticks)
310: 0x0967 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
311: 0x0978 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s067" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
312: 0x0987 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
313: 0x098D [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
314: 0x0993 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
315: 0x0999 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
316: 0x099F [0x2A] GET_REQ_LEVEL(level=11, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
317: 0x09A5 [0x2A] GET_REQ_LEVEL(level=11, entity_id=LocalPlayer)
318: 0x09AB [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
319: 0x09B1 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x09C2
320: 0x09B9 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A))
321: 0x09BF [0x01] GOTO 0x09C8
322: 0x09C2 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A))

SUBROUTINE_09C8:
323: 0x09C8 [0x1C] WAIT(60* ticks)
324: 0x09CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s066" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
325: 0x09DC [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x5A)
326: 0x09E3 [0x1C] WAIT(30* ticks)
327: 0x09E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
328: 0x09F7 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
329: 0x09FD [0x2A] GET_REQ_LEVEL(level=8, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A))
330: 0x0A03 [0x1C] WAIT(30* ticks)
331: 0x0A06 [0x7B] Pichichi (ID: 17760341/0x010F0055) stops talking
332: 0x0A0B [0x4A] LocalPlayer looks at Pichichi (ID: 17760341/0x010F0055)
333: 0x0A14 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x5D)
334: 0x0A1B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s068" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
335: 0x0A2C [0x4B] UPDATE_ENTITY_YAW(entity=Pichichi (ID: 17760341/0x010F0055), yaw=5.6°*)
336: 0x0A33 [0x1C] WAIT(30* ticks)
337: 0x0A36 [0x27] REQ_SET(priority=0x08, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x11)
338: 0x0A3D [0x1C] WAIT(10* ticks)
339: 0x0A40 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "won4" with entities [Pichichi (ID: 17760341/0x010F0055), Pichichi (ID: 17760341/0x010F0055)]
340: 0x0A4D [0x2A] GET_REQ_LEVEL(level=8, entity_id=Pichichi (ID: 17760341/0x010F0055))
341: 0x0A53 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x5E)
342: 0x0A5A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x12)
343: 0x0A61 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s049" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
344: 0x0A72 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "wof4" with entities [Pichichi (ID: 17760341/0x010F0055), Pichichi (ID: 17760341/0x010F0055)]
345: 0x0A7F [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x4C)
346: 0x0A86 [0x1C] WAIT(50* ticks)
347: 0x0A89 [0x4A] LocalPlayer looks at Pichichi (ID: 17760341/0x010F0055)
348: 0x0A92 [0x1C] WAIT(50* ticks)
349: 0x0A95 [0x4A] LocalPlayer looks at Pichichi (ID: 17760341/0x010F0055)
350: 0x0A9E [0x1C] WAIT(50* ticks)
351: 0x0AA1 [0x4A] LocalPlayer looks at Pichichi (ID: 17760341/0x010F0055)
352: 0x0AAA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
353: 0x0ABB [0x1C] WAIT(60* ticks)
354: 0x0ABE [0x7B] Nanaa Mihgo (ID: 17760346/0x010F005A) stops talking
355: 0x0AC3 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 151*
356: 0x0AC7 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 151*
357: 0x0ACB [0x1C] WAIT(150* ticks)
358: 0x0ACE [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0AD9
359: 0x0AD6 [0x01] GOTO 0x0AE3
360: 0x0AD9 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17760420/0x010F00A4)
361: 0x0ADF [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
362: 0x0AE2 [0x78] ENABLE_GAME_TIMER_RESET_WEATHER()

SUBROUTINE_0AE3:
363: 0x0AE3 [0x00] END_REQSTACK()
```

### Event 386

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0AE4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0AE0:             00                                        .           
```

#### Opcodes

```
  0: 0x0AE4 [0x00] END_REQSTACK()
```

### Event 390

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0AE5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0AE0:                00                                      .          
```

#### Opcodes

```
  0: 0x0AE5 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0AE6     |
| Data Size    | 4380 bytes |
| Instructions | 549        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0AE0:                   03 01  00 00 80 02 01 00 01 80        ..........
0AF0: 00 F9 0A 38 22 80 01 07  0B 77 02 80 01 80 4E 01  ...8"....w....N.
0B00: A4 00 0F 01 38 03 80 29  0B F0 FF FF 7F 41 29 08  ....8..).....A).
0B10: 5B 00 0F 01 05 5C 00 1B  80 5C 01 1B 80 1C 07 80  [....\...\......
0B20: 4E 00 52 00 0F 01 4E 00  53 00 0F 01 4E 00 54 00  N.R...N.S...N.T.
0B30: 0F 01 4E 00 56 00 0F 01  4E 00 57 00 0F 01 4E 00  ..N.V...N.W...N.
0B40: 55 00 0F 01 80 52 00 0F  01 80 53 00 0F 01 80 54  U....R....S....T
0B50: 00 0F 01 80 56 00 0F 01  80 57 00 0F 01 80 55 00  ....V....W....U.
0B60: 0F 01 2C 55 00 0F 01 55  00 0F 01 77 6F 66 34 02  ..,U...U...wof4.
0B70: 01 00 01 80 00 CD 0B 45  08 80 09 00 0F 01 09 00  .......E........
0B80: 0F 01 73 30 35 35 01 80  45 09 80 09 00 0F 01 09  ..s055..E.......
0B90: 00 0F 01 66 64 69 31 01  80 2B 52 00 0F 01 23 80  ...fdi1..+R...#.
0BA0: 23 4A F0 FF FF 7F 52 00  0F 01 52 08 80 09 00 0F  #J....R...R.....
0BB0: 01 09 00 0F 01 73 30 35  35 45 08 80 09 00 0F 01  .....s055E......
0BC0: 09 00 0F 01 73 30 35 33  01 80 01 EF 0B 45 08 80  ....s053.....E..
0BD0: 09 00 0F 01 09 00 0F 01  73 30 35 33 01 80 45 09  ........s053..E.
0BE0: 80 09 00 0F 01 09 00 0F  01 66 64 69 31 01 80 27  .........fdi1..'
0BF0: 0B 52 00 0F 01 97 27 0B  53 00 0F 01 46 27 0B 54  .R....'.S...F'.T
0C00: 00 0F 01 3A 27 0B 56 00  0F 01 39 27 0B 57 00 0F  ...:'.V...9'.W..
0C10: 01 3F 27 0B 55 00 0F 01  54 2A 0B 52 00 0F 01 55  .?'.U...T*.R...U
0C20: 08 80 09 00 0F 01 09 00  0F 01 73 30 35 33 45 08  ..........s053E.
0C30: 80 09 00 0F 01 09 00 0F  01 73 31 30 34 01 80 2A  .........s104..*
0C40: 0B 53 00 0F 01 2A 0B 54  00 0F 01 2A 0B 56 00 0F  .S...*.T...*.V..
0C50: 01 2A 0B 57 00 0F 01 2A  0B 55 00 0F 01 02 01 00  .*.W...*.U......
0C60: 01 80 00 8A 0C 2B 52 00  0F 01 24 80 23 4A 52 00  .....+R...$.#JR.
0C70: 0F 01 55 00 0F 01 45 08  80 09 00 0F 01 09 00 0F  ..U...E.........
0C80: 01 73 30 35 34 01 80 01  93 0C 4A 52 00 0F 01 55  .s054.....JR...U
0C90: 00 0F 01 2B 52 00 0F 01  25 80 23 27 08 54 00 0F  ...+R...%.#'.T..
0CA0: 01 05 27 08 53 00 0F 01  09 27 08 57 00 0F 01 03  ..'.S....'.W....
0CB0: 27 08 56 00 0F 01 03 29  0B 53 00 0F 01 4A 29 0B  '.V....).S...J).
0CC0: 54 00 0F 01 3F 29 0B 56  00 0F 01 3E 29 0B 57 00  T...?).V...>).W.
0CD0: 0F 01 45 2A 08 54 00 0F  01 2A 08 53 00 0F 01 2A  ..E*.T...*.S...*
0CE0: 08 57 00 0F 01 2A 08 56  00 0F 01 29 08 54 00 0F  .W...*.V...).T..
0CF0: 01 06 29 08 53 00 0F 01  0A 29 08 57 00 0F 01 04  ..).S....).W....
0D00: 29 08 56 00 0F 01 04 45  09 80 09 00 0F 01 09 00  ).V....E........
0D10: 0F 01 66 64 6F 31 01 80  1C 10 80 4C 02 01 00 01  ..fdo1.....L....
0D20: 80 00 2A 0D 38 22 80 01  2D 0D 38 03 80 1C 09 80  ..*.8"..-.8.....
0D30: 4D 29 0B F0 FF FF 7F 46  29 0B 5A 00 0F 01 19 1C  M).....F).Z.....
0D40: 1A 80 4E 00 5A 00 0F 01  80 5A 00 0F 01 27 0B 52  ..N.Z....Z...'.R
0D50: 00 0F 01 75 27 0B 53 00  0F 01 37 27 0B 54 00 0F  ...u'.S...7'.T..
0D60: 01 42 45 08 80 09 00 0F  01 09 00 0F 01 73 30 32  .BE..........s02
0D70: 36 01 80 45 09 80 09 00  0F 01 09 00 0F 01 66 64  6..E..........fd
0D80: 69 31 01 80 2B 52 00 0F  01 26 80 23 4B 5A 00 0F  i1..+R...&.#KZ..
0D90: 01 27 80 45 09 80 09 00  0F 01 09 00 0F 01 66 64  .'.E..........fd
0DA0: 6F 31 01 80 27 0B 55 00  0F 01 38 52 08 80 09 00  o1..'.U...8R....
0DB0: 0F 01 09 00 0F 01 73 30  32 36 45 08 80 09 00 0F  ......s026E.....
0DC0: 01 09 00 0F 01 73 30 32  38 01 80 29 0B F0 FF FF  .....s028..)....
0DD0: 7F 47 27 0B 56 00 0F 01  2D 27 0B 57 00 0F 01 2F  .G'.V...-'.W.../
0DE0: 45 09 80 09 00 0F 01 09  00 0F 01 66 64 69 31 01  E..........fdi1.
0DF0: 80 1C 1F 80 02 01 00 01  80 00 02 0E 4E 00 F0 FF  ............N...
0E00: FF 7F 27 0B F0 FF FF 7F  48 2A 0B 52 00 0F 01 2A  ..'.....H*.R...*
0E10: 0B 53 00 0F 01 2A 0B 54  00 0F 01 2A 0B 56 00 0F  .S...*.T...*.V..
0E20: 01 2A 0B 57 00 0F 01 55  08 80 09 00 0F 01 09 00  .*.W...U........
0E30: 0F 01 73 30 32 38 45 08  80 09 00 0F 01 09 00 0F  ..s028E.........
0E40: 01 73 30 34 30 01 80 29  0B 52 00 0F 01 7A 2A 0B  .s040..).R...z*.
0E50: F0 FF FF 7F 45 08 80 09  00 0F 01 09 00 0F 01 73  ....E..........s
0E60: 30 32 37 01 80 27 0B 5A  00 0F 01 1A 2B 5A 00 0F  027..'.Z....+Z..
0E70: 01 28 80 23 2A 0B 55 00  0F 01 4A 5A 00 0F 01 52  .(.#*.U...JZ...R
0E80: 00 0F 01 52 08 80 09 00  0F 01 09 00 0F 01 73 30  ...R..........s0
0E90: 32 37 45 08 80 09 00 0F  01 09 00 0F 01 73 31 30  27E..........s10
0EA0: 36 01 80 29 0B 52 00 0F  01 7B 45 08 80 09 00 0F  6..).R...{E.....
0EB0: 01 09 00 0F 01 73 30 32  39 01 80 29 0B 5A 00 0F  .....s029..).Z..
0EC0: 01 1F 4A 52 00 0F 01 53  00 0F 01 4A 53 00 0F 01  ..JR...S...JS...
0ED0: 52 00 0F 01 29 0B 52 00  0F 01 7C 29 0B 53 00 0F  R...).R...|).S..
0EE0: 01 39 45 08 80 09 00 0F  01 09 00 0F 01 73 30 33  .9E..........s03
0EF0: 30 01 80 4A 52 00 0F 01  5A 00 0F 01 4A 53 00 0F  0..JR...Z...JS..
0F00: 01 5A 00 0F 01 27 0B F0  FF FF 7F 49 27 0B 53 00  .Z...'.....I'.S.
0F10: 0F 01 38 27 0B 54 00 0F  01 43 27 0B 55 00 0F 01  ..8'.T...C'.U...
0F20: 3A 27 0B 56 00 0F 01 30  27 0B 57 00 0F 01 33 27  :'.V...0'.W...3'
0F30: 0B 5A 00 0F 01 1B 27 0B  52 00 0F 01 78 2B 5A 00  .Z....'.R...x+Z.
0F40: 0F 01 29 80 23 2A 0B 5A  00 0F 01 4A F0 FF FF 7F  ..).#*.Z...J....
0F50: 5A 00 0F 01 52 08 80 09  00 0F 01 09 00 0F 01 73  Z...R..........s
0F60: 30 33 30 45 08 80 09 00  0F 01 09 00 0F 01 73 30  030E..........s0
0F70: 33 31 01 80 4A 5A 00 0F  01 55 00 0F 01 29 0B 5A  31..JZ...U...).Z
0F80: 00 0F 01 20 7B 5A 00 0F  01 29 0B 5A 00 0F 01 21  ... {Z...).Z...!
0F90: 29 0B 52 00 0F 01 7D 52  08 80 09 00 0F 01 09 00  ).R...}R........
0FA0: 0F 01 73 30 33 31 45 08  80 09 00 0F 01 09 00 0F  ..s031E.........
0FB0: 01 73 30 33 32 01 80 4B  5A 00 0F 01 2A 80 1C 1A  .s032..KZ...*...
0FC0: 80 29 0B 5A 00 0F 01 22  52 08 80 09 00 0F 01 09  .).Z..."R.......
0FD0: 00 0F 01 73 30 33 32 45  08 80 09 00 0F 01 09 00  ...s032E........
0FE0: 0F 01 73 30 33 33 01 80  5D 01 80 11 80 79 00 5A  ..s033..]....y.Z
0FF0: 00 0F 01 5C 00 0F 01 29  0B 5A 00 0F 01 1C 27 0B  ...\...).Z....'.
1000: 53 00 0F 01 38 27 0B 54  00 0F 01 43 27 0B 55 00  S...8'.T...C'.U.
1010: 0F 01 3A 27 0B 56 00 0F  01 30 27 0B 57 00 0F 01  ..:'.V...0'.W...
1020: 30 27 0D 52 00 0F 01 78  4A 5A 00 0F 01 57 00 0F  0'.R...xJZ...W..
1030: 01 4A F0 FF FF 7F 5A 00  0F 01 27 0B 5A 00 0F 01  .J....Z...'.Z...
1040: 1D 1C 1A 80 4A F0 FF FF  7F 5A 00 0F 01 52 08 80  ....J....Z...R..
1050: 09 00 0F 01 09 00 0F 01  73 30 33 33 45 08 80 09  ........s033E...
1060: 00 0F 01 09 00 0F 01 73  30 33 34 01 80 4C 2A 0D  .......s034..L*.
1070: 52 00 0F 01 2A 0B 53 00  0F 01 2A 0B 54 00 0F 01  R...*.S...*.T...
1080: 2A 0B 55 00 0F 01 2A 0B  56 00 0F 01 2A 0B 5A 00  *.U...*.V...*.Z.
1090: 0F 01 2A 0B 57 00 0F 01  1C 10 80 4A 52 00 0F 01  ..*.W......JR...
10A0: 5A 00 0F 01 4A 53 00 0F  01 5A 00 0F 01 1C 10 80  Z...JS...Z......
10B0: 4D 55 08 80 09 00 0F 01  09 00 0F 01 73 30 33 34  MU..........s034
10C0: 45 08 80 F0 FF FF 7F F0  FF FF 7F 73 31 30 32 01  E..........s102.
10D0: 80 7B 5A 00 0F 01 4A 57  00 0F 01 5A 00 0F 01 1C  .{Z...JW...Z....
10E0: 10 80 4A 52 00 0F 01 F0  FF FF 7F 4A 53 00 0F 01  ..JR.......JS...
10F0: 52 00 0F 01 4A 54 00 0F  01 52 00 0F 01 29 0B 52  R...JT...R...).R
1100: 00 0F 01 7E 45 08 80 09  00 0F 01 09 00 0F 01 73  ...~E..........s
1110: 30 33 35 01 80 5C 00 2B  80 5C 01 2B 80 5D 05 80  035..\.+.\.+.]..
1120: 10 80 27 0B 57 00 0F 01  31 27 0B 56 00 0F 01 2E  ..'.W...1'.V....
1130: 4A 52 00 0F 01 5A 00 0F  01 4A 53 00 0F 01 5A 00  JR...Z...JS...Z.
1140: 0F 01 4A 54 00 0F 01 5A  00 0F 01 2A 0B 57 00 0F  ..JT...Z...*.W..
1150: 01 4A 56 00 0F 01 52 00  0F 01 29 0B 56 00 0F 01  .JV...R...).V...
1160: 31 2A 0B 57 00 0F 01 29  08 57 00 0F 01 09 29 0B  1*.W...).W....).
1170: 57 00 0F 01 34 45 08 80  09 00 0F 01 09 00 0F 01  W...4E..........
1180: 73 30 33 36 01 80 29 08  57 00 0F 01 0A 29 0B 5A  s036..).W....).Z
1190: 00 0F 01 23 29 0B 5A 00  0F 01 24 7C 01 57 00 0F  ...#).Z...$|.W..
11A0: 01 4A 57 00 0F 01 52 00  0F 01 1C 1A 80 29 0B 57  .JW...R......).W
11B0: 00 0F 01 38 4A F0 FF FF  7F 52 00 0F 01 4A 54 00  ...8J....R...JT.
11C0: 0F 01 52 00 0F 01 4A 53  00 0F 01 52 00 0F 01 4A  ..R...JS...R...J
11D0: 55 00 0F 01 52 00 0F 01  4A 56 00 0F 01 52 00 0F  U...R...JV...R..
11E0: 01 4A 52 00 0F 01 55 00  0F 01 52 08 80 09 00 0F  .JR...U...R.....
11F0: 01 09 00 0F 01 73 30 33  36 45 08 80 09 00 0F 01  .....s036E......
1200: 09 00 0F 01 73 30 33 37  01 80 27 0B 57 00 0F 01  ....s037..'.W...
1210: 32 27 0B 56 00 0F 01 2F  29 0B 52 00 0F 01 7F 1C  2'.V.../).R.....
1220: 11 80 52 08 80 09 00 0F  01 09 00 0F 01 73 30 33  ..R..........s03
1230: 37 45 08 80 F0 FF FF 7F  F0 FF FF 7F 73 31 30 33  7E..........s103
1240: 01 80 29 0B 52 00 0F 01  80 2A 0B 57 00 0F 01 2A  ..).R....*.W...*
1250: 0B 56 00 0F 01 4A 56 00  0F 01 57 00 0F 01 4A 57  .V...JV...W...JW
1260: 00 0F 01 56 00 0F 01 1C  07 80 45 08 80 09 00 0F  ...V......E.....
1270: 01 09 00 0F 01 73 30 33  38 01 80 27 08 53 00 0F  .....s038..'.S..
1280: 01 12 27 08 54 00 0F 01  10 4A 57 00 0F 01 52 00  ..'.T....JW...R.
1290: 0F 01 4A 56 00 0F 01 52  00 0F 01 29 0B 52 00 0F  ..JV...R...).R..
12A0: 01 81 29 0B 52 00 0F 01  82 45 08 80 09 00 0F 01  ..).R....E......
12B0: 09 00 0F 01 73 30 33 39  01 80 27 0B 52 00 0F 01  ....s039..'.R...
12C0: 77 2B 52 00 0F 01 2C 80  23 2A 0B 52 00 0F 01 55  w+R...,.#*.R...U
12D0: 08 80 09 00 0F 01 09 00  0F 01 73 30 33 39 45 09  ..........s039E.
12E0: 80 09 00 0F 01 09 00 0F  01 66 64 6F 31 01 80 1C  .........fdo1...
12F0: 10 80 2A 08 53 00 0F 01  2A 08 54 00 0F 01 29 0B  ..*.S...*.T...).
1300: 52 00 0F 01 85 29 0B 53  00 0F 01 3A 29 0B 54 00  R....).S...:).T.
1310: 0F 01 44 29 0B 55 00 0F  01 3B 29 0B 56 00 0F 01  ..D).U...;).V...
1320: 32 29 0B 57 00 0F 01 35  29 0B F0 FF FF 7F 4A 29  2).W...5).....J)
1330: 0B 5B 00 0F 01 09 22 00  80 5B 00 0F 01 1C 09 80  .[...."..[......
1340: 45 08 80 09 00 0F 01 09  00 0F 01 73 30 36 39 01  E..........s069.
1350: 80 45 09 80 09 00 0F 01  09 00 0F 01 66 64 69 31  .E..........fdi1
1360: 01 80 55 08 80 09 00 0F  01 09 00 0F 01 73 30 36  ..U..........s06
1370: 39 45 08 80 09 00 0F 01  09 00 0F 01 73 30 37 34  9E..........s074
1380: 01 80 29 0B 52 00 0F 01  8A 45 08 80 09 00 0F 01  ..).R....E......
1390: 09 00 0F 01 73 30 37 30  01 80 27 0B 52 00 0F 01  ....s070..'.R...
13A0: 89 2B 52 00 0F 01 2D 80  23 2A 0B 52 00 0F 01 29  .+R...-.#*.R...)
13B0: 0B 54 00 0F 01 48 4A 57  00 0F 01 56 00 0F 01 29  .T...HJW...V...)
13C0: 0B 57 00 0F 01 39 52 08  80 09 00 0F 01 09 00 0F  .W...9R.........
13D0: 01 73 30 37 30 45 08 80  09 00 0F 01 09 00 0F 01  .s070E..........
13E0: 73 30 37 31 01 80 4A F0  FF FF 7F 53 00 0F 01 4A  s071..J....S...J
13F0: 52 00 0F 01 53 00 0F 01  27 0B 53 00 0F 01 3C 2B  R...S...'.S...<+
1400: 53 00 0F 01 2E 80 23 1C  1F 80 4A 54 00 0F 01 53  S.....#...JT...S
1410: 00 0F 01 4A 57 00 0F 01  53 00 0F 01 1C 1F 80 2B  ...JW...S......+
1420: 53 00 0F 01 2F 80 23 2A  0B 53 00 0F 01 4A 56 00  S.../.#*.S...JV.
1430: 0F 01 53 00 0F 01 4A 55  00 0F 01 53 00 0F 01 52  ..S...JU...S...R
1440: 08 80 09 00 0F 01 09 00  0F 01 73 30 37 31 45 08  ..........s071E.
1450: 80 09 00 0F 01 09 00 0F  01 73 30 37 39 01 80 5D  .........s079..]
1460: 01 80 07 80 4B 53 00 0F  01 30 80 7B 53 00 0F 01  ....KS...0.{S...
1470: 1C 07 80 45 08 80 09 00  0F 01 09 00 0F 01 73 30  ...E..........s0
1480: 37 32 01 80 27 0B 53 00  0F 01 3D 2B 53 00 0F 01  72..'.S...=+S...
1490: 31 80 23 1C 1F 80 4A F0  FF FF 7F 53 00 0F 01 4A  1.#...J....S...J
14A0: 56 00 0F 01 53 00 0F 01  4A 52 00 0F 01 53 00 0F  V...S...JR...S..
14B0: 01 4A 55 00 0F 01 53 00  0F 01 45 08 80 09 00 0F  .JU...S...E.....
14C0: 01 09 00 0F 01 73 30 37  36 01 80 1C 32 80 27 08  .....s076...2.'.
14D0: 57 00 0F 01 07 4A F0 FF  FF 7F 53 00 0F 01 4A 56  W....J....S...JV
14E0: 00 0F 01 53 00 0F 01 4A  52 00 0F 01 53 00 0F 01  ...S...JR...S...
14F0: 4A 55 00 0F 01 53 00 0F  01 1C 32 80 4A F0 FF FF  JU...S....2.J...
1500: 7F 53 00 0F 01 4A 56 00  0F 01 53 00 0F 01 4A 52  .S...JV...S...JR
1510: 00 0F 01 53 00 0F 01 4A  55 00 0F 01 53 00 0F 01  ...S...JU...S...
1520: 1C 32 80 27 08 56 00 0F  01 06 4A 52 00 0F 01 53  .2.'.V....JR...S
1530: 00 0F 01 52 08 80 09 00  0F 01 09 00 0F 01 73 30  ...R..........s0
1540: 37 36 45 08 80 09 00 0F  01 09 00 0F 01 73 30 37  76E..........s07
1550: 35 01 80 29 0B 54 00 0F  01 47 2A 08 57 00 0F 01  5..).T...G*.W...
1560: 2A 08 56 00 0F 01 2A 0B  55 00 0F 01 2A 0B 53 00  *.V...*.U...*.S.
1570: 0F 01 4A 55 00 0F 01 5B  00 0F 01 29 08 53 00 0F  ..JU...[...).S..
1580: 01 12 29 0B 53 00 0F 01  40 29 08 54 00 0F 01 07  ..).S...@).T....
1590: 45 08 80 09 00 0F 01 09  00 0F 01 73 30 37 37 01  E..........s077.
15A0: 80 5D 05 80 07 80 4A F0  FF FF 7F 55 00 0F 01 27  .]....J....U...'
15B0: 0B 55 00 0F 01 3C 29 0B  52 00 0F 01 8B 2B 55 00  .U...<).R....+U.
15C0: 0F 01 33 80 23 4A 52 00  0F 01 55 00 0F 01 1C 1A  ..3.#JR...U.....
15D0: 80 29 08 52 00 0F 01 0E  29 08 52 00 0F 01 0F 29  .).R....).R....)
15E0: 08 54 00 0F 01 08 45 08  80 09 00 0F 01 09 00 0F  .T....E.........
15F0: 01 73 30 37 33 01 80 1C  1A 80 29 0B 52 00 0F 01  .s073.....).R...
1600: 87 29 0B 52 00 0F 01 8C  2A 0B 55 00 0F 01 4A 55  .).R....*.U...JU
1610: 00 0F 01 52 00 0F 01 29  0B 55 00 0F 01 41 29 0B  ...R...).U...A).
1620: 52 00 0F 01 8D 4B 55 00  0F 01 34 80 1C 1A 80 27  R....KU...4....'
1630: 0B 55 00 0F 01 3D 1C 1A  80 45 08 80 09 00 0F 01  .U...=...E......
1640: 09 00 0F 01 73 30 38 30  01 80 2B 55 00 0F 01 35  ....s080..+U...5
1650: 80 23 2A 0B 55 00 0F 01  7B 55 00 0F 01 27 0B 52  .#*.U...{U...'.R
1660: 00 0F 01 88 4A 52 00 0F  01 5B 00 0F 01 4A 55 00  ....JR...[...JU.
1670: 0F 01 5B 00 0F 01 2B 52  00 0F 01 36 80 23 2A 0B  ..[...+R...6.#*.
1680: 52 00 0F 01 1C 1F 80 45  08 80 09 00 0F 01 09 00  R......E........
1690: 0F 01 73 30 38 32 01 80  4A 52 00 0F 01 55 00 0F  ..s082..JR...U..
16A0: 01 5D 01 80 09 80 4E 00  5B 00 0F 01 29 08 5B 00  .]....N.[...).[.
16B0: 0F 01 05 2C 55 00 0F 01  55 00 0F 01 77 6F 6E 34  ...,U...U...won4
16C0: 29 08 55 00 0F 01 11 2B  55 00 0F 01 37 80 23 29  ).U....+U...7.#)
16D0: 08 55 00 0F 01 12 62 38  80 55 00 0F 01 5B 00 0F  .U....b8.U...[..
16E0: 01 6D 61 69 6E 01 80 1C  07 80 29 0B 52 00 0F 01  .main.....).R...
16F0: 8F 45 08 80 09 00 0F 01  09 00 0F 01 73 30 38 31  .E..........s081
1700: 01 80 2C 55 00 0F 01 55  00 0F 01 77 6F 66 34 62  ..,U...U...wof4b
1710: 38 80 55 00 0F 01 5B 00  0F 01 6D 61 69 31 01 80  8.U...[...mai1..
1720: 4A 52 00 0F 01 5B 00 0F  01 4A 55 00 0F 01 5B 00  JR...[...JU...[.
1730: 0F 01 29 08 55 00 0F 01  15 1C 07 80 52 08 80 09  ..).U.......R...
1740: 00 0F 01 09 00 0F 01 73  30 38 31 45 08 80 09 00  .......s081E....
1750: 0F 01 09 00 0F 01 73 30  38 33 01 80 29 08 5B 00  ......s083..).[.
1760: 0F 01 06 29 08 52 00 0F  01 0C 29 08 54 00 0F 01  ...).R....).T...
1770: 10 29 0B 52 00 0F 01 86  5C 00 04 80 5C 01 04 80  .).R....\...\...
1780: 5D 05 80 07 80 1C 10 80  55 08 80 09 00 0F 01 09  ].......U.......
1790: 00 0F 01 73 30 38 33 45  08 80 09 00 0F 01 09 00  ...s083E........
17A0: 0F 01 73 30 38 34 01 80  29 0B 52 00 0F 01 84 29  ..s084..).R....)
17B0: 08 5B 00 0F 01 07 29 0B  55 00 0F 01 44 52 08 80  .[....).U...DR..
17C0: 09 00 0F 01 09 00 0F 01  73 30 38 34 45 08 80 09  ........s084E...
17D0: 00 0F 01 09 00 0F 01 73  30 38 35 01 80 29 0B 5B  .......s085..).[
17E0: 00 0F 01 0A 29 0B 55 00  0F 01 45 1C 07 80 45 08  ....).U...E...E.
17F0: 80 09 00 0F 01 09 00 0F  01 73 30 38 37 01 80 29  .........s087..)
1800: 08 55 00 0F 01 03 2B 55  00 0F 01 39 80 23 29 08  .U....+U...9.#).
1810: 55 00 0F 01 04 29 08 55  00 0F 01 05 29 08 55 00  U....).U....).U.
1820: 0F 01 06 29 0B 55 00 0F  01 46 29 0B 55 00 0F 01  ...).U...F).U...
1830: 47 45 08 80 09 00 0F 01  09 00 0F 01 73 30 38 36  GE..........s086
1840: 01 80 1C 07 80 29 0B 5B  00 0F 01 0D 45 09 80 09  .....).[....E...
1850: 00 0F 01 09 00 0F 01 66  64 6F 31 01 80 1C 10 80  .......fdo1.....
1860: 1C 07 80 29 0B 5B 00 0F  01 0E 45 08 80 09 00 0F  ...).[....E.....
1870: 01 09 00 0F 01 73 30 34  31 01 80 27 0B 53 00 0F  .....s041..'.S..
1880: 01 41 27 0B 54 00 0F 01  49 27 0B F0 FF FF 7F 4C  .A'.T...I'.....L
1890: 27 0B 57 00 0F 01 3A 27  0B 56 00 0F 01 34 27 0B  '.W...:'.V...4'.
18A0: 5B 00 0F 01 0F 27 0B 55  00 0F 01 48 27 0D 52 00  [....'.U...H'.R.
18B0: 0F 01 90 4C 45 09 80 09  00 0F 01 09 00 0F 01 66  ...LE..........f
18C0: 64 69 31 01 80 2B 52 00  0F 01 3A 80 23 1C 10 80  di1..+R...:.#...
18D0: 55 08 80 09 00 0F 01 09  00 0F 01 73 30 34 31 2A  U..........s041*
18E0: 0B 56 00 0F 01 45 08 80  09 00 0F 01 09 00 0F 01  .V...E..........
18F0: 73 30 34 33 01 80 4E 01  F0 FF FF 7F 4D 29 0B 52  s043..N.....M).R
1900: 00 0F 01 92 29 0B 53 00  0F 01 43 4A 54 00 0F 01  ....).S...CJT...
1910: 53 00 0F 01 29 0B 54 00  0F 01 4B 2A 0D 52 00 0F  S...).T...K*.R..
1920: 01 2A 0B 53 00 0F 01 2A  0B 54 00 0F 01 4A 52 00  .*.S...*.T...JR.
1930: 0F 01 55 00 0F 01 4A 53  00 0F 01 52 00 0F 01 4A  ..U...JS...R...J
1940: 54 00 0F 01 52 00 0F 01  4A 57 00 0F 01 52 00 0F  T...R...JW...R..
1950: 01 4A 56 00 0F 01 52 00  0F 01 4A 55 00 0F 01 52  .JV...R...JU...R
1960: 00 0F 01 29 0B 52 00 0F  01 93 52 08 80 09 00 0F  ...).R....R.....
1970: 01 09 00 0F 01 73 30 34  33 45 08 80 09 00 0F 01  .....s043E......
1980: 09 00 0F 01 73 30 35 31  01 80 02 01 00 01 80 00  ....s051........
1990: 9B 19 4E 00 F0 FF FF 7F  01 9B 19 29 0B 52 00 0F  ..N........).R..
19A0: 01 94 27 08 54 00 0F 01  05 27 08 53 00 0F 01 09  ..'.T....'.S....
19B0: 27 08 57 00 0F 01 03 27  08 56 00 0F 01 03 29 0B  '.W....'.V....).
19C0: 53 00 0F 01 4A 29 0B 54  00 0F 01 3F 29 0B 57 00  S...J).T...?).W.
19D0: 0F 01 45 29 0B 56 00 0F  01 3E 2A 08 54 00 0F 01  ..E).V...>*.T...
19E0: 2A 08 53 00 0F 01 2A 08  57 00 0F 01 2A 08 56 00  *.S...*.W...*.V.
19F0: 0F 01 29 08 54 00 0F 01  06 29 08 53 00 0F 01 0A  ..).T....).S....
1A00: 29 08 57 00 0F 01 04 29  08 56 00 0F 01 04 45 08  ).W....).V....E.
1A10: 80 09 00 0F 01 09 00 0F  01 73 30 34 34 01 80 27  .........s044..'
1A20: 0B 52 00 0F 01 91 27 0B  53 00 0F 01 42 27 0B 54  .R....'.S...B'.T
1A30: 00 0F 01 4A 27 0B F0 FF  FF 7F 4D 27 0B 56 00 0F  ...J'.....M'.V..
1A40: 01 35 27 0B 57 00 0F 01  3B 29 0B 55 00 0F 01 4A  .5'.W...;).U...J
1A50: 29 0B 55 00 0F 01 4D 45  08 80 09 00 0F 01 09 00  ).U...ME........
1A60: 0F 01 73 30 34 35 01 80  29 0B 55 00 0F 01 4B 55  ..s045..).U...KU
1A70: 08 80 09 00 0F 01 09 00  0F 01 73 30 34 35 4A 55  ..........s045JU
1A80: 00 0F 01 5B 00 0F 01 29  0B 55 00 0F 01 4E 4A 5B  ...[...).U...NJ[
1A90: 00 0F 01 55 00 0F 01 4B  5B 00 0F 01 3B 80 45 08  ...U...K[...;.E.
1AA0: 80 09 00 0F 01 09 00 0F  01 73 30 34 37 01 80 29  .........s047..)
1AB0: 0B 5B 00 0F 01 15 55 08  80 09 00 0F 01 09 00 0F  .[....U.........
1AC0: 01 73 30 34 37 45 08 80  09 00 0F 01 09 00 0F 01  .s047E..........
1AD0: 73 30 34 36 01 80 29 0B  5B 00 0F 01 12 29 0B 55  s046..).[....).U
1AE0: 00 0F 01 4F 4A 5B 00 0F  01 55 00 0F 01 45 08 80  ...OJ[...U...E..
1AF0: 09 00 0F 01 09 00 0F 01  73 30 34 38 01 80 29 0B  ........s048..).
1B00: 5B 00 0F 01 13 1C 07 80  45 08 80 09 00 0F 01 09  [.......E.......
1B10: 00 0F 01 73 30 34 36 01  80 29 0B 55 00 0F 01 50  ...s046..).U...P
1B20: 45 08 80 09 00 0F 01 09  00 0F 01 73 30 35 30 01  E..........s050.
1B30: 80 27 0B 55 00 0F 01 4C  1C 1F 80 29 0B 5B 00 0F  .'.U...L...).[..
1B40: 01 14 45 08 80 09 00 0F  01 09 00 0F 01 73 30 35  ..E..........s05
1B50: 32 01 80 2A 0B 55 00 0F  01 4A 55 00 0F 01 5B 00  2..*.U...JU...[.
1B60: 0F 01 29 0B 55 00 0F 01  51 29 0B 5B 00 0F 01 15  ..).U...Q).[....
1B70: 2B 5B 00 0F 01 3C 80 23  45 08 80 09 00 0F 01 09  +[...<.#E.......
1B80: 00 0F 01 73 30 34 39 01  80 27 0B 5B 00 0F 01 11  ...s049..'.[....
1B90: 55 08 80 09 00 0F 01 09  00 0F 01 73 30 34 39 45  U..........s049E
1BA0: 09 80 09 00 0F 01 09 00  0F 01 66 64 6F 31 01 80  ..........fdo1..
1BB0: 1C 10 80 2A 0B 5B 00 0F  01 2A 0B 52 00 0F 01 2A  ...*.[...*.R...*
1BC0: 0B 53 00 0F 01 2A 0B 54  00 0F 01 2A 0B 56 00 0F  .S...*.T...*.V..
1BD0: 01 2A 0B 57 00 0F 01 5C  00 20 80 5C 01 20 80 5D  .*.W...\. .\. .]
1BE0: 05 80 00 80 1C 11 80 7B  52 00 0F 01 02 01 00 01  .......{R.......
1BF0: 80 00 F7 1B 01 01 1C 4E  00 A4 00 0F 01 38 22 80  .......N.....8".
1C00: 78 00                                             x.              
```

#### Opcodes

```
  0: 0x0AE6 [0x03] ExtData[1]->WorkLocal[1] = 1*
  1: 0x0AEB [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0AF9
  2: 0x0AF3 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  3: 0x0AF6 [0x01] GOTO 0x0B07
  4: 0x0AF9 [0x77] SET_EVENT_TIME_WEATHER(hour=12*, weather=0*)
  5: 0x0AFE [0x4E] SET_ENTITY_HIDE_FLAG: Hide Unnamed NPC (ID: 17760420/0x010F00A4)
  6: 0x0B04 [0x38] SET_CLIENT_EVENT_MODE(mode=2067*)

SUBROUTINE_0B07:
  7: 0x0B07 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x41)
  8: 0x0B0E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x05)
  9: 0x0B15 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 123*
 10: 0x0B19 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 123*
 11: 0x0B1D [0x1C] WAIT(100* ticks)
 12: 0x0B20 [0x4E] SET_ENTITY_HIDE_FLAG: Show Kohlo-Lakolo (ID: 17760338/0x010F0052)
 13: 0x0B26 [0x4E] SET_ENTITY_HIDE_FLAG: Show Papo-Hopo (ID: 17760339/0x010F0053)
 14: 0x0B2C [0x4E] SET_ENTITY_HIDE_FLAG: Show Gomada-Vulmada (ID: 17760340/0x010F0054)
 15: 0x0B32 [0x4E] SET_ENTITY_HIDE_FLAG: Show Yafa Yaa (ID: 17760342/0x010F0056)
 16: 0x0B38 [0x4E] SET_ENTITY_HIDE_FLAG: Show Pyo Nzon (ID: 17760343/0x010F0057)
 17: 0x0B3E [0x4E] SET_ENTITY_HIDE_FLAG: Show Pichichi (ID: 17760341/0x010F0055)
 18: 0x0B44 [0x80] LOAD_WAIT(entity=Kohlo-Lakolo (ID: 17760338/0x010F0052))
 19: 0x0B49 [0x80] LOAD_WAIT(entity=Papo-Hopo (ID: 17760339/0x010F0053))
 20: 0x0B4E [0x80] LOAD_WAIT(entity=Gomada-Vulmada (ID: 17760340/0x010F0054))
 21: 0x0B53 [0x80] LOAD_WAIT(entity=Yafa Yaa (ID: 17760342/0x010F0056))
 22: 0x0B58 [0x80] LOAD_WAIT(entity=Pyo Nzon (ID: 17760343/0x010F0057))
 23: 0x0B5D [0x80] LOAD_WAIT(entity=Pichichi (ID: 17760341/0x010F0055))
 24: 0x0B62 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "wof4" with entities [Pichichi (ID: 17760341/0x010F0055), Pichichi (ID: 17760341/0x010F0055)]
 25: 0x0B6F [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0BCD
 26: 0x0B77 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s055" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 27: 0x0B88 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
 28: 0x0B99 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3989*]:
    → "Ahoy! Ahoy!"
 29: 0x0BA0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0BA1 [0x4A] LocalPlayer looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
 31: 0x0BAA [0x52] END_LOAD_SCHEDULER: End scheduler "s055" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
 32: 0x0BB9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s053" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 33: 0x0BCA [0x01] GOTO 0x0BEF
 34: 0x0BCD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s053" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 35: 0x0BDE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]

SUBROUTINE_0BEF:
 36: 0x0BEF [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x97)
 37: 0x0BF6 [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x46)
 38: 0x0BFD [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x3A)
 39: 0x0C04 [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x39)
 40: 0x0C0B [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x3F)
 41: 0x0C12 [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x54)
 42: 0x0C19 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
 43: 0x0C1F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s053" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
 44: 0x0C2E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s104" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 45: 0x0C3F [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
 46: 0x0C45 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
 47: 0x0C4B [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
 48: 0x0C51 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
 49: 0x0C57 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
 50: 0x0C5D [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0C8A
 51: 0x0C65 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3990*]:
    → "Good! Now that we're all here, it's time for the final showdown with that Cat Burglar!"
 52: 0x0C6C [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x0C6D [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
 54: 0x0C76 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s054" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 55: 0x0C87 [0x01] GOTO 0x0C93
 56: 0x0C8A [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)

SUBROUTINE_0C93:
 57: 0x0C93 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3991*]:
    → "Star Onion Brigade, are you ready already? Then CHAAAA`RRGE!"
 58: 0x0C9A [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0C9B [0x27] REQ_SET(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x05)
 60: 0x0CA2 [0x27] REQ_SET(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x09)
 61: 0x0CA9 [0x27] REQ_SET(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x03)
 62: 0x0CB0 [0x27] REQ_SET(priority=0x08, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x03)
 63: 0x0CB7 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x4A)
 64: 0x0CBE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x3F)
 65: 0x0CC5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x3E)
 66: 0x0CCC [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x45)
 67: 0x0CD3 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
 68: 0x0CD9 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
 69: 0x0CDF [0x2A] GET_REQ_LEVEL(level=8, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
 70: 0x0CE5 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
 71: 0x0CEB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x06)
 72: 0x0CF2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x0A)
 73: 0x0CF9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x04)
 74: 0x0D00 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x04)
 75: 0x0D07 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
 76: 0x0D18 [0x1C] WAIT(60* ticks)
 77: 0x0D1B [0x4C] EventEntity->StatusEvent = 8 // Open door
 78: 0x0D1C [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0D2A
 79: 0x0D24 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 80: 0x0D27 [0x01] GOTO 0x0D2D
 81: 0x0D2A [0x38] SET_CLIENT_EVENT_MODE(mode=2067*)

SUBROUTINE_0D2D:
 82: 0x0D2D [0x1C] WAIT(200* ticks)
 83: 0x0D30 [0x4D] EventEntity->StatusEvent = 9 // Close door
 84: 0x0D31 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x46)
 85: 0x0D38 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x19)
 86: 0x0D3F [0x1C] WAIT(30* ticks)
 87: 0x0D42 [0x4E] SET_ENTITY_HIDE_FLAG: Show Nanaa Mihgo (ID: 17760346/0x010F005A)
 88: 0x0D48 [0x80] LOAD_WAIT(entity=Nanaa Mihgo (ID: 17760346/0x010F005A))
 89: 0x0D4D [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x75)
 90: 0x0D54 [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x37)
 91: 0x0D5B [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x42)
 92: 0x0D62 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s026" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
 93: 0x0D73 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
 94: 0x0D84 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [3992*]:
    → "Ta-da`! The Star Onion Brigade is on the scene!"
 95: 0x0D8B [0x23] WAIT_FOR_DIALOG_INTERACTION
 96: 0x0D8C [0x4B] UPDATE_ENTITY_YAW(entity=Nanaa Mihgo (ID: 17760346/0x010F005A), yaw=11.0°*)
 97: 0x0D93 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
 98: 0x0DA4 [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x38)
 99: 0x0DAB [0x52] END_LOAD_SCHEDULER: End scheduler "s026" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
100: 0x0DBA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s028" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
101: 0x0DCB [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x47)
102: 0x0DD2 [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x2D)
103: 0x0DD9 [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x2F)
104: 0x0DE0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
105: 0x0DF1 [0x1C] WAIT(50* ticks)
106: 0x0DF4 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0E02
107: 0x0DFC [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
108: 0x0E02 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x48)
109: 0x0E09 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
110: 0x0E0F [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
111: 0x0E15 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
112: 0x0E1B [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
113: 0x0E21 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
114: 0x0E27 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s028" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
115: 0x0E36 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s040" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
116: 0x0E47 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x7A)
117: 0x0E4E [0x2A] GET_REQ_LEVEL(level=11, entity_id=LocalPlayer)
118: 0x0E54 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s027" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
119: 0x0E65 [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x1A)
120: 0x0E6C [0x2B] Nanaa Mihgo (ID: 17760346/0x010F005A) [3995*]:
    → "Not you brrrats again! Don't you have betterrr things to do all day than to rrrub my furrr the wrrrong way?"
121: 0x0E73 [0x23] WAIT_FOR_DIALOG_INTERACTION
122: 0x0E74 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
123: 0x0E7A [0x4A] Nanaa Mihgo (ID: 17760346/0x010F005A) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
124: 0x0E83 [0x52] END_LOAD_SCHEDULER: End scheduler "s027" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
125: 0x0E92 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s106" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
126: 0x0EA3 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x7B)
127: 0x0EAA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s029" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
128: 0x0EBB [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x1F)
129: 0x0EC2 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Papo-Hopo (ID: 17760339/0x010F0053)
130: 0x0ECB [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
131: 0x0ED4 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x7C)
132: 0x0EDB [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x39)
133: 0x0EE2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s030" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
134: 0x0EF3 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
135: 0x0EFC [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
136: 0x0F05 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x49)
137: 0x0F0C [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x38)
138: 0x0F13 [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x43)
139: 0x0F1A [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x3A)
140: 0x0F21 [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x30)
141: 0x0F28 [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x33)
142: 0x0F2F [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x1B)
143: 0x0F36 [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x78)
144: 0x0F3D [0x2B] Nanaa Mihgo (ID: 17760346/0x010F005A) [4002*]:
    → "Then allow me to fill you in. The ministerrr of the Orastery is trying to revive "summoning magic"--the verrry magic that the Star Sibyl has forrrbidden."
145: 0x0F44 [0x23] WAIT_FOR_DIALOG_INTERACTION
146: 0x0F45 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A))
147: 0x0F4B [0x4A] LocalPlayer looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
148: 0x0F54 [0x52] END_LOAD_SCHEDULER: End scheduler "s030" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
149: 0x0F63 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s031" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
150: 0x0F74 [0x4A] Nanaa Mihgo (ID: 17760346/0x010F005A) looks at Pichichi (ID: 17760341/0x010F0055)
151: 0x0F7D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x20)
152: 0x0F84 [0x7B] Nanaa Mihgo (ID: 17760346/0x010F005A) stops talking
153: 0x0F89 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x21)
154: 0x0F90 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x7D)
155: 0x0F97 [0x52] END_LOAD_SCHEDULER: End scheduler "s031" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
156: 0x0FA6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s032" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
157: 0x0FB7 [0x4B] UPDATE_ENTITY_YAW(entity=Nanaa Mihgo (ID: 17760346/0x010F005A), yaw=5.5°*)
158: 0x0FBE [0x1C] WAIT(30* ticks)
159: 0x0FC1 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x22)
160: 0x0FC8 [0x52] END_LOAD_SCHEDULER: End scheduler "s032" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
161: 0x0FD7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s033" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
162: 0x0FE8 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=300*)
163: 0x0FED [0x79] Nanaa Mihgo (ID: 17760346/0x010F005A) looks at Door:Doctor's Residence (ID: 17760348/0x010F005C) (Basic look)
164: 0x0FF7 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x1C)
165: 0x0FFE [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x38)
166: 0x1005 [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x43)
167: 0x100C [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x3A)
168: 0x1013 [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x30)
169: 0x101A [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x30)
170: 0x1021 [0x27] REQ_SET(priority=0x0D, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x78)
171: 0x1028 [0x4A] Nanaa Mihgo (ID: 17760346/0x010F005A) looks at Pyo Nzon (ID: 17760343/0x010F0057)
172: 0x1031 [0x4A] LocalPlayer looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
173: 0x103A [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x1D)
174: 0x1041 [0x1C] WAIT(30* ticks)
175: 0x1044 [0x4A] LocalPlayer looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
176: 0x104D [0x52] END_LOAD_SCHEDULER: End scheduler "s033" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
177: 0x105C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s034" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
178: 0x106D [0x4C] EventEntity->StatusEvent = 8 // Open door
179: 0x106E [0x2A] GET_REQ_LEVEL(level=13, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
180: 0x1074 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
181: 0x107A [0x2A] GET_REQ_LEVEL(level=11, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
182: 0x1080 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
183: 0x1086 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
184: 0x108C [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A))
185: 0x1092 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
186: 0x1098 [0x1C] WAIT(60* ticks)
187: 0x109B [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
188: 0x10A4 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
189: 0x10AD [0x1C] WAIT(60* ticks)
190: 0x10B0 [0x4D] EventEntity->StatusEvent = 9 // Close door
191: 0x10B1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s034" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
192: 0x10C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s102" with entities [LocalPlayer, LocalPlayer], work=[139*, 0*]
193: 0x10D1 [0x7B] Nanaa Mihgo (ID: 17760346/0x010F005A) stops talking
194: 0x10D6 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
195: 0x10DF [0x1C] WAIT(60* ticks)
196: 0x10E2 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at LocalPlayer
197: 0x10EB [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
198: 0x10F4 [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
199: 0x10FD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x7E)
200: 0x1104 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s035" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
201: 0x1115 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 161*
202: 0x1119 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 161*
203: 0x111D [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=60*)
204: 0x1122 [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x31)
205: 0x1129 [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x2E)
206: 0x1130 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
207: 0x1139 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
208: 0x1142 [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Nanaa Mihgo (ID: 17760346/0x010F005A)
209: 0x114B [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
210: 0x1151 [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
211: 0x115A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x31)
212: 0x1161 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
213: 0x1167 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x09)
214: 0x116E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x34)
215: 0x1175 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s036" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
216: 0x1186 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x0A)
217: 0x118D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x23)
218: 0x1194 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17760346/0x010F005A), tag_num=0x24)
219: 0x119B [0x7C] Pyo Nzon (ID: 17760343/0x010F0057)->Render.Flags2 |= 0x01
220: 0x11A1 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
221: 0x11AA [0x1C] WAIT(30* ticks)
222: 0x11AD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x38)
223: 0x11B4 [0x4A] LocalPlayer looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
224: 0x11BD [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
225: 0x11C6 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
226: 0x11CF [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
227: 0x11D8 [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
228: 0x11E1 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
229: 0x11EA [0x52] END_LOAD_SCHEDULER: End scheduler "s036" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
230: 0x11F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s037" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
231: 0x120A [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x32)
232: 0x1211 [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x2F)
233: 0x1218 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x7F)
234: 0x121F [0x1C] WAIT(300* ticks)
235: 0x1222 [0x52] END_LOAD_SCHEDULER: End scheduler "s037" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
236: 0x1231 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s103" with entities [LocalPlayer, LocalPlayer], work=[139*, 0*]
237: 0x1242 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x80)
238: 0x1249 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
239: 0x124F [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
240: 0x1255 [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Pyo Nzon (ID: 17760343/0x010F0057)
241: 0x125E [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Yafa Yaa (ID: 17760342/0x010F0056)
242: 0x1267 [0x1C] WAIT(100* ticks)
243: 0x126A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s038" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
244: 0x127B [0x27] REQ_SET(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x12)
245: 0x1282 [0x27] REQ_SET(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x10)
246: 0x1289 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
247: 0x1292 [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
248: 0x129B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x81)
249: 0x12A2 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x82)
250: 0x12A9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s039" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
251: 0x12BA [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x77)
252: 0x12C1 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [4019*]:
    → "Th-there's got to be a perfectly reasonable explanation for this! L-let's check out where the s-sound came from...e-everyone!"
253: 0x12C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
254: 0x12C9 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
255: 0x12CF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s039" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
256: 0x12DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
257: 0x12EF [0x1C] WAIT(60* ticks)
258: 0x12F2 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
259: 0x12F8 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
260: 0x12FE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x85)
261: 0x1305 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x3A)
262: 0x130C [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x44)
263: 0x1313 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x3B)
264: 0x131A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x32)
265: 0x1321 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x35)
266: 0x1328 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x4A)
267: 0x132F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x09)
268: 0x1336 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
269: 0x1338 [0x80] LOAD_WAIT(entity=Joker (ID: 17760347/0x010F005B))
270: 0x133D [0x1C] WAIT(200* ticks)
271: 0x1340 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s069" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
272: 0x1351 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
273: 0x1362 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s069" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
274: 0x1371 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s074" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
275: 0x1382 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x8A)
276: 0x1389 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s070" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
277: 0x139A [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x89)
278: 0x13A1 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [4021*]:
    → "The sound we heard was just the wind blowing in from there..."
279: 0x13A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
280: 0x13A9 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
281: 0x13AF [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x48)
282: 0x13B6 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Yafa Yaa (ID: 17760342/0x010F0056)
283: 0x13BF [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x39)
284: 0x13C6 [0x52] END_LOAD_SCHEDULER: End scheduler "s070" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
285: 0x13D5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s071" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
286: 0x13E6 [0x4A] LocalPlayer looks at Papo-Hopo (ID: 17760339/0x010F0053)
287: 0x13EF [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Papo-Hopo (ID: 17760339/0x010F0053)
288: 0x13F8 [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x3C)
289: 0x13FF [0x2B] Papo-Hopo (ID: 17760339/0x010F0053) [4024*]:
    → "So da ghosty's twue identity was just da wind!"
290: 0x1406 [0x23] WAIT_FOR_DIALOG_INTERACTION
291: 0x1407 [0x1C] WAIT(50* ticks)
292: 0x140A [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Papo-Hopo (ID: 17760339/0x010F0053)
293: 0x1413 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Papo-Hopo (ID: 17760339/0x010F0053)
294: 0x141C [0x1C] WAIT(50* ticks)
295: 0x141F [0x2B] Papo-Hopo (ID: 17760339/0x010F0053) [4025*]:
    → "It's pwetty dark and hard to tell, but if dere are a lot of gaps in da walls, den dey might give us a clue to get out of here!"
296: 0x1426 [0x23] WAIT_FOR_DIALOG_INTERACTION
297: 0x1427 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
298: 0x142D [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Papo-Hopo (ID: 17760339/0x010F0053)
299: 0x1436 [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Papo-Hopo (ID: 17760339/0x010F0053)
300: 0x143F [0x52] END_LOAD_SCHEDULER: End scheduler "s071" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
301: 0x144E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s079" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
302: 0x145F [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=100*)
303: 0x1464 [0x4B] UPDATE_ENTITY_YAW(entity=Papo-Hopo (ID: 17760339/0x010F0053), yaw=16.9°*)
304: 0x146B [0x7B] Papo-Hopo (ID: 17760339/0x010F0053) stops talking
305: 0x1470 [0x1C] WAIT(100* ticks)
306: 0x1473 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s072" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
307: 0x1484 [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x3D)
308: 0x148B [0x2B] Papo-Hopo (ID: 17760339/0x010F0053) [4026*]:
    → "Arrrrrgggghhhyaaaa!!!"
309: 0x1492 [0x23] WAIT_FOR_DIALOG_INTERACTION
310: 0x1493 [0x1C] WAIT(50* ticks)
311: 0x1496 [0x4A] LocalPlayer looks at Papo-Hopo (ID: 17760339/0x010F0053)
312: 0x149F [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Papo-Hopo (ID: 17760339/0x010F0053)
313: 0x14A8 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Papo-Hopo (ID: 17760339/0x010F0053)
314: 0x14B1 [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Papo-Hopo (ID: 17760339/0x010F0053)
315: 0x14BA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s076" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
316: 0x14CB [0x1C] WAIT(15* ticks)
317: 0x14CE [0x27] REQ_SET(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x07)
318: 0x14D5 [0x4A] LocalPlayer looks at Papo-Hopo (ID: 17760339/0x010F0053)
319: 0x14DE [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Papo-Hopo (ID: 17760339/0x010F0053)
320: 0x14E7 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Papo-Hopo (ID: 17760339/0x010F0053)
321: 0x14F0 [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Papo-Hopo (ID: 17760339/0x010F0053)
322: 0x14F9 [0x1C] WAIT(15* ticks)
323: 0x14FC [0x4A] LocalPlayer looks at Papo-Hopo (ID: 17760339/0x010F0053)
324: 0x1505 [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Papo-Hopo (ID: 17760339/0x010F0053)
325: 0x150E [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Papo-Hopo (ID: 17760339/0x010F0053)
326: 0x1517 [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Papo-Hopo (ID: 17760339/0x010F0053)
327: 0x1520 [0x1C] WAIT(15* ticks)
328: 0x1523 [0x27] REQ_SET(priority=0x08, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x06)
329: 0x152A [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Papo-Hopo (ID: 17760339/0x010F0053)
330: 0x1533 [0x52] END_LOAD_SCHEDULER: End scheduler "s076" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
331: 0x1542 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s075" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
332: 0x1553 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x47)
333: 0x155A [0x2A] GET_REQ_LEVEL(level=8, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
334: 0x1560 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
335: 0x1566 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
336: 0x156C [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
337: 0x1572 [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Joker (ID: 17760347/0x010F005B)
338: 0x157B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x12)
339: 0x1582 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x40)
340: 0x1589 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x07)
341: 0x1590 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s077" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
342: 0x15A1 [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=100*)
343: 0x15A6 [0x4A] LocalPlayer looks at Pichichi (ID: 17760341/0x010F0055)
344: 0x15AF [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x3C)
345: 0x15B6 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x8B)
346: 0x15BD [0x2B] Pichichi (ID: 17760341/0x010F0055) [4030*]:
    → "You mean ath in...a dead body!?"
347: 0x15C4 [0x23] WAIT_FOR_DIALOG_INTERACTION
348: 0x15C5 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
349: 0x15CE [0x1C] WAIT(30* ticks)
350: 0x15D1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x0E)
351: 0x15D8 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x0F)
352: 0x15DF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x08)
353: 0x15E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s073" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
354: 0x15F7 [0x1C] WAIT(30* ticks)
355: 0x15FA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x87)
356: 0x1601 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x8C)
357: 0x1608 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
358: 0x160E [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
359: 0x1617 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x41)
360: 0x161E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x8D)
361: 0x1625 [0x4B] UPDATE_ENTITY_YAW(entity=Pichichi (ID: 17760341/0x010F0055), yaw=11.8°*)
362: 0x162C [0x1C] WAIT(30* ticks)
363: 0x162F [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x3D)
364: 0x1636 [0x1C] WAIT(30* ticks)
365: 0x1639 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s080" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
366: 0x164A [0x2B] Pichichi (ID: 17760341/0x010F0055) [4034*]:
    → "But a ghothty ith an undead body, not a dead body, right?"
367: 0x1651 [0x23] WAIT_FOR_DIALOG_INTERACTION
368: 0x1652 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
369: 0x1658 [0x7B] Pichichi (ID: 17760341/0x010F0055) stops talking
370: 0x165D [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x88)
371: 0x1664 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Joker (ID: 17760347/0x010F005B)
372: 0x166D [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Joker (ID: 17760347/0x010F005B)
373: 0x1676 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [4035*]:
    → "Um... Either way, I don't think it's wise to find out!"
374: 0x167D [0x23] WAIT_FOR_DIALOG_INTERACTION
375: 0x167E [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
376: 0x1684 [0x1C] WAIT(50* ticks)
377: 0x1687 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s082" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
378: 0x1698 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
379: 0x16A1 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
380: 0x16A6 [0x4E] SET_ENTITY_HIDE_FLAG: Show Joker (ID: 17760347/0x010F005B)
381: 0x16AC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x05)
382: 0x16B3 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "won4" with entities [Pichichi (ID: 17760341/0x010F0055), Pichichi (ID: 17760341/0x010F0055)]
383: 0x16C0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x11)
384: 0x16C7 [0x2B] Pichichi (ID: 17760341/0x010F0055) [4037*]:
    → "Huh...?"
385: 0x16CE [0x23] WAIT_FOR_DIALOG_INTERACTION
386: 0x16CF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x12)
387: 0x16D6 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Pichichi (ID: 17760341/0x010F0055), Joker (ID: 17760347/0x010F005B)], work=[13*, 0*]
388: 0x16E7 [0x1C] WAIT(100* ticks)
389: 0x16EA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x8F)
390: 0x16F1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s081" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
391: 0x1702 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "wof4" with entities [Pichichi (ID: 17760341/0x010F0055), Pichichi (ID: 17760341/0x010F0055)]
392: 0x170F [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "mai1" with entities [Pichichi (ID: 17760341/0x010F0055), Joker (ID: 17760347/0x010F005B)], work=[13*, 0*]
393: 0x1720 [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Joker (ID: 17760347/0x010F005B)
394: 0x1729 [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Joker (ID: 17760347/0x010F005B)
395: 0x1732 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x15)
396: 0x1739 [0x1C] WAIT(100* ticks)
397: 0x173C [0x52] END_LOAD_SCHEDULER: End scheduler "s081" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
398: 0x174B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s083" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
399: 0x175C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x06)
400: 0x1763 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x0C)
401: 0x176A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x10)
402: 0x1771 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x86)
403: 0x1778 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 120*
404: 0x177C [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 120*
405: 0x1780 [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=100*)
406: 0x1785 [0x1C] WAIT(60* ticks)
407: 0x1788 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s083" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
408: 0x1797 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s084" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
409: 0x17A8 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x84)
410: 0x17AF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x07)
411: 0x17B6 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x44)
412: 0x17BD [0x52] END_LOAD_SCHEDULER: End scheduler "s084" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
413: 0x17CC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s085" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
414: 0x17DD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x0A)
415: 0x17E4 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x45)
416: 0x17EB [0x1C] WAIT(100* ticks)
417: 0x17EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s087" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
418: 0x17FF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x03)
419: 0x1806 [0x2B] Pichichi (ID: 17760341/0x010F0055) [4042*]:
    → "And you are...?"
420: 0x180D [0x23] WAIT_FOR_DIALOG_INTERACTION
421: 0x180E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x04)
422: 0x1815 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x05)
423: 0x181C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x06)
424: 0x1823 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x46)
425: 0x182A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x47)
426: 0x1831 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s086" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
427: 0x1842 [0x1C] WAIT(100* ticks)
428: 0x1845 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x0D)
429: 0x184C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
430: 0x185D [0x1C] WAIT(60* ticks)
431: 0x1860 [0x1C] WAIT(100* ticks)
432: 0x1863 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x0E)
433: 0x186A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s041" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
434: 0x187B [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x41)
435: 0x1882 [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x49)
436: 0x1889 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x4C)
437: 0x1890 [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x3A)
438: 0x1897 [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x34)
439: 0x189E [0x27] REQ_SET(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x0F)
440: 0x18A5 [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x48)
441: 0x18AC [0x27] REQ_SET(priority=0x0D, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x90)
442: 0x18B3 [0x4C] EventEntity->StatusEvent = 8 // Open door
443: 0x18B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
444: 0x18C5 [0x2B] Kohlo-Lakolo (ID: 17760338/0x010F0052) [4048*]:
    → "Ye`ah! I'm glad to be out of there!"
445: 0x18CC [0x23] WAIT_FOR_DIALOG_INTERACTION
446: 0x18CD [0x1C] WAIT(60* ticks)
447: 0x18D0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s041" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
448: 0x18DF [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
449: 0x18E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s043" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
450: 0x18F6 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
451: 0x18FC [0x4D] EventEntity->StatusEvent = 9 // Close door
452: 0x18FD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x92)
453: 0x1904 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x43)
454: 0x190B [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Papo-Hopo (ID: 17760339/0x010F0053)
455: 0x1914 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x4B)
456: 0x191B [0x2A] GET_REQ_LEVEL(level=13, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
457: 0x1921 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
458: 0x1927 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
459: 0x192D [0x4A] Kohlo-Lakolo (ID: 17760338/0x010F0052) looks at Pichichi (ID: 17760341/0x010F0055)
460: 0x1936 [0x4A] Papo-Hopo (ID: 17760339/0x010F0053) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
461: 0x193F [0x4A] Gomada-Vulmada (ID: 17760340/0x010F0054) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
462: 0x1948 [0x4A] Pyo Nzon (ID: 17760343/0x010F0057) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
463: 0x1951 [0x4A] Yafa Yaa (ID: 17760342/0x010F0056) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
464: 0x195A [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Kohlo-Lakolo (ID: 17760338/0x010F0052)
465: 0x1963 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x93)
466: 0x196A [0x52] END_LOAD_SCHEDULER: End scheduler "s043" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
467: 0x1979 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s051" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
468: 0x198A [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x199B
469: 0x1992 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
470: 0x1998 [0x01] GOTO 0x199B

SUBROUTINE_199B:
471: 0x199B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x94)
472: 0x19A2 [0x27] REQ_SET(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x05)
473: 0x19A9 [0x27] REQ_SET(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x09)
474: 0x19B0 [0x27] REQ_SET(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x03)
475: 0x19B7 [0x27] REQ_SET(priority=0x08, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x03)
476: 0x19BE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x4A)
477: 0x19C5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x3F)
478: 0x19CC [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x45)
479: 0x19D3 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x3E)
480: 0x19DA [0x2A] GET_REQ_LEVEL(level=8, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
481: 0x19E0 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
482: 0x19E6 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
483: 0x19EC [0x2A] GET_REQ_LEVEL(level=8, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
484: 0x19F2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x06)
485: 0x19F9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x0A)
486: 0x1A00 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x04)
487: 0x1A07 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x04)
488: 0x1A0E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s044" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
489: 0x1A1F [0x27] REQ_SET(priority=0x0B, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052), tag_num=0x91)
490: 0x1A26 [0x27] REQ_SET(priority=0x0B, entity_id=Papo-Hopo (ID: 17760339/0x010F0053), tag_num=0x42)
491: 0x1A2D [0x27] REQ_SET(priority=0x0B, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054), tag_num=0x4A)
492: 0x1A34 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x4D)
493: 0x1A3B [0x27] REQ_SET(priority=0x0B, entity_id=Yafa Yaa (ID: 17760342/0x010F0056), tag_num=0x35)
494: 0x1A42 [0x27] REQ_SET(priority=0x0B, entity_id=Pyo Nzon (ID: 17760343/0x010F0057), tag_num=0x3B)
495: 0x1A49 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x4A)
496: 0x1A50 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x4D)
497: 0x1A57 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s045" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
498: 0x1A68 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x4B)
499: 0x1A6F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s045" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
500: 0x1A7E [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Joker (ID: 17760347/0x010F005B)
501: 0x1A87 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x4E)
502: 0x1A8E [0x4A] Joker (ID: 17760347/0x010F005B) looks at Pichichi (ID: 17760341/0x010F0055)
503: 0x1A97 [0x4B] UPDATE_ENTITY_YAW(entity=Joker (ID: 17760347/0x010F005B), yaw=17.1°*)
504: 0x1A9E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s047" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
505: 0x1AAF [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x15)
506: 0x1AB6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s047" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
507: 0x1AC5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s046" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
508: 0x1AD6 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x12)
509: 0x1ADD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x4F)
510: 0x1AE4 [0x4A] Joker (ID: 17760347/0x010F005B) looks at Pichichi (ID: 17760341/0x010F0055)
511: 0x1AED [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s048" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
512: 0x1AFE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x13)
513: 0x1B05 [0x1C] WAIT(100* ticks)
514: 0x1B08 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s046" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
515: 0x1B19 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x50)
516: 0x1B20 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s050" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
517: 0x1B31 [0x27] REQ_SET(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x4C)
518: 0x1B38 [0x1C] WAIT(50* ticks)
519: 0x1B3B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x14)
520: 0x1B42 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s052" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
521: 0x1B53 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pichichi (ID: 17760341/0x010F0055))
522: 0x1B59 [0x4A] Pichichi (ID: 17760341/0x010F0055) looks at Joker (ID: 17760347/0x010F005B)
523: 0x1B62 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pichichi (ID: 17760341/0x010F0055), tag_num=0x51)
524: 0x1B69 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x15)
525: 0x1B70 [0x2B] Joker (ID: 17760347/0x010F005B) [4064*]:
    → "jOkEr$26iS nOt A gHoSt! JoKEr Is a$26CaRdIan!"
526: 0x1B77 [0x23] WAIT_FOR_DIALOG_INTERACTION
527: 0x1B78 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s049" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[139*, 0*]
528: 0x1B89 [0x27] REQ_SET(priority=0x0B, entity_id=Joker (ID: 17760347/0x010F005B), tag_num=0x11)
529: 0x1B90 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s049" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=139*
530: 0x1B9F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [PRODUCER (ID: 17760265/0x010F0009), PRODUCER (ID: 17760265/0x010F0009)], work=[200*, 0*]
531: 0x1BB0 [0x1C] WAIT(60* ticks)
532: 0x1BB3 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Joker (ID: 17760347/0x010F005B))
533: 0x1BB9 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kohlo-Lakolo (ID: 17760338/0x010F0052))
534: 0x1BBF [0x2A] GET_REQ_LEVEL(level=11, entity_id=Papo-Hopo (ID: 17760339/0x010F0053))
535: 0x1BC5 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Gomada-Vulmada (ID: 17760340/0x010F0054))
536: 0x1BCB [0x2A] GET_REQ_LEVEL(level=11, entity_id=Yafa Yaa (ID: 17760342/0x010F0056))
537: 0x1BD1 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pyo Nzon (ID: 17760343/0x010F0057))
538: 0x1BD7 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 151*
539: 0x1BDB [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 151*
540: 0x1BDF [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
541: 0x1BE4 [0x1C] WAIT(300* ticks)
542: 0x1BE7 [0x7B] Kohlo-Lakolo (ID: 17760338/0x010F0052) stops talking
543: 0x1BEC [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x1BF7
544: 0x1BF4 [0x01] GOTO 0x1C01
545: 0x1BF7 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17760420/0x010F00A4)
546: 0x1BFD [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
547: 0x1C00 [0x78] ENABLE_GAME_TIMER_RESET_WEATHER()

SUBROUTINE_1C01:
548: 0x1C01 [0x00] END_REQSTACK()
```

### Event 432

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x1C02  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
1C00:       00                                            .             
```

#### Opcodes

```
  0: 0x1C02 [0x00] END_REQSTACK()
```

### Event 433

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x1C03  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
1C00:          00                                          .            
```

#### Opcodes

```
  0: 0x1C03 [0x00] END_REQSTACK()
```
