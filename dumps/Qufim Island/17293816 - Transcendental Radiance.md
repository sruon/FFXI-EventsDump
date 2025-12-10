# 17293816 - Transcendental Radiance

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qufim Island (ID: 126) |
| Block Size       | 1092 bytes             |
| Total Events     | 3                      |
| References Count | 20                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [47](#event-47)       | 0x0001       |      1 |              1 |
| [46](#event-46)       | 0x0002       |    981 |            117 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0280      |         640 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0602      |        1538 |
|       4 | 0x04F7      |        1271 |
|       5 | 0x2CFB      |       11515 |
|       6 | 0x2CFE      |       11518 |
|       7 | 0x003C      |          60 |
|       8 | 0x2CFD      |       11517 |
|       9 | 0x2CFF      |       11519 |
|      10 | 0x40000000  |  1073741824 |
|      11 | 0x00C8      |         200 |
|      12 | 0x0013      |          19 |
|      13 | 0x0230      |         560 |
|      14 | 0x00C9      |         201 |
|      15 | 0x001E      |          30 |
|      16 | 0x0088      |         136 |
|      17 | 0x002D      |          45 |
|      18 | 0x0002      |           2 |
|      19 | 0x00D7      |         215 |

## String References

- **11515**: Your $3 resonates with the eerie light before you.
- **11517**: [Enter the portal/Warp to Abyssea - Empyreal Paradox]? [Proceed. ($3 cruor)/Not yet.]
- **11518**: Cruor will not be expended for those possessing $6.
- **11519**: You do not have enough energy in cruor to warp to your destination.

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

### Event 47

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

### Event 46

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 981 bytes |
| Instructions | 62        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 4A F0 FF FF  7F F8 E1 07 01 6F 76 F0     .J........ov.
0010: FF FF 7F 79 02 F0 FF FF  7F 00 80 01 80 02 09 10  ...y............
0020: 02 80 00 2D 00 03 02 10  03 80 01 32 00 03 02 10  ...-.......2....
0030: 04 80 48 05 80 23 03 02  10 03 80 48 06 80 1C 07  ..H..#.....H....
0040: 80 43 00 43 01 03 02 10  02 80 24 08 80 02 80 01  .C.C......$.....
0050: 80 25 02 00 10 01 80 00  37 01 43 00 43 01 03 00  .%......7.C.C...
0060: 00 03 10 02 00 00 02 80  00 73 00 03 01 10 02 80  .........s......
0070: 01 87 00 02 06 10 02 80  00 7F 00 48 09 80 23 03  ...........H..#.
0080: 01 10 0A 80 01 42 01 42  46 01 45 0B 80 F0 FF FF  .....B.BF.E.....
0090: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 07 80 38 0C  .....fdo1.....8.
00A0: 80 29 01 F0 FF FF 7F 2F  45 0D 80 F0 FF FF 7F F0  .)...../E.......
00B0: FF FF 7F 33 37 30 30 01  80 45 0B 80 F0 FF FF 7F  ...3700..E......
00C0: F0 FF FF 7F 66 64 69 31  01 80 1C 07 80 45 0B 80  ....fdi1.....E..
00D0: F0 FF FF 7F F0 FF FF 7F  62 6C 6F 6E 01 80 45 0E  ........blon..E.
00E0: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 01 80 45  .........blon..E
00F0: 0B 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 01 80  ..........ovl1..
0100: 29 01 F0 FF FF 7F 30 45  0B 80 F0 FF FF 7F F0 FF  ).....0E........
0110: FF 7F 62 6C 6F 66 01 80  1C 0F 80 C5 10 80 F0 FF  ..blof..........
0120: FF 7F F0 FF FF 7F 6B 69  6C 61 01 80 1A A9 01 1A  ......kila......
0130: CA 01 46 00 01 42 01 02  00 10 02 80 00 42 01 01  ..F..B.......B..
0140: 42 01 20 00 21 00 45 0B  80 F0 FF FF 7F F0 FF FF  B. .!.E.........
0150: 7F 66 64 69 30 01 80 55  0B 80 F0 FF FF 7F F0 FF  .fdi0..U........
0160: FF 7F 66 64 69 30 1B 45  0B 80 F0 FF FF 7F F0 FF  ..fdi0.E........
0170: FF 7F 66 64 6F 30 01 80  55 0B 80 F0 FF FF 7F F0  ..fdo0..U.......
0180: FF FF 7F 66 64 6F 30 1B  45 0B 80 F0 FF FF 7F F0  ...fdo0.E.......
0190: FF FF 7F 66 64 69 31 01  80 55 0B 80 F0 FF FF 7F  ...fdi1..U......
01A0: F0 FF FF 7F 66 64 69 31  1B 45 0B 80 F0 FF FF 7F  ....fdi1.E......
01B0: F0 FF FF 7F 66 64 6F 31  01 80 55 0B 80 F0 FF FF  ....fdo1..U.....
01C0: 7F F0 FF FF 7F 66 64 6F  31 1B 45 0E 80 F0 FF FF  .....fdo1.E.....
01D0: 7F F0 FF FF 7F 77 68 69  31 01 80 55 0E 80 F0 FF  .....whi1..U....
01E0: FF 7F F0 FF FF 7F 77 68  69 31 1B 45 0E 80 F0 FF  ......whi1.E....
01F0: FF 7F F0 FF FF 7F 77 68  6F 31 01 80 55 0E 80 F0  ......who1..U...
0200: FF FF 7F F0 FF FF 7F 77  68 6F 31 1B 45 0E 80 F0  .......who1.E...
0210: FF FF 7F F0 FF FF 7F 77  68 6F 32 01 80 55 0E 80  .......who2..U..
0220: F0 FF FF 7F F0 FF FF 7F  77 68 6F 32 1B 45 0E 80  ........who2.E..
0230: F0 FF FF 7F F0 FF FF 7F  77 68 6F 33 01 80 55 0E  ........who3..U.
0240: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 33 1B 62 02  .........who3.b.
0250: 80 F0 FF FF 7F F0 FF FF  7F 6D 61 69 6E 01 80 1C  .........main...
0260: 11 80 45 0B 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0270: 31 01 80 55 0B 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U..........fd
0280: 6F 31 1B 45 0B 80 F0 FF  FF 7F F0 FF FF 7F 66 64  o1.E..........fd
0290: 69 31 01 80 62 12 80 F0  FF FF 7F F0 FF FF 7F 6D  i1..b..........m
02A0: 61 69 6E 01 80 1C 0F 80  55 0B 80 F0 FF FF 7F F0  ain.....U.......
02B0: FF FF 7F 66 64 69 31 1B  45 0B 80 F0 FF FF 7F F0  ...fdi1.E.......
02C0: FF FF 7F 62 6C 6F 6E 01  80 45 0E 80 F0 FF FF 7F  ...blon..E......
02D0: F0 FF FF 7F 62 6C 6F 6E  01 80 1B 45 0E 80 F0 FF  ....blon...E....
02E0: FF 7F F0 FF FF 7F 77 68  69 30 01 80 55 0E 80 F0  ......whi0..U...
02F0: FF FF 7F F0 FF FF 7F 77  68 69 30 1B 45 0E 80 F0  .......whi0.E...
0300: FF FF 7F F0 FF FF 7F 77  68 6F 30 01 80 55 0E 80  .......who0..U..
0310: F0 FF FF 7F F0 FF FF 7F  77 68 6F 30 1B 45 13 80  ........who0.E..
0320: F0 FF FF 7F F0 FF FF 7F  65 66 6F 6E 01 80 55 13  ........efon..U.
0330: 80 F0 FF FF 7F F0 FF FF  7F 65 66 6F 6E 1B 45 0B  .........efon.E.
0340: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 73 01 80 1B  .........fdis...
0350: 45 0B 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 73 01  E..........fdos.
0360: 80 55 0B 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 73  .U..........fdos
0370: 1B 45 0B 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 66  .E..........fdif
0380: 01 80 1B 45 0B 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0390: 6F 66 01 80 55 0B 80 F0  FF FF 7F F0 FF FF 7F 66  of..U..........f
03A0: 64 6F 66 1B 45 0B 80 F0  FF FF 7F F0 FF FF 7F 66  dof.E..........f
03B0: 64 69 70 01 80 1B 45 0B  80 F0 FF FF 7F F0 FF FF  dip...E.........
03C0: 7F 66 64 6F 70 01 80 55  0B 80 F0 FF FF 7F F0 FF  .fdop..U........
03D0: FF 7F 66 64 6F 70 1B                              ..fdop.         
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x4A] LocalPlayer looks at Transcendental Radiance (ID: 17293816/0x0107E1F8)
  2: 0x000D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000E [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  4: 0x0013 [0x79] LocalPlayer looks at Unknown NPC (ID: 2147581952/0x80018000) (Direct axis set)
  5: 0x001D [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x002D
  6: 0x0025 [0x03] Work_Zone[2] = 1538*
  7: 0x002A [0x01] GOTO 0x0032
  8: 0x002D [0x03] Work_Zone[2] = 1271*

SUBROUTINE_0032:
  9: 0x0032 [0x48] [System] [11515*]:
    → "Your $3 resonates with the eerie light before you."
 10: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0036 [0x03] Work_Zone[2] = 1538*
 12: 0x003B [0x48] [System] [11518*]:
    → "Cruor will not be expended for those possessing $6."
 13: 0x003E [0x1C] WAIT(60* ticks)
 14: 0x0041 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 15: 0x0043 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 16: 0x0045 [0x03] Work_Zone[2] = 1*
 17: 0x004A [0x24] CREATE_DIALOG(message_id=11517*, default_option=1*, option_flags=0*)
    → "[Enter the portal/Warp to Abyssea - Empyreal Paradox]? [Proceed. ($3 cruor)/Not yet.]"
 18: 0x0051 [0x25] WAIT_DIALOG_SELECT()
 19: 0x0052 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0137
 20: 0x005A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 21: 0x005C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 22: 0x005E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
 23: 0x0063 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0073
 24: 0x006B [0x03] Work_Zone[1] = 1*
 25: 0x0070 [0x01] GOTO 0x0087
 26: 0x0073 [0x02] IF !(Work_Zone[6] == 1*) GOTO 0x007F
 27: 0x007B [0x48] [System] [11519*]:
    → "You do not have enough energy in cruor to warp to your destination."
 28: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x007F [0x03] Work_Zone[1] = 1073741824*
 30: 0x0084 [0x01] GOTO 0x0142

SUBROUTINE_0087:
 31: 0x0087 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 32: 0x0088 [0x46] CAMERA_CONTROL: Disable user control
 33: 0x008A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 34: 0x009B [0x1C] WAIT(60* ticks)
 35: 0x009E [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 36: 0x00A1 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x2F)
 37: 0x00A8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "3700" with entities [LocalPlayer, LocalPlayer], work=[560*, 0*]
 38: 0x00B9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x00CA [0x1C] WAIT(60* ticks)
 40: 0x00CD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 41: 0x00DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 42: 0x00EF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x0100 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x30)
 44: 0x0107 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 45: 0x0118 [0x1C] WAIT(30* ticks)
 46: 0x011B [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8001616C for entities [LocalPlayer, LocalPlayer], work=136*, param=26987
 47: 0x012C [0x1A] CALL_SUBROUTINE(address=0x01A9)
 48: 0x012F [0x1A] CALL_SUBROUTINE(address=0x01CA)
 49: 0x0132 [0x46] CAMERA_CONTROL: Restore default settings
 50: 0x0134 [0x01] GOTO 0x0142
 51: 0x0137 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0142
 52: 0x013F [0x01] GOTO 0x0142

SUBROUTINE_0142:
 53: 0x0142 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 54: 0x0144 [0x21] END_EVENT
 55: 0x0145 [0x00] END_REQSTACK()

SUBROUTINE_01A9:
 56: 0x01A9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x01BA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 58: 0x01C9 [0x1B] RETURN

SUBROUTINE_01CA:
 59: 0x01CA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 60: 0x01DB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
 61: 0x01EA [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0146 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0157 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0166 [0x1B] RETURN
     0x0167 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0178 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0187 [0x1B] RETURN
     0x0188 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0199 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x01A8 [0x1B] RETURN
# Dead code (unreachable instructions):
     0x01EB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01FC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x020B [0x1B] RETURN
     0x020C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x021D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x022C [0x1B] RETURN
     0x022D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x023E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x024D [0x1B] RETURN
     0x024E [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x025F [0x1C] WAIT(45* ticks)
     0x0262 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0273 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0282 [0x1B] RETURN
     0x0283 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0294 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x02A5 [0x1C] WAIT(30* ticks)
     0x02A8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x02B7 [0x1B] RETURN
     0x02B8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02DA [0x1B] RETURN
     0x02DB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02EC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x02FB [0x1B] RETURN
     0x02FC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x030D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x031C [0x1B] RETURN
     0x031D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x032E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x033D [0x1B] RETURN
     0x033E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x034F [0x1B] RETURN
     0x0350 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0361 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0370 [0x1B] RETURN
     0x0371 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0382 [0x1B] RETURN
     0x0383 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0394 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x03A3 [0x1B] RETURN
     0x03A4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03B5 [0x1B] RETURN
     0x03B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03C7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x03D6 [0x1B] RETURN
```
