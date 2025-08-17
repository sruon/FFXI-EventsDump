# 16933525 - Swirling Vortex

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 644 bytes         |
| Total Events     | 2                 |
| References Count | 35                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [112](#event-112)     | 0x0001       |    478 |             90 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0015      |          21 |
|       2 | 0x0004      |           4 |
|       3 | 0x0001      |           1 |
|       4 | 0x1C49      |        7241 |
|       5 | 0x0016      |          22 |
|       6 | 0x0002      |           2 |
|       7 | 0x0017      |          23 |
|       8 | 0x0003      |           3 |
|       9 | 0x0018      |          24 |
|      10 | 0x0019      |          25 |
|      11 | 0x0005      |           5 |
|      12 | 0x0006      |           6 |
|      13 | 0x0007      |           7 |
|      14 | 0x00FF      |         255 |
|      15 | 0x0064      |         100 |
|      16 | 0xFFF6B900  |  4294359296 |
|      17 | 0xFFF6D840  |  4294367296 |
|      18 | 0x07E8      |        2024 |
|      19 | 0x94700     |      608000 |
|      20 | 0xFFF8DBE0  |  4294499296 |
|      21 | 0xFFF67698  |  4294342296 |
|      22 | 0x0E00      |        3584 |
|      23 | 0xFFF73600  |  4294391296 |
|      24 | 0xFFF97820  |  4294539296 |
|      25 | 0x0A00      |        2560 |
|      26 | 0xFFFA2018  |  4294582296 |
|      27 | 0xFFFD5080  |  4294791296 |
|      28 | 0xFFF66AE0  |  4294339296 |
|      29 | 0x0049      |          73 |
|      30 | 0x008C      |         140 |
|      31 | 0x00C8      |         200 |
|      32 | 0x003C      |          60 |
|      33 | 0x004A      |          74 |
|      34 | 0x00AA      |         170 |

## String References

- **7241**: Destination? (Currently [/NW/SW/NE/SE] #$2). [[/NW/SW/NE/SE] #1./[/NW/SW/NE/SE] #2./[/NW/SW/NE/SE] #3./[/NW/SW/NE/SE] #4./[/NW//NE] #5./Entrance #1./Entrance #2./Never mind.]

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

### Event 112

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 478 bytes |
| Instructions | 74        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 00 00 00 80  03 01 00 00 80 03 00 00    ..............
0010: 03 10 08 00 00 01 80 3C  01 00 02 80 03 80 03 04  .......<........
0020: 10 00 00 0B 04 10 24 04  80 00 00 01 00 25 02 00  ......$......%..
0030: 10 00 80 00 3E 00 03 01  10 01 80 01 AE 00 02 00  ....>...........
0040: 10 03 80 00 4E 00 03 01  10 05 80 01 AE 00 02 00  ....N...........
0050: 10 06 80 00 5E 00 03 01  10 07 80 01 AE 00 02 00  ....^...........
0060: 10 08 80 00 6E 00 03 01  10 09 80 01 AE 00 02 00  ....n...........
0070: 10 02 80 00 7E 00 03 01  10 0A 80 01 AE 00 02 00  ....~...........
0080: 10 0B 80 00 8E 00 03 01  10 03 80 01 AE 00 02 00  ................
0090: 10 0C 80 00 9E 00 03 01  10 06 80 01 AE 00 02 00  ................
00A0: 10 0D 80 00 AE 00 03 01  10 00 80 01 AE 00 02 00  ................
00B0: 10 00 00 00 BE 00 03 01  10 0E 80 01 75 01 02 01  ............u...
00C0: 10 00 80 00 C9 00 01 75  01 42 03 02 00 01 10 03  .......u.B......
00D0: 01 10 0F 80 43 00 43 01  03 01 10 02 00 29 01 F0  ....C.C......)..
00E0: FF FF 7F 02 02 01 10 03  80 80 FB 00 47 00 10 80  ............G...
00F0: 11 80 00 80 12 80 47 01  01 6E 01 02 01 10 06 80  ......G..n......
0100: 80 12 01 47 00 13 80 11  80 00 80 00 80 47 01 01  ...G.........G..
0110: 6E 01 02 01 10 01 80 80  29 01 47 00 14 80 15 80  n.......).G.....
0120: 00 80 16 80 47 01 01 6E  01 02 01 10 05 80 80 40  ....G..n.......@
0130: 01 47 00 17 80 18 80 00  80 19 80 47 01 01 6E 01  .G.........G..n.
0140: 02 01 10 07 80 80 57 01  47 00 18 80 1A 80 00 80  ......W.G.......
0150: 16 80 47 01 01 6E 01 02  01 10 09 80 80 6E 01 47  ..G..n.......n.G
0160: 00 1B 80 1C 80 00 80 19  80 47 01 01 6E 01 29 01  .........G..n.).
0170: F0 FF FF 7F 03 20 00 21  00 9F 1D 80 F0 FF FF 7F  ..... .!........
0180: F0 FF FF 7F 6D 61 69 6E  00 80 03 02 00 01 10 03  ....main........
0190: 01 10 0F 80 43 00 43 01  03 01 10 02 00 1C 1E 80  ....C.C.........
01A0: 45 1F 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 00  E..........fdo1.
01B0: 80 1C 20 80 46 01 1B 45  1F 80 F0 FF FF 7F F0 FF  .. .F..E........
01C0: FF 7F 66 64 69 31 00 80  9F 21 80 F0 FF FF 7F F0  ..fdi1...!......
01D0: FF FF 7F 6D 61 69 6E 00  80 1C 22 80 46 00 1B     ...main...".F.. 
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[0] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[1] = 0*
  3: 0x000D [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  4: 0x0012 [0x08] ExtData[1]->WorkLocal[0] -= 21*
  5: 0x0017 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=4*, condition_work_offset=1*)
  6: 0x001E [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[0]
  7: 0x0023 [0x0B] Work_Zone[4]++
  8: 0x0026 [0x24] CREATE_DIALOG(message_id=7241*, default_option=ExtData[1]->WorkLocal[0], option_flags=ExtData[1]->WorkLocal[1])
    → "Destination? (Currently [/NW/SW/NE/SE] #$2). [[/NW/SW/NE/SE] #1./[/NW/SW/NE/SE] #2./[/NW/SW/NE/SE] #3./[/NW/SW/NE/SE] #4./[/NW//NE] #5./Entrance #1./Entrance #2./Never mind.]"
  9: 0x002D [0x25] WAIT_DIALOG_SELECT()
 10: 0x002E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003E
 11: 0x0036 [0x03] Work_Zone[1] = 21*
 12: 0x003B [0x01] GOTO 0x00AE
 13: 0x003E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004E
 14: 0x0046 [0x03] Work_Zone[1] = 22*
 15: 0x004B [0x01] GOTO 0x00AE
 16: 0x004E [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x005E
 17: 0x0056 [0x03] Work_Zone[1] = 23*
 18: 0x005B [0x01] GOTO 0x00AE
 19: 0x005E [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x006E
 20: 0x0066 [0x03] Work_Zone[1] = 24*
 21: 0x006B [0x01] GOTO 0x00AE
 22: 0x006E [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x007E
 23: 0x0076 [0x03] Work_Zone[1] = 25*
 24: 0x007B [0x01] GOTO 0x00AE
 25: 0x007E [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x008E
 26: 0x0086 [0x03] Work_Zone[1] = 1*
 27: 0x008B [0x01] GOTO 0x00AE
 28: 0x008E [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x009E
 29: 0x0096 [0x03] Work_Zone[1] = 2*
 30: 0x009B [0x01] GOTO 0x00AE
 31: 0x009E [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00AE
 32: 0x00A6 [0x03] Work_Zone[1] = 0*
 33: 0x00AB [0x01] GOTO 0x00AE

SUBROUTINE_00AE:
 34: 0x00AE [0x02] IF !(Work_Zone[0] == ExtData[1]->WorkLocal[0]) GOTO 0x00BE
 35: 0x00B6 [0x03] Work_Zone[1] = 255*
 36: 0x00BB [0x01] GOTO 0x0175
 37: 0x00BE [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x00C9
 38: 0x00C6 [0x01] GOTO 0x0175
 39: 0x00C9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 40: 0x00CA [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[1]
 41: 0x00CF [0x03] Work_Zone[1] = 100*
 42: 0x00D4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 43: 0x00D6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 44: 0x00D8 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
 45: 0x00DD [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 46: 0x00E4 [0x02] IF !(Work_Zone[1] == 1*) GOTO 0x00FB
 47: 0x00EC [0x47] UPDATE_PLAYER_POS(-608.000*, -600.000*, 0.000*, yaw=177.9°*)
 48: 0x00F6 [0x47] WAIT_PLAYER_POS_UPDATE
 49: 0x00F8 [0x01] GOTO 0x016E
 50: 0x00FB [0x02] IF !(Work_Zone[1] == 2*) GOTO 0x0112
 51: 0x0103 [0x47] UPDATE_PLAYER_POS(608.000*, -600.000*, 0.000*, yaw=0.0°*)
 52: 0x010D [0x47] WAIT_PLAYER_POS_UPDATE
 53: 0x010F [0x01] GOTO 0x016E
 54: 0x0112 [0x02] IF !(Work_Zone[1] == 21*) GOTO 0x0129
 55: 0x011A [0x47] UPDATE_PLAYER_POS(-468.000*, -625.000*, 0.000*, yaw=315.0°*)
 56: 0x0124 [0x47] WAIT_PLAYER_POS_UPDATE
 57: 0x0126 [0x01] GOTO 0x016E
 58: 0x0129 [0x02] IF !(Work_Zone[1] == 22*) GOTO 0x0140
 59: 0x0131 [0x47] UPDATE_PLAYER_POS(-576.000*, -428.000*, 0.000*, yaw=225.0°*)
 60: 0x013B [0x47] WAIT_PLAYER_POS_UPDATE
 61: 0x013D [0x01] GOTO 0x016E
 62: 0x0140 [0x02] IF !(Work_Zone[1] == 23*) GOTO 0x0157
 63: 0x0148 [0x47] UPDATE_PLAYER_POS(-428.000*, -385.000*, 0.000*, yaw=315.0°*)
 64: 0x0152 [0x47] WAIT_PLAYER_POS_UPDATE
 65: 0x0154 [0x01] GOTO 0x016E
 66: 0x0157 [0x02] IF !(Work_Zone[1] == 24*) GOTO 0x016E
 67: 0x015F [0x47] UPDATE_PLAYER_POS(-176.000*, -628.000*, 0.000*, yaw=225.0°*)
 68: 0x0169 [0x47] WAIT_PLAYER_POS_UPDATE
 69: 0x016B [0x01] GOTO 0x016E

SUBROUTINE_016E:
 70: 0x016E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_0175:
 71: 0x0175 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 72: 0x0177 [0x21] END_EVENT
 73: 0x0178 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0179 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[73*, 0*]
     0x018A [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[1]
     0x018F [0x03] Work_Zone[1] = 100*
     0x0194 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0196 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0198 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
     0x019D [0x1C] WAIT(140* ticks)
     0x01A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x01B1 [0x1C] WAIT(60* ticks)
     0x01B4 [0x46] CAMERA_CONTROL: Disable user control
     0x01B6 [0x1B] RETURN
     0x01B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x01C8 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[74*, 0*]
     0x01D9 [0x1C] WAIT(170* ticks)
     0x01DC [0x46] CAMERA_CONTROL: Restore default settings
     0x01DE [0x1B] RETURN
```
