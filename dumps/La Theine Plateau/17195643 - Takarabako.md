# 17195643 - Takarabako

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 2600 bytes                  |
| Total Events     | 2                           |
| References Count | 32                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [119](#event-119)     | 0x0001       |   2446 |            303 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0064      |         100 |
|       3 | 0x0013      |          19 |
|       4 | 0x003C      |          60 |
|       5 | 0x1D53      |        7507 |
|       6 | 0x1D54      |        7508 |
|       7 | 0x0078      |         120 |
|       8 | 0x007F      |         127 |
|       9 | 0x0001      |           1 |
|      10 | 0x1D55      |        7509 |
|      11 | 0x000F      |          15 |
|      12 | 0x1D56      |        7510 |
|      13 | 0x1D57      |        7511 |
|      14 | 0x001E      |          30 |
|      15 | 0x1D58      |        7512 |
|      16 | 0x00AA      |         170 |
|      17 | 0x1D5C      |        7516 |
|      18 | 0x005C      |          92 |
|      19 | 0x1D69      |        7529 |
|      20 | 0x0014      |          20 |
|      21 | 0x000A      |          10 |
|      22 | 0x006E      |         110 |
|      23 | 0x00C9      |         201 |
|      24 | 0x012C      |         300 |
|      25 | 0x0008      |           8 |
|      26 | 0x1D72      |        7538 |
|      27 | 0x1D74      |        7540 |
|      28 | 0x1D79      |        7545 |
|      29 | 0x0190      |         400 |
|      30 | 0x1D80      |        7552 |
|      31 | 0x1D81      |        7553 |

## String References

- **7507**: You find an old chest!
- **7508**: However, your $3 breaks.

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

### Event 119

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 2446 bytes |
| Instructions | 303        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 46 01 5D 00  80 01 80 45 01 80 F8 FF    .BF.]....E....
0010: FF 7F F8 FF FF 7F 66 64  6F 31 00 80 1C 02 80 38  ......fdo1.....8
0020: 03 80 29 0B F0 FF FF 7F  0C 29 0B F0 FF FF 7F 0E  ..)......)......
0030: 22 00 4E 00 7A 62 06 01  80 7A 62 06 01 29 0B F0  ".N.zb...zb..)..
0040: FF FF 7F 14 1C 04 80 48  05 80 23 48 06 80 23 5C  .......H..#H..#\
0050: 00 07 80 5C 01 07 80 5D  08 80 09 80 29 0B F0 FF  ...\...]....)...
0060: FF 7F 10 27 0B 71 62 06  01 18 45 01 80 F8 FF FF  ...'.qb...E.....
0070: 7F F8 FF FF 7F 66 64 69  31 00 80 27 0B 7A 62 06  .....fdi1..'.zb.
0080: 01 23 2B 7A 62 06 01 0A  80 23 2A 0B 7A 62 06 01  .#+zb....#*.zb..
0090: 2A 0B 71 62 06 01 52 0B  80 F0 FF FF 7F F0 FF FF  *.qb..R.........
00A0: 7F 73 30 37 37 4A F0 FF  FF 7F 7A 62 06 01 45 0B  .s077J....zb..E.
00B0: 80 F0 FF FF 7F F0 FF FF  7F 73 30 37 36 00 80 27  .........s076..'
00C0: 0B 7A 62 06 01 24 2B 7A  62 06 01 0C 80 23 2B 7A  .zb..$+zb....#+z
00D0: 62 06 01 0D 80 23 2A 0B  7A 62 06 01 27 0B 7A 62  b....#*.zb..'.zb
00E0: 06 01 20 1C 0E 80 52 0B  80 F0 FF FF 7F F0 FF FF  .. ...R.........
00F0: 7F 73 30 37 36 45 01 80  F8 FF FF 7F F8 FF FF 7F  .s076E..........
0100: 66 64 6F 31 00 80 1C 04  80 2A 0B 7A 62 06 01 4A  fdo1.....*.zb..J
0110: F0 FF FF 7F 7B 62 06 01  6F 76 F0 FF FF 7F 27 0B  ....{b..ov....'.
0120: 7A 62 06 01 1F 45 0B 80  F0 FF FF 7F F0 FF FF 7F  zb...E..........
0130: 73 30 37 38 00 80 2C F8  FF FF 7F F8 FF FF 7F 6F  s078..,........o
0140: 70 65 6E 45 01 80 F8 FF  FF 7F F8 FF FF 7F 66 64  penE..........fd
0150: 69 31 00 80 2B 7A 62 06  01 0F 80 23 2A 0B 7A 62  i1..+zb....#*.zb
0160: 06 01 29 0B 7A 62 06 01  2A 52 0B 80 F0 FF FF 7F  ..).zb..*R......
0170: F0 FF FF 7F 73 30 37 38  45 0B 80 F0 FF FF 7F F0  ....s078E.......
0180: FF FF 7F 73 30 37 39 00  80 5D 00 80 01 80 29 0B  ...s079..]....).
0190: 7A 62 06 01 2B 1C 04 80  29 0B 71 62 06 01 19 4A  zb..+...).qb...J
01A0: 7A 62 06 01 71 62 06 01  4A F0 FF FF 7F 71 62 06  zb..qb..J....qb.
01B0: 01 4E 00 77 62 06 01 52  0B 80 F0 FF FF 7F F0 FF  .N.wb..R........
01C0: FF 7F 73 30 37 39 5C 00  10 80 5C 01 10 80 5D 08  ..s079\...\...].
01D0: 80 09 80 27 0B 77 62 06  01 10 1C 0E 80 45 0B 80  ...'.wb......E..
01E0: F0 FF FF 7F F0 FF FF 7F  73 30 37 32 00 80 2B 77  ........s072..+w
01F0: 62 06 01 11 80 23 4E 00  71 62 06 01 4E 00 75 62  b....#N.qb..N.ub
0200: 06 01 4E 00 72 62 06 01  4E 00 76 62 06 01 4E 00  ..N.rb..N.vb..N.
0210: 74 62 06 01 4E 00 73 62  06 01 4E 00 78 62 06 01  tb..N.sb..N.xb..
0220: 1C 02 80 52 0B 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...R..........s0
0230: 37 32 45 01 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  72E..........ovl
0240: 31 00 80 45 0B 80 F0 FF  FF 7F F0 FF FF 7F 73 30  1..E..........s0
0250: 37 33 00 80 27 0B 73 62  06 01 19 27 0B 74 62 06  73..'.sb...'.tb.
0260: 01 0F 27 0B 75 62 06 01  15 27 0B 71 62 06 01 15  ..'.ub...'.qb...
0270: 27 0B 72 62 06 01 11 27  0B 76 62 06 01 0A 55 0B  '.rb...'.vb...U.
0280: 80 F0 FF FF 7F F0 FF FF  7F 73 30 37 33 45 01 80  .........s073E..
0290: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 00 80 45 0B  ........ovl1..E.
02A0: 80 F0 FF FF 7F F0 FF FF  7F 73 30 37 34 00 80 1C  .........s074...
02B0: 01 80 52 0B 80 F0 FF FF  7F F0 FF FF 7F 73 30 37  ..R..........s07
02C0: 34 45 01 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  4E..........ovl1
02D0: 00 80 45 12 80 F0 FF FF  7F F0 FF FF 7F 73 30 37  ..E..........s07
02E0: 34 00 80 2A 0B 77 62 06  01 2A 0B 73 62 06 01 2A  4..*.wb..*.sb..*
02F0: 0B 74 62 06 01 2A 0B 75  62 06 01 2A 0B 71 62 06  .tb..*.ub..*.qb.
0300: 01 2A 0B 72 62 06 01 2A  0B 76 62 06 01 29 0B 7A  .*.rb..*.vb..).z
0310: 62 06 01 22 29 08 7A 62  06 01 05 29 08 7A 62 06  b..").zb...).zb.
0320: 01 06 52 12 80 F0 FF FF  7F F0 FF FF 7F 73 30 37  ..R..........s07
0330: 34 45 12 80 F0 FF FF 7F  F0 FF FF 7F 73 30 37 32  4E..........s072
0340: 00 80 29 0B 74 62 06 01  10 29 0B 73 62 06 01 1A  ..).tb...).sb...
0350: 52 0B 80 F0 FF FF 7F F0  FF FF 7F 73 30 37 32 45  R..........s072E
0360: 0B 80 F0 FF FF 7F F0 FF  FF 7F 73 30 38 30 00 80  ..........s080..
0370: 4A 76 62 06 01 71 62 06  01 6F 76 76 62 06 01 29  Jvb..qb..ovvb..)
0380: 0B 76 62 06 01 0B 79 00  71 62 06 01 76 62 06 01  .vb...y.qb..vb..
0390: 29 0B 71 62 06 01 1A 52  0B 80 F0 FF FF 7F F0 FF  ).qb...R........
03A0: FF 7F 73 30 38 30 45 0B  80 F0 FF FF 7F F0 FF FF  ..s080E.........
03B0: 7F 73 30 38 31 00 80 4A  76 62 06 01 7A 62 06 01  .s081..Jvb..zb..
03C0: 7B 71 62 06 01 29 0B 71  62 06 01 1B 79 00 72 62  {qb..).qb...y.rb
03D0: 06 01 71 62 06 01 29 0B  72 62 06 01 13 52 0B 80  ..qb..).rb...R..
03E0: F0 FF FF 7F F0 FF FF 7F  73 30 38 31 45 01 80 F0  ........s081E...
03F0: FF FF 7F F0 FF FF 7F 6F  76 6C 31 00 80 45 0B 80  .......ovl1..E..
0400: F0 FF FF 7F F0 FF FF 7F  73 30 38 32 00 80 29 0B  ........s082..).
0410: 71 62 06 01 1C 52 0B 80  F0 FF FF 7F F0 FF FF 7F  qb...R..........
0420: 73 30 38 32 45 0B 80 F0  FF FF 7F F0 FF FF 7F 73  s082E..........s
0430: 30 38 33 00 80 7B 72 62  06 01 79 00 71 62 06 01  083..{rb..y.qb..
0440: 73 62 06 01 29 0B 71 62  06 01 1D 29 0B 73 62 06  sb..).qb...).sb.
0450: 01 1B 52 0B 80 F0 FF FF  7F F0 FF FF 7F 73 30 38  ..R..........s08
0460: 33 45 0B 80 F0 FF FF 7F  F0 FF FF 7F 73 30 38 34  3E..........s084
0470: 00 80 7B 71 62 06 01 79  00 76 62 06 01 75 62 06  ..{qb..y.vb..ub.
0480: 01 29 0B 75 62 06 01 16  52 0B 80 F0 FF FF 7F F0  .).ub...R.......
0490: FF FF 7F 73 30 38 34 45  0B 80 F0 FF FF 7F F0 FF  ...s084E........
04A0: FF 7F 73 30 38 35 00 80  7B 76 62 06 01 4A 76 62  ..s085..{vb..Jvb
04B0: 06 01 77 62 06 01 29 0B  77 62 06 01 11 6F 76 76  ..wb..).wb...ovv
04C0: 62 06 01 29 08 76 62 06  01 03 29 08 76 62 06 01  b..).vb...).vb..
04D0: 04 52 0B 80 F0 FF FF 7F  F0 FF FF 7F 73 30 38 35  .R..........s085
04E0: 45 0B 80 F0 FF FF 7F F0  FF FF 7F 73 30 38 36 00  E..........s086.
04F0: 80 79 00 71 62 06 01 76  62 06 01 4A 76 62 06 01  .y.qb..vb..Jvb..
0500: 71 62 06 01 29 08 76 62  06 01 01 29 0B 76 62 06  qb..).vb...).vb.
0510: 01 0C 52 0B 80 F0 FF FF  7F F0 FF FF 7F 73 30 38  ..R..........s08
0520: 36 29 0B 77 62 06 01 0F  45 0B 80 F0 FF FF 7F F0  6).wb...E.......
0530: FF FF 7F 73 30 38 37 00  80 27 0B 71 62 06 01 16  ...s087..'.qb...
0540: 2B 71 62 06 01 13 80 23  29 08 76 62 06 01 02 2A  +qb....#).vb...*
0550: 0B 71 62 06 01 7B 71 62  06 01 52 0B 80 F0 FF FF  .qb..{qb..R.....
0560: 7F F0 FF FF 7F 73 30 38  37 45 0B 80 F0 FF FF 7F  .....s087E......
0570: F0 FF FF 7F 73 30 38 38  00 80 29 0B 71 62 06 01  ....s088..).qb..
0580: 1F 52 0B 80 F0 FF FF 7F  F0 FF FF 7F 73 30 38 38  .R..........s088
0590: 45 0B 80 F0 FF FF 7F F0  FF FF 7F 73 30 38 39 00  E..........s089.
05A0: 80 4A 77 62 06 01 74 62  06 01 4A 76 62 06 01 74  .Jwb..tb..Jvb..t
05B0: 62 06 01 79 00 71 62 06  01 74 62 06 01 29 08 74  b..y.qb..tb..).t
05C0: 62 06 01 01 29 0B 74 62  06 01 11 29 0B 72 62 06  b...).tb...).rb.
05D0: 01 14 52 0B 80 F0 FF FF  7F F0 FF FF 7F 73 30 38  ..R..........s08
05E0: 39 45 0B 80 F0 FF FF 7F  F0 FF FF 7F 73 30 39 30  9E..........s090
05F0: 00 80 4A 71 62 06 01 72  62 06 01 6F 76 71 62 06  ..Jqb..rb..ovqb.
0600: 01 29 0B 71 62 06 01 20  29 08 74 62 06 01 02 52  .).qb.. ).tb...R
0610: 0B 80 F0 FF FF 7F F0 FF  FF 7F 73 30 39 30 79 00  ..........s090y.
0620: 71 62 06 01 78 62 06 01  1C 04 80 29 0B 71 62 06  qb..xb.....).qb.
0630: 01 21 5D 00 80 14 80 27  0B 78 62 06 01 02 1C 15  .!]....'.xb.....
0640: 80 45 12 80 F0 FF FF 7F  F0 FF FF 7F 73 30 37 33  .E..........s073
0650: 00 80 1C 16 80 52 12 80  F0 FF FF 7F F0 FF FF 7F  .....R..........
0660: 73 30 37 33 45 0B 80 F0  FF FF 7F F0 FF FF 7F 73  s073E..........s
0670: 30 39 31 00 80 27 0B F0  FF FF 7F 11 27 0B 7A 62  091..'......'.zb
0680: 06 01 1E 1C 04 80 45 17  80 F0 FF FF 7F F0 FF FF  ......E.........
0690: 7F 77 68 6F 31 00 80 2A  0B 7A 62 06 01 2A 0B F0  .who1..*.zb..*..
06A0: FF FF 7F 52 0B 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...R..........s0
06B0: 39 31 1C 18 80 5C 00 08  80 5C 01 08 80 5D 08 80  91...\...\...]..
06C0: 09 80 45 01 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  ..E..........fdo
06D0: 31 00 80 1C 18 80 02 09  10 19 80 00 E4 06 4E 01  1.............N.
06E0: F0 FF FF 7F 45 0B 80 F0  FF FF 7F F0 FF FF 7F 73  ....E..........s
06F0: 30 39 32 00 80 45 17 80  F0 FF FF 7F F0 FF FF 7F  092..E..........
0700: 77 68 69 31 00 80 29 0B  77 62 06 01 12 29 0B 73  whi1..).wb...).s
0710: 62 06 01 1C 27 0B 7A 62  06 01 26 29 0B 74 62 06  b...'.zb..&).tb.
0720: 01 12 2A 0B 7A 62 06 01  27 0B 72 62 06 01 12 2B  ..*.zb..'.rb...+
0730: 72 62 06 01 1A 80 23 2A  0B 72 62 06 01 27 0B 7A  rb....#*.rb..'.z
0740: 62 06 01 26 29 0B 71 62  06 01 22 2A 0B 7A 62 06  b..&).qb.."*.zb.
0750: 01 27 0B 71 62 06 01 17  2B 71 62 06 01 1B 80 23  .'.qb...+qb....#
0760: 2A 0B 71 62 06 01 27 0B  7A 62 06 01 26 29 0B 75  *.qb..'.zb..&).u
0770: 62 06 01 17 2A 0B 7A 62  06 01 29 0B 71 62 06 01  b...*.zb..).qb..
0780: 24 1C 02 80 29 0B 76 62  06 01 0D 29 0B 71 62 06  $...).vb...).qb.
0790: 01 25 5D 00 80 01 80 1C  02 80 2B 71 62 06 01 1C  .%].......+qb...
07A0: 80 23 1C 18 80 4E 01 71  62 06 01 4E 01 75 62 06  .#...N.qb..N.ub.
07B0: 01 4E 01 72 62 06 01 4E  01 76 62 06 01 4E 01 74  .N.rb..N.vb..N.t
07C0: 62 06 01 4E 01 77 62 06  01 4E 01 73 62 06 01 4E  b..N.wb..N.sb..N
07D0: 01 78 62 06 01 29 0B F0  FF FF 7F 13 4A 7A 62 06  .xb..)......Jzb.
07E0: 01 F0 FF FF 7F 6F 76 7A  62 06 01 79 00 7A 62 06  .....ovzb..y.zb.
07F0: 01 F0 FF FF 7F 4E 01 F0  FF FF 7F 29 08 7A 62 06  .....N.....).zb.
0800: 01 05 29 08 7A 62 06 01  06 1C 1D 80 5C 00 00 80  ..).zb......\...
0810: 5C 01 00 80 5D 08 80 09  80 02 09 10 19 80 00 2C  \...]..........,
0820: 08 4E 00 F0 FF FF 7F 80  F0 FF FF 7F 45 0B 80 F0  .N..........E...
0830: FF FF 7F F0 FF FF 7F 73  30 39 33 00 80 45 01 80  .......s093..E..
0840: F8 FF FF 7F F8 FF FF 7F  66 64 69 31 00 80 29 0B  ........fdi1..).
0850: 7A 62 06 01 2C 52 0B 80  F0 FF FF 7F F0 FF FF 7F  zb..,R..........
0860: 73 30 39 33 4E 00 F0 FF  FF 7F 45 0B 80 F0 FF FF  s093N.....E.....
0870: 7F F0 FF FF 7F 73 30 39  34 00 80 29 0B F0 FF FF  .....s094..)....
0880: 7F 12 29 0B 7A 62 06 01  2D 52 0B 80 F0 FF FF 7F  ..).zb..-R......
0890: F0 FF FF 7F 73 30 39 34  45 0B 80 F0 FF FF 7F F0  ....s094E.......
08A0: FF FF 7F 73 30 39 35 00  80 4A F0 FF FF 7F 7B 62  ...s095..J....{b
08B0: 06 01 6F 76 F0 FF FF 7F  79 00 7A 62 06 01 7B 62  ..ov....y.zb..{b
08C0: 06 01 29 0B 7A 62 06 01  2E 79 00 7A 62 06 01 F0  ..).zb...y.zb...
08D0: FF FF 7F 29 0B 7A 62 06  01 2F 52 0B 80 F0 FF FF  ...).zb../R.....
08E0: 7F F0 FF FF 7F 73 30 39  35 45 0B 80 F0 FF FF 7F  .....s095E......
08F0: F0 FF FF 7F 73 30 39 36  00 80 29 0B 7A 62 06 01  ....s096..).zb..
0900: 30 45 0B 80 F0 FF FF 7F  F0 FF FF 7F 73 30 39 37  0E..........s097
0910: 00 80 27 0B 7A 62 06 01  25 2B 7A 62 06 01 1E 80  ..'.zb..%+zb....
0920: 23 2A 0B 7A 62 06 01 5D  00 80 01 80 1C 04 80 2B  #*.zb..].......+
0930: 7A 62 06 01 1F 80 23 45  01 80 F8 FF FF 7F F8 FF  zb....#E........
0940: FF 7F 66 64 6F 31 00 80  1C 01 80 52 0B 80 F0 FF  ..fdo1.....R....
0950: FF 7F F0 FF FF 7F 73 30  39 37 5C 00 00 80 5C 01  ......s097\...\.
0960: 00 80 5D 08 80 09 80 46  00 45 01 80 F8 FF FF 7F  ..]....F.E......
0970: F8 FF FF 7F 66 64 69 31  00 80 45 17 80 F0 FF FF  ....fdi1..E.....
0980: 7F F0 FF FF 7F 71 73 74  63 00 80 20 00 21 00     .....qstc.. .!. 
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0006 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
  4: 0x000B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  5: 0x001C [0x1C] WAIT(100* ticks)
  6: 0x001F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  7: 0x0022 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0C)
  8: 0x0029 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0E)
  9: 0x0030 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
 10: 0x0032 [0x4E] SET_ENTITY_HIDE_FLAG: Show Nanaa Mihgo (ID: 17195642/0x0106627A)
 11: 0x0038 [0x80] LOAD_WAIT(entity=Nanaa Mihgo (ID: 17195642/0x0106627A))
 12: 0x003D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x14)
 13: 0x0044 [0x1C] WAIT(60* ticks)
 14: 0x0047 [0x48] [System] [7507*]:
    → "You find an old chest!"
 15: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x004B [0x48] [System] [7508*]:
    → "However, your $3 breaks."
 17: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x004F [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 120*
 19: 0x0053 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 120*
 20: 0x0057 [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
 21: 0x005C [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x10)
 22: 0x0063 [0x27] REQ_SET(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x18)
 23: 0x006A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 24: 0x007B [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x23)
 25: 0x0082 [0x2B] Nanaa Mihgo (ID: 17195642/0x0106627A) [7509*]:
    → "Hey! What do you think you're doing, finding the trrreasure chest before me!?"
 26: 0x0089 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x008A [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A))
 28: 0x0090 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Vauderame (ID: 17195633/0x01066271))
 29: 0x0096 [0x52] END_LOAD_SCHEDULER: End scheduler "s077" with entities [LocalPlayer, LocalPlayer], work=15*
 30: 0x00A5 [0x4A] LocalPlayer looks at Nanaa Mihgo (ID: 17195642/0x0106627A)
 31: 0x00AE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s076" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
 32: 0x00BF [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x24)
 33: 0x00C6 [0x2B] Nanaa Mihgo (ID: 17195642/0x0106627A) [7510*]:
    → "Rrright, move it or lose it. I'll be the one to open it."
 34: 0x00CD [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x00CE [0x2B] Nanaa Mihgo (ID: 17195642/0x0106627A) [7511*]:
    → "There might be some kinda nasty trrrap just waiting to spring on a kitten like you."
 36: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x00D6 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A))
 38: 0x00DC [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x20)
 39: 0x00E3 [0x1C] WAIT(30* ticks)
 40: 0x00E6 [0x52] END_LOAD_SCHEDULER: End scheduler "s076" with entities [LocalPlayer, LocalPlayer], work=15*
 41: 0x00F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 42: 0x0106 [0x1C] WAIT(60* ticks)
 43: 0x0109 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A))
 44: 0x010F [0x4A] LocalPlayer looks at Takarabako (ID: 17195643/0x0106627B)
 45: 0x0118 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 46: 0x0119 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 47: 0x011E [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x1F)
 48: 0x0125 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s078" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
 49: 0x0136 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "open" with entities [EventEntity, EventEntity]
 50: 0x0143 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 51: 0x0154 [0x2B] Nanaa Mihgo (ID: 17195642/0x0106627A) [7512*]:
    → "...Rauuugh! Got it open! Now, let's take a look at the treasure..."
 52: 0x015B [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x015C [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A))
 54: 0x0162 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x2A)
 55: 0x0169 [0x52] END_LOAD_SCHEDULER: End scheduler "s078" with entities [LocalPlayer, LocalPlayer], work=15*
 56: 0x0178 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s079" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
 57: 0x0189 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
 58: 0x018E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x2B)
 59: 0x0195 [0x1C] WAIT(60* ticks)
 60: 0x0198 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x19)
 61: 0x019F [0x4A] Nanaa Mihgo (ID: 17195642/0x0106627A) looks at Vauderame (ID: 17195633/0x01066271)
 62: 0x01A8 [0x4A] LocalPlayer looks at Vauderame (ID: 17195633/0x01066271)
 63: 0x01B1 [0x4E] SET_ENTITY_HIDE_FLAG: Show Ulzana (ID: 17195639/0x01066277)
 64: 0x01B7 [0x52] END_LOAD_SCHEDULER: End scheduler "s079" with entities [LocalPlayer, LocalPlayer], work=15*
 65: 0x01C6 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 170*
 66: 0x01CA [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 170*
 67: 0x01CE [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
 68: 0x01D3 [0x27] REQ_SET(priority=0x0B, entity_id=Ulzana (ID: 17195639/0x01066277), tag_num=0x10)
 69: 0x01DA [0x1C] WAIT(30* ticks)
 70: 0x01DD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s072" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
 71: 0x01EE [0x2B] Ulzana (ID: 17195639/0x01066277) [7516*]:
    → "You two! Stay where you are!"
 72: 0x01F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 73: 0x01F6 [0x4E] SET_ENTITY_HIDE_FLAG: Show Vauderame (ID: 17195633/0x01066271)
 74: 0x01FC [0x4E] SET_ENTITY_HIDE_FLAG: Show Pauluart (ID: 17195637/0x01066275)
 75: 0x0202 [0x4E] SET_ENTITY_HIDE_FLAG: Show Chepelle (ID: 17195634/0x01066272)
 76: 0x0208 [0x4E] SET_ENTITY_HIDE_FLAG: Show Kanika (ID: 17195638/0x01066276)
 77: 0x020E [0x4E] SET_ENTITY_HIDE_FLAG: Show Sneaking Tiger (ID: 17195636/0x01066274)
 78: 0x0214 [0x4E] SET_ENTITY_HIDE_FLAG: Show Linzaza (ID: 17195635/0x01066273)
 79: 0x021A [0x4E] SET_ENTITY_HIDE_FLAG: Show Rohemolipaud (ID: 17195640/0x01066278)
 80: 0x0220 [0x1C] WAIT(100* ticks)
 81: 0x0223 [0x52] END_LOAD_SCHEDULER: End scheduler "s072" with entities [LocalPlayer, LocalPlayer], work=15*
 82: 0x0232 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 83: 0x0243 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s073" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
 84: 0x0254 [0x27] REQ_SET(priority=0x0B, entity_id=Linzaza (ID: 17195635/0x01066273), tag_num=0x19)
 85: 0x025B [0x27] REQ_SET(priority=0x0B, entity_id=Sneaking Tiger (ID: 17195636/0x01066274), tag_num=0x0F)
 86: 0x0262 [0x27] REQ_SET(priority=0x0B, entity_id=Pauluart (ID: 17195637/0x01066275), tag_num=0x15)
 87: 0x0269 [0x27] REQ_SET(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x15)
 88: 0x0270 [0x27] REQ_SET(priority=0x0B, entity_id=Chepelle (ID: 17195634/0x01066272), tag_num=0x11)
 89: 0x0277 [0x27] REQ_SET(priority=0x0B, entity_id=Kanika (ID: 17195638/0x01066276), tag_num=0x0A)
 90: 0x027E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s073" with entities [LocalPlayer, LocalPlayer], work=15*
 91: 0x028D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 92: 0x029E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s074" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
 93: 0x02AF [0x1C] WAIT(200* ticks)
 94: 0x02B2 [0x52] END_LOAD_SCHEDULER: End scheduler "s074" with entities [LocalPlayer, LocalPlayer], work=15*
 95: 0x02C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 96: 0x02D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s074" with entities [LocalPlayer, LocalPlayer], work=[92*, 0*]
 97: 0x02E3 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Ulzana (ID: 17195639/0x01066277))
 98: 0x02E9 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Linzaza (ID: 17195635/0x01066273))
 99: 0x02EF [0x2A] GET_REQ_LEVEL(level=11, entity_id=Sneaking Tiger (ID: 17195636/0x01066274))
