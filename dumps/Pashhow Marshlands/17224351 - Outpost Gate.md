# 17224351 - Outpost Gate

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Pashhow Marshlands (ID: 109) |
| Block Size       | 2288 bytes                   |
| Total Events     | 3                            |
| References Count | 48                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [21](#event-21)       | 0x0001       |    549 |             84 |
| [22](#event-22)       | 0x0226       |   1517 |            195 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0013      |          19 |
|       1 | 0x000F      |          15 |
|       2 | 0x007F      |         127 |
|       3 | 0x00B0      |         176 |
|       4 | 0x0000      |           0 |
|       5 | 0x0006      |           6 |
|       6 | 0x20C5      |        8389 |
|       7 | 0x0001      |           1 |
|       8 | 0x20C6      |        8390 |
|       9 | 0x20C7      |        8391 |
|      10 | 0x002D      |          45 |
|      11 | 0x0009      |           9 |
|      12 | 0x20C8      |        8392 |
|      13 | 0x20C9      |        8393 |
|      14 | 0x003C      |          60 |
|      15 | 0x001A      |          26 |
|      16 | 0x20CA      |        8394 |
|      17 | 0x20CB      |        8395 |
|      18 | 0x20CC      |        8396 |
|      19 | 0x001E      |          30 |
|      20 | 0x0065      |         101 |
|      21 | 0x0067      |         103 |
|      22 | 0x00C8      |         200 |
|      23 | 0x20CD      |        8397 |
|      24 | 0x20CE      |        8398 |
|      25 | 0x20CF      |        8399 |
|      26 | 0x20D0      |        8400 |
|      27 | 0x0080      |         128 |
|      28 | 0x20D1      |        8401 |
|      29 | 0x00B3      |         179 |
|      30 | 0x20D2      |        8402 |
|      31 | 0x00B4      |         180 |
|      32 | 0x00EA      |         234 |
|      33 | 0x0105      |         261 |
|      34 | 0x0003      |           3 |
|      35 | 0x20D3      |        8403 |
|      36 | 0x20D4      |        8404 |
|      37 | 0x006D      |         109 |
|      38 | 0x20D5      |        8405 |
|      39 | 0x20D6      |        8406 |
|      40 | 0x20D7      |        8407 |
|      41 | 0x20D8      |        8408 |
|      42 | 0x20D9      |        8409 |
|      43 | 0x0004      |           4 |
|      44 | 0x20DA      |        8410 |
|      45 | 0x00C9      |         201 |
|      46 | 0x0002      |           2 |
|      47 | 0x00D7      |         215 |

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

### Event 21

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 549 bytes |
| Instructions | 84        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 00 00 03 10 03  01 00 09 10 1A E5 05 46   B.............F
0010: 01 38 00 80 1C 01 80 5C  00 02 80 5C 01 02 80 5C  .8.....\...\...\
0020: 02 02 80 5C 03 02 80 9A  27 10 A0 D2 06 01 03 92  ...\....'.......
0030: 01 A0 D2 06 01 27 10 F0  FF FF 7F 09 27 10 A0 D2  .....'......'...
0040: 06 01 04 94 01 A0 D2 06  01 1C 01 80 79 00 F0 FF  ............y...
0050: FF 7F A0 D2 06 01 27 10  A0 D2 06 01 05 45 03 80  ......'......E..
0060: F0 FF FF 7F F0 FF FF 7F  6F 72 30 30 04 80 1A C4  ........or00....
0070: 05 2A 10 A0 D2 06 01 1C  05 80 66 04 80 A0 D2 06  .*........f.....
0080: 01 A0 D2 06 01 64 69 73  30 2B A0 D2 06 01 06 80  .....dis0+......
0090: 23 52 03 80 F0 FF FF 7F  F0 FF FF 7F 6F 72 30 30  #R..........or00
00A0: 45 03 80 F0 FF FF 7F F0  FF FF 7F 6F 72 30 31 04  E..........or01.
00B0: 80 02 01 00 07 80 00 C4  00 2B A0 D2 06 01 08 80  .........+......
00C0: 23 01 CC 00 2B A0 D2 06  01 09 80 23 1A E5 05 1C  #...+......#....
00D0: 0A 80 7B A0 D2 06 01 27  10 F0 FF FF 7F 0A 27 10  ..{....'......'.
00E0: A0 D2 06 01 06 66 0B 80  A0 D2 06 01 A0 D2 06 01  .....f..........
00F0: 73 69 74 6C 1C 01 80 52  03 80 F0 FF FF 7F F0 FF  sitl...R........
0100: FF 7F 6F 72 30 31 45 03  80 F0 FF FF 7F F0 FF FF  ..or01E.........
0110: 7F 6F 72 30 32 04 80 1A  C4 05 2B A0 D2 06 01 0C  .or02.....+.....
0120: 80 23 52 03 80 F0 FF FF  7F F0 FF FF 7F 6F 72 30  .#R..........or0
0130: 32 45 03 80 F0 FF FF 7F  F0 FF FF 7F 6F 72 30 33  2E..........or03
0140: 04 80 2B A0 D2 06 01 0D  80 23 66 0B 80 A0 D2 06  ..+......#f.....
0150: 01 A0 D2 06 01 73 69 74  31 1C 0E 80 79 00 A0 D2  .....sit1...y...
0160: 06 01 F0 FF FF 7F 52 03  80 F0 FF FF 7F F0 FF FF  ......R.........
0170: 7F 6F 72 30 33 45 03 80  F0 FF FF 7F F0 FF FF 7F  .or03E..........
0180: 6F 72 30 34 04 80 1C 0E  80 6E A0 D2 06 01 0F 80  or04.....n......
0190: 99 A0 D2 06 01 99 A0 D2  06 01 2B A0 D2 06 01 10  ..........+.....
01A0: 80 23 29 10 A0 D2 06 01  07 27 10 A0 D2 06 01 08  .#)......'......
01B0: 03 03 10 00 00 2B A0 D2  06 01 11 80 23 2A 10 A0  .....+......#*..
01C0: D2 06 01 52 03 80 F0 FF  FF 7F F0 FF FF 7F 6F 72  ...R..........or
01D0: 30 34 45 03 80 F0 FF FF  7F F0 FF FF 7F 6F 72 30  04E..........or0
01E0: 35 04 80 66 0B 80 A0 D2  06 01 A0 D2 06 01 74 77  5..f..........tw
01F0: 62 30 2B A0 D2 06 01 12  80 23 1A E5 05 1C 13 80  b0+......#......
0200: 5C 00 04 80 5C 01 04 80  5C 02 14 80 5C 03 15 80  \...\...\...\...
0210: 9A 46 00 45 16 80 F0 FF  FF 7F F0 FF FF 7F 66 64  .F.E..........fd
0220: 69 32 04 80 21 00                                 i2..!.          
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[9]
  3: 0x000C [0x1A] CALL_SUBROUTINE(address=0x05E5)
  4: 0x000F [0x46] CAMERA_CONTROL: Disable user control
  5: 0x0011 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x0014 [0x1C] WAIT(15* ticks)
  7: 0x0017 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 127*
  8: 0x001B [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 127*
  9: 0x001F [0x5C] MUSIC_CONTROL: Set Combat (Solo) music to song 127*
 10: 0x0023 [0x5C] MUSIC_CONTROL: Set Combat (Party) music to song 127*
 11: 0x0027 [0x9A] WAIT_MUSIC_SERVER()
 12: 0x0028 [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x03)
 13: 0x002F [0x92] Ulzana (ID: 17224352/0x0106D2A0)->Render.Flags3 ^= 0x01
 14: 0x0035 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x09)
 15: 0x003C [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x04)
 16: 0x0043 [0x94] Ulzana (ID: 17224352/0x0106D2A0)->Render.Flags3 ^= 0x01
 17: 0x0049 [0x1C] WAIT(15* ticks)
 18: 0x004C [0x79] LocalPlayer looks at Ulzana (ID: 17224352/0x0106D2A0) (Basic look)
 19: 0x0056 [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x05)
 20: 0x005D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or00" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 21: 0x006E [0x1A] CALL_SUBROUTINE(address=0x05C4)
 22: 0x0071 [0x2A] GET_REQ_LEVEL(level=16, entity_id=Ulzana (ID: 17224352/0x0106D2A0))
 23: 0x0077 [0x1C] WAIT(6* ticks)
 24: 0x007A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [Ulzana (ID: 17224352/0x0106D2A0), Ulzana (ID: 17224352/0x0106D2A0)], work=0*
 25: 0x0089 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8389*]:
    → "Whaddaya want? I got no time for adventurers."
 26: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0091 [0x52] END_LOAD_SCHEDULER: End scheduler "or00" with entities [LocalPlayer, LocalPlayer], work=176*
 28: 0x00A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or01" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 29: 0x00B1 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x00C4
 30: 0x00B9 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8390*]:
    → "Huh? Where'd you hear... Well, whatever."
 31: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x00C1 [0x01] GOTO 0x00CC
 33: 0x00C4 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8391*]:
    → "You say you got business with me?"
 34: 0x00CB [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00CC:
 35: 0x00CC [0x1A] CALL_SUBROUTINE(address=0x05E5)
 36: 0x00CF [0x1C] WAIT(45* ticks)
 37: 0x00D2 [0x7B] Ulzana (ID: 17224352/0x0106D2A0) stops talking
 38: 0x00D7 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x0A)
 39: 0x00DE [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x06)
 40: 0x00E5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sitl" with entities [Ulzana (ID: 17224352/0x0106D2A0), Ulzana (ID: 17224352/0x0106D2A0)], work=9*
 41: 0x00F4 [0x1C] WAIT(15* ticks)
 42: 0x00F7 [0x52] END_LOAD_SCHEDULER: End scheduler "or01" with entities [LocalPlayer, LocalPlayer], work=176*
 43: 0x0106 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or02" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 44: 0x0117 [0x1A] CALL_SUBROUTINE(address=0x05C4)
 45: 0x011A [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8392*]:
    → "Silver Comet... What the hell are you bothering me about that old chocobo story for? You some kind of crackpot?"
 46: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x0122 [0x52] END_LOAD_SCHEDULER: End scheduler "or02" with entities [LocalPlayer, LocalPlayer], work=176*
 48: 0x0131 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or03" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 49: 0x0142 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8393*]:
    → "Leave me alone, you loon."
 50: 0x0149 [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x014A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit1" with entities [Ulzana (ID: 17224352/0x0106D2A0), Ulzana (ID: 17224352/0x0106D2A0)], work=9*
 52: 0x0159 [0x1C] WAIT(60* ticks)
 53: 0x015C [0x79] Ulzana (ID: 17224352/0x0106D2A0) looks at LocalPlayer (Basic look)
 54: 0x0166 [0x52] END_LOAD_SCHEDULER: End scheduler "or03" with entities [LocalPlayer, LocalPlayer], work=176*
 55: 0x0175 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or04" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 56: 0x0186 [0x1C] WAIT(60* ticks)
 57: 0x0189 [0x6E] Ulzana (ID: 17224352/0x0106D2A0) uses emote 26*
 58: 0x0190 [0x99] Wait for Ulzana (ID: 17224352/0x0106D2A0) animation to complete
 59: 0x0195 [0x99] Wait for Ulzana (ID: 17224352/0x0106D2A0) animation to complete
 60: 0x019A [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8394*]:
    → "Can't you see I'm busy? This place gets too wet and too dark too quick to be wasting time chatting."
 61: 0x01A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x01A2 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x07)
 63: 0x01A9 [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x08)
 64: 0x01B0 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
 65: 0x01B5 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8395*]:
    → "Hold up a minute. If you bring me some $1, I might be willing to give you the time of day."
 66: 0x01BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 67: 0x01BD [0x2A] GET_REQ_LEVEL(level=16, entity_id=Ulzana (ID: 17224352/0x0106D2A0))
 68: 0x01C3 [0x52] END_LOAD_SCHEDULER: End scheduler "or04" with entities [LocalPlayer, LocalPlayer], work=176*
 69: 0x01D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or05" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 70: 0x01E3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twb0" with entities [Ulzana (ID: 17224352/0x0106D2A0), Ulzana (ID: 17224352/0x0106D2A0)], work=9*
 71: 0x01F2 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8396*]:
    → "Yep, three of those ought to do it. I'll give you until the day after tomorrow."
 72: 0x01F9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 73: 0x01FA [0x1A] CALL_SUBROUTINE(address=0x05E5)
 74: 0x01FD [0x1C] WAIT(30* ticks)
 75: 0x0200 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 76: 0x0204 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 77: 0x0208 [0x5C] MUSIC_CONTROL: Set Combat (Solo) music to song 101*
 78: 0x020C [0x5C] MUSIC_CONTROL: Set Combat (Party) music to song 103*
 79: 0x0210 [0x9A] WAIT_MUSIC_SERVER()
 80: 0x0211 [0x46] CAMERA_CONTROL: Restore default settings
 81: 0x0213 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 82: 0x0224 [0x21] END_EVENT
 83: 0x0225 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0226     |
