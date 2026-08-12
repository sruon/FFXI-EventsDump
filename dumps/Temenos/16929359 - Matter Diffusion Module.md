# 16929359 - Matter Diffusion Module

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 452 bytes        |
| Total Events     | 2                |
| References Count | 28               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1024](#event-1024)   | 0x0001       |    314 |             62 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0029      |          41 |
|       2 | 0x0004      |           4 |
|       3 | 0x0001      |           1 |
|       4 | 0x0005      |           5 |
|       5 | 0x0006      |           6 |
|       6 | 0x0003      |           3 |
|       7 | 0x1C46      |        7238 |
|       8 | 0x002A      |          42 |
|       9 | 0x0002      |           2 |
|      10 | 0x002B      |          43 |
|      11 | 0x0007      |           7 |
|      12 | 0x0008      |           8 |
|      13 | 0x00FF      |         255 |
|      14 | 0x0064      |         100 |
|      15 | 0x8D9A0     |      580000 |
|      16 | 0x14FF0     |       86000 |
|      17 | 0x0400      |        1024 |
|      18 | 0x3F7A0     |      260000 |
|      19 | 0xFFF84F40  |  4294463296 |
|      20 | 0xFFFD85B4  |  4294804916 |
|      21 | 0x0C00      |        3072 |
|      22 | 0x4E20      |       20000 |
|      23 | 0xFFF7B300  |  4294423296 |
|      24 | 0xFFFFF6B4  |  4294964916 |
|      25 | 0xFFFB7BC0  |  4294671296 |
|      26 | 0xFFF85EE0  |  4294467296 |
|      27 | 0x0800      |        2048 |

## String References

- **7238**: Destination? (Currently: [/N/W/E/C] Tower, Floor $2). [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Entrance./Never mind.]

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

### Event 1024

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 314 bytes |
| Instructions | 62        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 00 00 00 80  03 01 00 00 80 03 00 00    ..............
0010: 03 10 08 00 00 01 80 3C  01 00 02 80 03 80 3C 01  .......<......<.
0020: 00 04 80 03 80 3C 01 00  05 80 03 80 03 04 10 00  .....<..........
0030: 00 0B 04 10 3C 01 00 06  80 03 80 24 07 80 00 00  ....<......$....
0040: 01 00 25 02 00 10 00 80  00 53 00 03 01 10 01 80  ..%......S......
0050: 01 93 00 02 00 10 03 80  00 63 00 03 01 10 08 80  .........c......
0060: 01 93 00 02 00 10 09 80  00 73 00 03 01 10 0A 80  .........s......
0070: 01 93 00 02 00 10 0B 80  00 83 00 03 01 10 03 80  ................
0080: 01 93 00 02 00 10 0C 80  00 93 00 03 01 10 00 80  ................
0090: 01 93 00 02 00 10 00 00  00 A3 00 03 01 10 0D 80  ................
00A0: 01 37 01 02 01 10 00 80  00 AE 00 01 37 01 02 01  .7..........7...
00B0: 10 03 10 00 B9 00 01 37  01 42 03 02 00 01 10 03  .......7.B......
00C0: 01 10 0E 80 43 00 43 01  03 01 10 02 00 29 01 F0  ....C.C......)..
00D0: FF FF 7F 02 02 01 10 03  80 80 EB 00 47 00 0F 80  ............G...
00E0: 10 80 00 80 11 80 47 01  01 30 01 02 01 10 01 80  ......G..0......
00F0: 80 02 01 47 00 12 80 13  80 14 80 15 80 47 01 01  ...G.........G..
0100: 30 01 02 01 10 08 80 80  19 01 47 00 16 80 17 80  0.........G.....
0110: 18 80 15 80 47 01 01 30  01 02 01 10 0A 80 80 30  ....G..0.......0
0120: 01 47 00 19 80 1A 80 14  80 1B 80 47 01 01 30 01  .G.........G..0.
0130: 29 01 F0 FF FF 7F 03 20  00 21 00                 )...... .!.     
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[0] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[1] = 0*
  3: 0x000D [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  4: 0x0012 [0x08] ExtData[1]->WorkLocal[0] -= 41*
  5: 0x0017 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=4*, condition_work_offset=1*)
  6: 0x001E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=5*, condition_work_offset=1*)
  7: 0x0025 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=6*, condition_work_offset=1*)
  8: 0x002C [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[0]
  9: 0x0031 [0x0B] Work_Zone[4]++
 10: 0x0034 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=3*, condition_work_offset=1*)
 11: 0x003B [0x24] CREATE_DIALOG(message_id=7238*, default_option=ExtData[1]->WorkLocal[0], option_flags=ExtData[1]->WorkLocal[1])
    → "Destination? (Currently: [/N/W/E/C] Tower, Floor $2). [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Entrance./Never mind.]"
 12: 0x0042 [0x25] WAIT_DIALOG_SELECT()
 13: 0x0043 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0053
 14: 0x004B [0x03] Work_Zone[1] = 41*
 15: 0x0050 [0x01] GOTO 0x0093
 16: 0x0053 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0063
 17: 0x005B [0x03] Work_Zone[1] = 42*
 18: 0x0060 [0x01] GOTO 0x0093
 19: 0x0063 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0073
 20: 0x006B [0x03] Work_Zone[1] = 43*
 21: 0x0070 [0x01] GOTO 0x0093
 22: 0x0073 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0083
 23: 0x007B [0x03] Work_Zone[1] = 1*
 24: 0x0080 [0x01] GOTO 0x0093
 25: 0x0083 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x0093
 26: 0x008B [0x03] Work_Zone[1] = 0*
 27: 0x0090 [0x01] GOTO 0x0093

