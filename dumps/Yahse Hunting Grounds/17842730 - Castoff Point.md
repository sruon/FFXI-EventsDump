# 17842730 - Castoff Point

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Yahse Hunting Grounds (ID: 260) |
| Block Size       | 728 bytes                       |
| Total Events     | 2                               |
| References Count | 31                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [16](#event-16)       | 0x0001       |    579 |             71 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0877      |        2167 |
|       2 | 0x089D      |        2205 |
|       3 | 0x1ECC      |        7884 |
|       4 | 0x1ECF      |        7887 |
|       5 | 0x0000      |           0 |
|       6 | 0x0004      |           4 |
|       7 | 0x00C8      |         200 |
|       8 | 0x67297     |      422551 |
|       9 | 0xFFFFC150  |  4294951248 |
|      10 | 0x004A      |          74 |
|      11 | 0x010F      |         271 |
|      12 | 0x5A2F1     |      369393 |
|      13 | 0xFFFFD473  |  4294956147 |
|      14 | 0x0FA0      |        4000 |
|      15 | 0x0726      |        1830 |
|      16 | 0x0013      |          19 |
|      17 | 0x58072     |      360562 |
|      18 | 0xFFFFD5A0  |  4294956448 |
|      19 | 0x0FC4      |        4036 |
|      20 | 0x66D0C     |      421132 |
|      21 | 0xFFFFC61F  |  4294952479 |
|      22 | 0x0239      |         569 |
|      23 | 0x07E1      |        2017 |
|      24 | 0x0017      |          23 |
|      25 | 0x0078      |         120 |
|      26 | 0x5ADF0     |      372208 |
|      27 | 0xFFFFD89E  |  4294957214 |
|      28 | 0x0F8C      |        3980 |
|      29 | 0x001E      |          30 |
|      30 | 0x005A      |          90 |

## String References

- **7884**: You should be able to head [to the other side/over there] if you have the $3 and $3.
- **7887**: Head [for the other side/over there]? [Yes./No./Dive right in.]

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
| Data Size    | 579 bytes |
| Instructions | 71        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 04 10 00 80 03 06  10 01 80 03 05 10 02 80   ...............
0010: 48 03 80 23 03 04 10 00  80 24 04 80 05 80 06 80  H..#.....$......
0020: 25 02 00 10 05 80 00 A2  00 42 43 00 43 01 1A AF  %........BC.C...
0030: 00 45 07 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0040: 05 80 55 07 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
0050: 31 02 02 10 05 80 80 68  00 47 00 08 80 09 80 0A  1......h.G......
0060: 80 0B 80 47 01 01 7F 00  02 02 10 00 80 80 7F 00  ...G............
0070: 47 00 0C 80 0D 80 0E 80  0F 80 47 01 01 7F 00 45  G.........G....E
0080: 07 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 05 80  ..........fdi1..
0090: 55 07 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  U..........fdi1.
00A0: AD 00 02 00 10 00 80 00  AD 00 01 AD 00 21 00 45  .............!.E
00B0: 07 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 05 80  ..........fdo1..
00C0: 55 07 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 46  U..........fdo1F
00D0: 01 38 10 80 02 02 10 05  80 00 EC 00 BA F0 FF FF  .8..............
00E0: 7F 11 80 12 80 0E 80 13  80 01 F9 00 BA F0 FF FF  ................
00F0: 7F 14 80 15 80 16 80 17  80 02 02 10 05 80 00 15  ................
0100: 01 45 18 80 F0 FF FF 7F  F0 FF FF 7F 73 33 30 35  .E..........s305
0110: 05 80 01 26 01 45 18 80  F0 FF FF 7F F0 FF FF 7F  ...&.E..........
0120: 73 33 30 33 05 80 45 07  80 F0 FF FF 7F F0 FF FF  s303..E.........
0130: 7F 66 64 69 32 05 80 27  10 F0 FF FF 7F 02 1C 19  .fdi2..'........
0140: 80 45 07 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0150: 05 80 55 07 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
0160: 31 2A 10 F0 FF FF 7F 02  02 10 05 80 00 A6 01 29  1*.............)
0170: 10 2C 42 10 01 03 BA F0  FF FF 7F 1A 80 1B 80 1C  .,B.............
0180: 80 18 80 52 18 80 F0 FF  FF 7F F0 FF FF 7F 73 33  ...R..........s3
0190: 30 35 45 18 80 F0 FF FF  7F F0 FF FF 7F 73 33 30  05E..........s30
01A0: 36 05 80 01 CD 01 29 10  2C 42 10 01 02 52 18 80  6.....).,B...R..
01B0: F0 FF FF 7F F0 FF FF 7F  73 33 30 33 45 18 80 F0  ........s303E...
01C0: FF FF 7F F0 FF FF 7F 73  33 30 34 05 80 45 07 80  .......s304..E..
01D0: F0 FF FF 7F F0 FF FF 7F  66 64 69 32 05 80 1C 1D  ........fdi2....
01E0: 80 27 10 F0 FF FF 7F 03  1C 1E 80 45 07 80 F0 FF  .'.........E....
01F0: FF 7F F0 FF FF 7F 66 64  6F 31 05 80 55 07 80 F0  ......fdo1..U...
0200: FF FF 7F F0 FF FF 7F 66  64 6F 31 2A 10 F0 FF FF  .......fdo1*....
0210: 7F 02 02 10 05 80 00 2B  02 52 18 80 F0 FF FF 7F  .......+.R......
0220: F0 FF FF 7F 73 33 30 36  01 3A 02 52 18 80 F0 FF  ....s306.:.R....
0230: FF 7F F0 FF FF 7F 73 33  30 34 29 10 2C 42 10 01  ......s304).,B..
0240: 04 46 00 1B                                       .F..            
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[4] = 1*
  1: 0x0006 [0x03] Work_Zone[6] = 2167*
  2: 0x000B [0x03] Work_Zone[5] = 2205*
  3: 0x0010 [0x48] [System] [7884*]:
    → "You should be able to head [to the other side/over there] if you have the $3 and $3."
  4: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0014 [0x03] Work_Zone[4] = 1*
  6: 0x0019 [0x24] CREATE_DIALOG(message_id=7887*, default_option=0*, option_flags=4*)
    → "Head [for the other side/over there]? [Yes./No./Dive right in.]"
  7: 0x0020 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0021 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00A2
  9: 0x0029 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x002A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x002C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x002E [0x1A] CALL_SUBROUTINE(address=0x00AF)
 13: 0x0031 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0042 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 15: 0x0051 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0068
 16: 0x0059 [0x47] UPDATE_PLAYER_POS(422.551*, -16.048*, 0.074*, yaw=23.8°*)
 17: 0x0063 [0x47] WAIT_PLAYER_POS_UPDATE
 18: 0x0065 [0x01] GOTO 0x007F
 19: 0x0068 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x007F
 20: 0x0070 [0x47] UPDATE_PLAYER_POS(369.393*, -11.149*, 4.000*, yaw=160.8°*)
 21: 0x007A [0x47] WAIT_PLAYER_POS_UPDATE
 22: 0x007C [0x01] GOTO 0x007F

