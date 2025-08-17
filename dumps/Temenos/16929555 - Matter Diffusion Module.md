# 16929555 - Matter Diffusion Module

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 1408 bytes       |
| Total Events     | 2                |
| References Count | 69               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1000](#event-1000)   | 0x0001       |   1106 |            202 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0004      |           4 |
|       2 | 0x0001      |           1 |
|       3 | 0x1C3F      |        7231 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x0005      |           5 |
|       7 | 0x0006      |           6 |
|       8 | 0x0032      |          50 |
|       9 | 0x1C40      |        7232 |
|      10 | 0x000A      |          10 |
|      11 | 0x0007      |           7 |
|      12 | 0x0008      |           8 |
|      13 | 0x0064      |         100 |
|      14 | 0x000B      |          11 |
|      15 | 0x5CC60     |      380000 |
|      16 | 0x5BCC0     |      376000 |
|      17 | 0x117C4     |       71620 |
|      18 | 0x0C00      |        3072 |
|      19 | 0x000C      |          12 |
|      20 | 0x2BF20     |      180000 |
|      21 | 0xFFFEBE34  |  4294884916 |
|      22 | 0x000D      |          13 |
|      23 | 0xEA60      |       60000 |
|      24 | 0x000E      |          14 |
|      25 | 0xFFFDDD20  |  4294827296 |
|      26 | 0x000F      |          15 |
|      27 | 0xFFFC0860  |  4294707296 |
|      28 | 0x12F34     |       77620 |
|      29 | 0x0010      |          16 |
|      30 | 0xFFF8FB20  |  4294507296 |
|      31 | 0x0011      |          17 |
|      32 | 0xFFF72660  |  4294387296 |
|      33 | 0x0015      |          21 |
|      34 | 0x17700     |       96000 |
|      35 | 0xFFFFF6B4  |  4294964916 |
|      36 | 0x0016      |          22 |
|      37 | 0xFFFD85B4  |  4294804916 |
|      38 | 0x0017      |          23 |
|      39 | 0x0018      |          24 |
|      40 | 0x0019      |          25 |
|      41 | 0x001A      |          26 |
|      42 | 0x001B      |          27 |
|      43 | 0x001F      |          31 |
|      44 | 0xFFFD3140  |  4294783296 |
|      45 | 0x0020      |          32 |
|      46 | 0x0021      |          33 |
|      47 | 0x0022      |          34 |
|      48 | 0x0023      |          35 |
|      49 | 0x0024      |          36 |
|      50 | 0x0025      |          37 |
|      51 | 0x0029      |          41 |
|      52 | 0x8D9A0     |      580000 |
|      53 | 0xFFF7B300  |  4294423296 |
|      54 | 0x002A      |          42 |
|      55 | 0x3F7A0     |      260000 |
|      56 | 0xFFF84F40  |  4294463296 |
|      57 | 0x002B      |          43 |
|      58 | 0x4E20      |       20000 |
|      59 | 0x002C      |          44 |
|      60 | 0xFFFB7BC0  |  4294671296 |
|      61 | 0xFFF85EE0  |  4294467296 |
|      62 | 0x0800      |        2048 |
|      63 | 0x004B      |          75 |
|      64 | 0x00B4      |         180 |
|      65 | 0x00C8      |         200 |
|      66 | 0x003C      |          60 |
|      67 | 0x004C      |          76 |
|      68 | 0x00AA      |         170 |

## String References

- **7231**: Enter which tower? [Northern Tower./Western Tower./Eastern Tower./Central Tower./Central Tower - 1st Basement./Never mind.]
- **7232**: Enter which floor of the tower? [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Back./Never mind.]

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

### Event 1000

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 1106 bytes |
| Instructions | 182        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 02 00 00 80  03 00 00 00 80 03 01 00    ..............
0010: 00 80 3C 00 00 01 80 02  80 24 03 80 02 00 00 00  ..<......$......
0020: 25 02 00 10 00 80 00 31  00 03 02 10 02 80 01 96  %......1........
0030: 00 02 00 10 02 80 00 41  00 03 02 10 04 80 01 96  .......A........
0040: 00 02 00 10 04 80 00 51  00 03 02 10 05 80 01 96  .......Q........
0050: 00 02 00 10 05 80 00 76  00 03 02 10 01 80 3C 01  .......v......<.
0060: 00 01 80 02 80 3C 01 00  06 80 02 80 3C 01 00 07  .....<......<...
0070: 80 02 80 01 96 00 02 00  10 01 80 00 86 00 03 02  ................
0080: 10 08 80 01 96 00 02 00  10 06 80 00 96 00 03 02  ................
0090: 10 00 80 01 96 00 02 02  10 00 80 00 A1 00 01 E9  ................
00A0: 03 02 02 10 08 80 00 AC  00 01 6D 01 03 02 00 02  ..........m.....
00B0: 10 0C 02 00 24 09 80 00  80 01 00 25 02 00 10 00  ....$......%....
00C0: 80 00 D1 00 14 02 10 0A  80 07 02 10 02 80 01 6D  ...............m
00D0: 01 02 00 10 02 80 00 E6  00 14 02 10 0A 80 07 02  ................
00E0: 10 04 80 01 6D 01 02 00  10 04 80 00 FB 00 14 02  ....m...........
00F0: 10 0A 80 07 02 10 05 80  01 6D 01 02 00 10 05 80  .........m......
0100: 00 10 01 14 02 10 0A 80  07 02 10 01 80 01 6D 01  ..............m.
0110: 02 00 10 01 80 00 25 01  14 02 10 0A 80 07 02 10  ......%.........
0120: 06 80 01 6D 01 02 00 10  06 80 00 3A 01 14 02 10  ...m.......:....
0130: 0A 80 07 02 10 07 80 01  6D 01 02 00 10 07 80 00  ........m.......
0140: 4F 01 14 02 10 0A 80 07  02 10 0B 80 01 6D 01 02  O............m..
0150: 00 10 0B 80 00 5D 01 01  08 00 01 6D 01 02 00 10  .....].....m....
0160: 0C 80 00 6D 01 03 02 10  00 80 01 6D 01 02 02 10  ...m.......m....
0170: 00 80 00 78 01 01 E9 03  03 01 10 02 10 42 03 03  ...x.........B..
0180: 00 01 10 03 01 10 0D 80  43 00 43 01 03 01 10 03  ........C.C.....
0190: 00 29 01 F0 FF FF 7F 02  02 01 10 0E 80 80 AF 01  .)..............
01A0: 47 00 0F 80 10 80 11 80  12 80 47 01 01 E2 03 02  G.........G.....
01B0: 01 10 13 80 80 C6 01 47  00 14 80 10 80 15 80 12  .......G........
01C0: 80 47 01 01 E2 03 02 01  10 16 80 80 DD 01 47 00  .G............G.
01D0: 17 80 10 80 11 80 12 80  47 01 01 E2 03 02 01 10  ........G.......
01E0: 18 80 80 F4 01 47 00 19  80 10 80 15 80 12 80 47  .....G.........G
01F0: 01 01 E2 03 02 01 10 1A  80 80 0B 02 47 00 1B 80  ............G...
0200: 10 80 1C 80 12 80 47 01  01 E2 03 02 01 10 1D 80  ......G.........
0210: 80 22 02 47 00 1E 80 10  80 15 80 12 80 47 01 01  .".G.........G..
0220: E2 03 02 01 10 1F 80 80  39 02 47 00 20 80 10 80  ........9.G. ...
0230: 1C 80 12 80 47 01 01 E2  03 02 01 10 21 80 80 50  ....G.......!..P
0240: 02 47 00 0F 80 22 80 23  80 12 80 47 01 01 E2 03  .G...".#...G....
0250: 02 01 10 24 80 80 67 02  47 00 14 80 22 80 25 80  ...$..g.G...".%.
0260: 12 80 47 01 01 E2 03 02  01 10 26 80 80 7E 02 47  ..G.......&..~.G
0270: 00 17 80 22 80 23 80 12  80 47 01 01 E2 03 02 01  ...".#...G......
0280: 10 27 80 80 95 02 47 00  19 80 22 80 25 80 12 80  .'....G...".%...
0290: 47 01 01 E2 03 02 01 10  28 80 80 AC 02 47 00 1B  G.......(....G..
02A0: 80 22 80 23 80 12 80 47  01 01 E2 03 02 01 10 29  .".#...G.......)
02B0: 80 80 C3 02 47 00 1E 80  22 80 25 80 12 80 47 01  ....G...".%...G.
02C0: 01 E2 03 02 01 10 2A 80  80 DA 02 47 00 20 80 22  ......*....G. ."
02D0: 80 23 80 12 80 47 01 01  E2 03 02 01 10 2B 80 80  .#...G.......+..
02E0: F1 02 47 00 0F 80 2C 80  11 80 12 80 47 01 01 E2  ..G...,.....G...
02F0: 03 02 01 10 2D 80 80 08  03 47 00 14 80 2C 80 15  ....-....G...,..
0300: 80 12 80 47 01 01 E2 03  02 01 10 2E 80 80 1F 03  ...G............
0310: 47 00 17 80 2C 80 11 80  12 80 47 01 01 E2 03 02  G...,.....G.....
0320: 01 10 2F 80 80 36 03 47  00 19 80 2C 80 15 80 12  ../..6.G...,....
0330: 80 47 01 01 E2 03 02 01  10 30 80 80 4D 03 47 00  .G.......0..M.G.
0340: 1B 80 2C 80 1C 80 12 80  47 01 01 E2 03 02 01 10  ..,.....G.......
0350: 31 80 80 64 03 47 00 1E  80 2C 80 15 80 12 80 47  1..d.G...,.....G
0360: 01 01 E2 03 02 01 10 32  80 80 7B 03 47 00 20 80  .......2..{.G. .
0370: 2C 80 1C 80 12 80 47 01  01 E2 03 02 01 10 33 80  ,.....G.......3.
0380: 80 92 03 47 00 34 80 35  80 23 80 12 80 47 01 01  ...G.4.5.#...G..
0390: E2 03 02 01 10 36 80 80  A9 03 47 00 37 80 38 80  .....6....G.7.8.
03A0: 25 80 12 80 47 01 01 E2  03 02 01 10 39 80 80 C0  %...G.......9...
03B0: 03 47 00 3A 80 35 80 23  80 12 80 47 01 01 E2 03  .G.:.5.#...G....
03C0: 02 01 10 3B 80 80 D7 03  47 00 3C 80 3D 80 25 80  ...;....G.<.=.%.
03D0: 3E 80 47 01 01 E2 03 02  01 10 08 80 80 E2 03 01  >.G.............
03E0: E2 03 29 01 F0 FF FF 7F  03 20 00 21 00 9F 3F 80  ..)...... .!..?.
03F0: F0 FF FF 7F F0 FF FF 7F  6D 61 69 6E 00 80 03 03  ........main....
0400: 00 01 10 03 01 10 0D 80  43 00 43 01 03 01 10 03  ........C.C.....
0410: 00 1C 40 80 45 41 80 F0  FF FF 7F F0 FF FF 7F 66  ..@.EA.........f
0420: 64 6F 31 00 80 1C 42 80  46 01 1B 45 41 80 F0 FF  do1...B.F..EA...
0430: FF 7F F0 FF FF 7F 66 64  69 31 00 80 9F 43 80 F0  ......fdi1...C..
0440: FF FF 7F F0 FF FF 7F 6D  61 69 6E 00 80 1C 44 80  .......main...D.
0450: 46 00 1B                                          F..             
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[2] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[0] = 0*
  3: 0x000D [0x03] ExtData[1]->WorkLocal[1] = 0*
  4: 0x0012 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=4*, condition_work_offset=1*)
  5: 0x0019 [0x24] CREATE_DIALOG(message_id=7231*, default_option=ExtData[1]->WorkLocal[2], option_flags=ExtData[1]->WorkLocal[0])
    → "Enter which tower? [Northern Tower./Western Tower./Eastern Tower./Central Tower./Central Tower - 1st Basement./Never mind.]"
  6: 0x0020 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0021 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0031
  8: 0x0029 [0x03] Work_Zone[2] = 1*
  9: 0x002E [0x01] GOTO 0x0096
 10: 0x0031 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0041
 11: 0x0039 [0x03] Work_Zone[2] = 2*
 12: 0x003E [0x01] GOTO 0x0096
 13: 0x0041 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0051
 14: 0x0049 [0x03] Work_Zone[2] = 3*
 15: 0x004E [0x01] GOTO 0x0096
 16: 0x0051 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0076
 17: 0x0059 [0x03] Work_Zone[2] = 4*
 18: 0x005E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=4*, condition_work_offset=1*)
 19: 0x0065 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=5*, condition_work_offset=1*)
 20: 0x006C [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=6*, condition_work_offset=1*)
 21: 0x0073 [0x01] GOTO 0x0096
 22: 0x0076 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0086
 23: 0x007E [0x03] Work_Zone[2] = 50*
 24: 0x0083 [0x01] GOTO 0x0096
 25: 0x0086 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0096
 26: 0x008E [0x03] Work_Zone[2] = 0*
 27: 0x0093 [0x01] GOTO 0x0096