100: 0x02F5 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Pauluart (ID: 17195637/0x01066275))
101: 0x02FB [0x2A] GET_REQ_LEVEL(level=11, entity_id=Vauderame (ID: 17195633/0x01066271))
102: 0x0301 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Chepelle (ID: 17195634/0x01066272))
103: 0x0307 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Kanika (ID: 17195638/0x01066276))
104: 0x030D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x22)
105: 0x0314 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x05)
106: 0x031B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x06)
107: 0x0322 [0x52] END_LOAD_SCHEDULER: End scheduler "s074" with entities [LocalPlayer, LocalPlayer], work=92*
108: 0x0331 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s072" with entities [LocalPlayer, LocalPlayer], work=[92*, 0*]
109: 0x0342 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Sneaking Tiger (ID: 17195636/0x01066274), tag_num=0x10)
110: 0x0349 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Linzaza (ID: 17195635/0x01066273), tag_num=0x1A)
111: 0x0350 [0x52] END_LOAD_SCHEDULER: End scheduler "s072" with entities [LocalPlayer, LocalPlayer], work=15*
112: 0x035F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s080" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
113: 0x0370 [0x4A] Kanika (ID: 17195638/0x01066276) looks at Vauderame (ID: 17195633/0x01066271)
114: 0x0379 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
115: 0x037A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Kanika (ID: 17195638/0x01066276) Render.Flags0 and Render.Flags3 conditions are met
116: 0x037F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kanika (ID: 17195638/0x01066276), tag_num=0x0B)
117: 0x0386 [0x79] Vauderame (ID: 17195633/0x01066271) looks at Kanika (ID: 17195638/0x01066276) (Basic look)
118: 0x0390 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x1A)
119: 0x0397 [0x52] END_LOAD_SCHEDULER: End scheduler "s080" with entities [LocalPlayer, LocalPlayer], work=15*
120: 0x03A6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s081" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
121: 0x03B7 [0x4A] Kanika (ID: 17195638/0x01066276) looks at Nanaa Mihgo (ID: 17195642/0x0106627A)
122: 0x03C0 [0x7B] Vauderame (ID: 17195633/0x01066271) stops talking
123: 0x03C5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x1B)
124: 0x03CC [0x79] Chepelle (ID: 17195634/0x01066272) looks at Vauderame (ID: 17195633/0x01066271) (Basic look)
125: 0x03D6 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Chepelle (ID: 17195634/0x01066272), tag_num=0x13)
126: 0x03DD [0x52] END_LOAD_SCHEDULER: End scheduler "s081" with entities [LocalPlayer, LocalPlayer], work=15*
127: 0x03EC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
128: 0x03FD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s082" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
129: 0x040E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x1C)
130: 0x0415 [0x52] END_LOAD_SCHEDULER: End scheduler "s082" with entities [LocalPlayer, LocalPlayer], work=15*
131: 0x0424 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s083" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
132: 0x0435 [0x7B] Chepelle (ID: 17195634/0x01066272) stops talking
133: 0x043A [0x79] Vauderame (ID: 17195633/0x01066271) looks at Linzaza (ID: 17195635/0x01066273) (Basic look)
134: 0x0444 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x1D)
135: 0x044B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Linzaza (ID: 17195635/0x01066273), tag_num=0x1B)
136: 0x0452 [0x52] END_LOAD_SCHEDULER: End scheduler "s083" with entities [LocalPlayer, LocalPlayer], work=15*
137: 0x0461 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s084" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
138: 0x0472 [0x7B] Vauderame (ID: 17195633/0x01066271) stops talking
139: 0x0477 [0x79] Kanika (ID: 17195638/0x01066276) looks at Pauluart (ID: 17195637/0x01066275) (Basic look)
140: 0x0481 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pauluart (ID: 17195637/0x01066275), tag_num=0x16)
141: 0x0488 [0x52] END_LOAD_SCHEDULER: End scheduler "s084" with entities [LocalPlayer, LocalPlayer], work=15*
142: 0x0497 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s085" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
143: 0x04A8 [0x7B] Kanika (ID: 17195638/0x01066276) stops talking
144: 0x04AD [0x4A] Kanika (ID: 17195638/0x01066276) looks at Ulzana (ID: 17195639/0x01066277)
145: 0x04B6 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Ulzana (ID: 17195639/0x01066277), tag_num=0x11)
146: 0x04BD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
147: 0x04BE [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Kanika (ID: 17195638/0x01066276) Render.Flags0 and Render.Flags3 conditions are met
148: 0x04C3 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kanika (ID: 17195638/0x01066276), tag_num=0x03)
149: 0x04CA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kanika (ID: 17195638/0x01066276), tag_num=0x04)
150: 0x04D1 [0x52] END_LOAD_SCHEDULER: End scheduler "s085" with entities [LocalPlayer, LocalPlayer], work=15*
151: 0x04E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s086" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
152: 0x04F1 [0x79] Vauderame (ID: 17195633/0x01066271) looks at Kanika (ID: 17195638/0x01066276) (Basic look)
153: 0x04FB [0x4A] Kanika (ID: 17195638/0x01066276) looks at Vauderame (ID: 17195633/0x01066271)
154: 0x0504 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kanika (ID: 17195638/0x01066276), tag_num=0x01)
155: 0x050B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kanika (ID: 17195638/0x01066276), tag_num=0x0C)
156: 0x0512 [0x52] END_LOAD_SCHEDULER: End scheduler "s086" with entities [LocalPlayer, LocalPlayer], work=15*
157: 0x0521 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Ulzana (ID: 17195639/0x01066277), tag_num=0x0F)
158: 0x0528 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s087" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
159: 0x0539 [0x27] REQ_SET(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x16)
160: 0x0540 [0x2B] Vauderame (ID: 17195633/0x01066271) [7529*]:
    → "You forget, Kanika. Atarefaunet's band is no more. We are now known as Vauderame's Knights."
