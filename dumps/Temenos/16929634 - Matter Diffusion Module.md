# 16929634 - Matter Diffusion Module

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 488 bytes        |
| Total Events     | 2                |
| References Count | 29               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1022](#event-1022)   | 0x0001       |    346 |             68 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0029      |          41 |
|       2 | 0x0004      |           4 |
|       3 | 0x0001      |           1 |
|       4 | 0x0005      |           5 |
|       5 | 0x0006      |           6 |
|       6 | 0x1C41      |        7233 |
|       7 | 0x002A      |          42 |
|       8 | 0x0002      |           2 |
|       9 | 0x002B      |          43 |
|      10 | 0x0003      |           3 |
|      11 | 0x002C      |          44 |
|      12 | 0x0007      |           7 |
|      13 | 0x0008      |           8 |
|      14 | 0x00FF      |         255 |
|      15 | 0x0064      |         100 |
|      16 | 0x8D9A0     |      580000 |
|      17 | 0x14FF0     |       86000 |
|      18 | 0x0400      |        1024 |
|      19 | 0xFFF7B300  |  4294423296 |
|      20 | 0xFFFFF6B4  |  4294964916 |
|      21 | 0x0C00      |        3072 |
|      22 | 0x3F7A0     |      260000 |
|      23 | 0xFFF84F40  |  4294463296 |
|      24 | 0xFFFD85B4  |  4294804916 |
|      25 | 0x4E20      |       20000 |
|      26 | 0xFFFB7BC0  |  4294671296 |
|      27 | 0xFFF85EE0  |  4294467296 |
|      28 | 0x0800      |        2048 |

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

### Event 1022

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 346 bytes |
| Instructions | 68        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 00 00 00 80  03 01 00 00 80 03 00 00    ..............
0010: 03 10 08 00 00 01 80 3C  01 00 02 80 03 80 3C 01  .......<......<.
0020: 00 04 80 03 80 3C 01 00  05 80 03 80 03 04 10 00  .....<..........
0030: 00 0B 04 10 24 06 80 00  00 01 00 25 02 00 10 00  ....$......%....
0040: 80 00 4C 00 03 01 10 01  80 01 9C 00 02 00 10 03  ..L.............
0050: 80 00 5C 00 03 01 10 07  80 01 9C 00 02 00 10 08  ..\.............
0060: 80 00 6C 00 03 01 10 09  80 01 9C 00 02 00 10 0A  ..l.............
0070: 80 00 7C 00 03 01 10 0B  80 01 9C 00 02 00 10 0C  ..|.............
0080: 80 00 8C 00 03 01 10 03  80 01 9C 00 02 00 10 0D  ................
0090: 80 00 9C 00 03 01 10 00  80 01 9C 00 02 00 10 00  ................
00A0: 00 00 AC 00 03 01 10 0E  80 01 57 01 02 01 10 00  ..........W.....
00B0: 80 00 B7 00 01 57 01 02  01 10 03 10 00 C2 00 01  .....W..........
00C0: 57 01 42 03 02 00 01 10  03 01 10 0F 80 43 00 43  W.B..........C.C
00D0: 01 03 01 10 02 00 29 01  F0 FF FF 7F 02 02 01 10  ......).........
00E0: 03 80 80 F4 00 47 00 10  80 11 80 00 80 12 80 47  .....G.........G
00F0: 01 01 50 01 02 01 10 01  80 80 0B 01 47 00 10 80  ..P.........G...
0100: 13 80 14 80 15 80 47 01  01 50 01 02 01 10 07 80  ......G..P......
0110: 80 22 01 47 00 16 80 17  80 18 80 15 80 47 01 01  .".G.........G..
0120: 50 01 02 01 10 09 80 80  39 01 47 00 19 80 13 80  P.......9.G.....
0130: 14 80 15 80 47 01 01 50  01 02 01 10 0B 80 80 50  ....G..P.......P
0140: 01 47 00 1A 80 1B 80 18  80 1C 80 47 01 01 50 01  .G.........G..P.
0150: 29 01 F0 FF FF 7F 03 20  00 21 00                 )...... .!.     
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
 10: 0x0034 [0x24] CREATE_DIALOG(message_id=7233*, default_option=ExtData[1]->WorkLocal[0], option_flags=ExtData[1]->WorkLocal[1])
    → "Destination? (Currently: [/N/W/E/C] Tower, Floor $2). [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Entrance./Never mind.]"
 11: 0x003B [0x25] WAIT_DIALOG_SELECT()
 12: 0x003C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004C
 13: 0x0044 [0x03] Work_Zone[1] = 41*
 14: 0x0049 [0x01] GOTO 0x009C
 15: 0x004C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x005C
 16: 0x0054 [0x03] Work_Zone[1] = 42*
 17: 0x0059 [0x01] GOTO 0x009C
 18: 0x005C [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x006C
 19: 0x0064 [0x03] Work_Zone[1] = 43*
 20: 0x0069 [0x01] GOTO 0x009C
 21: 0x006C [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x007C
 22: 0x0074 [0x03] Work_Zone[1] = 44*
 23: 0x0079 [0x01] GOTO 0x009C
 24: 0x007C [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x008C
 25: 0x0084 [0x03] Work_Zone[1] = 1*
 26: 0x0089 [0x01] GOTO 0x009C
 27: 0x008C [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x009C
 28: 0x0094 [0x03] Work_Zone[1] = 0*
 29: 0x0099 [0x01] GOTO 0x009C

SUBROUTINE_009C:
 30: 0x009C [0x02] IF !(Work_Zone[0] == ExtData[1]->WorkLocal[0]) GOTO 0x00AC
 31: 0x00A4 [0x03] Work_Zone[1] = 255*
 32: 0x00A9 [0x01] GOTO 0x0157
 33: 0x00AC [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x00B7
 34: 0x00B4 [0x01] GOTO 0x0157
 35: 0x00B7 [0x02] IF !(Work_Zone[1] == Work_Zone[3]) GOTO 0x00C2
 36: 0x00BF [0x01] GOTO 0x0157
 37: 0x00C2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 38: 0x00C3 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[1]
 39: 0x00C8 [0x03] Work_Zone[1] = 100*
 40: 0x00CD [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 41: 0x00CF [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 42: 0x00D1 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
 43: 0x00D6 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 44: 0x00DD [0x02] IF !(Work_Zone[1] == 1*) GOTO 0x00F4
 45: 0x00E5 [0x47] UPDATE_PLAYER_POS(580.000*, 86.000*, 0.000*, yaw=90.0°*)
 46: 0x00EF [0x47] WAIT_PLAYER_POS_UPDATE
 47: 0x00F1 [0x01] GOTO 0x0150
 48: 0x00F4 [0x02] IF !(Work_Zone[1] == 41*) GOTO 0x010B
 49: 0x00FC [0x47] UPDATE_PLAYER_POS(580.000*, -544.000*, -2.380*, yaw=270.0°*)
 50: 0x0106 [0x47] WAIT_PLAYER_POS_UPDATE
 51: 0x0108 [0x01] GOTO 0x0150
 52: 0x010B [0x02] IF !(Work_Zone[1] == 42*) GOTO 0x0122
 53: 0x0113 [0x47] UPDATE_PLAYER_POS(260.000*, -504.000*, -162.380*, yaw=270.0°*)
 54: 0x011D [0x47] WAIT_PLAYER_POS_UPDATE
 55: 0x011F [0x01] GOTO 0x0150
 56: 0x0122 [0x02] IF !(Work_Zone[1] == 43*) GOTO 0x0139
 57: 0x012A [0x47] UPDATE_PLAYER_POS(20.000*, -544.000*, -2.380*, yaw=270.0°*)
 58: 0x0134 [0x47] WAIT_PLAYER_POS_UPDATE
 59: 0x0136 [0x01] GOTO 0x0150
 60: 0x0139 [0x02] IF !(Work_Zone[1] == 44*) GOTO 0x0150
 61: 0x0141 [0x47] UPDATE_PLAYER_POS(-296.000*, -500.000*, -162.380*, yaw=180.0°*)
 62: 0x014B [0x47] WAIT_PLAYER_POS_UPDATE
 63: 0x014D [0x01] GOTO 0x0150

SUBROUTINE_0150:
 64: 0x0150 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_0157:
 65: 0x0157 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 66: 0x0159 [0x21] END_EVENT
 67: 0x015A [0x00] END_REQSTACK()
```
