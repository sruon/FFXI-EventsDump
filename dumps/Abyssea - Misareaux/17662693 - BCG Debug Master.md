# 17662693 - BCG Debug Master

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Abyssea - Misareaux (ID: 216) |
| Block Size       | 2788 bytes                    |
| Total Events     | 2                             |
| References Count | 39                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [122](#event-122)     | 0x0001       |   2605 |            485 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0007      |           7 |
|       3 | 0x0008      |           8 |
|       4 | 0x000A      |          10 |
|       5 | 0x000B      |          11 |
|       6 | 0x000D      |          13 |
|       7 | 0x000E      |          14 |
|       8 | 0x0010      |          16 |
|       9 | 0x0011      |          17 |
|      10 | 0x0013      |          19 |
|      11 | 0x0014      |          20 |
|      12 | 0x0016      |          22 |
|      13 | 0x0002      |           2 |
|      14 | 0x0003      |           3 |
|      15 | 0x0005      |           5 |
|      16 | 0x0006      |           6 |
|      17 | 0x0009      |           9 |
|      18 | 0x000C      |          12 |
|      19 | 0x000F      |          15 |
|      20 | 0x0012      |          18 |
|      21 | 0x0015      |          21 |
|      22 | 0x0018      |          24 |
|      23 | 0x1EC9      |        7881 |
|      24 | 0x0004      |           4 |
|      25 | 0x1ECA      |        7882 |
|      26 | 0x270F      |        9999 |
|      27 | 0x1ECE      |        7886 |
|      28 | 0x001F      |          31 |
|      29 | 0x1ECB      |        7883 |
|      30 | 0x06A6      |        1702 |
|      31 | 0x06A7      |        1703 |
|      32 | 0x06A8      |        1704 |
|      33 | 0x06A9      |        1705 |
|      34 | 0x06AA      |        1706 |
|      35 | 0x06AB      |        1707 |
|      36 | 0x06AC      |        1708 |
|      37 | 0x1ECC      |        7884 |
|      38 | 0x1ECD      |        7885 |

## String References

- **7881**: Debug what? [Nothing./Clone ward./Resistance soldiers./Martello core./Verge 1./Verge 2./Verge 3./Resistance Credits.]
- **7882**: Barrier debug. (average HP value: $0) [Return./Pulse martello HP/Clone ward 1 HP/Clone ward 2 HP/Clone ward 3 HP/Clone ward 4 HP/Clone ward 5 HP/Clone ward 6 HP/Clone ward 7 HP/Clone ward durability: $1]
- **7883**: Resistance soldier debug. [Return./Attack: $0/Delay: $1/Skill: $2/Recovery: $3]
- **7884**: Martello core debug. [Return./3: $1/$3: $3/$3: $5/$3: $7/$3: $9/$3: $11/$3: $13]
- **7885**: Enemy pop location $0 debug. [Return./Next attack value: $1/Fore Trap attack reduction: $2/Fore Trap delay extension: $3/Rear Trap paralysis duration: $4/Rear Trap paralysis success rate: $5]
- **7886**: Value adjuster (Current: $0) [Cancel./+1/+2/+3/+5/+10/+20/+30/+50/+100/+200/+300/+500/+1000/-1/-2/-3/-5/-10/-20/-30/-50/-100/-200/-300/-500/-1000]

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

### Event 122

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 2605 bytes |
| Instructions | 485        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    06 03 00 06 04 00 06  05 00 06 06 00 06 07 00   ...............
0010: 06 08 00 06 09 00 06 0A  00 06 0B 00 06 0C 00 06  ................
0020: 0D 00 06 0E 00 06 0F 00  06 10 00 06 11 00 06 12  ................
0030: 00 06 13 00 06 14 00 06  15 00 06 16 00 06 17 00  ................
0040: 06 18 00 06 19 00 06 1A  00 06 1B 00 06 1C 00 06  ................
0050: 1D 00 06 1E 00 06 1F 00  06 20 00 06 21 00 06 22  ......... ..!.."
0060: 00 06 23 00 06 24 00 06  25 00 06 26 00 06 27 00  ..#..$..%..&..'.
0070: 06 28 00 06 29 00 06 2A  00 03 01 00 02 10 41 00  .(..)..*......A.
0080: 80 00 80 03 10 02 00 41  01 80 02 80 03 10 03 00  .......A........
0090: 41 03 80 04 80 03 10 04  00 41 05 80 06 80 03 10  A........A......
00A0: 05 00 41 07 80 08 80 03  10 06 00 41 09 80 0A 80  ..A........A....
00B0: 03 10 07 00 41 0B 80 0C  80 03 10 08 00 41 00 80  ....A........A..
00C0: 0D 80 04 10 09 00 41 0E  80 0F 80 04 10 0A 00 41  ......A........A
00D0: 10 80 03 80 04 10 0B 00  41 11 80 05 80 04 10 0C  ........A.......
00E0: 00 41 12 80 07 80 04 10  0D 00 41 13 80 09 80 04  .A........A.....
00F0: 10 0E 00 41 14 80 0B 80  04 10 0F 00 41 00 80 0D  ...A........A...
0100: 80 05 10 10 00 41 0E 80  11 80 05 10 11 00 41 04  .....A........A.
0110: 80 12 80 05 10 12 00 41  06 80 13 80 05 10 13 00  .......A........
0120: 41 08 80 14 80 05 10 14  00 41 0A 80 15 80 05 10  A........A......
0130: 15 00 41 0C 80 16 80 05  10 16 00 41 00 80 0D 80  ..A........A....
0140: 06 10 17 00 41 0E 80 11  80 06 10 18 00 41 04 80  ....A........A..
0150: 12 80 06 10 19 00 41 06  80 13 80 06 10 1A 00 41  ......A........A
0160: 08 80 14 80 06 10 1B 00  41 0A 80 15 80 06 10 1C  ........A.......
0170: 00 41 0C 80 16 80 06 10  1D 00 41 00 80 0D 80 07  .A........A.....
0180: 10 1E 00 41 0E 80 11 80  07 10 1F 00 41 04 80 12  ...A........A...
0190: 80 07 10 20 00 41 06 80  13 80 07 10 21 00 41 08  ... .A......!.A.
01A0: 80 14 80 07 10 22 00 41  0A 80 15 80 07 10 23 00  .....".A......#.
01B0: 41 0C 80 16 80 07 10 24  00 05 29 00 02 29 00 00  A......$..)..)..
01C0: 80 02 2C 0A 03 26 00 00  80 24 17 80 00 80 00 80  ..,..&...$......
01D0: 25 02 00 10 00 80 00 E4  01 03 26 00 00 80 06 29  %.........&....)
01E0: 00 01 29 0A 02 00 10 01  80 00 4B 03 03 26 00 01  ..).......K..&..
01F0: 80 05 2A 00 02 2A 00 00  80 02 48 03 3C 25 00 01  ..*..*....H.<%..
0200: 80 01 80 3C 25 00 0D 80  01 80 3C 25 00 0E 80 01  ...<%.....<%....
0210: 80 3C 25 00 18 80 01 80  3C 25 00 0F 80 01 80 3C  .<%.....<%.....<
0220: 25 00 10 80 01 80 3C 25  00 02 80 01 80 3C 25 00  %.....<%.....<%.
0230: 03 80 01 80 06 27 00 03  02 10 03 00 03 03 10 04  .....'..........
0240: 00 24 19 80 00 80 25 00  25 02 00 10 00 80 00 57  .$....%.%......W
0250: 02 06 2A 00 01 E7 02 02  00 10 01 80 00 67 02 03  ..*..........g..
0260: 27 00 01 80 01 E7 02 02  00 10 0D 80 00 77 02 03  '............w..
0270: 27 00 0D 80 01 E7 02 02  00 10 0E 80 00 87 02 03  '...............
0280: 27 00 0E 80 01 E7 02 02  00 10 18 80 00 97 02 03  '...............
0290: 27 00 18 80 01 E7 02 02  00 10 0F 80 00 A7 02 03  '...............
02A0: 27 00 0F 80 01 E7 02 02  00 10 10 80 00 B7 02 03  '...............
02B0: 27 00 10 80 01 E7 02 02  00 10 02 80 00 C7 02 03  '...............
02C0: 27 00 02 80 01 E7 02 02  00 10 03 80 00 D7 02 03  '...............
02D0: 27 00 03 80 01 E7 02 02  00 10 11 80 00 E7 02 03  '...............
02E0: 27 00 11 80 01 E7 02 02  27 00 00 80 02 45 03 02  '.......'....E..
02F0: 27 00 11 80 00 FF 02 03  02 10 04 00 01 04 03 03  '...............
0300: 02 10 1A 80 24 1B 80 00  80 00 80 25 02 00 10 00  ....$......%....
0310: 80 00 17 03 01 17 03 02  00 10 00 80 02 45 03 03  .............E..
0320: 28 00 00 10 40 00 80 02  80 01 10 26 00 40 03 80  (...@......&.@..
0330: 13 80 01 10 27 00 40 08  80 1C 80 01 10 28 00 06  ....'.@......(..
0340: 29 00 06 2A 00 01 F4 01  01 29 0A 02 00 10 0D 80  )..*.....)......
0350: 00 5F 04 03 26 00 0D 80  05 2A 00 02 2A 00 00 80  ._..&....*..*...
0360: 02 5C 04 06 27 00 03 02  10 05 00 03 03 10 06 00  .\..'...........
0370: 03 04 10 07 00 03 05 10  08 00 24 1D 80 00 80 00  ..........$.....
0380: 80 25 02 00 10 00 80 00  90 03 06 2A 00 01 D0 03  .%.........*....
0390: 02 00 10 01 80 00 A0 03  03 27 00 01 80 01 D0 03  .........'......
03A0: 02 00 10 0D 80 00 B0 03  03 27 00 0D 80 01 D0 03  .........'......
03B0: 02 00 10 0E 80 00 C0 03  03 27 00 0E 80 01 D0 03  .........'......
03C0: 02 00 10 18 80 00 D0 03  03 27 00 18 80 01 D0 03  .........'......
03D0: 02 27 00 00 80 02 59 04  02 27 00 01 80 80 E8 03  .'....Y..'......
03E0: 03 02 10 05 00 01 18 04  02 27 00 0D 80 80 F8 03  .........'......
03F0: 03 02 10 06 00 01 18 04  02 27 00 0E 80 80 08 04  .........'......
0400: 03 02 10 07 00 01 18 04  02 27 00 18 80 80 18 04  .........'......
0410: 03 02 10 08 00 01 18 04  24 1B 80 00 80 00 80 25  ........$......%
0420: 02 00 10 00 80 00 2B 04  01 2B 04 02 00 10 00 80  ......+..+......
0430: 02 59 04 03 28 00 00 10  40 00 80 02 80 01 10 26  .Y..(...@......&
0440: 00 40 03 80 13 80 01 10  27 00 40 08 80 1C 80 01  .@......'.@.....
0450: 10 28 00 06 29 00 06 2A  00 01 5B 03 01 29 0A 02  .(..)..*..[..)..
0460: 00 10 0E 80 00 05 06 03  26 00 0E 80 05 2A 00 02  ........&....*..
0470: 2A 00 00 80 02 02 06 06  27 00 03 02 10 1E 80 03  *.......'.......
0480: 03 10 09 00 03 04 10 1F  80 03 05 10 0A 00 03 06  ................
0490: 10 20 80 03 07 10 0B 00  03 08 10 21 80 03 09 10  . .........!....
04A0: 0C 00 03 00 17 22 80 03  01 17 0D 00 03 02 17 23  .....".........#
04B0: 80 03 03 17 0E 00 03 04  17 24 80 03 05 17 0F 00  .........$......
04C0: 24 25 80 00 80 00 80 25  02 00 10 00 80 00 D6 04  $%.....%........
04D0: 06 2A 00 01 46 05 02 00  10 01 80 00 E6 04 03 27  .*..F..........'
04E0: 00 01 80 01 46 05 02 00  10 0D 80 00 F6 04 03 27  ....F..........'
04F0: 00 0D 80 01 46 05 02 00  10 0E 80 00 06 05 03 27  ....F..........'
0500: 00 0E 80 01 46 05 02 00  10 18 80 00 16 05 03 27  ....F..........'
0510: 00 18 80 01 46 05 02 00  10 0F 80 00 26 05 03 27  ....F.......&..'
0520: 00 0F 80 01 46 05 02 00  10 10 80 00 36 05 03 27  ....F.......6..'
0530: 00 10 80 01 46 05 02 00  10 02 80 00 46 05 03 27  ....F.......F..'
0540: 00 02 80 01 46 05 02 27  00 00 80 02 FF 05 02 27  ....F..'.......'
0550: 00 01 80 80 5E 05 03 02  10 09 00 01 BE 05 02 27  ....^..........'
0560: 00 0D 80 80 6E 05 03 02  10 0A 00 01 BE 05 02 27  ....n..........'
0570: 00 0E 80 80 7E 05 03 02  10 0B 00 01 BE 05 02 27  ....~..........'
0580: 00 18 80 80 8E 05 03 02  10 0C 00 01 BE 05 02 27  ...............'
0590: 00 0F 80 80 9E 05 03 02  10 0D 00 01 BE 05 02 27  ...............'
05A0: 00 10 80 80 AE 05 03 02  10 0E 00 01 BE 05 02 27  ...............'
05B0: 00 02 80 80 BE 05 03 02  10 0F 00 01 BE 05 24 1B  ..............$.
05C0: 80 00 80 00 80 25 02 00  10 00 80 00 D1 05 01 D1  .....%..........
05D0: 05 02 00 10 00 80 02 FF  05 03 28 00 00 10 40 00  ..........(...@.
05E0: 80 02 80 01 10 26 00 40  03 80 13 80 01 10 27 00  .....&.@......'.
05F0: 40 08 80 1C 80 01 10 28  00 06 29 00 06 2A 00 01  @......(..)..*..
0600: 6F 04 01 29 0A 02 00 10  18 80 00 43 07 03 26 00  o..).......C..&.
0610: 18 80 05 2A 00 02 2A 00  00 80 02 40 07 06 27 00  ...*..*....@..'.
0620: 03 02 10 01 80 03 03 10  11 00 03 04 10 13 00 03  ................
0630: 05 10 14 00 03 06 10 15  00 03 07 10 16 00 24 26  ..............$&
0640: 80 00 80 00 80 25 02 00  10 00 80 00 54 06 06 2A  .....%......T..*
0650: 00 01 A4 06 02 00 10 01  80 00 64 06 03 27 00 01  ..........d..'..
0660: 80 01 A4 06 02 00 10 0D  80 00 74 06 03 27 00 0D  ..........t..'..
0670: 80 01 A4 06 02 00 10 0E  80 00 84 06 03 27 00 0E  .............'..
0680: 80 01 A4 06 02 00 10 18  80 00 94 06 03 27 00 18  .............'..
0690: 80 01 A4 06 02 00 10 0F  80 00 A4 06 03 27 00 0F  .............'..
06A0: 80 01 A4 06 02 27 00 00  80 02 3D 07 02 27 00 01  .....'....=..'..
06B0: 80 80 BC 06 03 02 10 11  00 01 FC 06 02 27 00 0D  .............'..
06C0: 80 80 CC 06 03 02 10 13  00 01 FC 06 02 27 00 0E  .............'..
06D0: 80 80 DC 06 03 02 10 14  00 01 FC 06 02 27 00 18  .............'..
06E0: 80 80 EC 06 03 02 10 15  00 01 FC 06 02 27 00 0F  .............'..
06F0: 80 80 FC 06 03 02 10 16  00 01 FC 06 24 1B 80 00  ............$...
0700: 80 00 80 25 02 00 10 00  80 00 0F 07 01 0F 07 02  ...%............
0710: 00 10 00 80 02 3D 07 03  28 00 00 10 40 00 80 02  .....=..(...@...
0720: 80 01 10 26 00 40 03 80  13 80 01 10 27 00 40 08  ...&.@......'.@.
0730: 80 1C 80 01 10 28 00 06  29 00 06 2A 00 01 15 06  .....(..)..*....
0740: 01 29 0A 02 00 10 0F 80  00 81 08 03 26 00 0F 80  .)..........&...
0750: 05 2A 00 02 2A 00 00 80  02 7E 08 06 27 00 03 02  .*..*....~..'...
0760: 10 0D 80 03 03 10 18 00  03 04 10 1A 00 03 05 10  ................
0770: 1B 00 03 06 10 1C 00 03  07 10 1D 00 24 26 80 00  ............$&..
0780: 80 00 80 25 02 00 10 00  80 00 92 07 06 2A 00 01  ...%.........*..
0790: E2 07 02 00 10 01 80 00  A2 07 03 27 00 01 80 01  ...........'....
07A0: E2 07 02 00 10 0D 80 00  B2 07 03 27 00 0D 80 01  ...........'....
07B0: E2 07 02 00 10 0E 80 00  C2 07 03 27 00 0E 80 01  ...........'....
07C0: E2 07 02 00 10 18 80 00  D2 07 03 27 00 18 80 01  ...........'....
07D0: E2 07 02 00 10 0F 80 00  E2 07 03 27 00 0F 80 01  ...........'....
07E0: E2 07 02 27 00 00 80 02  7B 08 02 27 00 01 80 80  ...'....{..'....
07F0: FA 07 03 02 10 18 00 01  3A 08 02 27 00 0D 80 80  ........:..'....
0800: 0A 08 03 02 10 1A 00 01  3A 08 02 27 00 0E 80 80  ........:..'....
0810: 1A 08 03 02 10 1B 00 01  3A 08 02 27 00 18 80 80  ........:..'....
0820: 2A 08 03 02 10 1C 00 01  3A 08 02 27 00 0F 80 80  *.......:..'....
0830: 3A 08 03 02 10 1D 00 01  3A 08 24 1B 80 00 80 00  :.......:.$.....
0840: 80 25 02 00 10 00 80 00  4D 08 01 4D 08 02 00 10  .%......M..M....
0850: 00 80 02 7B 08 03 28 00  00 10 40 00 80 02 80 01  ...{..(...@.....
0860: 10 26 00 40 03 80 13 80  01 10 27 00 40 08 80 1C  .&.@......'.@...
0870: 80 01 10 28 00 06 29 00  06 2A 00 01 53 07 01 29  ...(..)..*..S..)
0880: 0A 02 00 10 10 80 00 BF  09 03 26 00 10 80 05 2A  ..........&....*
0890: 00 02 2A 00 00 80 02 BC  09 06 27 00 03 02 10 0E  ..*.......'.....
08A0: 80 03 03 10 1F 00 03 04  10 21 00 03 05 10 22 00  .........!....".
08B0: 03 06 10 23 00 03 07 10  24 00 24 26 80 00 80 00  ...#....$.$&....
08C0: 80 25 02 00 10 00 80 00  D0 08 06 2A 00 01 20 09  .%.........*.. .
08D0: 02 00 10 01 80 00 E0 08  03 27 00 01 80 01 20 09  .........'.... .
08E0: 02 00 10 0D 80 00 F0 08  03 27 00 0D 80 01 20 09  .........'.... .
08F0: 02 00 10 0E 80 00 00 09  03 27 00 0E 80 01 20 09  .........'.... .
0900: 02 00 10 18 80 00 10 09  03 27 00 18 80 01 20 09  .........'.... .
0910: 02 00 10 0F 80 00 20 09  03 27 00 0F 80 01 20 09  ...... ..'.... .
0920: 02 27 00 00 80 02 B9 09  02 27 00 01 80 80 38 09  .'.......'....8.
0930: 03 02 10 1F 00 01 78 09  02 27 00 0D 80 80 48 09  ......x..'....H.
0940: 03 02 10 21 00 01 78 09  02 27 00 0E 80 80 58 09  ...!..x..'....X.
0950: 03 02 10 22 00 01 78 09  02 27 00 18 80 80 68 09  ..."..x..'....h.
0960: 03 02 10 23 00 01 78 09  02 27 00 0F 80 80 78 09  ...#..x..'....x.
0970: 03 02 10 24 00 01 78 09  24 1B 80 00 80 00 80 25  ...$..x.$......%
0980: 02 00 10 00 80 00 8B 09  01 8B 09 02 00 10 00 80  ................
0990: 02 B9 09 03 28 00 00 10  40 00 80 02 80 01 10 26  ....(...@......&
09A0: 00 40 03 80 13 80 01 10  27 00 40 08 80 1C 80 01  .@......'.@.....
09B0: 10 28 00 06 29 00 06 2A  00 01 91 08 01 29 0A 02  .(..)..*.....)..
09C0: 00 10 02 80 00 29 0A 03  26 00 02 80 05 2A 00 02  .....)..&....*..
09D0: 2A 00 00 80 02 26 0A 06  27 00 03 02 10 01 00 24  *....&..'......$
09E0: 1B 80 00 80 00 80 25 02  00 10 00 80 00 F5 09 06  ......%.........
09F0: 29 00 01 F5 09 02 00 10  00 80 02 23 0A 03 28 00  )..........#..(.
0A00: 00 10 40 00 80 02 80 01  10 26 00 40 03 80 13 80  ..@......&.@....
0A10: 01 10 27 00 40 08 80 1C  80 01 10 28 00 06 29 00  ..'.@......(..).
0A20: 06 2A 00 01 CF 09 01 29  0A 01 BC 01 21 00        .*.....)....!.  
```

#### Opcodes

```
  0: 0x0001 [0x06] ExtData[1]->WorkLocal[3] = 0
  1: 0x0004 [0x06] ExtData[1]->WorkLocal[4] = 0
  2: 0x0007 [0x06] ExtData[1]->WorkLocal[5] = 0
  3: 0x000A [0x06] ExtData[1]->WorkLocal[6] = 0
  4: 0x000D [0x06] ExtData[1]->WorkLocal[7] = 0
  5: 0x0010 [0x06] ExtData[1]->WorkLocal[8] = 0
  6: 0x0013 [0x06] ExtData[1]->WorkLocal[9] = 0
  7: 0x0016 [0x06] ExtData[1]->WorkLocal[10] = 0
  8: 0x0019 [0x06] ExtData[1]->WorkLocal[11] = 0
  9: 0x001C [0x06] ExtData[1]->WorkLocal[12] = 0
 10: 0x001F [0x06] ExtData[1]->WorkLocal[13] = 0
 11: 0x0022 [0x06] ExtData[1]->WorkLocal[14] = 0
 12: 0x0025 [0x06] ExtData[1]->WorkLocal[15] = 0
 13: 0x0028 [0x06] ExtData[1]->WorkLocal[16] = 0
 14: 0x002B [0x06] ExtData[1]->WorkLocal[17] = 0
 15: 0x002E [0x06] ExtData[1]->WorkLocal[18] = 0
 16: 0x0031 [0x06] ExtData[1]->WorkLocal[19] = 0
 17: 0x0034 [0x06] ExtData[1]->WorkLocal[20] = 0
 18: 0x0037 [0x06] ExtData[1]->WorkLocal[21] = 0
 19: 0x003A [0x06] ExtData[1]->WorkLocal[22] = 0
 20: 0x003D [0x06] ExtData[1]->WorkLocal[23] = 0
 21: 0x0040 [0x06] ExtData[1]->WorkLocal[24] = 0
 22: 0x0043 [0x06] ExtData[1]->WorkLocal[25] = 0
 23: 0x0046 [0x06] ExtData[1]->WorkLocal[26] = 0
 24: 0x0049 [0x06] ExtData[1]->WorkLocal[27] = 0
 25: 0x004C [0x06] ExtData[1]->WorkLocal[28] = 0
 26: 0x004F [0x06] ExtData[1]->WorkLocal[29] = 0
 27: 0x0052 [0x06] ExtData[1]->WorkLocal[30] = 0
 28: 0x0055 [0x06] ExtData[1]->WorkLocal[31] = 0
 29: 0x0058 [0x06] ExtData[1]->WorkLocal[32] = 0
 30: 0x005B [0x06] ExtData[1]->WorkLocal[33] = 0
 31: 0x005E [0x06] ExtData[1]->WorkLocal[34] = 0
 32: 0x0061 [0x06] ExtData[1]->WorkLocal[35] = 0
 33: 0x0064 [0x06] ExtData[1]->WorkLocal[36] = 0
 34: 0x0067 [0x06] ExtData[1]->WorkLocal[37] = 0
 35: 0x006A [0x06] ExtData[1]->WorkLocal[38] = 0
 36: 0x006D [0x06] ExtData[1]->WorkLocal[39] = 0
 37: 0x0070 [0x06] ExtData[1]->WorkLocal[40] = 0
 38: 0x0073 [0x06] ExtData[1]->WorkLocal[41] = 0
 39: 0x0076 [0x06] ExtData[1]->WorkLocal[42] = 0
 40: 0x0079 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
 41: 0x007E [0x41] ExtData[1]->WorkLocal[2] = Work_Zone[3] (bits 0*-0*)
 42: 0x0087 [0x41] ExtData[1]->WorkLocal[3] = Work_Zone[3] (bits 1*-7*)
 43: 0x0090 [0x41] ExtData[1]->WorkLocal[4] = Work_Zone[3] (bits 8*-10*)
 44: 0x0099 [0x41] ExtData[1]->WorkLocal[5] = Work_Zone[3] (bits 11*-13*)
 45: 0x00A2 [0x41] ExtData[1]->WorkLocal[6] = Work_Zone[3] (bits 14*-16*)
 46: 0x00AB [0x41] ExtData[1]->WorkLocal[7] = Work_Zone[3] (bits 17*-19*)
 47: 0x00B4 [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[3] (bits 20*-22*)
 48: 0x00BD [0x41] ExtData[1]->WorkLocal[9] = Work_Zone[4] (bits 0*-2*)
 49: 0x00C6 [0x41] ExtData[1]->WorkLocal[10] = Work_Zone[4] (bits 3*-5*)
 50: 0x00CF [0x41] ExtData[1]->WorkLocal[11] = Work_Zone[4] (bits 6*-8*)
 51: 0x00D8 [0x41] ExtData[1]->WorkLocal[12] = Work_Zone[4] (bits 9*-11*)
 52: 0x00E1 [0x41] ExtData[1]->WorkLocal[13] = Work_Zone[4] (bits 12*-14*)
 53: 0x00EA [0x41] ExtData[1]->WorkLocal[14] = Work_Zone[4] (bits 15*-17*)
 54: 0x00F3 [0x41] ExtData[1]->WorkLocal[15] = Work_Zone[4] (bits 18*-20*)
 55: 0x00FC [0x41] ExtData[1]->WorkLocal[16] = Work_Zone[5] (bits 0*-2*)
 56: 0x0105 [0x41] ExtData[1]->WorkLocal[17] = Work_Zone[5] (bits 3*-9*)
 57: 0x010E [0x41] ExtData[1]->WorkLocal[18] = Work_Zone[5] (bits 10*-12*)
 58: 0x0117 [0x41] ExtData[1]->WorkLocal[19] = Work_Zone[5] (bits 13*-15*)
 59: 0x0120 [0x41] ExtData[1]->WorkLocal[20] = Work_Zone[5] (bits 16*-18*)
 60: 0x0129 [0x41] ExtData[1]->WorkLocal[21] = Work_Zone[5] (bits 19*-21*)
 61: 0x0132 [0x41] ExtData[1]->WorkLocal[22] = Work_Zone[5] (bits 22*-24*)
 62: 0x013B [0x41] ExtData[1]->WorkLocal[23] = Work_Zone[6] (bits 0*-2*)
 63: 0x0144 [0x41] ExtData[1]->WorkLocal[24] = Work_Zone[6] (bits 3*-9*)
 64: 0x014D [0x41] ExtData[1]->WorkLocal[25] = Work_Zone[6] (bits 10*-12*)
 65: 0x0156 [0x41] ExtData[1]->WorkLocal[26] = Work_Zone[6] (bits 13*-15*)
 66: 0x015F [0x41] ExtData[1]->WorkLocal[27] = Work_Zone[6] (bits 16*-18*)
 67: 0x0168 [0x41] ExtData[1]->WorkLocal[28] = Work_Zone[6] (bits 19*-21*)
 68: 0x0171 [0x41] ExtData[1]->WorkLocal[29] = Work_Zone[6] (bits 22*-24*)
 69: 0x017A [0x41] ExtData[1]->WorkLocal[30] = Work_Zone[7] (bits 0*-2*)
 70: 0x0183 [0x41] ExtData[1]->WorkLocal[31] = Work_Zone[7] (bits 3*-9*)
 71: 0x018C [0x41] ExtData[1]->WorkLocal[32] = Work_Zone[7] (bits 10*-12*)
 72: 0x0195 [0x41] ExtData[1]->WorkLocal[33] = Work_Zone[7] (bits 13*-15*)
 73: 0x019E [0x41] ExtData[1]->WorkLocal[34] = Work_Zone[7] (bits 16*-18*)
 74: 0x01A7 [0x41] ExtData[1]->WorkLocal[35] = Work_Zone[7] (bits 19*-21*)
 75: 0x01B0 [0x41] ExtData[1]->WorkLocal[36] = Work_Zone[7] (bits 22*-24*)
 76: 0x01B9 [0x05] ExtData[1]->WorkLocal[41] = 1
 77: 0x01BC [0x02] IF !(ExtData[1]->WorkLocal[41] <= 0*) GOTO 0x0A2C
 78: 0x01C4 [0x03] ExtData[1]->WorkLocal[38] = 0*
 79: 0x01C9 [0x24] CREATE_DIALOG(message_id=7881*, default_option=0*, option_flags=0*)
    → "Debug what? [Nothing./Clone ward./Resistance soldiers./Martello core./Verge 1./Verge 2./Verge 3./Resistance Credits.]"
 80: 0x01D0 [0x25] WAIT_DIALOG_SELECT()
 81: 0x01D1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01E4
 82: 0x01D9 [0x03] ExtData[1]->WorkLocal[38] = 0*
 83: 0x01DE [0x06] ExtData[1]->WorkLocal[41] = 0
 84: 0x01E1 [0x01] GOTO 0x0A29
 85: 0x01E4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x034B
 86: 0x01EC [0x03] ExtData[1]->WorkLocal[38] = 1*
 87: 0x01F1 [0x05] ExtData[1]->WorkLocal[42] = 1

SUBROUTINE_01F4:
 88: 0x01F4 [0x02] IF !(ExtData[1]->WorkLocal[42] <= 0*) GOTO 0x0348
 89: 0x01FC [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[37], bit_index_work_offset=1*, condition_work_offset=1*)
 90: 0x0203 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[37], bit_index_work_offset=2*, condition_work_offset=1*)
 91: 0x020A [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[37], bit_index_work_offset=3*, condition_work_offset=1*)
 92: 0x0211 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[37], bit_index_work_offset=4*, condition_work_offset=1*)
 93: 0x0218 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[37], bit_index_work_offset=5*, condition_work_offset=1*)
 94: 0x021F [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[37], bit_index_work_offset=6*, condition_work_offset=1*)
 95: 0x0226 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[37], bit_index_work_offset=7*, condition_work_offset=1*)
 96: 0x022D [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[37], bit_index_work_offset=8*, condition_work_offset=1*)
 97: 0x0234 [0x06] ExtData[1]->WorkLocal[39] = 0
 98: 0x0237 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[3]
 99: 0x023C [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[4]
100: 0x0241 [0x24] CREATE_DIALOG(message_id=7882*, default_option=0*, option_flags=ExtData[1]->WorkLocal[37])
    → "Barrier debug. (average HP value: $0) [Return./Pulse martello HP/Clone ward 1 HP/Clone ward 2 HP/Clone ward 3 HP/Clone ward 4 HP/Clone ward 5 HP/Clone ward 6 HP/Clone ward 7 HP/Clone ward durability: $1]"
101: 0x0248 [0x25] WAIT_DIALOG_SELECT()
102: 0x0249 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0257
103: 0x0251 [0x06] ExtData[1]->WorkLocal[42] = 0
104: 0x0254 [0x01] GOTO 0x02E7
105: 0x0257 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0267
106: 0x025F [0x03] ExtData[1]->WorkLocal[39] = 1*
107: 0x0264 [0x01] GOTO 0x02E7
108: 0x0267 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0277
109: 0x026F [0x03] ExtData[1]->WorkLocal[39] = 2*
110: 0x0274 [0x01] GOTO 0x02E7
111: 0x0277 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0287
112: 0x027F [0x03] ExtData[1]->WorkLocal[39] = 3*
113: 0x0284 [0x01] GOTO 0x02E7
114: 0x0287 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0297
115: 0x028F [0x03] ExtData[1]->WorkLocal[39] = 4*
116: 0x0294 [0x01] GOTO 0x02E7
117: 0x0297 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x02A7
118: 0x029F [0x03] ExtData[1]->WorkLocal[39] = 5*
119: 0x02A4 [0x01] GOTO 0x02E7
120: 0x02A7 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x02B7
121: 0x02AF [0x03] ExtData[1]->WorkLocal[39] = 6*
122: 0x02B4 [0x01] GOTO 0x02E7
123: 0x02B7 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x02C7
124: 0x02BF [0x03] ExtData[1]->WorkLocal[39] = 7*
125: 0x02C4 [0x01] GOTO 0x02E7
126: 0x02C7 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x02D7
127: 0x02CF [0x03] ExtData[1]->WorkLocal[39] = 8*
128: 0x02D4 [0x01] GOTO 0x02E7
129: 0x02D7 [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x02E7
130: 0x02DF [0x03] ExtData[1]->WorkLocal[39] = 9*
131: 0x02E4 [0x01] GOTO 0x02E7

SUBROUTINE_02E7:
132: 0x02E7 [0x02] IF !(ExtData[1]->WorkLocal[39] <= 0*) GOTO 0x0345
133: 0x02EF [0x02] IF !(ExtData[1]->WorkLocal[39] == 9*) GOTO 0x02FF
134: 0x02F7 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[4]
135: 0x02FC [0x01] GOTO 0x0304
136: 0x02FF [0x03] Work_Zone[2] = 9999*

SUBROUTINE_0304:
137: 0x0304 [0x24] CREATE_DIALOG(message_id=7886*, default_option=0*, option_flags=0*)
    → "Value adjuster (Current: $0) [Cancel./+1/+2/+3/+5/+10/+20/+30/+50/+100/+200/+300/+500/+1000/-1/-2/-3/-5/-10/-20/-30/-50/-100/-200/-300/-500/-1000]"
138: 0x030B [0x25] WAIT_DIALOG_SELECT()
139: 0x030C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0317
140: 0x0314 [0x01] GOTO 0x0317

SUBROUTINE_0317:
141: 0x0317 [0x02] IF !(Work_Zone[0] <= 0*) GOTO 0x0345
142: 0x031F [0x03] ExtData[1]->WorkLocal[40] = Work_Zone[0]
143: 0x0324 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[38])
144: 0x032D [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[39])
145: 0x0336 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[40])
146: 0x033F [0x06] ExtData[1]->WorkLocal[41] = 0
147: 0x0342 [0x06] ExtData[1]->WorkLocal[42] = 0
148: 0x0345 [0x01] GOTO 0x01F4
149: 0x0348 [0x01] GOTO 0x0A29
150: 0x034B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x045F
151: 0x0353 [0x03] ExtData[1]->WorkLocal[38] = 2*
152: 0x0358 [0x05] ExtData[1]->WorkLocal[42] = 1

