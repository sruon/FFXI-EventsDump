# 17723546 - DoorReliquary

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 2712 bytes                    |
| Total Events     | 9                             |
| References Count | 51                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [38](#event-38)          | 0x0001       |      1 |              1 |
| [37](#event-37)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |      2 |              2 |
| [65535.2](#event-655352) | 0x0005       |      2 |              2 |
| [49](#event-49)          | 0x0007       |   2442 |            333 |
| [762](#event-762)        | 0x0991       |      1 |              1 |
| [65535.3](#event-655353) | 0x0992       |      2 |              2 |
| [65535.4](#event-655354) | 0x0994       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x00A0      |         160 |
|       3 | 0x0013      |          19 |
|       4 | 0x008C      |         140 |
|       5 | 0x0073      |         115 |
|       6 | 0x0083      |         131 |
|       7 | 0x0028      |          40 |
|       8 | 0x2FC5      |       12229 |
|       9 | 0x001E      |          30 |
|      10 | 0x00F0      |         240 |
|      11 | 0x0078      |         120 |
|      12 | 0x005A      |          90 |
|      13 | 0x2FC7      |       12231 |
|      14 | 0x000A      |          10 |
|      15 | 0x2FC8      |       12232 |
|      16 | 0x0005      |           5 |
|      17 | 0x2FC9      |       12233 |
|      18 | 0x003C      |          60 |
|      19 | 0x000F      |          15 |
|      20 | 0x2FCA      |       12234 |
|      21 | 0x2FCB      |       12235 |
|      22 | 0x2FCC      |       12236 |
|      23 | 0x2FCD      |       12237 |
|      24 | 0x2FCE      |       12238 |
|      25 | 0x2FCF      |       12239 |
|      26 | 0x0014      |          20 |
|      27 | 0x2FD0      |       12240 |
|      28 | 0x2FD1      |       12241 |
|      29 | 0x2FD2      |       12242 |
|      30 | 0x2FD3      |       12243 |
|      31 | 0x0001      |           1 |
|      32 | 0x2FD4      |       12244 |
|      33 | 0x0080      |         128 |
|      34 | 0x2FD5      |       12245 |
|      35 | 0x2FD6      |       12246 |
|      36 | 0x2FD7      |       12247 |
|      37 | 0x2FD8      |       12248 |
|      38 | 0x2FD9      |       12249 |
|      39 | 0x2FDA      |       12250 |
|      40 | 0x2FDB      |       12251 |
|      41 | 0x2FDC      |       12252 |
|      42 | 0x2FDD      |       12253 |
|      43 | 0x2FDE      |       12254 |
|      44 | 0x2FDF      |       12255 |
|      45 | 0x2FE0      |       12256 |
|      46 | 0x2FE1      |       12257 |
|      47 | 0x00B4      |         180 |
|      48 | 0x2FE2      |       12258 |
|      49 | 0x006B      |         107 |
|      50 | 0x00C9      |         201 |

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

### Event 38

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          4C 00                                       L.           
```

#### Opcodes

```
  0: 0x0003 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                4D 00                                   M.         
```

#### Opcodes

```
  0: 0x0005 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 49

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0007     |
| Data Size    | 2442 bytes |
| Instructions | 333        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      20  01 46 01 2F 00 B2 70 0E          .F./..p.
0010: 01 2F 00 B3 70 0E 01 42  45 00 80 F0 FF FF 7F F0  ./..p..BE.......
0020: FF FF 7F 66 64 6F 31 01  80 55 00 80 F0 FF FF 7F  ...fdo1..U......
0030: F0 FF FF 7F 66 64 6F 31  5C 00 02 80 5C 01 02 80  ....fdo1\...\...
0040: 38 03 80 29 03 F0 FF FF  7F 46 4E 01 0C 70 0E 01  8..).....FN..p..
0050: 4E 01 F0 FF FF 7F 2F 00  02 70 0E 01 2F 00 B1 70  N...../..p../..p
0060: 0E 01 2F 00 B0 70 0E 01  2F 00 AF 70 0E 01 2F 00  ../..p../..p../.
0070: B4 70 0E 01 2F 00 B5 70  0E 01 2F 00 B6 70 0E 01  .p../..p../..p..
0080: 2F 00 B7 70 0E 01 2F 00  B8 70 0E 01 2F 00 B9 70  /..p../..p../..p
0090: 0E 01 27 03 B2 70 0E 01  02 29 03 B3 70 0E 01 02  ..'..p...)..p...
00A0: 80 29 70 0E 01 80 B2 70  0E 01 80 B3 70 0E 01 5B  .)p....p....p..[
00B0: 04 80 B1 70 0E 01 B1 70  0E 01 00 FE FE FE 5B 05  ...p...p......[.
00C0: 80 02 70 0E 01 02 70 0E  01 00 FE FE FE 45 06 80  ..p...p......E..
00D0: F0 FF FF 7F F0 FF FF 7F  72 30 30 30 01 80 45 00  ........r000..E.
00E0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 01 80 55  .........fdi1..U
00F0: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 27 03  ..........fdi1'.
0100: 14 70 0E 01 09 55 06 80  F0 FF FF 7F F0 FF FF 7F  .p...U..........
0110: 72 30 30 30 1C 07 80 45  06 80 F0 FF FF 7F F0 FF  r000...E........
0120: FF 7F 72 30 30 31 01 80  55 06 80 F0 FF FF 7F F0  ..r001..U.......
0130: FF FF 7F 72 30 30 31 4E  00 02 70 0E 01 4E 00 B1  ...r001N..p..N..
0140: 70 0E 01 4E 00 B4 70 0E  01 4E 00 B5 70 0E 01 4E  p..N..p..N..p..N
0150: 00 B6 70 0E 01 4E 00 B7  70 0E 01 4E 00 B8 70 0E  ..p..N..p..N..p.
0160: 01 4E 00 B9 70 0E 01 2B  14 70 0E 01 08 80 23 4E  .N..p..+.p....#N
0170: 00 29 70 0E 01 27 03 29  70 0E 01 08 1C 09 80 27  .)p..'.)p......'
0180: 03 AF 70 0E 01 04 1C 0A  80 45 06 80 F0 FF FF 7F  ..p......E......
0190: F0 FF FF 7F 72 30 30 32  01 80 55 06 80 F0 FF FF  ....r002..U.....
01A0: 7F F0 FF FF 7F 72 30 30  32 2A 03 AF 70 0E 01 29  .....r002*..p..)
01B0: 04 29 70 0E 01 09 1C 0B  80 27 04 AF 70 0E 01 05  .)p......'..p...
01C0: 1C 0C 80 27 03 02 70 0E  01 25 27 03 B1 70 0E 01  ...'..p..%'..p..
01D0: 10 27 03 B4 70 0E 01 07  27 03 B6 70 0E 01 0C 27  .'..p...'..p...'
01E0: 03 B8 70 0E 01 0C 27 03  B5 70 0E 01 0C 27 03 B7  ..p...'..p...'..
01F0: 70 0E 01 0C 27 03 B9 70  0E 01 08 1C 09 80 45 06  p...'..p......E.
0200: 80 F0 FF FF 7F F0 FF FF  7F 72 30 30 33 01 80 55  .........r003..U
0210: 06 80 F0 FF FF 7F F0 FF  FF 7F 72 30 30 33 1C 0C  ..........r003..
0220: 80 2A 03 02 70 0E 01 2A  03 B1 70 0E 01 2A 03 B4  .*..p..*..p..*..
0230: 70 0E 01 2A 03 B5 70 0E  01 2A 03 B6 70 0E 01 2A  p..*..p..*..p..*
0240: 03 B7 70 0E 01 2A 03 B8  70 0E 01 2A 03 B9 70 0E  ..p..*..p..*..p.
0250: 01 1C 0C 80 29 03 B1 70  0E 01 11 2B B1 70 0E 01  ....)..p...+.p..
0260: 0D 80 23 27 04 B1 70 0E  01 12 79 00 02 70 0E 01  ..#'..p...y..p..
0270: B1 70 0E 01 79 00 AF 70  0E 01 B1 70 0E 01 1C 09  .p..y..p...p....
0280: 80 27 03 02 70 0E 01 26  1C 0E 80 45 06 80 F0 FF  .'..p..&...E....
0290: FF 7F F0 FF FF 7F 72 30  30 34 01 80 55 06 80 F0  ......r004..U...
02A0: FF FF 7F F0 FF FF 7F 72  30 30 34 2A 03 02 70 0E  .......r004*..p.
02B0: 01 1C 0E 80 27 04 02 70  0E 01 31 2B 02 70 0E 01  ....'..p..1+.p..
02C0: 0F 80 23 2A 04 B1 70 0E  01 27 05 B1 70 0E 01 13  ..#*..p..'..p...
02D0: 1C 0E 80 45 06 80 F0 FF  FF 7F F0 FF FF 7F 72 30  ...E..........r0
02E0: 30 35 01 80 27 04 02 70  0E 01 32 2A 05 B1 70 0E  05..'..p..2*..p.
02F0: 01 4E 01 02 70 0E 01 4E  01 B4 70 0E 01 4E 01 B5  .N..p..N..p..N..
0300: 70 0E 01 4E 01 B6 70 0E  01 4E 01 B7 70 0E 01 4E  p..N..p..N..p..N
0310: 01 B8 70 0E 01 4E 01 B9  70 0E 01 55 06 80 F0 FF  ..p..N..p..U....
0320: FF 7F F0 FF FF 7F 72 30  30 35 4E 00 02 70 0E 01  ......r005N..p..
0330: 4E 00 B4 70 0E 01 4E 00  B5 70 0E 01 4E 00 B6 70  N..p..N..p..N..p
0340: 0E 01 4E 00 B7 70 0E 01  4E 00 B8 70 0E 01 4E 00  ..N..p..N..p..N.
0350: B9 70 0E 01 1C 10 80 45  06 80 F0 FF FF 7F F0 FF  .p.....E........
0360: FF 7F 72 30 30 36 01 80  55 06 80 F0 FF FF 7F F0  ..r006..U.......
0370: FF FF 7F 72 30 30 36 2B  02 70 0E 01 11 80 23 1C  ...r006+.p....#.
0380: 0C 80 4A B1 70 0E 01 02  70 0E 01 6F 76 B1 70 0E  ..J.p...p..ov.p.
0390: 01 6B 64 66 74 30 B1 70  0E 01 1C 12 80 29 03 B1  .kdft0.p.....)..
03A0: 70 0E 01 14 27 04 B1 70  0E 01 15 1C 13 80 45 06  p...'..p......E.
03B0: 80 F0 FF FF 7F F0 FF FF  7F 72 30 30 37 01 80 55  .........r007..U
03C0: 06 80 F0 FF FF 7F F0 FF  FF 7F 72 30 30 37 2A 04  ..........r007*.
03D0: B1 70 0E 01 79 00 B4 70  0E 01 B1 70 0E 01 79 00  .p..y..p...p..y.
03E0: B5 70 0E 01 B1 70 0E 01  79 00 B6 70 0E 01 B1 70  .p...p..y..p...p
03F0: 0E 01 79 00 B7 70 0E 01  B1 70 0E 01 79 00 B8 70  ..y..p...p..y..p
0400: 0E 01 B1 70 0E 01 79 00  B9 70 0E 01 B1 70 0E 01  ...p..y..p...p..
0410: 45 06 80 F0 FF FF 7F F0  FF FF 7F 72 30 31 39 01  E..........r019.
0420: 80 55 06 80 F0 FF FF 7F  F0 FF FF 7F 72 30 31 39  .U..........r019
0430: 2B 02 70 0E 01 14 80 23  1C 12 80 45 06 80 F0 FF  +.p....#...E....
0440: FF 7F F0 FF FF 7F 72 30  32 32 01 80 55 06 80 F0  ......r022..U...
0450: FF FF 7F F0 FF FF 7F 72  30 32 32 1C 12 80 2B B4  .......r022...+.
0460: 70 0E 01 15 80 23 27 03  02 70 0E 01 27 2B 02 70  p....#'..p..'+.p
0470: 0E 01 16 80 23 2A 03 02  70 0E 01 4A 02 70 0E 01  ....#*..p..J.p..
0480: B1 70 0E 01 6F 76 02 70  0E 01 45 06 80 F0 FF FF  .p..ov.p..E.....
0490: 7F F0 FF FF 7F 72 30 30  38 01 80 55 06 80 F0 FF  .....r008..U....
04A0: FF 7F F0 FF FF 7F 72 30  30 38 1C 09 80 27 03 02  ......r008...'..
04B0: 70 0E 01 2D 2B 02 70 0E  01 17 80 23 45 06 80 F0  p..-+.p....#E...
04C0: FF FF 7F F0 FF FF 7F 72  30 30 39 01 80 55 06 80  .......r009..U..
04D0: F0 FF FF 7F F0 FF FF 7F  72 30 30 39 27 03 02 70  ........r009'..p
04E0: 0E 01 2E 2B B1 70 0E 01  18 80 23 27 03 B1 70 0E  ...+.p....#'..p.
04F0: 01 16 1C 09 80 45 06 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0500: 72 30 32 35 01 80 55 06  80 F0 FF FF 7F F0 FF FF  r025..U.........
0510: 7F 72 30 32 35 2A 03 B1  70 0E 01 1C 12 80 45 06  .r025*..p.....E.
0520: 80 F0 FF FF 7F F0 FF FF  7F 72 30 32 36 01 80 55  .........r026..U
0530: 06 80 F0 FF FF 7F F0 FF  FF 7F 72 30 32 36 2B 02  ..........r026+.
0540: 70 0E 01 19 80 23 27 03  B1 70 0E 01 17 27 03 02  p....#'..p...'..
0550: 70 0E 01 33 1C 09 80 2A  03 B1 70 0E 01 1C 0C 80  p..3...*..p.....
0560: 27 04 B1 70 0E 01 18 1C  1A 80 45 06 80 F0 FF FF  '..p......E.....
0570: 7F F0 FF FF 7F 72 30 32  33 01 80 55 06 80 F0 FF  .....r023..U....
0580: FF 7F F0 FF FF 7F 72 30  32 33 2B 02 70 0E 01 1B  ......r023+.p...
0590: 80 23 45 06 80 F0 FF FF  7F F0 FF FF 7F 72 30 32  .#E..........r02
05A0: 34 01 80 2B B1 70 0E 01  1C 80 23 55 06 80 F0 FF  4..+.p....#U....
05B0: FF 7F F0 FF FF 7F 72 30  32 34 27 03 AF 70 0E 01  ......r024'..p..
05C0: 06 1C 09 80 45 06 80 F0  FF FF 7F F0 FF FF 7F 72  ....E..........r
05D0: 30 31 31 01 80 55 06 80  F0 FF FF 7F F0 FF FF 7F  011..U..........
05E0: 72 30 31 31 29 03 B0 70  0E 01 02 29 04 AF 70 0E  r011)..p...)..p.
05F0: 01 07 29 04 B0 70 0E 01  03 27 05 B0 70 0E 01 04  ..)..p...'..p...
0600: 1C 09 80 45 06 80 F0 FF  FF 7F F0 FF FF 7F 72 30  ...E..........r0
0610: 31 32 01 80 55 06 80 F0  FF FF 7F F0 FF FF 7F 72  12..U..........r
0620: 30 31 32 27 03 02 70 0E  01 28 2B 02 70 0E 01 1D  012'..p..(+.p...
0630: 80 23 45 06 80 F0 FF FF  7F F0 FF FF 7F 72 30 31  .#E..........r01
0640: 33 01 80 55 06 80 F0 FF  FF 7F F0 FF FF 7F 72 30  3..U..........r0
0650: 31 33 2A 05 B0 70 0E 01  29 03 AF 70 0E 01 08 27  13*..p..)..p...'
0660: 04 AF 70 0E 01 09 27 06  B0 70 0E 01 05 2B 35 70  ..p...'..p...+5p
0670: 0E 01 1E 80 23 79 00 02  70 0E 01 AF 70 0E 01 2A  ....#y..p...p..*
0680: 06 B0 70 0E 01 1C 09 80  45 06 80 F0 FF FF 7F F0  ..p.....E.......
0690: FF FF 7F 72 30 31 34 01  80 55 06 80 F0 FF FF 7F  ...r014..U......
06A0: F0 FF FF 7F 72 30 31 34  6C B1 70 0E 01 01 80 1F  ....r014l.p.....
06B0: 80 27 03 B1 70 0E 01 19  2A 04 AF 70 0E 01 1C 13  .'..p...*..p....
06C0: 80 79 00 AF 70 0E 01 B1  70 0E 01 1C 0B 80 27 03  .y..p...p.....'.
06D0: B0 70 0E 01 06 2B AF 70  0E 01 20 80 23 27 03 AF  .p...+.p.. .#'..
06E0: 70 0E 01 0A 1C 12 80 6C  B1 70 0E 01 21 80 1F 80  p......l.p..!...
06F0: 4A B1 70 0E 01 AF 70 0E  01 45 06 80 F0 FF FF 7F  J.p...p..E......
0700: F0 FF FF 7F 72 30 32 30  01 80 55 06 80 F0 FF FF  ....r020..U.....
0710: 7F F0 FF FF 7F 72 30 32  30 2A 03 AF 70 0E 01 2B  .....r020*..p..+
0720: B1 70 0E 01 22 80 23 2B  AF 70 0E 01 23 80 23 2B  .p..".#+.p..#.#+
0730: AF 70 0E 01 24 80 23 27  03 F0 FF FF 7F 47 1C 09  .p..$.#'.....G..
0740: 80 27 03 02 70 0E 01 29  1C 09 80 4A AF 70 0E 01  .'..p..)...J.p..
0750: 02 70 0E 01 6F 76 AF 70  0E 01 1C 09 80 45 06 80  .p..ov.p.....E..
0760: F0 FF FF 7F F0 FF FF 7F  72 30 31 35 01 80 55 06  ........r015..U.
0770: 80 F0 FF FF 7F F0 FF FF  7F 72 30 31 35 1C 12 80  .........r015...
0780: 2B AF 70 0E 01 25 80 23  7C 00 02 70 0E 01 2B 02  +.p..%.#|..p..+.
0790: 70 0E 01 26 80 23 7C 01  02 70 0E 01 2A 03 F0 FF  p..&.#|..p..*...
07A0: FF 7F 4A AF 70 0E 01 F0  FF FF 7F 6F 76 AF 70 0E  ..J.p......ov.p.
07B0: 01 2B AF 70 0E 01 27 80  23 2B AF 70 0E 01 28 80  .+.p..'.#+.p..(.
07C0: 23 29 03 AF 70 0E 01 0B  2B AF 70 0E 01 29 80 23  #)..p...+.p..).#
07D0: 1C 12 80 4A AF 70 0E 01  B1 70 0E 01 6F 76 AF 70  ...J.p...p..ov.p
07E0: 0E 01 1C 12 80 45 06 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
07F0: 72 30 31 36 01 80 55 06  80 F0 FF FF 7F F0 FF FF  r016..U.........
0800: 7F 72 30 31 36 6F 76 AF  70 0E 01 2B AF 70 0E 01  .r016ov.p..+.p..
0810: 2A 80 23 2B AF 70 0E 01  2B 80 23 27 03 AF 70 0E  *.#+.p..+.#'..p.
0820: 01 0B 2B AF 70 0E 01 2C  80 23 2A 03 AF 70 0E 01  ..+.p..,.#*..p..
0830: 1C 09 80 2B AF 70 0E 01  2D 80 23 1C 12 80 29 03  ...+.p..-.#...).
0840: AF 70 0E 01 0D 27 04 AF  70 0E 01 0E 1C 0C 80 27  .p...'..p......'
0850: 03 B1 70 0E 01 1A 79 00  02 70 0E 01 B1 70 0E 01  ..p...y..p...p..
0860: 79 00 F0 FF FF 7F B1 70  0E 01 1C 09 80 45 06 80  y......p.....E..
0870: F0 FF FF 7F F0 FF FF 7F  72 30 31 37 01 80 55 06  ........r017..U.
0880: 80 F0 FF FF 7F F0 FF FF  7F 72 30 31 37 2B B1 70  .........r017+.p
0890: 0E 01 2E 80 23 27 03 AF  70 0E 01 0F 1C 09 80 45  ....#'..p......E
08A0: 06 80 F0 FF FF 7F F0 FF  FF 7F 72 30 31 38 01 80  ..........r018..
08B0: 55 06 80 F0 FF FF 7F F0  FF FF 7F 72 30 31 38 2A  U..........r018*
08C0: 03 AF 70 0E 01 27 04 AF  70 0E 01 10 6C AF 70 0E  ..p..'..p...l.p.
08D0: 01 01 80 2F 80 1C 0B 80  45 06 80 F0 FF FF 7F F0  .../....E.......
08E0: FF FF 7F 72 30 31 37 01  80 55 06 80 F0 FF FF 7F  ...r017..U......
08F0: F0 FF FF 7F 72 30 31 37  1C 0B 80 2F 00 10 70 0E  ....r017.../..p.
0900: 01 4E 00 10 70 0E 01 2B  B1 70 0E 01 30 80 23 1C  .N..p..+.p..0.#.
0910: 0B 80 45 06 80 F0 FF FF  7F F0 FF FF 7F 72 30 32  ..E..........r02
0920: 31 01 80 55 06 80 F0 FF  FF 7F F0 FF FF 7F 72 30  1..U..........r0
0930: 32 31 29 03 10 70 0E 01  14 27 04 10 70 0E 01 15  21)..p...'..p...
0940: 1C 12 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0950: 6F 32 01 80 55 00 80 F0  FF FF 7F F0 FF FF 7F 66  o2..U..........f
0960: 64 6F 32 5C 00 31 80 5C  01 31 80 46 00 45 32 80  do2\.1.\.1.F.E2.
0970: F0 FF FF 7F F0 FF FF 7F  71 73 74 63 01 80 45 00  ........qstc..E.
0980: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 32 01 80 21  .........fdi2..!
0990: 00                                                .               
```

#### Opcodes

```
  0: 0x0007 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0009 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x000B [0x2F] Unnamed NPC (ID: 17723570/0x010E70B2)->Render.Flags0 &= ~0x80000 // Bit 19
  3: 0x0011 [0x2F] Unnamed NPC (ID: 17723571/0x010E70B3)->Render.Flags0 &= ~0x80000 // Bit 19
  4: 0x0017 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0018 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x0029 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  7: 0x0038 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 160*
  8: 0x003C [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 160*
  9: 0x0040 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 10: 0x0043 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x46)
 11: 0x004A [0x4E] SET_ENTITY_HIDE_FLAG: Hide Miageau (ID: 17723404/0x010E700C)
 12: 0x0050 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
 13: 0x0056 [0x2F] Trion (ID: 17723394/0x010E7002)->Render.Flags0 &= ~0x80000 // Bit 19
 14: 0x005C [0x2F] Curilla (ID: 17723569/0x010E70B1)->Render.Flags0 &= ~0x80000 // Bit 19
 15: 0x0062 [0x2F] Unnamed NPC (ID: 17723568/0x010E70B0)->Render.Flags0 &= ~0x80000 // Bit 19
 16: 0x0068 [0x2F] Rainemard (ID: 17723567/0x010E70AF)->Render.Flags0 &= ~0x80000 // Bit 19
 17: 0x006E [0x2F] Ferdechiond (ID: 17723572/0x010E70B4)->Render.Flags0 &= ~0x80000 // Bit 19
 18: 0x0074 [0x2F] Unnamed NPC (ID: 17723573/0x010E70B5)->Render.Flags0 &= ~0x80000 // Bit 19
 19: 0x007A [0x2F] Unnamed NPC (ID: 17723574/0x010E70B6)->Render.Flags0 &= ~0x80000 // Bit 19
 20: 0x0080 [0x2F] Unnamed NPC (ID: 17723575/0x010E70B7)->Render.Flags0 &= ~0x80000 // Bit 19
 21: 0x0086 [0x2F] Unnamed NPC (ID: 17723576/0x010E70B8)->Render.Flags0 &= ~0x80000 // Bit 19
 22: 0x008C [0x2F] Unnamed NPC (ID: 17723577/0x010E70B9)->Render.Flags0 &= ~0x80000 // Bit 19
 23: 0x0092 [0x27] REQ_SET(priority=0x03, entity_id=Unnamed NPC (ID: 17723570/0x010E70B2), tag_num=0x02)
 24: 0x0099 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Unnamed NPC (ID: 17723571/0x010E70B3), tag_num=0x02)
 25: 0x00A0 [0x80] LOAD_WAIT(entity=Aurege (ID: 17723433/0x010E7029))
 26: 0x00A5 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17723570/0x010E70B2))
 27: 0x00AA [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17723571/0x010E70B3))
 28: 0x00AF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [Curilla (ID: 17723569/0x010E70B1), Curilla (ID: 17723569/0x010E70B1)], work=140*
 29: 0x00BE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [Trion (ID: 17723394/0x010E7002), Trion (ID: 17723394/0x010E7002)], work=115*
 30: 0x00CD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r000" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 31: 0x00DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x00EF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 33: 0x00FE [0x27] REQ_SET(priority=0x03, entity_id=Maurine (ID: 17723412/0x010E7014), tag_num=0x09)
 34: 0x0105 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r000" with entities [LocalPlayer, LocalPlayer], work=131*
 35: 0x0114 [0x1C] WAIT(40* ticks)
 36: 0x0117 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r001" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 37: 0x0128 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r001" with entities [LocalPlayer, LocalPlayer], work=131*
 38: 0x0137 [0x4E] SET_ENTITY_HIDE_FLAG: Show Trion (ID: 17723394/0x010E7002)
 39: 0x013D [0x4E] SET_ENTITY_HIDE_FLAG: Show Curilla (ID: 17723569/0x010E70B1)
 40: 0x0143 [0x4E] SET_ENTITY_HIDE_FLAG: Show Ferdechiond (ID: 17723572/0x010E70B4)
 41: 0x0149 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723573/0x010E70B5)
 42: 0x014F [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723574/0x010E70B6)
 43: 0x0155 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723575/0x010E70B7)
 44: 0x015B [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723576/0x010E70B8)
 45: 0x0161 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723577/0x010E70B9)
 46: 0x0167 [0x2B] Maurine (ID: 17723412/0x010E7014) [12229*]:
    → "A ghost of a red mage is in the church!"
 47: 0x016E [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x016F [0x4E] SET_ENTITY_HIDE_FLAG: Show Aurege (ID: 17723433/0x010E7029)
 49: 0x0175 [0x27] REQ_SET(priority=0x03, entity_id=Aurege (ID: 17723433/0x010E7029), tag_num=0x08)
 50: 0x017C [0x1C] WAIT(30* ticks)
 51: 0x017F [0x27] REQ_SET(priority=0x03, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x04)
 52: 0x0186 [0x1C] WAIT(240* ticks)
 53: 0x0189 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r002" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 54: 0x019A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r002" with entities [LocalPlayer, LocalPlayer], work=131*
 55: 0x01A9 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Rainemard (ID: 17723567/0x010E70AF))
 56: 0x01AF [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Aurege (ID: 17723433/0x010E7029), tag_num=0x09)
 57: 0x01B6 [0x1C] WAIT(120* ticks)
 58: 0x01B9 [0x27] REQ_SET(priority=0x04, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x05)
 59: 0x01C0 [0x1C] WAIT(90* ticks)
 60: 0x01C3 [0x27] REQ_SET(priority=0x03, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x25)
 61: 0x01CA [0x27] REQ_SET(priority=0x03, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x10)
 62: 0x01D1 [0x27] REQ_SET(priority=0x03, entity_id=Ferdechiond (ID: 17723572/0x010E70B4), tag_num=0x07)
 63: 0x01D8 [0x27] REQ_SET(priority=0x03, entity_id=Unnamed NPC (ID: 17723574/0x010E70B6), tag_num=0x0C)
 64: 0x01DF [0x27] REQ_SET(priority=0x03, entity_id=Unnamed NPC (ID: 17723576/0x010E70B8), tag_num=0x0C)
 65: 0x01E6 [0x27] REQ_SET(priority=0x03, entity_id=Unnamed NPC (ID: 17723573/0x010E70B5), tag_num=0x0C)
 66: 0x01ED [0x27] REQ_SET(priority=0x03, entity_id=Unnamed NPC (ID: 17723575/0x010E70B7), tag_num=0x0C)
 67: 0x01F4 [0x27] REQ_SET(priority=0x03, entity_id=Unnamed NPC (ID: 17723577/0x010E70B9), tag_num=0x08)
 68: 0x01FB [0x1C] WAIT(30* ticks)
 69: 0x01FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r003" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 70: 0x020F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r003" with entities [LocalPlayer, LocalPlayer], work=131*
 71: 0x021E [0x1C] WAIT(90* ticks)
 72: 0x0221 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Trion (ID: 17723394/0x010E7002))
 73: 0x0227 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Curilla (ID: 17723569/0x010E70B1))
 74: 0x022D [0x2A] GET_REQ_LEVEL(level=3, entity_id=Ferdechiond (ID: 17723572/0x010E70B4))
 75: 0x0233 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Unnamed NPC (ID: 17723573/0x010E70B5))
 76: 0x0239 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Unnamed NPC (ID: 17723574/0x010E70B6))
 77: 0x023F [0x2A] GET_REQ_LEVEL(level=3, entity_id=Unnamed NPC (ID: 17723575/0x010E70B7))
 78: 0x0245 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Unnamed NPC (ID: 17723576/0x010E70B8))
 79: 0x024B [0x2A] GET_REQ_LEVEL(level=3, entity_id=Unnamed NPC (ID: 17723577/0x010E70B9))
 80: 0x0251 [0x1C] WAIT(90* ticks)
 81: 0x0254 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x11)
 82: 0x025B [0x2B] Curilla (ID: 17723569/0x010E70B1) [12231*]:
    → "Father!"
 83: 0x0262 [0x23] WAIT_FOR_DIALOG_INTERACTION
 84: 0x0263 [0x27] REQ_SET(priority=0x04, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x12)
 85: 0x026A [0x79] Trion (ID: 17723394/0x010E7002) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
 86: 0x0274 [0x79] Rainemard (ID: 17723567/0x010E70AF) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
 87: 0x027E [0x1C] WAIT(30* ticks)
 88: 0x0281 [0x27] REQ_SET(priority=0x03, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x26)
 89: 0x0288 [0x1C] WAIT(10* ticks)
 90: 0x028B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r004" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 91: 0x029C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r004" with entities [LocalPlayer, LocalPlayer], work=131*
 92: 0x02AB [0x2A] GET_REQ_LEVEL(level=3, entity_id=Trion (ID: 17723394/0x010E7002))
 93: 0x02B1 [0x1C] WAIT(10* ticks)
 94: 0x02B4 [0x27] REQ_SET(priority=0x04, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x31)
 95: 0x02BB [0x2B] Trion (ID: 17723394/0x010E7002) [12232*]:
    → "Wait, Curilla! Be not deceived! That is no father of yours!"
 96: 0x02C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 97: 0x02C3 [0x2A] GET_REQ_LEVEL(level=4, entity_id=Curilla (ID: 17723569/0x010E70B1))
 98: 0x02C9 [0x27] REQ_SET(priority=0x05, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x13)
 99: 0x02D0 [0x1C] WAIT(10* ticks)
