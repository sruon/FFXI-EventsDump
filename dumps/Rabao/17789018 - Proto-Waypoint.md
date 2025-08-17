# 17789018 - Proto-Waypoint

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Rabao (ID: 247) |
| Block Size       | 3092 bytes      |
| Total Events     | 5               |
| References Count | 55              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [141](#event-141)        | 0x0001       |   2102 |            424 |
| [142](#event-142)        | 0x0837       |     72 |             13 |
| [65535.1](#event-655351) | 0x087F       |    658 |             62 |
| [151](#event-151)        | 0x0B11       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x001E      |          30 |
|       2 | 0x008C      |         140 |
|       3 | 0x006E      |         110 |
|       4 | 0x0002      |           2 |
|       5 | 0x1FFFFFFC  |   536870908 |
|       6 | 0x2FFFFFFC  |   805306364 |
|       7 | 0x00F3      |         243 |
|       8 | 0x0001      |           1 |
|       9 | 0x00F8      |         248 |
|      10 | 0x0003      |           3 |
|      11 | 0x00F9      |         249 |
|      12 | 0x0004      |           4 |
|      13 | 0x00F7      |         247 |
|      14 | 0x0005      |           5 |
|      15 | 0x00FC      |         252 |
|      16 | 0x0006      |           6 |
|      17 | 0xC350      |       50000 |
|      18 | 0x0064      |         100 |
|      19 | 0x012C      |         300 |
|      20 | 0x2DB1      |       11697 |
|      21 | 0x2DA3      |       11683 |
|      22 | 0x2DA4      |       11684 |
|      23 | 0x2DB0      |       11696 |
|      24 | 0x0007      |           7 |
|      25 | 0x0008      |           8 |
|      26 | 0x0009      |           9 |
|      27 | 0x000A      |          10 |
|      28 | 0x000B      |          11 |
|      29 | 0x000C      |          12 |
|      30 | 0x000D      |          13 |
|      31 | 0x000E      |          14 |
|      32 | 0x000F      |          15 |
|      33 | 0x0010      |          16 |
|      34 | 0x0011      |          17 |
|      35 | 0x0012      |          18 |
|      36 | 0x0013      |          19 |
|      37 | 0x0014      |          20 |
|      38 | 0x0015      |          21 |
|      39 | 0x0016      |          22 |
|      40 | 0x0017      |          23 |
|      41 | 0x0018      |          24 |
|      42 | 0x0019      |          25 |
|      43 | 0x001A      |          26 |
|      44 | 0x001B      |          27 |
|      45 | 0x001C      |          28 |
|      46 | 0x001D      |          29 |
|      47 | 0x2DAE      |       11694 |
|      48 | 0x2DAF      |       11695 |
|      49 | 0x0063      |          99 |
|      50 | 0x005A      |          90 |
|      51 | 0x00C8      |         200 |
|      52 | 0x00C9      |         201 |
|      53 | 0x002D      |          45 |
|      54 | 0x00D7      |         215 |

## String References

- **11683**: Leaning in closely to the device, one can make out miniscule etchings that read, "Trade various crystals to this waypoint to receive kinetic units that may be used when you wish to warp to another locale."
- **11684**: "Travelers may not possess more than $1 at a given time. Should someone trade an amount of crystals that would result in a surplus of kinetic units, those units will be lost to the aether."
- **11694**: You will not be asked to confirm your choice of destination. Switching to simple teleporation mode.
- **11695**: You will be asked to confirm your choice of destination. Returning to normal teleportation mode.
- **11696**: Warp to your destination? [Yes./No.]
- **11697**: Where will you go? (Kinetic Units: $3) [Nowhere, thanks./I'd rather read an explanation./Ru'Lude Gardens. ($4 unit[/s])/Selbina. ($4 unit[/s])/Mhaura. ($4 unit[/s])/Rabao. ($4 unit[/s])/Norg. ($4 unit[/s])/West Ronfaure. ($5 unit[/s])/North Gustaberg. ($5 unit[/s])/West Sarutabaruta. ($5 unit[/s])/La Theine Plateau. ($5 unit[/s])/Konschtat Highlands. ($5 unit[/s])/Tahrongi Canyon. ($5 unit[/s])/Jugner Forest. ($5 unit[/s])/Pashhow Marshlands. ($5 unit[/s])/Meriphataud Mountains. ($5 unit[/s])/Attohwa Chasm. ($5 unit[/s])/Uleguerand Range. ($5 unit[/s])/Davoi. ($6 unit[/s])/Beadeaux. ($6 unit[/s])/Castle Oztroja. ($6 unit[/s])/Quicksand Caves. ($6 unit[/s])/Sea Serpent Grotto. ($6 unit[/s])/Temple of Uggalepih. ($6 unit[/s])/The Boyahda Tree. ($6 unit[/s])/Oldton Movalpolos. ($6 unit[/s])/Riverne - Site #B01. ($6 unit[/s])/Castle Zvahl Keep. ($6 unit[/s])/Decline destination confirmation./Accept destination confirmation.]

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

### Event 141

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 2102 bytes |
| Instructions | 370        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 00 80 03 00  00 02 10 03 02 00 05 10   ...............
0010: 03 01 00 04 10 03 03 00  06 10 4A F0 FF FF 7F F8  ..........J.....
0020: FF FF 7F 02 03 00 01 80  00 2E 00 01 43 00 42 CD  ............C.B.
0030: 02 80 F8 FF FF 7F F8 FF  FF 7F 73 30 30 30 00 80  ..........s000..
0040: 1C 03 80 10 00 00 04 80  02 03 00 01 80 00 58 00  ..............X.
0050: 0F 00 00 05 80 01 5D 00  0F 00 00 06 80 02 01 00  ......].........
0060: 07 80 80 6F 00 3C 00 00  04 80 08 80 01 B7 00 02  ...o.<..........
0070: 01 00 09 80 80 81 00 3C  00 00 0A 80 08 80 01 B7  .......<........
0080: 00 02 01 00 0B 80 80 93  00 3C 00 00 0C 80 08 80  .........<......
0090: 01 B7 00 02 01 00 0D 80  80 A5 00 3C 00 00 0E 80  ...........<....
00A0: 08 80 01 B7 00 02 01 00  0F 80 80 B7 00 3C 00 00  .............<..
00B0: 10 80 08 80 01 B7 00 03  01 10 00 80 03 03 10 11  ................
00C0: 80 03 05 10 02 00 03 06  10 01 80 03 07 10 12 80  ................
00D0: 03 08 10 13 80 24 14 80  00 80 00 00 25 02 00 10  .....$......%...
00E0: 00 80 00 ED 00 1A 0B 08  21 00 01 CF 07 02 00 10  ........!.......
00F0: 08 80 00 03 01 48 15 80  23 48 16 80 23 01 B7 00  .....H..#H..#...
0100: 01 CF 07 02 00 10 04 80  00 44 01 02 03 00 01 80  .........D......
0110: 00 1B 01 03 01 10 0C 80  01 41 01 24 17 80 08 80  .........A.$....
0120: 00 80 25 02 00 10 00 80  00 33 01 03 01 10 0C 80  ..%......3......
0130: 01 41 01 02 00 10 08 80  00 41 01 01 B7 00 01 41  .A.......A.....A
0140: 01 01 CF 07 02 00 10 0A  80 00 85 01 02 03 00 01  ................
0150: 80 00 5C 01 03 01 10 0E  80 01 82 01 24 17 80 08  ..\.........$...
0160: 80 00 80 25 02 00 10 00  80 00 74 01 03 01 10 0E  ...%......t.....
0170: 80 01 82 01 02 00 10 08  80 00 82 01 01 B7 00 01  ................
0180: 82 01 01 CF 07 02 00 10  0C 80 00 C6 01 02 03 00  ................
0190: 01 80 00 9D 01 03 01 10  10 80 01 C3 01 24 17 80  .............$..
01A0: 08 80 00 80 25 02 00 10  00 80 00 B5 01 03 01 10  ....%...........
01B0: 10 80 01 C3 01 02 00 10  08 80 00 C3 01 01 B7 00  ................
01C0: 01 C3 01 01 CF 07 02 00  10 0E 80 00 07 02 02 03  ................
01D0: 00 01 80 00 DE 01 03 01  10 18 80 01 04 02 24 17  ..............$.
01E0: 80 08 80 00 80 25 02 00  10 00 80 00 F6 01 03 01  .....%..........
01F0: 10 18 80 01 04 02 02 00  10 08 80 00 04 02 01 B7  ................
0200: 00 01 04 02 01 CF 07 02  00 10 10 80 00 48 02 02  .............H..
0210: 03 00 01 80 00 1F 02 03  01 10 19 80 01 45 02 24  .............E.$
0220: 17 80 08 80 00 80 25 02  00 10 00 80 00 37 02 03  ......%......7..
0230: 01 10 19 80 01 45 02 02  00 10 08 80 00 45 02 01  .....E.......E..
0240: B7 00 01 45 02 01 CF 07  02 00 10 18 80 00 89 02  ...E............
0250: 02 03 00 01 80 00 60 02  03 01 10 1A 80 01 86 02  ......`.........
0260: 24 17 80 08 80 00 80 25  02 00 10 00 80 00 78 02  $......%......x.
0270: 03 01 10 1A 80 01 86 02  02 00 10 08 80 00 86 02  ................
0280: 01 B7 00 01 86 02 01 CF  07 02 00 10 19 80 00 CA  ................
0290: 02 02 03 00 01 80 00 A1  02 03 01 10 1B 80 01 C7  ................
02A0: 02 24 17 80 08 80 00 80  25 02 00 10 00 80 00 B9  .$......%.......
02B0: 02 03 01 10 1B 80 01 C7  02 02 00 10 08 80 00 C7  ................
02C0: 02 01 B7 00 01 C7 02 01  CF 07 02 00 10 1A 80 00  ................
02D0: 0B 03 02 03 00 01 80 00  E2 02 03 01 10 1C 80 01  ................
02E0: 08 03 24 17 80 08 80 00  80 25 02 00 10 00 80 00  ..$......%......
02F0: FA 02 03 01 10 1C 80 01  08 03 02 00 10 08 80 00  ................
0300: 08 03 01 B7 00 01 08 03  01 CF 07 02 00 10 1B 80  ................
0310: 00 4C 03 02 03 00 01 80  00 23 03 03 01 10 1D 80  .L.......#......
0320: 01 49 03 24 17 80 08 80  00 80 25 02 00 10 00 80  .I.$......%.....
0330: 00 3B 03 03 01 10 1D 80  01 49 03 02 00 10 08 80  .;.......I......
0340: 00 49 03 01 B7 00 01 49  03 01 CF 07 02 00 10 1C  .I.....I........
0350: 80 00 8D 03 02 03 00 01  80 00 64 03 03 01 10 1E  ..........d.....
0360: 80 01 8A 03 24 17 80 08  80 00 80 25 02 00 10 00  ....$......%....
0370: 80 00 7C 03 03 01 10 1E  80 01 8A 03 02 00 10 08  ..|.............
0380: 80 00 8A 03 01 B7 00 01  8A 03 01 CF 07 02 00 10  ................
0390: 1D 80 00 CE 03 02 03 00  01 80 00 A5 03 03 01 10  ................
03A0: 1F 80 01 CB 03 24 17 80  08 80 00 80 25 02 00 10  .....$......%...
03B0: 00 80 00 BD 03 03 01 10  1F 80 01 CB 03 02 00 10  ................
03C0: 08 80 00 CB 03 01 B7 00  01 CB 03 01 CF 07 02 00  ................
03D0: 10 1E 80 00 0F 04 02 03  00 01 80 00 E6 03 03 01  ................
03E0: 10 20 80 01 0C 04 24 17  80 08 80 00 80 25 02 00  . ....$......%..
03F0: 10 00 80 00 FE 03 03 01  10 20 80 01 0C 04 02 00  ......... ......
0400: 10 08 80 00 0C 04 01 B7  00 01 0C 04 01 CF 07 02  ................
0410: 00 10 1F 80 00 50 04 02  03 00 01 80 00 27 04 03  .....P.......'..
0420: 01 10 21 80 01 4D 04 24  17 80 08 80 00 80 25 02  ..!..M.$......%.
0430: 00 10 00 80 00 3F 04 03  01 10 21 80 01 4D 04 02  .....?....!..M..
0440: 00 10 08 80 00 4D 04 01  B7 00 01 4D 04 01 CF 07  .....M.....M....
0450: 02 00 10 20 80 00 91 04  02 03 00 01 80 00 68 04  ... ..........h.
0460: 03 01 10 22 80 01 8E 04  24 17 80 08 80 00 80 25  ..."....$......%
0470: 02 00 10 00 80 00 80 04  03 01 10 22 80 01 8E 04  ..........."....
0480: 02 00 10 08 80 00 8E 04  01 B7 00 01 8E 04 01 CF  ................
0490: 07 02 00 10 21 80 00 D2  04 02 03 00 01 80 00 A9  ....!...........
04A0: 04 03 01 10 23 80 01 CF  04 24 17 80 08 80 00 80  ....#....$......
04B0: 25 02 00 10 00 80 00 C1  04 03 01 10 23 80 01 CF  %...........#...
04C0: 04 02 00 10 08 80 00 CF  04 01 B7 00 01 CF 04 01  ................
04D0: CF 07 02 00 10 22 80 00  13 05 02 03 00 01 80 00  ....."..........
04E0: EA 04 03 01 10 24 80 01  10 05 24 17 80 08 80 00  .....$....$.....
04F0: 80 25 02 00 10 00 80 00  02 05 03 01 10 24 80 01  .%...........$..
0500: 10 05 02 00 10 08 80 00  10 05 01 B7 00 01 10 05  ................
0510: 01 CF 07 02 00 10 23 80  00 54 05 02 03 00 01 80  ......#..T......
0520: 00 2B 05 03 01 10 25 80  01 51 05 24 17 80 08 80  .+....%..Q.$....
0530: 00 80 25 02 00 10 00 80  00 43 05 03 01 10 25 80  ..%......C....%.
0540: 01 51 05 02 00 10 08 80  00 51 05 01 B7 00 01 51  .Q.......Q.....Q
0550: 05 01 CF 07 02 00 10 24  80 00 95 05 02 03 00 01  .......$........
0560: 80 00 6C 05 03 01 10 26  80 01 92 05 24 17 80 08  ..l....&....$...
0570: 80 00 80 25 02 00 10 00  80 00 84 05 03 01 10 26  ...%...........&
0580: 80 01 92 05 02 00 10 08  80 00 92 05 01 B7 00 01  ................
0590: 92 05 01 CF 07 02 00 10  25 80 00 D6 05 02 03 00  ........%.......
05A0: 01 80 00 AD 05 03 01 10  27 80 01 D3 05 24 17 80  ........'....$..
05B0: 08 80 00 80 25 02 00 10  00 80 00 C5 05 03 01 10  ....%...........
05C0: 27 80 01 D3 05 02 00 10  08 80 00 D3 05 01 B7 00  '...............
05D0: 01 D3 05 01 CF 07 02 00  10 26 80 00 17 06 02 03  .........&......
05E0: 00 01 80 00 EE 05 03 01  10 28 80 01 14 06 24 17  .........(....$.
05F0: 80 08 80 00 80 25 02 00  10 00 80 00 06 06 03 01  .....%..........
0600: 10 28 80 01 14 06 02 00  10 08 80 00 14 06 01 B7  .(..............
0610: 00 01 14 06 01 CF 07 02  00 10 27 80 00 58 06 02  ..........'..X..
0620: 03 00 01 80 00 2F 06 03  01 10 29 80 01 55 06 24  ...../....)..U.$
0630: 17 80 08 80 00 80 25 02  00 10 00 80 00 47 06 03  ......%......G..
0640: 01 10 29 80 01 55 06 02  00 10 08 80 00 55 06 01  ..)..U.......U..
0650: B7 00 01 55 06 01 CF 07  02 00 10 28 80 00 99 06  ...U.......(....
0660: 02 03 00 01 80 00 70 06  03 01 10 2A 80 01 96 06  ......p....*....
0670: 24 17 80 08 80 00 80 25  02 00 10 00 80 00 88 06  $......%........
0680: 03 01 10 2A 80 01 96 06  02 00 10 08 80 00 96 06  ...*............
0690: 01 B7 00 01 96 06 01 CF  07 02 00 10 29 80 00 DA  ............)...
06A0: 06 02 03 00 01 80 00 B1  06 03 01 10 2B 80 01 D7  ............+...
06B0: 06 24 17 80 08 80 00 80  25 02 00 10 00 80 00 C9  .$......%.......
06C0: 06 03 01 10 2B 80 01 D7  06 02 00 10 08 80 00 D7  ....+...........
06D0: 06 01 B7 00 01 D7 06 01  CF 07 02 00 10 2A 80 00  .............*..
06E0: 1B 07 02 03 00 01 80 00  F2 06 03 01 10 2C 80 01  .............,..
06F0: 18 07 24 17 80 08 80 00  80 25 02 00 10 00 80 00  ..$......%......
0700: 0A 07 03 01 10 2C 80 01  18 07 02 00 10 08 80 00  .....,..........
0710: 18 07 01 B7 00 01 18 07  01 CF 07 02 00 10 2B 80  ..............+.
0720: 00 5C 07 02 03 00 01 80  00 33 07 03 01 10 2D 80  .\.......3....-.
0730: 01 59 07 24 17 80 08 80  00 80 25 02 00 10 00 80  .Y.$......%.....
0740: 00 4B 07 03 01 10 2D 80  01 59 07 02 00 10 08 80  .K....-..Y......
0750: 00 59 07 01 B7 00 01 59  07 01 CF 07 02 00 10 2C  .Y.....Y.......,
0760: 80 00 9D 07 02 03 00 01  80 00 74 07 03 01 10 2E  ..........t.....
0770: 80 01 9A 07 24 17 80 08  80 00 80 25 02 00 10 00  ....$......%....
0780: 80 00 8C 07 03 01 10 2E  80 01 9A 07 02 00 10 08  ................
0790: 80 00 9A 07 01 B7 00 01  9A 07 01 CF 07 02 00 10  ................
07A0: 2D 80 00 B6 07 03 01 10  04 80 48 2F 80 23 1A 0B  -.........H/.#..
07B0: 08 21 00 01 CF 07 02 00  10 2E 80 00 CF 07 03 01  .!..............
07C0: 10 0A 80 48 30 80 23 1A  0B 08 21 00 01 CF 07 43  ...H0.#...!....C
07D0: 00 43 01 02 02 10 00 80  01 E6 07 03 01 10 31 80  .C............1.
07E0: 1A 0B 08 01 09 08 CD 02  80 F8 FF FF 7F F0 FF FF  ................
07F0: 7F 6D 61 69 6E 00 80 1C  32 80 92 01 F0 FF FF 7F  .main...2.......
0800: 1C 01 80 1A E3 08 1C 01  80 21 00 02 03 00 01 80  .........!......
0810: 00 16 08 01 36 08 CE 02  80 F8 FF FF 7F F8 FF FF  ....6...........
0820: 7F 73 30 30 30 CD 02 80  F8 FF FF 7F F8 FF FF 7F  .s000...........
0830: 73 74 70 30 00 80 1B                              stp0...         
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  2: 0x000B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[5]
  3: 0x0010 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[4]
  4: 0x0015 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[6]
  5: 0x001A [0x4A] LocalPlayer looks at EventEntity
  6: 0x0023 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x002E
  7: 0x002B [0x01] GOTO 0x0043
  8: 0x002E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x002F [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "s000" with entities [EventEntity, EventEntity], work=[140*, 0*]
 10: 0x0040 [0x1C] WAIT(110* ticks)

SUBROUTINE_0043:
 11: 0x0043 [0x10] ExtData[1]->WorkLocal[0] <<= 2*
 12: 0x0048 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0058
 13: 0x0050 [0x0F] ExtData[1]->WorkLocal[0] ^= 536870908*
 14: 0x0055 [0x01] GOTO 0x005D
 15: 0x0058 [0x0F] ExtData[1]->WorkLocal[0] ^= 805306364*

SUBROUTINE_005D:
 16: 0x005D [0x02] IF !(ExtData[1]->WorkLocal[1] == 243*) GOTO 0x006F
 17: 0x0065 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=2*, condition_work_offset=1*)
 18: 0x006C [0x01] GOTO 0x00B7
 19: 0x006F [0x02] IF !(ExtData[1]->WorkLocal[1] == 248*) GOTO 0x0081
 20: 0x0077 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=3*, condition_work_offset=1*)
 21: 0x007E [0x01] GOTO 0x00B7
 22: 0x0081 [0x02] IF !(ExtData[1]->WorkLocal[1] == 249*) GOTO 0x0093
 23: 0x0089 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=4*, condition_work_offset=1*)
 24: 0x0090 [0x01] GOTO 0x00B7
 25: 0x0093 [0x02] IF !(ExtData[1]->WorkLocal[1] == 247*) GOTO 0x00A5
 26: 0x009B [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=5*, condition_work_offset=1*)
 27: 0x00A2 [0x01] GOTO 0x00B7
 28: 0x00A5 [0x02] IF !(ExtData[1]->WorkLocal[1] == 252*) GOTO 0x00B7
 29: 0x00AD [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=6*, condition_work_offset=1*)
 30: 0x00B4 [0x01] GOTO 0x00B7

SUBROUTINE_00B7:
 31: 0x00B7 [0x03] Work_Zone[1] = 0*
 32: 0x00BC [0x03] Work_Zone[3] = 50000*
 33: 0x00C1 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[2]
 34: 0x00C6 [0x03] Work_Zone[6] = 30*
 35: 0x00CB [0x03] Work_Zone[7] = 100*
 36: 0x00D0 [0x03] Work_Zone[8] = 300*
 37: 0x00D5 [0x24] CREATE_DIALOG(message_id=11697*, default_option=0*, option_flags=ExtData[1]->WorkLocal[0])
    → "Where will you go? (Kinetic Units: $3) [Nowhere, thanks./I'd rather read an explanation./Ru'Lude Gardens. ($4 unit[/s])/Selbina. ($4 unit[/s])/Mhaura. ($4 unit[/s])/Rabao. ($4 unit[/s])/Norg. ($4 unit[/s])/West Ronfaure. ($5 unit[/s])/North Gustaberg. ($5 unit[/s])/West Sarutabaruta. ($5 unit[/s])/La Theine Plateau. ($5 unit[/s])/Konschtat Highlands. ($5 unit[/s])/Tahrongi Canyon. ($5 unit[/s])/Jugner Forest. ($5 unit[/s])/Pashhow Marshlands. ($5 unit[/s])/Meriphataud Mountains. ($5 unit[/s])/Attohwa Chasm. ($5 unit[/s])/Uleguerand Range. ($5 unit[/s])/Davoi. ($6 unit[/s])/Beadeaux. ($6 unit[/s])/Castle Oztroja. ($6 unit[/s])/Quicksand Caves. ($6 unit[/s])/Sea Serpent Grotto. ($6 unit[/s])/Temple of Uggalepih. ($6 unit[/s])/The Boyahda Tree. ($6 unit[/s])/Oldton Movalpolos. ($6 unit[/s])/Riverne - Site #B01. ($6 unit[/s])/Castle Zvahl Keep. ($6 unit[/s])/Decline destination confirmation./Accept destination confirmation.]"
 38: 0x00DC [0x25] WAIT_DIALOG_SELECT()
 39: 0x00DD [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00ED
 40: 0x00E5 [0x1A] CALL_SUBROUTINE(address=0x080B)
 41: 0x00E8 [0x21] END_EVENT
 42: 0x00E9 [0x00] END_REQSTACK()

SUBROUTINE_0141:
 43: 0x0141 [0x01] GOTO 0x07CF
 44: 0x0144 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0185
 45: 0x014C [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x015C
 46: 0x0154 [0x03] Work_Zone[1] = 5*
 47: 0x0159 [0x01] GOTO 0x0182
 48: 0x015C [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
 49: 0x0163 [0x25] WAIT_DIALOG_SELECT()
 50: 0x0164 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0174
 51: 0x016C [0x03] Work_Zone[1] = 5*
 52: 0x0171 [0x01] GOTO 0x0182
 53: 0x0174 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0182
 54: 0x017C [0x01] GOTO 0x00B7

SUBROUTINE_0182:
 55: 0x0182 [0x01] GOTO 0x07CF
 56: 0x0185 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x01C6
 57: 0x018D [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x019D
 58: 0x0195 [0x03] Work_Zone[1] = 6*
 59: 0x019A [0x01] GOTO 0x01C3
 60: 0x019D [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
 61: 0x01A4 [0x25] WAIT_DIALOG_SELECT()
 62: 0x01A5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01B5
 63: 0x01AD [0x03] Work_Zone[1] = 6*
 64: 0x01B2 [0x01] GOTO 0x01C3
 65: 0x01B5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01C3
 66: 0x01BD [0x01] GOTO 0x00B7

SUBROUTINE_01C3:
 67: 0x01C3 [0x01] GOTO 0x07CF
 68: 0x01C6 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0207
 69: 0x01CE [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x01DE
 70: 0x01D6 [0x03] Work_Zone[1] = 7*
 71: 0x01DB [0x01] GOTO 0x0204
 72: 0x01DE [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
 73: 0x01E5 [0x25] WAIT_DIALOG_SELECT()
 74: 0x01E6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01F6
 75: 0x01EE [0x03] Work_Zone[1] = 7*
 76: 0x01F3 [0x01] GOTO 0x0204
 77: 0x01F6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0204
 78: 0x01FE [0x01] GOTO 0x00B7

SUBROUTINE_0204:
 79: 0x0204 [0x01] GOTO 0x07CF
 80: 0x0207 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0248
 81: 0x020F [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x021F
 82: 0x0217 [0x03] Work_Zone[1] = 8*
 83: 0x021C [0x01] GOTO 0x0245
 84: 0x021F [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
 85: 0x0226 [0x25] WAIT_DIALOG_SELECT()
 86: 0x0227 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0237
 87: 0x022F [0x03] Work_Zone[1] = 8*
 88: 0x0234 [0x01] GOTO 0x0245
 89: 0x0237 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0245
 90: 0x023F [0x01] GOTO 0x00B7

SUBROUTINE_0245:
 91: 0x0245 [0x01] GOTO 0x07CF
 92: 0x0248 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0289
 93: 0x0250 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0260
 94: 0x0258 [0x03] Work_Zone[1] = 9*
 95: 0x025D [0x01] GOTO 0x0286
 96: 0x0260 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
 97: 0x0267 [0x25] WAIT_DIALOG_SELECT()
 98: 0x0268 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0278
 99: 0x0270 [0x03] Work_Zone[1] = 9*
100: 0x0275 [0x01] GOTO 0x0286
101: 0x0278 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0286
102: 0x0280 [0x01] GOTO 0x00B7

SUBROUTINE_0286:
103: 0x0286 [0x01] GOTO 0x07CF
104: 0x0289 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x02CA
105: 0x0291 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x02A1
106: 0x0299 [0x03] Work_Zone[1] = 10*
107: 0x029E [0x01] GOTO 0x02C7
108: 0x02A1 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
109: 0x02A8 [0x25] WAIT_DIALOG_SELECT()
110: 0x02A9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02B9
111: 0x02B1 [0x03] Work_Zone[1] = 10*
112: 0x02B6 [0x01] GOTO 0x02C7
113: 0x02B9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02C7
114: 0x02C1 [0x01] GOTO 0x00B7

SUBROUTINE_02C7:
115: 0x02C7 [0x01] GOTO 0x07CF
116: 0x02CA [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x030B
117: 0x02D2 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x02E2
118: 0x02DA [0x03] Work_Zone[1] = 11*
119: 0x02DF [0x01] GOTO 0x0308
120: 0x02E2 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
121: 0x02E9 [0x25] WAIT_DIALOG_SELECT()
122: 0x02EA [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02FA
123: 0x02F2 [0x03] Work_Zone[1] = 11*
124: 0x02F7 [0x01] GOTO 0x0308
125: 0x02FA [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0308
126: 0x0302 [0x01] GOTO 0x00B7

SUBROUTINE_0308:
127: 0x0308 [0x01] GOTO 0x07CF
128: 0x030B [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x034C
129: 0x0313 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0323
130: 0x031B [0x03] Work_Zone[1] = 12*
131: 0x0320 [0x01] GOTO 0x0349
132: 0x0323 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
133: 0x032A [0x25] WAIT_DIALOG_SELECT()
134: 0x032B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x033B
135: 0x0333 [0x03] Work_Zone[1] = 12*
136: 0x0338 [0x01] GOTO 0x0349
137: 0x033B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0349
138: 0x0343 [0x01] GOTO 0x00B7

SUBROUTINE_0349:
139: 0x0349 [0x01] GOTO 0x07CF
140: 0x034C [0x02] IF !(Work_Zone[0] == 11*) GOTO 0x038D
141: 0x0354 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0364
142: 0x035C [0x03] Work_Zone[1] = 13*
143: 0x0361 [0x01] GOTO 0x038A
144: 0x0364 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
145: 0x036B [0x25] WAIT_DIALOG_SELECT()
146: 0x036C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x037C
147: 0x0374 [0x03] Work_Zone[1] = 13*
148: 0x0379 [0x01] GOTO 0x038A
149: 0x037C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x038A
150: 0x0384 [0x01] GOTO 0x00B7

SUBROUTINE_038A:
151: 0x038A [0x01] GOTO 0x07CF
152: 0x038D [0x02] IF !(Work_Zone[0] == 12*) GOTO 0x03CE
153: 0x0395 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x03A5
154: 0x039D [0x03] Work_Zone[1] = 14*
155: 0x03A2 [0x01] GOTO 0x03CB
156: 0x03A5 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
157: 0x03AC [0x25] WAIT_DIALOG_SELECT()
158: 0x03AD [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03BD
159: 0x03B5 [0x03] Work_Zone[1] = 14*
160: 0x03BA [0x01] GOTO 0x03CB
161: 0x03BD [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03CB
162: 0x03C5 [0x01] GOTO 0x00B7

SUBROUTINE_03CB:
163: 0x03CB [0x01] GOTO 0x07CF
164: 0x03CE [0x02] IF !(Work_Zone[0] == 13*) GOTO 0x040F
165: 0x03D6 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x03E6
166: 0x03DE [0x03] Work_Zone[1] = 15*
167: 0x03E3 [0x01] GOTO 0x040C
168: 0x03E6 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
169: 0x03ED [0x25] WAIT_DIALOG_SELECT()
170: 0x03EE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03FE
171: 0x03F6 [0x03] Work_Zone[1] = 15*
172: 0x03FB [0x01] GOTO 0x040C
173: 0x03FE [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x040C
174: 0x0406 [0x01] GOTO 0x00B7

SUBROUTINE_040C:
175: 0x040C [0x01] GOTO 0x07CF
176: 0x040F [0x02] IF !(Work_Zone[0] == 14*) GOTO 0x0450
177: 0x0417 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0427
178: 0x041F [0x03] Work_Zone[1] = 16*
179: 0x0424 [0x01] GOTO 0x044D
180: 0x0427 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
181: 0x042E [0x25] WAIT_DIALOG_SELECT()
182: 0x042F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x043F
183: 0x0437 [0x03] Work_Zone[1] = 16*
184: 0x043C [0x01] GOTO 0x044D
185: 0x043F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x044D
186: 0x0447 [0x01] GOTO 0x00B7

SUBROUTINE_044D:
187: 0x044D [0x01] GOTO 0x07CF
188: 0x0450 [0x02] IF !(Work_Zone[0] == 15*) GOTO 0x0491
189: 0x0458 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0468
190: 0x0460 [0x03] Work_Zone[1] = 17*
191: 0x0465 [0x01] GOTO 0x048E
192: 0x0468 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
193: 0x046F [0x25] WAIT_DIALOG_SELECT()
194: 0x0470 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0480
195: 0x0478 [0x03] Work_Zone[1] = 17*
196: 0x047D [0x01] GOTO 0x048E
197: 0x0480 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x048E
198: 0x0488 [0x01] GOTO 0x00B7

SUBROUTINE_048E:
199: 0x048E [0x01] GOTO 0x07CF
200: 0x0491 [0x02] IF !(Work_Zone[0] == 16*) GOTO 0x04D2
201: 0x0499 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x04A9
202: 0x04A1 [0x03] Work_Zone[1] = 18*
203: 0x04A6 [0x01] GOTO 0x04CF
204: 0x04A9 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
205: 0x04B0 [0x25] WAIT_DIALOG_SELECT()
206: 0x04B1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x04C1
207: 0x04B9 [0x03] Work_Zone[1] = 18*
208: 0x04BE [0x01] GOTO 0x04CF
209: 0x04C1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x04CF
210: 0x04C9 [0x01] GOTO 0x00B7

SUBROUTINE_04CF:
211: 0x04CF [0x01] GOTO 0x07CF
212: 0x04D2 [0x02] IF !(Work_Zone[0] == 17*) GOTO 0x0513
213: 0x04DA [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x04EA
214: 0x04E2 [0x03] Work_Zone[1] = 19*
215: 0x04E7 [0x01] GOTO 0x0510
216: 0x04EA [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
217: 0x04F1 [0x25] WAIT_DIALOG_SELECT()
218: 0x04F2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0502
219: 0x04FA [0x03] Work_Zone[1] = 19*
220: 0x04FF [0x01] GOTO 0x0510
221: 0x0502 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0510
222: 0x050A [0x01] GOTO 0x00B7

SUBROUTINE_0510:
223: 0x0510 [0x01] GOTO 0x07CF
224: 0x0513 [0x02] IF !(Work_Zone[0] == 18*) GOTO 0x0554
225: 0x051B [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x052B
226: 0x0523 [0x03] Work_Zone[1] = 20*
227: 0x0528 [0x01] GOTO 0x0551
228: 0x052B [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
229: 0x0532 [0x25] WAIT_DIALOG_SELECT()
230: 0x0533 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0543
231: 0x053B [0x03] Work_Zone[1] = 20*
232: 0x0540 [0x01] GOTO 0x0551
233: 0x0543 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0551
234: 0x054B [0x01] GOTO 0x00B7

SUBROUTINE_0551:
235: 0x0551 [0x01] GOTO 0x07CF
236: 0x0554 [0x02] IF !(Work_Zone[0] == 19*) GOTO 0x0595
237: 0x055C [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x056C
238: 0x0564 [0x03] Work_Zone[1] = 21*
239: 0x0569 [0x01] GOTO 0x0592
240: 0x056C [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
241: 0x0573 [0x25] WAIT_DIALOG_SELECT()
242: 0x0574 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0584
243: 0x057C [0x03] Work_Zone[1] = 21*
244: 0x0581 [0x01] GOTO 0x0592
245: 0x0584 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0592
246: 0x058C [0x01] GOTO 0x00B7

SUBROUTINE_0592:
247: 0x0592 [0x01] GOTO 0x07CF
248: 0x0595 [0x02] IF !(Work_Zone[0] == 20*) GOTO 0x05D6
249: 0x059D [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x05AD
250: 0x05A5 [0x03] Work_Zone[1] = 22*
251: 0x05AA [0x01] GOTO 0x05D3
252: 0x05AD [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
253: 0x05B4 [0x25] WAIT_DIALOG_SELECT()
254: 0x05B5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x05C5
255: 0x05BD [0x03] Work_Zone[1] = 22*
256: 0x05C2 [0x01] GOTO 0x05D3
257: 0x05C5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x05D3
258: 0x05CD [0x01] GOTO 0x00B7

SUBROUTINE_05D3:
259: 0x05D3 [0x01] GOTO 0x07CF
260: 0x05D6 [0x02] IF !(Work_Zone[0] == 21*) GOTO 0x0617
261: 0x05DE [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x05EE
262: 0x05E6 [0x03] Work_Zone[1] = 23*
263: 0x05EB [0x01] GOTO 0x0614
264: 0x05EE [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
265: 0x05F5 [0x25] WAIT_DIALOG_SELECT()
266: 0x05F6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0606
267: 0x05FE [0x03] Work_Zone[1] = 23*
268: 0x0603 [0x01] GOTO 0x0614
269: 0x0606 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0614
270: 0x060E [0x01] GOTO 0x00B7

SUBROUTINE_0614:
271: 0x0614 [0x01] GOTO 0x07CF
272: 0x0617 [0x02] IF !(Work_Zone[0] == 22*) GOTO 0x0658
273: 0x061F [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x062F
274: 0x0627 [0x03] Work_Zone[1] = 24*
275: 0x062C [0x01] GOTO 0x0655
276: 0x062F [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
277: 0x0636 [0x25] WAIT_DIALOG_SELECT()
278: 0x0637 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0647
279: 0x063F [0x03] Work_Zone[1] = 24*
280: 0x0644 [0x01] GOTO 0x0655
281: 0x0647 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0655
282: 0x064F [0x01] GOTO 0x00B7

SUBROUTINE_0655:
283: 0x0655 [0x01] GOTO 0x07CF
284: 0x0658 [0x02] IF !(Work_Zone[0] == 23*) GOTO 0x0699
285: 0x0660 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0670
286: 0x0668 [0x03] Work_Zone[1] = 25*
287: 0x066D [0x01] GOTO 0x0696
288: 0x0670 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
289: 0x0677 [0x25] WAIT_DIALOG_SELECT()
290: 0x0678 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0688
291: 0x0680 [0x03] Work_Zone[1] = 25*
292: 0x0685 [0x01] GOTO 0x0696
293: 0x0688 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0696
294: 0x0690 [0x01] GOTO 0x00B7

SUBROUTINE_0696:
295: 0x0696 [0x01] GOTO 0x07CF
296: 0x0699 [0x02] IF !(Work_Zone[0] == 24*) GOTO 0x06DA
297: 0x06A1 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x06B1
298: 0x06A9 [0x03] Work_Zone[1] = 26*
299: 0x06AE [0x01] GOTO 0x06D7
300: 0x06B1 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
301: 0x06B8 [0x25] WAIT_DIALOG_SELECT()
302: 0x06B9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x06C9
303: 0x06C1 [0x03] Work_Zone[1] = 26*
304: 0x06C6 [0x01] GOTO 0x06D7
305: 0x06C9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x06D7
306: 0x06D1 [0x01] GOTO 0x00B7

SUBROUTINE_06D7:
307: 0x06D7 [0x01] GOTO 0x07CF
308: 0x06DA [0x02] IF !(Work_Zone[0] == 25*) GOTO 0x071B
309: 0x06E2 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x06F2
310: 0x06EA [0x03] Work_Zone[1] = 27*
311: 0x06EF [0x01] GOTO 0x0718
312: 0x06F2 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
313: 0x06F9 [0x25] WAIT_DIALOG_SELECT()
314: 0x06FA [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x070A
315: 0x0702 [0x03] Work_Zone[1] = 27*
316: 0x0707 [0x01] GOTO 0x0718
317: 0x070A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0718
318: 0x0712 [0x01] GOTO 0x00B7

SUBROUTINE_0718:
319: 0x0718 [0x01] GOTO 0x07CF
320: 0x071B [0x02] IF !(Work_Zone[0] == 26*) GOTO 0x075C
321: 0x0723 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0733
322: 0x072B [0x03] Work_Zone[1] = 28*
323: 0x0730 [0x01] GOTO 0x0759
324: 0x0733 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
325: 0x073A [0x25] WAIT_DIALOG_SELECT()
326: 0x073B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x074B
327: 0x0743 [0x03] Work_Zone[1] = 28*
328: 0x0748 [0x01] GOTO 0x0759
329: 0x074B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0759
330: 0x0753 [0x01] GOTO 0x00B7

SUBROUTINE_0759:
331: 0x0759 [0x01] GOTO 0x07CF
332: 0x075C [0x02] IF !(Work_Zone[0] == 27*) GOTO 0x079D
333: 0x0764 [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0774
334: 0x076C [0x03] Work_Zone[1] = 29*
335: 0x0771 [0x01] GOTO 0x079A
336: 0x0774 [0x24] CREATE_DIALOG(message_id=11696*, default_option=1*, option_flags=0*)
    → "Warp to your destination? [Yes./No.]"
337: 0x077B [0x25] WAIT_DIALOG_SELECT()
338: 0x077C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x078C
339: 0x0784 [0x03] Work_Zone[1] = 29*
340: 0x0789 [0x01] GOTO 0x079A
341: 0x078C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x079A
342: 0x0794 [0x01] GOTO 0x00B7

SUBROUTINE_079A:
343: 0x079A [0x01] GOTO 0x07CF
344: 0x079D [0x02] IF !(Work_Zone[0] == 28*) GOTO 0x07B6
345: 0x07A5 [0x03] Work_Zone[1] = 2*
346: 0x07AA [0x48] [System] [11694*]:
    → "You will not be asked to confirm your choice of destination. Switching to simple teleporation mode."
347: 0x07AD [0x23] WAIT_FOR_DIALOG_INTERACTION
348: 0x07AE [0x1A] CALL_SUBROUTINE(address=0x080B)
349: 0x07B1 [0x21] END_EVENT
350: 0x07B2 [0x00] END_REQSTACK()

SUBROUTINE_07CF:
351: 0x07CF [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
352: 0x07D1 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
353: 0x07D3 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x07E6
354: 0x07DB [0x03] Work_Zone[1] = 99*
355: 0x07E0 [0x1A] CALL_SUBROUTINE(address=0x080B)
356: 0x07E3 [0x01] GOTO 0x0809
357: 0x07E6 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [EventEntity, LocalPlayer], work=[140*, 0*]
358: 0x07F7 [0x1C] WAIT(90* ticks)
359: 0x07FA [0x92] LocalPlayer->Render.Flags3 ^= 0x01
360: 0x0800 [0x1C] WAIT(30* ticks)
361: 0x0803 [0x1A] CALL_SUBROUTINE(address=0x08E3)
362: 0x0806 [0x1C] WAIT(30* ticks)

SUBROUTINE_0809:
363: 0x0809 [0x21] END_EVENT
364: 0x080A [0x00] END_REQSTACK()

SUBROUTINE_080B:
365: 0x080B [0x02] IF !(ExtData[1]->WorkLocal[3] == 30*) GOTO 0x0816
366: 0x0813 [0x01] GOTO 0x0836
367: 0x0816 [0xCE] WAIT_LOAD_SCHEDULER_ALT4: Wait for scheduler "s000" with entities [EventEntity, EventEntity], work=140*
368: 0x0825 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "stp0" with entities [EventEntity, EventEntity], work=[140*, 0*]

SUBROUTINE_0836:
369: 0x0836 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00EA [0x01] GOTO 0x07CF
     0x0100 [0x01] GOTO 0x07CF
     0x013E [0x01] GOTO 0x0141
# Dead code (unreachable instructions):
     0x017F [0x01] GOTO 0x0182
# Dead code (unreachable instructions):
     0x01C0 [0x01] GOTO 0x01C3
# Dead code (unreachable instructions):
     0x0201 [0x01] GOTO 0x0204
# Dead code (unreachable instructions):
     0x0242 [0x01] GOTO 0x0245
# Dead code (unreachable instructions):
     0x0283 [0x01] GOTO 0x0286
# Dead code (unreachable instructions):
     0x02C4 [0x01] GOTO 0x02C7
# Dead code (unreachable instructions):
     0x0305 [0x01] GOTO 0x0308
# Dead code (unreachable instructions):
     0x0346 [0x01] GOTO 0x0349
# Dead code (unreachable instructions):
     0x0387 [0x01] GOTO 0x038A
# Dead code (unreachable instructions):
     0x03C8 [0x01] GOTO 0x03CB
# Dead code (unreachable instructions):
     0x0409 [0x01] GOTO 0x040C
# Dead code (unreachable instructions):
     0x044A [0x01] GOTO 0x044D
# Dead code (unreachable instructions):
     0x048B [0x01] GOTO 0x048E
# Dead code (unreachable instructions):
     0x04CC [0x01] GOTO 0x04CF
# Dead code (unreachable instructions):
     0x050D [0x01] GOTO 0x0510
# Dead code (unreachable instructions):
     0x054E [0x01] GOTO 0x0551
# Dead code (unreachable instructions):
     0x058F [0x01] GOTO 0x0592
# Dead code (unreachable instructions):
     0x05D0 [0x01] GOTO 0x05D3
# Dead code (unreachable instructions):
     0x0611 [0x01] GOTO 0x0614
# Dead code (unreachable instructions):
     0x0652 [0x01] GOTO 0x0655
# Dead code (unreachable instructions):
     0x0693 [0x01] GOTO 0x0696
# Dead code (unreachable instructions):
     0x06D4 [0x01] GOTO 0x06D7
# Dead code (unreachable instructions):
     0x0715 [0x01] GOTO 0x0718
# Dead code (unreachable instructions):
     0x0756 [0x01] GOTO 0x0759
# Dead code (unreachable instructions):
     0x0797 [0x01] GOTO 0x079A
# Dead code (unreachable instructions):
     0x07B3 [0x01] GOTO 0x07CF
     0x07CC [0x01] GOTO 0x07CF
```

### Event 142

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0837   |
| Data Size    | 72 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0830:                      42  03 01 10 02 10 4A F0 FF         B.....J..
0840: FF 7F F8 FF FF 7F CD 02  80 F8 FF FF 7F F8 FF FF  ................
0850: 7F 73 30 30 30 00 80 1C  03 80 CD 02 80 F8 FF FF  .s000...........
0860: 7F F0 FF FF 7F 6D 61 69  6E 00 80 1C 32 80 92 01  .....main...2...
0870: F0 FF FF 7F 1C 01 80 1A  E3 08 1C 01 80 21 00     .............!. 
```

#### Opcodes

```
  0: 0x0837 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0838 [0x03] Work_Zone[1] = Work_Zone[2]
  2: 0x083D [0x4A] LocalPlayer looks at EventEntity
  3: 0x0846 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "s000" with entities [EventEntity, EventEntity], work=[140*, 0*]
  4: 0x0857 [0x1C] WAIT(110* ticks)
  5: 0x085A [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [EventEntity, LocalPlayer], work=[140*, 0*]
  6: 0x086B [0x1C] WAIT(90* ticks)
  7: 0x086E [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  8: 0x0874 [0x1C] WAIT(30* ticks)
  9: 0x0877 [0x1A] CALL_SUBROUTINE(address=0x08E3)
 10: 0x087A [0x1C] WAIT(30* ticks)
 11: 0x087D [0x21] END_EVENT
 12: 0x087E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x087F    |
| Data Size    | 658 bytes |
| Instructions | 1         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0870:                                               00                 .
0880: 45 33 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 30 00  E3.........fdi0.
0890: 80 55 33 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 30  .U3.........fdi0
08A0: 1B 45 33 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 30  .E3.........fdo0
08B0: 00 80 55 33 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U3.........fdo
08C0: 30 1B 45 33 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  0.E3.........fdi
08D0: 31 00 80 55 33 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U3.........fd
08E0: 69 31 1B 45 33 80 F0 FF  FF 7F F0 FF FF 7F 66 64  i1.E3.........fd
08F0: 6F 31 00 80 55 33 80 F0  FF FF 7F F0 FF FF 7F 66  o1..U3.........f
0900: 64 6F 31 1B 45 34 80 F0  FF FF 7F F0 FF FF 7F 77  do1.E4.........w
0910: 68 69 31 00 80 55 34 80  F0 FF FF 7F F0 FF FF 7F  hi1..U4.........
0920: 77 68 69 31 1B 45 34 80  F0 FF FF 7F F0 FF FF 7F  whi1.E4.........
0930: 77 68 6F 31 00 80 55 34  80 F0 FF FF 7F F0 FF FF  who1..U4........
0940: 7F 77 68 6F 31 1B 45 34  80 F0 FF FF 7F F0 FF FF  .who1.E4........
0950: 7F 77 68 6F 32 00 80 55  34 80 F0 FF FF 7F F0 FF  .who2..U4.......
0960: FF 7F 77 68 6F 32 1B 45  34 80 F0 FF FF 7F F0 FF  ..who2.E4.......
0970: FF 7F 77 68 6F 33 00 80  55 34 80 F0 FF FF 7F F0  ..who3..U4......
0980: FF FF 7F 77 68 6F 33 1B  62 08 80 F0 FF FF 7F F0  ...who3.b.......
0990: FF FF 7F 6D 61 69 6E 00  80 1C 35 80 45 33 80 F0  ...main...5.E3..
09A0: FF FF 7F F0 FF FF 7F 66  64 6F 31 00 80 55 33 80  .......fdo1..U3.
09B0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 1B 45 33 80  ........fdo1.E3.
09C0: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 00 80 62 04  ........fdi1..b.
09D0: 80 F0 FF FF 7F F0 FF FF  7F 6D 61 69 6E 00 80 1C  .........main...
09E0: 01 80 55 33 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..U3.........fdi
09F0: 31 1B 45 33 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  1.E3.........blo
0A00: 6E 00 80 45 34 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  n..E4.........bl
0A10: 6F 6E 00 80 1B 45 34 80  F0 FF FF 7F F0 FF FF 7F  on...E4.........
0A20: 77 68 69 30 00 80 55 34  80 F0 FF FF 7F F0 FF FF  whi0..U4........
0A30: 7F 77 68 69 30 1B 45 34  80 F0 FF FF 7F F0 FF FF  .whi0.E4........
0A40: 7F 77 68 6F 30 00 80 55  34 80 F0 FF FF 7F F0 FF  .who0..U4.......
0A50: FF 7F 77 68 6F 30 1B 45  36 80 F0 FF FF 7F F0 FF  ..who0.E6.......
0A60: FF 7F 65 66 6F 6E 00 80  55 36 80 F0 FF FF 7F F0  ..efon..U6......
0A70: FF FF 7F 65 66 6F 6E 1B  45 33 80 F0 FF FF 7F F0  ...efon.E3......
0A80: FF FF 7F 66 64 69 73 00  80 1B 45 33 80 F0 FF FF  ...fdis...E3....
0A90: 7F F0 FF FF 7F 66 64 6F  73 00 80 55 33 80 F0 FF  .....fdos..U3...
0AA0: FF 7F F0 FF FF 7F 66 64  6F 73 1B 45 33 80 F0 FF  ......fdos.E3...
0AB0: FF 7F F0 FF FF 7F 66 64  69 66 00 80 1B 45 33 80  ......fdif...E3.
0AC0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 66 00 80 55 33  ........fdof..U3
0AD0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 66 1B 45 33  .........fdof.E3
0AE0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 70 00 80 1B  .........fdip...
0AF0: 45 33 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 70 00  E3.........fdop.
0B00: 80 55 33 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 70  .U3.........fdop
0B10: 1B                                                .               
```

#### Opcodes

```
  0: 0x087F [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0880 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0891 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x08A0 [0x1B] RETURN
     0x08A1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x08B2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x08C1 [0x1B] RETURN
     0x08C2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x08D3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x08E2 [0x1B] RETURN
     0x08E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x08F4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0903 [0x1B] RETURN
     0x0904 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0915 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0924 [0x1B] RETURN
     0x0925 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0936 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0945 [0x1B] RETURN
     0x0946 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0957 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0966 [0x1B] RETURN
     0x0967 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0978 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0987 [0x1B] RETURN
     0x0988 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x0999 [0x1C] WAIT(45* ticks)
     0x099C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x09AD [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x09BC [0x1B] RETURN
     0x09BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x09CE [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x09DF [0x1C] WAIT(30* ticks)
     0x09E2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x09F1 [0x1B] RETURN
     0x09F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0A03 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0A14 [0x1B] RETURN
     0x0A15 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0A26 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0A35 [0x1B] RETURN
     0x0A36 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0A47 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0A56 [0x1B] RETURN
     0x0A57 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x0A68 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x0A77 [0x1B] RETURN
     0x0A78 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0A89 [0x1B] RETURN
     0x0A8A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0A9B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0AAA [0x1B] RETURN
     0x0AAB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0ABC [0x1B] RETURN
     0x0ABD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0ACE [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0ADD [0x1B] RETURN
     0x0ADE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0AEF [0x1B] RETURN
     0x0AF0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0B01 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0B10 [0x1B] RETURN
```

### Event 151

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0B11  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0B10:    00                                              .              
```

#### Opcodes

```
  0: 0x0B11 [0x00] END_REQSTACK()
```
