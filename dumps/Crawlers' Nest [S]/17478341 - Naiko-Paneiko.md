# 17478341 - Naiko-Paneiko

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Crawlers' Nest [S] (ID: 171) |
| Block Size       | 1860 bytes                   |
| Total Events     | 7                            |
| References Count | 45                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [16](#event-16)       | 0x0001       |    611 |             81 |
| [17](#event-17)       | 0x0264       |    322 |             46 |
| [18](#event-18)       | 0x03A6       |    302 |             44 |
| [19](#event-19)       | 0x04D4       |    347 |             48 |
| [20](#event-20)       | 0x062F       |     26 |              8 |
| [21](#event-21)       | 0x0649       |     26 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0013      |          19 |
|       3 | 0x48761     |      296801 |
|       4 | 0xFFFF91F0  |  4294939120 |
|       5 | 0xFFFF7FB7  |  4294934455 |
|       6 | 0x07C0      |        1984 |
|       7 | 0x003C      |          60 |
|       8 | 0x013B      |         315 |
|       9 | 0x00B6      |         182 |
|      10 | 0x1DA6      |        7590 |
|      11 | 0x000F      |          15 |
|      12 | 0x0031      |          49 |
|      13 | 0x1DA7      |        7591 |
|      14 | 0x1DA8      |        7592 |
|      15 | 0x1DA9      |        7593 |
|      16 | 0x1DAA      |        7594 |
|      17 | 0x1DAB      |        7595 |
|      18 | 0x0004      |           4 |
|      19 | 0x1DAC      |        7596 |
|      20 | 0x1DAD      |        7597 |
|      21 | 0x1DAE      |        7598 |
|      22 | 0x1DB0      |        7600 |
|      23 | 0x0022      |          34 |
|      24 | 0x1DB1      |        7601 |
|      25 | 0x0078      |         120 |
|      26 | 0x001E      |          30 |
|      27 | 0x0021      |          33 |
|      28 | 0x1DB9      |        7609 |
|      29 | 0x1DBB      |        7611 |
|      30 | 0x1DBC      |        7612 |
|      31 | 0x005A      |          90 |
|      32 | 0x001D      |          29 |
|      33 | 0x1DBA      |        7610 |
|      34 | 0x002D      |          45 |
|      35 | 0x000D      |          13 |
|      36 | 0x1DB4      |        7604 |
|      37 | 0x1DB5      |        7605 |
|      38 | 0x1DB6      |        7606 |
|      39 | 0x1DB8      |        7608 |
|      40 | 0x00C9      |         201 |
|      41 | 0x1DBD      |        7613 |
|      42 | 0x1DBE      |        7614 |
|      43 | 0x1DB2      |        7602 |
|      44 | 0x1DB3      |        7603 |

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

### Event 16

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 611 bytes |
| Instructions | 81        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 45 00 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F   BE..........fdo
0010: 31 01 80 55 00 80 F8 FF  FF 7F F8 FF FF 7F 66 64  1..U..........fd
0020: 6F 31 46 01 38 02 80 92  01 C5 B2 0A 01 94 01 F0  o1F.8...........
0030: FF FF 7F 94 01 C5 B2 0A  01 BA F0 FF FF 7F 03 80  ................
0040: 04 80 05 80 06 80 4E 00  C5 B2 0A 01 4A F0 FF FF  ......N.....J...
0050: 7F C5 B2 0A 01 4A C5 B2  0A 01 F0 FF FF 7F 80 C5  .....J..........
0060: B2 0A 01 1C 07 80 45 08  80 F0 FF FF 7F F0 FF FF  ......E.........
0070: 7F 6E 30 30 30 01 80 45  00 80 F0 FF FF 7F F0 FF  .n000..E........
0080: FF 7F 66 64 69 31 01 80  5C 00 09 80 5C 01 09 80  ..fdi1..\...\...
0090: 9A 1C 07 80 6E C5 B2 0A  01 01 80 99 C5 B2 0A 01  ....n...........
00A0: 2B C5 B2 0A 01 0A 80 23  99 C5 B2 0A 01 52 08 80  +......#.....R..
00B0: F0 FF FF 7F F0 FF FF 7F  6E 30 30 30 45 08 80 F0  ........n000E...
00C0: FF FF 7F F0 FF FF 7F 6E  30 30 31 01 80 1C 0B 80  .......n001.....
00D0: 66 0C 80 C5 B2 0A 01 C5  B2 0A 01 74 68 6B 31 2B  f..........thk1+
00E0: C5 B2 0A 01 0D 80 23 66  0C 80 C5 B2 0A 01 C5 B2  ......#f........
00F0: 0A 01 74 68 6B 32 2B C5  B2 0A 01 0E 80 23 52 08  ..thk2+......#R.
0100: 80 F0 FF FF 7F F0 FF FF  7F 6E 30 30 31 45 08 80  .........n001E..
0110: F0 FF FF 7F F0 FF FF 7F  6E 30 30 32 01 80 2B C5  ........n002..+.
0120: B2 0A 01 0F 80 23 6E C5  B2 0A 01 01 80 99 C5 B2  .....#n.........
0130: 0A 01 2B C5 B2 0A 01 10  80 23 99 C5 B2 0A 01 52  ..+......#.....R
0140: 08 80 F0 FF FF 7F F0 FF  FF 7F 6E 30 30 32 45 08  ..........n002E.
0150: 80 F0 FF FF 7F F0 FF FF  7F 6E 30 30 33 01 80 2B  .........n003..+
0160: C5 B2 0A 01 11 80 23 6E  C5 B2 0A 01 12 80 99 C5  ......#n........
0170: B2 0A 01 2B C5 B2 0A 01  13 80 23 99 C5 B2 0A 01  ...+......#.....
0180: 52 08 80 F0 FF FF 7F F0  FF FF 7F 6E 30 30 33 45  R..........n003E
0190: 08 80 F0 FF FF 7F F0 FF  FF 7F 6E 30 30 34 01 80  ..........n004..
01A0: 66 0C 80 C5 B2 0A 01 C5  B2 0A 01 74 6C 6B 30 2B  f..........tlk0+
01B0: C5 B2 0A 01 14 80 23 2B  C5 B2 0A 01 15 80 23 66  ......#+......#f
01C0: 0C 80 C5 B2 0A 01 C5 B2  0A 01 74 6C 6B 31 52 08  ..........tlk1R.
01D0: 80 F0 FF FF 7F F0 FF FF  7F 6E 30 30 34 45 08 80  .........n004E..
01E0: F0 FF FF 7F F0 FF FF 7F  6E 30 30 35 01 80 2B C5  ........n005..+.
01F0: B2 0A 01 16 80 23 6E C5  B2 0A 01 17 80 99 C5 B2  .....#n.........
0200: 0A 01 2B C5 B2 0A 01 18  80 23 99 C5 B2 0A 01 1C  ..+......#......
0210: 07 80 5D 01 80 19 80 45  00 80 F8 FF FF 7F F8 FF  ..]....E........
0220: FF 7F 66 64 6F 31 01 80  55 00 80 F8 FF FF 7F F8  ..fdo1..U.......
0230: FF FF 7F 66 64 6F 31 52  08 80 F0 FF FF 7F F0 FF  ...fdo1R........
0240: FF 7F 6E 30 30 35 5C 00  01 80 5C 01 01 80 9A 46  ..n005\...\....F
0250: 00 45 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 32  .E..........fdi2
0260: 01 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0013 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
  3: 0x0022 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0024 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x0027 [0x92] Naiko-Paneiko (ID: 17478341/0x010AB2C5)->Render.Flags3 ^= 0x01
  6: 0x002D [0x94] LocalPlayer->Render.Flags3 ^= 0x01
  7: 0x0033 [0x94] Naiko-Paneiko (ID: 17478341/0x010AB2C5)->Render.Flags3 ^= 0x01
  8: 0x0039 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=296.801*, pos_z=-28.176*, pos_y=-32.841*, direction=174.4°*)
  9: 0x0046 [0x4E] SET_ENTITY_HIDE_FLAG: Show Naiko-Paneiko (ID: 17478341/0x010AB2C5)
 10: 0x004C [0x4A] LocalPlayer looks at Naiko-Paneiko (ID: 17478341/0x010AB2C5)
 11: 0x0055 [0x4A] Naiko-Paneiko (ID: 17478341/0x010AB2C5) looks at LocalPlayer
 12: 0x005E [0x80] LOAD_WAIT(entity=Naiko-Paneiko (ID: 17478341/0x010AB2C5))
 13: 0x0063 [0x1C] WAIT(60* ticks)
 14: 0x0066 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n000" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 15: 0x0077 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0088 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 182*
 17: 0x008C [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 182*
 18: 0x0090 [0x9A] WAIT_MUSIC_SERVER()
 19: 0x0091 [0x1C] WAIT(60* ticks)
 20: 0x0094 [0x6E] Naiko-Paneiko (ID: 17478341/0x010AB2C5) uses emote 0*
 21: 0x009B [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 22: 0x00A0 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7590*]:
    → "Hey there, kid, I'm Naiko-Paneiko, up-and-coming ace journalist. Journeying to the remotest frontlines of battle to cover all the news that's fit to printaru!"
 23: 0x00A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x00A8 [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 25: 0x00AD [0x52] END_LOAD_SCHEDULER: End scheduler "n000" with entities [LocalPlayer, LocalPlayer], work=315*
 26: 0x00BC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n001" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 27: 0x00CD [0x1C] WAIT(15* ticks)
 28: 0x00D0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Naiko-Paneiko (ID: 17478341/0x010AB2C5), Naiko-Paneiko (ID: 17478341/0x010AB2C5)], work=49*
 29: 0x00DF [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7591*]:
    → "I'll travel all over Vana'diel if I have to! To tell people the truth! The real truth about this war that the wartime papers aren't printing!"
 30: 0x00E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x00E7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Naiko-Paneiko (ID: 17478341/0x010AB2C5), Naiko-Paneiko (ID: 17478341/0x010AB2C5)], work=49*
 32: 0x00F6 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7592*]:
    → "...Oh, what's this? You've got a slight air of journalism about you, kid. Whaddaya say? Wanna help a Taru out?"
 33: 0x00FD [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x00FE [0x52] END_LOAD_SCHEDULER: End scheduler "n001" with entities [LocalPlayer, LocalPlayer], work=315*
 35: 0x010D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n002" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 36: 0x011E [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7593*]:
    → "There's just two things a good journalist has gotta have, kid! Impeccable verbiage, and a nose for the truth! And, well...and feet, I suppose...to go story-hunting... Three things!"
 37: 0x0125 [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x0126 [0x6E] Naiko-Paneiko (ID: 17478341/0x010AB2C5) uses emote 0*
 39: 0x012D [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 40: 0x0132 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7594*]:
    → "And I sense all of those things in you. Especially the feet! You're practically overflowing with journalistic vibes, kid! A natural-born newshound! And I'm not only saying that because I'm tragically shorthanded, either."
 41: 0x0139 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x013A [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 43: 0x013F [0x52] END_LOAD_SCHEDULER: End scheduler "n002" with entities [LocalPlayer, LocalPlayer], work=315*
 44: 0x014E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n003" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 45: 0x015F [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7595*]:
    → "In fact, it so happens that I just received a hotaru lead! I was eavesdropping on some sol--I mean... I overheard some soldiers talking the other day. Yeah, that's it!"
 46: 0x0166 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x0167 [0x6E] Naiko-Paneiko (ID: 17478341/0x010AB2C5) uses emote 4*
 48: 0x016E [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 49: 0x0173 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7596*]:
    → "Rumor has it that a peculiar oddity of a monster has appeared in the Rolanberry Fields."
 50: 0x017A [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x017B [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 52: 0x0180 [0x52] END_LOAD_SCHEDULER: End scheduler "n003" with entities [LocalPlayer, LocalPlayer], work=315*
 53: 0x018F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n004" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 54: 0x01A0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Naiko-Paneiko (ID: 17478341/0x010AB2C5), Naiko-Paneiko (ID: 17478341/0x010AB2C5)], work=49*
 55: 0x01AF [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7597*]:
    → "Supposedly some soldiers have been dispatched to take care of it. So go track them down and find out exactly whataru is going on, kid!"
 56: 0x01B6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x01B7 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7598*]:
    → "Here ya go. Use this to reportaru back as soon as you hear something."
 58: 0x01BE [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x01BF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Naiko-Paneiko (ID: 17478341/0x010AB2C5), Naiko-Paneiko (ID: 17478341/0x010AB2C5)], work=49*
 60: 0x01CE [0x52] END_LOAD_SCHEDULER: End scheduler "n004" with entities [LocalPlayer, LocalPlayer], work=315*
 61: 0x01DD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n005" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 62: 0x01EE [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7600*]:
    → "You even know how to use a linkpearl, kid? Tell ya what, I'll wait a while and then give you a call."
 63: 0x01F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 64: 0x01F6 [0x6E] Naiko-Paneiko (ID: 17478341/0x010AB2C5) uses emote 34*
 65: 0x01FD [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 66: 0x0202 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7601*]:
    → "Woohoo, this is what we live for, kid! Can't ya feel it!? Now get a move on! There's no time to lose! A cold story is no story at all!"
 67: 0x0209 [0x23] WAIT_FOR_DIALOG_INTERACTION
 68: 0x020A [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 69: 0x020F [0x1C] WAIT(60* ticks)
 70: 0x0212 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=120*)
 71: 0x0217 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 72: 0x0228 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 73: 0x0237 [0x52] END_LOAD_SCHEDULER: End scheduler "n005" with entities [LocalPlayer, LocalPlayer], work=315*
 74: 0x0246 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 75: 0x024A [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 76: 0x024E [0x9A] WAIT_MUSIC_SERVER()
 77: 0x024F [0x46] CAMERA_CONTROL: Restore default settings
 78: 0x0251 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 79: 0x0262 [0x21] END_EVENT
 80: 0x0263 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0264    |
| Data Size    | 322 bytes |
| Instructions | 46        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:             42 45 00 80  F8 FF FF 7F F8 FF FF 7F      BE..........
0270: 66 64 6F 31 01 80 55 00  80 F8 FF FF 7F F8 FF FF  fdo1..U.........
0280: 7F 66 64 6F 31 46 01 38  02 80 4E 00 C5 B2 0A 01  .fdo1F.8..N.....
0290: 92 01 C5 B2 0A 01 94 01  F0 FF FF 7F 94 01 C5 B2  ................
02A0: 0A 01 BA F0 FF FF 7F 03  80 04 80 05 80 06 80 80  ................
02B0: C5 B2 0A 01 4A F0 FF FF  7F C5 B2 0A 01 4A C5 B2  ....J........J..
02C0: 0A 01 F0 FF FF 7F 1C 07  80 5C 00 09 80 5C 01 09  .........\...\..
02D0: 80 9A 45 08 80 F0 FF FF  7F F0 FF FF 7F 6E 30 30  ..E..........n00
02E0: 36 01 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  6..E..........fd
02F0: 69 31 01 80 1C 1A 80 6E  C5 B2 0A 01 1B 80 99 C5  i1.....n........
0300: B2 0A 01 2B C5 B2 0A 01  1C 80 23 2B C5 B2 0A 01  ...+......#+....
0310: 1D 80 23 99 C5 B2 0A 01  52 08 80 F0 FF FF 7F F0  ..#.....R.......
0320: FF FF 7F 6E 30 30 36 45  08 80 F0 FF FF 7F F0 FF  ...n006E........
0330: FF 7F 6E 30 30 37 01 80  6E C5 B2 0A 01 01 80 99  ..n007..n.......
0340: C5 B2 0A 01 2B C5 B2 0A  01 1E 80 23 99 C5 B2 0A  ....+......#....
0350: 01 1C 07 80 5D 01 80 1F  80 45 00 80 F8 FF FF 7F  ....]....E......
0360: F8 FF FF 7F 66 64 6F 31  01 80 55 00 80 F8 FF FF  ....fdo1..U.....
0370: 7F F8 FF FF 7F 66 64 6F  31 52 08 80 F0 FF FF 7F  .....fdo1R......
0380: F0 FF FF 7F 6E 30 30 37  5C 00 01 80 5C 01 01 80  ....n007\...\...
0390: 9A 46 00 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  .F.E..........fd
03A0: 69 32 01 80 21 00                                 i2..!.          
```

#### Opcodes

```
  0: 0x0264 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0265 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0276 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
  3: 0x0285 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0287 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x028A [0x4E] SET_ENTITY_HIDE_FLAG: Show Naiko-Paneiko (ID: 17478341/0x010AB2C5)
  6: 0x0290 [0x92] Naiko-Paneiko (ID: 17478341/0x010AB2C5)->Render.Flags3 ^= 0x01
  7: 0x0296 [0x94] LocalPlayer->Render.Flags3 ^= 0x01
  8: 0x029C [0x94] Naiko-Paneiko (ID: 17478341/0x010AB2C5)->Render.Flags3 ^= 0x01
  9: 0x02A2 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=296.801*, pos_z=-28.176*, pos_y=-32.841*, direction=174.4°*)
 10: 0x02AF [0x80] LOAD_WAIT(entity=Naiko-Paneiko (ID: 17478341/0x010AB2C5))
 11: 0x02B4 [0x4A] LocalPlayer looks at Naiko-Paneiko (ID: 17478341/0x010AB2C5)
 12: 0x02BD [0x4A] Naiko-Paneiko (ID: 17478341/0x010AB2C5) looks at LocalPlayer
 13: 0x02C6 [0x1C] WAIT(60* ticks)
 14: 0x02C9 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 182*
 15: 0x02CD [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 182*
 16: 0x02D1 [0x9A] WAIT_MUSIC_SERVER()
 17: 0x02D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n006" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 18: 0x02E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x02F4 [0x1C] WAIT(30* ticks)
 20: 0x02F7 [0x6E] Naiko-Paneiko (ID: 17478341/0x010AB2C5) uses emote 33*
 21: 0x02FE [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 22: 0x0303 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7609*]:
    → "Oooh, look who's back! We got problems, kid?"
 23: 0x030A [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x030B [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7611*]:
    → "I just don'taru get it. These articles are all based on the finest intelligence gathering. But we can't even sell an issue! And just look at these losses! Get out there and get me some more stories!"
 25: 0x0312 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0313 [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 27: 0x0318 [0x52] END_LOAD_SCHEDULER: End scheduler "n006" with entities [LocalPlayer, LocalPlayer], work=315*
 28: 0x0327 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n007" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 29: 0x0338 [0x6E] Naiko-Paneiko (ID: 17478341/0x010AB2C5) uses emote 0*
 30: 0x033F [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 31: 0x0344 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7612*]:
    → "Rewrite! From the beginning! Go back and get your facts straightaru! Move it!"
 32: 0x034B [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x034C [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 34: 0x0351 [0x1C] WAIT(60* ticks)
 35: 0x0354 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=90*)
 36: 0x0359 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 37: 0x036A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 38: 0x0379 [0x52] END_LOAD_SCHEDULER: End scheduler "n007" with entities [LocalPlayer, LocalPlayer], work=315*
 39: 0x0388 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 40: 0x038C [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 41: 0x0390 [0x9A] WAIT_MUSIC_SERVER()
 42: 0x0391 [0x46] CAMERA_CONTROL: Restore default settings
 43: 0x0393 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 44: 0x03A4 [0x21] END_EVENT
 45: 0x03A5 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x03A6    |
| Data Size    | 302 bytes |
| Instructions | 44        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03A0:                   42 45  00 80 F8 FF FF 7F F8 FF        BE........
03B0: FF 7F 66 64 6F 31 01 80  55 00 80 F8 FF FF 7F F8  ..fdo1..U.......
03C0: FF FF 7F 66 64 6F 31 46  01 38 02 80 4E 00 C5 B2  ...fdo1F.8..N...
03D0: 0A 01 92 01 C5 B2 0A 01  94 01 F0 FF FF 7F 94 01  ................
03E0: C5 B2 0A 01 BA F0 FF FF  7F 03 80 04 80 05 80 06  ................
03F0: 80 4A F0 FF FF 7F C5 B2  0A 01 4A C5 B2 0A 01 F0  .J........J.....
0400: FF FF 7F 80 C5 B2 0A 01  1C 07 80 5C 00 09 80 5C  ...........\...\
0410: 01 09 80 9A 45 08 80 F0  FF FF 7F F0 FF FF 7F 6E  ....E..........n
0420: 30 30 36 01 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  006..E..........
0430: 66 64 69 31 01 80 1C 1A  80 6E C5 B2 0A 01 20 80  fdi1.....n.... .
0440: 99 C5 B2 0A 01 2B C5 B2  0A 01 1C 80 23 2B C5 B2  .....+......#+..
0450: 0A 01 21 80 23 99 C5 B2  0A 01 52 08 80 F0 FF FF  ..!.#.....R.....
0460: 7F F0 FF FF 7F 6E 30 30  36 45 08 80 F0 FF FF 7F  .....n006E......
0470: F0 FF FF 7F 6E 30 30 37  01 80 6E C5 B2 0A 01 17  ....n007..n.....
0480: 80 99 C5 B2 0A 01 2B C5  B2 0A 01 1E 80 23 1C 22  ......+......#."
0490: 80 5D 01 80 1F 80 45 00  80 F8 FF FF 7F F8 FF FF  .]....E.........
04A0: 7F 66 64 6F 31 01 80 55  00 80 F8 FF FF 7F F8 FF  .fdo1..U........
04B0: FF 7F 66 64 6F 31 5C 00  01 80 5C 01 01 80 9A 46  ..fdo1\...\....F
04C0: 00 45 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 32  .E..........fdi2
04D0: 01 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x03A6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x03A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x03B8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
  3: 0x03C7 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x03C9 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x03CC [0x4E] SET_ENTITY_HIDE_FLAG: Show Naiko-Paneiko (ID: 17478341/0x010AB2C5)
  6: 0x03D2 [0x92] Naiko-Paneiko (ID: 17478341/0x010AB2C5)->Render.Flags3 ^= 0x01
  7: 0x03D8 [0x94] LocalPlayer->Render.Flags3 ^= 0x01
  8: 0x03DE [0x94] Naiko-Paneiko (ID: 17478341/0x010AB2C5)->Render.Flags3 ^= 0x01
  9: 0x03E4 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=296.801*, pos_z=-28.176*, pos_y=-32.841*, direction=174.4°*)
 10: 0x03F1 [0x4A] LocalPlayer looks at Naiko-Paneiko (ID: 17478341/0x010AB2C5)
 11: 0x03FA [0x4A] Naiko-Paneiko (ID: 17478341/0x010AB2C5) looks at LocalPlayer
 12: 0x0403 [0x80] LOAD_WAIT(entity=Naiko-Paneiko (ID: 17478341/0x010AB2C5))
 13: 0x0408 [0x1C] WAIT(60* ticks)
 14: 0x040B [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 182*
 15: 0x040F [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 182*
 16: 0x0413 [0x9A] WAIT_MUSIC_SERVER()
 17: 0x0414 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n006" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 18: 0x0425 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0436 [0x1C] WAIT(30* ticks)
 20: 0x0439 [0x6E] Naiko-Paneiko (ID: 17478341/0x010AB2C5) uses emote 29*
 21: 0x0440 [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 22: 0x0445 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7609*]:
    → "Oooh, look who's back! We got problems, kid?"
 23: 0x044C [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x044D [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7610*]:
    → "This just doesn't make any sense! Nothing but columns based on solid factaru, and I'm receiving complaint after complaint from readers saying that they're all fabrications and falsehoods!"
 25: 0x0454 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0455 [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 27: 0x045A [0x52] END_LOAD_SCHEDULER: End scheduler "n006" with entities [LocalPlayer, LocalPlayer], work=315*
 28: 0x0469 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n007" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 29: 0x047A [0x6E] Naiko-Paneiko (ID: 17478341/0x010AB2C5) uses emote 34*
 30: 0x0481 [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 31: 0x0486 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7612*]:
    → "Rewrite! From the beginning! Go back and get your facts straightaru! Move it!"
 32: 0x048D [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x048E [0x1C] WAIT(45* ticks)
 34: 0x0491 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=90*)
 35: 0x0496 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 36: 0x04A7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 37: 0x04B6 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 38: 0x04BA [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 39: 0x04BE [0x9A] WAIT_MUSIC_SERVER()
 40: 0x04BF [0x46] CAMERA_CONTROL: Restore default settings
 41: 0x04C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 42: 0x04D2 [0x21] END_EVENT
 43: 0x04D3 [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x04D4    |
| Data Size    | 347 bytes |
| Instructions | 48        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04D0:             03 00 00 03  10 42 45 00 80 F8 FF FF      .....BE.....
04E0: 7F F8 FF FF 7F 66 64 6F  31 01 80 55 00 80 F8 FF  .....fdo1..U....
04F0: FF 7F F8 FF FF 7F 66 64  6F 31 46 01 38 02 80 4E  ......fdo1F.8..N
0500: 00 C5 B2 0A 01 92 01 C5  B2 0A 01 94 01 F0 FF FF  ................
0510: 7F 94 01 C5 B2 0A 01 BA  F0 FF FF 7F 03 80 04 80  ................
0520: 05 80 06 80 4A F0 FF FF  7F C5 B2 0A 01 1C 07 80  ....J...........
0530: 5C 00 09 80 5C 01 09 80  9A 45 08 80 F0 FF FF 7F  \...\....E......
0540: F0 FF FF 7F 6E 30 30 36  01 80 45 00 80 F0 FF FF  ....n006..E.....
0550: 7F F0 FF FF 7F 66 64 69  31 01 80 1C 1A 80 6E C5  .....fdi1.....n.
0560: B2 0A 01 23 80 99 C5 B2  0A 01 2B C5 B2 0A 01 24  ...#......+....$
0570: 80 23 2B C5 B2 0A 01 25  80 23 99 C5 B2 0A 01 52  .#+....%.#.....R
0580: 08 80 F0 FF FF 7F F0 FF  FF 7F 6E 30 30 36 45 08  ..........n006E.
0590: 80 F0 FF FF 7F F0 FF FF  7F 6E 30 30 37 01 80 66  .........n007..f
05A0: 0C 80 C5 B2 0A 01 C5 B2  0A 01 74 6C 6B 30 02 00  ..........tlk0..
05B0: 00 01 80 00 C1 05 2B C5  B2 0A 01 26 80 23 01 C9  ......+....&.#..
05C0: 05 2B C5 B2 0A 01 27 80  23 1C 07 80 5D 01 80 19  .+....'.#...]...
05D0: 80 45 00 80 F8 FF FF 7F  F8 FF FF 7F 66 64 6F 31  .E..........fdo1
05E0: 01 80 55 00 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  ..U..........fdo
05F0: 31 52 08 80 F0 FF FF 7F  F0 FF FF 7F 6E 30 30 37  1R..........n007
0600: 5C 00 01 80 5C 01 01 80  9A 46 00 45 28 80 F8 FF  \...\....F.E(...
0610: FF 7F F8 FF FF 7F 71 73  74 63 01 80 45 00 80 F0  ......qstc..E...
0620: FF FF 7F F0 FF FF 7F 66  64 69 32 01 80 21 00     .......fdi2..!. 
```

#### Opcodes

```
  0: 0x04D4 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  1: 0x04D9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x04DA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  3: 0x04EB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
  4: 0x04FA [0x46] CAMERA_CONTROL: Disable user control
  5: 0x04FC [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x04FF [0x4E] SET_ENTITY_HIDE_FLAG: Show Naiko-Paneiko (ID: 17478341/0x010AB2C5)
  7: 0x0505 [0x92] Naiko-Paneiko (ID: 17478341/0x010AB2C5)->Render.Flags3 ^= 0x01
  8: 0x050B [0x94] LocalPlayer->Render.Flags3 ^= 0x01
  9: 0x0511 [0x94] Naiko-Paneiko (ID: 17478341/0x010AB2C5)->Render.Flags3 ^= 0x01
 10: 0x0517 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=296.801*, pos_z=-28.176*, pos_y=-32.841*, direction=174.4°*)
 11: 0x0524 [0x4A] LocalPlayer looks at Naiko-Paneiko (ID: 17478341/0x010AB2C5)
 12: 0x052D [0x1C] WAIT(60* ticks)
 13: 0x0530 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 182*
 14: 0x0534 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 182*
 15: 0x0538 [0x9A] WAIT_MUSIC_SERVER()
 16: 0x0539 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n006" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 17: 0x054A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x055B [0x1C] WAIT(30* ticks)
 19: 0x055E [0x6E] Naiko-Paneiko (ID: 17478341/0x010AB2C5) uses emote 13*
 20: 0x0565 [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 21: 0x056A [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7604*]:
    → "Oh, there you are, kid. Greataru work! That was some top-rate info you delivered. I knew I was right about you!"
 22: 0x0571 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0572 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7605*]:
    → "We gotta put this in printaru and get it in the paper-wapers, double-time! It's sure to get rave reviews from our readers!"
 24: 0x0579 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x057A [0x99] Wait for Naiko-Paneiko (ID: 17478341/0x010AB2C5) animation to complete
 26: 0x057F [0x52] END_LOAD_SCHEDULER: End scheduler "n006" with entities [LocalPlayer, LocalPlayer], work=315*
 27: 0x058E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "n007" with entities [LocalPlayer, LocalPlayer], work=[315*, 0*]
 28: 0x059F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Naiko-Paneiko (ID: 17478341/0x010AB2C5), Naiko-Paneiko (ID: 17478341/0x010AB2C5)], work=49*
 29: 0x05AE [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x05C1
 30: 0x05B6 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7606*]:
    → "Here ya go, kid. A little token of appreciation from one journalistaru to another. A good newshound's gotta know where they're going before they can track down the stories. Put it to good use."
 31: 0x05BD [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x05BE [0x01] GOTO 0x05C9
 33: 0x05C1 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7608*]:
    → "Here ya go, kid. Put it to good use."
 34: 0x05C8 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_05C9:
 35: 0x05C9 [0x1C] WAIT(60* ticks)
 36: 0x05CC [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=120*)
 37: 0x05D1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 38: 0x05E2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 39: 0x05F1 [0x52] END_LOAD_SCHEDULER: End scheduler "n007" with entities [LocalPlayer, LocalPlayer], work=315*
 40: 0x0600 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 41: 0x0604 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 42: 0x0608 [0x9A] WAIT_MUSIC_SERVER()
 43: 0x0609 [0x46] CAMERA_CONTROL: Restore default settings
 44: 0x060B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 45: 0x061C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 46: 0x062D [0x21] END_EVENT
 47: 0x062E [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x062F   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0620:                                               1E                 .
0630: F0 FF FF 7F 1C 1A 80 2B  C5 B2 0A 01 29 80 23 2B  .......+....).#+
0640: C5 B2 0A 01 2A 80 23 21  00                       ....*.#!.       
```

#### Opcodes

```
  0: 0x062F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0634 [0x1C] WAIT(30* ticks)
  2: 0x0637 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7613*]:
    → "Alll rightaru! Let's make the news!"
  3: 0x063E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x063F [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7614*]:
    → "I might justaru send you off on another story-hunt, kid. Be ready-weady! A good journalist always is!"
  5: 0x0646 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0647 [0x21] END_EVENT
  7: 0x0648 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0649   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0640:                             1E F0 FF FF 7F 1C 1A           .......
0650: 80 2B C5 B2 0A 01 2B 80  23 2B C5 B2 0A 01 2C 80  .+....+.#+....,.
0660: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0649 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x064E [0x1C] WAIT(30* ticks)
  2: 0x0651 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7602*]:
    → "What are you doing, kid? Get to the Rolanberry Fields rightaru away! There won't be any news left if you don't step on it!"
  3: 0x0658 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0659 [0x2B] Naiko-Paneiko (ID: 17478341/0x010AB2C5) [7603*]:
    → "If you're not turned on to the news, the news will turn on you! Now get with the program, kid!"
  5: 0x0660 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0661 [0x21] END_EVENT
  7: 0x0662 [0x00] END_REQSTACK()
```