100: 0x02D3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r005" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
101: 0x02E4 [0x27] REQ_SET(priority=0x04, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x32)
102: 0x02EB [0x2A] GET_REQ_LEVEL(level=5, entity_id=Curilla (ID: 17723569/0x010E70B1))
103: 0x02F1 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Trion (ID: 17723394/0x010E7002)
104: 0x02F7 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Ferdechiond (ID: 17723572/0x010E70B4)
105: 0x02FD [0x4E] SET_ENTITY_HIDE_FLAG: Hide Unnamed NPC (ID: 17723573/0x010E70B5)
106: 0x0303 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Unnamed NPC (ID: 17723574/0x010E70B6)
107: 0x0309 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Unnamed NPC (ID: 17723575/0x010E70B7)
108: 0x030F [0x4E] SET_ENTITY_HIDE_FLAG: Hide Unnamed NPC (ID: 17723576/0x010E70B8)
109: 0x0315 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Unnamed NPC (ID: 17723577/0x010E70B9)
110: 0x031B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r005" with entities [LocalPlayer, LocalPlayer], work=131*
111: 0x032A [0x4E] SET_ENTITY_HIDE_FLAG: Show Trion (ID: 17723394/0x010E7002)
112: 0x0330 [0x4E] SET_ENTITY_HIDE_FLAG: Show Ferdechiond (ID: 17723572/0x010E70B4)
113: 0x0336 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723573/0x010E70B5)
114: 0x033C [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723574/0x010E70B6)
115: 0x0342 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723575/0x010E70B7)
116: 0x0348 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723576/0x010E70B8)
117: 0x034E [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17723577/0x010E70B9)
118: 0x0354 [0x1C] WAIT(5* ticks)
119: 0x0357 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r006" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
120: 0x0368 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r006" with entities [LocalPlayer, LocalPlayer], work=131*
121: 0x0377 [0x2B] Trion (ID: 17723394/0x010E7002) [12233*]:
    → "Curilla!?"