SUBROUTINE_035B:
153: 0x035B [0x02] IF !(ExtData[1]->WorkLocal[42] <= 0*) GOTO 0x045C
154: 0x0363 [0x06] ExtData[1]->WorkLocal[39] = 0
155: 0x0366 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[5]
156: 0x036B [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[6]
157: 0x0370 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[7]
158: 0x0375 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[8]
159: 0x037A [0x24] CREATE_DIALOG(message_id=7883*, default_option=0*, option_flags=0*)
    → "Resistance soldier debug. [Return./Attack: $0/Delay: $1/Skill: $2/Recovery: $3]"
160: 0x0381 [0x25] WAIT_DIALOG_SELECT()
161: 0x0382 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0390
162: 0x038A [0x06] ExtData[1]->WorkLocal[42] = 0
163: 0x038D [0x01] GOTO 0x03D0
164: 0x0390 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03A0
165: 0x0398 [0x03] ExtData[1]->WorkLocal[39] = 1*
166: 0x039D [0x01] GOTO 0x03D0
167: 0x03A0 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x03B0
168: 0x03A8 [0x03] ExtData[1]->WorkLocal[39] = 2*
169: 0x03AD [0x01] GOTO 0x03D0
170: 0x03B0 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x03C0
171: 0x03B8 [0x03] ExtData[1]->WorkLocal[39] = 3*
172: 0x03BD [0x01] GOTO 0x03D0
173: 0x03C0 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x03D0
174: 0x03C8 [0x03] ExtData[1]->WorkLocal[39] = 4*
175: 0x03CD [0x01] GOTO 0x03D0

SUBROUTINE_03D0:
176: 0x03D0 [0x02] IF !(ExtData[1]->WorkLocal[39] <= 0*) GOTO 0x0459
177: 0x03D8 [0x02] IF !(ExtData[1]->WorkLocal[39] == 1*) GOTO 0x03E8
178: 0x03E0 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[5]
179: 0x03E5 [0x01] GOTO 0x0418
180: 0x03E8 [0x02] IF !(ExtData[1]->WorkLocal[39] == 2*) GOTO 0x03F8
181: 0x03F0 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[6]
182: 0x03F5 [0x01] GOTO 0x0418
183: 0x03F8 [0x02] IF !(ExtData[1]->WorkLocal[39] == 3*) GOTO 0x0408
184: 0x0400 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[7]
185: 0x0405 [0x01] GOTO 0x0418
186: 0x0408 [0x02] IF !(ExtData[1]->WorkLocal[39] == 4*) GOTO 0x0418
187: 0x0410 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[8]
188: 0x0415 [0x01] GOTO 0x0418

SUBROUTINE_0418:
189: 0x0418 [0x24] CREATE_DIALOG(message_id=7886*, default_option=0*, option_flags=0*)
    → "Value adjuster (Current: $0) [Cancel./+1/+2/+3/+5/+10/+20/+30/+50/+100/+200/+300/+500/+1000/-1/-2/-3/-5/-10/-20/-30/-50/-100/-200/-300/-500/-1000]"
190: 0x041F [0x25] WAIT_DIALOG_SELECT()
191: 0x0420 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x042B
192: 0x0428 [0x01] GOTO 0x042B

SUBROUTINE_042B:
193: 0x042B [0x02] IF !(Work_Zone[0] <= 0*) GOTO 0x0459
194: 0x0433 [0x03] ExtData[1]->WorkLocal[40] = Work_Zone[0]
195: 0x0438 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[38])
196: 0x0441 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[39])
197: 0x044A [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[40])
198: 0x0453 [0x06] ExtData[1]->WorkLocal[41] = 0
199: 0x0456 [0x06] ExtData[1]->WorkLocal[42] = 0
200: 0x0459 [0x01] GOTO 0x035B
201: 0x045C [0x01] GOTO 0x0A29
202: 0x045F [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0605
203: 0x0467 [0x03] ExtData[1]->WorkLocal[38] = 3*
204: 0x046C [0x05] ExtData[1]->WorkLocal[42] = 1

SUBROUTINE_046F:
205: 0x046F [0x02] IF !(ExtData[1]->WorkLocal[42] <= 0*) GOTO 0x0602
206: 0x0477 [0x06] ExtData[1]->WorkLocal[39] = 0
207: 0x047A [0x03] Work_Zone[2] = 1702*
208: 0x047F [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[9]
209: 0x0484 [0x03] Work_Zone[4] = 1703*
210: 0x0489 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[10]
211: 0x048E [0x03] Work_Zone[6] = 1704*
212: 0x0493 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[11]
213: 0x0498 [0x03] Work_Zone[8] = 1705*
214: 0x049D [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[12]
215: 0x04A2 [0x03] Work_Zone_1700[0] = 1706*
216: 0x04A7 [0x03] Work_Zone_1700[1] = ExtData[1]->WorkLocal[13]
217: 0x04AC [0x03] Work_Zone_1700[2] = 1707*
218: 0x04B1 [0x03] Work_Zone_1700[3] = ExtData[1]->WorkLocal[14]
219: 0x04B6 [0x03] Work_Zone_1700[4] = 1708*
220: 0x04BB [0x03] Work_Zone_1700[5] = ExtData[1]->WorkLocal[15]
221: 0x04C0 [0x24] CREATE_DIALOG(message_id=7884*, default_option=0*, option_flags=0*)
    → "Martello core debug. [Return./3: $1/$3: $3/$3: $5/$3: $7/$3: $9/$3: $11/$3: $13]"
222: 0x04C7 [0x25] WAIT_DIALOG_SELECT()
223: 0x04C8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x04D6
224: 0x04D0 [0x06] ExtData[1]->WorkLocal[42] = 0
225: 0x04D3 [0x01] GOTO 0x0546
226: 0x04D6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x04E6
227: 0x04DE [0x03] ExtData[1]->WorkLocal[39] = 1*
228: 0x04E3 [0x01] GOTO 0x0546
229: 0x04E6 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x04F6
230: 0x04EE [0x03] ExtData[1]->WorkLocal[39] = 2*
231: 0x04F3 [0x01] GOTO 0x0546
232: 0x04F6 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0506
233: 0x04FE [0x03] ExtData[1]->WorkLocal[39] = 3*
234: 0x0503 [0x01] GOTO 0x0546
235: 0x0506 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0516
236: 0x050E [0x03] ExtData[1]->WorkLocal[39] = 4*
237: 0x0513 [0x01] GOTO 0x0546
238: 0x0516 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0526
239: 0x051E [0x03] ExtData[1]->WorkLocal[39] = 5*
240: 0x0523 [0x01] GOTO 0x0546
241: 0x0526 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0536
242: 0x052E [0x03] ExtData[1]->WorkLocal[39] = 6*
243: 0x0533 [0x01] GOTO 0x0546
244: 0x0536 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0546
245: 0x053E [0x03] ExtData[1]->WorkLocal[39] = 7*
246: 0x0543 [0x01] GOTO 0x0546

SUBROUTINE_0546:
247: 0x0546 [0x02] IF !(ExtData[1]->WorkLocal[39] <= 0*) GOTO 0x05FF
248: 0x054E [0x02] IF !(ExtData[1]->WorkLocal[39] == 1*) GOTO 0x055E
249: 0x0556 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[9]
250: 0x055B [0x01] GOTO 0x05BE
251: 0x055E [0x02] IF !(ExtData[1]->WorkLocal[39] == 2*) GOTO 0x056E
252: 0x0566 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[10]
253: 0x056B [0x01] GOTO 0x05BE
254: 0x056E [0x02] IF !(ExtData[1]->WorkLocal[39] == 3*) GOTO 0x057E
255: 0x0576 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[11]
256: 0x057B [0x01] GOTO 0x05BE
257: 0x057E [0x02] IF !(ExtData[1]->WorkLocal[39] == 4*) GOTO 0x058E
258: 0x0586 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[12]
259: 0x058B [0x01] GOTO 0x05BE
260: 0x058E [0x02] IF !(ExtData[1]->WorkLocal[39] == 5*) GOTO 0x059E
261: 0x0596 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[13]
262: 0x059B [0x01] GOTO 0x05BE
263: 0x059E [0x02] IF !(ExtData[1]->WorkLocal[39] == 6*) GOTO 0x05AE
264: 0x05A6 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[14]
265: 0x05AB [0x01] GOTO 0x05BE
266: 0x05AE [0x02] IF !(ExtData[1]->WorkLocal[39] == 7*) GOTO 0x05BE
267: 0x05B6 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[15]
268: 0x05BB [0x01] GOTO 0x05BE

SUBROUTINE_05BE:
269: 0x05BE [0x24] CREATE_DIALOG(message_id=7886*, default_option=0*, option_flags=0*)
    → "Value adjuster (Current: $0) [Cancel./+1/+2/+3/+5/+10/+20/+30/+50/+100/+200/+300/+500/+1000/-1/-2/-3/-5/-10/-20/-30/-50/-100/-200/-300/-500/-1000]"
270: 0x05C5 [0x25] WAIT_DIALOG_SELECT()
271: 0x05C6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x05D1
272: 0x05CE [0x01] GOTO 0x05D1

SUBROUTINE_05D1:
273: 0x05D1 [0x02] IF !(Work_Zone[0] <= 0*) GOTO 0x05FF
274: 0x05D9 [0x03] ExtData[1]->WorkLocal[40] = Work_Zone[0]
275: 0x05DE [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[38])
276: 0x05E7 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[39])
277: 0x05F0 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[40])
278: 0x05F9 [0x06] ExtData[1]->WorkLocal[41] = 0
279: 0x05FC [0x06] ExtData[1]->WorkLocal[42] = 0
280: 0x05FF [0x01] GOTO 0x046F
281: 0x0602 [0x01] GOTO 0x0A29
282: 0x0605 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0743
283: 0x060D [0x03] ExtData[1]->WorkLocal[38] = 4*
284: 0x0612 [0x05] ExtData[1]->WorkLocal[42] = 1

SUBROUTINE_0615:
285: 0x0615 [0x02] IF !(ExtData[1]->WorkLocal[42] <= 0*) GOTO 0x0740
286: 0x061D [0x06] ExtData[1]->WorkLocal[39] = 0
287: 0x0620 [0x03] Work_Zone[2] = 1*
288: 0x0625 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[17]
289: 0x062A [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[19]
290: 0x062F [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[20]
291: 0x0634 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[21]
292: 0x0639 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[22]
293: 0x063E [0x24] CREATE_DIALOG(message_id=7885*, default_option=0*, option_flags=0*)
    → "Enemy pop location $0 debug. [Return./Next attack value: $1/Fore Trap attack reduction: $2/Fore Trap delay extension: $3/Rear Trap paralysis duration: $4/Rear Trap paralysis success rate: $5]"
294: 0x0645 [0x25] WAIT_DIALOG_SELECT()
295: 0x0646 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0654
296: 0x064E [0x06] ExtData[1]->WorkLocal[42] = 0
297: 0x0651 [0x01] GOTO 0x06A4
298: 0x0654 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0664
299: 0x065C [0x03] ExtData[1]->WorkLocal[39] = 1*
300: 0x0661 [0x01] GOTO 0x06A4
301: 0x0664 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0674
302: 0x066C [0x03] ExtData[1]->WorkLocal[39] = 2*
303: 0x0671 [0x01] GOTO 0x06A4
304: 0x0674 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0684
305: 0x067C [0x03] ExtData[1]->WorkLocal[39] = 3*
306: 0x0681 [0x01] GOTO 0x06A4
307: 0x0684 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0694
308: 0x068C [0x03] ExtData[1]->WorkLocal[39] = 4*
309: 0x0691 [0x01] GOTO 0x06A4
310: 0x0694 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x06A4
311: 0x069C [0x03] ExtData[1]->WorkLocal[39] = 5*
312: 0x06A1 [0x01] GOTO 0x06A4

SUBROUTINE_06A4:
313: 0x06A4 [0x02] IF !(ExtData[1]->WorkLocal[39] <= 0*) GOTO 0x073D
314: 0x06AC [0x02] IF !(ExtData[1]->WorkLocal[39] == 1*) GOTO 0x06BC
315: 0x06B4 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[17]
316: 0x06B9 [0x01] GOTO 0x06FC
317: 0x06BC [0x02] IF !(ExtData[1]->WorkLocal[39] == 2*) GOTO 0x06CC
318: 0x06C4 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[19]
319: 0x06C9 [0x01] GOTO 0x06FC
320: 0x06CC [0x02] IF !(ExtData[1]->WorkLocal[39] == 3*) GOTO 0x06DC
321: 0x06D4 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[20]
322: 0x06D9 [0x01] GOTO 0x06FC
323: 0x06DC [0x02] IF !(ExtData[1]->WorkLocal[39] == 4*) GOTO 0x06EC
324: 0x06E4 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[21]
325: 0x06E9 [0x01] GOTO 0x06FC
326: 0x06EC [0x02] IF !(ExtData[1]->WorkLocal[39] == 5*) GOTO 0x06FC
327: 0x06F4 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[22]
328: 0x06F9 [0x01] GOTO 0x06FC

SUBROUTINE_06FC:
329: 0x06FC [0x24] CREATE_DIALOG(message_id=7886*, default_option=0*, option_flags=0*)
    → "Value adjuster (Current: $0) [Cancel./+1/+2/+3/+5/+10/+20/+30/+50/+100/+200/+300/+500/+1000/-1/-2/-3/-5/-10/-20/-30/-50/-100/-200/-300/-500/-1000]"
330: 0x0703 [0x25] WAIT_DIALOG_SELECT()
331: 0x0704 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x070F
332: 0x070C [0x01] GOTO 0x070F

SUBROUTINE_070F:
333: 0x070F [0x02] IF !(Work_Zone[0] <= 0*) GOTO 0x073D
334: 0x0717 [0x03] ExtData[1]->WorkLocal[40] = Work_Zone[0]
335: 0x071C [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[38])
336: 0x0725 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[39])
337: 0x072E [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[40])
338: 0x0737 [0x06] ExtData[1]->WorkLocal[41] = 0
339: 0x073A [0x06] ExtData[1]->WorkLocal[42] = 0
340: 0x073D [0x01] GOTO 0x0615
341: 0x0740 [0x01] GOTO 0x0A29
342: 0x0743 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0881
343: 0x074B [0x03] ExtData[1]->WorkLocal[38] = 5*
344: 0x0750 [0x05] ExtData[1]->WorkLocal[42] = 1

SUBROUTINE_0753:
345: 0x0753 [0x02] IF !(ExtData[1]->WorkLocal[42] <= 0*) GOTO 0x087E
346: 0x075B [0x06] ExtData[1]->WorkLocal[39] = 0
347: 0x075E [0x03] Work_Zone[2] = 2*
348: 0x0763 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[24]
349: 0x0768 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[26]
350: 0x076D [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[27]
351: 0x0772 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[28]
352: 0x0777 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[29]
353: 0x077C [0x24] CREATE_DIALOG(message_id=7885*, default_option=0*, option_flags=0*)
    → "Enemy pop location $0 debug. [Return./Next attack value: $1/Fore Trap attack reduction: $2/Fore Trap delay extension: $3/Rear Trap paralysis duration: $4/Rear Trap paralysis success rate: $5]"
354: 0x0783 [0x25] WAIT_DIALOG_SELECT()
355: 0x0784 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0792
356: 0x078C [0x06] ExtData[1]->WorkLocal[42] = 0
357: 0x078F [0x01] GOTO 0x07E2
358: 0x0792 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x07A2
359: 0x079A [0x03] ExtData[1]->WorkLocal[39] = 1*
360: 0x079F [0x01] GOTO 0x07E2
361: 0x07A2 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x07B2
362: 0x07AA [0x03] ExtData[1]->WorkLocal[39] = 2*
363: 0x07AF [0x01] GOTO 0x07E2
364: 0x07B2 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x07C2
365: 0x07BA [0x03] ExtData[1]->WorkLocal[39] = 3*
366: 0x07BF [0x01] GOTO 0x07E2
367: 0x07C2 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x07D2
368: 0x07CA [0x03] ExtData[1]->WorkLocal[39] = 4*
369: 0x07CF [0x01] GOTO 0x07E2
370: 0x07D2 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x07E2
371: 0x07DA [0x03] ExtData[1]->WorkLocal[39] = 5*
372: 0x07DF [0x01] GOTO 0x07E2

SUBROUTINE_07E2:
373: 0x07E2 [0x02] IF !(ExtData[1]->WorkLocal[39] <= 0*) GOTO 0x087B
374: 0x07EA [0x02] IF !(ExtData[1]->WorkLocal[39] == 1*) GOTO 0x07FA
375: 0x07F2 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[24]
376: 0x07F7 [0x01] GOTO 0x083A
377: 0x07FA [0x02] IF !(ExtData[1]->WorkLocal[39] == 2*) GOTO 0x080A
378: 0x0802 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[26]
379: 0x0807 [0x01] GOTO 0x083A
380: 0x080A [0x02] IF !(ExtData[1]->WorkLocal[39] == 3*) GOTO 0x081A
381: 0x0812 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[27]
382: 0x0817 [0x01] GOTO 0x083A
383: 0x081A [0x02] IF !(ExtData[1]->WorkLocal[39] == 4*) GOTO 0x082A
384: 0x0822 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[28]
385: 0x0827 [0x01] GOTO 0x083A
386: 0x082A [0x02] IF !(ExtData[1]->WorkLocal[39] == 5*) GOTO 0x083A
387: 0x0832 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[29]
388: 0x0837 [0x01] GOTO 0x083A

SUBROUTINE_083A:
389: 0x083A [0x24] CREATE_DIALOG(message_id=7886*, default_option=0*, option_flags=0*)
    → "Value adjuster (Current: $0) [Cancel./+1/+2/+3/+5/+10/+20/+30/+50/+100/+200/+300/+500/+1000/-1/-2/-3/-5/-10/-20/-30/-50/-100/-200/-300/-500/-1000]"
390: 0x0841 [0x25] WAIT_DIALOG_SELECT()
391: 0x0842 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x084D
392: 0x084A [0x01] GOTO 0x084D

SUBROUTINE_084D:
393: 0x084D [0x02] IF !(Work_Zone[0] <= 0*) GOTO 0x087B
394: 0x0855 [0x03] ExtData[1]->WorkLocal[40] = Work_Zone[0]
395: 0x085A [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[38])
396: 0x0863 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[39])
397: 0x086C [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[40])
398: 0x0875 [0x06] ExtData[1]->WorkLocal[41] = 0
399: 0x0878 [0x06] ExtData[1]->WorkLocal[42] = 0
400: 0x087B [0x01] GOTO 0x0753
401: 0x087E [0x01] GOTO 0x0A29
402: 0x0881 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x09BF
403: 0x0889 [0x03] ExtData[1]->WorkLocal[38] = 6*
404: 0x088E [0x05] ExtData[1]->WorkLocal[42] = 1

SUBROUTINE_0891:
405: 0x0891 [0x02] IF !(ExtData[1]->WorkLocal[42] <= 0*) GOTO 0x09BC
406: 0x0899 [0x06] ExtData[1]->WorkLocal[39] = 0
407: 0x089C [0x03] Work_Zone[2] = 3*
408: 0x08A1 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[31]
409: 0x08A6 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[33]
410: 0x08AB [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[34]
411: 0x08B0 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[35]
412: 0x08B5 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[36]
413: 0x08BA [0x24] CREATE_DIALOG(message_id=7885*, default_option=0*, option_flags=0*)
    → "Enemy pop location $0 debug. [Return./Next attack value: $1/Fore Trap attack reduction: $2/Fore Trap delay extension: $3/Rear Trap paralysis duration: $4/Rear Trap paralysis success rate: $5]"
414: 0x08C1 [0x25] WAIT_DIALOG_SELECT()
415: 0x08C2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x08D0
416: 0x08CA [0x06] ExtData[1]->WorkLocal[42] = 0
417: 0x08CD [0x01] GOTO 0x0920
418: 0x08D0 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x08E0
419: 0x08D8 [0x03] ExtData[1]->WorkLocal[39] = 1*
420: 0x08DD [0x01] GOTO 0x0920
421: 0x08E0 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x08F0
422: 0x08E8 [0x03] ExtData[1]->WorkLocal[39] = 2*
423: 0x08ED [0x01] GOTO 0x0920
424: 0x08F0 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0900
425: 0x08F8 [0x03] ExtData[1]->WorkLocal[39] = 3*
426: 0x08FD [0x01] GOTO 0x0920
427: 0x0900 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0910
428: 0x0908 [0x03] ExtData[1]->WorkLocal[39] = 4*
429: 0x090D [0x01] GOTO 0x0920
430: 0x0910 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0920
431: 0x0918 [0x03] ExtData[1]->WorkLocal[39] = 5*
432: 0x091D [0x01] GOTO 0x0920

SUBROUTINE_0920:
433: 0x0920 [0x02] IF !(ExtData[1]->WorkLocal[39] <= 0*) GOTO 0x09B9
434: 0x0928 [0x02] IF !(ExtData[1]->WorkLocal[39] == 1*) GOTO 0x0938
435: 0x0930 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[31]
436: 0x0935 [0x01] GOTO 0x0978
437: 0x0938 [0x02] IF !(ExtData[1]->WorkLocal[39] == 2*) GOTO 0x0948
438: 0x0940 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[33]
439: 0x0945 [0x01] GOTO 0x0978
440: 0x0948 [0x02] IF !(ExtData[1]->WorkLocal[39] == 3*) GOTO 0x0958
441: 0x0950 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[34]
442: 0x0955 [0x01] GOTO 0x0978
443: 0x0958 [0x02] IF !(ExtData[1]->WorkLocal[39] == 4*) GOTO 0x0968
444: 0x0960 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[35]
445: 0x0965 [0x01] GOTO 0x0978
446: 0x0968 [0x02] IF !(ExtData[1]->WorkLocal[39] == 5*) GOTO 0x0978
447: 0x0970 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[36]
448: 0x0975 [0x01] GOTO 0x0978

SUBROUTINE_0978:
449: 0x0978 [0x24] CREATE_DIALOG(message_id=7886*, default_option=0*, option_flags=0*)
    → "Value adjuster (Current: $0) [Cancel./+1/+2/+3/+5/+10/+20/+30/+50/+100/+200/+300/+500/+1000/-1/-2/-3/-5/-10/-20/-30/-50/-100/-200/-300/-500/-1000]"
450: 0x097F [0x25] WAIT_DIALOG_SELECT()
451: 0x0980 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x098B
452: 0x0988 [0x01] GOTO 0x098B

SUBROUTINE_098B:
453: 0x098B [0x02] IF !(Work_Zone[0] <= 0*) GOTO 0x09B9
454: 0x0993 [0x03] ExtData[1]->WorkLocal[40] = Work_Zone[0]
455: 0x0998 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[38])
456: 0x09A1 [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[39])
457: 0x09AA [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[40])
458: 0x09B3 [0x06] ExtData[1]->WorkLocal[41] = 0
459: 0x09B6 [0x06] ExtData[1]->WorkLocal[42] = 0
460: 0x09B9 [0x01] GOTO 0x0891
461: 0x09BC [0x01] GOTO 0x0A29
462: 0x09BF [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0A29
463: 0x09C7 [0x03] ExtData[1]->WorkLocal[38] = 7*
464: 0x09CC [0x05] ExtData[1]->WorkLocal[42] = 1

SUBROUTINE_09CF:
465: 0x09CF [0x02] IF !(ExtData[1]->WorkLocal[42] <= 0*) GOTO 0x0A26
466: 0x09D7 [0x06] ExtData[1]->WorkLocal[39] = 0
467: 0x09DA [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
468: 0x09DF [0x24] CREATE_DIALOG(message_id=7886*, default_option=0*, option_flags=0*)
    → "Value adjuster (Current: $0) [Cancel./+1/+2/+3/+5/+10/+20/+30/+50/+100/+200/+300/+500/+1000/-1/-2/-3/-5/-10/-20/-30/-50/-100/-200/-300/-500/-1000]"
469: 0x09E6 [0x25] WAIT_DIALOG_SELECT()
470: 0x09E7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x09F5
471: 0x09EF [0x06] ExtData[1]->WorkLocal[41] = 0
472: 0x09F2 [0x01] GOTO 0x09F5

SUBROUTINE_09F5:
473: 0x09F5 [0x02] IF !(Work_Zone[0] <= 0*) GOTO 0x0A23
474: 0x09FD [0x03] ExtData[1]->WorkLocal[40] = Work_Zone[0]
475: 0x0A02 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[38])
476: 0x0A0B [0x40] SET_BIT_WORK_RANGE(start_bit=8*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[39])
477: 0x0A14 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[40])
478: 0x0A1D [0x06] ExtData[1]->WorkLocal[41] = 0
479: 0x0A20 [0x06] ExtData[1]->WorkLocal[42] = 0
480: 0x0A23 [0x01] GOTO 0x09CF
481: 0x0A26 [0x01] GOTO 0x0A29

SUBROUTINE_0A29:
482: 0x0A29 [0x01] GOTO 0x01BC
483: 0x0A2C [0x21] END_EVENT
484: 0x0A2D [0x00] END_REQSTACK()
```
