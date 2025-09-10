# 16929622 - Matter Diffusion Module

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 728 bytes        |
| Total Events     | 2                |
| References Count | 40               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1001](#event-1001)   | 0x0001       |    543 |            101 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x000B      |          11 |
|       2 | 0x1C41      |        7233 |
|       3 | 0x0001      |           1 |
|       4 | 0x000C      |          12 |
|       5 | 0x0002      |           2 |
|       6 | 0x000D      |          13 |
|       7 | 0x0003      |           3 |
|       8 | 0x000E      |          14 |
|       9 | 0x0004      |           4 |
|      10 | 0x000F      |          15 |
|      11 | 0x0005      |           5 |
|      12 | 0x0010      |          16 |
|      13 | 0x0006      |           6 |
|      14 | 0x0011      |          17 |
|      15 | 0x0007      |           7 |
|      16 | 0x0008      |           8 |
|      17 | 0x00FF      |         255 |
|      18 | 0x0064      |         100 |
|      19 | 0x8D9A0     |      580000 |
|      20 | 0x14FF0     |       86000 |
|      21 | 0x0400      |        1024 |
|      22 | 0x5CC60     |      380000 |
|      23 | 0x5BCC0     |      376000 |
|      24 | 0x117C4     |       71620 |
|      25 | 0x0C00      |        3072 |
|      26 | 0x2BF20     |      180000 |
|      27 | 0xFFFEBE34  |  4294884916 |
|      28 | 0xEA60      |       60000 |
|      29 | 0xFFFDDD20  |  4294827296 |
|      30 | 0xFFFC0860  |  4294707296 |
|      31 | 0x12F34     |       77620 |
|      32 | 0xFFF8FB20  |  4294507296 |
|      33 | 0xFFF72660  |  4294387296 |
|      34 | 0x004B      |          75 |
|      35 | 0x0028      |          40 |
|      36 | 0x00C8      |         200 |
|      37 | 0x003C      |          60 |
|      38 | 0x004C      |          76 |
|      39 | 0x00AA      |         170 |

## String References

- **7233**: Destination? (Currently: [/N/W/E/C] Tower, Floor $2). [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Entrance./Never mind.]

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

### Event 1001

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 543 bytes |
| Instructions | 86        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 00 00 00 80  03 01 00 00 80 03 00 00    ..............
0010: 03 10 08 00 00 01 80 03  04 10 00 00 0B 04 10 24  ...............$
0020: 02 80 00 00 01 00 25 02  00 10 00 80 00 37 00 03  ......%......7..
0030: 01 10 01 80 01 B7 00 02  00 10 03 80 00 47 00 03  .............G..
0040: 01 10 04 80 01 B7 00 02  00 10 05 80 00 57 00 03  .............W..
0050: 01 10 06 80 01 B7 00 02  00 10 07 80 00 67 00 03  .............g..
0060: 01 10 08 80 01 B7 00 02  00 10 09 80 00 77 00 03  .............w..
0070: 01 10 0A 80 01 B7 00 02  00 10 0B 80 00 87 00 03  ................
0080: 01 10 0C 80 01 B7 00 02  00 10 0D 80 00 97 00 03  ................
0090: 01 10 0E 80 01 B7 00 02  00 10 0F 80 00 A7 00 03  ................
00A0: 01 10 03 80 01 B7 00 02  00 10 10 80 00 B7 00 03  ................
00B0: 01 10 00 80 01 B7 00 02  00 10 00 00 00 C7 00 03  ................
00C0: 01 10 11 80 01 B7 01 02  01 10 00 80 00 D2 00 01  ................
00D0: B7 01 02 01 10 03 10 00  DD 00 01 B7 01 42 03 02  .............B..
00E0: 00 01 10 03 01 10 12 80  43 00 43 01 03 01 10 02  ........C.C.....
00F0: 00 29 01 F0 FF FF 7F 02  02 01 10 03 80 80 0F 01  .)..............
0100: 47 00 13 80 14 80 00 80  15 80 47 01 01 B0 01 02  G.........G.....
0110: 01 10 01 80 80 26 01 47  00 16 80 17 80 18 80 19  .....&.G........
0120: 80 47 01 01 B0 01 02 01  10 04 80 80 3D 01 47 00  .G..........=.G.
0130: 1A 80 17 80 1B 80 19 80  47 01 01 B0 01 02 01 10  ........G.......
0140: 06 80 80 54 01 47 00 1C  80 17 80 18 80 19 80 47  ...T.G.........G
0150: 01 01 B0 01 02 01 10 08  80 80 6B 01 47 00 1D 80  ..........k.G...
0160: 17 80 1B 80 19 80 47 01  01 B0 01 02 01 10 0A 80  ......G.........
0170: 80 82 01 47 00 1E 80 17  80 1F 80 19 80 47 01 01  ...G.........G..
0180: B0 01 02 01 10 0C 80 80  99 01 47 00 20 80 17 80  ..........G. ...
0190: 1B 80 19 80 47 01 01 B0  01 02 01 10 0E 80 80 B0  ....G...........
01A0: 01 47 00 21 80 17 80 1F  80 19 80 47 01 01 B0 01  .G.!.......G....
01B0: 29 01 F0 FF FF 7F 03 20  00 21 00 9F 22 80 F0 FF  )...... .!.."...
01C0: FF 7F F0 FF FF 7F 6D 61  69 6E 00 80 1C 12 80 03  ......main......
01D0: 02 00 01 10 03 01 10 12  80 43 00 43 01 03 01 10  .........C.C....
01E0: 02 00 1C 23 80 45 24 80  F0 FF FF 7F F0 FF FF 7F  ...#.E$.........
01F0: 66 64 6F 31 00 80 1C 25  80 1B 45 24 80 F0 FF FF  fdo1...%..E$....
0200: 7F F0 FF FF 7F 66 64 69  31 00 80 9F 26 80 F0 FF  .....fdi1...&...
0210: FF 7F F0 FF FF 7F 6D 61  69 6E 00 80 1C 27 80 1B  ......main...'..
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[0] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[1] = 0*
  3: 0x000D [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  4: 0x0012 [0x08] ExtData[1]->WorkLocal[0] -= 11*
  5: 0x0017 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[0]
  6: 0x001C [0x0B] Work_Zone[4]++
  7: 0x001F [0x24] CREATE_DIALOG(message_id=7233*, default_option=ExtData[1]->WorkLocal[0], option_flags=ExtData[1]->WorkLocal[1])
    → "Destination? (Currently: [/N/W/E/C] Tower, Floor $2). [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Entrance./Never mind.]"
  8: 0x0026 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0027 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0037
 10: 0x002F [0x03] Work_Zone[1] = 11*
 11: 0x0034 [0x01] GOTO 0x00B7
 12: 0x0037 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0047
 13: 0x003F [0x03] Work_Zone[1] = 12*
 14: 0x0044 [0x01] GOTO 0x00B7
 15: 0x0047 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0057
 16: 0x004F [0x03] Work_Zone[1] = 13*
 17: 0x0054 [0x01] GOTO 0x00B7
 18: 0x0057 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0067
 19: 0x005F [0x03] Work_Zone[1] = 14*
 20: 0x0064 [0x01] GOTO 0x00B7
 21: 0x0067 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0077
 22: 0x006F [0x03] Work_Zone[1] = 15*
 23: 0x0074 [0x01] GOTO 0x00B7
 24: 0x0077 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0087
 25: 0x007F [0x03] Work_Zone[1] = 16*
 26: 0x0084 [0x01] GOTO 0x00B7
 27: 0x0087 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0097
 28: 0x008F [0x03] Work_Zone[1] = 17*
 29: 0x0094 [0x01] GOTO 0x00B7
 30: 0x0097 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00A7
 31: 0x009F [0x03] Work_Zone[1] = 1*
 32: 0x00A4 [0x01] GOTO 0x00B7
 33: 0x00A7 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x00B7
 34: 0x00AF [0x03] Work_Zone[1] = 0*
 35: 0x00B4 [0x01] GOTO 0x00B7

SUBROUTINE_00B7:
 36: 0x00B7 [0x02] IF !(Work_Zone[0] == ExtData[1]->WorkLocal[0]) GOTO 0x00C7
 37: 0x00BF [0x03] Work_Zone[1] = 255*
 38: 0x00C4 [0x01] GOTO 0x01B7
 39: 0x00C7 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x00D2
 40: 0x00CF [0x01] GOTO 0x01B7
 41: 0x00D2 [0x02] IF !(Work_Zone[1] == Work_Zone[3]) GOTO 0x00DD
 42: 0x00DA [0x01] GOTO 0x01B7
 43: 0x00DD [0x42] SET_CLI_EVENT_CANCEL_DATA()
 44: 0x00DE [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[1]
 45: 0x00E3 [0x03] Work_Zone[1] = 100*
 46: 0x00E8 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 47: 0x00EA [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 48: 0x00EC [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
 49: 0x00F1 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 50: 0x00F8 [0x02] IF !(Work_Zone[1] == 1*) GOTO 0x010F
 51: 0x0100 [0x47] UPDATE_PLAYER_POS(580.000*, 86.000*, 0.000*, yaw=90.0°*)
 52: 0x010A [0x47] WAIT_PLAYER_POS_UPDATE
 53: 0x010C [0x01] GOTO 0x01B0
 54: 0x010F [0x02] IF !(Work_Zone[1] == 11*) GOTO 0x0126
 55: 0x0117 [0x47] UPDATE_PLAYER_POS(380.000*, 376.000*, 71.620*, yaw=270.0°*)
 56: 0x0121 [0x47] WAIT_PLAYER_POS_UPDATE
 57: 0x0123 [0x01] GOTO 0x01B0
 58: 0x0126 [0x02] IF !(Work_Zone[1] == 12*) GOTO 0x013D
 59: 0x012E [0x47] UPDATE_PLAYER_POS(180.000*, 376.000*, -82.380*, yaw=270.0°*)
 60: 0x0138 [0x47] WAIT_PLAYER_POS_UPDATE
 61: 0x013A [0x01] GOTO 0x01B0
 62: 0x013D [0x02] IF !(Work_Zone[1] == 13*) GOTO 0x0154
 63: 0x0145 [0x47] UPDATE_PLAYER_POS(60.000*, 376.000*, 71.620*, yaw=270.0°*)
 64: 0x014F [0x47] WAIT_PLAYER_POS_UPDATE
 65: 0x0151 [0x01] GOTO 0x01B0
 66: 0x0154 [0x02] IF !(Work_Zone[1] == 14*) GOTO 0x016B
 67: 0x015C [0x47] UPDATE_PLAYER_POS(-140.000*, 376.000*, -82.380*, yaw=270.0°*)
 68: 0x0166 [0x47] WAIT_PLAYER_POS_UPDATE
 69: 0x0168 [0x01] GOTO 0x01B0
 70: 0x016B [0x02] IF !(Work_Zone[1] == 15*) GOTO 0x0182
 71: 0x0173 [0x47] UPDATE_PLAYER_POS(-260.000*, 376.000*, 77.620*, yaw=270.0°*)
 72: 0x017D [0x47] WAIT_PLAYER_POS_UPDATE
 73: 0x017F [0x01] GOTO 0x01B0
 74: 0x0182 [0x02] IF !(Work_Zone[1] == 16*) GOTO 0x0199
 75: 0x018A [0x47] UPDATE_PLAYER_POS(-460.000*, 376.000*, -82.380*, yaw=270.0°*)
 76: 0x0194 [0x47] WAIT_PLAYER_POS_UPDATE
 77: 0x0196 [0x01] GOTO 0x01B0
 78: 0x0199 [0x02] IF !(Work_Zone[1] == 17*) GOTO 0x01B0
 79: 0x01A1 [0x47] UPDATE_PLAYER_POS(-580.000*, 376.000*, 77.620*, yaw=270.0°*)
 80: 0x01AB [0x47] WAIT_PLAYER_POS_UPDATE
 81: 0x01AD [0x01] GOTO 0x01B0

SUBROUTINE_01B0:
 82: 0x01B0 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_01B7:
 83: 0x01B7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 84: 0x01B9 [0x21] END_EVENT
 85: 0x01BA [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x01BB [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[75*, 0*]
     0x01CC [0x1C] WAIT(100* ticks)
     0x01CF [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[1]
     0x01D4 [0x03] Work_Zone[1] = 100*
     0x01D9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x01DB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x01DD [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
     0x01E2 [0x1C] WAIT(40* ticks)
     0x01E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x01F6 [0x1C] WAIT(60* ticks)
     0x01F9 [0x1B] RETURN
     0x01FA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x020B [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[76*, 0*]
     0x021C [0x1C] WAIT(170* ticks)
     0x021F [0x1B] RETURN
```
