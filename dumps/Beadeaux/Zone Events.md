# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Beadeaux (ID: 147) |
| Block Size       | 1224 bytes         |
| Total Events     | 7                  |
| References Count | 52                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [120](#event-120)        | 0x0001       |    326 |             49 |
| [121](#event-121)        | 0x0147       |    238 |             35 |
| [122](#event-122)        | 0x0235       |    380 |             51 |
| [65534](#event-65534)    | 0x03B1       |      1 |              1 |
| [65535.1](#event-655351) | 0x03B2       |      1 |              1 |
| [65535.2](#event-655352) | 0x03B3       |     23 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFA9160  |  4294611296 |
|       1 | 0xDEA8      |       57000 |
|       2 | 0x03E7      |         999 |
|       3 | 0x0ED8      |        3800 |
|       4 | 0x00C8      |         200 |
|       5 | 0x0000      |           0 |
|       6 | 0x002F      |          47 |
|       7 | 0x00D2      |         210 |
|       8 | 0x002D      |          45 |
|       9 | 0x1CBE      |        7358 |
|      10 | 0x1CBF      |        7359 |
|      11 | 0x0013      |          19 |
|      12 | 0x1CC0      |        7360 |
|      13 | 0x1CC1      |        7361 |
|      14 | 0x1CC2      |        7362 |
|      15 | 0x005A      |          90 |
|      16 | 0x1CC3      |        7363 |
|      17 | 0x003C      |          60 |
|      18 | 0x0064      |         100 |
|      19 | 0x001E      |          30 |
|      20 | 0xFFFBA053  |  4294680659 |
|      21 | 0x17EEB     |       98027 |
|      22 | 0x0471      |        1137 |
|      23 | 0x0FC0      |        4032 |
|      24 | 0x0078      |         120 |
|      25 | 0x1CC4      |        7364 |
|      26 | 0x000D      |          13 |
|      27 | 0xFFFB9859  |  4294678617 |
|      28 | 0x17994     |       96660 |
|      29 | 0x0527      |        1319 |
|      30 | 0x0178      |         376 |
|      31 | 0x1CC5      |        7365 |
|      32 | 0x1CC6      |        7366 |
|      33 | 0x1CC7      |        7367 |
|      34 | 0x00C9      |         201 |
|      35 | 0x1CDF      |        7391 |
|      36 | 0x1CE0      |        7392 |
|      37 | 0x1CE1      |        7393 |
|      38 | 0x1CE2      |        7394 |
|      39 | 0x1CE3      |        7395 |
|      40 | 0x1CE4      |        7396 |
|      41 | 0x1CE5      |        7397 |
|      42 | 0x07A2      |        1954 |
|      43 | 0x1CE6      |        7398 |
|      44 | 0xD7F1      |       55281 |
|      45 | 0xFFFF9E71  |  4294942321 |
|      46 | 0x0350      |         848 |
|      47 | 0x05B9      |        1465 |
|      48 | 0x0028      |          40 |
|      49 | 0xAA41      |       43585 |
|      50 | 0xFFFF7277  |  4294931063 |
|      51 | 0x0D24      |        3364 |

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

### Event 120

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 326 bytes |
| Instructions | 49        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 42 46 01 37 00  80 01 80 02 80 03 80 45   ".BF.7........E
0010: 04 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 05 80  ..........fdi1..
0020: 45 06 80 F0 FF FF 7F F0  FF FF 7F 73 30 30 30 05  E..........s000.
0030: 80 1C 07 80 27 0A D4 31  09 01 02 55 06 80 F0 FF  ....'..1...U....
0040: FF 7F F0 FF FF 7F 73 30  30 30 1C 08 80 29 0A D5  ......s000...)..
0050: 31 09 01 02 2B D5 31 09  01 09 80 23 4A D4 31 09  1...+.1....#J.1.
0060: 01 F0 FF FF 7F 2B D5 31  09 01 0A 80 23 66 0B 80  .....+.1....#f..
0070: D5 31 09 01 D5 31 09 01  74 6C 6B 30 2B D5 31 09  .1...1..tlk0+.1.
0080: 01 0C 80 23 2B D5 31 09  01 0D 80 23 6B 69 64 6C  ...#+.1....#kidl
0090: 30 D5 31 09 01 27 0A D4  31 09 01 03 2B D4 31 09  0.1..'..1...+.1.
00A0: 01 0E 80 23 1C 0F 80 4A  D5 31 09 01 D7 31 09 01  ...#...J.1...1..
00B0: 79 00 D5 31 09 01 D7 31  09 01 79 00 D6 31 09 01  y..1...1..y..1..
00C0: D5 31 09 01 79 00 F0 FF  FF 7F D5 31 09 01 79 00  .1..y......1..y.
00D0: D7 31 09 01 D5 31 09 01  2B D5 31 09 01 10 80 23  .1...1..+.1....#
00E0: 7B D5 31 09 01 7B D6 31  09 01 7B F0 FF FF 7F 7B  {.1..{.1..{....{
00F0: D7 31 09 01 27 0A D7 31  09 01 02 1C 11 80 27 0A  .1..'..1......'.
0100: D6 31 09 01 02 1C 12 80  27 0A D5 31 09 01 03 45  .1......'..1...E
0110: 04 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 05 80  ..........fdo1..
0120: 55 04 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 46  U..........fdo1F
0130: 00 1C 13 80 45 04 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0140: 64 69 31 05 80 21 00                              di1..!.         
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0006 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-356.000*, z=57.000*, y=0.999*, direction=334.0°*
  4: 0x000F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x0020 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=[47*, 0*]
  6: 0x0031 [0x1C] WAIT(210* ticks)
  7: 0x0034 [0x27] REQ_SET(priority=0x0A, entity_id=Naji (ID: 17379796/0x010931D4), tag_num=0x02)
  8: 0x003B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=47*
  9: 0x004A [0x1C] WAIT(45* ticks)
 10: 0x004D [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Ayame (ID: 17379797/0x010931D5), tag_num=0x02)
 11: 0x0054 [0x2B] Ayame (ID: 17379797/0x010931D5) [7358*]:
    → "Is everyone here, then? We are in Beadeaux, near the Quadav stronghold."
 12: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x005C [0x4A] Naji (ID: 17379796/0x010931D4) looks at LocalPlayer
 14: 0x0065 [0x2B] Ayame (ID: 17379797/0x010931D5) [7359*]:
    → "Our mission targets are the Copper Quadav, and only the Copper Quadav. We must eliminate twenty of them each, then retreat and regroup at the rendezvous point."
 15: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x006D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Ayame (ID: 17379797/0x010931D5), Ayame (ID: 17379797/0x010931D5)], work=19*
 17: 0x007C [0x2B] Ayame (ID: 17379797/0x010931D5) [7360*]:
    → "We will disperse and attack from different sides to prevent the enemy from setting up an effective defense."
 18: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0084 [0x2B] Ayame (ID: 17379797/0x010931D5) [7361*]:
    → "As soon as you've achieved your mission goals, disengage and regroup in the Pashhow Marshlands, in the area just beyond this exit."
 20: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x008C [0x6B] STOP_AND_IDLE: Ayame (ID: 17379797/0x010931D5) stops current action and resets to idle (animation="idl0")
 22: 0x0095 [0x27] REQ_SET(priority=0x0A, entity_id=Naji (ID: 17379796/0x010931D4), tag_num=0x03)
 23: 0x009C [0x2B] Naji (ID: 17379796/0x010931D4) [7362*]:
    → "All right! Come and get me, Coppers!"
 24: 0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x00A4 [0x1C] WAIT(90* ticks)
 26: 0x00A7 [0x4A] Ayame (ID: 17379797/0x010931D5) looks at Dalzakk (ID: 17379799/0x010931D7)
 27: 0x00B0 [0x79] Ayame (ID: 17379797/0x010931D5) looks at Dalzakk (ID: 17379799/0x010931D7) (Basic look)
 28: 0x00BA [0x79] Hani (ID: 17379798/0x010931D6) looks at Ayame (ID: 17379797/0x010931D5) (Basic look)
 29: 0x00C4 [0x79] LocalPlayer looks at Ayame (ID: 17379797/0x010931D5) (Basic look)
 30: 0x00CE [0x79] Dalzakk (ID: 17379799/0x010931D7) looks at Ayame (ID: 17379797/0x010931D5) (Basic look)
 31: 0x00D8 [0x2B] Ayame (ID: 17379797/0x010931D5) [7363*]:
    → "Do not follow his example, please... Let us begin. Good hunting!"
 32: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x00E0 [0x7B] Ayame (ID: 17379797/0x010931D5) stops talking
 34: 0x00E5 [0x7B] Hani (ID: 17379798/0x010931D6) stops talking
 35: 0x00EA [0x7B] LocalPlayer stops talking
 36: 0x00EF [0x7B] Dalzakk (ID: 17379799/0x010931D7) stops talking
 37: 0x00F4 [0x27] REQ_SET(priority=0x0A, entity_id=Dalzakk (ID: 17379799/0x010931D7), tag_num=0x02)
 38: 0x00FB [0x1C] WAIT(60* ticks)
 39: 0x00FE [0x27] REQ_SET(priority=0x0A, entity_id=Hani (ID: 17379798/0x010931D6), tag_num=0x02)
 40: 0x0105 [0x1C] WAIT(100* ticks)
 41: 0x0108 [0x27] REQ_SET(priority=0x0A, entity_id=Ayame (ID: 17379797/0x010931D5), tag_num=0x03)
 42: 0x010F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x0120 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 44: 0x012F [0x46] CAMERA_CONTROL: Restore default settings
 45: 0x0131 [0x1C] WAIT(30* ticks)
 46: 0x0134 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 47: 0x0145 [0x21] END_EVENT
 48: 0x0146 [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0147    |
| Data Size    | 238 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                      22  00 42 46 01 37 14 80 15         ".BF.7...
0150: 80 16 80 17 80 45 04 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0160: 66 64 69 31 05 80 45 06  80 F0 FF FF 7F F0 FF FF  fdi1..E.........
0170: 7F 73 30 30 31 05 80 1C  11 80 27 0A D8 31 09 01  .s001.....'..1..
0180: 02 1C 18 80 2B D8 31 09  01 19 80 23 1E D8 31 09  ....+.1....#..1.
0190: 01 1C 11 80 55 06 80 F0  FF FF 7F F0 FF FF 7F 73  ....U..........s
01A0: 30 30 31 32 1A 80 1F 00  1B 80 1C 80 1D 80 1F 01  0012............
01B0: 45 06 80 F0 FF FF 7F F0  FF FF 7F 73 30 30 32 05  E..........s002.
01C0: 80 5B 1E 80 D8 31 09 01  D8 31 09 01 74 6C 6B 30  .[...1...1..tlk0
01D0: 2B D8 31 09 01 1F 80 23  2B D8 31 09 01 20 80 23  +.1....#+.1.. .#
01E0: 6B 69 64 6C 30 D8 31 09  01 2B D8 31 09 01 21 80  kidl0.1..+.1..!.
01F0: 23 27 0A D8 31 09 01 03  1C 11 80 45 04 80 F0 FF  #'..1......E....
0200: FF 7F F0 FF FF 7F 66 64  6F 31 05 80 1C 11 80 46  ......fdo1.....F
0210: 00 45 04 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
0220: 05 80 45 22 80 F0 FF FF  7F F0 FF FF 7F 71 73 74  ..E".........qst
0230: 63 05 80 21 00                                    c..!.           
```

#### Opcodes

```
  0: 0x0147 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0149 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x014A [0x46] CAMERA_CONTROL: Disable user control
  3: 0x014C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-286.637*, z=98.027*, y=1.137*, direction=354.4°*
  4: 0x0155 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x0166 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=[47*, 0*]
  6: 0x0177 [0x1C] WAIT(60* ticks)
  7: 0x017A [0x27] REQ_SET(priority=0x0A, entity_id=Zeid (ID: 17379800/0x010931D8), tag_num=0x02)
  8: 0x0181 [0x1C] WAIT(120* ticks)
  9: 0x0184 [0x2B] Zeid (ID: 17379800/0x010931D8) [7364*]:
    → "I see you have learned to bear the weight of that blade--it is the weight of the lives you have taken with it."
 10: 0x018B [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x018C [0x1E] EventEntity looks at Zeid (ID: 17379800/0x010931D8) and starts talking
 12: 0x0191 [0x1C] WAIT(60* ticks)
 13: 0x0194 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=47*
 14: 0x01A3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
 15: 0x01A6 [0x1F] MOVE_ENTITY: EventEntity moves to X=-288.679*, Z=96.660*, Y=1.319*
 16: 0x01AE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 17: 0x01B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s002" with entities [LocalPlayer, LocalPlayer], work=[47*, 0*]
 18: 0x01C1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Zeid (ID: 17379800/0x010931D8), Zeid (ID: 17379800/0x010931D8)], work=376*
 19: 0x01D0 [0x2B] Zeid (ID: 17379800/0x010931D8) [7365*]:
    → "It is up to you to choose whether or not you will walk down the bloody path of the dark knight. But it might be wise to confront your past, first, before you make your decision..."
 20: 0x01D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x01D8 [0x2B] Zeid (ID: 17379800/0x010931D8) [7366*]:
    → "Your training to become a dark knight is already complete..."
 22: 0x01DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x01E0 [0x6B] STOP_AND_IDLE: Zeid (ID: 17379800/0x010931D8) stops current action and resets to idle (animation="idl0")
 24: 0x01E9 [0x2B] Zeid (ID: 17379800/0x010931D8) [7367*]:
    → "As long as your blade craves for the souls of your enemies, our paths may cross again. Until then, farewell."
 25: 0x01F0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x01F1 [0x27] REQ_SET(priority=0x0A, entity_id=Zeid (ID: 17379800/0x010931D8), tag_num=0x03)
 27: 0x01F8 [0x1C] WAIT(60* ticks)
 28: 0x01FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x020C [0x1C] WAIT(60* ticks)
 30: 0x020F [0x46] CAMERA_CONTROL: Restore default settings
 31: 0x0211 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x0222 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 33: 0x0233 [0x21] END_EVENT
 34: 0x0234 [0x00] END_REQSTACK()
```

### Event 122

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0235    |
| Data Size    | 380 bytes |
| Instructions | 51        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                22 00 42  46 01 37 14 80 15 80 16       ".BF.7.....
0240: 80 17 80 45 04 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0250: 69 31 05 80 45 06 80 F0  FF FF 7F F0 FF FF 7F 73  i1..E..........s
0260: 30 30 31 05 80 1C 11 80  27 0A D8 31 09 01 02 1C  001.....'..1....
0270: 18 80 2B D8 31 09 01 23  80 23 1E D8 31 09 01 1C  ..+.1..#.#..1...
0280: 11 80 52 06 80 F0 FF FF  7F F0 FF FF 7F 73 30 30  ..R..........s00
0290: 31 32 1A 80 1F 00 1B 80  1C 80 1D 80 1F 01 45 06  12............E.
02A0: 80 F0 FF FF 7F F0 FF FF  7F 73 30 30 32 05 80 5B  .........s002..[
02B0: 1E 80 D8 31 09 01 D8 31  09 01 74 6C 6B 30 2B D8  ...1...1..tlk0+.
02C0: 31 09 01 24 80 23 52 06  80 F0 FF FF 7F F0 FF FF  1..$.#R.........
02D0: 7F 73 30 30 32 45 06 80  F0 FF FF 7F F0 FF FF 7F  .s002E..........
02E0: 73 30 30 33 05 80 2B D8  31 09 01 25 80 23 6B 69  s003..+.1..%.#ki
02F0: 64 6C 30 D8 31 09 01 2B  D8 31 09 01 26 80 23 52  dl0.1..+.1..&.#R
0300: 06 80 F0 FF FF 7F F0 FF  FF 7F 73 30 30 33 45 06  ..........s003E.
0310: 80 F0 FF FF 7F F0 FF FF  7F 73 30 30 34 05 80 2B  .........s004..+
0320: D8 31 09 01 27 80 23 5B  1E 80 D8 31 09 01 D8 31  .1..'.#[...1...1
0330: 09 01 74 6C 6B 30 2B D8  31 09 01 28 80 23 6B 69  ..tlk0+.1..(.#ki
0340: 64 6C 30 D8 31 09 01 2B  D8 31 09 01 29 80 23 4B  dl0.1..+.1..).#K
0350: D8 31 09 01 2A 80 52 06  80 F0 FF FF 7F F0 FF FF  .1..*.R.........
0360: 7F 73 30 30 34 45 06 80  F0 FF FF 7F F0 FF FF 7F  .s004E..........
0370: 73 30 30 35 05 80 2B D8  31 09 01 2B 80 23 27 0A  s005..+.1..+.#'.
0380: D8 31 09 01 03 1C 11 80  45 04 80 F0 FF FF 7F F0  .1......E.......
0390: FF FF 7F 66 64 6F 31 05  80 1C 11 80 46 00 45 04  ...fdo1.....F.E.
03A0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 32 05 80 21  .........fdi2..!
03B0: 00                                                .               
```

#### Opcodes

```
  0: 0x0235 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0237 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0238 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x023A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-286.637*, z=98.027*, y=1.137*, direction=354.4°*
  4: 0x0243 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x0254 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=[47*, 0*]
  6: 0x0265 [0x1C] WAIT(60* ticks)
  7: 0x0268 [0x27] REQ_SET(priority=0x0A, entity_id=Zeid (ID: 17379800/0x010931D8), tag_num=0x02)
  8: 0x026F [0x1C] WAIT(120* ticks)
  9: 0x0272 [0x2B] Zeid (ID: 17379800/0x010931D8) [7391*]:
    → "I can see this place still lingers in your heart. Here is where it all began--where you set out on your journey as a Dark Knight."
 10: 0x0279 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x027A [0x1E] EventEntity looks at Zeid (ID: 17379800/0x010931D8) and starts talking
 12: 0x027F [0x1C] WAIT(60* ticks)
 13: 0x0282 [0x52] END_LOAD_SCHEDULER: End scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=47*
 14: 0x0291 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
 15: 0x0294 [0x1F] MOVE_ENTITY: EventEntity moves to X=-288.679*, Z=96.660*, Y=1.319*
 16: 0x029C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 17: 0x029E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s002" with entities [LocalPlayer, LocalPlayer], work=[47*, 0*]
 18: 0x02AF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Zeid (ID: 17379800/0x010931D8), Zeid (ID: 17379800/0x010931D8)], work=376*
 19: 0x02BE [0x2B] Zeid (ID: 17379800/0x010931D8) [7392*]:
    → "You've become stronger. However, you must never forget the souls of those that you have brought down with your mighty blade."
 20: 0x02C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x02C6 [0x52] END_LOAD_SCHEDULER: End scheduler "s002" with entities [LocalPlayer, LocalPlayer], work=47*
 22: 0x02D5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s003" with entities [LocalPlayer, LocalPlayer], work=[47*, 0*]
 23: 0x02E6 [0x2B] Zeid (ID: 17379800/0x010931D8) [7393*]:
    → "You have made many sacrifices to come this far. That is the road you have chosen, but also your sin."
 24: 0x02ED [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x02EE [0x6B] STOP_AND_IDLE: Zeid (ID: 17379800/0x010931D8) stops current action and resets to idle (animation="idl0")
 26: 0x02F7 [0x2B] Zeid (ID: 17379800/0x010931D8) [7394*]:
    → "However, at the same time, one life cannot continue on without the loss of another. Denying this truth would mean the end of all life in Vana'diel. This vicious circle must continue on."
 27: 0x02FE [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x02FF [0x52] END_LOAD_SCHEDULER: End scheduler "s003" with entities [LocalPlayer, LocalPlayer], work=47*
 29: 0x030E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s004" with entities [LocalPlayer, LocalPlayer], work=[47*, 0*]
 30: 0x031F [0x2B] Zeid (ID: 17379800/0x010931D8) [7395*]:
    → "Does the sword you wield shine as dark as the purest ebony? Do you thirst for new challenges that lie ahead? If so, seek out and destroy Gerwitz's Scythe."
 31: 0x0326 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0327 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Zeid (ID: 17379800/0x010931D8), Zeid (ID: 17379800/0x010931D8)], work=376*
 33: 0x0336 [0x2B] Zeid (ID: 17379800/0x010931D8) [7396*]:
    → "The scythe will be making its way toward the place where crystals gather. It will replenish its power there and then set out to seek fresh blood."
 34: 0x033D [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x033E [0x6B] STOP_AND_IDLE: Zeid (ID: 17379800/0x010931D8) stops current action and resets to idle (animation="idl0")
 36: 0x0347 [0x2B] Zeid (ID: 17379800/0x010931D8) [7397*]:
    → "To prove your strength to Gerwitz's beast, seek out the blood of a beast worthy enough and take it to the place where crystals gather. There you can call him."
 37: 0x034E [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x034F [0x4B] UPDATE_ENTITY_YAW(entity=Zeid (ID: 17379800/0x010931D8), yaw=10.7°*)
 39: 0x0356 [0x52] END_LOAD_SCHEDULER: End scheduler "s004" with entities [LocalPlayer, LocalPlayer], work=47*
 40: 0x0365 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s005" with entities [LocalPlayer, LocalPlayer], work=[47*, 0*]
 41: 0x0376 [0x2B] Zeid (ID: 17379800/0x010931D8) [7398*]:
    → "His beast is cautious and will not show itself to me. But to you...to you it may just..."
 42: 0x037D [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x037E [0x27] REQ_SET(priority=0x0A, entity_id=Zeid (ID: 17379800/0x010931D8), tag_num=0x03)
 44: 0x0385 [0x1C] WAIT(60* ticks)
 45: 0x0388 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 46: 0x0399 [0x1C] WAIT(60* ticks)
 47: 0x039C [0x46] CAMERA_CONTROL: Restore default settings
 48: 0x039E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x03AF [0x21] END_EVENT
 50: 0x03B0 [0x00] END_REQSTACK()
```

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03B1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:    00                                              .              
```

#### Opcodes

```
  0: 0x03B1 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03B2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:       00                                            .             
```

#### Opcodes

```
  0: 0x03B2 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03B3   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:          37 2C 80 2D 80  2E 80 2F 80 32 30 80 1F     7,.-.../.20..
03C0: 00 31 80 32 80 33 80 1F  01 00                    .1.2.3....      
```

#### Opcodes

```
  0: 0x03B3 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=55.281*, z=-24.975*, y=0.848*, direction=128.8°*
  1: 0x03BC [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x03BF [0x1F] MOVE_ENTITY: EventEntity moves to X=43.585*, Z=-36.233*, Y=3.364*
  3: 0x03C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x03C9 [0x00] END_REQSTACK()
```