122: 0x037E [0x23] WAIT_FOR_DIALOG_INTERACTION
123: 0x037F [0x1C] WAIT(90* ticks)
124: 0x0382 [0x4A] Curilla (ID: 17723569/0x010E70B1) looks at Trion (ID: 17723394/0x010E7002)
125: 0x038B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
126: 0x038C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Curilla (ID: 17723569/0x010E70B1) Render.Flags0 and Render.Flags3 conditions are met
127: 0x0391 [0x6B] STOP_AND_IDLE: Curilla (ID: 17723569/0x010E70B1) stops current action and resets to idle (animation="dft0")
128: 0x039A [0x1C] WAIT(60* ticks)
129: 0x039D [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x14)
130: 0x03A4 [0x27] REQ_SET(priority=0x04, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x15)
131: 0x03AB [0x1C] WAIT(15* ticks)
132: 0x03AE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r007" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
133: 0x03BF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r007" with entities [LocalPlayer, LocalPlayer], work=131*
134: 0x03CE [0x2A] GET_REQ_LEVEL(level=4, entity_id=Curilla (ID: 17723569/0x010E70B1))
135: 0x03D4 [0x79] Ferdechiond (ID: 17723572/0x010E70B4) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
136: 0x03DE [0x79] Unnamed NPC (ID: 17723573/0x010E70B5) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
137: 0x03E8 [0x79] Unnamed NPC (ID: 17723574/0x010E70B6) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
138: 0x03F2 [0x79] Unnamed NPC (ID: 17723575/0x010E70B7) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
139: 0x03FC [0x79] Unnamed NPC (ID: 17723576/0x010E70B8) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
140: 0x0406 [0x79] Unnamed NPC (ID: 17723577/0x010E70B9) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
141: 0x0410 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r019" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
142: 0x0421 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r019" with entities [LocalPlayer, LocalPlayer], work=131*
143: 0x0430 [0x2B] Trion (ID: 17723394/0x010E7002) [12234*]:
    → "Stop, Curilla!"
