# 17814121 - Magriffon

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 784 bytes                      |
| Total Events     | 2                              |
| References Count | 33                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [348](#event-348)     | 0x0001       |    624 |            133 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x000B      |          11 |
|       4 | 0x1F8E      |        8078 |
|       5 | 0x1F8F      |        8079 |
|       6 | 0x0276      |         630 |
|       7 | 0x1F90      |        8080 |
|       8 | 0x0028      |          40 |
|       9 | 0x0007      |           7 |
|      10 | 0x1F8C      |        8076 |
|      11 | 0x1F8D      |        8077 |
|      12 | 0x001E      |          30 |
|      13 | 0x001D      |          29 |
|      14 | 0x1F8A      |        8074 |
|      15 | 0x1F8B      |        8075 |
|      16 | 0x0014      |          20 |
|      17 | 0x1F88      |        8072 |
|      18 | 0x1F89      |        8073 |
|      19 | 0x000A      |          10 |
|      20 | 0x1F86      |        8070 |
|      21 | 0x1F87      |        8071 |
|      22 | 0x1F83      |        8067 |
|      23 | 0x1F84      |        8068 |
|      24 | 0x1F85      |        8069 |
|      25 | 0x00FE      |         254 |
|      26 | 0x1EB0      |        7856 |
|      27 | 0x1EB1      |        7857 |
|      28 | 0x0008      |           8 |
|      29 | 0x1EB2      |        7858 |
|      30 | 0x0002      |           2 |
|      31 | 0x0009      |           9 |
|      32 | 0x1EB3      |        7859 |

## String References

- **7856**: Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]
- **7857**: [Requirement/Objective completed]: Obtain all ancient abyssite found in this area.
- **7858**: [Requirement/Objective completed]: Obtain all atma found in this area.
- **7859**: [Requirement/Objective completed]: Complete all quests issued in this area.
- **8067**: <Player>? Can't say I've ever heard that name.
- **8068**: What did you expect? Those who live in chill, harsh environs such as these are slow to warm up to strangers.
- **8069**: But take heart. Do what you can to make yourself useful, and someday you might find yourself as beloved as me. Ahahaha!
- **8070**: <Player>, you say? Yes, I may have overheard a person mention someone who claims he might have possibly known a fellow who spoke a name that almost vaguely resembles yours...though I cannot be sure.
- **8071**: Keep working as you are, and I'm sure the community will warm up to you before long. Even if you're not as charming as yours truly. Ahahaha!
- **8072**: <Player>...? Yes, there's no mistaking it. That's a name I heard just this past day.
- **8073**: "Why, [he/she] almost reminds me of a young Magriffon," the fellow said. "Not half as brave and gallant, of course...but then again, who is?"
- **8074**: <Player>! You're quite the talk of the range these days. Seems your hard work has made quite an impression on the survivors.
- **8075**: Just between you and me, do feel free to take a break from playing [hero/heroine] all the time. There's no need to overshadow, er, a certain other prestigious personage. Would you not agree?
- **8076**: Ah, greetings, <Player>. Always a pleasure.
- **8077**: Every time I hear your name--quite often these days, I must say--it brings to mind my own remarkable exploits. Exploits that people don't seem to be speaking much of these days...<sigh>.
- **8078**: Well, you've certainly done it, <Player>. You've completely eclipsed yours truly in the hearts and minds of the survivors of Uleguerand.
- **8079**: I must admit: at first, I was more than a little jealous. But not anymore. We're truly fortunate that you arrived.
- **8080**: No doubt it's thanks to the $3 I acquired. I knew it was worth every last coin!

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

