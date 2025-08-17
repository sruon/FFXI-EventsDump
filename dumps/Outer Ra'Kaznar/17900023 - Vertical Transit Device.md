# 17900023 - Vertical Transit Device

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Outer Ra'Kaznar (ID: 274) |
| Block Size       | 1176 bytes                |
| Total Events     | 2                         |
| References Count | 39                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [46](#event-46)       | 0x0001       |    992 |            125 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E45      |        7749 |
|       1 | 0x1E46      |        7750 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x00C8      |         200 |
|       5 | 0x0013      |          19 |
|       6 | 0xFFF8FB2F  |  4294507311 |
|       7 | 0x70A1      |       28833 |
|       8 | 0xFFFDDD86  |  4294827398 |
|       9 | 0x0400      |        1024 |
|      10 | 0x02A5      |         677 |
|      11 | 0x8D9AE     |      580014 |
|      12 | 0x70D8      |       28888 |
|      13 | 0x18705     |      100101 |
|      14 | 0x0078      |         120 |
|      15 | 0x003C      |          60 |
|      16 | 0x005A      |          90 |
|      17 | 0x0028      |          40 |
|      18 | 0xFFF8FB20  |  4294507296 |
|      19 | 0x5C30      |       23600 |
|      20 | 0xFFFDDD20  |  4294827296 |
|      21 | 0x8D9A0     |      580000 |
|      22 | 0x186A0     |      100000 |
|      23 | 0xFFFEF278  |  4294898296 |
|      24 | 0x0002      |           2 |
|      25 | 0x81A38     |      531000 |
|      26 | 0xFFFFB1E0  |  4294947296 |
|      27 | 0xFFFFF800  |  4294965248 |
|      28 | 0x0003      |           3 |
|      29 | 0x7148      |       29000 |
|      30 | 0xFFFFFC00  |  4294966272 |
|      31 | 0x0004      |           4 |
|      32 | 0x0005      |           5 |
|      33 | 0xFFF83BB8  |  4294458296 |
|      34 | 0x0006      |           6 |
|      35 | 0x0007      |           7 |
|      36 | 0x001E      |          30 |
|      37 | 0x000F      |          15 |
|      38 | 0x40000000  |  1073741824 |

## String References

- **7749**: This baffling gadget seems to serve as transport to the [lower/higher] floors.
- **7750**: Head to a [lower/higher] floor? [Yes./No.]

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

### Event 46

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 992 bytes |
| Instructions | 125       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 02 80 25 02 00 10   H..#$......%...
0010: 02 80 00 CF 03 42 03 01  10 03 80 43 00 43 01 4A  .....B.....C.C.J
0020: F0 FF FF 7F F8 FF FF 7F  6F 76 F0 FF FF 7F 45 04  ........ov....E.
0030: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 02 80 55  .........fdo1..U
0040: 04 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 46 01  ..........fdo1F.
0050: 38 05 80 7B F0 FF FF 7F  02 02 10 02 80 00 81 00  8..{............
0060: BA F0 FF FF 7F 06 80 07  80 08 80 09 80 45 0A 80  .............E..
0070: F0 FF FF 7F F0 FF FF 7F  73 30 35 36 02 80 01 9F  ........s056....
0080: 00 BA F0 FF FF 7F 0B 80  0C 80 0D 80 09 80 45 0A  ..............E.
0090: 80 F0 FF FF 7F F0 FF FF  7F 73 30 35 37 02 80 45  .........s057..E
00A0: 04 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 02 80  ..........fdi1..
00B0: 55 04 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 02  U..........fdi1.
00C0: 02 10 02 80 00 D1 00 27  08 DF 21 11 01 05 01 D8  .......'..!.....
00D0: 00 27 08 E0 21 11 01 04  1C 0E 80 1C 0F 80 45 04  .'..!.........E.
00E0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 02 80 55  .........fdo1..U
00F0: 04 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 1C 10  ..........fdo1..
0100: 80 02 02 10 02 80 00 D1  01 52 0A 80 F0 FF FF 7F  .........R......
0110: F0 FF FF 7F 73 30 35 36  1C 11 80 7B F0 FF FF 7F  ....s056...{....
0120: BA F0 FF FF 7F 12 80 13  80 14 80 09 80 27 08 F0  .............'..
0130: FF FF 7F 1A 45 0A 80 F0  FF FF 7F F0 FF FF 7F 73  ....E..........s
0140: 30 35 38 02 80 45 04 80  F0 FF FF 7F F0 FF FF 7F  058..E..........
0150: 66 64 69 31 02 80 55 04  80 F0 FF FF 7F F0 FF FF  fdi1..U.........
0160: 7F 66 64 69 31 2A 08 F0  FF FF 7F 1C 0F 80 27 08  .fdi1*........'.
0170: DC 21 11 01 05 1C 0E 80  52 0A 80 F0 FF FF 7F F0  .!......R.......
0180: FF FF 7F 73 30 35 38 45  0A 80 F0 FF FF 7F F0 FF  ...s058E........
0190: FF 7F 73 30 36 31 02 80  27 08 F0 FF FF 7F 1B 45  ..s061..'......E
01A0: 04 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 02 80  ..........fdo1..
01B0: 55 04 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 52  U..........fdo1R
01C0: 0A 80 F0 FF FF 7F F0 FF  FF 7F 73 30 36 31 01 A9  ..........s061..
01D0: 02 52 0A 80 F0 FF FF 7F  F0 FF FF 7F 73 30 35 37  .R..........s057
01E0: 1C 11 80 7B F0 FF FF 7F  BA F0 FF FF 7F 15 80 13  ...{............
01F0: 80 16 80 09 80 27 08 F0  FF FF 7F 1D 45 0A 80 F0  .....'......E...
0200: FF FF 7F F0 FF FF 7F 73  30 35 39 02 80 45 04 80  .......s059..E..
0210: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 02 80 55 04  ........fdi1..U.
0220: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 2D F8 FF  .........fdi1-..
0230: FF 7F F8 FF FF 7F 70 6D  65 00 2A 08 F0 FF FF 7F  ......pme.*.....
0240: 1C 0F 80 27 08 DD 21 11  01 04 1C 0E 80 52 0A 80  ...'..!......R..
0250: F0 FF FF 7F F0 FF FF 7F  73 30 35 39 45 0A 80 F0  ........s059E...
0260: FF FF 7F F0 FF FF 7F 73  30 36 30 02 80 27 08 F0  .......s060..'..
0270: FF FF 7F 1E 45 04 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0280: 64 6F 31 02 80 55 04 80  F0 FF FF 7F F0 FF FF 7F  do1..U..........
0290: 66 64 6F 31 2A 08 F0 FF  FF 7F 52 0A 80 F0 FF FF  fdo1*.....R.....
02A0: 7F F0 FF FF 7F 73 30 36  30 29 08 F0 FF FF 7F 1F  .....s060)......
02B0: 02 07 10 03 80 80 D4 02  BA F0 FF FF 7F 15 80 17  ................
02C0: 80 16 80 09 80 47 00 15  80 17 80 16 80 09 80 47  .....G.........G
02D0: 01 01 97 03 02 07 10 18  80 80 F8 02 BA F0 FF FF  ................
02E0: 7F 19 80 1A 80 16 80 1B  80 47 00 19 80 1A 80 16  .........G......
02F0: 80 1B 80 47 01 01 97 03  02 07 10 1C 80 80 1C 03  ...G............
0300: BA F0 FF FF 7F 15 80 1D  80 16 80 1E 80 47 00 15  .............G..
0310: 80 1D 80 16 80 1E 80 47  01 01 97 03 02 07 10 1F  .......G........
0320: 80 80 40 03 BA F0 FF FF  7F 12 80 17 80 14 80 09  ..@.............
0330: 80 47 00 12 80 17 80 14  80 09 80 47 01 01 97 03  .G.........G....
0340: 02 07 10 20 80 80 64 03  BA F0 FF FF 7F 21 80 1A  ... ..d......!..
0350: 80 14 80 1B 80 47 00 21  80 1A 80 14 80 1B 80 47  .....G.!.......G
0360: 01 01 97 03 02 07 10 22  80 80 88 03 BA F0 FF FF  ......."........
0370: 7F 12 80 1D 80 14 80 1E  80 47 00 12 80 1D 80 14  .........G......
0380: 80 1E 80 47 01 01 97 03  02 07 10 23 80 80 97 03  ...G.......#....
0390: 43 00 43 01 01 97 03 46  00 1C 24 80 02 07 10 23  C.C....F..$....#
03A0: 80 03 C7 03 80 F0 FF FF  7F 1C 25 80 AB 11 02 80  ..........%.....
03B0: 1C 03 80 45 04 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
03C0: 69 32 02 80 01 CC 03 03  01 10 23 80 01 DF 03 02  i2........#.....
03D0: 00 10 03 80 00 DF 03 03  01 10 26 80 01 DF 03 21  ..........&....!
03E0: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7749*]:
    → "This baffling gadget seems to serve as transport to the [lower/higher] floors."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7750*, default_option=0*, option_flags=0*)
    → "Head to a [lower/higher] floor? [Yes./No.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03CF
  5: 0x0015 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x0016 [0x03] Work_Zone[1] = 1*
  7: 0x001B [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001D [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x001F [0x4A] LocalPlayer looks at EventEntity
 10: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x0029 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 12: 0x002E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x003F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 14: 0x004E [0x46] CAMERA_CONTROL: Disable user control
 15: 0x0050 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 16: 0x0053 [0x7B] LocalPlayer stops talking
 17: 0x0058 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0081
 18: 0x0060 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-459.985*, pos_z=28.833*, pos_y=-139.898*, direction=90.0°*)
 19: 0x006D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s056" with entities [LocalPlayer, LocalPlayer], work=[677*, 0*]
 20: 0x007E [0x01] GOTO 0x009F
 21: 0x0081 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=580.014*, pos_z=28.888*, pos_y=100.101*, direction=90.0°*)
 22: 0x008E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s057" with entities [LocalPlayer, LocalPlayer], work=[677*, 0*]

SUBROUTINE_009F:
 23: 0x009F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x00B0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 25: 0x00BF [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00D1
 26: 0x00C7 [0x27] REQ_SET(priority=0x08, entity_id=Unknown NPC (ID: 17899999/0x011121DF), tag_num=0x05)
 27: 0x00CE [0x01] GOTO 0x00D8
 28: 0x00D1 [0x27] REQ_SET(priority=0x08, entity_id=Unknown NPC (ID: 17900000/0x011121E0), tag_num=0x04)

SUBROUTINE_00D8:
 29: 0x00D8 [0x1C] WAIT(120* ticks)
 30: 0x00DB [0x1C] WAIT(60* ticks)
 31: 0x00DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x00EF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 33: 0x00FE [0x1C] WAIT(90* ticks)
 34: 0x0101 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x01D1
 35: 0x0109 [0x52] END_LOAD_SCHEDULER: End scheduler "s056" with entities [LocalPlayer, LocalPlayer], work=677*
 36: 0x0118 [0x1C] WAIT(40* ticks)
 37: 0x011B [0x7B] LocalPlayer stops talking
 38: 0x0120 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-460.000*, pos_z=23.600*, pos_y=-140.000*, direction=90.0°*)
 39: 0x012D [0x27] REQ_SET(priority=0x08, entity_id=LocalPlayer, tag_num=0x1A)
 40: 0x0134 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s058" with entities [LocalPlayer, LocalPlayer], work=[677*, 0*]
 41: 0x0145 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 42: 0x0156 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 43: 0x0165 [0x2A] GET_REQ_LEVEL(level=8, entity_id=LocalPlayer)
 44: 0x016B [0x1C] WAIT(60* ticks)
 45: 0x016E [0x27] REQ_SET(priority=0x08, entity_id=Unknown NPC (ID: 17899996/0x011121DC), tag_num=0x05)
 46: 0x0175 [0x1C] WAIT(120* ticks)
 47: 0x0178 [0x52] END_LOAD_SCHEDULER: End scheduler "s058" with entities [LocalPlayer, LocalPlayer], work=677*
 48: 0x0187 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s061" with entities [LocalPlayer, LocalPlayer], work=[677*, 0*]
 49: 0x0198 [0x27] REQ_SET(priority=0x08, entity_id=LocalPlayer, tag_num=0x1B)
 50: 0x019F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 51: 0x01B0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 52: 0x01BF [0x52] END_LOAD_SCHEDULER: End scheduler "s061" with entities [LocalPlayer, LocalPlayer], work=677*
 53: 0x01CE [0x01] GOTO 0x02A9
 54: 0x01D1 [0x52] END_LOAD_SCHEDULER: End scheduler "s057" with entities [LocalPlayer, LocalPlayer], work=677*
 55: 0x01E0 [0x1C] WAIT(40* ticks)
 56: 0x01E3 [0x7B] LocalPlayer stops talking
 57: 0x01E8 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=580.000*, pos_z=23.600*, pos_y=100.000*, direction=90.0°*)
 58: 0x01F5 [0x27] REQ_SET(priority=0x08, entity_id=LocalPlayer, tag_num=0x1D)
 59: 0x01FC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s059" with entities [LocalPlayer, LocalPlayer], work=[677*, 0*]
 60: 0x020D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 61: 0x021E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 62: 0x022D [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "pme" with entities [EventEntity, EventEntity]
 63: 0x023A [0x2A] GET_REQ_LEVEL(level=8, entity_id=LocalPlayer)
 64: 0x0240 [0x1C] WAIT(60* ticks)
 65: 0x0243 [0x27] REQ_SET(priority=0x08, entity_id=Unknown NPC (ID: 17899997/0x011121DD), tag_num=0x04)
 66: 0x024A [0x1C] WAIT(120* ticks)
 67: 0x024D [0x52] END_LOAD_SCHEDULER: End scheduler "s059" with entities [LocalPlayer, LocalPlayer], work=677*
 68: 0x025C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s060" with entities [LocalPlayer, LocalPlayer], work=[677*, 0*]
 69: 0x026D [0x27] REQ_SET(priority=0x08, entity_id=LocalPlayer, tag_num=0x1E)
 70: 0x0274 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 71: 0x0285 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 72: 0x0294 [0x2A] GET_REQ_LEVEL(level=8, entity_id=LocalPlayer)
 73: 0x029A [0x52] END_LOAD_SCHEDULER: End scheduler "s060" with entities [LocalPlayer, LocalPlayer], work=677*

SUBROUTINE_02A9:
 74: 0x02A9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x1F)
 75: 0x02B0 [0x02] IF !(Work_Zone[7] == 1*) GOTO 0x02D4
 76: 0x02B8 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=580.000*, pos_z=-69.000*, pos_y=100.000*, direction=90.0°*)
 77: 0x02C5 [0x47] UPDATE_PLAYER_POS(580.000*, -69.000*, 100.000*, yaw=90.0°*)
 78: 0x02CF [0x47] WAIT_PLAYER_POS_UPDATE
 79: 0x02D1 [0x01] GOTO 0x0397
 80: 0x02D4 [0x02] IF !(Work_Zone[7] == 2*) GOTO 0x02F8
 81: 0x02DC [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=531.000*, pos_z=-20.000*, pos_y=100.000*, direction=377476039.2°*)
 82: 0x02E9 [0x47] UPDATE_PLAYER_POS(531.000*, -20.000*, 100.000*, yaw=377476039.2°*)
 83: 0x02F3 [0x47] WAIT_PLAYER_POS_UPDATE
 84: 0x02F5 [0x01] GOTO 0x0397
 85: 0x02F8 [0x02] IF !(Work_Zone[7] == 3*) GOTO 0x031C
 86: 0x0300 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=580.000*, pos_z=29.000*, pos_y=100.000*, direction=377476129.2°*)
 87: 0x030D [0x47] UPDATE_PLAYER_POS(580.000*, 29.000*, 100.000*, yaw=377476129.2°*)
 88: 0x0317 [0x47] WAIT_PLAYER_POS_UPDATE
 89: 0x0319 [0x01] GOTO 0x0397
 90: 0x031C [0x02] IF !(Work_Zone[7] == 4*) GOTO 0x0340
 91: 0x0324 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-460.000*, pos_z=-69.000*, pos_y=-140.000*, direction=90.0°*)
 92: 0x0331 [0x47] UPDATE_PLAYER_POS(-460.000*, -69.000*, -140.000*, yaw=90.0°*)
 93: 0x033B [0x47] WAIT_PLAYER_POS_UPDATE
 94: 0x033D [0x01] GOTO 0x0397
 95: 0x0340 [0x02] IF !(Work_Zone[7] == 5*) GOTO 0x0364
 96: 0x0348 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-509.000*, pos_z=-20.000*, pos_y=-140.000*, direction=377476039.2°*)
 97: 0x0355 [0x47] UPDATE_PLAYER_POS(-509.000*, -20.000*, -140.000*, yaw=377476039.2°*)
 98: 0x035F [0x47] WAIT_PLAYER_POS_UPDATE
 99: 0x0361 [0x01] GOTO 0x0397
