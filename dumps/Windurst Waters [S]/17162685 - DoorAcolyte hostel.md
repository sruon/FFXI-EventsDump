# 17162685 - DoorAcolyte hostel

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 2660 bytes                   |
| Total Events     | 2                            |
| References Count | 74                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [171](#event-171)     | 0x0001       |   2339 |            290 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DCD      |        7629 |
|       1 | 0x1DCE      |        7630 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0013      |          19 |
|       6 | 0x242FB     |      148219 |
|       7 | 0x3B4CE     |      242894 |
|       8 | 0xFFFFE13D  |  4294959421 |
|       9 | 0x07EC      |        2028 |
|      10 | 0x1DCF      |        7631 |
|      11 | 0x0078      |         120 |
|      12 | 0x00C9      |         201 |
|      13 | 0x0155      |         341 |
|      14 | 0x00A3      |         163 |
|      15 | 0x1DD0      |        7632 |
|      16 | 0x1DD1      |        7633 |
|      17 | 0x0001      |           1 |
|      18 | 0x1DD2      |        7634 |
|      19 | 0x1DD3      |        7635 |
|      20 | 0x1DD4      |        7636 |
|      21 | 0x24A38     |      150072 |
|      22 | 0x3C602     |      247298 |
|      23 | 0xFFFFE13E  |  4294959422 |
|      24 | 0x03AA      |         938 |
|      25 | 0x1DD5      |        7637 |
|      26 | 0x001E      |          30 |
|      27 | 0x0007      |           7 |
|      28 | 0x0028      |          40 |
|      29 | 0x1DD6      |        7638 |
|      30 | 0x1DD7      |        7639 |
|      31 | 0x1DD8      |        7640 |
|      32 | 0x241ED     |      147949 |
|      33 | 0x3B6F1     |      243441 |
|      34 | 0x0FED      |        4077 |
|      35 | 0x2424F     |      148047 |
|      36 | 0x3B315     |      242453 |
|      37 | 0x24651     |      149073 |
|      38 | 0x3B506     |      242950 |
|      39 | 0x084C      |        2124 |
|      40 | 0x247EC     |      149484 |
|      41 | 0x3AF79     |      241529 |
|      42 | 0x0B15      |        2837 |
|      43 | 0x002D      |          45 |
|      44 | 0x005A      |          90 |
|      45 | 0x09B5      |        2485 |
|      46 | 0x0055      |          85 |
|      47 | 0x1DD9      |        7641 |
|      48 | 0x0051      |          81 |
|      49 | 0x1DDA      |        7642 |
|      50 | 0x041C      |        1052 |
|      51 | 0x1DDB      |        7643 |
|      52 | 0x0096      |         150 |
|      53 | 0x0015      |          21 |
|      54 | 0x1DDC      |        7644 |
|      55 | 0x1DDD      |        7645 |
|      56 | 0x1DDE      |        7646 |
|      57 | 0x1DDF      |        7647 |
|      58 | 0x1DE0      |        7648 |
|      59 | 0x1DE1      |        7649 |
|      60 | 0x0006      |           6 |
|      61 | 0x1DE2      |        7650 |
|      62 | 0x1DE3      |        7651 |
|      63 | 0x1DE4      |        7652 |
|      64 | 0x1DE5      |        7653 |
|      65 | 0x1DE6      |        7654 |
|      66 | 0x1DE7      |        7655 |
|      67 | 0x084A      |        2122 |
|      68 | 0x0031      |          49 |
|      69 | 0x1DE8      |        7656 |
|      70 | 0x00F0      |         240 |
|      71 | 0x1DE9      |        7657 |
|      72 | 0x0C26      |        3110 |
|      73 | 0x00B6      |         182 |

## String References

- **7629**: You feel somebody's presence behind the door...
- **7630**: Knock on the door? [Yes./No.]
- **7631**: <Player> raps on the door.
- **7633**: Someone appears to be inside!
- **7643**: 5 are strewn all about the children's feet...
- **7656**: Hampu-Kampu picks up the $3 dejectedly.

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

### Event 171

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 2339 bytes |
| Instructions | 290        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 48 00 80 23  24 01 80 02 80 02 80 25    .BH..#$......%
0010: 02 00 10 02 80 00 FF 08  43 00 43 01 42 46 01 45  ........C.C.BF.E
0020: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 02 80  ..........fdo1..
0030: 1C 04 80 38 05 80 BA F0  FF FF 7F 06 80 07 80 08  ...8............
0040: 80 09 80 80 F0 FF FF 7F  48 0A 80 1C 0B 80 45 03  ........H.....E.
0050: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 02 80 45  .........blon..E
0060: 0C 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 02 80  ..........blon..
0070: 45 0D 80 F0 FF FF 7F F0  FF FF 7F 39 34 30 34 02  E..........9404.
0080: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
0090: 02 80 1C 04 80 5C 00 0E  80 5C 01 0E 80 9A 2B 01  .....\...\....+.
00A0: E2 05 01 0F 80 23 48 10  80 23 52 0D 80 F0 FF FF  .....#H..#R.....
00B0: 7F F0 FF FF 7F 39 34 30  34 45 03 80 F0 FF FF 7F  .....9404E......
00C0: F0 FF FF 7F 62 6C 6F 66  02 80 45 0D 80 F0 FF FF  ....blof..E.....
00D0: 7F F0 FF FF 7F 39 34 30  35 02 80 03 01 10 11 80  .....9405.......
00E0: 24 01 80 02 80 02 80 25  02 00 10 02 80 00 C5 08  $......%........
00F0: 48 0A 80 1C 0B 80 52 0D  80 F0 FF FF 7F F0 FF FF  H.....R.........
0100: 7F 39 34 30 35 45 03 80  F0 FF FF 7F F0 FF FF 7F  .9405E..........
0110: 62 6C 6F 6E 02 80 45 0C  80 F0 FF FF 7F F0 FF FF  blon..E.........
0120: 7F 62 6C 6F 6E 02 80 45  0D 80 F0 FF FF 7F F0 FF  .blon..E........
0130: FF 7F 39 34 30 34 02 80  2B 01 E2 05 01 12 80 23  ..9404..+......#
0140: 52 0D 80 F0 FF FF 7F F0  FF FF 7F 39 34 30 34 45  R..........9404E
0150: 03 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 66 02 80  ..........blof..
0160: 45 0D 80 F0 FF FF 7F F0  FF FF 7F 39 34 30 36 02  E..........9406.
0170: 80 2B 01 E2 05 01 13 80  23 2B BF E1 05 01 14 80  .+......#+......
0180: 23 4E 00 BC E1 05 01 BA  BC E1 05 01 15 80 16 80  #N..............
0190: 17 80 18 80 80 BC E1 05  01 92 01 BC E1 05 01 2B  ...............+
01A0: BC E1 05 01 19 80 23 52  0D 80 F0 FF FF 7F F0 FF  ......#R........
01B0: FF 7F 39 34 30 36 45 0D  80 F0 FF FF 7F F0 FF FF  ..9406E.........
01C0: 7F 39 34 30 35 02 80 4A  F0 FF FF 7F BC E1 05 01  .9405..J........
01D0: 29 0F BC E1 05 01 08 4A  BC E1 05 01 F0 FF FF 7F  )......J........
01E0: 6F 70 79 00 BC E1 05 01  F0 FF FF 7F 1C 1A 80 6E  opy............n
01F0: F0 FF FF 7F 1B 80 99 F0  FF FF 7F 99 F0 FF FF 7F  ................
0200: 1C 04 80 66 1C 80 BC E1  05 01 BC E1 05 01 74 6C  ...f..........tl
0210: 6B 30 2B BC E1 05 01 1D  80 23 66 1C 80 BC E1 05  k0+......#f.....
0220: 01 BC E1 05 01 74 6C 6B  31 52 0D 80 F0 FF FF 7F  .....tlk1R......
0230: F0 FF FF 7F 39 34 30 35  45 0D 80 F0 FF FF 7F F0  ....9405E.......
0240: FF FF 7F 39 34 30 37 02  80 4A F0 FF FF 7F BD E1  ...9407..J......
0250: 05 01 6F 70 29 0F BC E1  05 01 09 4A BC E1 05 01  ..op)......J....
0260: BD E1 05 01 6F 70 66 1C  80 BC E1 05 01 BC E1 05  ....opf.........
0270: 01 74 6C 6B 30 2B BC E1  05 01 1E 80 23 2B BC E1  .tlk0+......#+..
0280: 05 01 1F 80 23 66 1C 80  BC E1 05 01 BC E1 05 01  ....#f..........
0290: 74 6C 6B 31 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  tlk1E..........f
02A0: 64 6F 31 02 80 1C 04 80  45 0D 80 F0 FF FF 7F F0  do1.....E.......
02B0: FF FF 7F 64 6F 70 6E 02  80 52 0D 80 F0 FF FF 7F  ...dopn..R......
02C0: F0 FF FF 7F 39 34 30 37  2F 00 BE E1 05 01 4E 00  ....9407/.....N.
02D0: BE E1 05 01 BA BE E1 05  01 20 80 21 80 08 80 22  ......... .!..."
02E0: 80 80 BE E1 05 01 92 01  BE E1 05 01 2F 00 BF E1  ............/...
02F0: 05 01 4E 00 BF E1 05 01  BA BF E1 05 01 23 80 24  ..N..........#.$
0300: 80 08 80 22 80 80 BF E1  05 01 92 01 BF E1 05 01  ..."............
0310: BA BC E1 05 01 25 80 26  80 08 80 27 80 BA F0 FF  .....%.&...'....
0320: FF 7F 28 80 29 80 08 80  2A 80 1C 04 80 45 0D 80  ..(.)...*....E..
0330: F0 FF FF 7F F0 FF FF 7F  64 63 6C 73 02 80 1C 04  ........dcls....
0340: 80 5C 00 2B 80 5C 01 2B  80 9A 45 0D 80 F0 FF FF  .\.+.\.+..E.....
0350: 7F F0 FF FF 7F 39 34 30  38 02 80 45 03 80 F0 FF  .....9408..E....
0360: FF 7F F0 FF FF 7F 66 64  69 31 02 80 1C 04 80 1C  ......fdi1......
0370: 2C 80 52 0D 80 F0 FF FF  7F F0 FF FF 7F 39 34 30  ,.R..........940
0380: 38 45 03 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  8E..........ovl1
0390: 02 80 45 0D 80 F0 FF FF  7F F0 FF FF 7F 39 34 31  ..E..........941
03A0: 36 02 80 4B BE E1 05 01  2D 80 6F 70 79 00 BC E1  6..K....-.opy...
03B0: 05 01 BE E1 05 01 5B 2E  80 BE E1 05 01 BE E1 05  ......[.........
03C0: 01 74 6C 6B 30 2B BE E1  05 01 2F 80 23 5B 2E 80  .tlk0+..../.#[..
03D0: BE E1 05 01 BE E1 05 01  74 6C 6B 65 1C 1A 80 52  ........tlke...R
03E0: 0D 80 F0 FF FF 7F F0 FF  FF 7F 39 34 31 36 45 0D  ..........9416E.
03F0: 80 F0 FF FF 7F F0 FF FF  7F 39 34 31 37 02 80 1C  .........9417...
0400: 04 80 79 00 BC E1 05 01  BF E1 05 01 4A BF E1 05  ..y.........J...
0410: 01 BC E1 05 01 5B 30 80  BF E1 05 01 BF E1 05 01  .....[0.........
0420: 68 61 69 30 2B BF E1 05  01 31 80 23 53 BF E1 05  hai0+....1.#S...
0430: 01 BF E1 05 01 68 61 69  30 52 0D 80 F0 FF FF 7F  .....hai0R......
0440: F0 FF FF 7F 39 34 31 37  45 0D 80 F0 FF FF 7F F0  ....9417E.......
0450: FF FF 7F 39 34 30 34 02  80 7B BC E1 05 01 03 02  ...9404..{......
0460: 10 32 80 48 33 80 1C 34  80 27 0F C1 E1 05 01 02  .2.H3..4.'......
0470: 1C 04 80 6E BC E1 05 01  35 80 99 BC E1 05 01 2B  ...n....5......+
0480: BC E1 05 01 36 80 23 99  BC E1 05 01 1C 2C 80 52  ....6.#......,.R
0490: 0D 80 F0 FF FF 7F F0 FF  FF 7F 39 34 30 34 45 03  ..........9404E.
04A0: 80 F0 FF FF 7F F0 FF FF  7F 6F 76 6C 31 02 80 45  .........ovl1..E
04B0: 0D 80 F0 FF FF 7F F0 FF  FF 7F 39 34 30 39 02 80  ..........9409..
04C0: 4A BE E1 05 01 BC E1 05  01 79 00 BE E1 05 01 BC  J........y......
04D0: E1 05 01 79 00 BC E1 05  01 BE E1 05 01 5B 2E 80  ...y.........[..
04E0: BE E1 05 01 BE E1 05 01  74 6C 6B 30 2B BE E1 05  ........tlk0+...
04F0: 01 37 80 23 79 00 F0 FF  FF 7F BE E1 05 01 5B 2E  .7.#y.........[.
0500: 80 BE E1 05 01 BE E1 05  01 74 6C 6B 65 1C 1A 80  .........tlke...
0510: 66 1C 80 BC E1 05 01 BC  E1 05 01 74 6C 6B 30 2B  f..........tlk0+
0520: BC E1 05 01 38 80 23 66  1C 80 BC E1 05 01 BC E1  ....8.#f........
0530: 05 01 74 6C 6B 31 52 0D  80 F0 FF FF 7F F0 FF FF  ..tlk1R.........
0540: 7F 39 34 30 39 45 03 80  F0 FF FF 7F F0 FF FF 7F  .9409E..........
0550: 6F 76 6C 31 02 80 45 0D  80 F0 FF FF 7F F0 FF FF  ovl1..E.........
0560: 7F 39 34 31 30 02 80 5B  2E 80 BE E1 05 01 BE E1  .9410..[........
0570: 05 01 61 6E 67 30 2B BE  E1 05 01 39 80 23 52 0D  ..ang0+....9.#R.
0580: 80 F0 FF FF 7F F0 FF FF  7F 39 34 31 30 45 0D 80  .........9410E..
0590: F0 FF FF 7F F0 FF FF 7F  39 34 31 31 02 80 2B BE  ........9411..+.
05A0: E1 05 01 3A 80 23 52 0D  80 F0 FF FF 7F F0 FF FF  ...:.#R.........
05B0: 7F 39 34 31 31 45 0D 80  F0 FF FF 7F F0 FF FF 7F  .9411E..........
05C0: 39 34 31 32 02 80 2B BE  E1 05 01 3B 80 23 52 0D  9412..+....;.#R.
05D0: 80 F0 FF FF 7F F0 FF FF  7F 39 34 31 32 5B 2E 80  .........9412[..
05E0: BE E1 05 01 BE E1 05 01  74 6C 6B 65 45 0D 80 F0  ........tlkeE...
05F0: FF FF 7F F0 FF FF 7F 39  34 30 39 02 80 6E BC E1  .......9409..n..
0600: 05 01 3C 80 99 BC E1 05  01 2B BC E1 05 01 3D 80  ..<......+....=.
0610: 23 99 BC E1 05 01 52 0D  80 F0 FF FF 7F F0 FF FF  #.....R.........
0620: 7F 39 34 30 39 45 03 80  F0 FF FF 7F F0 FF FF 7F  .9409E..........
0630: 62 6C 6F 6E 02 80 45 0C  80 F0 FF FF 7F F0 FF FF  blon..E.........
0640: 7F 62 6C 6F 6E 02 80 45  0D 80 F0 FF FF 7F F0 FF  .blon..E........
0650: FF 7F 39 34 31 38 02 80  1C 1A 80 45 03 80 F0 FF  ..9418.....E....
0660: FF 7F F0 FF FF 7F 62 6C  6F 66 02 80 5B 2E 80 BE  ......blof..[...
0670: E1 05 01 BE E1 05 01 61  6E 67 30 4A BF E1 05 01  .......ang0J....
0680: BE E1 05 01 6F 70 2B BE  E1 05 01 3E 80 23 52 0D  ....op+....>.#R.
0690: 80 F0 FF FF 7F F0 FF FF  7F 39 34 31 38 45 0D 80  .........9418E..
06A0: F0 FF FF 7F F0 FF FF 7F  39 34 31 39 02 80 5B 30  ........9419..[0
06B0: 80 BF E1 05 01 BF E1 05  01 62 69 6B 30 2B BE E1  .........bik0+..
06C0: 05 01 3F 80 23 53 BF E1  05 01 BF E1 05 01 62 69  ..?.#S........bi
06D0: 6B 30 52 0D 80 F0 FF FF  7F F0 FF FF 7F 39 34 31  k0R..........941
06E0: 39 45 03 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  9E..........ovl1
06F0: 02 80 45 0D 80 F0 FF FF  7F F0 FF FF 7F 39 34 32  ..E..........942
0700: 35 02 80 27 0F BE E1 05  01 03 4A BC E1 05 01 BE  5..'......J.....
0710: E1 05 01 1C 2C 80 4A BF  E1 05 01 BC E1 05 01 6F  ....,.J........o
0720: 70 1C 1A 80 4A BF E1 05  01 BE E1 05 01 6F 70 4A  p...J........opJ
0730: BC E1 05 01 BE E1 05 01  29 0F BF E1 05 01 03 1C  ........).......
0740: 1A 80 52 0D 80 F0 FF FF  7F F0 FF FF 7F 39 34 32  ..R..........942
0750: 35 45 0D 80 F0 FF FF 7F  F0 FF FF 7F 39 34 31 33  5E..........9413
0760: 02 80 1C 1A 80 4A BE E1  05 01 BC E1 05 01 4A BF  .....J........J.
0770: E1 05 01 BC E1 05 01 6F  70 5B 2E 80 BE E1 05 01  .......op[......
0780: BE E1 05 01 61 6E 67 30  2B BE E1 05 01 40 80 23  ....ang0+....@.#
0790: 5B 30 80 BF E1 05 01 BF  E1 05 01 68 61 69 30 2B  [0.........hai0+
07A0: BF E1 05 01 41 80 23 53  BF E1 05 01 BF E1 05 01  ....A.#S........
07B0: 68 61 69 30 27 0F BE E1  05 01 04 1C 04 80 29 0F  hai0'.........).
07C0: BF E1 05 01 04 1C 1A 80  66 1C 80 BC E1 05 01 BC  ........f.......
07D0: E1 05 01 74 6C 6B 30 2B  BC E1 05 01 42 80 23 66  ...tlk0+....B.#f
07E0: 1C 80 BC E1 05 01 BC E1  05 01 74 6C 6B 31 1C 04  ..........tlk1..
07F0: 80 52 0D 80 F0 FF FF 7F  F0 FF FF 7F 39 34 31 33  .R..........9413
0800: 45 0D 80 F0 FF FF 7F F0  FF FF 7F 39 34 31 34 02  E..........9414.
0810: 80 1C 1A 80 4B BC E1 05  01 43 80 6F 70 66 44 80  ....K....C.opfD.
0820: BC E1 05 01 BC E1 05 01  73 68 61 30 03 02 10 32  ........sha0...2
0830: 80 48 45 80 1C 46 80 52  0D 80 F0 FF FF 7F F0 FF  .HE..F.R........
0840: FF 7F 39 34 31 34 45 0D  80 F0 FF FF 7F F0 FF FF  ..9414E.........
0850: 7F 39 34 31 35 02 80 2B  BC E1 05 01 47 80 66 44  .9415..+....G.fD
0860: 80 BC E1 05 01 BC E1 05  01 73 68 61 31 1C 04 80  .........sha1...
0870: 4B BC E1 05 01 48 80 6F  70 27 0F BC E1 05 01 0A  K....H.op'......
0880: 1C 46 80 45 03 80 F0 FF  FF 7F F0 FF FF 7F 66 64  .F.E..........fd
0890: 6F 31 02 80 1C 04 80 52  0D 80 F0 FF FF 7F F0 FF  o1.....R........
08A0: FF 7F 39 34 31 35 5C 00  49 80 5C 01 49 80 9A 46  ..9415\.I.\.I..F
08B0: 00 45 03 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
08C0: 02 80 01 FC 08 02 00 10  11 80 00 FC 08 45 03 80  .............E..
08D0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 02 80 1C 04  ........fdo1....
08E0: 80 03 01 10 02 80 46 00  45 03 80 F0 FF FF 7F F0  ......F.E.......
08F0: FF FF 7F 66 64 69 31 02  80 01 FC 08 01 20 09 02  ...fdi1...... ..
0900: 00 10 11 80 00 20 09 03  01 10 02 80 45 03 80 F0  ..... ......E...
0910: FF FF 7F F0 FF FF 7F 66  64 69 31 02 80 01 20 09  .......fdi1... .
0920: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x48] [System] [7629*]:
    → "You feel somebody's presence behind the door..."
  3: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0008 [0x24] CREATE_DIALOG(message_id=7630*, default_option=0*, option_flags=0*)
    → "Knock on the door? [Yes./No.]"
  5: 0x000F [0x25] WAIT_DIALOG_SELECT()
  6: 0x0010 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x08FF
  7: 0x0018 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x001C [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x001D [0x46] CAMERA_CONTROL: Disable user control
 11: 0x001F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x0030 [0x1C] WAIT(60* ticks)
 13: 0x0033 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 14: 0x0036 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=148.219*, pos_z=242.894*, pos_y=-7.875*, direction=178.2°*)
 15: 0x0043 [0x80] LOAD_WAIT(entity=LocalPlayer)
 16: 0x0048 [0x48] [System] [7631*]:
    → "<Player> raps on the door."
 17: 0x004B [0x1C] WAIT(120* ticks)
 18: 0x004E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x005F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 20: 0x0070 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9404" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 21: 0x0081 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0092 [0x1C] WAIT(60* ticks)
 23: 0x0095 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 163*
 24: 0x0099 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 163*
 25: 0x009D [0x9A] WAIT_MUSIC_SERVER()
 26: 0x009E [0x2B] ??? (ID: 17162753/0x0105E201) [7632*]:
    → "Go away!"
 27: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x00A6 [0x48] [System] [7633*]:
    → "Someone appears to be inside!"
 29: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x00AA [0x52] END_LOAD_SCHEDULER: End scheduler "9404" with entities [LocalPlayer, LocalPlayer], work=341*
 31: 0x00B9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x00CA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9405" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 33: 0x00DB [0x03] Work_Zone[1] = 1*
 34: 0x00E0 [0x24] CREATE_DIALOG(message_id=7630*, default_option=0*, option_flags=0*)
    → "Knock on the door? [Yes./No.]"
 35: 0x00E7 [0x25] WAIT_DIALOG_SELECT()
 36: 0x00E8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x08C5
 37: 0x00F0 [0x48] [System] [7631*]:
    → "<Player> raps on the door."
 38: 0x00F3 [0x1C] WAIT(120* ticks)
 39: 0x00F6 [0x52] END_LOAD_SCHEDULER: End scheduler "9405" with entities [LocalPlayer, LocalPlayer], work=341*
 40: 0x0105 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 41: 0x0116 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 42: 0x0127 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9404" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 43: 0x0138 [0x2B] ??? (ID: 17162753/0x0105E201) [7634*]:
    → "Ain't nobody herrre, so go away!"
 44: 0x013F [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x0140 [0x52] END_LOAD_SCHEDULER: End scheduler "9404" with entities [LocalPlayer, LocalPlayer], work=341*
 46: 0x014F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 47: 0x0160 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9406" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 48: 0x0171 [0x2B] ??? (ID: 17162753/0x0105E201) [7635*]:
    → "(Shhh! Keep it down, Tek!)"
 49: 0x0178 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x0179 [0x2B] Tek Lengyon (ID: 17162687/0x0105E1BF) [7636*]:
    → "Um, oops. Sorry, Kipopo..."
 51: 0x0180 [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x0181 [0x4E] SET_ENTITY_HIDE_FLAG: Show Hampu-Kampu (ID: 17162684/0x0105E1BC)
 53: 0x0187 [0xBA] SET_ENTITY_POSITION(entity_id=Hampu-Kampu (ID: 17162684/0x0105E1BC), pos_x=150.072*, pos_z=247.298*, pos_y=-7.874*, direction=82.4°*)
 54: 0x0194 [0x80] LOAD_WAIT(entity=Hampu-Kampu (ID: 17162684/0x0105E1BC))
 55: 0x0199 [0x92] Hampu-Kampu (ID: 17162684/0x0105E1BC)->Render.Flags3 ^= 0x01
 56: 0x019F [0x2B] Hampu-Kampu (ID: 17162684/0x0105E1BC) [7637*]:
    → "Oh, you are--!"
 57: 0x01A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x01A7 [0x52] END_LOAD_SCHEDULER: End scheduler "9406" with entities [LocalPlayer, LocalPlayer], work=341*
 59: 0x01B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9405" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 60: 0x01C7 [0x4A] LocalPlayer looks at Hampu-Kampu (ID: 17162684/0x0105E1BC)
 61: 0x01D0 [0x29] REQ_SET_WAIT(priority=0x0F, entity_id=Hampu-Kampu (ID: 17162684/0x0105E1BC), tag_num=0x08)
 62: 0x01D7 [0x4A] Hampu-Kampu (ID: 17162684/0x0105E1BC) looks at LocalPlayer
 63: 0x01E0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 64: 0x01E1 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 65: 0x01E2 [0x79] Hampu-Kampu (ID: 17162684/0x0105E1BC) looks at LocalPlayer (Basic look)
 66: 0x01EC [0x1C] WAIT(30* ticks)
 67: 0x01EF [0x6E] LocalPlayer uses emote 7*
 68: 0x01F6 [0x99] Wait for LocalPlayer animation to complete
 69: 0x01FB [0x99] Wait for LocalPlayer animation to complete
 70: 0x0200 [0x1C] WAIT(60* ticks)
 71: 0x0203 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=40*
 72: 0x0212 [0x2B] Hampu-Kampu (ID: 17162684/0x0105E1BC) [7638*]:
    → "...So this is where my daughtaru's been hiding."
 73: 0x0219 [0x23] WAIT_FOR_DIALOG_INTERACTION
 74: 0x021A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=40*
 75: 0x0229 [0x52] END_LOAD_SCHEDULER: End scheduler "9405" with entities [LocalPlayer, LocalPlayer], work=341*
 76: 0x0238 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9407" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 77: 0x0249 [0x4A] LocalPlayer looks at Door:Acolyte hostel (ID: 17162685/0x0105E1BD)
 78: 0x0252 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 79: 0x0253 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 80: 0x0254 [0x29] REQ_SET_WAIT(priority=0x0F, entity_id=Hampu-Kampu (ID: 17162684/0x0105E1BC), tag_num=0x09)
 81: 0x025B [0x4A] Hampu-Kampu (ID: 17162684/0x0105E1BC) looks at Door:Acolyte hostel (ID: 17162685/0x0105E1BD)
 82: 0x0264 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 83: 0x0265 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 84: 0x0266 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=40*
 85: 0x0275 [0x2B] Hampu-Kampu (ID: 17162684/0x0105E1BC) [7639*]:
    → "Kipopo, I know you have Daddy's bag."
 86: 0x027C [0x23] WAIT_FOR_DIALOG_INTERACTION
 87: 0x027D [0x2B] Hampu-Kampu (ID: 17162684/0x0105E1BC) [7640*]:
    → "Daddy spent a lot of time making it for an importantaru person, so please be a good girl and give it back."
 88: 0x0284 [0x23] WAIT_FOR_DIALOG_INTERACTION
 89: 0x0285 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=40*
 90: 0x0294 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 91: 0x02A5 [0x1C] WAIT(60* ticks)
 92: 0x02A8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dopn" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 93: 0x02B9 [0x52] END_LOAD_SCHEDULER: End scheduler "9407" with entities [LocalPlayer, LocalPlayer], work=341*
 94: 0x02C8 [0x2F] Kipopo (ID: 17162686/0x0105E1BE)->Render.Flags0 &= ~0x80000 // Bit 19
 95: 0x02CE [0x4E] SET_ENTITY_HIDE_FLAG: Show Kipopo (ID: 17162686/0x0105E1BE)
 96: 0x02D4 [0xBA] SET_ENTITY_POSITION(entity_id=Kipopo (ID: 17162686/0x0105E1BE), pos_x=147.949*, pos_z=243.441*, pos_y=-7.875*, direction=358.3°*)
 97: 0x02E1 [0x80] LOAD_WAIT(entity=Kipopo (ID: 17162686/0x0105E1BE))
 98: 0x02E6 [0x92] Kipopo (ID: 17162686/0x0105E1BE)->Render.Flags3 ^= 0x01
 99: 0x02EC [0x2F] Tek Lengyon (ID: 17162687/0x0105E1BF)->Render.Flags0 &= ~0x80000 // Bit 19
100: 0x02F2 [0x4E] SET_ENTITY_HIDE_FLAG: Show Tek Lengyon (ID: 17162687/0x0105E1BF)
101: 0x02F8 [0xBA] SET_ENTITY_POSITION(entity_id=Tek Lengyon (ID: 17162687/0x0105E1BF), pos_x=148.047*, pos_z=242.453*, pos_y=-7.875*, direction=358.3°*)
102: 0x0305 [0x80] LOAD_WAIT(entity=Tek Lengyon (ID: 17162687/0x0105E1BF))
103: 0x030A [0x92] Tek Lengyon (ID: 17162687/0x0105E1BF)->Render.Flags3 ^= 0x01
104: 0x0310 [0xBA] SET_ENTITY_POSITION(entity_id=Hampu-Kampu (ID: 17162684/0x0105E1BC), pos_x=149.073*, pos_z=242.950*, pos_y=-7.875*, direction=186.7°*)
105: 0x031D [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=149.484*, pos_z=241.529*, pos_y=-7.875*, direction=249.3°*)
106: 0x032A [0x1C] WAIT(60* ticks)
107: 0x032D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dcls" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
108: 0x033E [0x1C] WAIT(60* ticks)
109: 0x0341 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 45*
110: 0x0345 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 45*
111: 0x0349 [0x9A] WAIT_MUSIC_SERVER()
112: 0x034A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9408" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
113: 0x035B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
114: 0x036C [0x1C] WAIT(60* ticks)
115: 0x036F [0x1C] WAIT(90* ticks)
116: 0x0372 [0x52] END_LOAD_SCHEDULER: End scheduler "9408" with entities [LocalPlayer, LocalPlayer], work=341*
117: 0x0381 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
118: 0x0392 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9416" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
119: 0x03A3 [0x4B] UPDATE_ENTITY_YAW(entity=Kipopo (ID: 17162686/0x0105E1BE), yaw=13.7°*)
120: 0x03AA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
121: 0x03AB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
122: 0x03AC [0x79] Hampu-Kampu (ID: 17162684/0x0105E1BC) looks at Kipopo (ID: 17162686/0x0105E1BE) (Basic look)
123: 0x03B6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Kipopo (ID: 17162686/0x0105E1BE), Kipopo (ID: 17162686/0x0105E1BE)], work=85*
124: 0x03C5 [0x2B] Kipopo (ID: 17162686/0x0105E1BE) [7641*]:
    → "There's nothing to give back. Tek's ripped it to shreds."
125: 0x03CC [0x23] WAIT_FOR_DIALOG_INTERACTION
126: 0x03CD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [Kipopo (ID: 17162686/0x0105E1BE), Kipopo (ID: 17162686/0x0105E1BE)], work=85*
127: 0x03DC [0x1C] WAIT(30* ticks)
128: 0x03DF [0x52] END_LOAD_SCHEDULER: End scheduler "9416" with entities [LocalPlayer, LocalPlayer], work=341*
129: 0x03EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9417" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
130: 0x03FF [0x1C] WAIT(60* ticks)
131: 0x0402 [0x79] Hampu-Kampu (ID: 17162684/0x0105E1BC) looks at Tek Lengyon (ID: 17162687/0x0105E1BF) (Basic look)
132: 0x040C [0x4A] Tek Lengyon (ID: 17162687/0x0105E1BF) looks at Hampu-Kampu (ID: 17162684/0x0105E1BC)
133: 0x0415 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hai0" with entities [Tek Lengyon (ID: 17162687/0x0105E1BF), Tek Lengyon (ID: 17162687/0x0105E1BF)], work=81*
134: 0x0424 [0x2B] Tek Lengyon (ID: 17162687/0x0105E1BF) [7642*]:
    → "Ding-dong! The bag is dead!t Which old bag? The new handbag!t"
135: 0x042B [0x23] WAIT_FOR_DIALOG_INTERACTION
136: 0x042C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hai0" with entities [Tek Lengyon (ID: 17162687/0x0105E1BF), Tek Lengyon (ID: 17162687/0x0105E1BF)]
137: 0x0439 [0x52] END_LOAD_SCHEDULER: End scheduler "9417" with entities [LocalPlayer, LocalPlayer], work=341*
138: 0x0448 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9404" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
139: 0x0459 [0x7B] Hampu-Kampu (ID: 17162684/0x0105E1BC) stops talking
140: 0x045E [0x03] Work_Zone[2] = 1052*
141: 0x0463 [0x48] [System] [7643*]:
    → "5 are strewn all about the children's feet..."
142: 0x0466 [0x1C] WAIT(150* ticks)
143: 0x0469 [0x27] REQ_SET(priority=0x0F, entity_id=??? (ID: 17162689/0x0105E1C1), tag_num=0x02)
144: 0x0470 [0x1C] WAIT(60* ticks)
145: 0x0473 [0x6E] Hampu-Kampu (ID: 17162684/0x0105E1BC) uses emote 21*
146: 0x047A [0x99] Wait for Hampu-Kampu (ID: 17162684/0x0105E1BC) animation to complete
147: 0x047F [0x2B] Hampu-Kampu (ID: 17162684/0x0105E1BC) [7644*]:
    → "Wh-wh-what!?"
148: 0x0486 [0x23] WAIT_FOR_DIALOG_INTERACTION
149: 0x0487 [0x99] Wait for Hampu-Kampu (ID: 17162684/0x0105E1BC) animation to complete
150: 0x048C [0x1C] WAIT(90* ticks)
151: 0x048F [0x52] END_LOAD_SCHEDULER: End scheduler "9404" with entities [LocalPlayer, LocalPlayer], work=341*
152: 0x049E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
153: 0x04AF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9409" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
154: 0x04C0 [0x4A] Kipopo (ID: 17162686/0x0105E1BE) looks at Hampu-Kampu (ID: 17162684/0x0105E1BC)
155: 0x04C9 [0x79] Kipopo (ID: 17162686/0x0105E1BE) looks at Hampu-Kampu (ID: 17162684/0x0105E1BC) (Basic look)
156: 0x04D3 [0x79] Hampu-Kampu (ID: 17162684/0x0105E1BC) looks at Kipopo (ID: 17162686/0x0105E1BE) (Basic look)
157: 0x04DD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Kipopo (ID: 17162686/0x0105E1BE), Kipopo (ID: 17162686/0x0105E1BE)], work=85*
158: 0x04EC [0x2B] Kipopo (ID: 17162686/0x0105E1BE) [7645*]:
    → "I thoughtaru you were making the bag for Kipopo!"
159: 0x04F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
160: 0x04F4 [0x79] LocalPlayer looks at Kipopo (ID: 17162686/0x0105E1BE) (Basic look)
161: 0x04FE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [Kipopo (ID: 17162686/0x0105E1BE), Kipopo (ID: 17162686/0x0105E1BE)], work=85*
162: 0x050D [0x1C] WAIT(30* ticks)
163: 0x0510 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=40*
164: 0x051F [0x2B] Hampu-Kampu (ID: 17162684/0x0105E1BC) [7646*]:
    → "I...I'm sorry..."
165: 0x0526 [0x23] WAIT_FOR_DIALOG_INTERACTION
166: 0x0527 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=40*
167: 0x0536 [0x52] END_LOAD_SCHEDULER: End scheduler "9409" with entities [LocalPlayer, LocalPlayer], work=341*
168: 0x0545 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
169: 0x0556 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9410" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
170: 0x0567 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [Kipopo (ID: 17162686/0x0105E1BE), Kipopo (ID: 17162686/0x0105E1BE)], work=85*
171: 0x0576 [0x2B] Kipopo (ID: 17162686/0x0105E1BE) [7647*]:
    → "Who's this importantaru person anyway?"
172: 0x057D [0x23] WAIT_FOR_DIALOG_INTERACTION
173: 0x057E [0x52] END_LOAD_SCHEDULER: End scheduler "9410" with entities [LocalPlayer, LocalPlayer], work=341*
174: 0x058D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9411" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
175: 0x059E [0x2B] Kipopo (ID: 17162686/0x0105E1BE) [7648*]:
    → "Isn't Kipopo your importantaru person?"
176: 0x05A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
177: 0x05A6 [0x52] END_LOAD_SCHEDULER: End scheduler "9411" with entities [LocalPlayer, LocalPlayer], work=341*
178: 0x05B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9412" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
179: 0x05C6 [0x2B] Kipopo (ID: 17162686/0x0105E1BE) [7649*]:
    → "Have you already forgotten about Mommy?"
180: 0x05CD [0x23] WAIT_FOR_DIALOG_INTERACTION
181: 0x05CE [0x52] END_LOAD_SCHEDULER: End scheduler "9412" with entities [LocalPlayer, LocalPlayer], work=341*
182: 0x05DD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [Kipopo (ID: 17162686/0x0105E1BE), Kipopo (ID: 17162686/0x0105E1BE)], work=85*
183: 0x05EC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9409" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
184: 0x05FD [0x6E] Hampu-Kampu (ID: 17162684/0x0105E1BC) uses emote 6*
185: 0x0604 [0x99] Wait for Hampu-Kampu (ID: 17162684/0x0105E1BC) animation to complete
186: 0x0609 [0x2B] Hampu-Kampu (ID: 17162684/0x0105E1BC) [7650*]:
    → "N-no, of course not... It's just that I thought it was high timey-wime you had a new--"
187: 0x0610 [0x23] WAIT_FOR_DIALOG_INTERACTION
188: 0x0611 [0x99] Wait for Hampu-Kampu (ID: 17162684/0x0105E1BC) animation to complete
189: 0x0616 [0x52] END_LOAD_SCHEDULER: End scheduler "9409" with entities [LocalPlayer, LocalPlayer], work=341*
190: 0x0625 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
191: 0x0636 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
192: 0x0647 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9418" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
193: 0x0658 [0x1C] WAIT(30* ticks)
194: 0x065B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
195: 0x066C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [Kipopo (ID: 17162686/0x0105E1BE), Kipopo (ID: 17162686/0x0105E1BE)], work=85*
196: 0x067B [0x4A] Tek Lengyon (ID: 17162687/0x0105E1BF) looks at Kipopo (ID: 17162686/0x0105E1BE)
197: 0x0684 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
198: 0x0685 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
199: 0x0686 [0x2B] Kipopo (ID: 17162686/0x0105E1BE) [7651*]:
    → "I won't forgive you if you betray Mommy!"
200: 0x068D [0x23] WAIT_FOR_DIALOG_INTERACTION
201: 0x068E [0x52] END_LOAD_SCHEDULER: End scheduler "9418" with entities [LocalPlayer, LocalPlayer], work=341*
202: 0x069D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9419" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
203: 0x06AE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [Tek Lengyon (ID: 17162687/0x0105E1BF), Tek Lengyon (ID: 17162687/0x0105E1BF)], work=81*
204: 0x06BD [0x2B] Kipopo (ID: 17162686/0x0105E1BE) [7652*]:
    → "Only Kipopo can be your importantaru person!"
205: 0x06C4 [0x23] WAIT_FOR_DIALOG_INTERACTION
206: 0x06C5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [Tek Lengyon (ID: 17162687/0x0105E1BF), Tek Lengyon (ID: 17162687/0x0105E1BF)]
207: 0x06D2 [0x52] END_LOAD_SCHEDULER: End scheduler "9419" with entities [LocalPlayer, LocalPlayer], work=341*
208: 0x06E1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
209: 0x06F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9425" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
210: 0x0703 [0x27] REQ_SET(priority=0x0F, entity_id=Kipopo (ID: 17162686/0x0105E1BE), tag_num=0x03)
211: 0x070A [0x4A] Hampu-Kampu (ID: 17162684/0x0105E1BC) looks at Kipopo (ID: 17162686/0x0105E1BE)
212: 0x0713 [0x1C] WAIT(90* ticks)
213: 0x0716 [0x4A] Tek Lengyon (ID: 17162687/0x0105E1BF) looks at Hampu-Kampu (ID: 17162684/0x0105E1BC)
214: 0x071F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
215: 0x0720 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
216: 0x0721 [0x1C] WAIT(30* ticks)
217: 0x0724 [0x4A] Tek Lengyon (ID: 17162687/0x0105E1BF) looks at Kipopo (ID: 17162686/0x0105E1BE)
218: 0x072D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
219: 0x072E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
220: 0x072F [0x4A] Hampu-Kampu (ID: 17162684/0x0105E1BC) looks at Kipopo (ID: 17162686/0x0105E1BE)
221: 0x0738 [0x29] REQ_SET_WAIT(priority=0x0F, entity_id=Tek Lengyon (ID: 17162687/0x0105E1BF), tag_num=0x03)
222: 0x073F [0x1C] WAIT(30* ticks)
223: 0x0742 [0x52] END_LOAD_SCHEDULER: End scheduler "9425" with entities [LocalPlayer, LocalPlayer], work=341*
224: 0x0751 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9413" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
225: 0x0762 [0x1C] WAIT(30* ticks)
226: 0x0765 [0x4A] Kipopo (ID: 17162686/0x0105E1BE) looks at Hampu-Kampu (ID: 17162684/0x0105E1BC)
227: 0x076E [0x4A] Tek Lengyon (ID: 17162687/0x0105E1BF) looks at Hampu-Kampu (ID: 17162684/0x0105E1BC)
228: 0x0777 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
229: 0x0778 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
230: 0x0779 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [Kipopo (ID: 17162686/0x0105E1BE), Kipopo (ID: 17162686/0x0105E1BE)], work=85*
231: 0x0788 [0x2B] Kipopo (ID: 17162686/0x0105E1BE) [7653*]:
    → "I hate you, I hate you! Daddy can go and chokey-woke on a rabbit mantle!"
232: 0x078F [0x23] WAIT_FOR_DIALOG_INTERACTION
233: 0x0790 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hai0" with entities [Tek Lengyon (ID: 17162687/0x0105E1BF), Tek Lengyon (ID: 17162687/0x0105E1BF)], work=81*
234: 0x079F [0x2B] Tek Lengyon (ID: 17162687/0x0105E1BF) [7654*]:
    → "Nyahaha.t And that's all for today's episode of "Tek the Tannerrr"! Till next time, folks!"
235: 0x07A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
236: 0x07A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hai0" with entities [Tek Lengyon (ID: 17162687/0x0105E1BF), Tek Lengyon (ID: 17162687/0x0105E1BF)]
237: 0x07B4 [0x27] REQ_SET(priority=0x0F, entity_id=Kipopo (ID: 17162686/0x0105E1BE), tag_num=0x04)
238: 0x07BB [0x1C] WAIT(60* ticks)
239: 0x07BE [0x29] REQ_SET_WAIT(priority=0x0F, entity_id=Tek Lengyon (ID: 17162687/0x0105E1BF), tag_num=0x04)
240: 0x07C5 [0x1C] WAIT(30* ticks)
241: 0x07C8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=40*
242: 0x07D7 [0x2B] Hampu-Kampu (ID: 17162684/0x0105E1BC) [7655*]:
    → "K-Kipopo..."
243: 0x07DE [0x23] WAIT_FOR_DIALOG_INTERACTION
244: 0x07DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=40*
245: 0x07EE [0x1C] WAIT(60* ticks)
246: 0x07F1 [0x52] END_LOAD_SCHEDULER: End scheduler "9413" with entities [LocalPlayer, LocalPlayer], work=341*
247: 0x0800 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9414" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
248: 0x0811 [0x1C] WAIT(30* ticks)
249: 0x0814 [0x4B] UPDATE_ENTITY_YAW(entity=Hampu-Kampu (ID: 17162684/0x0105E1BC), yaw=11.7°*)
250: 0x081B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
251: 0x081C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
252: 0x081D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=49*
253: 0x082C [0x03] Work_Zone[2] = 1052*
254: 0x0831 [0x48] [System] [7656*]:
    → "Hampu-Kampu picks up the $3 dejectedly."
255: 0x0834 [0x1C] WAIT(240* ticks)
256: 0x0837 [0x52] END_LOAD_SCHEDULER: End scheduler "9414" with entities [LocalPlayer, LocalPlayer], work=341*
257: 0x0846 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9415" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
258: 0x0857 [0x2B] Hampu-Kampu (ID: 17162684/0x0105E1BC) [7657*]:
    → "The...the handbag that I so poured my heartaru into... There's nothing left of it but scraps..."
259: 0x085E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [Hampu-Kampu (ID: 17162684/0x0105E1BC), Hampu-Kampu (ID: 17162684/0x0105E1BC)], work=49*
260: 0x086D [0x1C] WAIT(60* ticks)
261: 0x0870 [0x4B] UPDATE_ENTITY_YAW(entity=Hampu-Kampu (ID: 17162684/0x0105E1BC), yaw=17.1°*)
262: 0x0877 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
263: 0x0878 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
264: 0x0879 [0x27] REQ_SET(priority=0x0F, entity_id=Hampu-Kampu (ID: 17162684/0x0105E1BC), tag_num=0x0A)
265: 0x0880 [0x1C] WAIT(240* ticks)
266: 0x0883 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
267: 0x0894 [0x1C] WAIT(60* ticks)
268: 0x0897 [0x52] END_LOAD_SCHEDULER: End scheduler "9415" with entities [LocalPlayer, LocalPlayer], work=341*
269: 0x08A6 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 182*
270: 0x08AA [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 182*
271: 0x08AE [0x9A] WAIT_MUSIC_SERVER()
272: 0x08AF [0x46] CAMERA_CONTROL: Restore default settings
273: 0x08B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
274: 0x08C2 [0x01] GOTO 0x08FC
275: 0x08C5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x08FC
276: 0x08CD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
277: 0x08DE [0x1C] WAIT(60* ticks)
278: 0x08E1 [0x03] Work_Zone[1] = 0*
279: 0x08E6 [0x46] CAMERA_CONTROL: Restore default settings
280: 0x08E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
281: 0x08F9 [0x01] GOTO 0x08FC

SUBROUTINE_08FC:
282: 0x08FC [0x01] GOTO 0x0920
283: 0x08FF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0920
284: 0x0907 [0x03] Work_Zone[1] = 0*
285: 0x090C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
286: 0x091D [0x01] GOTO 0x0920

SUBROUTINE_0920:
287: 0x0920 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
288: 0x0922 [0x21] END_EVENT
289: 0x0923 [0x00] END_REQSTACK()
```