### Event 348

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 624 bytes |
| Instructions | 87        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 1E F0  FF FF 7F 6F 70 02 00 00   ..........op...
0010: 00 80 04 51 00 29 10 F0  FF FF 7F 06 02 02 10 01  ...Q.)..........
0020: 80 00 2C 00 03 02 10 02  80 01 31 00 03 02 10 01  ..,.......1.....
0030: 80 6E 69 D2 0F 01 03 80  99 69 D2 0F 01 1D 04 80  .ni......i......
0040: 23 1D 05 80 23 03 02 10  06 80 1D 07 80 23 01 A7  #...#........#..
0050: 01 02 00 00 08 80 04 8C  00 29 10 F0 FF FF 7F 06  .........)......
0060: 02 02 10 01 80 00 70 00  03 02 10 02 80 01 75 00  ......p.......u.
0070: 03 02 10 01 80 6E 69 D2  0F 01 09 80 99 69 D2 0F  .....ni......i..
0080: 01 1D 0A 80 23 1D 0B 80  23 01 A7 01 02 00 00 0C  ....#...#.......
0090: 80 04 D9 00 29 10 F0 FF  FF 7F 06 02 02 10 01 80  ....)...........
00A0: 00 AB 00 03 02 10 02 80  01 B0 00 03 02 10 01 80  ................
00B0: 66 0D 80 69 D2 0F 01 69  D2 0F 01 74 6C 6B 30 1D  f..i...i...tlk0.
00C0: 0E 80 23 1D 0F 80 23 66  0D 80 69 D2 0F 01 69 D2  ..#...#f..i...i.
00D0: 0F 01 74 6C 6B 31 01 A7  01 02 00 00 10 80 04 14  ..tlk1..........
00E0: 01 29 10 F0 FF FF 7F 06  02 02 10 01 80 00 F8 00  .)..............
00F0: 03 02 10 02 80 01 FD 00  03 02 10 01 80 6E 69 D2  .............ni.
0100: 0F 01 09 80 99 69 D2 0F  01 1D 11 80 23 1D 12 80  .....i......#...
0110: 23 01 A7 01 02 00 00 13  80 04 61 01 29 10 F0 FF  #.........a.)...
0120: FF 7F 06 02 02 10 01 80  00 33 01 03 02 10 02 80  .........3......
0130: 01 38 01 03 02 10 01 80  66 0D 80 69 D2 0F 01 69  .8......f..i...i
0140: D2 0F 01 74 68 6B 31 1D  14 80 23 1D 15 80 23 66  ...thk1...#...#f
0150: 0D 80 69 D2 0F 01 69 D2  0F 01 74 68 6B 32 01 A7  ..i...i...thk2..
0160: 01 29 10 F0 FF FF 7F 06  02 02 10 01 80 00 78 01  .)............x.
0170: 03 02 10 02 80 01 7D 01  03 02 10 01 80 66 0D 80  ......}......f..
0180: 69 D2 0F 01 69 D2 0F 01  74 68 6B 31 1D 16 80 23  i...i...thk1...#
0190: 1D 17 80 23 1D 18 80 23  66 0D 80 69 D2 0F 01 69  ...#...#f..i...i
01A0: D2 0F 01 74 68 6B 32 21  00 03 01 10 19 80 43 00  ...thk2!......C.
01B0: 43 01 03 01 00 02 10 03  02 00 03 10 03 03 00 04  C...............
01C0: 10 03 04 00 05 10 03 05  00 06 10 03 06 00 07 10  ................
01D0: 03 07 00 08 10 02 02 80  02 80 00 70 02 24 1A 80  ...........p.$..
01E0: 01 80 01 80 25 02 00 10  01 80 00 08 02 3E 07 00  ....%........>..
01F0: 09 80 FC 01 03 02 10 02  80 01 01 02 03 02 10 01  ................
0200: 80 48 1B 80 23 01 4F 02  02 00 10 02 80 00 2B 02  .H..#.O.......+.
0210: 3E 07 00 1C 80 1F 02 03  02 10 02 80 01 24 02 03  >............$..
0220: 02 10 01 80 48 1D 80 23  01 4F 02 02 00 10 1E 80  ....H..#.O......
0230: 00 4E 02 3E 07 00 1F 80  42 02 03 02 10 02 80 01  .N.>....B.......
0240: 47 02 03 02 10 01 80 48  20 80 23 01 4F 02 1B 03  G......H .#.O...
0250: 02 10 01 00 03 03 10 02  00 03 04 10 03 00 03 05  ................
0260: 10 04 00 03 06 10 05 00  03 07 10 06 00 01 D5 01  ................
0270: 1B                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000D [0x02] IF !(ExtData[1]->WorkLocal[0] < 50*) GOTO 0x0051
  5: 0x0015 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
  6: 0x001C [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x002C
  7: 0x0024 [0x03] Work_Zone[2] = 1*
  8: 0x0029 [0x01] GOTO 0x0031
  9: 0x002C [0x03] Work_Zone[2] = 0*

SUBROUTINE_0031:
 10: 0x0031 [0x6E] Magriffon (ID: 17814121/0x010FD269) uses emote 11*
 11: 0x0038 [0x99] Wait for Magriffon (ID: 17814121/0x010FD269) animation to complete
 12: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=8078*)
    → "Well, you've certainly done it, <Player>. You've completely eclipsed yours truly in the hearts and minds of the survivors of Uleguerand."
 13: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0041 [0x1D] PRINT_EVENT_MESSAGE(message_id=8079*)
    → "I must admit: at first, I was more than a little jealous. But not anymore. We're truly fortunate that you arrived."
 15: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0045 [0x03] Work_Zone[2] = 630*
 17: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=8080*)
    → "No doubt it's thanks to the $3 I acquired. I knew it was worth every last coin!"
 18: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x004E [0x01] GOTO 0x01A7
 20: 0x0051 [0x02] IF !(ExtData[1]->WorkLocal[0] < 40*) GOTO 0x008C
 21: 0x0059 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 22: 0x0060 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0070
 23: 0x0068 [0x03] Work_Zone[2] = 1*
 24: 0x006D [0x01] GOTO 0x0075
 25: 0x0070 [0x03] Work_Zone[2] = 0*