| Data Size    | 1517 bytes |
| Instructions | 140        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                   42 1A  E5 05 46 01 38 00 80 1C        B...F.8...
0230: 01 80 5C 00 02 80 5C 01  02 80 5C 02 02 80 5C 03  ..\...\...\...\.
0240: 02 80 9A 27 10 A0 D2 06  01 03 27 10 A2 D2 06 01  ...'......'.....
0250: 02 92 01 A0 D2 06 01 27  10 F0 FF FF 7F 09 27 10  .......'......'.
0260: A0 D2 06 01 04 94 01 A0  D2 06 01 1C 01 80 79 00  ..............y.
0270: F0 FF FF 7F A0 D2 06 01  27 10 A0 D2 06 01 05 45  ........'......E
0280: 03 80 F0 FF FF 7F F0 FF  FF 7F 6F 72 30 30 04 80  ..........or00..
0290: 1A C4 05 2A 10 A0 D2 06  01 1C 05 80 2B A0 D2 06  ...*........+...
02A0: 01 17 80 23 66 04 80 A0  D2 06 01 A0 D2 06 01 64  ...#f..........d
02B0: 69 73 30 2B A0 D2 06 01  18 80 23 1A E5 05 1C 0A  is0+......#.....
02C0: 80 27 10 F0 FF FF 7F 0B  27 10 A0 D2 06 01 09 66  .'......'......f
02D0: 04 80 A0 D2 06 01 A0 D2  06 01 74 6C 6B 31 1C 01  ..........tlk1..
02E0: 80 52 03 80 F0 FF FF 7F  F0 FF FF 7F 6F 72 30 30  .R..........or00
02F0: 45 03 80 F0 FF FF 7F F0  FF FF 7F 6F 72 31 30 04  E..........or10.
0300: 80 1A C4 05 2B A0 D2 06  01 19 80 23 2B A0 D2 06  ....+......#+...
0310: 01 1A 80 23 1A E5 05 1C  13 80 AB 09 77 07 80 05  ...#........w...
0320: 80 6C F0 FF FF 7F 04 80  07 80 27 10 A0 D2 06 01  .l........'.....
0330: 0A 27 10 A2 D2 06 01 03  66 0B 80 A0 D2 06 01 A0  .'......f.......
0340: D2 06 01 73 68 61 30 1C  13 80 6C A2 D2 06 01 1B  ...sha0...l.....
0350: 80 07 80 2B A0 D2 06 01  1C 80 23 52 03 80 F0 FF  ...+......#R....
0360: FF 7F F0 FF FF 7F 6F 72  31 30 45 03 80 F0 FF FF  ......or10E.....
0370: 7F F0 FF FF 7F 6F 72 31  31 04 80 45 1D 80 F0 FF  .....or11..E....
0380: FF 7F F0 FF FF 7F 65 66  6F 6E 04 80 1C 0E 80 2B  ......efon.....+
0390: A0 D2 06 01 1E 80 27 10  A2 D2 06 01 04 1C 1F 80  ......'.........
03A0: 1A E5 05 1C 13 80 2A 10  A2 D2 06 01 34 20 80 1C  ......*.....4 ..
03B0: 01 80 75 00 21 80 75 01  77 22 80 07 80 1C 01 80  ..u.!.u.w"......
03C0: 27 10 A2 D2 06 01 05 80  A2 D2 06 01 1C 01 80 52  '..............R
03D0: 03 80 F0 FF FF 7F F0 FF  FF 7F 6F 72 31 31 45 03  ..........or11E.
03E0: 80 F0 FF FF 7F F0 FF FF  7F 6F 72 31 32 04 80 45  .........or12..E
03F0: 1D 80 F0 FF FF 7F F0 FF  FF 7F 65 66 6F 6E 04 80  ..........efon..
0400: 2B A0 D2 06 01 23 80 23  2B A0 D2 06 01 24 80 23  +....#.#+....$.#
0410: 1A E5 05 1C 13 80 35 25  80 78 AB 0A 1C 01 80 27  ......5%.x.....'
0420: 10 F0 FF FF 7F 0B 27 10  A0 D2 06 01 09 6C F0 FF  ......'......l..
0430: FF 7F 1B 80 07 80 6C A2  D2 06 01 04 80 07 80 6B  ......l........k
0440: 69 64 6C 30 A0 D2 06 01  80 F0 FF FF 7F 80 A0 D2  idl0............
0450: 06 01 79 00 F0 FF FF 7F  A0 D2 06 01 7B A0 D2 06  ..y.........{...
0460: 01 94 01 A0 D2 06 01 1C  01 80 52 03 80 F0 FF FF  ..........R.....
0470: 7F F0 FF FF 7F 6F 72 31  32 45 03 80 F0 FF FF 7F  .....or12E......
0480: F0 FF FF 7F 6F 72 31 33  04 80 45 16 80 F0 FF FF  ....or13..E.....
0490: 7F F0 FF FF 7F 66 64 69  32 04 80 66 04 80 A0 D2  .....fdi2..f....
04A0: 06 01 A0 D2 06 01 74 68  6B 31 2B A0 D2 06 01 26  ......thk1+....&
04B0: 80 23 2B A0 D2 06 01 27  80 23 66 04 80 A0 D2 06  .#+....'.#f.....
04C0: 01 A0 D2 06 01 74 68 6B  32 1C 0E 80 79 00 A0 D2  .....thk2...y...
04D0: 06 01 F0 FF FF 7F 52 03  80 F0 FF FF 7F F0 FF FF  ......R.........
04E0: 7F 6F 72 31 33 45 03 80  F0 FF FF 7F F0 FF FF 7F  .or13E..........
04F0: 6F 72 31 34 04 80 2B A0  D2 06 01 28 80 23 2B A0  or14..+....(.#+.
0500: D2 06 01 29 80 23 52 03  80 F0 FF FF 7F F0 FF FF  ...).#R.........
0510: 7F 6F 72 31 34 45 03 80  F0 FF FF 7F F0 FF FF 7F  .or14E..........
0520: 6F 72 31 35 04 80 2B A0  D2 06 01 2A 80 23 6E A0  or15..+....*.#n.
0530: D2 06 01 2B 80 99 A0 D2  06 01 99 A0 D2 06 01 2B  ...+...........+
0540: A0 D2 06 01 2C 80 23 1A  E5 05 1C 13 80 52 03 80  ....,.#......R..
0550: F0 FF FF 7F F0 FF FF 7F  6F 72 31 35 5C 00 04 80  ........or15\...
0560: 5C 01 04 80 5C 02 14 80  5C 03 15 80 9A 46 00 45  \...\...\....F.E
0570: 16 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 32 04 80  ..........fdi2..
0580: 21 00 45 16 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  !.E..........fdi
0590: 30 04 80 55 16 80 F0 FF  FF 7F F0 FF FF 7F 66 64  0..U..........fd
05A0: 69 30 1B 45 16 80 F0 FF  FF 7F F0 FF FF 7F 66 64  i0.E..........fd
05B0: 6F 30 04 80 55 16 80 F0  FF FF 7F F0 FF FF 7F 66  o0..U..........f
05C0: 64 6F 30 1B 45 16 80 F0  FF FF 7F F0 FF FF 7F 66  do0.E..........f
05D0: 64 69 31 04 80 55 16 80  F0 FF FF 7F F0 FF FF 7F  di1..U..........
05E0: 66 64 69 31 1B 45 16 80  F0 FF FF 7F F0 FF FF 7F  fdi1.E..........
05F0: 66 64 6F 31 04 80 55 16  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
0600: 7F 66 64 6F 31 1B 45 2D  80 F0 FF FF 7F F0 FF FF  .fdo1.E-........
0610: 7F 77 68 69 31 04 80 55  2D 80 F0 FF FF 7F F0 FF  .whi1..U-.......
0620: FF 7F 77 68 69 31 1B 45  2D 80 F0 FF FF 7F F0 FF  ..whi1.E-.......
0630: FF 7F 77 68 6F 31 04 80  55 2D 80 F0 FF FF 7F F0  ..who1..U-......
0640: FF FF 7F 77 68 6F 31 1B  45 2D 80 F0 FF FF 7F F0  ...who1.E-......
0650: FF FF 7F 77 68 6F 32 04  80 55 2D 80 F0 FF FF 7F  ...who2..U-.....
0660: F0 FF FF 7F 77 68 6F 32  1B 45 2D 80 F0 FF FF 7F  ....who2.E-.....
0670: F0 FF FF 7F 77 68 6F 33  04 80 55 2D 80 F0 FF FF  ....who3..U-....
0680: 7F F0 FF FF 7F 77 68 6F  33 1B 62 07 80 F0 FF FF  .....who3.b.....
0690: 7F F0 FF FF 7F 6D 61 69  6E 04 80 1C 0A 80 45 16  .....main.....E.
06A0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 04 80 55  .........fdo1..U
06B0: 16 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 1B 45  ..........fdo1.E
06C0: 16 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 04 80  ..........fdi1..
06D0: 62 2E 80 F0 FF FF 7F F0  FF FF 7F 6D 61 69 6E 04  b..........main.
06E0: 80 1C 13 80 55 16 80 F0  FF FF 7F F0 FF FF 7F 66  ....U..........f
06F0: 64 69 31 1B 45 16 80 F0  FF FF 7F F0 FF FF 7F 62  di1.E..........b
0700: 6C 6F 6E 04 80 45 2D 80  F0 FF FF 7F F0 FF FF 7F  lon..E-.........
0710: 62 6C 6F 6E 04 80 1B 45  2D 80 F0 FF FF 7F F0 FF  blon...E-.......
0720: FF 7F 77 68 69 30 04 80  55 2D 80 F0 FF FF 7F F0  ..whi0..U-......
0730: FF FF 7F 77 68 69 30 1B  45 2D 80 F0 FF FF 7F F0  ...whi0.E-......
0740: FF FF 7F 77 68 6F 30 04  80 55 2D 80 F0 FF FF 7F  ...who0..U-.....
0750: F0 FF FF 7F 77 68 6F 30  1B 45 2F 80 F0 FF FF 7F  ....who0.E/.....
0760: F0 FF FF 7F 65 66 6F 6E  04 80 55 2F 80 F0 FF FF  ....efon..U/....
0770: 7F F0 FF FF 7F 65 66 6F  6E 1B 45 16 80 F0 FF FF  .....efon.E.....
0780: 7F F0 FF FF 7F 66 64 69  73 04 80 1B 45 16 80 F0  .....fdis...E...
0790: FF FF 7F F0 FF FF 7F 66  64 6F 73 04 80 55 16 80  .......fdos..U..
07A0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 73 1B 45 16 80  ........fdos.E..
07B0: F0 FF FF 7F F0 FF FF 7F  66 64 69 66 04 80 1B 45  ........fdif...E
07C0: 16 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 66 04 80  ..........fdof..
07D0: 55 16 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 66 1B  U..........fdof.
07E0: 45 16 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 70 04  E..........fdip.
07F0: 80 1B 45 16 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0800: 70 04 80 55 16 80 F0 FF  FF 7F F0 FF FF 7F 66 64  p..U..........fd
0810: 6F 70 1B                                          op.             
```

#### Opcodes

```
  0: 0x0226 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0227 [0x1A] CALL_SUBROUTINE(address=0x05E5)
  2: 0x022A [0x46] CAMERA_CONTROL: Disable user control
  3: 0x022C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  4: 0x022F [0x1C] WAIT(15* ticks)
  5: 0x0232 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 127*
  6: 0x0236 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 127*
  7: 0x023A [0x5C] MUSIC_CONTROL: Set Combat (Solo) music to song 127*
  8: 0x023E [0x5C] MUSIC_CONTROL: Set Combat (Party) music to song 127*
  9: 0x0242 [0x9A] WAIT_MUSIC_SERVER()
 10: 0x0243 [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x03)
 11: 0x024A [0x27] REQ_SET(priority=0x10, entity_id=Unnamed NPC (ID: 17224354/0x0106D2A2), tag_num=0x02)
 12: 0x0251 [0x92] Ulzana (ID: 17224352/0x0106D2A0)->Render.Flags3 ^= 0x01
 13: 0x0257 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x09)
 14: 0x025E [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x04)
 15: 0x0265 [0x94] Ulzana (ID: 17224352/0x0106D2A0)->Render.Flags3 ^= 0x01
 16: 0x026B [0x1C] WAIT(15* ticks)
 17: 0x026E [0x79] LocalPlayer looks at Ulzana (ID: 17224352/0x0106D2A0) (Basic look)
 18: 0x0278 [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x05)
 19: 0x027F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or00" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 20: 0x0290 [0x1A] CALL_SUBROUTINE(address=0x05C4)
 21: 0x0293 [0x2A] GET_REQ_LEVEL(level=16, entity_id=Ulzana (ID: 17224352/0x0106D2A0))
 22: 0x0299 [0x1C] WAIT(6* ticks)
 23: 0x029C [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8397*]:
    → "You brought what I asked for? Careful with that stuff, it's powerful smelly."
 24: 0x02A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x02A4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [Ulzana (ID: 17224352/0x0106D2A0), Ulzana (ID: 17224352/0x0106D2A0)], work=0*
 26: 0x02B3 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8398*]:
    → "It's good for hiding a person's scent, you see. Helps me get around."
 27: 0x02BA [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x02BB [0x1A] CALL_SUBROUTINE(address=0x05E5)
 29: 0x02BE [0x1C] WAIT(45* ticks)
 30: 0x02C1 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x0B)
 31: 0x02C8 [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x09)
 32: 0x02CF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Ulzana (ID: 17224352/0x0106D2A0), Ulzana (ID: 17224352/0x0106D2A0)], work=0*
 33: 0x02DE [0x1C] WAIT(15* ticks)
 34: 0x02E1 [0x52] END_LOAD_SCHEDULER: End scheduler "or00" with entities [LocalPlayer, LocalPlayer], work=176*
 35: 0x02F0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or10" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 36: 0x0301 [0x1A] CALL_SUBROUTINE(address=0x05C4)
 37: 0x0304 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8399*]:
    → "Now, then. You wanted to hear about that chocobo, right?"
 38: 0x030B [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x030C [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8400*]:
    → "She was one of the fastest chocobos I've ever ridden, but damn near uncontrollable. I don't know how Silver Comet's owner handled her."
 40: 0x0313 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x0314 [0x1A] CALL_SUBROUTINE(address=0x05E5)
 42: 0x0317 [0x1C] WAIT(30* ticks)
 43: 0x031A [0xAB] EventEntity->UnknownFlag = 1 // Enable unknown flag
 44: 0x031C [0x77] SET_EVENT_TIME_WEATHER(hour=1*, weather=6*)
 45: 0x0321 [0x6C] FADE_ENTITY_COLOR(entity_id=LocalPlayer, end_alpha=0*, fade_time=1*)
 46: 0x032A [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x0A)
 47: 0x0331 [0x27] REQ_SET(priority=0x10, entity_id=Unnamed NPC (ID: 17224354/0x0106D2A2), tag_num=0x03)
 48: 0x0338 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [Ulzana (ID: 17224352/0x0106D2A0), Ulzana (ID: 17224352/0x0106D2A0)], work=9*
 49: 0x0347 [0x1C] WAIT(30* ticks)
 50: 0x034A [0x6C] FADE_ENTITY_COLOR(entity_id=Unnamed NPC (ID: 17224354/0x0106D2A2), end_alpha=128*, fade_time=1*)
 51: 0x0353 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8401*]:
    → "I guess the death of her former owner is what sent her off the edge. That chocobo wasn't right in the head."
 52: 0x035A [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x035B [0x52] END_LOAD_SCHEDULER: End scheduler "or10" with entities [LocalPlayer, LocalPlayer], work=176*
 54: 0x036A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or11" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 55: 0x037B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[179*, 0*]
 56: 0x038C [0x1C] WAIT(60* ticks)
 57: 0x038F [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8402*]:
    → "She threw herself headlong into the marshes. Thought my number was up, I can tell you!"
 58: 0x0396 [0x27] REQ_SET(priority=0x10, entity_id=Unnamed NPC (ID: 17224354/0x0106D2A2), tag_num=0x04)
 59: 0x039D [0x1C] WAIT(180* ticks)
 60: 0x03A0 [0x1A] CALL_SUBROUTINE(address=0x05E5)
 61: 0x03A3 [0x1C] WAIT(30* ticks)
 62: 0x03A6 [0x2A] GET_REQ_LEVEL(level=16, entity_id=Unnamed NPC (ID: 17224354/0x0106D2A2))
 63: 0x03AC [0x34] LOAD_UNLOAD_ZONE(zone_id=234*)
 64: 0x03AF [0x1C] WAIT(15* ticks)
 65: 0x03B2 [0x75] LOAD_ROOM(Load indoor room, room=261*)
 66: 0x03B6 [0x75] LOAD_ROOM(No action)
 67: 0x03B8 [0x77] SET_EVENT_TIME_WEATHER(hour=3*, weather=1*)
 68: 0x03BD [0x1C] WAIT(15* ticks)
 69: 0x03C0 [0x27] REQ_SET(priority=0x10, entity_id=Unnamed NPC (ID: 17224354/0x0106D2A2), tag_num=0x05)
 70: 0x03C7 [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17224354/0x0106D2A2))
 71: 0x03CC [0x1C] WAIT(15* ticks)
 72: 0x03CF [0x52] END_LOAD_SCHEDULER: End scheduler "or11" with entities [LocalPlayer, LocalPlayer], work=176*
 73: 0x03DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or12" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 74: 0x03EF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[179*, 0*]
 75: 0x0400 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8403*]:
    → "When I saw her in the stables, she was wearing a collar attached to a chain."
 76: 0x0407 [0x23] WAIT_FOR_DIALOG_INTERACTION
 77: 0x0408 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8404*]:
    → "That wasn't to keep the general's mount from being stolen--it was to keep Silver Comet from flying the coop, so to speak."
 78: 0x040F [0x23] WAIT_FOR_DIALOG_INTERACTION
 79: 0x0410 [0x1A] CALL_SUBROUTINE(address=0x05E5)
 80: 0x0413 [0x1C] WAIT(30* ticks)
 81: 0x0416 [0x35] LOAD_ZONE_NO_CLOSE(zone_id=109*)
 82: 0x0419 [0x78] ENABLE_GAME_TIMER_RESET_WEATHER()
 83: 0x041A [0xAB] EventEntity->UnknownFlag = 0 // Disable unknown flag
 84: 0x041C [0x1C] WAIT(15* ticks)
 85: 0x041F [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x0B)
 86: 0x0426 [0x27] REQ_SET(priority=0x10, entity_id=Ulzana (ID: 17224352/0x0106D2A0), tag_num=0x09)
 87: 0x042D [0x6C] FADE_ENTITY_COLOR(entity_id=LocalPlayer, end_alpha=128*, fade_time=1*)
 88: 0x0436 [0x6C] FADE_ENTITY_COLOR(entity_id=Unnamed NPC (ID: 17224354/0x0106D2A2), end_alpha=0*, fade_time=1*)
 89: 0x043F [0x6B] STOP_AND_IDLE: Ulzana (ID: 17224352/0x0106D2A0) stops current action and resets to idle (animation="idl0")
 90: 0x0448 [0x80] LOAD_WAIT(entity=LocalPlayer)
 91: 0x044D [0x80] LOAD_WAIT(entity=Ulzana (ID: 17224352/0x0106D2A0))
 92: 0x0452 [0x79] LocalPlayer looks at Ulzana (ID: 17224352/0x0106D2A0) (Basic look)
 93: 0x045C [0x7B] Ulzana (ID: 17224352/0x0106D2A0) stops talking
 94: 0x0461 [0x94] Ulzana (ID: 17224352/0x0106D2A0)->Render.Flags3 ^= 0x01
 95: 0x0467 [0x1C] WAIT(15* ticks)
 96: 0x046A [0x52] END_LOAD_SCHEDULER: End scheduler "or12" with entities [LocalPlayer, LocalPlayer], work=176*
 97: 0x0479 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or13" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
 98: 0x048A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 99: 0x049B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Ulzana (ID: 17224352/0x0106D2A0), Ulzana (ID: 17224352/0x0106D2A0)], work=0*