SUBROUTINE_0093:
 28: 0x0093 [0x02] IF !(Work_Zone[0] == ExtData[1]->WorkLocal[0]) GOTO 0x00A3
 29: 0x009B [0x03] Work_Zone[1] = 255*
 30: 0x00A0 [0x01] GOTO 0x0137
 31: 0x00A3 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x00AE
 32: 0x00AB [0x01] GOTO 0x0137
 33: 0x00AE [0x02] IF !(Work_Zone[1] == Work_Zone[3]) GOTO 0x00B9
 34: 0x00B6 [0x01] GOTO 0x0137
 35: 0x00B9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 36: 0x00BA [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[1]
 37: 0x00BF [0x03] Work_Zone[1] = 100*
 38: 0x00C4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 39: 0x00C6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 40: 0x00C8 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
 41: 0x00CD [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 42: 0x00D4 [0x02] IF !(Work_Zone[1] == 1*) GOTO 0x00EB
 43: 0x00DC [0x47] UPDATE_PLAYER_POS(580.000*, 86.000*, 0.000*, yaw=90.0°*)
 44: 0x00E6 [0x47] WAIT_PLAYER_POS_UPDATE
 45: 0x00E8 [0x01] GOTO 0x0130
 46: 0x00EB [0x02] IF !(Work_Zone[1] == 41*) GOTO 0x0102
 47: 0x00F3 [0x47] UPDATE_PLAYER_POS(260.000*, -504.000*, -162.380*, yaw=270.0°*)
 48: 0x00FD [0x47] WAIT_PLAYER_POS_UPDATE
 49: 0x00FF [0x01] GOTO 0x0130
 50: 0x0102 [0x02] IF !(Work_Zone[1] == 42*) GOTO 0x0119
 51: 0x010A [0x47] UPDATE_PLAYER_POS(20.000*, -544.000*, -2.380*, yaw=270.0°*)
 52: 0x0114 [0x47] WAIT_PLAYER_POS_UPDATE
 53: 0x0116 [0x01] GOTO 0x0130
 54: 0x0119 [0x02] IF !(Work_Zone[1] == 43*) GOTO 0x0130
 55: 0x0121 [0x47] UPDATE_PLAYER_POS(-296.000*, -500.000*, -162.380*, yaw=180.0°*)
 56: 0x012B [0x47] WAIT_PLAYER_POS_UPDATE
 57: 0x012D [0x01] GOTO 0x0130

SUBROUTINE_0130:
 58: 0x0130 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_0137:
 59: 0x0137 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 60: 0x0139 [0x21] END_EVENT
 61: 0x013A [0x00] END_REQSTACK()
```