SUBROUTINE_0075:
 26: 0x0075 [0x6E] Magriffon (ID: 17814121/0x010FD269) uses emote 7*
 27: 0x007C [0x99] Wait for Magriffon (ID: 17814121/0x010FD269) animation to complete
 28: 0x0081 [0x1D] PRINT_EVENT_MESSAGE(message_id=8076*)
    → "Ah, greetings, <Player>. Always a pleasure."
 29: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=8077*)
    → "Every time I hear your name--quite often these days, I must say--it brings to mind my own remarkable exploits. Exploits that people don't seem to be speaking much of these days...<sigh>."
 31: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0089 [0x01] GOTO 0x01A7
 33: 0x008C [0x02] IF !(ExtData[1]->WorkLocal[0] < 30*) GOTO 0x00D9
 34: 0x0094 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 35: 0x009B [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00AB
 36: 0x00A3 [0x03] Work_Zone[2] = 1*
 37: 0x00A8 [0x01] GOTO 0x00B0
 38: 0x00AB [0x03] Work_Zone[2] = 0*

SUBROUTINE_00B0:
 39: 0x00B0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Magriffon (ID: 17814121/0x010FD269), Magriffon (ID: 17814121/0x010FD269)], work=29*
 40: 0x00BF [0x1D] PRINT_EVENT_MESSAGE(message_id=8074*)
    → "<Player>! You're quite the talk of the range these days. Seems your hard work has made quite an impression on the survivors."
 41: 0x00C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x00C3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8075*)
    → "Just between you and me, do feel free to take a break from playing [hero/heroine] all the time. There's no need to overshadow, er, a certain other prestigious personage. Would you not agree?"
 43: 0x00C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x00C7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Magriffon (ID: 17814121/0x010FD269), Magriffon (ID: 17814121/0x010FD269)], work=29*
 45: 0x00D6 [0x01] GOTO 0x01A7
 46: 0x00D9 [0x02] IF !(ExtData[1]->WorkLocal[0] < 20*) GOTO 0x0114
 47: 0x00E1 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 48: 0x00E8 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00F8
 49: 0x00F0 [0x03] Work_Zone[2] = 1*
 50: 0x00F5 [0x01] GOTO 0x00FD
 51: 0x00F8 [0x03] Work_Zone[2] = 0*

SUBROUTINE_00FD:
 52: 0x00FD [0x6E] Magriffon (ID: 17814121/0x010FD269) uses emote 7*
 53: 0x0104 [0x99] Wait for Magriffon (ID: 17814121/0x010FD269) animation to complete
 54: 0x0109 [0x1D] PRINT_EVENT_MESSAGE(message_id=8072*)
    → "<Player>...? Yes, there's no mistaking it. That's a name I heard just this past day."
 55: 0x010C [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x010D [0x1D] PRINT_EVENT_MESSAGE(message_id=8073*)
    → ""Why, [he/she] almost reminds me of a young Magriffon," the fellow said. "Not half as brave and gallant, of course...but then again, who is?""
 57: 0x0110 [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x0111 [0x01] GOTO 0x01A7
 59: 0x0114 [0x02] IF !(ExtData[1]->WorkLocal[0] < 10*) GOTO 0x0161
 60: 0x011C [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 61: 0x0123 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0133
 62: 0x012B [0x03] Work_Zone[2] = 1*
 63: 0x0130 [0x01] GOTO 0x0138
 64: 0x0133 [0x03] Work_Zone[2] = 0*

SUBROUTINE_0138:
 65: 0x0138 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Magriffon (ID: 17814121/0x010FD269), Magriffon (ID: 17814121/0x010FD269)], work=29*
 66: 0x0147 [0x1D] PRINT_EVENT_MESSAGE(message_id=8070*)
    → "<Player>, you say? Yes, I may have overheard a person mention someone who claims he might have possibly known a fellow who spoke a name that almost vaguely resembles yours...though I cannot be sure."
 67: 0x014A [0x23] WAIT_FOR_DIALOG_INTERACTION
 68: 0x014B [0x1D] PRINT_EVENT_MESSAGE(message_id=8071*)
    → "Keep working as you are, and I'm sure the community will warm up to you before long. Even if you're not as charming as yours truly. Ahahaha!"
 69: 0x014E [0x23] WAIT_FOR_DIALOG_INTERACTION
 70: 0x014F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Magriffon (ID: 17814121/0x010FD269), Magriffon (ID: 17814121/0x010FD269)], work=29*
 71: 0x015E [0x01] GOTO 0x01A7
 72: 0x0161 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x06)
 73: 0x0168 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0178
 74: 0x0170 [0x03] Work_Zone[2] = 1*
 75: 0x0175 [0x01] GOTO 0x017D
 76: 0x0178 [0x03] Work_Zone[2] = 0*