144: 0x0437 [0x23] WAIT_FOR_DIALOG_INTERACTION
145: 0x0438 [0x1C] WAIT(60* ticks)
146: 0x043B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r022" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
147: 0x044C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r022" with entities [LocalPlayer, LocalPlayer], work=131*
148: 0x045B [0x1C] WAIT(60* ticks)
149: 0x045E [0x2B] Ferdechiond (ID: 17723572/0x010E70B4) [12235*]:
    → "Prince Trion!"
150: 0x0465 [0x23] WAIT_FOR_DIALOG_INTERACTION
151: 0x0466 [0x27] REQ_SET(priority=0x03, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x27)
152: 0x046D [0x2B] Trion (ID: 17723394/0x010E7002) [12236*]:
    → "Knights, stand down!"
153: 0x0474 [0x23] WAIT_FOR_DIALOG_INTERACTION
154: 0x0475 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Trion (ID: 17723394/0x010E7002))
155: 0x047B [0x4A] Trion (ID: 17723394/0x010E7002) looks at Curilla (ID: 17723569/0x010E70B1)
156: 0x0484 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
157: 0x0485 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Trion (ID: 17723394/0x010E7002) Render.Flags0 and Render.Flags3 conditions are met
158: 0x048A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r008" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
159: 0x049B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r008" with entities [LocalPlayer, LocalPlayer], work=131*
160: 0x04AA [0x1C] WAIT(30* ticks)
161: 0x04AD [0x27] REQ_SET(priority=0x03, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x2D)
162: 0x04B4 [0x2B] Trion (ID: 17723394/0x010E7002) [12237*]:
    → "Curilla, drop your sword."