161: 0x0547 [0x23] WAIT_FOR_DIALOG_INTERACTION
162: 0x0548 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kanika (ID: 17195638/0x01066276), tag_num=0x02)
163: 0x054F [0x2A] GET_REQ_LEVEL(level=11, entity_id=Vauderame (ID: 17195633/0x01066271))
164: 0x0555 [0x7B] Vauderame (ID: 17195633/0x01066271) stops talking
165: 0x055A [0x52] END_LOAD_SCHEDULER: End scheduler "s087" with entities [LocalPlayer, LocalPlayer], work=15*
166: 0x0569 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s088" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
167: 0x057A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x1F)
168: 0x0581 [0x52] END_LOAD_SCHEDULER: End scheduler "s088" with entities [LocalPlayer, LocalPlayer], work=15*
169: 0x0590 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s089" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
170: 0x05A1 [0x4A] Ulzana (ID: 17195639/0x01066277) looks at Sneaking Tiger (ID: 17195636/0x01066274)
171: 0x05AA [0x4A] Kanika (ID: 17195638/0x01066276) looks at Sneaking Tiger (ID: 17195636/0x01066274)
172: 0x05B3 [0x79] Vauderame (ID: 17195633/0x01066271) looks at Sneaking Tiger (ID: 17195636/0x01066274) (Basic look)
173: 0x05BD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Sneaking Tiger (ID: 17195636/0x01066274), tag_num=0x01)
174: 0x05C4 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Sneaking Tiger (ID: 17195636/0x01066274), tag_num=0x11)
175: 0x05CB [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Chepelle (ID: 17195634/0x01066272), tag_num=0x14)
176: 0x05D2 [0x52] END_LOAD_SCHEDULER: End scheduler "s089" with entities [LocalPlayer, LocalPlayer], work=15*
177: 0x05E1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s090" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
178: 0x05F2 [0x4A] Vauderame (ID: 17195633/0x01066271) looks at Chepelle (ID: 17195634/0x01066272)
179: 0x05FB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
180: 0x05FC [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Vauderame (ID: 17195633/0x01066271) Render.Flags0 and Render.Flags3 conditions are met
181: 0x0601 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x20)
182: 0x0608 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Sneaking Tiger (ID: 17195636/0x01066274), tag_num=0x02)
183: 0x060F [0x52] END_LOAD_SCHEDULER: End scheduler "s090" with entities [LocalPlayer, LocalPlayer], work=15*
184: 0x061E [0x79] Vauderame (ID: 17195633/0x01066271) looks at Rohemolipaud (ID: 17195640/0x01066278) (Basic look)
185: 0x0628 [0x1C] WAIT(60* ticks)
186: 0x062B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x21)
187: 0x0632 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=20*)
188: 0x0637 [0x27] REQ_SET(priority=0x0B, entity_id=Rohemolipaud (ID: 17195640/0x01066278), tag_num=0x02)
189: 0x063E [0x1C] WAIT(10* ticks)
190: 0x0641 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s073" with entities [LocalPlayer, LocalPlayer], work=[92*, 0*]
191: 0x0652 [0x1C] WAIT(110* ticks)
192: 0x0655 [0x52] END_LOAD_SCHEDULER: End scheduler "s073" with entities [LocalPlayer, LocalPlayer], work=92*
193: 0x0664 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s091" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
194: 0x0675 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x11)
195: 0x067C [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x1E)
196: 0x0683 [0x1C] WAIT(60* ticks)
197: 0x0686 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
198: 0x0697 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A))
199: 0x069D [0x2A] GET_REQ_LEVEL(level=11, entity_id=LocalPlayer)
200: 0x06A3 [0x52] END_LOAD_SCHEDULER: End scheduler "s091" with entities [LocalPlayer, LocalPlayer], work=15*
201: 0x06B2 [0x1C] WAIT(300* ticks)
202: 0x06B5 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 127*
203: 0x06B9 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 127*
204: 0x06BD [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
205: 0x06C2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
206: 0x06D3 [0x1C] WAIT(300* ticks)
207: 0x06D6 [0x02] IF !(Work_Zone[9] == 8*) GOTO 0x06E4
208: 0x06DE [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
209: 0x06E4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s092" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
210: 0x06F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
211: 0x0706 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Ulzana (ID: 17195639/0x01066277), tag_num=0x12)
212: 0x070D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Linzaza (ID: 17195635/0x01066273), tag_num=0x1C)
213: 0x0714 [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x26)
214: 0x071B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Sneaking Tiger (ID: 17195636/0x01066274), tag_num=0x12)
215: 0x0722 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A))
216: 0x0728 [0x27] REQ_SET(priority=0x0B, entity_id=Chepelle (ID: 17195634/0x01066272), tag_num=0x12)
217: 0x072F [0x2B] Chepelle (ID: 17195634/0x01066272) [7538*]:
    → "...Are you sure about those two? It's not like you to leave loose ends, even if their memory has been erased."
