# 17277204 - QuHau Spring

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Ro'Maeve (ID: 122) |
| Block Size       | 3268 bytes         |
| Total Events     | 5                  |
| References Count | 38                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2](#event-2)         | 0x0001       |    989 |            122 |
| [4](#event-4)         | 0x03DE       |   1174 |            136 |
| [7](#event-7)         | 0x0874       |    136 |             25 |
| [8](#event-8)         | 0x08FC       |    778 |             82 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0013      |          19 |
|       3 | 0x00CC      |         204 |
|       4 | 0x007F      |         127 |
|       5 | 0x0001      |           1 |
|       6 | 0x00E4      |         228 |
|       7 | 0x0078      |         120 |
|       8 | 0x1CA1      |        7329 |
|       9 | 0x0005      |           5 |
|      10 | 0x0006      |           6 |
|      11 | 0x1CA2      |        7330 |
|      12 | 0x000A      |          10 |
|      13 | 0x00C9      |         201 |
|      14 | 0x007D      |         125 |
|      15 | 0x1CA3      |        7331 |
|      16 | 0x0032      |          50 |
|      17 | 0x0064      |         100 |
|      18 | 0x003C      |          60 |
|      19 | 0x00D3      |         211 |
|      20 | 0x1CA4      |        7332 |
|      21 | 0x1CA5      |        7333 |
|      22 | 0x1CA6      |        7334 |
|      23 | 0x0002      |           2 |
|      24 | 0x00FC      |         252 |
|      25 | 0x0028      |          40 |
|      26 | 0x0029      |          41 |
|      27 | 0x0026      |          38 |
|      28 | 0x0400      |        1024 |
|      29 | 0x000F      |          15 |
|      30 | 0x00D7      |         215 |
|      31 | 0x0003      |           3 |
|      32 | 0x1D0B      |        7435 |
|      33 | 0x1D0C      |        7436 |
|      34 | 0x002D      |          45 |
|      35 | 0x04ED      |        1261 |
|      36 | 0x1D0F      |        7439 |
|      37 | 0x001E      |          30 |

## String References

- **7329**: A haunting song suddenly echoes throughout the ruins...
- **7435**: You immerse the $0 and $1 in the waters of the spring.
- **7436**: You immerse the shards of the five Crystal Warriors, along with the $0 and $1, in the waters of the spring.
- **7439**: You immerse the shards of the five Crystal Warriors, along with the $0, in the waters of the spring.

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

### Event 2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 989 bytes |
| Instructions | 122       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 46 01 5D 00  80 01 80 45 01 80 F8 FF    .BF.]....E....
0010: FF 7F F8 FF FF 7F 66 64  6F 31 00 80 1C 01 80 38  ......fdo1.....8
0020: 02 80 5C 00 03 80 5C 01  03 80 5D 04 80 05 80 1C  ..\...\...].....
0030: 01 80 4E 00 16 A1 07 01  80 16 A1 07 01 29 0B F0  ..N..........)..
0040: FF FF 7F 02 29 08 F0 FF  FF 7F 05 45 06 80 F0 FF  ....)......E....
0050: FF 7F F0 FF FF 7F 73 30  30 30 00 80 45 01 80 F8  ......s000..E...
0060: FF FF 7F F8 FF FF 7F 66  64 69 31 00 80 1C 07 80  .......fdi1.....
0070: 48 08 80 23 1C 07 80 52  06 80 F0 FF FF 7F F0 FF  H..#...R........
0080: FF 7F 73 30 30 30 45 01  80 F0 FF FF 7F F0 FF FF  ..s000E.........
0090: 7F 6F 76 6C 31 00 80 02  09 10 09 80 00 B3 00 45  .ovl1..........E
00A0: 06 80 F0 FF FF 7F F0 FF  FF 7F 73 30 30 37 00 80  ..........s007..
00B0: 01 E0 00 02 09 10 0A 80  00 CF 00 45 06 80 F0 FF  ...........E....
00C0: FF 7F F0 FF FF 7F 73 30  30 37 00 80 01 E0 00 45  ......s007.....E
00D0: 06 80 F0 FF FF 7F F0 FF  FF 7F 73 30 30 31 00 80  ..........s001..
00E0: 4E 00 15 A1 07 01 4A F0  FF FF 7F 16 A1 07 01 2B  N.....J........+
00F0: 16 A1 07 01 0B 80 23 6F  76 F0 FF FF 7F 79 00 F0  ......#ov....y..
0100: FF FF 7F 15 A1 07 01 1C  0C 80 80 15 A1 07 01 02  ................
0110: 09 10 09 80 00 29 01 52  06 80 F0 FF FF 7F F0 FF  .....).R........
0120: FF 7F 73 30 30 37 01 52  01 02 09 10 0A 80 00 43  ..s007.R.......C
0130: 01 52 06 80 F0 FF FF 7F  F0 FF FF 7F 73 30 30 37  .R..........s007
0140: 01 52 01 52 06 80 F0 FF  FF 7F F0 FF FF 7F 73 30  .R.R..........s0
0150: 30 31 5D 00 80 05 80 45  01 80 F0 FF FF 7F F0 FF  01]....E........
0160: FF 7F 62 6C 6F 6E 00 80  45 0D 80 F0 FF FF 7F F0  ..blon..E.......
0170: FF FF 7F 62 6C 6F 6E 00  80 45 06 80 F0 FF FF 7F  ...blon..E......
0180: F0 FF FF 7F 73 30 30 32  00 80 27 0B 15 A1 07 01  ....s002..'.....
0190: 02 1C 05 80 5C 00 0E 80  5C 01 0E 80 5D 04 80 05  ....\...\...]...
01A0: 80 1C 07 80 52 06 80 F0  FF FF 7F F0 FF FF 7F 73  ....R..........s
01B0: 30 30 32 45 01 80 F0 FF  FF 7F F0 FF FF 7F 6F 76  002E..........ov
01C0: 6C 31 00 80 45 06 80 F0  FF FF 7F F0 FF FF 7F 73  l1..E..........s
01D0: 30 30 35 00 80 4A F0 FF  FF 7F 15 A1 07 01 2B 16  005..J........+.
01E0: A1 07 01 0F 80 23 1C 10  80 2A 0B 15 A1 07 01 52  .....#...*.....R
01F0: 06 80 F0 FF FF 7F F0 FF  FF 7F 73 30 30 35 45 01  ..........s005E.
0200: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 66 00 80 45  .........blof..E
0210: 01 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 00 80  ..........ovl1..
0220: 45 06 80 F0 FF FF 7F F0  FF FF 7F 73 30 30 33 00  E..........s003.
0230: 80 5D 00 80 01 80 1C 11  80 29 0B 15 A1 07 01 04  .].......)......
0240: 29 0B 15 A1 07 01 03 62  05 80 15 A1 07 01 15 A1  )......b........
0250: 07 01 6D 61 69 6E 00 80  45 01 80 F8 FF FF 7F F8  ..main..E.......
0260: FF FF 7F 66 64 6F 31 00  80 1C 12 80 5C 00 13 80  ...fdo1.....\...
0270: 5C 01 13 80 5D 04 80 05  80 52 06 80 F0 FF FF 7F  \...]....R......
0280: F0 FF FF 7F 73 30 30 33  45 06 80 F0 FF FF 7F F0  ....s003E.......
0290: FF FF 7F 73 30 30 34 00  80 1C 12 80 45 01 80 F8  ...s004.....E...
02A0: FF FF 7F F8 FF FF 7F 66  64 69 31 00 80 1C 12 80  .......fdi1.....
02B0: 79 00 F0 FF FF 7F 16 A1  07 01 4A 16 A1 07 01 F0  y.........J.....
02C0: FF FF 7F 6F 76 16 A1 07  01 2B 16 A1 07 01 14 80  ...ov....+......
02D0: 23 2B 16 A1 07 01 15 80  23 52 06 80 F0 FF FF 7F  #+......#R......
02E0: F0 FF FF 7F 73 30 30 34  45 01 80 F8 FF FF 7F F8  ....s004E.......
02F0: FF FF 7F 66 64 6F 31 00  80 1C 12 80 4A F0 FF FF  ...fdo1.....J...
0300: 7F 16 A1 07 01 6F 76 F0  FF FF 7F 02 09 10 09 80  .....ov.........
0310: 00 27 03 45 06 80 F0 FF  FF 7F F0 FF FF 7F 73 30  .'.E..........s0
0320: 30 37 00 80 01 54 03 02  09 10 0A 80 00 43 03 45  07...T.......C.E
0330: 06 80 F0 FF FF 7F F0 FF  FF 7F 73 30 30 37 00 80  ..........s007..
0340: 01 54 03 45 06 80 F0 FF  FF 7F F0 FF FF 7F 73 30  .T.E..........s0
0350: 30 36 00 80 45 01 80 F8  FF FF 7F F8 FF FF 7F 66  06..E..........f
0360: 64 69 31 00 80 2B 16 A1  07 01 16 80 23 45 01 80  di1..+......#E..
0370: F8 FF FF 7F F8 FF FF 7F  66 64 6F 31 00 80 1C 12  ........fdo1....
0380: 80 02 09 10 09 80 00 9B  03 52 06 80 F0 FF FF 7F  .........R......
0390: F0 FF FF 7F 73 30 30 37  01 C4 03 02 09 10 0A 80  ....s007........
03A0: 00 B5 03 52 06 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...R..........s0
03B0: 30 37 01 C4 03 52 06 80  F0 FF FF 7F F0 FF FF 7F  07...R..........
03C0: 73 30 30 36 46 00 1C 01  80 45 01 80 F8 FF FF 7F  s006F....E......
03D0: F8 FF FF 7F 66 64 69 31  00 80 20 00 21 00        ....fdi1.. .!.  
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0006 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
  4: 0x000B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  5: 0x001C [0x1C] WAIT(200* ticks)
  6: 0x001F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  7: 0x0022 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 204*
  8: 0x0026 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 204*
  9: 0x002A [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
 10: 0x002F [0x1C] WAIT(200* ticks)
 11: 0x0032 [0x4E] SET_ENTITY_HIDE_FLAG: Show Talking Doll (ID: 17277206/0x0107A116)
 12: 0x0038 [0x80] LOAD_WAIT(entity=Talking Doll (ID: 17277206/0x0107A116))
 13: 0x003D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x02)
 14: 0x0044 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x05)
 15: 0x004B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]
 16: 0x005C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 17: 0x006D [0x1C] WAIT(120* ticks)
 18: 0x0070 [0x48] [System] [7329*]:
    → "A haunting song suddenly echoes throughout the ruins..."
 19: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0074 [0x1C] WAIT(120* ticks)
 21: 0x0077 [0x52] END_LOAD_SCHEDULER: End scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=228*
 22: 0x0086 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x0097 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x00B3
 24: 0x009F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]
 25: 0x00B0 [0x01] GOTO 0x00E0
 26: 0x00B3 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x00CF
 27: 0x00BB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]
 28: 0x00CC [0x01] GOTO 0x00E0
 29: 0x00CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]