163: 0x04BB [0x23] WAIT_FOR_DIALOG_INTERACTION
164: 0x04BC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r009" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
165: 0x04CD [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r009" with entities [LocalPlayer, LocalPlayer], work=131*
166: 0x04DC [0x27] REQ_SET(priority=0x03, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x2E)
167: 0x04E3 [0x2B] Curilla (ID: 17723569/0x010E70B1) [12238*]:
    → "I will not be defeated..."
168: 0x04EA [0x23] WAIT_FOR_DIALOG_INTERACTION
169: 0x04EB [0x27] REQ_SET(priority=0x03, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x16)
170: 0x04F2 [0x1C] WAIT(30* ticks)
171: 0x04F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r025" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
172: 0x0506 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r025" with entities [LocalPlayer, LocalPlayer], work=131*
173: 0x0515 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Curilla (ID: 17723569/0x010E70B1))
174: 0x051B [0x1C] WAIT(60* ticks)
175: 0x051E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r026" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
176: 0x052F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r026" with entities [LocalPlayer, LocalPlayer], work=131*
177: 0x053E [0x2B] Trion (ID: 17723394/0x010E7002) [12239*]:
    → "Argh!"
178: 0x0545 [0x23] WAIT_FOR_DIALOG_INTERACTION
179: 0x0546 [0x27] REQ_SET(priority=0x03, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x17)
180: 0x054D [0x27] REQ_SET(priority=0x03, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x33)
181: 0x0554 [0x1C] WAIT(30* ticks)
182: 0x0557 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Curilla (ID: 17723569/0x010E70B1))
183: 0x055D [0x1C] WAIT(90* ticks)
184: 0x0560 [0x27] REQ_SET(priority=0x04, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x18)
185: 0x0567 [0x1C] WAIT(20* ticks)
186: 0x056A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r023" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
187: 0x057B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r023" with entities [LocalPlayer, LocalPlayer], work=131*
188: 0x058A [0x2B] Trion (ID: 17723394/0x010E7002) [12240*]:
    → "Curilla!"