SUBROUTINE_0096:
 28: 0x0096 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00A1
 29: 0x009E [0x01] GOTO 0x03E9
 30: 0x00A1 [0x02] IF !(Work_Zone[2] == 50*) GOTO 0x00AC
 31: 0x00A9 [0x01] GOTO 0x016D
 32: 0x00AC [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[2]
 33: 0x00B1 [0x0C] ExtData[1]->WorkLocal[2]--
 34: 0x00B4 [0x24] CREATE_DIALOG(message_id=7232*, default_option=0*, option_flags=ExtData[1]->WorkLocal[1])
    → "Enter which floor of the tower? [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Back./Never mind.]"
 35: 0x00BB [0x25] WAIT_DIALOG_SELECT()
 36: 0x00BC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00D1
 37: 0x00C4 [0x14] Work_Zone[2] *= 10*
 38: 0x00C9 [0x07] Work_Zone[2] += 1*
 39: 0x00CE [0x01] GOTO 0x016D
 40: 0x00D1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00E6
 41: 0x00D9 [0x14] Work_Zone[2] *= 10*
 42: 0x00DE [0x07] Work_Zone[2] += 2*
 43: 0x00E3 [0x01] GOTO 0x016D
 44: 0x00E6 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00FB
 45: 0x00EE [0x14] Work_Zone[2] *= 10*
 46: 0x00F3 [0x07] Work_Zone[2] += 3*
 47: 0x00F8 [0x01] GOTO 0x016D
 48: 0x00FB [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0110
 49: 0x0103 [0x14] Work_Zone[2] *= 10*
 50: 0x0108 [0x07] Work_Zone[2] += 4*
 51: 0x010D [0x01] GOTO 0x016D
 52: 0x0110 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0125
 53: 0x0118 [0x14] Work_Zone[2] *= 10*
 54: 0x011D [0x07] Work_Zone[2] += 5*
 55: 0x0122 [0x01] GOTO 0x016D
 56: 0x0125 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x013A
 57: 0x012D [0x14] Work_Zone[2] *= 10*
 58: 0x0132 [0x07] Work_Zone[2] += 6*
 59: 0x0137 [0x01] GOTO 0x016D
 60: 0x013A [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x014F
 61: 0x0142 [0x14] Work_Zone[2] *= 10*
 62: 0x0147 [0x07] Work_Zone[2] += 7*
 63: 0x014C [0x01] GOTO 0x016D
 64: 0x014F [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x015D
 65: 0x0157 [0x01] GOTO 0x0008

SUBROUTINE_016D:
 66: 0x016D [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0178
 67: 0x0175 [0x01] GOTO 0x03E9
 68: 0x0178 [0x03] Work_Zone[1] = Work_Zone[2]
 69: 0x017D [0x42] SET_CLI_EVENT_CANCEL_DATA()
 70: 0x017E [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[1]
 71: 0x0183 [0x03] Work_Zone[1] = 100*
 72: 0x0188 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 73: 0x018A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 74: 0x018C [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[3]
 75: 0x0191 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 76: 0x0198 [0x02] IF !(Work_Zone[1] == 11*) GOTO 0x01AF
 77: 0x01A0 [0x47] UPDATE_PLAYER_POS(380.000*, 376.000*, 71.620*, yaw=270.0°*)
 78: 0x01AA [0x47] WAIT_PLAYER_POS_UPDATE
 79: 0x01AC [0x01] GOTO 0x03E2
 80: 0x01AF [0x02] IF !(Work_Zone[1] == 12*) GOTO 0x01C6
 81: 0x01B7 [0x47] UPDATE_PLAYER_POS(180.000*, 376.000*, -82.380*, yaw=270.0°*)
 82: 0x01C1 [0x47] WAIT_PLAYER_POS_UPDATE
 83: 0x01C3 [0x01] GOTO 0x03E2
 84: 0x01C6 [0x02] IF !(Work_Zone[1] == 13*) GOTO 0x01DD
 85: 0x01CE [0x47] UPDATE_PLAYER_POS(60.000*, 376.000*, 71.620*, yaw=270.0°*)
 86: 0x01D8 [0x47] WAIT_PLAYER_POS_UPDATE
 87: 0x01DA [0x01] GOTO 0x03E2
 88: 0x01DD [0x02] IF !(Work_Zone[1] == 14*) GOTO 0x01F4
 89: 0x01E5 [0x47] UPDATE_PLAYER_POS(-140.000*, 376.000*, -82.380*, yaw=270.0°*)
 90: 0x01EF [0x47] WAIT_PLAYER_POS_UPDATE
 91: 0x01F1 [0x01] GOTO 0x03E2
 92: 0x01F4 [0x02] IF !(Work_Zone[1] == 15*) GOTO 0x020B
 93: 0x01FC [0x47] UPDATE_PLAYER_POS(-260.000*, 376.000*, 77.620*, yaw=270.0°*)
 94: 0x0206 [0x47] WAIT_PLAYER_POS_UPDATE
 95: 0x0208 [0x01] GOTO 0x03E2
 96: 0x020B [0x02] IF !(Work_Zone[1] == 16*) GOTO 0x0222
 97: 0x0213 [0x47] UPDATE_PLAYER_POS(-460.000*, 376.000*, -82.380*, yaw=270.0°*)
 98: 0x021D [0x47] WAIT_PLAYER_POS_UPDATE
 99: 0x021F [0x01] GOTO 0x03E2
100: 0x0222 [0x02] IF !(Work_Zone[1] == 17*) GOTO 0x0239
101: 0x022A [0x47] UPDATE_PLAYER_POS(-580.000*, 376.000*, 77.620*, yaw=270.0°*)
102: 0x0234 [0x47] WAIT_PLAYER_POS_UPDATE
103: 0x0236 [0x01] GOTO 0x03E2
104: 0x0239 [0x02] IF !(Work_Zone[1] == 21*) GOTO 0x0250
105: 0x0241 [0x47] UPDATE_PLAYER_POS(380.000*, 96.000*, -2.380*, yaw=270.0°*)
106: 0x024B [0x47] WAIT_PLAYER_POS_UPDATE
107: 0x024D [0x01] GOTO 0x03E2
108: 0x0250 [0x02] IF !(Work_Zone[1] == 22*) GOTO 0x0267
109: 0x0258 [0x47] UPDATE_PLAYER_POS(180.000*, 96.000*, -162.380*, yaw=270.0°*)
110: 0x0262 [0x47] WAIT_PLAYER_POS_UPDATE
111: 0x0264 [0x01] GOTO 0x03E2
112: 0x0267 [0x02] IF !(Work_Zone[1] == 23*) GOTO 0x027E
113: 0x026F [0x47] UPDATE_PLAYER_POS(60.000*, 96.000*, -2.380*, yaw=270.0°*)
114: 0x0279 [0x47] WAIT_PLAYER_POS_UPDATE
115: 0x027B [0x01] GOTO 0x03E2
116: 0x027E [0x02] IF !(Work_Zone[1] == 24*) GOTO 0x0295
117: 0x0286 [0x47] UPDATE_PLAYER_POS(-140.000*, 96.000*, -162.380*, yaw=270.0°*)
118: 0x0290 [0x47] WAIT_PLAYER_POS_UPDATE
119: 0x0292 [0x01] GOTO 0x03E2
120: 0x0295 [0x02] IF !(Work_Zone[1] == 25*) GOTO 0x02AC
121: 0x029D [0x47] UPDATE_PLAYER_POS(-260.000*, 96.000*, -2.380*, yaw=270.0°*)
122: 0x02A7 [0x47] WAIT_PLAYER_POS_UPDATE
123: 0x02A9 [0x01] GOTO 0x03E2
124: 0x02AC [0x02] IF !(Work_Zone[1] == 26*) GOTO 0x02C3
125: 0x02B4 [0x47] UPDATE_PLAYER_POS(-460.000*, 96.000*, -162.380*, yaw=270.0°*)
126: 0x02BE [0x47] WAIT_PLAYER_POS_UPDATE
127: 0x02C0 [0x01] GOTO 0x03E2
128: 0x02C3 [0x02] IF !(Work_Zone[1] == 27*) GOTO 0x02DA
129: 0x02CB [0x47] UPDATE_PLAYER_POS(-580.000*, 96.000*, -2.380*, yaw=270.0°*)
130: 0x02D5 [0x47] WAIT_PLAYER_POS_UPDATE
131: 0x02D7 [0x01] GOTO 0x03E2
132: 0x02DA [0x02] IF !(Work_Zone[1] == 31*) GOTO 0x02F1
133: 0x02E2 [0x47] UPDATE_PLAYER_POS(380.000*, -184.000*, 71.620*, yaw=270.0°*)
134: 0x02EC [0x47] WAIT_PLAYER_POS_UPDATE
135: 0x02EE [0x01] GOTO 0x03E2
136: 0x02F1 [0x02] IF !(Work_Zone[1] == 32*) GOTO 0x0308
137: 0x02F9 [0x47] UPDATE_PLAYER_POS(180.000*, -184.000*, -82.380*, yaw=270.0°*)
138: 0x0303 [0x47] WAIT_PLAYER_POS_UPDATE
139: 0x0305 [0x01] GOTO 0x03E2
140: 0x0308 [0x02] IF !(Work_Zone[1] == 33*) GOTO 0x031F
141: 0x0310 [0x47] UPDATE_PLAYER_POS(60.000*, -184.000*, 71.620*, yaw=270.0°*)
142: 0x031A [0x47] WAIT_PLAYER_POS_UPDATE
143: 0x031C [0x01] GOTO 0x03E2
144: 0x031F [0x02] IF !(Work_Zone[1] == 34*) GOTO 0x0336
145: 0x0327 [0x47] UPDATE_PLAYER_POS(-140.000*, -184.000*, -82.380*, yaw=270.0°*)
146: 0x0331 [0x47] WAIT_PLAYER_POS_UPDATE
147: 0x0333 [0x01] GOTO 0x03E2
148: 0x0336 [0x02] IF !(Work_Zone[1] == 35*) GOTO 0x034D
149: 0x033E [0x47] UPDATE_PLAYER_POS(-260.000*, -184.000*, 77.620*, yaw=270.0°*)
150: 0x0348 [0x47] WAIT_PLAYER_POS_UPDATE
151: 0x034A [0x01] GOTO 0x03E2
152: 0x034D [0x02] IF !(Work_Zone[1] == 36*) GOTO 0x0364
153: 0x0355 [0x47] UPDATE_PLAYER_POS(-460.000*, -184.000*, -82.380*, yaw=270.0°*)
154: 0x035F [0x47] WAIT_PLAYER_POS_UPDATE
155: 0x0361 [0x01] GOTO 0x03E2
156: 0x0364 [0x02] IF !(Work_Zone[1] == 37*) GOTO 0x037B
157: 0x036C [0x47] UPDATE_PLAYER_POS(-580.000*, -184.000*, 77.620*, yaw=270.0°*)
158: 0x0376 [0x47] WAIT_PLAYER_POS_UPDATE
159: 0x0378 [0x01] GOTO 0x03E2
160: 0x037B [0x02] IF !(Work_Zone[1] == 41*) GOTO 0x0392
161: 0x0383 [0x47] UPDATE_PLAYER_POS(580.000*, -544.000*, -2.380*, yaw=270.0°*)
162: 0x038D [0x47] WAIT_PLAYER_POS_UPDATE
163: 0x038F [0x01] GOTO 0x03E2
164: 0x0392 [0x02] IF !(Work_Zone[1] == 42*) GOTO 0x03A9
165: 0x039A [0x47] UPDATE_PLAYER_POS(260.000*, -504.000*, -162.380*, yaw=270.0°*)
166: 0x03A4 [0x47] WAIT_PLAYER_POS_UPDATE
167: 0x03A6 [0x01] GOTO 0x03E2
168: 0x03A9 [0x02] IF !(Work_Zone[1] == 43*) GOTO 0x03C0
169: 0x03B1 [0x47] UPDATE_PLAYER_POS(20.000*, -544.000*, -2.380*, yaw=270.0°*)
170: 0x03BB [0x47] WAIT_PLAYER_POS_UPDATE
171: 0x03BD [0x01] GOTO 0x03E2
172: 0x03C0 [0x02] IF !(Work_Zone[1] == 44*) GOTO 0x03D7
173: 0x03C8 [0x47] UPDATE_PLAYER_POS(-296.000*, -500.000*, -162.380*, yaw=180.0°*)
174: 0x03D2 [0x47] WAIT_PLAYER_POS_UPDATE
175: 0x03D4 [0x01] GOTO 0x03E2
176: 0x03D7 [0x02] IF !(Work_Zone[1] == 50*) GOTO 0x03E2
177: 0x03DF [0x01] GOTO 0x03E2

SUBROUTINE_03E2:
178: 0x03E2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_03E9:
179: 0x03E9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
180: 0x03EB [0x21] END_EVENT
181: 0x03EC [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x015A [0x01] GOTO 0x016D
# Dead code (unreachable instructions):
     0x03ED [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[75*, 0*]
     0x03FE [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[1]
     0x0403 [0x03] Work_Zone[1] = 100*
     0x0408 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x040A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x040C [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[3]
     0x0411 [0x1C] WAIT(180* ticks)
     0x0414 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0425 [0x1C] WAIT(60* ticks)
     0x0428 [0x46] CAMERA_CONTROL: Disable user control
     0x042A [0x1B] RETURN
     0x042B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x043C [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[76*, 0*]
     0x044D [0x1C] WAIT(170* ticks)
     0x0450 [0x46] CAMERA_CONTROL: Restore default settings
     0x0452 [0x1B] RETURN
```