SUBROUTINE_017D:
 77: 0x017D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Magriffon (ID: 17814121/0x010FD269), Magriffon (ID: 17814121/0x010FD269)], work=29*
 78: 0x018C [0x1D] PRINT_EVENT_MESSAGE(message_id=8067*)
    → "<Player>? Can't say I've ever heard that name."
 79: 0x018F [0x23] WAIT_FOR_DIALOG_INTERACTION
 80: 0x0190 [0x1D] PRINT_EVENT_MESSAGE(message_id=8068*)
    → "What did you expect? Those who live in chill, harsh environs such as these are slow to warm up to strangers."
 81: 0x0193 [0x23] WAIT_FOR_DIALOG_INTERACTION
 82: 0x0194 [0x1D] PRINT_EVENT_MESSAGE(message_id=8069*)
    → "But take heart. Do what you can to make yourself useful, and someday you might find yourself as beloved as me. Ahahaha!"
 83: 0x0197 [0x23] WAIT_FOR_DIALOG_INTERACTION
 84: 0x0198 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Magriffon (ID: 17814121/0x010FD269), Magriffon (ID: 17814121/0x010FD269)], work=29*

SUBROUTINE_01A7:
 85: 0x01A7 [0x21] END_EVENT
 86: 0x01A8 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x01A9 [0x03] Work_Zone[1] = 254*
     0x01AE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x01B0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x01B2 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
     0x01B7 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[3]
     0x01BC [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[4]
     0x01C1 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[5]
     0x01C6 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[6]
     0x01CB [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[7]
     0x01D0 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[8]
     0x01D5 [0x02] IF !(1* == 1*) GOTO 0x0270
     0x01DD [0x24] CREATE_DIALOG(message_id=7856*, default_option=0*, option_flags=0*)
    → "Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]"
     0x01E4 [0x25] WAIT_DIALOG_SELECT()
     0x01E5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0208
     0x01ED [0x3E] IF !(ExtData[1]->WorkLocal[7] bit 7*) GOTO 0x01FC
     0x01F4 [0x03] Work_Zone[2] = 1*
     0x01F9 [0x01] GOTO 0x0201
     0x01FC [0x03] Work_Zone[2] = 0*
     0x0201 [0x48] [System] [7857*]:
    → "[Requirement/Objective completed]: Obtain all ancient abyssite found in this area."
     0x0204 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0205 [0x01] GOTO 0x024F
     0x0208 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x022B
     0x0210 [0x3E] IF !(ExtData[1]->WorkLocal[7] bit 8*) GOTO 0x021F
     0x0217 [0x03] Work_Zone[2] = 1*
     0x021C [0x01] GOTO 0x0224
     0x021F [0x03] Work_Zone[2] = 0*
     0x0224 [0x48] [System] [7858*]:
    → "[Requirement/Objective completed]: Obtain all atma found in this area."
     0x0227 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0228 [0x01] GOTO 0x024F
     0x022B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x024E
     0x0233 [0x3E] IF !(ExtData[1]->WorkLocal[7] bit 9*) GOTO 0x0242
     0x023A [0x03] Work_Zone[2] = 1*
     0x023F [0x01] GOTO 0x0247
     0x0242 [0x03] Work_Zone[2] = 0*
     0x0247 [0x48] [System] [7859*]:
    → "[Requirement/Objective completed]: Complete all quests issued in this area."
     0x024A [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x024B [0x01] GOTO 0x024F
     0x024E [0x1B] RETURN
     0x024F [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
     0x0254 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
     0x0259 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
     0x025E [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[4]
     0x0263 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[5]
     0x0268 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[6]
     0x026D [0x01] GOTO 0x01D5
     0x0270 [0x1B] RETURN
```