100: 0x0364 [0x02] IF !(Work_Zone[7] == 6*) GOTO 0x0388
101: 0x036C [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-460.000*, pos_z=29.000*, pos_y=-140.000*, direction=377476129.2°*)
102: 0x0379 [0x47] UPDATE_PLAYER_POS(-460.000*, 29.000*, -140.000*, yaw=377476129.2°*)
103: 0x0383 [0x47] WAIT_PLAYER_POS_UPDATE
104: 0x0385 [0x01] GOTO 0x0397
105: 0x0388 [0x02] IF !(Work_Zone[7] == 7*) GOTO 0x0397
106: 0x0390 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
107: 0x0392 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
108: 0x0394 [0x01] GOTO 0x0397

SUBROUTINE_0397:
109: 0x0397 [0x46] CAMERA_CONTROL: Restore default settings
110: 0x0399 [0x1C] WAIT(30* ticks)
111: 0x039C [0x02] IF !(Work_Zone[7] >= 7*) GOTO 0x03C7
112: 0x03A4 [0x80] LOAD_WAIT(entity=LocalPlayer)
113: 0x03A9 [0x1C] WAIT(15* ticks)
114: 0x03AC [0xAB] EventEntity->DespawnValue = 0* // Set despawn value
115: 0x03B0 [0x1C] WAIT(1* ticks)
116: 0x03B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
117: 0x03C4 [0x01] GOTO 0x03CC
118: 0x03C7 [0x03] Work_Zone[1] = 7*

SUBROUTINE_03CC:
119: 0x03CC [0x01] GOTO 0x03DF
120: 0x03CF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03DF
121: 0x03D7 [0x03] Work_Zone[1] = 1073741824*
122: 0x03DC [0x01] GOTO 0x03DF

SUBROUTINE_03DF:
123: 0x03DF [0x21] END_EVENT
124: 0x03E0 [0x00] END_REQSTACK()
```
