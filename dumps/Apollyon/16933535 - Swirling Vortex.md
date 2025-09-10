# 16933535 - Swirling Vortex

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 672 bytes         |
| Total Events     | 2                 |
| References Count | 38                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [114](#event-114)     | 0x0001       |    494 |             93 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x001F      |          31 |
|       2 | 0x1C49      |        7241 |
|       3 | 0x0001      |           1 |
|       4 | 0x0020      |          32 |
|       5 | 0x0002      |           2 |
|       6 | 0x0021      |          33 |
|       7 | 0x0003      |           3 |
|       8 | 0x0022      |          34 |
|       9 | 0x0004      |           4 |
|      10 | 0x0023      |          35 |
|      11 | 0x0005      |           5 |
|      12 | 0x0006      |           6 |
|      13 | 0x0007      |           7 |
|      14 | 0x00FF      |         255 |
|      15 | 0x0064      |         100 |
|      16 | 0xFFF6B900  |  4294359296 |
|      17 | 0xFFF6D840  |  4294367296 |
|      18 | 0x07E8      |        2024 |
|      19 | 0x94700     |      608000 |
|      20 | 0x6B6C0     |      440000 |
|      21 | 0xFFFEA840  |  4294879296 |
|      22 | 0x0C00      |        3072 |
|      23 | 0x825F0     |      534000 |
|      24 | 0x29BF8     |      171000 |
|      25 | 0x0E00      |        3584 |
|      26 | 0x47C70     |      294000 |
|      27 | 0x99520     |      628000 |
|      28 | 0x79568     |      497000 |
|      29 | 0x0A00      |        2560 |
|      30 | 0x5EBA0     |      388000 |
|      31 | 0x79950     |      498000 |
|      32 | 0x0049      |          73 |
|      33 | 0x008C      |         140 |
|      34 | 0x00C8      |         200 |
|      35 | 0x003C      |          60 |
|      36 | 0x004A      |          74 |
|      37 | 0x00AA      |         170 |

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

### Event 114

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 494 bytes |
| Instructions | 77        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 00 00 00 80  03 01 00 00 80 03 00 00    ..............
0010: 03 10 08 00 00 01 80 03  04 10 00 00 0B 04 10 24  ...............$
0020: 02 80 00 00 01 00 25 02  00 10 00 80 00 37 00 03  ......%......7..
0030: 01 10 01 80 01 A7 00 02  00 10 03 80 00 47 00 03  .............G..
0040: 01 10 04 80 01 A7 00 02  00 10 05 80 00 57 00 03  .............W..
0050: 01 10 06 80 01 A7 00 02  00 10 07 80 00 67 00 03  .............g..
0060: 01 10 08 80 01 A7 00 02  00 10 09 80 00 77 00 03  .............w..
0070: 01 10 0A 80 01 A7 00 02  00 10 0B 80 00 87 00 03  ................
0080: 01 10 03 80 01 A7 00 02  00 10 0C 80 00 97 00 03  ................
0090: 01 10 05 80 01 A7 00 02  00 10 0D 80 00 A7 00 03  ................
00A0: 01 10 00 80 01 A7 00 02  00 10 00 00 00 B7 00 03  ................
00B0: 01 10 0E 80 01 85 01 02  01 10 00 80 00 C2 00 01  ................
00C0: 85 01 42 03 02 00 01 10  03 01 10 0F 80 43 00 43  ..B..........C.C
00D0: 01 03 01 10 02 00 29 01  F0 FF FF 7F 02 02 01 10  ......).........
00E0: 03 80 80 F4 00 47 00 10  80 11 80 00 80 12 80 47  .....G.........G
00F0: 01 01 7E 01 02 01 10 05  80 80 0B 01 47 00 13 80  ..~.........G...
0100: 11 80 00 80 00 80 47 01  01 7E 01 02 01 10 01 80  ......G..~......
0110: 80 22 01 47 00 14 80 15  80 00 80 16 80 47 01 01  .".G.........G..
0120: 7E 01 02 01 10 04 80 80  39 01 47 00 17 80 18 80  ~.......9.G.....
0130: 00 80 19 80 47 01 01 7E  01 02 01 10 06 80 80 50  ....G..~.......P
0140: 01 47 00 1A 80 18 80 00  80 19 80 47 01 01 7E 01  .G.........G..~.
0150: 02 01 10 08 80 80 67 01  47 00 1B 80 1C 80 00 80  ......g.G.......
0160: 1D 80 47 01 01 7E 01 02  01 10 0A 80 80 7E 01 47  ..G..~.......~.G
0170: 00 1E 80 1F 80 00 80 1D  80 47 01 01 7E 01 29 01  .........G..~.).
0180: F0 FF FF 7F 03 20 00 21  00 9F 20 80 F0 FF FF 7F  ..... .!.. .....
0190: F0 FF FF 7F 6D 61 69 6E  00 80 03 02 00 01 10 03  ....main........
01A0: 01 10 0F 80 43 00 43 01  03 01 10 02 00 1C 21 80  ....C.C.......!.
01B0: 45 22 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 00  E".........fdo1.
01C0: 80 1C 23 80 46 01 1B 45  22 80 F0 FF FF 7F F0 FF  ..#.F..E".......
01D0: FF 7F 66 64 69 31 00 80  9F 24 80 F0 FF FF 7F F0  ..fdi1...$......
01E0: FF FF 7F 6D 61 69 6E 00  80 1C 25 80 46 00 1B     ...main...%.F.. 
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[0] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[1] = 0*
  3: 0x000D [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  4: 0x0012 [0x08] ExtData[1]->WorkLocal[0] -= 31*
  5: 0x0017 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[0]
  6: 0x001C [0x0B] Work_Zone[4]++
  7: 0x001F [0x24] CREATE_DIALOG(message_id=7241*, default_option=ExtData[1]->WorkLocal[0], option_flags=ExtData[1]->WorkLocal[1])
    → "Destination? (Currently [/NW/SW/NE/SE] #$2). [[/NW/SW/NE/SE] #1./[/NW/SW/NE/SE] #2./[/NW/SW/NE/SE] #3./[/NW/SW/NE/SE] #4./[/NW//NE] #5./Entrance #1./Entrance #2./Never mind.]"
  8: 0x0026 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0027 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0037
 10: 0x002F [0x03] Work_Zone[1] = 31*
 11: 0x0034 [0x01] GOTO 0x00A7
 12: 0x0037 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0047
 13: 0x003F [0x03] Work_Zone[1] = 32*
 14: 0x0044 [0x01] GOTO 0x00A7
 15: 0x0047 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0057
 16: 0x004F [0x03] Work_Zone[1] = 33*
 17: 0x0054 [0x01] GOTO 0x00A7
 18: 0x0057 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0067
 19: 0x005F [0x03] Work_Zone[1] = 34*
 20: 0x0064 [0x01] GOTO 0x00A7
 21: 0x0067 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0077
 22: 0x006F [0x03] Work_Zone[1] = 35*
 23: 0x0074 [0x01] GOTO 0x00A7
 24: 0x0077 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0087
 25: 0x007F [0x03] Work_Zone[1] = 1*
 26: 0x0084 [0x01] GOTO 0x00A7
 27: 0x0087 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0097
 28: 0x008F [0x03] Work_Zone[1] = 2*
 29: 0x0094 [0x01] GOTO 0x00A7
 30: 0x0097 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00A7
 31: 0x009F [0x03] Work_Zone[1] = 0*
 32: 0x00A4 [0x01] GOTO 0x00A7

SUBROUTINE_00A7:
 33: 0x00A7 [0x02] IF !(Work_Zone[0] == ExtData[1]->WorkLocal[0]) GOTO 0x00B7
 34: 0x00AF [0x03] Work_Zone[1] = 255*
 35: 0x00B4 [0x01] GOTO 0x0185
 36: 0x00B7 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x00C2
 37: 0x00BF [0x01] GOTO 0x0185
 38: 0x00C2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 39: 0x00C3 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[1]
 40: 0x00C8 [0x03] Work_Zone[1] = 100*
 41: 0x00CD [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 42: 0x00CF [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 43: 0x00D1 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
 44: 0x00D6 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 45: 0x00DD [0x02] IF !(Work_Zone[1] == 1*) GOTO 0x00F4
 46: 0x00E5 [0x47] UPDATE_PLAYER_POS(-608.000*, -600.000*, 0.000*, yaw=177.9°*)
 47: 0x00EF [0x47] WAIT_PLAYER_POS_UPDATE
 48: 0x00F1 [0x01] GOTO 0x017E
 49: 0x00F4 [0x02] IF !(Work_Zone[1] == 2*) GOTO 0x010B
 50: 0x00FC [0x47] UPDATE_PLAYER_POS(608.000*, -600.000*, 0.000*, yaw=0.0°*)
 51: 0x0106 [0x47] WAIT_PLAYER_POS_UPDATE
 52: 0x0108 [0x01] GOTO 0x017E
 53: 0x010B [0x02] IF !(Work_Zone[1] == 31*) GOTO 0x0122
 54: 0x0113 [0x47] UPDATE_PLAYER_POS(440.000*, -88.000*, 0.000*, yaw=270.0°*)
 55: 0x011D [0x47] WAIT_PLAYER_POS_UPDATE
 56: 0x011F [0x01] GOTO 0x017E
 57: 0x0122 [0x02] IF !(Work_Zone[1] == 32*) GOTO 0x0139
 58: 0x012A [0x47] UPDATE_PLAYER_POS(534.000*, 171.000*, 0.000*, yaw=315.0°*)
 59: 0x0134 [0x47] WAIT_PLAYER_POS_UPDATE
 60: 0x0136 [0x01] GOTO 0x017E
 61: 0x0139 [0x02] IF !(Work_Zone[1] == 33*) GOTO 0x0150
 62: 0x0141 [0x47] UPDATE_PLAYER_POS(294.000*, 171.000*, 0.000*, yaw=315.0°*)
 63: 0x014B [0x47] WAIT_PLAYER_POS_UPDATE
 64: 0x014D [0x01] GOTO 0x017E
 65: 0x0150 [0x02] IF !(Work_Zone[1] == 34*) GOTO 0x0167
 66: 0x0158 [0x47] UPDATE_PLAYER_POS(628.000*, 497.000*, 0.000*, yaw=225.0°*)
 67: 0x0162 [0x47] WAIT_PLAYER_POS_UPDATE
 68: 0x0164 [0x01] GOTO 0x017E
 69: 0x0167 [0x02] IF !(Work_Zone[1] == 35*) GOTO 0x017E
 70: 0x016F [0x47] UPDATE_PLAYER_POS(388.000*, 498.000*, 0.000*, yaw=225.0°*)
 71: 0x0179 [0x47] WAIT_PLAYER_POS_UPDATE
 72: 0x017B [0x01] GOTO 0x017E

SUBROUTINE_017E:
 73: 0x017E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_0185:
 74: 0x0185 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 75: 0x0187 [0x21] END_EVENT
 76: 0x0188 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0189 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[73*, 0*]
     0x019A [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[1]
     0x019F [0x03] Work_Zone[1] = 100*
     0x01A4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x01A6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x01A8 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
     0x01AD [0x1C] WAIT(140* ticks)
     0x01B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x01C1 [0x1C] WAIT(60* ticks)
     0x01C4 [0x46] CAMERA_CONTROL: Disable user control
     0x01C6 [0x1B] RETURN
     0x01C7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x01D8 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[74*, 0*]
     0x01E9 [0x1C] WAIT(170* ticks)
     0x01EC [0x46] CAMERA_CONTROL: Restore default settings
     0x01EE [0x1B] RETURN
```
