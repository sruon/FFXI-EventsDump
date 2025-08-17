# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Kuftal Tunnel (ID: 174) |
| Block Size       | 1456 bytes              |
| Total Events     | 4                       |
| References Count | 46                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [13](#event-13)       | 0x0002       |    790 |             99 |
| [14](#event-14)       | 0x0318       |    448 |             55 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x001E      |          30 |
|       3 | 0xFFFF93D9  |  4294939609 |
|       4 | 0xFFFD3426  |  4294784038 |
|       5 | 0xFFFFD9A7  |  4294957479 |
|       6 | 0x04D6      |        1238 |
|       7 | 0x0045      |          69 |
|       8 | 0x0013      |          19 |
|       9 | 0x00DA      |         218 |
|      10 | 0x0001      |           1 |
|      11 | 0x0009      |           9 |
|      12 | 0x0002      |           2 |
|      13 | 0x0003      |           3 |
|      14 | 0x001D      |          29 |
|      15 | 0x0004      |           4 |
|      16 | 0x0027      |          39 |
|      17 | 0x0005      |           5 |
|      18 | 0x0031      |          49 |
|      19 | 0x0006      |           6 |
|      20 | 0x0007      |           7 |
|      21 | 0x003B      |          59 |
|      22 | 0x0008      |           8 |
|      23 | 0x1CBB      |        7355 |
|      24 | 0x00C2      |         194 |
|      25 | 0x1CBC      |        7356 |
|      26 | 0x00C9      |         201 |
|      27 | 0x0078      |         120 |
|      28 | 0x1CBD      |        7357 |
|      29 | 0x1CBE      |        7358 |
|      30 | 0x0091      |         145 |
|      31 | 0x1CBF      |        7359 |
|      32 | 0x1CC0      |        7360 |
|      33 | 0x1CC1      |        7361 |
|      34 | 0x1CC2      |        7362 |
|      35 | 0x1CC3      |        7363 |
|      36 | 0x003C      |          60 |
|      37 | 0xFFFF9116  |  4294938902 |
|      38 | 0xFFFD3324  |  4294783780 |
|      39 | 0xFFFFAAAC  |  4294945452 |
|      40 | 0x0B78      |        2936 |
|      41 | 0x0413      |        1043 |
|      42 | 0x1CC4      |        7364 |
|      43 | 0x1CC5      |        7365 |
|      44 | 0x1CC6      |        7366 |
|      45 | 0x1CC7      |        7367 |

## String References

- **7355**: You find the piece of wood.
- **7356**: There is some writing on it... "To whoever may find this... Werei"

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

### Event 65534

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

### Event 13

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 790 bytes |
| Instructions | 99        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       42 45 00 80 F8 FF  FF 7F F8 FF FF 7F 66 64    BE..........fd
0010: 6F 30 01 80 1C 02 80 37  03 80 04 80 05 80 06 80  o0.....7........
0020: 4E 00 77 E1 0A 01 66 07  80 77 E1 0A 01 77 E1 0A  N.w...f..w...w..
0030: 01 73 68 61 30 46 01 38  08 80 45 00 80 F8 FF FF  .sha0F.8..E.....
0040: 7F F8 FF FF 7F 66 64 69  31 01 80 45 09 80 F8 FF  .....fdi1..E....
0050: FF 7F F8 FF FF 7F 73 30  30 33 01 80 02 87 7F 0A  ......s003......
0060: 80 80 6C 00 03 00 00 0B  80 01 DC 00 02 87 7F 0C  ..l.............
0070: 80 80 7C 00 03 00 00 08  80 01 DC 00 02 87 7F 0D  ..|.............
0080: 80 80 8C 00 03 00 00 0E  80 01 DC 00 02 87 7F 0F  ................
0090: 80 80 9C 00 03 00 00 10  80 01 DC 00 02 87 7F 11  ................
00A0: 80 80 AC 00 03 00 00 12  80 01 DC 00 02 87 7F 13  ................
00B0: 80 80 BC 00 03 00 00 12  80 01 DC 00 02 87 7F 14  ................
00C0: 80 80 CC 00 03 00 00 15  80 01 DC 00 02 87 7F 16  ................
00D0: 80 80 DC 00 03 00 00 07  80 01 DC 00 66 00 00 F0  ............f...
00E0: FF FF 7F F0 FF FF 7F 73  68 61 30 53 F0 FF FF 7F  .......sha0S....
00F0: F0 FF FF 7F 73 68 61 30  66 00 00 F0 FF FF 7F F0  ....sha0f.......
0100: FF FF 7F 73 69 72 30 48  17 80 23 5C 00 18 80 5C  ...sir0H..#\...\
0110: 01 18 80 48 19 80 23 45  1A 80 F8 FF FF 7F F8 FF  ...H..#E........
0120: FF 7F 77 68 6F 31 01 80  55 1A 80 F8 FF FF 7F F8  ..who1..U.......
0130: FF FF 7F 77 68 6F 31 52  09 80 F8 FF FF 7F F8 FF  ...who1R........
0140: FF 7F 73 30 30 33 45 09  80 F8 FF FF 7F F8 FF FF  ..s003E.........
0150: 7F 73 30 30 34 01 80 45  1A 80 F8 FF FF 7F F8 FF  .s004..E........
0160: FF 7F 77 68 69 31 01 80  1C 1B 80 2B 77 E1 0A 01  ..whi1.....+w...
0170: 1C 80 23 2B 77 E1 0A 01  1D 80 23 45 1A 80 F8 FF  ..#+w.....#E....
0180: FF 7F F8 FF FF 7F 77 68  6F 30 01 80 55 1A 80 F8  ......who0..U...
0190: FF FF 7F F8 FF FF 7F 77  68 6F 30 52 09 80 F8 FF  .......who0R....
01A0: FF 7F F8 FF FF 7F 73 30  30 34 45 09 80 F8 FF FF  ......s004E.....
01B0: 7F F8 FF FF 7F 73 30 30  37 01 80 27 0A 78 E1 0A  .....s007..'.x..
01C0: 01 02 27 0A 79 E1 0A 01  02 27 0A 7A E1 0A 01 02  ..'.y....'.z....
01D0: 27 0A 7B E1 0A 01 02 27  0A 7C E1 0A 01 02 27 0A  '.{....'.|....'.
01E0: 7D E1 0A 01 02 27 0A 7E  E1 0A 01 02 27 0A 7F E1  }....'.~....'...
01F0: 0A 01 02 1C 11 80 45 1A  80 F8 FF FF 7F F8 FF FF  ......E.........
0200: 7F 77 68 69 31 01 80 1C  1E 80 6B 69 64 6C 30 77  .whi1.....kidl0w
0210: E1 0A 01 45 1A 80 F8 FF  FF 7F F8 FF FF 7F 77 68  ...E..........wh
0220: 6F 30 01 80 55 1A 80 F8  FF FF 7F F8 FF FF 7F 77  o0..U..........w
0230: 68 6F 30 52 09 80 F8 FF  FF 7F F8 FF FF 7F 73 30  ho0R..........s0
0240: 30 37 45 09 80 F8 FF FF  7F F8 FF FF 7F 73 30 30  07E..........s00
0250: 35 01 80 45 1A 80 F8 FF  FF 7F F8 FF FF 7F 77 68  5..E..........wh
0260: 69 31 01 80 2B 77 E1 0A  01 1F 80 23 2B 77 E1 0A  i1..+w.....#+w..
0270: 01 20 80 23 2B 77 E1 0A  01 21 80 23 45 00 80 F8  . .#+w...!.#E...
0280: FF FF 7F F8 FF FF 7F 6F  76 6C 31 01 80 52 09 80  .......ovl1..R..
0290: F8 FF FF 7F F8 FF FF 7F  73 30 30 35 45 09 80 F8  ........s005E...
02A0: FF FF 7F F8 FF FF 7F 73  30 30 36 01 80 27 0A 77  .......s006..'.w
02B0: E1 0A 01 02 2B 77 E1 0A  01 22 80 23 2B 77 E1 0A  ....+w...".#+w..
02C0: 01 23 80 23 55 09 80 F8  FF FF 7F F8 FF FF 7F 73  .#.#U..........s
02D0: 30 30 36 66 00 00 F0 FF  FF 7F F0 FF FF 7F 73 68  006f..........sh
02E0: 61 31 5D 01 80 24 80 45  00 80 F8 FF FF 7F F8 FF  a1]..$.E........
02F0: FF 7F 66 64 6F 31 01 80  1C 24 80 5C 00 01 80 5C  ..fdo1...$.\...\
0300: 01 01 80 46 00 45 00 80  F8 FF FF 7F F8 FF FF 7F  ...F.E..........
0310: 66 64 69 31 01 80 21 00                           fdi1..!.        
```

#### Opcodes

```
  0: 0x0002 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0003 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0014 [0x1C] WAIT(30* ticks)
  3: 0x0017 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-27.687*, z=-183.258*, y=-9.817*, direction=108.8°*
  4: 0x0020 [0x4E] SET_ENTITY_HIDE_FLAG: Show Werei (ID: 17490295/0x010AE177)
  5: 0x0026 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [Werei (ID: 17490295/0x010AE177), Werei (ID: 17490295/0x010AE177)], work=69*
  6: 0x0035 [0x46] CAMERA_CONTROL: Disable user control
  7: 0x0037 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x003A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  9: 0x004B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s003" with entities [EventEntity, EventEntity], work=[218*, 0*]
 10: 0x005C [0x02] IF !(LocalPlayer->Race == 1*) GOTO 0x006C
 11: 0x0064 [0x03] ExtData[1]->WorkLocal[0] = 9*
 12: 0x0069 [0x01] GOTO 0x00DC
 13: 0x006C [0x02] IF !(LocalPlayer->Race == 2*) GOTO 0x007C
 14: 0x0074 [0x03] ExtData[1]->WorkLocal[0] = 19*
 15: 0x0079 [0x01] GOTO 0x00DC
 16: 0x007C [0x02] IF !(LocalPlayer->Race == 3*) GOTO 0x008C
 17: 0x0084 [0x03] ExtData[1]->WorkLocal[0] = 29*
 18: 0x0089 [0x01] GOTO 0x00DC
 19: 0x008C [0x02] IF !(LocalPlayer->Race == 4*) GOTO 0x009C
 20: 0x0094 [0x03] ExtData[1]->WorkLocal[0] = 39*
 21: 0x0099 [0x01] GOTO 0x00DC
 22: 0x009C [0x02] IF !(LocalPlayer->Race == 5*) GOTO 0x00AC
 23: 0x00A4 [0x03] ExtData[1]->WorkLocal[0] = 49*
 24: 0x00A9 [0x01] GOTO 0x00DC
 25: 0x00AC [0x02] IF !(LocalPlayer->Race == 6*) GOTO 0x00BC
 26: 0x00B4 [0x03] ExtData[1]->WorkLocal[0] = 49*
 27: 0x00B9 [0x01] GOTO 0x00DC
 28: 0x00BC [0x02] IF !(LocalPlayer->Race == 7*) GOTO 0x00CC
 29: 0x00C4 [0x03] ExtData[1]->WorkLocal[0] = 59*
 30: 0x00C9 [0x01] GOTO 0x00DC
 31: 0x00CC [0x02] IF !(LocalPlayer->Race == 8*) GOTO 0x00DC
 32: 0x00D4 [0x03] ExtData[1]->WorkLocal[0] = 69*
 33: 0x00D9 [0x01] GOTO 0x00DC