SUBROUTINE_007F:
 23: 0x007F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x0090 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 25: 0x009F [0x01] GOTO 0x00AD
 26: 0x00A2 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00AD
 27: 0x00AA [0x01] GOTO 0x00AD

SUBROUTINE_00AD:
 28: 0x00AD [0x21] END_EVENT
 29: 0x00AE [0x00] END_REQSTACK()

SUBROUTINE_00AF:
 30: 0x00AF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x00C0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 32: 0x00CF [0x46] CAMERA_CONTROL: Disable user control
 33: 0x00D1 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 34: 0x00D4 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00EC
 35: 0x00DC [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=360.562*, pos_z=-10.848*, pos_y=4.000*, direction=354.7°*)
 36: 0x00E9 [0x01] GOTO 0x00F9
 37: 0x00EC [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=421.132*, pos_z=-14.817*, pos_y=0.569*, direction=177.3°*)

SUBROUTINE_00F9:
 38: 0x00F9 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0115
 39: 0x0101 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s305" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
 40: 0x0112 [0x01] GOTO 0x0126
 41: 0x0115 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s303" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]

SUBROUTINE_0126:
 42: 0x0126 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x0137 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
 44: 0x013E [0x1C] WAIT(120* ticks)
 45: 0x0141 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 46: 0x0152 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 47: 0x0161 [0x2A] GET_REQ_LEVEL(level=16, entity_id=LocalPlayer)
 48: 0x0167 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x01A6
 49: 0x016F [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Unnamed NPC (ID: 17842732/0x0110422C), tag_num=0x03)
 50: 0x0176 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=372.208*, pos_z=-10.082*, pos_y=3.980*, direction=2.0°*)
 51: 0x0183 [0x52] END_LOAD_SCHEDULER: End scheduler "s305" with entities [LocalPlayer, LocalPlayer], work=23*
 52: 0x0192 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s306" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
 53: 0x01A3 [0x01] GOTO 0x01CD
 54: 0x01A6 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Unnamed NPC (ID: 17842732/0x0110422C), tag_num=0x02)
 55: 0x01AD [0x52] END_LOAD_SCHEDULER: End scheduler "s303" with entities [LocalPlayer, LocalPlayer], work=23*
 56: 0x01BC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s304" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]

SUBROUTINE_01CD:
 57: 0x01CD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 58: 0x01DE [0x1C] WAIT(30* ticks)
 59: 0x01E1 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x03)
 60: 0x01E8 [0x1C] WAIT(90* ticks)
 61: 0x01EB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 62: 0x01FC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 63: 0x020B [0x2A] GET_REQ_LEVEL(level=16, entity_id=LocalPlayer)
 64: 0x0211 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x022B
 65: 0x0219 [0x52] END_LOAD_SCHEDULER: End scheduler "s306" with entities [LocalPlayer, LocalPlayer], work=23*
 66: 0x0228 [0x01] GOTO 0x023A
 67: 0x022B [0x52] END_LOAD_SCHEDULER: End scheduler "s304" with entities [LocalPlayer, LocalPlayer], work=23*

SUBROUTINE_023A:
 68: 0x023A [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Unnamed NPC (ID: 17842732/0x0110422C), tag_num=0x04)
 69: 0x0241 [0x46] CAMERA_CONTROL: Restore default settings
 70: 0x0243 [0x1B] RETURN
```