189: 0x0591 [0x23] WAIT_FOR_DIALOG_INTERACTION
190: 0x0592 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r024" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
191: 0x05A3 [0x2B] Curilla (ID: 17723569/0x010E70B1) [12241*]:
    → "But I am not afraid of defeat."
192: 0x05AA [0x23] WAIT_FOR_DIALOG_INTERACTION
193: 0x05AB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r024" with entities [LocalPlayer, LocalPlayer], work=131*
194: 0x05BA [0x27] REQ_SET(priority=0x03, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x06)
195: 0x05C1 [0x1C] WAIT(30* ticks)
196: 0x05C4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r011" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
197: 0x05D5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r011" with entities [LocalPlayer, LocalPlayer], work=131*
198: 0x05E4 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Unnamed NPC (ID: 17723568/0x010E70B0), tag_num=0x02)
199: 0x05EB [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x07)
200: 0x05F2 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Unnamed NPC (ID: 17723568/0x010E70B0), tag_num=0x03)
201: 0x05F9 [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17723568/0x010E70B0), tag_num=0x04)
202: 0x0600 [0x1C] WAIT(30* ticks)
203: 0x0603 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r012" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
204: 0x0614 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r012" with entities [LocalPlayer, LocalPlayer], work=131*
205: 0x0623 [0x27] REQ_SET(priority=0x03, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x28)
206: 0x062A [0x2B] Trion (ID: 17723394/0x010E7002) [12242*]:
    → "Look out!"