218: 0x0736 [0x23] WAIT_FOR_DIALOG_INTERACTION
219: 0x0737 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Chepelle (ID: 17195634/0x01066272))
220: 0x073D [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x26)
221: 0x0744 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x22)
222: 0x074B [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A))
223: 0x0751 [0x27] REQ_SET(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x17)
224: 0x0758 [0x2B] Vauderame (ID: 17195633/0x01066271) [7540*]:
    → "Then there is this adventurer. [He/She] looks like someone I did away with in another time..."
225: 0x075F [0x23] WAIT_FOR_DIALOG_INTERACTION
226: 0x0760 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Vauderame (ID: 17195633/0x01066271))
227: 0x0766 [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x26)
228: 0x076D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pauluart (ID: 17195637/0x01066275), tag_num=0x17)
229: 0x0774 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A))
230: 0x077A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x24)
231: 0x0781 [0x1C] WAIT(100* ticks)
232: 0x0784 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kanika (ID: 17195638/0x01066276), tag_num=0x0D)
233: 0x078B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17195633/0x01066271), tag_num=0x25)
234: 0x0792 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
235: 0x0797 [0x1C] WAIT(100* ticks)
236: 0x079A [0x2B] Vauderame (ID: 17195633/0x01066271) [7545*]:
    → "My homeland, Tavnazia."