SUBROUTINE_00DC:
 34: 0x00DC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [LocalPlayer, LocalPlayer], work=ExtData[1]->WorkLocal[0]
 35: 0x00EB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [LocalPlayer, LocalPlayer]
 36: 0x00F8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir0" with entities [LocalPlayer, LocalPlayer], work=ExtData[1]->WorkLocal[0]
 37: 0x0107 [0x48] [System] [7355*]:
    → "You find the piece of wood."
 38: 0x010A [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x010B [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 194*
 40: 0x010F [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 194*
 41: 0x0113 [0x48] [System] [7356*]:
    → "There is some writing on it... "To whoever may find this... Werei""
 42: 0x0116 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x0117 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 44: 0x0128 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [EventEntity, EventEntity], work=201*
 45: 0x0137 [0x52] END_LOAD_SCHEDULER: End scheduler "s003" with entities [EventEntity, EventEntity], work=218*
 46: 0x0146 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s004" with entities [EventEntity, EventEntity], work=[218*, 0*]
 47: 0x0157 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 48: 0x0168 [0x1C] WAIT(120* ticks)
 49: 0x016B [0x2B] Werei (ID: 17490295/0x010AE177) [7357*]:
    → ""My long journey is nearing an end. I have finally reached my destination.""
 50: 0x0172 [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x0173 [0x2B] Werei (ID: 17490295/0x010AE177) [7358*]:
    → ""This is the land of tragedy and sorrow. The place where our forefathers ran when they were driven from their home by the Antica.""
 52: 0x017A [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x017B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [EventEntity, EventEntity], work=[201*, 0*]
 54: 0x018C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [EventEntity, EventEntity], work=201*
 55: 0x019B [0x52] END_LOAD_SCHEDULER: End scheduler "s004" with entities [EventEntity, EventEntity], work=218*
 56: 0x01AA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s007" with entities [EventEntity, EventEntity], work=[218*, 0*]
 57: 0x01BB [0x27] REQ_SET(priority=0x0A, entity_id=Unnamed NPC (ID: 17490296/0x010AE178), tag_num=0x02)
 58: 0x01C2 [0x27] REQ_SET(priority=0x0A, entity_id=Unnamed NPC (ID: 17490297/0x010AE179), tag_num=0x02)
 59: 0x01C9 [0x27] REQ_SET(priority=0x0A, entity_id=Unnamed NPC (ID: 17490298/0x010AE17A), tag_num=0x02)
 60: 0x01D0 [0x27] REQ_SET(priority=0x0A, entity_id=Unnamed NPC (ID: 17490299/0x010AE17B), tag_num=0x02)
 61: 0x01D7 [0x27] REQ_SET(priority=0x0A, entity_id=Unnamed NPC (ID: 17490300/0x010AE17C), tag_num=0x02)
 62: 0x01DE [0x27] REQ_SET(priority=0x0A, entity_id=Unnamed NPC (ID: 17490301/0x010AE17D), tag_num=0x02)
 63: 0x01E5 [0x27] REQ_SET(priority=0x0A, entity_id=Unnamed NPC (ID: 17490302/0x010AE17E), tag_num=0x02)
 64: 0x01EC [0x27] REQ_SET(priority=0x0A, entity_id=Unnamed NPC (ID: 17490303/0x010AE17F), tag_num=0x02)
 65: 0x01F3 [0x1C] WAIT(5* ticks)
 66: 0x01F6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 67: 0x0207 [0x1C] WAIT(145* ticks)
 68: 0x020A [0x6B] STOP_AND_IDLE: Werei (ID: 17490295/0x010AE177) stops current action and resets to idle (animation="idl0")
 69: 0x0213 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [EventEntity, EventEntity], work=[201*, 0*]
 70: 0x0224 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [EventEntity, EventEntity], work=201*
 71: 0x0233 [0x52] END_LOAD_SCHEDULER: End scheduler "s007" with entities [EventEntity, EventEntity], work=218*
 72: 0x0242 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s005" with entities [EventEntity, EventEntity], work=[218*, 0*]
 73: 0x0253 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 74: 0x0264 [0x2B] Werei (ID: 17490295/0x010AE177) [7359*]:
    → ""All those who were chased to this cliff lost their lives. Some died by sword, others fell to the depths below.""
 75: 0x026B [0x23] WAIT_FOR_DIALOG_INTERACTION
 76: 0x026C [0x2B] Werei (ID: 17490295/0x010AE177) [7360*]:
    → ""This place is filled with the pain and suffering of a people who set out to a new land searching for a new life.""
 77: 0x0273 [0x23] WAIT_FOR_DIALOG_INTERACTION
 78: 0x0274 [0x2B] Werei (ID: 17490295/0x010AE177) [7361*]:
    → ""We Galka, with our new homes in Bastok, should not spend our time envying the life of our past brothers.""
 79: 0x027B [0x23] WAIT_FOR_DIALOG_INTERACTION
 80: 0x027C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 81: 0x028D [0x52] END_LOAD_SCHEDULER: End scheduler "s005" with entities [EventEntity, EventEntity], work=218*
 82: 0x029C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s006" with entities [EventEntity, EventEntity], work=[218*, 0*]
 83: 0x02AD [0x27] REQ_SET(priority=0x0A, entity_id=Werei (ID: 17490295/0x010AE177), tag_num=0x02)
 84: 0x02B4 [0x2B] Werei (ID: 17490295/0x010AE177) [7362*]:
    → ""My time in this life is coming to an end... However, I hope that someday, someone may find my message and take it back to my people in Bastok.""
 85: 0x02BB [0x23] WAIT_FOR_DIALOG_INTERACTION
 86: 0x02BC [0x2B] Werei (ID: 17490295/0x010AE177) [7363*]:
    → ""If one wishes to revisit the Galkan past, one must not forget those long ago who fought for their futures.""
 87: 0x02C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 88: 0x02C4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s006" with entities [EventEntity, EventEntity], work=218*
 89: 0x02D3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [LocalPlayer, LocalPlayer], work=ExtData[1]->WorkLocal[0]
 90: 0x02E2 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=60*)
 91: 0x02E7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 92: 0x02F8 [0x1C] WAIT(60* ticks)
 93: 0x02FB [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 94: 0x02FF [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 95: 0x0303 [0x46] CAMERA_CONTROL: Restore default settings
 96: 0x0305 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 97: 0x0316 [0x21] END_EVENT
 98: 0x0317 [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0318    |
| Data Size    | 448 bytes |
| Instructions | 55        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0310:                          42 45 00 80 F8 FF FF 7F          BE......
0320: F8 FF FF 7F 66 64 6F 30  01 80 1C 02 80 37 25 80  ....fdo0.....7%.
0330: 26 80 27 80 28 80 46 01  38 29 80 27 0A F1 FF FF  &.'.(.F.8).'....
0340: 7F 02 27 0A F2 FF FF 7F  02 27 0A F3 FF FF 7F 02  ..'......'......
0350: 27 0A F4 FF FF 7F 02 27  0A F5 FF FF 7F 02 1C 11  '......'........
0360: 80 45 09 80 F8 FF FF 7F  F8 FF FF 7F 73 30 30 38  .E..........s008
0370: 01 80 45 00 80 F8 FF FF  7F F8 FF FF 7F 66 64 69  ..E..........fdi
0380: 32 01 80 55 09 80 F8 FF  FF 7F F8 FF FF 7F 73 30  2..U..........s0
0390: 30 38 45 09 80 F8 FF FF  7F F8 FF FF 7F 73 30 30  08E..........s00
03A0: 39 01 80 27 0A 80 E1 0A  01 02 2B 80 E1 0A 01 2A  9..'......+....*
03B0: 80 23 1E 80 E1 0A 01 4A  F1 FF FF 7F 80 E1 0A 01  .#.....J........
03C0: 4A F2 FF FF 7F 80 E1 0A  01 4A F3 FF FF 7F 80 E1  J........J......
03D0: 0A 01 4A F4 FF FF 7F 80  E1 0A 01 4A F5 FF FF 7F  ..J........J....
03E0: 80 E1 0A 01 2A 0A 80 E1  0A 01 66 24 80 80 E1 0A  ....*.....f$....
03F0: 01 80 E1 0A 01 74 61 6C  6B 2B 80 E1 0A 01 2B 80  .....talk+....+.
0400: 23 52 09 80 F8 FF FF 7F  F8 FF FF 7F 73 30 30 39  #R..........s009
0410: 45 09 80 F8 FF FF 7F F8  FF FF 7F 73 30 31 30 01  E..........s010.
0420: 80 2B 80 E1 0A 01 2C 80  23 66 24 80 80 E1 0A 01  .+....,.#f$.....
0430: 80 E1 0A 01 74 6C 6B 31  2B 80 E1 0A 01 2D 80 23  ....tlk1+....-.#
0440: 27 0A 80 E1 0A 01 03 52  09 80 F8 FF FF 7F F8 FF  '......R........
0450: FF 7F 73 30 31 30 45 09  80 F8 FF FF 7F F8 FF FF  ..s010E.........
0460: 7F 73 30 31 31 01 80 1C  24 80 79 00 F4 FF FF 7F  .s011...$.y.....
0470: F5 FF FF 7F 79 00 F5 FF  FF 7F F4 FF FF 7F 1C 24  ....y..........$
0480: 80 79 00 F0 FF FF 7F F1  FF FF 7F 79 00 F1 FF FF  .y.........y....
0490: 7F F0 FF FF 7F 1C 24 80  79 00 F2 FF FF 7F F3 FF  ......$.y.......
04A0: FF 7F 79 00 F3 FF FF 7F  F2 FF FF 7F 1C 24 80 45  ..y..........$.E
04B0: 00 80 F8 FF FF 7F F8 FF  FF 7F 66 64 6F 32 01 80  ..........fdo2..
04C0: 1C 1B 80 46 00 45 00 80  F8 FF FF 7F F8 FF FF 7F  ...F.E..........
04D0: 66 64 69 31 01 80 21 00                           fdi1..!.        
```

#### Opcodes

```
  0: 0x0318 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0319 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x032A [0x1C] WAIT(30* ticks)
  3: 0x032D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-28.394*, z=-183.516*, y=-21.844*, direction=258.0°*
  4: 0x0336 [0x46] CAMERA_CONTROL: Disable user control
  5: 0x0338 [0x38] SET_CLIENT_EVENT_MODE(mode=1043*)
  6: 0x033B [0x27] REQ_SET(priority=0x0A, entity_id=Unknown NPC (ID: 2147483633/0x7FFFFFF1), tag_num=0x02)
  7: 0x0342 [0x27] REQ_SET(priority=0x0A, entity_id=Unknown NPC (ID: 2147483634/0x7FFFFFF2), tag_num=0x02)
  8: 0x0349 [0x27] REQ_SET(priority=0x0A, entity_id=Unknown NPC (ID: 2147483635/0x7FFFFFF3), tag_num=0x02)
  9: 0x0350 [0x27] REQ_SET(priority=0x0A, entity_id=Unknown NPC (ID: 2147483636/0x7FFFFFF4), tag_num=0x02)
 10: 0x0357 [0x27] REQ_SET(priority=0x0A, entity_id=Unknown NPC (ID: 2147483637/0x7FFFFFF5), tag_num=0x02)
 11: 0x035E [0x1C] WAIT(5* ticks)
 12: 0x0361 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s008" with entities [EventEntity, EventEntity], work=[218*, 0*]
 13: 0x0372 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 14: 0x0383 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s008" with entities [EventEntity, EventEntity], work=218*
 15: 0x0392 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s009" with entities [EventEntity, EventEntity], work=[218*, 0*]
 16: 0x03A3 [0x27] REQ_SET(priority=0x0A, entity_id=Hawk Nose (ID: 17490304/0x010AE180), tag_num=0x02)
 17: 0x03AA [0x2B] Hawk Nose (ID: 17490304/0x010AE180) [7364*]:
    → "Hey! What the hell do you think you're doing up here?"
 18: 0x03B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x03B2 [0x1E] EventEntity looks at Hawk Nose (ID: 17490304/0x010AE180) and starts talking
 20: 0x03B7 [0x4A] Unknown NPC (ID: 2147483633/0x7FFFFFF1) looks at Hawk Nose (ID: 17490304/0x010AE180)
 21: 0x03C0 [0x4A] Unknown NPC (ID: 2147483634/0x7FFFFFF2) looks at Hawk Nose (ID: 17490304/0x010AE180)
 22: 0x03C9 [0x4A] Unknown NPC (ID: 2147483635/0x7FFFFFF3) looks at Hawk Nose (ID: 17490304/0x010AE180)
 23: 0x03D2 [0x4A] Unknown NPC (ID: 2147483636/0x7FFFFFF4) looks at Hawk Nose (ID: 17490304/0x010AE180)
 24: 0x03DB [0x4A] Unknown NPC (ID: 2147483637/0x7FFFFFF5) looks at Hawk Nose (ID: 17490304/0x010AE180)
 25: 0x03E4 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Hawk Nose (ID: 17490304/0x010AE180))
 26: 0x03EA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "talk" with entities [Hawk Nose (ID: 17490304/0x010AE180), Hawk Nose (ID: 17490304/0x010AE180)], work=60*
 27: 0x03F9 [0x2B] Hawk Nose (ID: 17490304/0x010AE180) [7365*]:
    → "What!? That Datta asked you to see if this place would be good for sightseeing? What was that idiot thinking!?"
 28: 0x0400 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0401 [0x52] END_LOAD_SCHEDULER: End scheduler "s009" with entities [EventEntity, EventEntity], work=218*
 30: 0x0410 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s010" with entities [EventEntity, EventEntity], work=[218*, 0*]
 31: 0x0421 [0x2B] Hawk Nose (ID: 17490304/0x010AE180) [7366*]:
    → "If you didn't already know, hundreds of Galka lost their lives here long ago. The bottom of the cliff is teeming with ghosts!"
 32: 0x0428 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0429 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Hawk Nose (ID: 17490304/0x010AE180), Hawk Nose (ID: 17490304/0x010AE180)], work=60*
 34: 0x0438 [0x2B] Hawk Nose (ID: 17490304/0x010AE180) [7367*]:
    → "Who'd be crazy enough to come here on a vacation!? I'm getting out of here as fast as I can, and I recommend you do the same!"
 35: 0x043F [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x0440 [0x27] REQ_SET(priority=0x0A, entity_id=Hawk Nose (ID: 17490304/0x010AE180), tag_num=0x03)
 37: 0x0447 [0x52] END_LOAD_SCHEDULER: End scheduler "s010" with entities [EventEntity, EventEntity], work=218*
 38: 0x0456 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s011" with entities [EventEntity, EventEntity], work=[218*, 0*]
 39: 0x0467 [0x1C] WAIT(60* ticks)
 40: 0x046A [0x79] Unknown NPC (ID: 2147483636/0x7FFFFFF4) looks at Unknown NPC (ID: 2147483637/0x7FFFFFF5) (Basic look)
 41: 0x0474 [0x79] Unknown NPC (ID: 2147483637/0x7FFFFFF5) looks at Unknown NPC (ID: 2147483636/0x7FFFFFF4) (Basic look)
 42: 0x047E [0x1C] WAIT(60* ticks)
 43: 0x0481 [0x79] LocalPlayer looks at Unknown NPC (ID: 2147483633/0x7FFFFFF1) (Basic look)
 44: 0x048B [0x79] Unknown NPC (ID: 2147483633/0x7FFFFFF1) looks at LocalPlayer (Basic look)
 45: 0x0495 [0x1C] WAIT(60* ticks)
 46: 0x0498 [0x79] Unknown NPC (ID: 2147483634/0x7FFFFFF2) looks at Unknown NPC (ID: 2147483635/0x7FFFFFF3) (Basic look)
 47: 0x04A2 [0x79] Unknown NPC (ID: 2147483635/0x7FFFFFF3) looks at Unknown NPC (ID: 2147483634/0x7FFFFFF2) (Basic look)
 48: 0x04AC [0x1C] WAIT(60* ticks)
 49: 0x04AF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 50: 0x04C0 [0x1C] WAIT(120* ticks)
 51: 0x04C3 [0x46] CAMERA_CONTROL: Restore default settings
 52: 0x04C5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 53: 0x04D6 [0x21] END_EVENT
 54: 0x04D7 [0x00] END_REQSTACK()
```