207: 0x0631 [0x23] WAIT_FOR_DIALOG_INTERACTION
208: 0x0632 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r013" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
209: 0x0643 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r013" with entities [LocalPlayer, LocalPlayer], work=131*
210: 0x0652 [0x2A] GET_REQ_LEVEL(level=5, entity_id=Unnamed NPC (ID: 17723568/0x010E70B0))
211: 0x0658 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x08)
212: 0x065F [0x27] REQ_SET(priority=0x04, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x09)
213: 0x0666 [0x27] REQ_SET(priority=0x06, entity_id=Unnamed NPC (ID: 17723568/0x010E70B0), tag_num=0x05)
214: 0x066D [0x2B] ??? (ID: 17723445/0x010E7035) [12243*]:
    → "Ulp!"
215: 0x0674 [0x23] WAIT_FOR_DIALOG_INTERACTION
216: 0x0675 [0x79] Trion (ID: 17723394/0x010E7002) looks at Rainemard (ID: 17723567/0x010E70AF) (Basic look)
217: 0x067F [0x2A] GET_REQ_LEVEL(level=6, entity_id=Unnamed NPC (ID: 17723568/0x010E70B0))
218: 0x0685 [0x1C] WAIT(30* ticks)
219: 0x0688 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r014" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
220: 0x0699 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r014" with entities [LocalPlayer, LocalPlayer], work=131*
221: 0x06A8 [0x6C] FADE_ENTITY_COLOR(entity_id=Curilla (ID: 17723569/0x010E70B1), end_alpha=0*, fade_time=1*)
222: 0x06B1 [0x27] REQ_SET(priority=0x03, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x19)
223: 0x06B8 [0x2A] GET_REQ_LEVEL(level=4, entity_id=Rainemard (ID: 17723567/0x010E70AF))
224: 0x06BE [0x1C] WAIT(15* ticks)
225: 0x06C1 [0x79] Rainemard (ID: 17723567/0x010E70AF) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
226: 0x06CB [0x1C] WAIT(120* ticks)
227: 0x06CE [0x27] REQ_SET(priority=0x03, entity_id=Unnamed NPC (ID: 17723568/0x010E70B0), tag_num=0x06)
228: 0x06D5 [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12244*]:
    → "By a hair's breadth I made it in time. Curilla, forgive me for exposing you to this danger."
229: 0x06DC [0x23] WAIT_FOR_DIALOG_INTERACTION
230: 0x06DD [0x27] REQ_SET(priority=0x03, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x0A)
231: 0x06E4 [0x1C] WAIT(60* ticks)
232: 0x06E7 [0x6C] FADE_ENTITY_COLOR(entity_id=Curilla (ID: 17723569/0x010E70B1), end_alpha=128*, fade_time=1*)
233: 0x06F0 [0x4A] Curilla (ID: 17723569/0x010E70B1) looks at Rainemard (ID: 17723567/0x010E70AF)
234: 0x06F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r020" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
235: 0x070A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r020" with entities [LocalPlayer, LocalPlayer], work=131*
236: 0x0719 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Rainemard (ID: 17723567/0x010E70AF))
237: 0x071F [0x2B] Curilla (ID: 17723569/0x010E70B1) [12245*]:
    → "Father..."
238: 0x0726 [0x23] WAIT_FOR_DIALOG_INTERACTION
239: 0x0727 [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12246*]:
    → "A true warrior does not shrink from defeat. My only regret was not teaching that to you."
240: 0x072E [0x23] WAIT_FOR_DIALOG_INTERACTION
241: 0x072F [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12247*]:
    → "But it seems that you have already learned, Curilla. My, how you have grown!"
242: 0x0736 [0x23] WAIT_FOR_DIALOG_INTERACTION
243: 0x0737 [0x27] REQ_SET(priority=0x03, entity_id=LocalPlayer, tag_num=0x47)
244: 0x073E [0x1C] WAIT(30* ticks)
245: 0x0741 [0x27] REQ_SET(priority=0x03, entity_id=Trion (ID: 17723394/0x010E7002), tag_num=0x29)
246: 0x0748 [0x1C] WAIT(30* ticks)
247: 0x074B [0x4A] Rainemard (ID: 17723567/0x010E70AF) looks at Trion (ID: 17723394/0x010E7002)
248: 0x0754 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
249: 0x0755 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rainemard (ID: 17723567/0x010E70AF) Render.Flags0 and Render.Flags3 conditions are met
250: 0x075A [0x1C] WAIT(30* ticks)
251: 0x075D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r015" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
252: 0x076E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r015" with entities [LocalPlayer, LocalPlayer], work=131*
253: 0x077D [0x1C] WAIT(60* ticks)
254: 0x0780 [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12248*]:
    → "Watch over her, Prince."
255: 0x0787 [0x23] WAIT_FOR_DIALOG_INTERACTION
256: 0x0788 [0x7C] Trion (ID: 17723394/0x010E7002)->Render.Flags2 |= 0x00
257: 0x078E [0x2B] Trion (ID: 17723394/0x010E7002) [12249*]:
    → "You have my word."