237: 0x07A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
238: 0x07A2 [0x1C] WAIT(300* ticks)
239: 0x07A5 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Vauderame (ID: 17195633/0x01066271)
240: 0x07AB [0x4E] SET_ENTITY_HIDE_FLAG: Hide Pauluart (ID: 17195637/0x01066275)
241: 0x07B1 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Chepelle (ID: 17195634/0x01066272)
242: 0x07B7 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Kanika (ID: 17195638/0x01066276)
243: 0x07BD [0x4E] SET_ENTITY_HIDE_FLAG: Hide Sneaking Tiger (ID: 17195636/0x01066274)
244: 0x07C3 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Ulzana (ID: 17195639/0x01066277)
245: 0x07C9 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Linzaza (ID: 17195635/0x01066273)
246: 0x07CF [0x4E] SET_ENTITY_HIDE_FLAG: Hide Rohemolipaud (ID: 17195640/0x01066278)
247: 0x07D5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x13)
248: 0x07DC [0x4A] Nanaa Mihgo (ID: 17195642/0x0106627A) looks at LocalPlayer
249: 0x07E5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
250: 0x07E6 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Nanaa Mihgo (ID: 17195642/0x0106627A) Render.Flags0 and Render.Flags3 conditions are met
251: 0x07EB [0x79] Nanaa Mihgo (ID: 17195642/0x0106627A) looks at LocalPlayer (Basic look)
252: 0x07F5 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
253: 0x07FB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x05)
254: 0x0802 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x06)
255: 0x0809 [0x1C] WAIT(400* ticks)
256: 0x080C [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
257: 0x0810 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
258: 0x0814 [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
259: 0x0819 [0x02] IF !(Work_Zone[9] == 8*) GOTO 0x082C
260: 0x0821 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
261: 0x0827 [0x80] LOAD_WAIT(entity=LocalPlayer)
262: 0x082C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s093" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
263: 0x083D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
264: 0x084E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x2C)
265: 0x0855 [0x52] END_LOAD_SCHEDULER: End scheduler "s093" with entities [LocalPlayer, LocalPlayer], work=15*
266: 0x0864 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
267: 0x086A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s094" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
268: 0x087B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x12)
269: 0x0882 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x2D)
270: 0x0889 [0x52] END_LOAD_SCHEDULER: End scheduler "s094" with entities [LocalPlayer, LocalPlayer], work=15*
271: 0x0898 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s095" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
272: 0x08A9 [0x4A] LocalPlayer looks at Takarabako (ID: 17195643/0x0106627B)
273: 0x08B2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
274: 0x08B3 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
275: 0x08B8 [0x79] Nanaa Mihgo (ID: 17195642/0x0106627A) looks at Takarabako (ID: 17195643/0x0106627B) (Basic look)
276: 0x08C2 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x2E)
277: 0x08C9 [0x79] Nanaa Mihgo (ID: 17195642/0x0106627A) looks at LocalPlayer (Basic look)
278: 0x08D3 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x2F)
279: 0x08DA [0x52] END_LOAD_SCHEDULER: End scheduler "s095" with entities [LocalPlayer, LocalPlayer], work=15*
280: 0x08E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s096" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
281: 0x08FA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x30)
282: 0x0901 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s097" with entities [LocalPlayer, LocalPlayer], work=[15*, 0*]
283: 0x0912 [0x27] REQ_SET(priority=0x0B, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A), tag_num=0x25)
284: 0x0919 [0x2B] Nanaa Mihgo (ID: 17195642/0x0106627A) [7552*]:
    → "Time to leave this place behind. Although I would like to see Vauderame's face when he opens the chest to find it empty..."
285: 0x0920 [0x23] WAIT_FOR_DIALOG_INTERACTION
286: 0x0921 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Nanaa Mihgo (ID: 17195642/0x0106627A))
287: 0x0927 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
288: 0x092C [0x1C] WAIT(60* ticks)
289: 0x092F [0x2B] Nanaa Mihgo (ID: 17195642/0x0106627A) [7553*]:
    → "...Hmmm. I get the feeling there's something important I'm forgetting..."
290: 0x0936 [0x23] WAIT_FOR_DIALOG_INTERACTION
291: 0x0937 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
292: 0x0948 [0x1C] WAIT(200* ticks)
293: 0x094B [0x52] END_LOAD_SCHEDULER: End scheduler "s097" with entities [LocalPlayer, LocalPlayer], work=15*
294: 0x095A [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
295: 0x095E [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
296: 0x0962 [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
297: 0x0967 [0x46] CAMERA_CONTROL: Restore default settings
298: 0x0969 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
299: 0x097A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
300: 0x098B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
301: 0x098D [0x21] END_EVENT
302: 0x098E [0x00] END_REQSTACK()
```
