# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Ruhotz Silvermines (ID: 93) |
| Block Size       | 1940 bytes                  |
| Total Events     | 7                           |
| References Count | 80                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10001](#event-10001)    | 0x0001       |     26 |              7 |
| [10000](#event-10000)    | 0x001B       |     54 |             10 |
| [4](#event-4)            | 0x0051       |   1456 |            166 |
| [65535.1](#event-655351) | 0x0601       |     22 |              6 |
| [65535.2](#event-655352) | 0x0617       |      7 |              3 |
| [65535.3](#event-655353) | 0x061E       |      7 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0001      |           1 |
|       4 | 0x005A      |          90 |
|       5 | 0x001B      |          27 |
|       6 | 0x48F9C     |      298908 |
|       7 | 0x3F948     |      260424 |
|       8 | 0x02B3      |         691 |
|       9 | 0x0809      |        2057 |
|      10 | 0x3A22D     |      238125 |
|      11 | 0x3FA85     |      260741 |
|      12 | 0x06D5      |        1749 |
|      13 | 0x0022      |          34 |
|      14 | 0x3ACD3     |      240851 |
|      15 | 0x3F454     |      259156 |
|      16 | 0x0EA3      |        3747 |
|      17 | 0x367B2     |      223154 |
|      18 | 0x3ED44     |      257348 |
|      19 | 0x041A      |        1050 |
|      20 | 0x36AEA     |      223978 |
|      21 | 0x3F2A7     |      258727 |
|      22 | 0x04D0      |        1232 |
|      23 | 0x373DA     |      226266 |
|      24 | 0x3F64F     |      259663 |
|      25 | 0x0331      |         817 |
|      26 | 0x0021      |          33 |
|      27 | 0x367FE     |      223230 |
|      28 | 0x3FCF2     |      261362 |
|      29 | 0x0460      |        1120 |
|      30 | 0x37A50     |      227920 |
|      31 | 0x42837     |      272439 |
|      32 | 0x034F      |         847 |
|      33 | 0x373F7     |      226295 |
|      34 | 0x44717     |      280343 |
|      35 | 0x0212      |         530 |
|      36 | 0x38886     |      231558 |
|      37 | 0x44A68     |      281192 |
|      38 | 0x03E7      |         999 |
|      39 | 0x3D2E3     |      250595 |
|      40 | 0x41AEC     |      269036 |
|      41 | 0xFFFFF10A  |  4294963466 |
|      42 | 0x3C1D0     |      246224 |
|      43 | 0x38D65     |      232805 |
|      44 | 0xFFFFFDA1  |  4294966689 |
|      45 | 0x0DB1      |        3505 |
|      46 | 0x04E8      |        1256 |
|      47 | 0x014D      |         333 |
|      48 | 0x000F      |          15 |
|      49 | 0x0078      |         120 |
|      50 | 0x001E      |          30 |
|      51 | 0x1D50      |        7504 |
|      52 | 0x1D51      |        7505 |
|      53 | 0x3D299     |      250521 |
|      54 | 0x3A5C4     |      239044 |
|      55 | 0x0015      |          21 |
|      56 | 0x0005      |           5 |
|      57 | 0x38891     |      231569 |
|      58 | 0x42522     |      271650 |
|      59 | 0x04B6      |        1206 |
|      60 | 0x3867E     |      231038 |
|      61 | 0x43B39     |      277305 |
|      62 | 0x0424      |        1060 |
|      63 | 0x3978B     |      235403 |
|      64 | 0x43BA3     |      277411 |
|      65 | 0x041E      |        1054 |
|      66 | 0x3D2C7     |      250567 |
|      67 | 0x40C41     |      265281 |
|      68 | 0x0205      |         517 |
|      69 | 0x3D6A5     |      251557 |
|      70 | 0x3C5F8     |      247288 |
|      71 | 0x03A6      |         934 |
|      72 | 0x00E3      |         227 |
|      73 | 0x00C9      |         201 |
|      74 | 0x1D52      |        7506 |
|      75 | 0x00B4      |         180 |
|      76 | 0x0028      |          40 |
|      77 | 0x3B5EB     |      243179 |
|      78 | 0x3F5D3     |      259539 |
|      79 | 0x066D      |        1645 |

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

### Event 10001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 45 00 80 F0  FF FF 7F F0 FF FF 7F 66    .BE..........f
0010: 64 6F 31 01 80 1C 02 80  30 21 00                 do1.....0!.     
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0015 [0x1C] WAIT(60* ticks)
  4: 0x0018 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x0019 [0x21] END_EVENT
  6: 0x001A [0x00] END_REQSTACK()
```

### Event 10000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 54 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   20 01 42 02 09              .B..
0020: 10 01 80 00 3A 00 62 03  80 F0 FF FF 7F F0 FF FF  ....:.b.........
0030: 7F 6D 61 69 6E 01 80 1C  04 80 45 00 80 F0 FF FF  .main.....E.....
0040: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 02 80 30 21  .....fdo1.....0!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x001B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x001D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x001E [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x003A
  3: 0x0026 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  4: 0x0037 [0x1C] WAIT(90* ticks)
  5: 0x003A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x004B [0x1C] WAIT(60* ticks)
  7: 0x004E [0x30] SET_UCOFF_CONTINUE_ZERO()
  8: 0x004F [0x21] END_EVENT
  9: 0x0050 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0051     |
| Data Size    | 1456 bytes |
| Instructions | 166        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    42 45 00 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F   BE..........fdo
0060: 31 01 80 55 00 80 F8 FF  FF 7F F8 FF FF 7F 66 64  1..U..........fd
0070: 6F 31 46 01 38 05 80 2F  00 F5 D0 05 01 4E 00 F5  o1F.8../.....N..
0080: D0 05 01 2F 00 F4 D0 05  01 4E 00 F4 D0 05 01 2F  .../.....N...../
0090: 00 F6 D0 05 01 2F 00 F7  D0 05 01 2F 00 F8 D0 05  ...../...../....
00A0: 01 2F 00 F9 D0 05 01 2F  00 FA D0 05 01 2F 00 FB  ./...../...../..
00B0: D0 05 01 2F 00 FC D0 05  01 2F 00 FD D0 05 01 2F  .../...../...../
00C0: 00 FE D0 05 01 92 01 F5  D0 05 01 92 01 F4 D0 05  ................
00D0: 01 BA F5 D0 05 01 06 80  07 80 08 80 09 80 BA F4  ................
00E0: D0 05 01 0A 80 0B 80 0C  80 0D 80 BA F0 FF FF 7F  ................
00F0: 0E 80 0F 80 0C 80 10 80  BA FA D0 05 01 11 80 12  ................
0100: 80 13 80 0D 80 BA F9 D0  05 01 14 80 15 80 16 80  ................
0110: 0D 80 BA F6 D0 05 01 17  80 18 80 19 80 1A 80 BA  ................
0120: F7 D0 05 01 1B 80 1C 80  1D 80 0D 80 BA F8 D0 05  ................
0130: 01 1E 80 1F 80 20 80 0D  80 BA FB D0 05 01 21 80  ..... ........!.
0140: 22 80 23 80 1A 80 BA FC  D0 05 01 24 80 25 80 26  ".#........$.%.&
0150: 80 0D 80 BA FD D0 05 01  27 80 28 80 29 80 10 80  ........'.(.)...
0160: BA FE D0 05 01 2A 80 2B  80 2C 80 2D 80 80 F5 D0  .....*.+.,.-....
0170: 05 01 80 F4 D0 05 01 4E  01 F0 FF FF 7F 5B 2E 80  .......N.....[..
0180: F5 D0 05 01 F5 D0 05 01  65 76 61 30 27 05 F4 D0  ........eva0'...
0190: 05 01 02 45 2F 80 F8 FF  FF 7F F8 FF FF 7F 73 31  ...E/.........s1
01A0: 35 35 01 80 1C 30 80 45  00 80 F8 FF FF 7F F8 FF  55...0.E........
01B0: FF 7F 66 64 69 31 01 80  1C 31 80 52 2F 80 F8 FF  ..fdi1...1.R/...
01C0: FF 7F F8 FF FF 7F 73 31  35 35 45 2F 80 F8 FF FF  ......s155E/....
01D0: 7F F8 FF FF 7F 73 31 35  36 01 80 2A 05 F4 D0 05  .....s156..*....
01E0: 01 55 2F 80 F8 FF FF 7F  F8 FF FF 7F 73 31 35 36  .U/.........s156
01F0: 1C 32 80 45 2F 80 F8 FF  FF 7F F8 FF FF 7F 73 31  .2.E/.........s1
0200: 35 37 01 80 2B F4 D0 05  01 33 80 23 4E 00 F0 FF  57..+....3.#N...
0210: FF 7F 80 F0 FF FF 7F 55  2F 80 F8 FF FF 7F F8 FF  .......U/.......
0220: FF 7F 73 31 35 37 45 2F  80 F8 FF FF 7F F8 FF FF  ..s157E/........
0230: 7F 73 31 35 38 01 80 29  05 F0 FF FF 7F 04 4A F4  .s158..)......J.
0240: D0 05 01 F0 FF FF 7F 2B  F4 D0 05 01 34 80 23 4E  .......+....4.#N
0250: 00 F6 D0 05 01 4E 00 F7  D0 05 01 4E 00 F8 D0 05  .....N.....N....
0260: 01 4E 00 F9 D0 05 01 4E  00 FA D0 05 01 4E 00 FB  .N.....N.....N..
0270: D0 05 01 4E 00 FC D0 05  01 4E 00 FD D0 05 01 4E  ...N.....N.....N
0280: 00 FE D0 05 01 80 F6 D0  05 01 80 F7 D0 05 01 80  ................
0290: F8 D0 05 01 80 F9 D0 05  01 80 FA D0 05 01 80 FB  ................
02A0: D0 05 01 80 FC D0 05 01  80 FD D0 05 01 80 FE D0  ................
02B0: 05 01 4A F8 D0 05 01 F0  FF FF 7F 4A FB D0 05 01  ..J........J....
02C0: F0 FF FF 7F 4A FC D0 05  01 F0 FF FF 7F 4A FD D0  ....J........J..
02D0: 05 01 F0 FF FF 7F 1C 02  80 52 2F 80 F8 FF FF 7F  .........R/.....
02E0: F8 FF FF 7F 73 31 35 38  45 2F 80 F8 FF FF 7F F8  ....s158E/......
02F0: FF FF 7F 73 31 39 38 01  80 4A F4 D0 05 01 FD D0  ...s198..J......
0300: 05 01 4A F0 FF FF 7F FD  D0 05 01 1C 02 80 52 2F  ..J...........R/
0310: 80 F8 FF FF 7F F8 FF FF  7F 73 31 39 38 45 2F 80  .........s198E/.
0320: F8 FF FF 7F F8 FF FF 7F  73 31 39 39 01 80 BA FE  ........s199....
0330: D0 05 01 35 80 36 80 26  80 0D 80 80 FE D0 05 01  ...5.6.&........
0340: 4A FE D0 05 01 F0 FF FF  7F 1C 02 80 52 2F 80 F8  J...........R/..
0350: FF FF 7F F8 FF FF 7F 73  31 39 39 45 2F 80 F8 FF  .......s199E/...
0360: FF 7F F8 FF FF 7F 73 31  39 37 01 80 6E F0 FF FF  ......s197..n...
0370: 7F 37 80 99 F0 FF FF 7F  1C 04 80 27 05 F6 D0 05  .7.........'....
0380: 01 02 1C 38 80 27 05 F7  D0 05 01 02 1C 38 80 27  ...8.'.......8.'
0390: 05 F9 D0 05 01 02 1C 38  80 27 05 FA D0 05 01 02  .......8.'......
03A0: 1C 32 80 52 2F 80 F8 FF  FF 7F F8 FF FF 7F 73 31  .2.R/.........s1
03B0: 39 37 45 2F 80 F8 FF FF  7F F8 FF FF 7F 73 31 35  97E/.........s15
03C0: 39 01 80 2A 05 F6 D0 05  01 2A 05 F7 D0 05 01 2A  9..*.....*.....*
03D0: 05 F9 D0 05 01 2A 05 FA  D0 05 01 4A F0 FF FF 7F  .....*.....J....
03E0: F6 D0 05 01 BA F8 D0 05  01 39 80 3A 80 3B 80 0D  .........9.:.;..
03F0: 80 BA FB D0 05 01 3C 80  3D 80 3E 80 1A 80 BA FC  ......<.=.>.....
0400: D0 05 01 3F 80 40 80 41  80 0D 80 BA FD D0 05 01  ...?.@.A........
0410: 42 80 43 80 44 80 0D 80  BA FE D0 05 01 45 80 46  B.C.D........E.F
0420: 80 47 80 0D 80 80 F8 D0  05 01 80 FB D0 05 01 80  .G..............
0430: FC D0 05 01 80 FD D0 05  01 80 FE D0 05 01 1C 32  ...............2
0440: 80 5B 48 80 FA D0 05 01  FA D0 05 01 65 76 62 30  .[H.........evb0
0450: 52 2F 80 F8 FF FF 7F F8  FF FF 7F 73 31 35 39 45  R/.........s159E
0460: 2F 80 F8 FF FF 7F F8 FF  FF 7F 73 31 36 31 01 80  /.........s161..
0470: 1C 32 80 5B 48 80 F9 D0  05 01 F9 D0 05 01 65 76  .2.[H.........ev
0480: 62 30 53 F9 D0 05 01 F9  D0 05 01 65 76 62 30 52  b0S........evb0R
0490: 2F 80 F8 FF FF 7F F8 FF  FF 7F 73 31 36 31 45 2F  /.........s161E/
04A0: 80 F8 FF FF 7F F8 FF FF  7F 73 31 36 32 01 80 6B  .........s162..k
04B0: 69 64 6C 30 F9 D0 05 01  6B 69 64 6C 30 FA D0 05  idl0....kidl0...
04C0: 01 5B 49 80 F4 D0 05 01  F4 D0 05 01 6B 61 6D 73  .[I.........kams
04D0: 2B F4 D0 05 01 4A 80 23  27 05 F0 FF FF 7F 05 53  +....J.#'......S
04E0: F4 D0 05 01 F4 D0 05 01  6B 61 6D 73 2A 05 F0 FF  ........kams*...
04F0: FF 7F 5B 48 80 F6 D0 05  01 F6 D0 05 01 65 76 61  ..[H.........eva
0500: 30 52 2F 80 F8 FF FF 7F  F8 FF FF 7F 73 31 36 32  0R/.........s162
0510: 45 2F 80 F8 FF FF 7F F8  FF FF 7F 73 31 36 30 01  E/.........s160.
0520: 80 45 2F 80 F8 FF FF 7F  F8 FF FF 7F 65 76 61 30  .E/.........eva0
0530: 01 80 1C 4B 80 52 2F 80  F8 FF FF 7F F8 FF FF 7F  ...K.R/.........
0540: 73 31 36 30 45 2F 80 F8  FF FF 7F F8 FF FF 7F 73  s160E/.........s
0550: 31 36 33 01 80 1C 31 80  52 2F 80 F8 FF FF 7F F8  163...1.R/......
0560: FF FF 7F 73 31 36 33 45  2F 80 F8 FF FF 7F F8 FF  ...s163E/.......
0570: FF 7F 73 32 30 30 01 80  27 05 FA D0 05 01 03 27  ..s200..'......'
0580: 05 FB D0 05 01 02 27 05  FC D0 05 01 02 27 05 FD  ......'......'..
0590: D0 05 01 02 27 05 FE D0  05 01 02 27 05 F7 D0 05  ....'......'....
05A0: 01 03 27 05 F8 D0 05 01  03 27 05 F9 D0 05 01 03  ..'......'......
05B0: 1C 02 80 45 00 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
05C0: 6F 30 01 80 55 00 80 F8  FF FF 7F F8 FF FF 7F 66  o0..U..........f
05D0: 64 6F 30 52 2F 80 F8 FF  FF 7F F8 FF FF 7F 73 32  do0R/.........s2
05E0: 30 30 27 05 F0 FF FF 7F  06 46 00 1C 02 80 45 00  00'......F....E.
05F0: 80 F8 FF FF 7F F8 FF FF  7F 66 64 69 31 01 80 21  .........fdi1..!
0600: 00                                                .               
```

#### Opcodes

```
  0: 0x0051 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0052 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0063 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
  3: 0x0072 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0074 [0x38] SET_CLIENT_EVENT_MODE(mode=27*)
  5: 0x0077 [0x2F] Unnamed NPC (ID: 17158389/0x0105D0F5)->Render.Flags0 &= ~0x80000 // Bit 19
  6: 0x007D [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158389/0x0105D0F5)
  7: 0x0083 [0x2F] Volker (ID: 17158388/0x0105D0F4)->Render.Flags0 &= ~0x80000 // Bit 19
  8: 0x0089 [0x4E] SET_ENTITY_HIDE_FLAG: Show Volker (ID: 17158388/0x0105D0F4)
  9: 0x008F [0x2F] Unnamed NPC (ID: 17158390/0x0105D0F6)->Render.Flags0 &= ~0x80000 // Bit 19
 10: 0x0095 [0x2F] Unnamed NPC (ID: 17158391/0x0105D0F7)->Render.Flags0 &= ~0x80000 // Bit 19
 11: 0x009B [0x2F] Unnamed NPC (ID: 17158392/0x0105D0F8)->Render.Flags0 &= ~0x80000 // Bit 19
 12: 0x00A1 [0x2F] Unnamed NPC (ID: 17158393/0x0105D0F9)->Render.Flags0 &= ~0x80000 // Bit 19
 13: 0x00A7 [0x2F] Unnamed NPC (ID: 17158394/0x0105D0FA)->Render.Flags0 &= ~0x80000 // Bit 19
 14: 0x00AD [0x2F] Unnamed NPC (ID: 17158395/0x0105D0FB)->Render.Flags0 &= ~0x80000 // Bit 19
 15: 0x00B3 [0x2F] Unnamed NPC (ID: 17158396/0x0105D0FC)->Render.Flags0 &= ~0x80000 // Bit 19
 16: 0x00B9 [0x2F] Unnamed NPC (ID: 17158397/0x0105D0FD)->Render.Flags0 &= ~0x80000 // Bit 19
 17: 0x00BF [0x2F] Unnamed NPC (ID: 17158398/0x0105D0FE)->Render.Flags0 &= ~0x80000 // Bit 19
 18: 0x00C5 [0x92] Unnamed NPC (ID: 17158389/0x0105D0F5)->Render.Flags3 ^= 0x01
 19: 0x00CB [0x92] Volker (ID: 17158388/0x0105D0F4)->Render.Flags3 ^= 0x01
 20: 0x00D1 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158389/0x0105D0F5), pos_x=298.908*, pos_z=260.424*, pos_y=0.691*, direction=180.8°*)
 21: 0x00DE [0xBA] SET_ENTITY_POSITION(entity_id=Volker (ID: 17158388/0x0105D0F4), pos_x=238.125*, pos_z=260.741*, pos_y=1.749*, direction=3.0°*)
 22: 0x00EB [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=240.851*, pos_z=259.156*, pos_y=1.749*, direction=329.3°*)
 23: 0x00F8 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158394/0x0105D0FA), pos_x=223.154*, pos_z=257.348*, pos_y=1.050*, direction=3.0°*)
 24: 0x0105 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158393/0x0105D0F9), pos_x=223.978*, pos_z=258.727*, pos_y=1.232*, direction=3.0°*)
 25: 0x0112 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158390/0x0105D0F6), pos_x=226.266*, pos_z=259.663*, pos_y=0.817*, direction=2.9°*)
 26: 0x011F [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158391/0x0105D0F7), pos_x=223.230*, pos_z=261.362*, pos_y=1.120*, direction=3.0°*)
 27: 0x012C [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158392/0x0105D0F8), pos_x=227.920*, pos_z=272.439*, pos_y=0.847*, direction=3.0°*)
 28: 0x0139 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158395/0x0105D0FB), pos_x=226.295*, pos_z=280.343*, pos_y=0.530*, direction=2.9°*)
 29: 0x0146 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158396/0x0105D0FC), pos_x=231.558*, pos_z=281.192*, pos_y=0.999*, direction=3.0°*)
 30: 0x0153 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158397/0x0105D0FD), pos_x=250.595*, pos_z=269.036*, pos_y=-3.830*, direction=329.3°*)
 31: 0x0160 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158398/0x0105D0FE), pos_x=246.224*, pos_z=232.805*, pos_y=-0.607*, direction=308.0°*)
 32: 0x016D [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158389/0x0105D0F5))
 33: 0x0172 [0x80] LOAD_WAIT(entity=Volker (ID: 17158388/0x0105D0F4))
 34: 0x0177 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
 35: 0x017D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "eva0" with entities [Unnamed NPC (ID: 17158389/0x0105D0F5), Unnamed NPC (ID: 17158389/0x0105D0F5)], work=1256*
 36: 0x018C [0x27] REQ_SET(priority=0x05, entity_id=Volker (ID: 17158388/0x0105D0F4), tag_num=0x02)
 37: 0x0193 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s155" with entities [EventEntity, EventEntity], work=[333*, 0*]
 38: 0x01A4 [0x1C] WAIT(15* ticks)
 39: 0x01A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 40: 0x01B8 [0x1C] WAIT(120* ticks)
 41: 0x01BB [0x52] END_LOAD_SCHEDULER: End scheduler "s155" with entities [EventEntity, EventEntity], work=333*
 42: 0x01CA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s156" with entities [EventEntity, EventEntity], work=[333*, 0*]
 43: 0x01DB [0x2A] GET_REQ_LEVEL(level=5, entity_id=Volker (ID: 17158388/0x0105D0F4))
 44: 0x01E1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s156" with entities [EventEntity, EventEntity], work=333*
 45: 0x01F0 [0x1C] WAIT(30* ticks)
 46: 0x01F3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s157" with entities [EventEntity, EventEntity], work=[333*, 0*]
 47: 0x0204 [0x2B] Volker (ID: 17158388/0x0105D0F4) [7504*]:
    → "Ambassador Dieuler!"
 48: 0x020B [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x020C [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 50: 0x0212 [0x80] LOAD_WAIT(entity=LocalPlayer)
 51: 0x0217 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s157" with entities [EventEntity, EventEntity], work=333*
 52: 0x0226 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s158" with entities [EventEntity, EventEntity], work=[333*, 0*]
 53: 0x0237 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=LocalPlayer, tag_num=0x04)
 54: 0x023E [0x4A] Volker (ID: 17158388/0x0105D0F4) looks at LocalPlayer
 55: 0x0247 [0x2B] Volker (ID: 17158388/0x0105D0F4) [7505*]:
    → "Where did you come from...?"
 56: 0x024E [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x024F [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158390/0x0105D0F6)
 58: 0x0255 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158391/0x0105D0F7)
 59: 0x025B [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158392/0x0105D0F8)
 60: 0x0261 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158393/0x0105D0F9)
 61: 0x0267 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158394/0x0105D0FA)
 62: 0x026D [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158395/0x0105D0FB)
 63: 0x0273 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158396/0x0105D0FC)
 64: 0x0279 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158397/0x0105D0FD)
 65: 0x027F [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17158398/0x0105D0FE)
 66: 0x0285 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158390/0x0105D0F6))
 67: 0x028A [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158391/0x0105D0F7))
 68: 0x028F [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158392/0x0105D0F8))
 69: 0x0294 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158393/0x0105D0F9))
 70: 0x0299 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158394/0x0105D0FA))
 71: 0x029E [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158395/0x0105D0FB))
 72: 0x02A3 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158396/0x0105D0FC))
 73: 0x02A8 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158397/0x0105D0FD))
 74: 0x02AD [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158398/0x0105D0FE))
 75: 0x02B2 [0x4A] Unnamed NPC (ID: 17158392/0x0105D0F8) looks at LocalPlayer
 76: 0x02BB [0x4A] Unnamed NPC (ID: 17158395/0x0105D0FB) looks at LocalPlayer
 77: 0x02C4 [0x4A] Unnamed NPC (ID: 17158396/0x0105D0FC) looks at LocalPlayer
 78: 0x02CD [0x4A] Unnamed NPC (ID: 17158397/0x0105D0FD) looks at LocalPlayer
 79: 0x02D6 [0x1C] WAIT(60* ticks)
 80: 0x02D9 [0x52] END_LOAD_SCHEDULER: End scheduler "s158" with entities [EventEntity, EventEntity], work=333*
 81: 0x02E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s198" with entities [EventEntity, EventEntity], work=[333*, 0*]
 82: 0x02F9 [0x4A] Volker (ID: 17158388/0x0105D0F4) looks at Unnamed NPC (ID: 17158397/0x0105D0FD)
 83: 0x0302 [0x4A] LocalPlayer looks at Unnamed NPC (ID: 17158397/0x0105D0FD)
 84: 0x030B [0x1C] WAIT(60* ticks)
 85: 0x030E [0x52] END_LOAD_SCHEDULER: End scheduler "s198" with entities [EventEntity, EventEntity], work=333*
 86: 0x031D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s199" with entities [EventEntity, EventEntity], work=[333*, 0*]
 87: 0x032E [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158398/0x0105D0FE), pos_x=250.521*, pos_z=239.044*, pos_y=0.999*, direction=3.0°*)
 88: 0x033B [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158398/0x0105D0FE))
 89: 0x0340 [0x4A] Unnamed NPC (ID: 17158398/0x0105D0FE) looks at LocalPlayer
 90: 0x0349 [0x1C] WAIT(60* ticks)
 91: 0x034C [0x52] END_LOAD_SCHEDULER: End scheduler "s199" with entities [EventEntity, EventEntity], work=333*
 92: 0x035B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s197" with entities [EventEntity, EventEntity], work=[333*, 0*]
 93: 0x036C [0x6E] LocalPlayer uses emote 21*
 94: 0x0373 [0x99] Wait for LocalPlayer animation to complete
 95: 0x0378 [0x1C] WAIT(90* ticks)
 96: 0x037B [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158390/0x0105D0F6), tag_num=0x02)
 97: 0x0382 [0x1C] WAIT(5* ticks)
 98: 0x0385 [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158391/0x0105D0F7), tag_num=0x02)
 99: 0x038C [0x1C] WAIT(5* ticks)
100: 0x038F [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158393/0x0105D0F9), tag_num=0x02)
101: 0x0396 [0x1C] WAIT(5* ticks)
102: 0x0399 [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158394/0x0105D0FA), tag_num=0x02)
103: 0x03A0 [0x1C] WAIT(30* ticks)
104: 0x03A3 [0x52] END_LOAD_SCHEDULER: End scheduler "s197" with entities [EventEntity, EventEntity], work=333*
105: 0x03B2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s159" with entities [EventEntity, EventEntity], work=[333*, 0*]
106: 0x03C3 [0x2A] GET_REQ_LEVEL(level=5, entity_id=Unnamed NPC (ID: 17158390/0x0105D0F6))
107: 0x03C9 [0x2A] GET_REQ_LEVEL(level=5, entity_id=Unnamed NPC (ID: 17158391/0x0105D0F7))
108: 0x03CF [0x2A] GET_REQ_LEVEL(level=5, entity_id=Unnamed NPC (ID: 17158393/0x0105D0F9))
109: 0x03D5 [0x2A] GET_REQ_LEVEL(level=5, entity_id=Unnamed NPC (ID: 17158394/0x0105D0FA))
110: 0x03DB [0x4A] LocalPlayer looks at Unnamed NPC (ID: 17158390/0x0105D0F6)
111: 0x03E4 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158392/0x0105D0F8), pos_x=231.569*, pos_z=271.650*, pos_y=1.206*, direction=3.0°*)
112: 0x03F1 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158395/0x0105D0FB), pos_x=231.038*, pos_z=277.305*, pos_y=1.060*, direction=2.9°*)
113: 0x03FE [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158396/0x0105D0FC), pos_x=235.403*, pos_z=277.411*, pos_y=1.054*, direction=3.0°*)
114: 0x040B [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158397/0x0105D0FD), pos_x=250.567*, pos_z=265.281*, pos_y=0.517*, direction=3.0°*)
115: 0x0418 [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17158398/0x0105D0FE), pos_x=251.557*, pos_z=247.288*, pos_y=0.934*, direction=3.0°*)
116: 0x0425 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158392/0x0105D0F8))
117: 0x042A [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158395/0x0105D0FB))
118: 0x042F [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158396/0x0105D0FC))
119: 0x0434 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158397/0x0105D0FD))
120: 0x0439 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17158398/0x0105D0FE))
121: 0x043E [0x1C] WAIT(30* ticks)
122: 0x0441 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "evb0" with entities [Unnamed NPC (ID: 17158394/0x0105D0FA), Unnamed NPC (ID: 17158394/0x0105D0FA)], work=227*
123: 0x0450 [0x52] END_LOAD_SCHEDULER: End scheduler "s159" with entities [EventEntity, EventEntity], work=333*
124: 0x045F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s161" with entities [EventEntity, EventEntity], work=[333*, 0*]
125: 0x0470 [0x1C] WAIT(30* ticks)
126: 0x0473 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "evb0" with entities [Unnamed NPC (ID: 17158393/0x0105D0F9), Unnamed NPC (ID: 17158393/0x0105D0F9)], work=227*
127: 0x0482 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "evb0" with entities [Unnamed NPC (ID: 17158393/0x0105D0F9), Unnamed NPC (ID: 17158393/0x0105D0F9)]
128: 0x048F [0x52] END_LOAD_SCHEDULER: End scheduler "s161" with entities [EventEntity, EventEntity], work=333*
129: 0x049E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s162" with entities [EventEntity, EventEntity], work=[333*, 0*]
130: 0x04AF [0x6B] STOP_AND_IDLE: Unnamed NPC (ID: 17158393/0x0105D0F9) stops current action and resets to idle (animation="idl0")
131: 0x04B8 [0x6B] STOP_AND_IDLE: Unnamed NPC (ID: 17158394/0x0105D0FA) stops current action and resets to idle (animation="idl0")
132: 0x04C1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kams" with entities [Volker (ID: 17158388/0x0105D0F4), Volker (ID: 17158388/0x0105D0F4)], work=201*
133: 0x04D0 [0x2B] Volker (ID: 17158388/0x0105D0F4) [7506*]:
    → "Explanations will have to wait. To arms!"
134: 0x04D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
135: 0x04D8 [0x27] REQ_SET(priority=0x05, entity_id=LocalPlayer, tag_num=0x05)
136: 0x04DF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kams" with entities [Volker (ID: 17158388/0x0105D0F4), Volker (ID: 17158388/0x0105D0F4)]
137: 0x04EC [0x2A] GET_REQ_LEVEL(level=5, entity_id=LocalPlayer)
138: 0x04F2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "eva0" with entities [Unnamed NPC (ID: 17158390/0x0105D0F6), Unnamed NPC (ID: 17158390/0x0105D0F6)], work=227*
139: 0x0501 [0x52] END_LOAD_SCHEDULER: End scheduler "s162" with entities [EventEntity, EventEntity], work=333*
140: 0x0510 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s160" with entities [EventEntity, EventEntity], work=[333*, 0*]
141: 0x0521 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "eva0" with entities [EventEntity, EventEntity], work=[333*, 0*]
142: 0x0532 [0x1C] WAIT(180* ticks)
143: 0x0535 [0x52] END_LOAD_SCHEDULER: End scheduler "s160" with entities [EventEntity, EventEntity], work=333*
144: 0x0544 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s163" with entities [EventEntity, EventEntity], work=[333*, 0*]
145: 0x0555 [0x1C] WAIT(120* ticks)
146: 0x0558 [0x52] END_LOAD_SCHEDULER: End scheduler "s163" with entities [EventEntity, EventEntity], work=333*
147: 0x0567 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s200" with entities [EventEntity, EventEntity], work=[333*, 0*]
148: 0x0578 [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158394/0x0105D0FA), tag_num=0x03)
149: 0x057F [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158395/0x0105D0FB), tag_num=0x02)
150: 0x0586 [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158396/0x0105D0FC), tag_num=0x02)
151: 0x058D [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158397/0x0105D0FD), tag_num=0x02)
152: 0x0594 [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158398/0x0105D0FE), tag_num=0x02)
153: 0x059B [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158391/0x0105D0F7), tag_num=0x03)
154: 0x05A2 [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158392/0x0105D0F8), tag_num=0x03)
155: 0x05A9 [0x27] REQ_SET(priority=0x05, entity_id=Unnamed NPC (ID: 17158393/0x0105D0F9), tag_num=0x03)
156: 0x05B0 [0x1C] WAIT(60* ticks)
157: 0x05B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
158: 0x05C4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
159: 0x05D3 [0x52] END_LOAD_SCHEDULER: End scheduler "s200" with entities [EventEntity, EventEntity], work=333*
160: 0x05E2 [0x27] REQ_SET(priority=0x05, entity_id=LocalPlayer, tag_num=0x06)
161: 0x05E9 [0x46] CAMERA_CONTROL: Restore default settings
162: 0x05EB [0x1C] WAIT(60* ticks)
163: 0x05EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
164: 0x05FF [0x21] END_EVENT
165: 0x0600 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0601   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0600:    32 4C 80 1F 00 4D 80  4E 80 4F 80 1F 01 1E F4   2L...M.N.O.....
0610: D0 05 01 1C 32 80 00                              ....2..         
```

#### Opcodes

```
  0: 0x0601 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0604 [0x1F] MOVE_ENTITY: EventEntity moves to X=243.179*, Z=259.539*, Y=1.645*
  2: 0x060C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x060E [0x1E] EventEntity looks at Volker (ID: 17158388/0x0105D0F4) and starts talking
  4: 0x0613 [0x1C] WAIT(30* ticks)
  5: 0x0616 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0617  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0610:                      AB  03 AC 01 03 80 00               .......  
```

#### Opcodes

```
  0: 0x0617 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0619 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x061D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x061E  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0610:                                            AC 01                ..
0620: 01 80 AB 04 00                                    .....           
```

#### Opcodes

```
  0: 0x061E [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0622 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0624 [0x00] END_REQSTACK()
```