SUBROUTINE_00E0:
 30: 0x00E0 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17277205/0x0107A115)
 31: 0x00E6 [0x4A] LocalPlayer looks at Talking Doll (ID: 17277206/0x0107A116)
 32: 0x00EF [0x2B] Talking Doll (ID: 17277206/0x0107A116) [7330*]:
    → "Ahahahahaha! That's it! That's it! You've found it, slacker!"
 33: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x00F7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 35: 0x00F8 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 36: 0x00FD [0x79] LocalPlayer looks at Unnamed NPC (ID: 17277205/0x0107A115) (Basic look)
 37: 0x0107 [0x1C] WAIT(10* ticks)
 38: 0x010A [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17277205/0x0107A115))
 39: 0x010F [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x0129
 40: 0x0117 [0x52] END_LOAD_SCHEDULER: End scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=228*
 41: 0x0126 [0x01] GOTO 0x0152
 42: 0x0129 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x0143
 43: 0x0131 [0x52] END_LOAD_SCHEDULER: End scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=228*
 44: 0x0140 [0x01] GOTO 0x0152
 45: 0x0143 [0x52] END_LOAD_SCHEDULER: End scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=228*

SUBROUTINE_0152:
 46: 0x0152 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=1*)
 47: 0x0157 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 48: 0x0168 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 49: 0x0179 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s002" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]
 50: 0x018A [0x27] REQ_SET(priority=0x0B, entity_id=Unnamed NPC (ID: 17277205/0x0107A115), tag_num=0x02)
 51: 0x0191 [0x1C] WAIT(1* ticks)
 52: 0x0194 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 125*
 53: 0x0198 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 125*
 54: 0x019C [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
 55: 0x01A1 [0x1C] WAIT(120* ticks)
 56: 0x01A4 [0x52] END_LOAD_SCHEDULER: End scheduler "s002" with entities [LocalPlayer, LocalPlayer], work=228*
 57: 0x01B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 58: 0x01C4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s005" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]
 59: 0x01D5 [0x4A] LocalPlayer looks at Unnamed NPC (ID: 17277205/0x0107A115)
 60: 0x01DE [0x2B] Talking Doll (ID: 17277206/0x0107A116) [7331*]:
    → "Ahahahaha...huh? Wait, something's not right! The power is too concentrated..."
 61: 0x01E5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x01E6 [0x1C] WAIT(50* ticks)
 63: 0x01E9 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Unnamed NPC (ID: 17277205/0x0107A115))
 64: 0x01EF [0x52] END_LOAD_SCHEDULER: End scheduler "s005" with entities [LocalPlayer, LocalPlayer], work=228*
 65: 0x01FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 66: 0x020F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 67: 0x0220 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s003" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]
 68: 0x0231 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
 69: 0x0236 [0x1C] WAIT(100* ticks)
 70: 0x0239 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Unnamed NPC (ID: 17277205/0x0107A115), tag_num=0x04)
 71: 0x0240 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Unnamed NPC (ID: 17277205/0x0107A115), tag_num=0x03)
 72: 0x0247 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Unnamed NPC (ID: 17277205/0x0107A115), Unnamed NPC (ID: 17277205/0x0107A115)], work=[1*, 0*]
 73: 0x0258 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 74: 0x0269 [0x1C] WAIT(60* ticks)
 75: 0x026C [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 211*
 76: 0x0270 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 211*
 77: 0x0274 [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
 78: 0x0279 [0x52] END_LOAD_SCHEDULER: End scheduler "s003" with entities [LocalPlayer, LocalPlayer], work=228*
 79: 0x0288 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s004" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]
 80: 0x0299 [0x1C] WAIT(60* ticks)
 81: 0x029C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 82: 0x02AD [0x1C] WAIT(60* ticks)
 83: 0x02B0 [0x79] LocalPlayer looks at Talking Doll (ID: 17277206/0x0107A116) (Basic look)
 84: 0x02BA [0x4A] Talking Doll (ID: 17277206/0x0107A116) looks at LocalPlayer
 85: 0x02C3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 86: 0x02C4 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Talking Doll (ID: 17277206/0x0107A116) Render.Flags0 and Render.Flags3 conditions are met
 87: 0x02C9 [0x2B] Talking Doll (ID: 17277206/0x0107A116) [7332*]:
    → "Ahahahahaha! Oops! I guess that wasn't it! All right, all right, I don't need to hear your whining!"
 88: 0x02D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 89: 0x02D1 [0x2B] Talking Doll (ID: 17277206/0x0107A116) [7333*]:
    → "Just a moment there, slacker... Let me recalibrate my search!"
 90: 0x02D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 91: 0x02D9 [0x52] END_LOAD_SCHEDULER: End scheduler "s004" with entities [LocalPlayer, LocalPlayer], work=228*
 92: 0x02E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 93: 0x02F9 [0x1C] WAIT(60* ticks)
 94: 0x02FC [0x4A] LocalPlayer looks at Talking Doll (ID: 17277206/0x0107A116)
 95: 0x0305 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 96: 0x0306 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 97: 0x030B [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x0327
 98: 0x0313 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]
 99: 0x0324 [0x01] GOTO 0x0354
100: 0x0327 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x0343
101: 0x032F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]
102: 0x0340 [0x01] GOTO 0x0354
103: 0x0343 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s006" with entities [LocalPlayer, LocalPlayer], work=[228*, 0*]

SUBROUTINE_0354:
104: 0x0354 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
105: 0x0365 [0x2B] Talking Doll (ID: 17277206/0x0107A116) [7334*]:
    → "Ahahahahaha! Okay, this is not a drill! Sensing emanations from the southwest!"
106: 0x036C [0x23] WAIT_FOR_DIALOG_INTERACTION
107: 0x036D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
108: 0x037E [0x1C] WAIT(60* ticks)
109: 0x0381 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x039B
110: 0x0389 [0x52] END_LOAD_SCHEDULER: End scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=228*
111: 0x0398 [0x01] GOTO 0x03C4
112: 0x039B [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x03B5
113: 0x03A3 [0x52] END_LOAD_SCHEDULER: End scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=228*
114: 0x03B2 [0x01] GOTO 0x03C4
115: 0x03B5 [0x52] END_LOAD_SCHEDULER: End scheduler "s006" with entities [LocalPlayer, LocalPlayer], work=228*

SUBROUTINE_03C4:
116: 0x03C4 [0x46] CAMERA_CONTROL: Restore default settings
117: 0x03C6 [0x1C] WAIT(200* ticks)
118: 0x03C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
119: 0x03DA [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
120: 0x03DC [0x21] END_EVENT
121: 0x03DD [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x03DE     |
| Data Size    | 1174 bytes |
| Instructions | 136        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03D0:                                            20 01                 .
03E0: 42 46 01 5D 00 80 01 80  45 01 80 F0 FF FF 7F F0  BF.]....E.......
03F0: FF FF 7F 66 64 6F 31 00  80 1C 01 80 38 02 80 4E  ...fdo1.....8..N
0400: 00 1B A1 07 01 4E 00 1C  A1 07 01 4E 00 1D A1 07  .....N.....N....
0410: 01 4E 00 1E A1 07 01 4E  00 1F A1 07 01 4E 00 20  .N.....N.....N. 
0420: A1 07 01 4E 00 21 A1 07  01 4E 00 22 A1 07 01 4E  ...N.!...N."...N
0430: 00 23 A1 07 01 4E 00 24  A1 07 01 80 1B A1 07 01  .#...N.$........
0440: 80 1C A1 07 01 80 1D A1  07 01 80 1E A1 07 01 80  ................
0450: 1F A1 07 01 80 20 A1 07  01 80 21 A1 07 01 80 22  ..... ....!...."
0460: A1 07 01 80 23 A1 07 01  80 24 A1 07 01 6C 1B A1  ....#....$...l..
0470: 07 01 00 80 17 80 6C 1C  A1 07 01 00 80 17 80 6C  ......l........l
0480: 1D A1 07 01 00 80 17 80  6C 1E A1 07 01 00 80 17  ........l.......
0490: 80 6C 1F A1 07 01 00 80  17 80 6C 20 A1 07 01 00  .l........l ....
04A0: 80 17 80 6C 21 A1 07 01  00 80 17 80 6C 22 A1 07  ...l!.......l"..
04B0: 01 00 80 17 80 6C 23 A1  07 01 00 80 17 80 6C 24  .....l#.......l$
04C0: A1 07 01 00 80 17 80 1C  0C 80 92 01 1B A1 07 01  ................
04D0: 92 01 1C A1 07 01 92 01  1D A1 07 01 92 01 1E A1  ................
04E0: 07 01 92 01 1F A1 07 01  92 01 20 A1 07 01 92 01  .......... .....
04F0: 21 A1 07 01 92 01 22 A1  07 01 92 01 23 A1 07 01  !.....".....#...
0500: 92 01 24 A1 07 01 29 0B  F0 FF FF 7F 08 29 0B 1B  ..$...)......)..
0510: A1 07 01 02 29 0B 1C A1  07 01 02 29 0B 1D A1 07  ....)......)....
0520: 01 02 29 0B 1E A1 07 01  02 29 0B 1F A1 07 01 02  ..)......)......
0530: 29 0B 20 A1 07 01 02 29  0B 21 A1 07 01 02 29 0B  ). ....).!....).
0540: 22 A1 07 01 02 29 0B 23  A1 07 01 02 29 0B 24 A1  "....).#....).$.
0550: 07 01 02 45 18 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...E..........s0
0560: 35 30 00 80 45 01 80 F0  FF FF 7F F0 FF FF 7F 66  50..E..........f
0570: 64 69 31 00 80 02 05 10  05 80 00 91 05 9F 19 80  di1.............
0580: F0 FF FF 7F F0 FF FF 7F  6D 61 69 6E 00 80 01 AA  ........main....
0590: 05 02 05 10 17 80 00 AA  05 9F 1A 80 F0 FF FF 7F  ................
05A0: F0 FF FF 7F 6D 61 69 6E  00 80 55 18 80 F0 FF FF  ....main..U.....
05B0: 7F F0 FF FF 7F 73 30 35  30 48 08 80 23 45 01 80  .....s050H..#E..
05C0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 00 80 1C 12  ........fdo1....
05D0: 80 5C 00 03 80 5C 01 03  80 1C 01 80 6C 1B A1 07  .\...\......l...
05E0: 01 10 80 05 80 6C 1C A1  07 01 10 80 05 80 6C 1D  .....l........l.
05F0: A1 07 01 10 80 05 80 6C  1E A1 07 01 10 80 05 80  .......l........
0600: 6C 1F A1 07 01 10 80 05  80 6C 20 A1 07 01 10 80  l........l .....
0610: 05 80 6C 21 A1 07 01 10  80 05 80 6C 22 A1 07 01  ..l!.......l"...
0620: 10 80 05 80 6C 23 A1 07  01 10 80 05 80 6C 24 A1  ....l#.......l$.
0630: 07 01 10 80 05 80 9F 1B  80 1B A1 07 01 1B A1 07  ................
0640: 01 6D 61 69 6E 00 80 9F  1B 80 1C A1 07 01 1C A1  .main...........
0650: 07 01 6D 61 69 6E 00 80  9F 1B 80 1D A1 07 01 1D  ..main..........
0660: A1 07 01 6D 61 69 6E 00  80 9F 1B 80 1E A1 07 01  ...main.........
0670: 1E A1 07 01 6D 61 69 6E  00 80 9F 1B 80 1F A1 07  ....main........
0680: 01 1F A1 07 01 6D 61 69  6E 00 80 9F 1B 80 20 A1  .....main..... .
0690: 07 01 20 A1 07 01 6D 61  69 6E 00 80 9F 1B 80 21  .. ...main.....!
06A0: A1 07 01 21 A1 07 01 6D  61 69 6E 00 80 9F 1B 80  ...!...main.....
06B0: 22 A1 07 01 22 A1 07 01  6D 61 69 6E 00 80 9F 1B  "..."...main....
06C0: 80 23 A1 07 01 23 A1 07  01 6D 61 69 6E 00 80 9F  .#...#...main...
06D0: 1B 80 24 A1 07 01 24 A1  07 01 6D 61 69 6E 00 80  ..$...$...main..
06E0: 27 0B 1B A1 07 01 03 27  0B 1C A1 07 01 03 27 0B  '......'......'.
06F0: 1D A1 07 01 03 27 0B 1E  A1 07 01 03 27 0B 1F A1  .....'......'...
0700: 07 01 03 27 0B 23 A1 07  01 03 27 0B 24 A1 07 01  ...'.#....'.$...
0710: 03 52 18 80 F0 FF FF 7F  F0 FF FF 7F 73 30 35 30  .R..........s050
0720: 45 18 80 F0 FF FF 7F F0  FF FF 7F 73 30 35 31 00  E..........s051.
0730: 80 45 01 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
0740: 00 80 1C 11 80 52 18 80  F0 FF FF 7F F0 FF FF 7F  .....R..........
0750: 73 30 35 31 45 18 80 F0  FF FF 7F F0 FF FF 7F 73  s051E..........s
0760: 30 35 35 00 80 4B F0 FF  FF 7F 1C 80 1C 07 80 52  055..K.........R
0770: 18 80 F0 FF FF 7F F0 FF  FF 7F 73 30 35 35 45 01  ..........s055E.
0780: 80 F0 FF FF 7F F0 FF FF  7F 6F 76 6C 31 00 80 45  .........ovl1..E
0790: 18 80 F0 FF FF 7F F0 FF  FF 7F 73 30 35 32 00 80  ..........s052..
07A0: 1C 11 80 52 18 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...R..........s0
07B0: 35 32 45 01 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  52E..........ovl
07C0: 31 00 80 45 18 80 F0 FF  FF 7F F0 FF FF 7F 73 30  1..E..........s0
07D0: 35 36 00 80 1C 11 80 27  0B 21 A1 07 01 03 27 0B  56.....'.!....'.
07E0: 22 A1 07 01 03 27 0B 20  A1 07 01 03 52 18 80 F0  "....'. ....R...
07F0: FF FF 7F F0 FF FF 7F 73  30 35 36 45 18 80 F0 FF  .......s056E....
0800: FF 7F F0 FF FF 7F 73 30  35 33 00 80 1C 01 80 45  ......s053.....E
0810: 0D 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 31 00 80  ..........who1..
0820: 1C 11 80 5C 00 13 80 5C  01 13 80 52 18 80 F0 FF  ...\...\...R....
0830: FF 7F F0 FF FF 7F 73 30  35 33 45 18 80 F0 FF FF  ......s053E.....
0840: 7F F0 FF FF 7F 73 30 35  38 00 80 1C 12 80 52 18  .....s058.....R.
0850: 80 F0 FF FF 7F F0 FF FF  7F 73 30 35 38 46 00 45  .........s058F.E
0860: 0D 80 F0 FF FF 7F F0 FF  FF 7F 77 68 69 31 00 80  ..........whi1..
0870: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x03DE [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x03E0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x03E1 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x03E3 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
  4: 0x03E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x03F9 [0x1C] WAIT(200* ticks)
  6: 0x03FC [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  7: 0x03FF [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI01 (ID: 17277211/0x0107A11B)
  8: 0x0405 [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI02 (ID: 17277212/0x0107A11C)
  9: 0x040B [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI03 (ID: 17277213/0x0107A11D)
 10: 0x0411 [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI04 (ID: 17277214/0x0107A11E)
 11: 0x0417 [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI05 (ID: 17277215/0x0107A11F)
 12: 0x041D [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI06 (ID: 17277216/0x0107A120)
 13: 0x0423 [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI07 (ID: 17277217/0x0107A121)
 14: 0x0429 [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI08 (ID: 17277218/0x0107A122)
 15: 0x042F [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI09 (ID: 17277219/0x0107A123)
 16: 0x0435 [0x4E] SET_ENTITY_HIDE_FLAG: Show KODAI10 (ID: 17277220/0x0107A124)
 17: 0x043B [0x80] LOAD_WAIT(entity=KODAI01 (ID: 17277211/0x0107A11B))
 18: 0x0440 [0x80] LOAD_WAIT(entity=KODAI02 (ID: 17277212/0x0107A11C))
 19: 0x0445 [0x80] LOAD_WAIT(entity=KODAI03 (ID: 17277213/0x0107A11D))
 20: 0x044A [0x80] LOAD_WAIT(entity=KODAI04 (ID: 17277214/0x0107A11E))
 21: 0x044F [0x80] LOAD_WAIT(entity=KODAI05 (ID: 17277215/0x0107A11F))
 22: 0x0454 [0x80] LOAD_WAIT(entity=KODAI06 (ID: 17277216/0x0107A120))
 23: 0x0459 [0x80] LOAD_WAIT(entity=KODAI07 (ID: 17277217/0x0107A121))
 24: 0x045E [0x80] LOAD_WAIT(entity=KODAI08 (ID: 17277218/0x0107A122))
 25: 0x0463 [0x80] LOAD_WAIT(entity=KODAI09 (ID: 17277219/0x0107A123))
 26: 0x0468 [0x80] LOAD_WAIT(entity=KODAI10 (ID: 17277220/0x0107A124))
 27: 0x046D [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI01 (ID: 17277211/0x0107A11B), end_alpha=0*, fade_time=2*)
 28: 0x0476 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI02 (ID: 17277212/0x0107A11C), end_alpha=0*, fade_time=2*)
 29: 0x047F [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI03 (ID: 17277213/0x0107A11D), end_alpha=0*, fade_time=2*)
 30: 0x0488 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI04 (ID: 17277214/0x0107A11E), end_alpha=0*, fade_time=2*)
 31: 0x0491 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI05 (ID: 17277215/0x0107A11F), end_alpha=0*, fade_time=2*)
 32: 0x049A [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI06 (ID: 17277216/0x0107A120), end_alpha=0*, fade_time=2*)
 33: 0x04A3 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI07 (ID: 17277217/0x0107A121), end_alpha=0*, fade_time=2*)
 34: 0x04AC [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI08 (ID: 17277218/0x0107A122), end_alpha=0*, fade_time=2*)
 35: 0x04B5 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI09 (ID: 17277219/0x0107A123), end_alpha=0*, fade_time=2*)
 36: 0x04BE [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI10 (ID: 17277220/0x0107A124), end_alpha=0*, fade_time=2*)
 37: 0x04C7 [0x1C] WAIT(10* ticks)
 38: 0x04CA [0x92] KODAI01 (ID: 17277211/0x0107A11B)->Render.Flags3 ^= 0x01
 39: 0x04D0 [0x92] KODAI02 (ID: 17277212/0x0107A11C)->Render.Flags3 ^= 0x01
 40: 0x04D6 [0x92] KODAI03 (ID: 17277213/0x0107A11D)->Render.Flags3 ^= 0x01
 41: 0x04DC [0x92] KODAI04 (ID: 17277214/0x0107A11E)->Render.Flags3 ^= 0x01
 42: 0x04E2 [0x92] KODAI05 (ID: 17277215/0x0107A11F)->Render.Flags3 ^= 0x01
 43: 0x04E8 [0x92] KODAI06 (ID: 17277216/0x0107A120)->Render.Flags3 ^= 0x01
 44: 0x04EE [0x92] KODAI07 (ID: 17277217/0x0107A121)->Render.Flags3 ^= 0x01
 45: 0x04F4 [0x92] KODAI08 (ID: 17277218/0x0107A122)->Render.Flags3 ^= 0x01
 46: 0x04FA [0x92] KODAI09 (ID: 17277219/0x0107A123)->Render.Flags3 ^= 0x01
 47: 0x0500 [0x92] KODAI10 (ID: 17277220/0x0107A124)->Render.Flags3 ^= 0x01
 48: 0x0506 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x08)
 49: 0x050D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI01 (ID: 17277211/0x0107A11B), tag_num=0x02)
 50: 0x0514 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI02 (ID: 17277212/0x0107A11C), tag_num=0x02)
 51: 0x051B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI03 (ID: 17277213/0x0107A11D), tag_num=0x02)
 52: 0x0522 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI04 (ID: 17277214/0x0107A11E), tag_num=0x02)
 53: 0x0529 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI05 (ID: 17277215/0x0107A11F), tag_num=0x02)
 54: 0x0530 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI06 (ID: 17277216/0x0107A120), tag_num=0x02)
 55: 0x0537 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI07 (ID: 17277217/0x0107A121), tag_num=0x02)
 56: 0x053E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI08 (ID: 17277218/0x0107A122), tag_num=0x02)
 57: 0x0545 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI09 (ID: 17277219/0x0107A123), tag_num=0x02)
 58: 0x054C [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KODAI10 (ID: 17277220/0x0107A124), tag_num=0x02)
 59: 0x0553 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s050" with entities [LocalPlayer, LocalPlayer], work=[252*, 0*]
 60: 0x0564 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 61: 0x0575 [0x02] IF !(Work_Zone[5] == 1*) GOTO 0x0591
 62: 0x057D [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[40*, 0*]
 63: 0x058E [0x01] GOTO 0x05AA
 64: 0x0591 [0x02] IF !(Work_Zone[5] == 2*) GOTO 0x05AA
 65: 0x0599 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[41*, 0*]

SUBROUTINE_05AA:
 66: 0x05AA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s050" with entities [LocalPlayer, LocalPlayer], work=252*
 67: 0x05B9 [0x48] [System] [7329*]:
    → "A haunting song suddenly echoes throughout the ruins..."
 68: 0x05BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 69: 0x05BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 70: 0x05CE [0x1C] WAIT(60* ticks)
 71: 0x05D1 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 204*
 72: 0x05D5 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 204*
 73: 0x05D9 [0x1C] WAIT(200* ticks)
 74: 0x05DC [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI01 (ID: 17277211/0x0107A11B), end_alpha=50*, fade_time=1*)
 75: 0x05E5 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI02 (ID: 17277212/0x0107A11C), end_alpha=50*, fade_time=1*)
 76: 0x05EE [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI03 (ID: 17277213/0x0107A11D), end_alpha=50*, fade_time=1*)
 77: 0x05F7 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI04 (ID: 17277214/0x0107A11E), end_alpha=50*, fade_time=1*)
 78: 0x0600 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI05 (ID: 17277215/0x0107A11F), end_alpha=50*, fade_time=1*)
 79: 0x0609 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI06 (ID: 17277216/0x0107A120), end_alpha=50*, fade_time=1*)
 80: 0x0612 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI07 (ID: 17277217/0x0107A121), end_alpha=50*, fade_time=1*)
 81: 0x061B [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI08 (ID: 17277218/0x0107A122), end_alpha=50*, fade_time=1*)
 82: 0x0624 [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI09 (ID: 17277219/0x0107A123), end_alpha=50*, fade_time=1*)
 83: 0x062D [0x6C] FADE_ENTITY_COLOR(entity_id=KODAI10 (ID: 17277220/0x0107A124), end_alpha=50*, fade_time=1*)
 84: 0x0636 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI01 (ID: 17277211/0x0107A11B), KODAI01 (ID: 17277211/0x0107A11B)], work=[38*, 0*]
 85: 0x0647 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI02 (ID: 17277212/0x0107A11C), KODAI02 (ID: 17277212/0x0107A11C)], work=[38*, 0*]
 86: 0x0658 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI03 (ID: 17277213/0x0107A11D), KODAI03 (ID: 17277213/0x0107A11D)], work=[38*, 0*]
 87: 0x0669 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI04 (ID: 17277214/0x0107A11E), KODAI04 (ID: 17277214/0x0107A11E)], work=[38*, 0*]
 88: 0x067A [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI05 (ID: 17277215/0x0107A11F), KODAI05 (ID: 17277215/0x0107A11F)], work=[38*, 0*]
 89: 0x068B [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI06 (ID: 17277216/0x0107A120), KODAI06 (ID: 17277216/0x0107A120)], work=[38*, 0*]
 90: 0x069C [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI07 (ID: 17277217/0x0107A121), KODAI07 (ID: 17277217/0x0107A121)], work=[38*, 0*]
 91: 0x06AD [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI08 (ID: 17277218/0x0107A122), KODAI08 (ID: 17277218/0x0107A122)], work=[38*, 0*]
 92: 0x06BE [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI09 (ID: 17277219/0x0107A123), KODAI09 (ID: 17277219/0x0107A123)], work=[38*, 0*]
 93: 0x06CF [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [KODAI10 (ID: 17277220/0x0107A124), KODAI10 (ID: 17277220/0x0107A124)], work=[38*, 0*]
 94: 0x06E0 [0x27] REQ_SET(priority=0x0B, entity_id=KODAI01 (ID: 17277211/0x0107A11B), tag_num=0x03)
 95: 0x06E7 [0x27] REQ_SET(priority=0x0B, entity_id=KODAI02 (ID: 17277212/0x0107A11C), tag_num=0x03)
 96: 0x06EE [0x27] REQ_SET(priority=0x0B, entity_id=KODAI03 (ID: 17277213/0x0107A11D), tag_num=0x03)
 97: 0x06F5 [0x27] REQ_SET(priority=0x0B, entity_id=KODAI04 (ID: 17277214/0x0107A11E), tag_num=0x03)
 98: 0x06FC [0x27] REQ_SET(priority=0x0B, entity_id=KODAI05 (ID: 17277215/0x0107A11F), tag_num=0x03)
 99: 0x0703 [0x27] REQ_SET(priority=0x0B, entity_id=KODAI09 (ID: 17277219/0x0107A123), tag_num=0x03)
100: 0x070A [0x27] REQ_SET(priority=0x0B, entity_id=KODAI10 (ID: 17277220/0x0107A124), tag_num=0x03)
101: 0x0711 [0x52] END_LOAD_SCHEDULER: End scheduler "s050" with entities [LocalPlayer, LocalPlayer], work=252*
102: 0x0720 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s051" with entities [LocalPlayer, LocalPlayer], work=[252*, 0*]
103: 0x0731 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
104: 0x0742 [0x1C] WAIT(100* ticks)
105: 0x0745 [0x52] END_LOAD_SCHEDULER: End scheduler "s051" with entities [LocalPlayer, LocalPlayer], work=252*
106: 0x0754 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s055" with entities [LocalPlayer, LocalPlayer], work=[252*, 0*]
107: 0x0765 [0x4B] UPDATE_ENTITY_YAW(entity=LocalPlayer, yaw=5.6°*)
108: 0x076C [0x1C] WAIT(120* ticks)
109: 0x076F [0x52] END_LOAD_SCHEDULER: End scheduler "s055" with entities [LocalPlayer, LocalPlayer], work=252*
110: 0x077E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
111: 0x078F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s052" with entities [LocalPlayer, LocalPlayer], work=[252*, 0*]
112: 0x07A0 [0x1C] WAIT(100* ticks)
113: 0x07A3 [0x52] END_LOAD_SCHEDULER: End scheduler "s052" with entities [LocalPlayer, LocalPlayer], work=252*
114: 0x07B2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
115: 0x07C3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s056" with entities [LocalPlayer, LocalPlayer], work=[252*, 0*]
116: 0x07D4 [0x1C] WAIT(100* ticks)
117: 0x07D7 [0x27] REQ_SET(priority=0x0B, entity_id=KODAI07 (ID: 17277217/0x0107A121), tag_num=0x03)
118: 0x07DE [0x27] REQ_SET(priority=0x0B, entity_id=KODAI08 (ID: 17277218/0x0107A122), tag_num=0x03)
119: 0x07E5 [0x27] REQ_SET(priority=0x0B, entity_id=KODAI06 (ID: 17277216/0x0107A120), tag_num=0x03)
120: 0x07EC [0x52] END_LOAD_SCHEDULER: End scheduler "s056" with entities [LocalPlayer, LocalPlayer], work=252*
121: 0x07FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s053" with entities [LocalPlayer, LocalPlayer], work=[252*, 0*]
122: 0x080C [0x1C] WAIT(200* ticks)
123: 0x080F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
124: 0x0820 [0x1C] WAIT(100* ticks)
125: 0x0823 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 211*
126: 0x0827 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 211*
127: 0x082B [0x52] END_LOAD_SCHEDULER: End scheduler "s053" with entities [LocalPlayer, LocalPlayer], work=252*
128: 0x083A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s058" with entities [LocalPlayer, LocalPlayer], work=[252*, 0*]
129: 0x084B [0x1C] WAIT(60* ticks)
130: 0x084E [0x52] END_LOAD_SCHEDULER: End scheduler "s058" with entities [LocalPlayer, LocalPlayer], work=252*
131: 0x085D [0x46] CAMERA_CONTROL: Restore default settings
132: 0x085F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
133: 0x0870 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
134: 0x0872 [0x21] END_EVENT
135: 0x0873 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0874    |
| Data Size    | 136 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0870:             42 03 00 00  09 10 1A D8 09 46 01 38      B........F.8
0880: 02 80 27 10 F0 FF FF 7F  08 1C 1D 80 45 1E 80 F0  ..'.........E...
0890: FF FF 7F F0 FF FF 7F 6B  6E 73 31 00 80 45 01 80  .......kns1..E..
08A0: F0 FF FF 7F F0 FF FF 7F  66 64 69 32 00 80 6E F0  ........fdi2..n.
08B0: FF FF 7F 1F 80 99 F0 FF  FF 7F 02 00 00 00 80 00  ................
08C0: C9 08 48 20 80 23 01 CD  08 48 21 80 23 99 F0 FF  ..H .#...H!.#...
08D0: FF 7F 1A D8 09 1C 22 80  52 1E 80 F0 FF FF 7F F0  ......".R.......
08E0: FF FF 7F 6B 6E 73 31 46  00 45 01 80 F0 FF FF 7F  ...kns1F.E......
08F0: F0 FF FF 7F 66 64 69 32  00 80 21 00              ....fdi2..!.    
```

#### Opcodes

```
  0: 0x0874 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0875 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[9]
  2: 0x087A [0x1A] CALL_SUBROUTINE(address=0x09D8)
  3: 0x087D [0x46] CAMERA_CONTROL: Disable user control
  4: 0x087F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x0882 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x08)
  6: 0x0889 [0x1C] WAIT(15* ticks)
  7: 0x088C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "kns1" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
  8: 0x089D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x08AE [0x6E] LocalPlayer uses emote 3*
 10: 0x08B5 [0x99] Wait for LocalPlayer animation to complete
 11: 0x08BA [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x08C9
 12: 0x08C2 [0x48] [System] [7435*]:
    → "You immerse the $0 and $1 in the waters of the spring."
 13: 0x08C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x08C6 [0x01] GOTO 0x08CD
 15: 0x08C9 [0x48] [System] [7436*]:
    → "You immerse the shards of the five Crystal Warriors, along with the $0 and $1, in the waters of the spring."
 16: 0x08CC [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_08CD:
 17: 0x08CD [0x99] Wait for LocalPlayer animation to complete
 18: 0x08D2 [0x1A] CALL_SUBROUTINE(address=0x09D8)
 19: 0x08D5 [0x1C] WAIT(45* ticks)
 20: 0x08D8 [0x52] END_LOAD_SCHEDULER: End scheduler "kns1" with entities [LocalPlayer, LocalPlayer], work=215*
 21: 0x08E7 [0x46] CAMERA_CONTROL: Restore default settings
 22: 0x08E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x08FA [0x21] END_EVENT
 24: 0x08FB [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x08FC    |
| Data Size    | 778 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
08F0:                                      42 1A D8 09              B...
0900: 46 01 38 02 80 27 10 F0  FF FF 7F 08 1C 1D 80 45  F.8..'.........E
0910: 1E 80 F0 FF FF 7F F0 FF  FF 7F 6B 6E 73 31 00 80  ..........kns1..
0920: 45 01 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 32 00  E..........fdi2.
0930: 80 6E F0 FF FF 7F 1F 80  99 F0 FF FF 7F 03 02 10  .n..............
0940: 23 80 48 24 80 23 99 F0  FF FF 7F 1A D8 09 1C 22  #.H$.#........."
0950: 80 52 1E 80 F0 FF FF 7F  F0 FF FF 7F 6B 6E 73 31  .R..........kns1
0960: 46 00 45 01 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  F.E..........fdi
0970: 32 00 80 21 00 45 01 80  F0 FF FF 7F F0 FF FF 7F  2..!.E..........
0980: 66 64 69 30 00 80 55 01  80 F0 FF FF 7F F0 FF FF  fdi0..U.........
0990: 7F 66 64 69 30 1B 45 01  80 F0 FF FF 7F F0 FF FF  .fdi0.E.........
09A0: 7F 66 64 6F 30 00 80 55  01 80 F0 FF FF 7F F0 FF  .fdo0..U........
09B0: FF 7F 66 64 6F 30 1B 45  01 80 F0 FF FF 7F F0 FF  ..fdo0.E........
09C0: FF 7F 66 64 69 31 00 80  55 01 80 F0 FF FF 7F F0  ..fdi1..U.......
09D0: FF FF 7F 66 64 69 31 1B  45 01 80 F0 FF FF 7F F0  ...fdi1.E.......
09E0: FF FF 7F 66 64 6F 31 00  80 55 01 80 F0 FF FF 7F  ...fdo1..U......
09F0: F0 FF FF 7F 66 64 6F 31  1B 45 0D 80 F0 FF FF 7F  ....fdo1.E......
0A00: F0 FF FF 7F 77 68 69 31  00 80 55 0D 80 F0 FF FF  ....whi1..U.....
0A10: 7F F0 FF FF 7F 77 68 69  31 1B 45 0D 80 F0 FF FF  .....whi1.E.....
0A20: 7F F0 FF FF 7F 77 68 6F  31 00 80 55 0D 80 F0 FF  .....who1..U....
0A30: FF 7F F0 FF FF 7F 77 68  6F 31 1B 45 0D 80 F0 FF  ......who1.E....
0A40: FF 7F F0 FF FF 7F 77 68  6F 32 00 80 55 0D 80 F0  ......who2..U...
0A50: FF FF 7F F0 FF FF 7F 77  68 6F 32 1B 45 0D 80 F0  .......who2.E...
0A60: FF FF 7F F0 FF FF 7F 77  68 6F 33 00 80 55 0D 80  .......who3..U..
0A70: F0 FF FF 7F F0 FF FF 7F  77 68 6F 33 1B 62 05 80  ........who3.b..
0A80: F0 FF FF 7F F0 FF FF 7F  6D 61 69 6E 00 80 1C 22  ........main..."
0A90: 80 45 01 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0AA0: 00 80 55 01 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
0AB0: 31 1B 45 01 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  1.E..........fdi
0AC0: 31 00 80 62 17 80 F0 FF  FF 7F F0 FF FF 7F 6D 61  1..b..........ma
0AD0: 69 6E 00 80 1C 25 80 55  01 80 F0 FF FF 7F F0 FF  in...%.U........
0AE0: FF 7F 66 64 69 31 1B 45  01 80 F0 FF FF 7F F0 FF  ..fdi1.E........
0AF0: FF 7F 62 6C 6F 6E 00 80  45 0D 80 F0 FF FF 7F F0  ..blon..E.......
0B00: FF FF 7F 62 6C 6F 6E 00  80 1B 45 0D 80 F0 FF FF  ...blon...E.....
0B10: 7F F0 FF FF 7F 77 68 69  30 00 80 55 0D 80 F0 FF  .....whi0..U....
0B20: FF 7F F0 FF FF 7F 77 68  69 30 1B 45 0D 80 F0 FF  ......whi0.E....
0B30: FF 7F F0 FF FF 7F 77 68  6F 30 00 80 55 0D 80 F0  ......who0..U...
0B40: FF FF 7F F0 FF FF 7F 77  68 6F 30 1B 45 1E 80 F0  .......who0.E...
0B50: FF FF 7F F0 FF FF 7F 65  66 6F 6E 00 80 55 1E 80  .......efon..U..
0B60: F0 FF FF 7F F0 FF FF 7F  65 66 6F 6E 1B 45 01 80  ........efon.E..
0B70: F0 FF FF 7F F0 FF FF 7F  66 64 69 73 00 80 1B 45  ........fdis...E
0B80: 01 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 73 00 80  ..........fdos..
0B90: 55 01 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 73 1B  U..........fdos.
0BA0: 45 01 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 66 00  E..........fdif.
0BB0: 80 1B 45 01 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0BC0: 66 00 80 55 01 80 F0 FF  FF 7F F0 FF FF 7F 66 64  f..U..........fd
0BD0: 6F 66 1B 45 01 80 F0 FF  FF 7F F0 FF FF 7F 66 64  of.E..........fd
0BE0: 69 70 00 80 1B 45 01 80  F0 FF FF 7F F0 FF FF 7F  ip...E..........
0BF0: 66 64 6F 70 00 80 55 01  80 F0 FF FF 7F F0 FF FF  fdop..U.........
0C00: 7F 66 64 6F 70 1B                                 .fdop.          
```

#### Opcodes

```
  0: 0x08FC [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x08FD [0x1A] CALL_SUBROUTINE(address=0x09D8)
  2: 0x0900 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0902 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  4: 0x0905 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x08)
  5: 0x090C [0x1C] WAIT(15* ticks)
  6: 0x090F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "kns1" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
  7: 0x0920 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0931 [0x6E] LocalPlayer uses emote 3*
  9: 0x0938 [0x99] Wait for LocalPlayer animation to complete
 10: 0x093D [0x03] Work_Zone[2] = 1261*
 11: 0x0942 [0x48] [System] [7439*]:
    → "You immerse the shards of the five Crystal Warriors, along with the $0, in the waters of the spring."
 12: 0x0945 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0946 [0x99] Wait for LocalPlayer animation to complete
 14: 0x094B [0x1A] CALL_SUBROUTINE(address=0x09D8)
 15: 0x094E [0x1C] WAIT(45* ticks)
 16: 0x0951 [0x52] END_LOAD_SCHEDULER: End scheduler "kns1" with entities [LocalPlayer, LocalPlayer], work=215*
 17: 0x0960 [0x46] CAMERA_CONTROL: Restore default settings
 18: 0x0962 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0973 [0x21] END_EVENT
 20: 0x0974 [0x00] END_REQSTACK()

SUBROUTINE_09D8:
 21: 0x09D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x09E9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 23: 0x09F8 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0975 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0986 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0995 [0x1B] RETURN
     0x0996 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x09A7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x09B6 [0x1B] RETURN
     0x09B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x09C8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x09D7 [0x1B] RETURN
# Dead code (unreachable instructions):
     0x09F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0A0A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0A19 [0x1B] RETURN
     0x0A1A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0A2B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0A3A [0x1B] RETURN
     0x0A3B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0A4C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0A5B [0x1B] RETURN
     0x0A5C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0A6D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0A7C [0x1B] RETURN
     0x0A7D [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x0A8E [0x1C] WAIT(45* ticks)
     0x0A91 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0AA2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0AB1 [0x1B] RETURN
     0x0AB2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0AC3 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x0AD4 [0x1C] WAIT(30* ticks)
     0x0AD7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0AE6 [0x1B] RETURN
     0x0AE7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0AF8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0B09 [0x1B] RETURN
     0x0B0A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0B1B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0B2A [0x1B] RETURN
     0x0B2B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0B3C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0B4B [0x1B] RETURN
     0x0B4C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x0B5D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x0B6C [0x1B] RETURN
     0x0B6D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0B7E [0x1B] RETURN
     0x0B7F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0B90 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0B9F [0x1B] RETURN
     0x0BA0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0BB1 [0x1B] RETURN
     0x0BB2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0BC3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0BD2 [0x1B] RETURN
     0x0BD3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0BE4 [0x1B] RETURN
     0x0BE5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0BF6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0C05 [0x1B] RETURN
```
