# 17748057 - DoorCornelias Room

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 2224 bytes           |
| Total Events     | 7                    |
| References Count | 61                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [621](#event-621)        | 0x0001       |    317 |             45 |
| [622](#event-622)        | 0x013E       |    826 |            118 |
| [765](#event-765)        | 0x0478       |      1 |              1 |
| [65535.1](#event-655351) | 0x0479       |      5 |              3 |
| [65535.2](#event-655352) | 0x047E       |      5 |              3 |
| [777](#event-777)        | 0x0483       |    780 |            101 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x001E      |          30 |
|       3 | 0x0089      |         137 |
|       4 | 0x0003      |           3 |
|       5 | 0x1F20      |        7968 |
|       6 | 0x000A      |          10 |
|       7 | 0x0014      |          20 |
|       8 | 0x1F21      |        7969 |
|       9 | 0x0092      |         146 |
|      10 | 0x000F      |          15 |
|      11 | 0x1F22      |        7970 |
|      12 | 0x1F23      |        7971 |
|      13 | 0x003C      |          60 |
|      14 | 0x0005      |           5 |
|      15 | 0x1F24      |        7972 |
|      16 | 0x1F25      |        7973 |
|      17 | 0x0093      |         147 |
|      18 | 0x1F26      |        7974 |
|      19 | 0x1F27      |        7975 |
|      20 | 0x1F28      |        7976 |
|      21 | 0x009F      |         159 |
|      22 | 0x1F29      |        7977 |
|      23 | 0x1F2A      |        7978 |
|      24 | 0x1F2B      |        7979 |
|      25 | 0x1F2C      |        7980 |
|      26 | 0x0001      |           1 |
|      27 | 0x1F2D      |        7981 |
|      28 | 0x1F2E      |        7982 |
|      29 | 0x1F2F      |        7983 |
|      30 | 0x0091      |         145 |
|      31 | 0x1F30      |        7984 |
|      32 | 0x1F31      |        7985 |
|      33 | 0x1F32      |        7986 |
|      34 | 0x1F33      |        7987 |
|      35 | 0x0094      |         148 |
|      36 | 0x1F34      |        7988 |
|      37 | 0x1F35      |        7989 |
|      38 | 0x009A      |         154 |
|      39 | 0x1F36      |        7990 |
|      40 | 0x0078      |         120 |
|      41 | 0x00B4      |         180 |
|      42 | 0x22AB      |        8875 |
|      43 | 0x22AC      |        8876 |
|      44 | 0x22AD      |        8877 |
|      45 | 0x22AE      |        8878 |
|      46 | 0x22AF      |        8879 |
|      47 | 0x00EE      |         238 |
|      48 | 0x22B0      |        8880 |
|      49 | 0x22B1      |        8881 |
|      50 | 0x22B2      |        8882 |
|      51 | 0x22B3      |        8883 |
|      52 | 0x22B4      |        8884 |
|      53 | 0x22B5      |        8885 |
|      54 | 0x22B6      |        8886 |
|      55 | 0x22B7      |        8887 |
|      56 | 0x22B8      |        8888 |
|      57 | 0x22B9      |        8889 |
|      58 | 0x22BA      |        8890 |
|      59 | 0x22BB      |        8891 |
|      60 | 0x22BC      |        8892 |

## String References

- **7979**: Have you ever heard of a Musketeer named Cornelia? [Yes, I have./Who?]

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

### Event 621

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 317 bytes |
| Instructions | 45        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F   BE..........fdo
0010: 30 01 80 1C 02 80 46 01  45 03 80 F0 FF FF 7F F0  0.....F.E.......
0020: FF FF 7F 73 30 37 33 01  80 38 04 80 29 0A F0 FF  ...s073..8..)...
0030: FF 7F 1A 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0040: 69 30 01 80 4A 24 D0 0E  01 F0 FF FF 7F 2B 24 D0  i0..J$.......+$.
0050: 0E 01 05 80 23 4A 32 D0  0E 01 24 D0 0E 01 4C 45  ....#J2...$...LE
0060: 03 80 F0 FF FF 7F F0 FF  FF 7F 73 30 37 34 01 80  ..........s074..
0070: 27 0A 32 D0 0E 01 0D 1C  06 80 4A 24 D0 0E 01 32  '.2.......J$...2
0080: D0 0E 01 1C 07 80 2B 32  D0 0E 01 08 80 23 2A 0A  ......+2.....#*.
0090: 32 D0 0E 01 5B 09 80 32  D0 0E 01 32 D0 0E 01 6A  2...[..2...2...j
00A0: 79 61 30 1C 0A 80 7B 32  D0 0E 01 1C 07 80 27 0A  ya0...{2......'.
00B0: 32 D0 0E 01 11 1C 06 80  4A F0 FF FF 7F 32 D0 0E  2.......J....2..
00C0: 01 79 00 24 D0 0E 01 32  D0 0E 01 27 0A 24 D0 0E  .y.$...2...'.$..
00D0: 01 06 1C 0A 80 4A F0 FF  FF 7F 32 D0 0E 01 2B 24  .....J....2...+$
00E0: D0 0E 01 0B 80 23 5B 01  80 24 D0 0E 01 24 D0 0E  .....#[..$...$..
00F0: 01 74 6C 6B 30 2B 24 D0  0E 01 0C 80 23 6B 69 64  .tlk0+$.....#kid
0100: 6C 30 24 D0 0E 01 45 00  80 F0 FF FF 7F F0 FF FF  l0$...E.........
0110: 7F 66 64 6F 31 01 80 1C  0D 80 55 03 80 F0 FF FF  .fdo1.....U.....
0120: 7F F0 FF FF 7F 73 30 37  34 46 00 45 00 80 F0 FF  .....s074F.E....
0130: FF 7F F0 FF FF 7F 66 64  69 31 01 80 21 00        ......fdi1..!.  
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x0013 [0x1C] WAIT(30* ticks)
  3: 0x0016 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0018 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s073" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
  5: 0x0029 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  6: 0x002C [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=LocalPlayer, tag_num=0x1A)
  7: 0x0033 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0044 [0x4A] Franziska (ID: 17748004/0x010ED024) looks at LocalPlayer
  9: 0x004D [0x2B] Franziska (ID: 17748004/0x010ED024) [7968*]:
    → "Lady Cornelia is in her room doing her studies. Please come back some other--"
 10: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0055 [0x4A] Cornelia (ID: 17748018/0x010ED032) looks at Franziska (ID: 17748004/0x010ED024)
 12: 0x005E [0x4C] EventEntity->StatusEvent = 8 // Open door
 13: 0x005F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s074" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 14: 0x0070 [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x0D)
 15: 0x0077 [0x1C] WAIT(10* ticks)
 16: 0x007A [0x4A] Franziska (ID: 17748004/0x010ED024) looks at Cornelia (ID: 17748018/0x010ED032)
 17: 0x0083 [0x1C] WAIT(20* ticks)
 18: 0x0086 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7969*]:
    → "I've had enough of studying. I'm going out!"
 19: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x008E [0x2A] GET_REQ_LEVEL(level=10, entity_id=Cornelia (ID: 17748018/0x010ED032))
 21: 0x0094 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "jya0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=146*
 22: 0x00A3 [0x1C] WAIT(15* ticks)
 23: 0x00A6 [0x7B] Cornelia (ID: 17748018/0x010ED032) stops talking
 24: 0x00AB [0x1C] WAIT(20* ticks)
 25: 0x00AE [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x11)
 26: 0x00B5 [0x1C] WAIT(10* ticks)
 27: 0x00B8 [0x4A] LocalPlayer looks at Cornelia (ID: 17748018/0x010ED032)
 28: 0x00C1 [0x79] Franziska (ID: 17748004/0x010ED024) looks at Cornelia (ID: 17748018/0x010ED032) (Basic look)
 29: 0x00CB [0x27] REQ_SET(priority=0x0A, entity_id=Franziska (ID: 17748004/0x010ED024), tag_num=0x06)
 30: 0x00D2 [0x1C] WAIT(15* ticks)
 31: 0x00D5 [0x4A] LocalPlayer looks at Cornelia (ID: 17748018/0x010ED032)
 32: 0x00DE [0x2B] Franziska (ID: 17748004/0x010ED024) [7970*]:
    → "Milady, don't-- Oh, not again!"
 33: 0x00E5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x00E6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Franziska (ID: 17748004/0x010ED024), Franziska (ID: 17748004/0x010ED024)], work=0*
 35: 0x00F5 [0x2B] Franziska (ID: 17748004/0x010ED024) [7971*]:
    → "Why must she be like this? If the First Lady were still alive, she would never have tolerated this kind of behavior!"
 36: 0x00FC [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x00FD [0x6B] STOP_AND_IDLE: Franziska (ID: 17748004/0x010ED024) stops current action and resets to idle (animation="idl0")
 38: 0x0106 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x0117 [0x1C] WAIT(60* ticks)
 40: 0x011A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s074" with entities [LocalPlayer, LocalPlayer], work=137*
 41: 0x0129 [0x46] CAMERA_CONTROL: Restore default settings
 42: 0x012B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x013C [0x21] END_EVENT
 44: 0x013D [0x00] END_REQSTACK()
```

### Event 622

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x013E    |
| Data Size    | 826 bytes |
| Instructions | 118       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            42 45                BE
0140: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 30 01 80  ..........fdo0..
0150: 1C 02 80 46 01 38 04 80  29 0A F0 FF FF 7F 1B 45  ...F.8..)......E
0160: 03 80 F0 FF FF 7F F0 FF  FF 7F 73 30 37 33 01 80  ..........s073..
0170: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 30 01  E..........fdi0.
0180: 80 1C 0E 80 4A 24 D0 0E  01 F0 FF FF 7F 2B 24 D0  ....J$.......+$.
0190: 0E 01 0F 80 23 4C 45 03  80 F0 FF FF 7F F0 FF FF  ....#LE.........
01A0: 7F 73 30 37 34 01 80 27  0A 32 D0 0E 01 0E 1C 06  .s074..'.2......
01B0: 80 4A 24 D0 0E 01 32 D0  0E 01 4A F0 FF FF 7F 32  .J$...2...J....2
01C0: D0 0E 01 2B 24 D0 0E 01  10 80 23 2A 0A 32 D0 0E  ...+$.....#*.2..
01D0: 01 5B 11 80 32 D0 0E 01  32 D0 0E 01 74 6C 63 30  .[..2...2...tlc0
01E0: 2B 32 D0 0E 01 12 80 23  6B 69 64 6C 30 32 D0 0E  +2.....#kidl02..
01F0: 01 1C 06 80 27 0A 32 D0  0E 01 0F 1C 06 80 27 0A  ....'.2.......'.
0200: F0 FF FF 7F 1C 5B 01 80  24 D0 0E 01 24 D0 0E 01  .....[..$...$...
0210: 74 6C 6B 30 2B 24 D0 0E  01 13 80 23 2A 0A F0 FF  tlk0+$.....#*...
0220: FF 7F 4D 45 03 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ..ME..........s0
0230: 37 35 01 80 6B 69 64 6C  30 24 D0 0E 01 1C 07 80  75..kidl0$......
0240: 27 0A 24 D0 0E 01 07 1C  07 80 5D 01 80 0D 80 45  '.$.......]....E
0250: 03 80 F0 FF FF 7F F0 FF  FF 7F 73 30 37 36 01 80  ..........s076..
0260: 27 0A 32 D0 0E 01 10 27  0A F0 FF FF 7F 1D 2B 24  '.2....'......+$
0270: D0 0E 01 14 80 23 2A 0A  32 D0 0E 01 5C 00 15 80  .....#*.2...\...
0280: 5C 01 15 80 5B 09 80 32  D0 0E 01 32 D0 0E 01 74  \...[..2...2...t
0290: 6C 62 30 2B 32 D0 0E 01  16 80 23 5B 09 80 32 D0  lb0+2.....#[..2.
02A0: 0E 01 32 D0 0E 01 74 6C  62 31 1C 02 80 4A 32 D0  ..2...tlb1...J2.
02B0: 0E 01 F0 FF FF 7F 2B 32  D0 0E 01 17 80 23 24 18  ......+2.....#$.
02C0: 80 01 80 01 80 25 02 00  10 01 80 00 E8 02 5B 11  .....%........[.
02D0: 80 32 D0 0E 01 32 D0 0E  01 74 6C 63 30 2B 32 D0  .2...2...tlc0+2.
02E0: 0E 01 19 80 23 01 0A 03  02 00 10 1A 80 00 0A 03  ....#...........
02F0: 5B 11 80 32 D0 0E 01 32  D0 0E 01 74 6C 63 30 2B  [..2...2...tlc0+
0300: 32 D0 0E 01 1B 80 23 01  0A 03 53 32 D0 0E 01 32  2.....#...S2...2
0310: D0 0E 01 74 6C 63 30 1C  0E 80 27 0A 32 D0 0E 01  ...tlc0...'.2...
0320: 13 52 03 80 F0 FF FF 7F  F0 FF FF 7F 73 30 37 36  .R..........s076
0330: 45 03 80 F0 FF FF 7F F0  FF FF 7F 73 30 37 37 01  E..........s077.
0340: 80 2B 32 D0 0E 01 1C 80  23 2B 32 D0 0E 01 1D 80  .+2.....#+2.....
0350: 23 2A 0A 32 D0 0E 01 5B  1E 80 32 D0 0E 01 32 D0  #*.2...[..2...2.
0360: 0E 01 74 68 6B 31 2B 32  D0 0E 01 1F 80 23 2B 32  ..thk1+2.....#+2
0370: D0 0E 01 20 80 23 5B 1E  80 32 D0 0E 01 32 D0 0E  ... .#[..2...2..
0380: 01 74 68 6B 32 2B 32 D0  0E 01 21 80 23 53 32 D0  .thk2+2...!.#S2.
0390: 0E 01 32 D0 0E 01 74 68  6B 32 1C 1A 80 4A 32 D0  ..2...thk2...J2.
03A0: 0E 01 F0 FF FF 7F 2B 32  D0 0E 01 22 80 23 52 03  ......+2...".#R.
03B0: 80 F0 FF FF 7F F0 FF FF  7F 73 30 37 37 45 03 80  .........s077E..
03C0: F0 FF FF 7F F0 FF FF 7F  73 30 39 32 01 80 1C 07  ........s092....
03D0: 80 5B 23 80 32 D0 0E 01  32 D0 0E 01 75 74 75 30  .[#.2...2...utu0
03E0: 2B 32 D0 0E 01 24 80 23  1C 02 80 5B 23 80 32 D0  +2...$.#...[#.2.
03F0: 0E 01 32 D0 0E 01 75 74  75 31 1C 02 80 5D 01 80  ..2...utu1...]..
0400: 0D 80 5B 09 80 32 D0 0E  01 32 D0 0E 01 69 6B 72  ..[..2...2...ikr
0410: 30 2B 32 D0 0E 01 25 80  23 5B 09 80 32 D0 0E 01  0+2...%.#[..2...
0420: 32 D0 0E 01 69 6B 72 31  5C 00 26 80 5C 01 26 80  2...ikr1\.&.\.&.
0430: 2B 32 D0 0E 01 27 80 23  4C 27 0A 32 D0 0E 01 12  +2...'.#L'.2....
0440: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 01  E..........fdo1.
0450: 80 1C 28 80 52 03 80 F0  FF FF 7F F0 FF FF 7F 73  ..(.R..........s
0460: 30 39 32 46 00 45 00 80  F0 FF FF 7F F0 FF FF 7F  092F.E..........
0470: 66 64 69 31 01 80 21 00                           fdi1..!.        
```

#### Opcodes

```
  0: 0x013E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x013F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x0150 [0x1C] WAIT(30* ticks)
  3: 0x0153 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0155 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  5: 0x0158 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=LocalPlayer, tag_num=0x1B)
  6: 0x015F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s073" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
  7: 0x0170 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0181 [0x1C] WAIT(5* ticks)
  9: 0x0184 [0x4A] Franziska (ID: 17748004/0x010ED024) looks at LocalPlayer
 10: 0x018D [0x2B] Franziska (ID: 17748004/0x010ED024) [7972*]:
    → "Lady Cornelia is in her room doing her studies. For once, she isn't--"
 11: 0x0194 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0195 [0x4C] EventEntity->StatusEvent = 8 // Open door
 13: 0x0196 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s074" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 14: 0x01A7 [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x0E)
 15: 0x01AE [0x1C] WAIT(10* ticks)
 16: 0x01B1 [0x4A] Franziska (ID: 17748004/0x010ED024) looks at Cornelia (ID: 17748018/0x010ED032)
 17: 0x01BA [0x4A] LocalPlayer looks at Cornelia (ID: 17748018/0x010ED032)
 18: 0x01C3 [0x2B] Franziska (ID: 17748004/0x010ED024) [7973*]:
    → "No, Milady! Not this time! The president has given me strict orders not to let you out of your--"
 19: 0x01CA [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x01CB [0x2A] GET_REQ_LEVEL(level=10, entity_id=Cornelia (ID: 17748018/0x010ED032))
 21: 0x01D1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=147*
 22: 0x01E0 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7974*]:
    → "Hello. Come in."
 23: 0x01E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x01E8 [0x6B] STOP_AND_IDLE: Cornelia (ID: 17748018/0x010ED032) stops current action and resets to idle (animation="idl0")
 25: 0x01F1 [0x1C] WAIT(10* ticks)
 26: 0x01F4 [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x0F)
 27: 0x01FB [0x1C] WAIT(10* ticks)
 28: 0x01FE [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x1C)
 29: 0x0205 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Franziska (ID: 17748004/0x010ED024), Franziska (ID: 17748004/0x010ED024)], work=0*
 30: 0x0214 [0x2B] Franziska (ID: 17748004/0x010ED024) [7975*]:
    → "Oh, you were expecting a guest! I'm sorry, I thought you were trying to sneak out--"
 31: 0x021B [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x021C [0x2A] GET_REQ_LEVEL(level=10, entity_id=LocalPlayer)
 33: 0x0222 [0x4D] EventEntity->StatusEvent = 9 // Close door
 34: 0x0223 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s075" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 35: 0x0234 [0x6B] STOP_AND_IDLE: Franziska (ID: 17748004/0x010ED024) stops current action and resets to idle (animation="idl0")
 36: 0x023D [0x1C] WAIT(20* ticks)
 37: 0x0240 [0x27] REQ_SET(priority=0x0A, entity_id=Franziska (ID: 17748004/0x010ED024), tag_num=0x07)
 38: 0x0247 [0x1C] WAIT(20* ticks)
 39: 0x024A [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=60*)
 40: 0x024F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s076" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 41: 0x0260 [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x10)
 42: 0x0267 [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x1D)
 43: 0x026E [0x2B] Franziska (ID: 17748004/0x010ED024) [7976*]:
    → "Wait, Milady, no! You shouldn't be letting some adventurer into your room! You know the kind of places they frequent! And it wouldn't be proper!"
 44: 0x0275 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x0276 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Cornelia (ID: 17748018/0x010ED032))
 46: 0x027C [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 159*
 47: 0x0280 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 159*
 48: 0x0284 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=146*
 49: 0x0293 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7977*]:
    → "Oh, brother... Can you believe her? This is what I have to put up with every day. I usually manage to sneak out, though."
 50: 0x029A [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x029B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=146*
 52: 0x02AA [0x1C] WAIT(30* ticks)
 53: 0x02AD [0x4A] Cornelia (ID: 17748018/0x010ED032) looks at LocalPlayer
 54: 0x02B6 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7978*]:
    → "I've been meaning to ask you--have you ever heard the story of Cornelia the Musketeer?"
 55: 0x02BD [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x02BE [0x24] CREATE_DIALOG(message_id=7979*, default_option=0*, option_flags=0*)
    → "Have you ever heard of a Musketeer named Cornelia? [Yes, I have./Who?]"
 57: 0x02C5 [0x25] WAIT_DIALOG_SELECT()
 58: 0x02C6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02E8
 59: 0x02CE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=147*
 60: 0x02DD [0x2B] Cornelia (ID: 17748018/0x010ED032) [7980*]:
    → "Cornelia, the monk who became a Mythril Musketeer, is pretty famous. She helped all those in need, whether they were Galka or Hume, rich or poor."
 61: 0x02E4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x02E5 [0x01] GOTO 0x030A
 63: 0x02E8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x030A
 64: 0x02F0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=147*
 65: 0x02FF [0x2B] Cornelia (ID: 17748018/0x010ED032) [7981*]:
    → "You've never heard of her? She was a monk who became a Mythril Musketeer. She helped all those in need, Galka and Hume, rich and poor alike."
 66: 0x0306 [0x23] WAIT_FOR_DIALOG_INTERACTION
 67: 0x0307 [0x01] GOTO 0x030A

SUBROUTINE_030A:
 68: 0x030A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)]
 69: 0x0317 [0x1C] WAIT(5* ticks)
 70: 0x031A [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x13)
 71: 0x0321 [0x52] END_LOAD_SCHEDULER: End scheduler "s076" with entities [LocalPlayer, LocalPlayer], work=137*
 72: 0x0330 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s077" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 73: 0x0341 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7982*]:
    → "It was rumored that she and Talekeeper Raogrimm--the only Galka destined to have become a Musketeer Captain if he were still alive--were sharing a forbidden love..."
 74: 0x0348 [0x23] WAIT_FOR_DIALOG_INTERACTION
 75: 0x0349 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7983*]:
    → "But no one knows if that was true, since neither returned from their expedition to Xarcabard thirty years ago."
 76: 0x0350 [0x23] WAIT_FOR_DIALOG_INTERACTION
 77: 0x0351 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Cornelia (ID: 17748018/0x010ED032))
 78: 0x0357 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=145*
 79: 0x0366 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7984*]:
    → "My mother named me after her. She told me that she wanted me to grow up to be just like her--someone who would treat everyone equally, and loved by all."
 80: 0x036D [0x23] WAIT_FOR_DIALOG_INTERACTION
 81: 0x036E [0x2B] Cornelia (ID: 17748018/0x010ED032) [7985*]:
    → "Maybe that's why I try so hard to help the Galka...though even if I weren't named Cornelia, I wouldn't stand by and watch them be treated like they are."
 82: 0x0375 [0x23] WAIT_FOR_DIALOG_INTERACTION
 83: 0x0376 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=145*
 84: 0x0385 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7986*]:
    → "But it's no good. You've seen it, too. I just can't seem to do anything right. I wish I were as strong and smart as Lady Cornelia..."
 85: 0x038C [0x23] WAIT_FOR_DIALOG_INTERACTION
 86: 0x038D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)]
 87: 0x039A [0x1C] WAIT(1* ticks)
 88: 0x039D [0x4A] Cornelia (ID: 17748018/0x010ED032) looks at LocalPlayer
 89: 0x03A6 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7987*]:
    → "This Galka child told me the other day, "Why are you trying so hard? What can you do, you're just a girl!""
 90: 0x03AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 91: 0x03AE [0x52] END_LOAD_SCHEDULER: End scheduler "s077" with entities [LocalPlayer, LocalPlayer], work=137*
 92: 0x03BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s092" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 93: 0x03CE [0x1C] WAIT(20* ticks)
 94: 0x03D1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "utu0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=148*
 95: 0x03E0 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7988*]:
    → "Maybe he's right. Maybe I can't change anything..."
 96: 0x03E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 97: 0x03E8 [0x1C] WAIT(30* ticks)
 98: 0x03EB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "utu1" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=148*
 99: 0x03FA [0x1C] WAIT(30* ticks)
100: 0x03FD [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=60*)
101: 0x0402 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ikr0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=146*
102: 0x0411 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7989*]:
    → "No! I've got to try harder! I'll show that know-it-all, Gumbah, what I can do!"
103: 0x0418 [0x23] WAIT_FOR_DIALOG_INTERACTION
104: 0x0419 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ikr1" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=146*
105: 0x0428 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 154*
106: 0x042C [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 154*
107: 0x0430 [0x2B] Cornelia (ID: 17748018/0x010ED032) [7990*]:
    → "I'm sorry to leave you like this, but I've got to go!"
108: 0x0437 [0x23] WAIT_FOR_DIALOG_INTERACTION
109: 0x0438 [0x4C] EventEntity->StatusEvent = 8 // Open door
110: 0x0439 [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x12)
111: 0x0440 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
112: 0x0451 [0x1C] WAIT(120* ticks)
113: 0x0454 [0x52] END_LOAD_SCHEDULER: End scheduler "s092" with entities [LocalPlayer, LocalPlayer], work=137*
114: 0x0463 [0x46] CAMERA_CONTROL: Restore default settings
115: 0x0465 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
116: 0x0476 [0x21] END_EVENT
117: 0x0477 [0x00] END_REQSTACK()
```

### Event 765

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0478  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0470:                          00                               .       
```

#### Opcodes

```
  0: 0x0478 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0479  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0470:                             4C 1C 29 80 00                 L.)..  
```

#### Opcodes

```
  0: 0x0479 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x047A [0x1C] WAIT(180* ticks)
  2: 0x047D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x047E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0470:                                            4D 1C                M.
0480: 29 80 00                                          )..             
```

#### Opcodes

```
  0: 0x047E [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x047F [0x1C] WAIT(180* ticks)
  2: 0x0482 [0x00] END_REQSTACK()
```

### Event 777

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0483    |
| Data Size    | 780 bytes |
| Instructions | 101       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0480:          42 45 00 80 F0  FF FF 7F F0 FF FF 7F 66     BE..........f
0490: 64 6F 30 01 80 1C 02 80  46 01 38 04 80 29 0A F0  do0.....F.8..)..
04A0: FF FF 7F 1B 45 03 80 F0  FF FF 7F F0 FF FF 7F 73  ....E..........s
04B0: 30 37 33 01 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  073..E..........
04C0: 66 64 69 30 01 80 1C 0E  80 4A 24 D0 0E 01 F0 FF  fdi0.....J$.....
04D0: FF 7F 2B 24 D0 0E 01 0F  80 23 4C 45 03 80 F0 FF  ..+$.....#LE....
04E0: FF 7F F0 FF FF 7F 73 30  37 34 01 80 27 0A 32 D0  ......s074..'.2.
04F0: 0E 01 0E 1C 06 80 4A 24  D0 0E 01 32 D0 0E 01 4A  ......J$...2...J
0500: F0 FF FF 7F 32 D0 0E 01  2B 24 D0 0E 01 2A 80 23  ....2...+$...*.#
0510: 2A 0A 32 D0 0E 01 5B 11  80 32 D0 0E 01 32 D0 0E  *.2...[..2...2..
0520: 01 74 6C 63 30 2B 32 D0  0E 01 2B 80 23 6B 69 64  .tlc0+2...+.#kid
0530: 6C 30 32 D0 0E 01 1C 06  80 27 0A 32 D0 0E 01 0F  l02......'.2....
0540: 1C 06 80 27 0A F0 FF FF  7F 1C 5B 01 80 24 D0 0E  ...'......[..$..
0550: 01 24 D0 0E 01 74 6C 6B  30 2B 24 D0 0E 01 2C 80  .$...tlk0+$...,.
0560: 23 2A 0A F0 FF FF 7F 4D  45 03 80 F0 FF FF 7F F0  #*.....ME.......
0570: FF FF 7F 73 30 37 35 01  80 6B 69 64 6C 30 24 D0  ...s075..kidl0$.
0580: 0E 01 1C 07 80 27 0A 24  D0 0E 01 07 1C 07 80 45  .....'.$.......E
0590: 03 80 F0 FF FF 7F F0 FF  FF 7F 73 30 37 36 01 80  ..........s076..
05A0: 27 0A 32 D0 0E 01 10 27  0A F0 FF FF 7F 1D 2B 24  '.2....'......+$
05B0: D0 0E 01 2D 80 23 2A 0A  32 D0 0E 01 5B 09 80 32  ...-.#*.2...[..2
05C0: D0 0E 01 32 D0 0E 01 74  6C 62 30 2B 32 D0 0E 01  ...2...tlb0+2...
05D0: 2E 80 23 5B 09 80 32 D0  0E 01 32 D0 0E 01 74 6C  ..#[..2...2...tl
05E0: 62 31 1C 06 80 4A 32 D0  0E 01 F0 FF FF 7F 45 00  b1...J2.......E.
05F0: 80 F0 FF FF 7F F0 FF FF  7F 6F 76 6C 31 01 80 52  .........ovl1..R
0600: 03 80 F0 FF FF 7F F0 FF  FF 7F 73 30 37 36 45 2F  ..........s076E/
0610: 80 F0 FF FF 7F F0 FF FF  7F 73 30 35 30 01 80 2B  .........s050..+
0620: 32 D0 0E 01 30 80 23 5B  1E 80 32 D0 0E 01 32 D0  2...0.#[..2...2.
0630: 0E 01 74 6C 61 30 2B 32  D0 0E 01 31 80 23 2B 32  ..tla0+2...1.#+2
0640: D0 0E 01 32 80 23 5B 1E  80 32 D0 0E 01 32 D0 0E  ...2.#[..2...2..
0650: 01 74 6C 61 31 2B 32 D0  0E 01 33 80 23 45 00 80  .tla1+2...3.#E..
0660: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 01 80 52 2F  ........ovl1..R/
0670: 80 F0 FF FF 7F F0 FF FF  7F 73 30 35 30 45 2F 80  .........s050E/.
0680: F0 FF FF 7F F0 FF FF 7F  73 30 35 31 01 80 7B 32  ........s051..{2
0690: D0 0E 01 2B 32 D0 0E 01  34 80 23 2B 32 D0 0E 01  ...+2...4.#+2...
06A0: 35 80 23 2B 32 D0 0E 01  36 80 23 5B 1E 80 32 D0  5.#+2...6.#[..2.
06B0: 0E 01 32 D0 0E 01 74 68  6B 31 2B 32 D0 0E 01 37  ..2...thk1+2...7
06C0: 80 23 52 2F 80 F0 FF FF  7F F0 FF FF 7F 73 30 35  .#R/.........s05
06D0: 31 45 2F 80 F0 FF FF 7F  F0 FF FF 7F 73 30 35 32  1E/.........s052
06E0: 01 80 2B 24 D0 0E 01 38  80 23 5B 1E 80 32 D0 0E  ..+$...8.#[..2..
06F0: 01 32 D0 0E 01 74 68 6B  32 2B 32 D0 0E 01 39 80  .2...thk2+2...9.
0700: 23 52 2F 80 F0 FF FF 7F  F0 FF FF 7F 73 30 35 32  #R/.........s052
0710: 45 2F 80 F0 FF FF 7F F0  FF FF 7F 73 30 35 33 01  E/.........s053.
0720: 80 5B 1E 80 32 D0 0E 01  32 D0 0E 01 74 6C 61 30  .[..2...2...tla0
0730: 2B 32 D0 0E 01 3A 80 23  5B 1E 80 32 D0 0E 01 32  +2...:.#[..2...2
0740: D0 0E 01 74 6C 61 31 2B  32 D0 0E 01 3B 80 23 5B  ...tla1+2...;.#[
0750: 1E 80 32 D0 0E 01 32 D0  0E 01 77 61 76 30 2B 32  ..2...2...wav0+2
0760: D0 0E 01 3C 80 23 45 00  80 F0 FF FF 7F F0 FF FF  ...<.#E.........
0770: 7F 66 64 6F 31 01 80 1C  28 80 46 00 45 00 80 F0  .fdo1...(.F.E...
0780: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 21 00     .......fdi1..!. 
```

#### Opcodes

```
  0: 0x0483 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0484 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x0495 [0x1C] WAIT(30* ticks)
  3: 0x0498 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x049A [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  5: 0x049D [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=LocalPlayer, tag_num=0x1B)
  6: 0x04A4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s073" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
  7: 0x04B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x04C6 [0x1C] WAIT(5* ticks)
  9: 0x04C9 [0x4A] Franziska (ID: 17748004/0x010ED024) looks at LocalPlayer
 10: 0x04D2 [0x2B] Franziska (ID: 17748004/0x010ED024) [7972*]:
    → "Lady Cornelia is in her room doing her studies. For once, she isn't--"
 11: 0x04D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x04DA [0x4C] EventEntity->StatusEvent = 8 // Open door
 13: 0x04DB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s074" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 14: 0x04EC [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x0E)
 15: 0x04F3 [0x1C] WAIT(10* ticks)
 16: 0x04F6 [0x4A] Franziska (ID: 17748004/0x010ED024) looks at Cornelia (ID: 17748018/0x010ED032)
 17: 0x04FF [0x4A] LocalPlayer looks at Cornelia (ID: 17748018/0x010ED032)
 18: 0x0508 [0x2B] Franziska (ID: 17748004/0x010ED024) [8875*]:
    → "Milady! I will not allow you to sneak out of your chambers again, and I will definitely not allow any adventurers in here."
 19: 0x050F [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0510 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Cornelia (ID: 17748018/0x010ED032))
 21: 0x0516 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=147*
 22: 0x0525 [0x2B] Cornelia (ID: 17748018/0x010ED032) [8876*]:
    → "Oh, <Player>. My father sent you, right?"
 23: 0x052C [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x052D [0x6B] STOP_AND_IDLE: Cornelia (ID: 17748018/0x010ED032) stops current action and resets to idle (animation="idl0")
 25: 0x0536 [0x1C] WAIT(10* ticks)
 26: 0x0539 [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x0F)
 27: 0x0540 [0x1C] WAIT(10* ticks)
 28: 0x0543 [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x1C)
 29: 0x054A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Franziska (ID: 17748004/0x010ED024), Franziska (ID: 17748004/0x010ED024)], work=0*
 30: 0x0559 [0x2B] Franziska (ID: 17748004/0x010ED024) [8877*]:
    → "The president! I...I apologize. Please proceed..."
 31: 0x0560 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0561 [0x2A] GET_REQ_LEVEL(level=10, entity_id=LocalPlayer)
 33: 0x0567 [0x4D] EventEntity->StatusEvent = 9 // Close door
 34: 0x0568 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s075" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 35: 0x0579 [0x6B] STOP_AND_IDLE: Franziska (ID: 17748004/0x010ED024) stops current action and resets to idle (animation="idl0")
 36: 0x0582 [0x1C] WAIT(20* ticks)
 37: 0x0585 [0x27] REQ_SET(priority=0x0A, entity_id=Franziska (ID: 17748004/0x010ED024), tag_num=0x07)
 38: 0x058C [0x1C] WAIT(20* ticks)
 39: 0x058F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s076" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 40: 0x05A0 [0x27] REQ_SET(priority=0x0A, entity_id=Cornelia (ID: 17748018/0x010ED032), tag_num=0x10)
 41: 0x05A7 [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x1D)
 42: 0x05AE [0x2B] Franziska (ID: 17748004/0x010ED024) [8878*]:
    → "Wait... Milady! I have not heard of any meetings with any adventurers! You have tricked me! Milady!"
 43: 0x05B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x05B6 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Cornelia (ID: 17748018/0x010ED032))
 45: 0x05BC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=146*
 46: 0x05CB [0x2B] Cornelia (ID: 17748018/0x010ED032) [8879*]:
    → "Franziska means well, but she's got to loosen up, don't you think?"
 47: 0x05D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x05D3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=146*
 49: 0x05E2 [0x1C] WAIT(10* ticks)
 50: 0x05E5 [0x4A] Cornelia (ID: 17748018/0x010ED032) looks at LocalPlayer
 51: 0x05EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 52: 0x05FF [0x52] END_LOAD_SCHEDULER: End scheduler "s076" with entities [LocalPlayer, LocalPlayer], work=137*
 53: 0x060E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s050" with entities [LocalPlayer, LocalPlayer], work=[238*, 0*]
 54: 0x061F [0x2B] Cornelia (ID: 17748018/0x010ED032) [8880*]:
    → "Anyway, you'll never guess who was here just a couple of days ago."
 55: 0x0626 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x0627 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=145*
 57: 0x0636 [0x2B] Cornelia (ID: 17748018/0x010ED032) [8881*]:
    → "I can't believe that my father would even let him near this place..."
 58: 0x063D [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x063E [0x2B] Cornelia (ID: 17748018/0x010ED032) [8882*]:
    → "Gumbah. Gumbah came here, to my room. He didn't say anything for the first few minutes, but when he opened his mouth, the first words out were "thank you.""
 60: 0x0645 [0x23] WAIT_FOR_DIALOG_INTERACTION
 61: 0x0646 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=145*
 62: 0x0655 [0x2B] Cornelia (ID: 17748018/0x010ED032) [8883*]:
    → ""Thank you." What did he mean? I haven't done anything worth thanking. I've only caused him pain and trouble."
 63: 0x065C [0x23] WAIT_FOR_DIALOG_INTERACTION
 64: 0x065D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 65: 0x066E [0x52] END_LOAD_SCHEDULER: End scheduler "s050" with entities [LocalPlayer, LocalPlayer], work=238*
 66: 0x067D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s051" with entities [LocalPlayer, LocalPlayer], work=[238*, 0*]
 67: 0x068E [0x7B] Cornelia (ID: 17748018/0x010ED032) stops talking
 68: 0x0693 [0x2B] Cornelia (ID: 17748018/0x010ED032) [8884*]:
    → "For someone who has lived more than two hundred years, he's not that good with telling people how he feels. But, you know, I'm kind of happy that he told me what he did..."
 69: 0x069A [0x23] WAIT_FOR_DIALOG_INTERACTION
 70: 0x069B [0x2B] Cornelia (ID: 17748018/0x010ED032) [8885*]:
    → "I've only been on Vana'diel for a tenth of time he has, so I can't really talk about being good at expressing feelings..."
 71: 0x06A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 72: 0x06A3 [0x2B] Cornelia (ID: 17748018/0x010ED032) [8886*]:
    → "Anyway, once the ice was broken, we started talking about all sorts of stuff."
 73: 0x06AA [0x23] WAIT_FOR_DIALOG_INTERACTION
 74: 0x06AB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=145*
 75: 0x06BA [0x2B] Cornelia (ID: 17748018/0x010ED032) [8887*]:
    → "For some reason, he seemed really interested in one of Lucius' new programs. I wonder what that was all about?"
 76: 0x06C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 77: 0x06C2 [0x52] END_LOAD_SCHEDULER: End scheduler "s051" with entities [LocalPlayer, LocalPlayer], work=238*
 78: 0x06D1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s052" with entities [LocalPlayer, LocalPlayer], work=[238*, 0*]
 79: 0x06E2 [0x2B] Franziska (ID: 17748004/0x010ED024) [8888*]:
    → "Milady! It is time for your studies!"
 80: 0x06E9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 81: 0x06EA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=145*
 82: 0x06F9 [0x2B] Cornelia (ID: 17748018/0x010ED032) [8889*]:
    → "Yes, Franziska! I know!"
 83: 0x0700 [0x23] WAIT_FOR_DIALOG_INTERACTION
 84: 0x0701 [0x52] END_LOAD_SCHEDULER: End scheduler "s052" with entities [LocalPlayer, LocalPlayer], work=238*
 85: 0x0710 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s053" with entities [LocalPlayer, LocalPlayer], work=[238*, 0*]
 86: 0x0721 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=145*
 87: 0x0730 [0x2B] Cornelia (ID: 17748018/0x010ED032) [8890*]:
    → "You know, I think I'm going to start putting a little more effort into my studies. I think I finally know what I want to be when I get older."
 88: 0x0737 [0x23] WAIT_FOR_DIALOG_INTERACTION
 89: 0x0738 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=145*
 90: 0x0747 [0x2B] Cornelia (ID: 17748018/0x010ED032) [8891*]:
    → "What do I want to be? I can't tell you yet. That's still a secret."
 91: 0x074E [0x23] WAIT_FOR_DIALOG_INTERACTION
 92: 0x074F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wav0" with entities [Cornelia (ID: 17748018/0x010ED032), Cornelia (ID: 17748018/0x010ED032)], work=145*
 93: 0x075E [0x2B] Cornelia (ID: 17748018/0x010ED032) [8892*]:
    → "Well, you should probably go before Franziska has Iron Eater drag you out. Thanks for coming and listening to me."
 94: 0x0765 [0x23] WAIT_FOR_DIALOG_INTERACTION
 95: 0x0766 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 96: 0x0777 [0x1C] WAIT(120* ticks)
 97: 0x077A [0x46] CAMERA_CONTROL: Restore default settings
 98: 0x077C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 99: 0x078D [0x21] END_EVENT
100: 0x078E [0x00] END_REQSTACK()
```
