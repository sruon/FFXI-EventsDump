# 17723461 - Heruze-Moruze

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 1664 bytes                    |
| Total Events     | 5                             |
| References Count | 35                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [582](#event-582)     | 0x0001       |   1377 |            176 |
| [554](#event-554)     | 0x0562       |     36 |             10 |
| [577](#event-577)     | 0x0586       |     36 |             10 |
| [578](#event-578)     | 0x05AA       |     36 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x0164      |         356 |
|       2 | 0x003C      |          60 |
|       3 | 0x0083      |         131 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x0028      |          40 |
|       7 | 0x2CC5      |       11461 |
|       8 | 0x001E      |          30 |
|       9 | 0x0001      |           1 |
|      10 | 0x0010      |          16 |
|      11 | 0x005A      |          90 |
|      12 | 0x02FA      |         762 |
|      13 | 0x4928      |       18728 |
|      14 | 0x8F1E      |       36638 |
|      15 | 0xFFFFF731  |  4294965041 |
|      16 | 0xFFFFF830  |  4294965296 |
|      17 | 0x0BE9      |        3049 |
|      18 | 0x4936      |       18742 |
|      19 | 0x0078      |         120 |
|      20 | 0x000F      |          15 |
|      21 | 0x0063      |          99 |
|      22 | 0x4929      |       18729 |
|      23 | 0x021A      |         538 |
|      24 | 0x492A      |       18730 |
|      25 | 0x492B      |       18731 |
|      26 | 0x492C      |       18732 |
|      27 | 0x492D      |       18733 |
|      28 | 0x0007      |           7 |
|      29 | 0xFFFF36CB  |  4294915787 |
|      30 | 0x8CEB      |       36075 |
|      31 | 0x0163      |         355 |
|      32 | 0x2CC1      |       11457 |
|      33 | 0x2CC2      |       11458 |
|      34 | 0x2CC3      |       11459 |

## String References

- **11457**: If it's the consul you're a-seeking, she's inside!
- **11458**: A San d'Orian, are you? This is the Consulate of Windurst. We provide all sorts of aid to our countrymen here.
- **11459**: A Bastoker, are you? This is the Consulate of Windurst. If you're looking for your consulate, it's out the door and across the way.
- **11461**: You've come on orders from the homeland, have you? You should speak with Consul Kasaroro.
- **18742**: @@

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

### Event 582

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 1377 bytes |
| Instructions | 129        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 00 00 09 10 46  01 38 00 80 75 00 01 80   B.....F.8..u...
0010: 75 01 80 F8 FF FF 7F 1C  02 80 45 03 80 F0 FF FF  u.........E.....
0020: 7F F0 FF FF 7F 73 30 38  30 04 80 45 05 80 F0 FF  .....s080..E....
0030: FF 7F F0 FF FF 7F 66 64  6F 31 04 80 27 64 F0 FF  ......fdo1..'d..
0040: FF 7F 27 27 65 47 70 0E  01 02 45 05 80 F0 FF FF  ..''eGp...E.....
0050: 7F F0 FF FF 7F 66 64 69  31 04 80 66 06 80 F8 FF  .....fdi1..f....
0060: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 07 80 23 5E 69  ......tlk0...#^i
0070: 64 6C 30 1C 02 80 45 03  80 F0 FF FF 7F F0 FF FF  dl0...E.........
0080: 7F 73 30 38 31 04 80 27  65 47 70 0E 01 03 2A 65  .s081..'eGp...*e
0090: 47 70 0E 01 27 65 47 70  0E 01 04 2A 65 47 70 0E  Gp..'eGp...*eGp.
00A0: 01 1C 08 80 79 00 F0 FF  FF 7F 47 70 0E 01 27 67  ....y.....Gp..'g
00B0: F0 FF FF 7F 2B 45 03 80  F0 FF FF 7F F0 FF FF 7F  ....+E..........
00C0: 73 30 38 32 04 80 27 65  47 70 0E 01 05 2A 65 47  s082..'eGp...*eG
00D0: 70 0E 01 55 03 80 F0 FF  FF 7F F0 FF FF 7F 73 30  p..U..........s0
00E0: 38 32 1C 08 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  82...E..........
00F0: 73 30 38 33 04 80 27 65  47 70 0E 01 06 2A 65 47  s083..'eGp...*eG
0100: 70 0E 01 1C 08 80 27 65  47 70 0E 01 07 2A 65 47  p.....'eGp...*eG
0110: 70 0E 01 1C 08 80 45 03  80 F0 FF FF 7F F0 FF FF  p.....E.........
0120: 7F 73 30 38 34 04 80 27  65 47 70 0E 01 08 2A 65  .s084..'eGp...*e
0130: 47 70 0E 01 1C 08 80 45  03 80 F0 FF FF 7F F0 FF  Gp.....E........
0140: FF 7F 73 30 38 35 04 80  27 65 47 70 0E 01 09 2A  ..s085..'eGp...*
0150: 65 47 70 0E 01 1C 08 80  27 65 47 70 0E 01 0A 2A  eGp.....'eGp...*
0160: 65 47 70 0E 01 1C 08 80  45 03 80 F0 FF FF 7F F0  eGp.....E.......
0170: FF FF 7F 73 30 38 36 04  80 27 65 47 70 0E 01 0B  ...s086..'eGp...
0180: 2A 65 47 70 0E 01 1C 08  80 27 65 47 70 0E 01 0C  *eGp.....'eGp...
0190: 2A 65 47 70 0E 01 1C 08  80 27 65 47 70 0E 01 0D  *eGp.....'eGp...
01A0: 2A 65 47 70 0E 01 1C 08  80 27 67 F0 FF FF 7F 2B  *eGp.....'g....+
01B0: 1C 08 80 45 03 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...E..........s0
01C0: 38 37 04 80 1C 08 80 27  65 47 70 0E 01 0E 2A 65  87.....'eGp...*e
01D0: 47 70 0E 01 02 00 00 09  80 00 DF 01 1A CC 03 29  Gp.............)
01E0: 05 47 70 0E 01 0F 1C 08  80 27 66 97 70 0E 01 02  .Gp......'f.p...
01F0: 1C 08 80 27 67 F0 FF FF  7F 2B 27 65 47 70 0E 01  ...'g....+'eGp..
0200: 10 2A 66 97 70 0E 01 45  05 80 F0 FF FF 7F F0 FF  .*f.p..E........
0210: FF 7F 66 64 6F 31 04 80  1C 02 80 1C 02 80 46 00  ..fdo1........F.
0220: 1C 05 80 45 05 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0230: 69 31 04 80 21 00 27 05  40 70 0E 01 11 6E F0 FF  i1..!.'.@p...n..
0240: FF 7F 0A 80 99 F0 FF FF  7F 1C 0B 80 2A 05 40 70  ............*.@p
0250: 0E 01 52 03 80 F0 FF FF  7F F0 FF FF 7F 73 30 33  ..R..........s03
0260: 32 45 0C 80 F8 FF FF 7F  F8 FF FF 7F 73 30 35 39  2E..........s059
0270: 04 80 4A 40 70 0E 01 F0  FF FF 7F 1C 08 80 2B 40  ..J@p.........+@
0280: 70 0E 01 0D 80 23 45 05  80 F0 FF FF 7F F0 FF FF  p....#E.........
0290: 7F 66 64 6F 31 04 80 55  05 80 F0 FF FF 7F F0 FF  .fdo1..U........
02A0: FF 7F 66 64 6F 31 52 0C  80 F8 FF FF 7F F8 FF FF  ..fdo1R.........
02B0: 7F 73 30 35 39 BA F0 FF  FF 7F 0E 80 0F 80 10 80  .s059...........
02C0: 11 80 80 F0 FF FF 7F 4A  F0 FF FF 7F 40 70 0E 01  .......J....@p..
02D0: 4A 40 70 0E 01 F0 FF FF  7F 1C 02 80 48 12 80 1C  J@p.........H...
02E0: 13 80 45 0C 80 F8 FF FF  7F F8 FF FF 7F 73 30 36  ..E..........s06
02F0: 30 04 80 1C 14 80 45 05  80 F0 FF FF 7F F0 FF FF  0.....E.........
0300: 7F 66 64 69 31 04 80 5B  15 80 40 70 0E 01 40 70  .fdi1..[..@p..@p
0310: 0E 01 79 65 73 30 2B 40  70 0E 01 16 80 23 5B 17  ..yes0+@p....#[.
0320: 80 40 70 0E 01 40 70 0E  01 74 6C 34 30 2B 40 70  .@p..@p..tl40+@p
0330: 0E 01 18 80 23 52 0C 80  F8 FF FF 7F F8 FF FF 7F  ....#R..........
0340: 73 30 36 30 45 0C 80 F8  FF FF 7F F8 FF FF 7F 73  s060E..........s
0350: 30 36 31 04 80 2B 40 70  0E 01 19 80 23 2B 40 70  061..+@p....#+@p
0360: 0E 01 1A 80 23 52 0C 80  F8 FF FF 7F F8 FF FF 7F  ....#R..........
0370: 73 30 36 31 45 0C 80 F8  FF FF 7F F8 FF FF 7F 73  s061E..........s
0380: 30 36 32 04 80 5B 17 80  40 70 0E 01 40 70 0E 01  062..[..@p..@p..
0390: 74 6C 34 31 2B 40 70 0E  01 1B 80 23 6E F0 FF FF  tl41+@p....#n...
03A0: 7F 1C 80 99 F0 FF FF 7F  1C 0B 80 52 0C 80 F8 FF  ...........R....
03B0: FF 7F F8 FF FF 7F 73 30  36 32 45 0C 80 F8 FF FF  ......s062E.....
03C0: 7F F8 FF FF 7F 73 30 36  33 04 80 1B 27 05 47 70  .....s063...'.Gp
03D0: 0E 01 11 6E F0 FF FF 7F  0A 80 99 F0 FF FF 7F 1C  ...n............
03E0: 0B 80 2A 05 47 70 0E 01  52 03 80 F0 FF FF 7F F0  ..*.Gp..R.......
03F0: FF FF 7F 73 30 38 37 45  0C 80 F8 FF FF 7F F8 FF  ...s087E........
0400: FF 7F 73 30 36 34 04 80  4A 47 70 0E 01 F0 FF FF  ..s064..JGp.....
0410: 7F 1C 08 80 2B 47 70 0E  01 0D 80 23 45 05 80 F0  ....+Gp....#E...
0420: FF FF 7F F0 FF FF 7F 66  64 6F 31 04 80 55 05 80  .......fdo1..U..
0430: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 52 0C 80 F8  ........fdo1R...
0440: FF FF 7F F8 FF FF 7F 73  30 36 34 BA F0 FF FF 7F  .......s064.....
0450: 1D 80 1E 80 10 80 1F 80  80 F0 FF FF 7F 4A F0 FF  .............J..
0460: FF 7F 47 70 0E 01 4A 47  70 0E 01 F0 FF FF 7F 1C  ..Gp..JGp.......
0470: 02 80 48 12 80 1C 13 80  45 0C 80 F8 FF FF 7F F8  ..H.....E.......
0480: FF FF 7F 73 30 36 35 04  80 1C 14 80 45 05 80 F0  ...s065.....E...
0490: FF FF 7F F0 FF FF 7F 66  64 69 31 04 80 5B 15 80  .......fdi1..[..
04A0: 47 70 0E 01 47 70 0E 01  79 65 73 30 2B 47 70 0E  Gp..Gp..yes0+Gp.
04B0: 01 16 80 23 5B 17 80 47  70 0E 01 47 70 0E 01 74  ...#[..Gp..Gp..t
04C0: 6C 34 30 2B 47 70 0E 01  18 80 23 52 0C 80 F8 FF  l40+Gp....#R....
04D0: FF 7F F8 FF FF 7F 73 30  36 35 45 0C 80 F8 FF FF  ......s065E.....
04E0: 7F F8 FF FF 7F 73 30 36  36 04 80 2B 47 70 0E 01  .....s066..+Gp..
04F0: 19 80 23 2B 47 70 0E 01  1A 80 23 52 0C 80 F8 FF  ..#+Gp....#R....
0500: FF 7F F8 FF FF 7F 73 30  36 36 45 0C 80 F8 FF FF  ......s066E.....
0510: 7F F8 FF FF 7F 73 30 36  37 04 80 5B 17 80 47 70  .....s067..[..Gp
0520: 0E 01 47 70 0E 01 74 6C  34 31 2B 47 70 0E 01 1B  ..Gp..tl41+Gp...
0530: 80 23 6E F0 FF FF 7F 1C  80 99 F0 FF FF 7F 1C 0B  .#n.............
0540: 80 52 0C 80 F8 FF FF 7F  F8 FF FF 7F 73 30 36 37  .R..........s067
0550: 45 0C 80 F8 FF FF 7F F8  FF FF 7F 73 30 36 38 04  E..........s068.
0560: 80 1B                                             ..              
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[9]
  2: 0x0007 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0009 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  4: 0x000C [0x75] LOAD_ROOM(Load indoor room, room=356*)
  5: 0x0010 [0x75] LOAD_ROOM(No action)
  6: 0x0012 [0x80] LOAD_WAIT(entity=EventEntity)
  7: 0x0017 [0x1C] WAIT(60* ticks)
  8: 0x001A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s080" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
  9: 0x002B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x003C [0x27] REQ_SET(priority=0x64, entity_id=LocalPlayer, tag_num=0x27)
 11: 0x0043 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x02)
 12: 0x004A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 14: 0x006A [0x1D] PRINT_EVENT_MESSAGE(message_id=11461*)
    → "You've come on orders from the homeland, have you? You should speak with Consul Kasaroro."
 15: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x006E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 17: 0x0073 [0x1C] WAIT(60* ticks)
 18: 0x0076 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s081" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 19: 0x0087 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x03)
 20: 0x008E [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 21: 0x0094 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x04)
 22: 0x009B [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 23: 0x00A1 [0x1C] WAIT(30* ticks)
 24: 0x00A4 [0x79] LocalPlayer looks at Lion (ID: 17723463/0x010E7047) (Basic look)
 25: 0x00AE [0x27] REQ_SET(priority=0x67, entity_id=LocalPlayer, tag_num=0x2B)
 26: 0x00B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s082" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 27: 0x00C6 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x05)
 28: 0x00CD [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 29: 0x00D3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s082" with entities [LocalPlayer, LocalPlayer], work=131*
 30: 0x00E2 [0x1C] WAIT(30* ticks)
 31: 0x00E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s083" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 32: 0x00F6 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x06)
 33: 0x00FD [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 34: 0x0103 [0x1C] WAIT(30* ticks)
 35: 0x0106 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x07)
 36: 0x010D [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 37: 0x0113 [0x1C] WAIT(30* ticks)
 38: 0x0116 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s084" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 39: 0x0127 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x08)
 40: 0x012E [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 41: 0x0134 [0x1C] WAIT(30* ticks)
 42: 0x0137 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s085" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 43: 0x0148 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x09)
 44: 0x014F [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 45: 0x0155 [0x1C] WAIT(30* ticks)
 46: 0x0158 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x0A)
 47: 0x015F [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 48: 0x0165 [0x1C] WAIT(30* ticks)
 49: 0x0168 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s086" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 50: 0x0179 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x0B)
 51: 0x0180 [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 52: 0x0186 [0x1C] WAIT(30* ticks)
 53: 0x0189 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x0C)
 54: 0x0190 [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 55: 0x0196 [0x1C] WAIT(30* ticks)
 56: 0x0199 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x0D)
 57: 0x01A0 [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 58: 0x01A6 [0x1C] WAIT(30* ticks)
 59: 0x01A9 [0x27] REQ_SET(priority=0x67, entity_id=LocalPlayer, tag_num=0x2B)
 60: 0x01B0 [0x1C] WAIT(30* ticks)
 61: 0x01B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s087" with entities [LocalPlayer, LocalPlayer], work=[131*, 0*]
 62: 0x01C4 [0x1C] WAIT(30* ticks)
 63: 0x01C7 [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x0E)
 64: 0x01CE [0x2A] GET_REQ_LEVEL(level=101, entity_id=Lion (ID: 17723463/0x010E7047))
 65: 0x01D4 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x01DF
 66: 0x01DC [0x1A] CALL_SUBROUTINE(address=0x03CC)
 67: 0x01DF [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x0F)
 68: 0x01E6 [0x1C] WAIT(30* ticks)
 69: 0x01E9 [0x27] REQ_SET(priority=0x66, entity_id=Door:Windurstian Consul (ID: 17723543/0x010E7097), tag_num=0x02)
 70: 0x01F0 [0x1C] WAIT(30* ticks)
 71: 0x01F3 [0x27] REQ_SET(priority=0x67, entity_id=LocalPlayer, tag_num=0x2B)
 72: 0x01FA [0x27] REQ_SET(priority=0x65, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x10)
 73: 0x0201 [0x2A] GET_REQ_LEVEL(level=102, entity_id=Door:Windurstian Consul (ID: 17723543/0x010E7097))
 74: 0x0207 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 75: 0x0218 [0x1C] WAIT(60* ticks)
 76: 0x021B [0x1C] WAIT(60* ticks)
 77: 0x021E [0x46] CAMERA_CONTROL: Restore default settings
 78: 0x0220 [0x1C] WAIT(200* ticks)
 79: 0x0223 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 80: 0x0234 [0x21] END_EVENT
 81: 0x0235 [0x00] END_REQSTACK()

SUBROUTINE_03CC:
 82: 0x03CC [0x27] REQ_SET(priority=0x05, entity_id=Lion (ID: 17723463/0x010E7047), tag_num=0x11)
 83: 0x03D3 [0x6E] LocalPlayer uses emote 16*
 84: 0x03DA [0x99] Wait for LocalPlayer animation to complete
 85: 0x03DF [0x1C] WAIT(90* ticks)
 86: 0x03E2 [0x2A] GET_REQ_LEVEL(level=5, entity_id=Lion (ID: 17723463/0x010E7047))
 87: 0x03E8 [0x52] END_LOAD_SCHEDULER: End scheduler "s087" with entities [LocalPlayer, LocalPlayer], work=131*
 88: 0x03F7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s064" with entities [EventEntity, EventEntity], work=[762*, 0*]
 89: 0x0408 [0x4A] Lion (ID: 17723463/0x010E7047) looks at LocalPlayer
 90: 0x0411 [0x1C] WAIT(30* ticks)
 91: 0x0414 [0x2B] Lion (ID: 17723463/0x010E7047) [18728*]:
    → "There's something else?"
 92: 0x041B [0x23] WAIT_FOR_DIALOG_INTERACTION
 93: 0x041C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 94: 0x042D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 95: 0x043C [0x52] END_LOAD_SCHEDULER: End scheduler "s064" with entities [EventEntity, EventEntity], work=762*
 96: 0x044B [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-51.509*, pos_z=36.075*, pos_y=-2.000*, direction=31.2°*)
 97: 0x0458 [0x80] LOAD_WAIT(entity=LocalPlayer)
 98: 0x045D [0x4A] LocalPlayer looks at Lion (ID: 17723463/0x010E7047)
 99: 0x0466 [0x4A] Lion (ID: 17723463/0x010E7047) looks at LocalPlayer
100: 0x046F [0x1C] WAIT(60* ticks)
101: 0x0472 [0x48] [System] [18742*]:
    → "@@"
102: 0x0475 [0x1C] WAIT(120* ticks)
103: 0x0478 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s065" with entities [EventEntity, EventEntity], work=[762*, 0*]
104: 0x0489 [0x1C] WAIT(15* ticks)
105: 0x048C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
106: 0x049D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes0" with entities [Lion (ID: 17723463/0x010E7047), Lion (ID: 17723463/0x010E7047)], work=99*
107: 0x04AC [0x2B] Lion (ID: 17723463/0x010E7047) [18729*]:
    → "You say my father told you to seek me out?"
108: 0x04B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
109: 0x04B4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl40" with entities [Lion (ID: 17723463/0x010E7047), Lion (ID: 17723463/0x010E7047)], work=538*
110: 0x04C3 [0x2B] Lion (ID: 17723463/0x010E7047) [18730*]:
    → "I've been trying to figure out as much as I can about the strange portals that link our Vana'diel to another dimension."
111: 0x04CA [0x23] WAIT_FOR_DIALOG_INTERACTION
112: 0x04CB [0x52] END_LOAD_SCHEDULER: End scheduler "s065" with entities [EventEntity, EventEntity], work=762*
113: 0x04DA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s066" with entities [EventEntity, EventEntity], work=[762*, 0*]
114: 0x04EB [0x2B] Lion (ID: 17723463/0x010E7047) [18731*]:
    → "But we've got other problems to deal with first. Let's worry about it once we've finished our current mission."
115: 0x04F2 [0x23] WAIT_FOR_DIALOG_INTERACTION
116: 0x04F3 [0x2B] Lion (ID: 17723463/0x010E7047) [18732*]:
    → "I'll meet you at the Crag of Holla in La Theine Plateau once we've got that burden off our shoulders. Or we could catch up at Dem or Mea, if that's preferable to you."
117: 0x04FA [0x23] WAIT_FOR_DIALOG_INTERACTION
118: 0x04FB [0x52] END_LOAD_SCHEDULER: End scheduler "s066" with entities [EventEntity, EventEntity], work=762*
119: 0x050A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s067" with entities [EventEntity, EventEntity], work=[762*, 0*]
120: 0x051B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl41" with entities [Lion (ID: 17723463/0x010E7047), Lion (ID: 17723463/0x010E7047)], work=538*
121: 0x052A [0x2B] Lion (ID: 17723463/0x010E7047) [18733*]:
    → "Remember to see the missions posed to you by your home nation to completion first, though."
122: 0x0531 [0x23] WAIT_FOR_DIALOG_INTERACTION
123: 0x0532 [0x6E] LocalPlayer uses emote 7*
124: 0x0539 [0x99] Wait for LocalPlayer animation to complete
125: 0x053E [0x1C] WAIT(90* ticks)
126: 0x0541 [0x52] END_LOAD_SCHEDULER: End scheduler "s067" with entities [EventEntity, EventEntity], work=762*
127: 0x0550 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s068" with entities [EventEntity, EventEntity], work=[762*, 0*]
128: 0x0561 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0236 [0x27] REQ_SET(priority=0x05, entity_id=Lion (ID: 17723456/0x010E7040), tag_num=0x11)
     0x023D [0x6E] LocalPlayer uses emote 16*
     0x0244 [0x99] Wait for LocalPlayer animation to complete
     0x0249 [0x1C] WAIT(90* ticks)
     0x024C [0x2A] GET_REQ_LEVEL(level=5, entity_id=Lion (ID: 17723456/0x010E7040))
     0x0252 [0x52] END_LOAD_SCHEDULER: End scheduler "s032" with entities [LocalPlayer, LocalPlayer], work=131*
     0x0261 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s059" with entities [EventEntity, EventEntity], work=[762*, 0*]
     0x0272 [0x4A] Lion (ID: 17723456/0x010E7040) looks at LocalPlayer
     0x027B [0x1C] WAIT(30* ticks)
     0x027E [0x2B] Lion (ID: 17723456/0x010E7040) [18728*]:
    → "There's something else?"
     0x0285 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0286 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0297 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x02A6 [0x52] END_LOAD_SCHEDULER: End scheduler "s059" with entities [EventEntity, EventEntity], work=762*
     0x02B5 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=36.638*, pos_z=-2.255*, pos_y=-2.000*, direction=268.0°*)
     0x02C2 [0x80] LOAD_WAIT(entity=LocalPlayer)
     0x02C7 [0x4A] LocalPlayer looks at Lion (ID: 17723456/0x010E7040)
     0x02D0 [0x4A] Lion (ID: 17723456/0x010E7040) looks at LocalPlayer
     0x02D9 [0x1C] WAIT(60* ticks)
     0x02DC [0x48] [System] [18742*]:
    → "@@"
     0x02DF [0x1C] WAIT(120* ticks)
     0x02E2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s060" with entities [EventEntity, EventEntity], work=[762*, 0*]
     0x02F3 [0x1C] WAIT(15* ticks)
     0x02F6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0307 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes0" with entities [Lion (ID: 17723456/0x010E7040), Lion (ID: 17723456/0x010E7040)], work=99*
     0x0316 [0x2B] Lion (ID: 17723456/0x010E7040) [18729*]:
    → "You say my father told you to seek me out?"
     0x031D [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x031E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl40" with entities [Lion (ID: 17723456/0x010E7040), Lion (ID: 17723456/0x010E7040)], work=538*
     0x032D [0x2B] Lion (ID: 17723456/0x010E7040) [18730*]:
    → "I've been trying to figure out as much as I can about the strange portals that link our Vana'diel to another dimension."
     0x0334 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0335 [0x52] END_LOAD_SCHEDULER: End scheduler "s060" with entities [EventEntity, EventEntity], work=762*
     0x0344 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s061" with entities [EventEntity, EventEntity], work=[762*, 0*]
     0x0355 [0x2B] Lion (ID: 17723456/0x010E7040) [18731*]:
    → "But we've got other problems to deal with first. Let's worry about it once we've finished our current mission."
     0x035C [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x035D [0x2B] Lion (ID: 17723456/0x010E7040) [18732*]:
    → "I'll meet you at the Crag of Holla in La Theine Plateau once we've got that burden off our shoulders. Or we could catch up at Dem or Mea, if that's preferable to you."
     0x0364 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0365 [0x52] END_LOAD_SCHEDULER: End scheduler "s061" with entities [EventEntity, EventEntity], work=762*
     0x0374 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s062" with entities [EventEntity, EventEntity], work=[762*, 0*]
     0x0385 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tl41" with entities [Lion (ID: 17723456/0x010E7040), Lion (ID: 17723456/0x010E7040)], work=538*
     0x0394 [0x2B] Lion (ID: 17723456/0x010E7040) [18733*]:
    → "Remember to see the missions posed to you by your home nation to completion first, though."
     0x039B [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x039C [0x6E] LocalPlayer uses emote 7*
     0x03A3 [0x99] Wait for LocalPlayer animation to complete
     0x03A8 [0x1C] WAIT(90* ticks)
     0x03AB [0x52] END_LOAD_SCHEDULER: End scheduler "s062" with entities [EventEntity, EventEntity], work=762*
     0x03BA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s063" with entities [EventEntity, EventEntity], work=[762*, 0*]
     0x03CB [0x1B] RETURN
```

### Event 554

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0562   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0560:       1E F0 FF FF 7F 6F  70 66 06 80 F8 FF FF 7F    .....opf......
0570: F8 FF FF 7F 74 6C 6B 30  1D 20 80 23 5E 69 64 6C  ....tlk0. .#^idl
0580: 30 1C 08 80 21 00                                 0...!.          
```

#### Opcodes

```
  0: 0x0562 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0567 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0568 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0569 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0578 [0x1D] PRINT_EVENT_MESSAGE(message_id=11457*)
    → "If it's the consul you're a-seeking, she's inside!"
  5: 0x057B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x057C [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0581 [0x1C] WAIT(30* ticks)
  8: 0x0584 [0x21] END_EVENT
  9: 0x0585 [0x00] END_REQSTACK()
```

### Event 577

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0586   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0580:                   1E F0  FF FF 7F 6F 70 66 06 80        .....opf..
0590: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 21 80 23  ........tlk0.!.#
05A0: 5E 69 64 6C 30 1C 08 80  21 00                    ^idl0...!.      
```

#### Opcodes

```
  0: 0x0586 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x058B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x058C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x058D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x059C [0x1D] PRINT_EVENT_MESSAGE(message_id=11458*)
    → "A San d'Orian, are you? This is the Consulate of Windurst. We provide all sorts of aid to our countrymen here."
  5: 0x059F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x05A0 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x05A5 [0x1C] WAIT(30* ticks)
  8: 0x05A8 [0x21] END_EVENT
  9: 0x05A9 [0x00] END_REQSTACK()
```

### Event 578

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x05AA   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
05A0:                                1E F0 FF FF 7F 6F            .....o
05B0: 70 66 06 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  pf..........tlk0
05C0: 1D 22 80 23 5E 69 64 6C  30 1C 08 80 21 00        .".#^idl0...!.  
```

#### Opcodes

```
  0: 0x05AA [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x05AF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x05B0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x05B1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x05C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=11459*)
    → "A Bastoker, are you? This is the Consulate of Windurst. If you're looking for your consulate, it's out the door and across the way."
  5: 0x05C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x05C4 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x05C9 [0x1C] WAIT(30* ticks)
  8: 0x05CC [0x21] END_EVENT
  9: 0x05CD [0x00] END_REQSTACK()
```