100: 0x04AA [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8405*]:
    → "That general's a real schemer. Said that if Silver Comet was released, she would be able to find Shooting Star."
101: 0x04B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
102: 0x04B2 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8406*]:
    → "It's his fault I almost got killed!"
103: 0x04B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
104: 0x04BA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Ulzana (ID: 17224352/0x0106D2A0), Ulzana (ID: 17224352/0x0106D2A0)], work=0*
105: 0x04C9 [0x1C] WAIT(60* ticks)
106: 0x04CC [0x79] Ulzana (ID: 17224352/0x0106D2A0) looks at LocalPlayer (Basic look)
107: 0x04D6 [0x52] END_LOAD_SCHEDULER: End scheduler "or13" with entities [LocalPlayer, LocalPlayer], work=176*
108: 0x04E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or14" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
109: 0x04F6 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8407*]:
    → "Huh? Who's Shooting Star? He's a chocobo, too."
110: 0x04FD [0x23] WAIT_FOR_DIALOG_INTERACTION
111: 0x04FE [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8408*]:
    → "Shooting Star was Silver Comet's mate."
112: 0x0505 [0x23] WAIT_FOR_DIALOG_INTERACTION
113: 0x0506 [0x52] END_LOAD_SCHEDULER: End scheduler "or14" with entities [LocalPlayer, LocalPlayer], work=176*
114: 0x0515 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "or15" with entities [LocalPlayer, LocalPlayer], work=[176*, 0*]
115: 0x0526 [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8409*]:
    → "Their love was a pure, uncomplicated thing, much more so than what people feel."
