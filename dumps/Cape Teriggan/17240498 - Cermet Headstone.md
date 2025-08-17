# 17240498 - Cermet Headstone

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Cape Teriggan (ID: 113) |
| Block Size       | 1264 bytes              |
| Total Events     | 4                       |
| References Count | 24                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [200](#event-200)     | 0x0001       |     39 |             10 |
| [201](#event-201)     | 0x0028       |     39 |             10 |
| [202](#event-202)     | 0x004F       |   1054 |            121 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E02      |        7682 |
|       1 | 0x1E03      |        7683 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x009F      |         159 |
|       5 | 0x0048      |          72 |
|       6 | 0x003C      |          60 |
|       7 | 0x0013      |          19 |
|       8 | 0x00E9      |         233 |
|       9 | 0x00C8      |         200 |
|      10 | 0x001E      |          30 |
|      11 | 0x1E11      |        7697 |
|      12 | 0x002D      |          45 |
|      13 | 0x1E12      |        7698 |
|      14 | 0x0041      |          65 |
|      15 | 0x00F0      |         240 |
|      16 | 0x005A      |          90 |
|      17 | 0x0003      |           3 |
|      18 | 0x1E13      |        7699 |
|      19 | 0x0065      |         101 |
|      20 | 0x00BF      |         191 |
|      21 | 0x00C9      |         201 |
|      22 | 0x0002      |           2 |
|      23 | 0x00D7      |         215 |

## String References

- **7682**: 6... A single fragment of light. The way in which it shines suggests that it is resonating with something...
- **7683**: Do you remove the $3? [Yes./No.]
- **7697**: You place $0 on the monument as an offering.
- **7698**: ...tha...nk...you...
- **7699**: Something is lying on the ground.

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

### Event 200

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F F8 FF  FF 7F 48 00 80 23 24 01   J........H..#$.
0010: 80 02 80 02 80 25 02 00  10 02 80 00 26 00 03 01  .....%......&...
0020: 10 03 80 01 26 00 21 00                           ....&.!.        
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at EventEntity
  1: 0x000A [0x48] [System] [7682*]:
    → "6... A single fragment of light. The way in which it shines suggests that it is resonating with something..."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x24] CREATE_DIALOG(message_id=7683*, default_option=0*, option_flags=0*)
    → "Do you remove the $3? [Yes./No.]"
  4: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0026
  6: 0x001E [0x03] Work_Zone[1] = 1*
  7: 0x0023 [0x01] GOTO 0x0026

SUBROUTINE_0026:
  8: 0x0026 [0x21] END_EVENT
  9: 0x0027 [0x00] END_REQSTACK()
```

### Event 201

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          4A F0 FF FF 7F F8 FF FF          J.......
0030: 7F 48 00 80 23 24 01 80  02 80 02 80 25 02 00 10  .H..#$......%...
0040: 02 80 00 4D 00 03 01 10  03 80 01 4D 00 21 00     ...M.......M.!. 
```

#### Opcodes

```
  0: 0x0028 [0x4A] LocalPlayer looks at EventEntity
  1: 0x0031 [0x48] [System] [7682*]:
    → "6... A single fragment of light. The way in which it shines suggests that it is resonating with something..."
  2: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0035 [0x24] CREATE_DIALOG(message_id=7683*, default_option=0*, option_flags=0*)
    → "Do you remove the $3? [Yes./No.]"
  4: 0x003C [0x25] WAIT_DIALOG_SELECT()
  5: 0x003D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004D
  6: 0x0045 [0x03] Work_Zone[1] = 1*
  7: 0x004A [0x01] GOTO 0x004D

SUBROUTINE_004D:
  8: 0x004D [0x21] END_EVENT
  9: 0x004E [0x00] END_REQSTACK()
```

### Event 202

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x004F     |
| Data Size    | 1054 bytes |
| Instructions | 63         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               42                 B
0050: 1A 3F 02 46 01 2C F0 FF  FF 7F F0 FF FF 7F 72 65  .?.F.,........re
0060: 73 30 5C 00 04 80 5C 01  04 80 5C 02 04 80 5C 03  s0\...\...\...\.
0070: 04 80 5D 02 80 03 80 9A  5D 05 80 06 80 38 07 80  ..].....]....8..
0080: 27 10 F0 FF FF 7F 02 80  F0 FF FF 7F 45 08 80 F0  '...........E...
0090: FF FF 7F F0 FF FF 7F 74  65 72 31 02 80 45 09 80  .......ter1..E..
00A0: F0 FF FF 7F F0 FF FF 7F  66 64 69 32 02 80 1C 0A  ........fdi2....
00B0: 80 48 0B 80 23 6B 69 64  6C 30 F0 FF FF 7F 1C 06  .H..#kidl0......
00C0: 80 4A F0 FF FF 7F B3 11  07 01 6F 76 F0 FF FF 7F  .J........ov....
00D0: 52 08 80 F0 FF FF 7F F0  FF FF 7F 74 65 72 31 45  R..........ter1E
00E0: 08 80 F0 FF FF 7F F0 FF  FF 7F 74 65 72 32 02 80  ..........ter2..
00F0: 29 10 B3 11 07 01 02 55  08 80 F0 FF FF 7F F0 FF  )......U........
0100: FF 7F 74 65 72 32 27 10  F0 FF FF 7F 03 45 09 80  ..ter2'......E..
0110: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 02 80 45 08  ........ovl1..E.
0120: 80 F0 FF FF 7F F0 FF FF  7F 74 65 72 33 02 80 29  .........ter3..)
0130: 10 B3 11 07 01 03 1C 0C  80 4A B3 11 07 01 F8 FF  .........J......
0140: FF 7F 6F 76 B3 11 07 01  2C B3 11 07 01 B3 11 07  ..ov....,.......
0150: 01 72 65 73 30 1C 06 80  48 0D 80 23 62 0E 80 B3  .res0...H..#b...
0160: 11 07 01 B3 11 07 01 73  67 30 31 02 80 6C B3 11  .......sg01..l..
0170: 07 01 02 80 0F 80 1C 10  80 62 11 80 B4 11 07 01  .........b......
0180: B4 11 07 01 6D 61 69 6E  02 80 1C 0A 80 79 00 F0  ....main.....y..
0190: FF FF 7F B4 11 07 01 48  12 80 23 5D 02 80 10 80  .......H..#]....
01A0: 1A 3F 02 1C 0C 80 46 00  5C 00 02 80 5C 01 02 80  .?....F.\...\...
01B0: 5C 02 13 80 5C 03 14 80  45 09 80 F0 FF FF 7F F0  \...\...E.......
01C0: FF FF 7F 66 64 69 32 02  80 45 15 80 F0 FF FF 7F  ...fdi2..E......
01D0: F0 FF FF 7F 71 73 74 63  02 80 21 00 45 09 80 F0  ....qstc..!.E...
01E0: FF FF 7F F0 FF FF 7F 66  64 69 30 02 80 55 09 80  .......fdi0..U..
01F0: F0 FF FF 7F F0 FF FF 7F  66 64 69 30 1B 45 09 80  ........fdi0.E..
0200: F0 FF FF 7F F0 FF FF 7F  66 64 6F 30 02 80 55 09  ........fdo0..U.
0210: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 30 1B 45 09  .........fdo0.E.
0220: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 02 80 55  .........fdi1..U
0230: 09 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 1B 45  ..........fdi1.E
0240: 09 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 02 80  ..........fdo1..
0250: 55 09 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 1B  U..........fdo1.
0260: 45 15 80 F0 FF FF 7F F0  FF FF 7F 77 68 69 31 02  E..........whi1.
0270: 80 55 15 80 F0 FF FF 7F  F0 FF FF 7F 77 68 69 31  .U..........whi1
0280: 1B 45 15 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 31  .E..........who1
0290: 02 80 55 15 80 F0 FF FF  7F F0 FF FF 7F 77 68 6F  ..U..........who
02A0: 31 1B 45 15 80 F0 FF FF  7F F0 FF FF 7F 77 68 6F  1.E..........who
02B0: 32 02 80 55 15 80 F0 FF  FF 7F F0 FF FF 7F 77 68  2..U..........wh
02C0: 6F 32 1B 45 15 80 F0 FF  FF 7F F0 FF FF 7F 77 68  o2.E..........wh
02D0: 6F 33 02 80 55 15 80 F0  FF FF 7F F0 FF FF 7F 77  o3..U..........w
02E0: 68 6F 33 1B 62 03 80 F0  FF FF 7F F0 FF FF 7F 6D  ho3.b..........m
02F0: 61 69 6E 02 80 1C 0C 80  45 09 80 F0 FF FF 7F F0  ain.....E.......
0300: FF FF 7F 66 64 6F 31 02  80 55 09 80 F0 FF FF 7F  ...fdo1..U......
0310: F0 FF FF 7F 66 64 6F 31  1B 45 09 80 F0 FF FF 7F  ....fdo1.E......
0320: F0 FF FF 7F 66 64 69 31  02 80 62 16 80 F0 FF FF  ....fdi1..b.....
0330: 7F F0 FF FF 7F 6D 61 69  6E 02 80 1C 0A 80 55 09  .....main.....U.
0340: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 1B 45 09  .........fdi1.E.
0350: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 02 80 45  .........blon..E
0360: 15 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 02 80  ..........blon..
0370: 1B 45 15 80 F0 FF FF 7F  F0 FF FF 7F 77 68 69 30  .E..........whi0
0380: 02 80 55 15 80 F0 FF FF  7F F0 FF FF 7F 77 68 69  ..U..........whi
0390: 30 1B 45 15 80 F0 FF FF  7F F0 FF FF 7F 77 68 6F  0.E..........who
03A0: 30 02 80 55 15 80 F0 FF  FF 7F F0 FF FF 7F 77 68  0..U..........wh
03B0: 6F 30 1B 45 17 80 F0 FF  FF 7F F0 FF FF 7F 65 66  o0.E..........ef
03C0: 6F 6E 02 80 55 17 80 F0  FF FF 7F F0 FF FF 7F 65  on..U..........e
03D0: 66 6F 6E 1B 45 09 80 F0  FF FF 7F F0 FF FF 7F 66  fon.E..........f
03E0: 64 69 73 02 80 1B 45 09  80 F0 FF FF 7F F0 FF FF  dis...E.........
03F0: 7F 66 64 6F 73 02 80 55  09 80 F0 FF FF 7F F0 FF  .fdos..U........
0400: FF 7F 66 64 6F 73 1B 45  09 80 F0 FF FF 7F F0 FF  ..fdos.E........
0410: FF 7F 66 64 69 66 02 80  1B 45 09 80 F0 FF FF 7F  ..fdif...E......
0420: F0 FF FF 7F 66 64 6F 66  02 80 55 09 80 F0 FF FF  ....fdof..U.....
0430: 7F F0 FF FF 7F 66 64 6F  66 1B 45 09 80 F0 FF FF  .....fdof.E.....
0440: 7F F0 FF FF 7F 66 64 69  70 02 80 1B 45 09 80 F0  .....fdip...E...
0450: FF FF 7F F0 FF FF 7F 66  64 6F 70 02 80 55 09 80  .......fdop..U..
0460: F0 FF FF 7F F0 FF FF 7F  66 64 6F 70 1B           ........fdop.   
```

#### Opcodes

```
  0: 0x004F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0050 [0x1A] CALL_SUBROUTINE(address=0x023F)
  2: 0x0053 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0055 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [LocalPlayer, LocalPlayer]
  4: 0x0062 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 159*
  5: 0x0066 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 159*
  6: 0x006A [0x5C] MUSIC_CONTROL: Set Combat (Solo) music to song 159*
  7: 0x006E [0x5C] MUSIC_CONTROL: Set Combat (Party) music to song 159*
  8: 0x0072 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=1*)
  9: 0x0077 [0x9A] WAIT_MUSIC_SERVER()
 10: 0x0078 [0x5D] SET_MUSIC_VOLUME(volume=72*, fade_time=60*)
 11: 0x007D [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0080 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
 13: 0x0087 [0x80] LOAD_WAIT(entity=LocalPlayer)
 14: 0x008C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ter1" with entities [LocalPlayer, LocalPlayer], work=[233*, 0*]
 15: 0x009D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x00AE [0x1C] WAIT(30* ticks)
 17: 0x00B1 [0x48] [System] [7697*]:
    → "You place $0 on the monument as an offering."
 18: 0x00B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00B5 [0x6B] STOP_AND_IDLE: LocalPlayer stops current action and resets to idle (animation="idl0")
 20: 0x00BE [0x1C] WAIT(60* ticks)
 21: 0x00C1 [0x4A] LocalPlayer looks at Guardian (ID: 17240499/0x010711B3)
 22: 0x00CA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 23: 0x00CB [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 24: 0x00D0 [0x52] END_LOAD_SCHEDULER: End scheduler "ter1" with entities [LocalPlayer, LocalPlayer], work=233*
 25: 0x00DF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ter2" with entities [LocalPlayer, LocalPlayer], work=[233*, 0*]
 26: 0x00F0 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Guardian (ID: 17240499/0x010711B3), tag_num=0x02)
 27: 0x00F7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "ter2" with entities [LocalPlayer, LocalPlayer], work=233*
 28: 0x0106 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x03)
 29: 0x010D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x011E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ter3" with entities [LocalPlayer, LocalPlayer], work=[233*, 0*]
 31: 0x012F [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Guardian (ID: 17240499/0x010711B3), tag_num=0x03)
 32: 0x0136 [0x1C] WAIT(45* ticks)
 33: 0x0139 [0x4A] Guardian (ID: 17240499/0x010711B3) looks at EventEntity
 34: 0x0142 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 35: 0x0143 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Guardian (ID: 17240499/0x010711B3) Render.Flags0 and Render.Flags3 conditions are met
 36: 0x0148 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [Guardian (ID: 17240499/0x010711B3), Guardian (ID: 17240499/0x010711B3)]
 37: 0x0155 [0x1C] WAIT(60* ticks)
 38: 0x0158 [0x48] [System] [7698*]:
    → "...tha...nk...you..."
 39: 0x015B [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x015C [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "sg01" with entities [Guardian (ID: 17240499/0x010711B3), Guardian (ID: 17240499/0x010711B3)], work=[65*, 0*]
 41: 0x016D [0x6C] FADE_ENTITY_COLOR(entity_id=Guardian (ID: 17240499/0x010711B3), end_alpha=0*, fade_time=240*)
 42: 0x0176 [0x1C] WAIT(90* ticks)
 43: 0x0179 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Unnamed NPC (ID: 17240500/0x010711B4), Unnamed NPC (ID: 17240500/0x010711B4)], work=[3*, 0*]
 44: 0x018A [0x1C] WAIT(30* ticks)
 45: 0x018D [0x79] LocalPlayer looks at Unnamed NPC (ID: 17240500/0x010711B4) (Basic look)
 46: 0x0197 [0x48] [System] [7699*]:
    → "Something is lying on the ground."
 47: 0x019A [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x019B [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=90*)
 49: 0x01A0 [0x1A] CALL_SUBROUTINE(address=0x023F)
 50: 0x01A3 [0x1C] WAIT(45* ticks)
 51: 0x01A6 [0x46] CAMERA_CONTROL: Restore default settings
 52: 0x01A8 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 53: 0x01AC [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 54: 0x01B0 [0x5C] MUSIC_CONTROL: Set Combat (Solo) music to song 101*
 55: 0x01B4 [0x5C] MUSIC_CONTROL: Set Combat (Party) music to song 191*
 56: 0x01B8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x01C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 58: 0x01DA [0x21] END_EVENT
 59: 0x01DB [0x00] END_REQSTACK()

SUBROUTINE_023F:
 60: 0x023F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 61: 0x0250 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 62: 0x025F [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x01DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x01ED [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x01FC [0x1B] RETURN
     0x01FD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x020E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x021D [0x1B] RETURN
     0x021E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x022F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x023E [0x1B] RETURN
# Dead code (unreachable instructions):
     0x0260 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0271 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0280 [0x1B] RETURN
     0x0281 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0292 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x02A1 [0x1B] RETURN
     0x02A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02B3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x02C2 [0x1B] RETURN
     0x02C3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02D4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x02E3 [0x1B] RETURN
     0x02E4 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x02F5 [0x1C] WAIT(45* ticks)
     0x02F8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0309 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0318 [0x1B] RETURN
     0x0319 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x032A [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x033B [0x1C] WAIT(30* ticks)
     0x033E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x034D [0x1B] RETURN
     0x034E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x035F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0370 [0x1B] RETURN
     0x0371 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0382 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0391 [0x1B] RETURN
     0x0392 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x03A3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x03B2 [0x1B] RETURN
     0x03B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x03C4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x03D3 [0x1B] RETURN
     0x03D4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03E5 [0x1B] RETURN
     0x03E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03F7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0406 [0x1B] RETURN
     0x0407 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0418 [0x1B] RETURN
     0x0419 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x042A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0439 [0x1B] RETURN
     0x043A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x044B [0x1B] RETURN
     0x044C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x045D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x046C [0x1B] RETURN
```