258: 0x0795 [0x23] WAIT_FOR_DIALOG_INTERACTION
259: 0x0796 [0x7C] Trion (ID: 17723394/0x010E7002)->Render.Flags2 |= 0x01
260: 0x079C [0x2A] GET_REQ_LEVEL(level=3, entity_id=LocalPlayer)
261: 0x07A2 [0x4A] Rainemard (ID: 17723567/0x010E70AF) looks at LocalPlayer
262: 0x07AB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
263: 0x07AC [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rainemard (ID: 17723567/0x010E70AF) Render.Flags0 and Render.Flags3 conditions are met
264: 0x07B1 [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12250*]:
    → "Long have I troubled you. When I appeared here, a minion of the dark followed me. For that I am sorry."
265: 0x07B8 [0x23] WAIT_FOR_DIALOG_INTERACTION
266: 0x07B9 [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12251*]:
    → "This will not fully expiate my sins, but perhaps you may find some use for it. Please accept it."
267: 0x07C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
268: 0x07C1 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x0B)
269: 0x07C8 [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12252*]:
    → "And keep a watchful eye on this church. It is a pity I can say nothing more."
270: 0x07CF [0x23] WAIT_FOR_DIALOG_INTERACTION
271: 0x07D0 [0x1C] WAIT(60* ticks)
272: 0x07D3 [0x4A] Rainemard (ID: 17723567/0x010E70AF) looks at Curilla (ID: 17723569/0x010E70B1)
273: 0x07DC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
274: 0x07DD [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rainemard (ID: 17723567/0x010E70AF) Render.Flags0 and Render.Flags3 conditions are met
275: 0x07E2 [0x1C] WAIT(60* ticks)
276: 0x07E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r016" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
277: 0x07F6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r016" with entities [LocalPlayer, LocalPlayer], work=131*
278: 0x0805 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
279: 0x0806 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rainemard (ID: 17723567/0x010E70AF) Render.Flags0 and Render.Flags3 conditions are met
280: 0x080B [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12253*]:
    → "Curilla, I am relieved to see you standing tall. Though we shall never meet again, I want you to remember..."
281: 0x0812 [0x23] WAIT_FOR_DIALOG_INTERACTION
282: 0x0813 [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12254*]:
    → "You will always be my daughter. And I will always watch over you."
283: 0x081A [0x23] WAIT_FOR_DIALOG_INTERACTION
284: 0x081B [0x27] REQ_SET(priority=0x03, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x0B)
285: 0x0822 [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12255*]:
    → "I should return this watch. Carry it in memory of me."
286: 0x0829 [0x23] WAIT_FOR_DIALOG_INTERACTION
287: 0x082A [0x2A] GET_REQ_LEVEL(level=3, entity_id=Rainemard (ID: 17723567/0x010E70AF))
288: 0x0830 [0x1C] WAIT(30* ticks)
289: 0x0833 [0x2B] Rainemard (ID: 17723567/0x010E70AF) [12256*]:
    → "Now, I must go... Farewell, my daughter!"
290: 0x083A [0x23] WAIT_FOR_DIALOG_INTERACTION
291: 0x083B [0x1C] WAIT(60* ticks)
292: 0x083E [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x0D)
293: 0x0845 [0x27] REQ_SET(priority=0x04, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x0E)
294: 0x084C [0x1C] WAIT(90* ticks)
295: 0x084F [0x27] REQ_SET(priority=0x03, entity_id=Curilla (ID: 17723569/0x010E70B1), tag_num=0x1A)
296: 0x0856 [0x79] Trion (ID: 17723394/0x010E7002) looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
297: 0x0860 [0x79] LocalPlayer looks at Curilla (ID: 17723569/0x010E70B1) (Basic look)
298: 0x086A [0x1C] WAIT(30* ticks)
299: 0x086D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r017" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
300: 0x087E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r017" with entities [LocalPlayer, LocalPlayer], work=131*
301: 0x088D [0x2B] Curilla (ID: 17723569/0x010E70B1) [12257*]:
    → "Father!"
302: 0x0894 [0x23] WAIT_FOR_DIALOG_INTERACTION
303: 0x0895 [0x27] REQ_SET(priority=0x03, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x0F)
304: 0x089C [0x1C] WAIT(30* ticks)
305: 0x089F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r018" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
306: 0x08B0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r018" with entities [LocalPlayer, LocalPlayer], work=131*
307: 0x08BF [0x2A] GET_REQ_LEVEL(level=3, entity_id=Rainemard (ID: 17723567/0x010E70AF))
308: 0x08C5 [0x27] REQ_SET(priority=0x04, entity_id=Rainemard (ID: 17723567/0x010E70AF), tag_num=0x10)
309: 0x08CC [0x6C] FADE_ENTITY_COLOR(entity_id=Rainemard (ID: 17723567/0x010E70AF), end_alpha=0*, fade_time=180*)
310: 0x08D5 [0x1C] WAIT(120* ticks)
311: 0x08D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r017" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
312: 0x08E9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r017" with entities [LocalPlayer, LocalPlayer], work=131*
313: 0x08F8 [0x1C] WAIT(120* ticks)
314: 0x08FB [0x2F] Shamonde (ID: 17723408/0x010E7010)->Render.Flags0 &= ~0x80000 // Bit 19
315: 0x0901 [0x4E] SET_ENTITY_HIDE_FLAG: Show Shamonde (ID: 17723408/0x010E7010)
316: 0x0907 [0x2B] Curilla (ID: 17723569/0x010E70B1) [12258*]:
    → "I'll always be your daughter."
317: 0x090E [0x23] WAIT_FOR_DIALOG_INTERACTION
318: 0x090F [0x1C] WAIT(120* ticks)
319: 0x0912 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r021" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
320: 0x0923 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r021" with entities [LocalPlayer, LocalPlayer], work=131*
321: 0x0932 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Shamonde (ID: 17723408/0x010E7010), tag_num=0x14)
322: 0x0939 [0x27] REQ_SET(priority=0x04, entity_id=Shamonde (ID: 17723408/0x010E7010), tag_num=0x15)
323: 0x0940 [0x1C] WAIT(60* ticks)
324: 0x0943 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
325: 0x0954 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
326: 0x0963 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 107*
327: 0x0967 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 107*
328: 0x096B [0x46] CAMERA_CONTROL: Restore default settings
329: 0x096D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
330: 0x097E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
331: 0x098F [0x21] END_EVENT
332: 0x0990 [0x00] END_REQSTACK()
```

### Event 762

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0991  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0990:    00                                              .              
```

#### Opcodes

```
  0: 0x0991 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0992  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0990:       4C 00                                         L.            
```

#### Opcodes

```
  0: 0x0992 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0993 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0994  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0990:             4D 00                                     M.          
```

#### Opcodes

```
  0: 0x0994 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0995 [0x00] END_REQSTACK()
```