116: 0x052D [0x23] WAIT_FOR_DIALOG_INTERACTION
117: 0x052E [0x6E] Ulzana (ID: 17224352/0x0106D2A0) uses emote 4*
118: 0x0535 [0x99] Wait for Ulzana (ID: 17224352/0x0106D2A0) animation to complete
119: 0x053A [0x99] Wait for Ulzana (ID: 17224352/0x0106D2A0) animation to complete
120: 0x053F [0x2B] Ulzana (ID: 17224352/0x0106D2A0) [8410*]:
    → "Ahahaha! I think this oil is starting to muddle my senses. I'll see you around, adventurer."
121: 0x0546 [0x23] WAIT_FOR_DIALOG_INTERACTION
122: 0x0547 [0x1A] CALL_SUBROUTINE(address=0x05E5)
123: 0x054A [0x1C] WAIT(30* ticks)
124: 0x054D [0x52] END_LOAD_SCHEDULER: End scheduler "or15" with entities [LocalPlayer, LocalPlayer], work=176*
125: 0x055C [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
126: 0x0560 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
127: 0x0564 [0x5C] MUSIC_CONTROL: Set Combat (Solo) music to song 101*
128: 0x0568 [0x5C] MUSIC_CONTROL: Set Combat (Party) music to song 103*
129: 0x056C [0x9A] WAIT_MUSIC_SERVER()
130: 0x056D [0x46] CAMERA_CONTROL: Restore default settings
131: 0x056F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
132: 0x0580 [0x21] END_EVENT
133: 0x0581 [0x00] END_REQSTACK()

SUBROUTINE_05C4:
134: 0x05C4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
135: 0x05D5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
136: 0x05E4 [0x1B] RETURN

SUBROUTINE_05E5:
137: 0x05E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
138: 0x05F6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
139: 0x0605 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0582 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0593 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x05A2 [0x1B] RETURN
     0x05A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x05B4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x05C3 [0x1B] RETURN
# Dead code (unreachable instructions):
     0x0606 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0617 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0626 [0x1B] RETURN
     0x0627 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0638 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0647 [0x1B] RETURN
     0x0648 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0659 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0668 [0x1B] RETURN
     0x0669 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x067A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0689 [0x1B] RETURN
     0x068A [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x069B [0x1C] WAIT(45* ticks)
     0x069E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x06AF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x06BE [0x1B] RETURN
     0x06BF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x06D0 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x06E1 [0x1C] WAIT(30* ticks)
     0x06E4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x06F3 [0x1B] RETURN
     0x06F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0705 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0716 [0x1B] RETURN
     0x0717 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0728 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0737 [0x1B] RETURN
     0x0738 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0749 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0758 [0x1B] RETURN
     0x0759 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x076A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x0779 [0x1B] RETURN
     0x077A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x078B [0x1B] RETURN
     0x078C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x079D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x07AC [0x1B] RETURN
     0x07AD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x07BE [0x1B] RETURN
     0x07BF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x07D0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x07DF [0x1B] RETURN
     0x07E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x07F1 [0x1B] RETURN
     0x07F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0803 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0812 [0x1B] RETURN
```
