# 16929569 - Matter Diffusion Module

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 1400 bytes       |
| Total Events     | 2                |
| References Count | 69               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1000](#event-1000)   | 0x0001       |   1099 |            201 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1C3F      |        7231 |
|       2 | 0x0001      |           1 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |
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
| Data Size    | 1099 bytes |
| Instructions | 181        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 02 00 00 80  03 00 00 02 10 03 01 00    ..............
0010: 00 80 24 01 80 02 00 00  00 25 02 00 10 00 80 00  ..$......%......
0020: 2A 00 03 02 10 02 80 01  8F 00 02 00 10 02 80 00  *...............
0030: 3A 00 03 02 10 03 80 01  8F 00 02 00 10 03 80 00  :...............
0040: 4A 00 03 02 10 04 80 01  8F 00 02 00 10 04 80 00  J...............
0050: 6F 00 03 02 10 05 80 3C  01 00 05 80 02 80 3C 01  o......<......<.
0060: 00 06 80 02 80 3C 01 00  07 80 02 80 01 8F 00 02  .....<..........
0070: 00 10 05 80 00 7F 00 03  02 10 08 80 01 8F 00 02  ................
0080: 00 10 06 80 00 8F 00 03  02 10 00 80 01 8F 00 02  ................
0090: 02 10 00 80 00 9A 00 01  E2 03 02 02 10 08 80 00  ................
00A0: A5 00 01 66 01 03 02 00  02 10 0C 02 00 24 09 80  ...f.........$..
00B0: 00 80 01 00 25 02 00 10  00 80 00 CA 00 14 02 10  ....%...........
00C0: 0A 80 07 02 10 02 80 01  66 01 02 00 10 02 80 00  ........f.......
00D0: DF 00 14 02 10 0A 80 07  02 10 03 80 01 66 01 02  .............f..
00E0: 00 10 03 80 00 F4 00 14  02 10 0A 80 07 02 10 04  ................
00F0: 80 01 66 01 02 00 10 04  80 00 09 01 14 02 10 0A  ..f.............
0100: 80 07 02 10 05 80 01 66  01 02 00 10 05 80 00 1E  .......f........
0110: 01 14 02 10 0A 80 07 02  10 06 80 01 66 01 02 00  ............f...
0120: 10 06 80 00 33 01 14 02  10 0A 80 07 02 10 07 80  ....3...........
0130: 01 66 01 02 00 10 07 80  00 48 01 14 02 10 0A 80  .f.......H......
0140: 07 02 10 0B 80 01 66 01  02 00 10 0B 80 00 56 01  ......f.......V.
0150: 01 0D 00 01 66 01 02 00  10 0C 80 00 66 01 03 02  ....f.......f...
0160: 10 00 80 01 66 01 02 02  10 00 80 00 71 01 01 E2  ....f.......q...
0170: 03 03 01 10 02 10 42 03  03 00 01 10 03 01 10 0D  ......B.........
0180: 80 43 00 43 01 03 01 10  03 00 29 01 F0 FF FF 7F  .C.C......).....
0190: 02 02 01 10 0E 80 80 A8  01 47 00 0F 80 10 80 11  .........G......
01A0: 80 12 80 47 01 01 DB 03  02 01 10 13 80 80 BF 01  ...G............
01B0: 47 00 14 80 10 80 15 80  12 80 47 01 01 DB 03 02  G.........G.....
01C0: 01 10 16 80 80 D6 01 47  00 17 80 10 80 11 80 12  .......G........
01D0: 80 47 01 01 DB 03 02 01  10 18 80 80 ED 01 47 00  .G............G.
01E0: 19 80 10 80 15 80 12 80  47 01 01 DB 03 02 01 10  ........G.......
01F0: 1A 80 80 04 02 47 00 1B  80 10 80 1C 80 12 80 47  .....G.........G
0200: 01 01 DB 03 02 01 10 1D  80 80 1B 02 47 00 1E 80  ............G...
0210: 10 80 15 80 12 80 47 01  01 DB 03 02 01 10 1F 80  ......G.........
0220: 80 32 02 47 00 20 80 10  80 1C 80 12 80 47 01 01  .2.G. .......G..
0230: DB 03 02 01 10 21 80 80  49 02 47 00 0F 80 22 80  .....!..I.G...".
0240: 23 80 12 80 47 01 01 DB  03 02 01 10 24 80 80 60  #...G.......$..`
0250: 02 47 00 14 80 22 80 25  80 12 80 47 01 01 DB 03  .G...".%...G....
0260: 02 01 10 26 80 80 77 02  47 00 17 80 22 80 23 80  ...&..w.G...".#.
0270: 12 80 47 01 01 DB 03 02  01 10 27 80 80 8E 02 47  ..G.......'....G
0280: 00 19 80 22 80 25 80 12  80 47 01 01 DB 03 02 01  ...".%...G......
0290: 10 28 80 80 A5 02 47 00  1B 80 22 80 23 80 12 80  .(....G...".#...
02A0: 47 01 01 DB 03 02 01 10  29 80 80 BC 02 47 00 1E  G.......)....G..
02B0: 80 22 80 25 80 12 80 47  01 01 DB 03 02 01 10 2A  .".%...G.......*
02C0: 80 80 D3 02 47 00 20 80  22 80 23 80 12 80 47 01  ....G. .".#...G.
02D0: 01 DB 03 02 01 10 2B 80  80 EA 02 47 00 0F 80 2C  ......+....G...,
02E0: 80 11 80 12 80 47 01 01  DB 03 02 01 10 2D 80 80  .....G.......-..
02F0: 01 03 47 00 14 80 2C 80  15 80 12 80 47 01 01 DB  ..G...,.....G...
0300: 03 02 01 10 2E 80 80 18  03 47 00 17 80 2C 80 11  .........G...,..
0310: 80 12 80 47 01 01 DB 03  02 01 10 2F 80 80 2F 03  ...G......./../.
0320: 47 00 19 80 2C 80 15 80  12 80 47 01 01 DB 03 02  G...,.....G.....
0330: 01 10 30 80 80 46 03 47  00 1B 80 2C 80 1C 80 12  ..0..F.G...,....
0340: 80 47 01 01 DB 03 02 01  10 31 80 80 5D 03 47 00  .G.......1..].G.
0350: 1E 80 2C 80 15 80 12 80  47 01 01 DB 03 02 01 10  ..,.....G.......
0360: 32 80 80 74 03 47 00 20  80 2C 80 1C 80 12 80 47  2..t.G. .,.....G
0370: 01 01 DB 03 02 01 10 33  80 80 8B 03 47 00 34 80  .......3....G.4.
0380: 35 80 23 80 12 80 47 01  01 DB 03 02 01 10 36 80  5.#...G.......6.
0390: 80 A2 03 47 00 37 80 38  80 25 80 12 80 47 01 01  ...G.7.8.%...G..
03A0: DB 03 02 01 10 39 80 80  B9 03 47 00 3A 80 35 80  .....9....G.:.5.
03B0: 23 80 12 80 47 01 01 DB  03 02 01 10 3B 80 80 D0  #...G.......;...
03C0: 03 47 00 3C 80 3D 80 25  80 3E 80 47 01 01 DB 03  .G.<.=.%.>.G....
03D0: 02 01 10 08 80 80 DB 03  01 DB 03 29 01 F0 FF FF  ...........)....
03E0: 7F 03 20 00 21 00 9F 3F  80 F0 FF FF 7F F0 FF FF  .. .!..?........
03F0: 7F 6D 61 69 6E 00 80 03  03 00 01 10 03 01 10 0D  .main...........
0400: 80 43 00 43 01 03 01 10  03 00 1C 40 80 45 41 80  .C.C.......@.EA.
0410: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 00 80 1C 42  ........fdo1...B
0420: 80 46 01 1B 45 41 80 F0  FF FF 7F F0 FF FF 7F 66  .F..EA.........f
0430: 64 69 31 00 80 9F 43 80  F0 FF FF 7F F0 FF FF 7F  di1...C.........
0440: 6D 61 69 6E 00 80 1C 44  80 46 00 1B              main...D.F..    
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[2] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x000D [0x03] ExtData[1]->WorkLocal[1] = 0*
  4: 0x0012 [0x24] CREATE_DIALOG(message_id=7231*, default_option=ExtData[1]->WorkLocal[2], option_flags=ExtData[1]->WorkLocal[0])
    → "Enter which tower? [Northern Tower./Western Tower./Eastern Tower./Central Tower./Central Tower - 1st Basement./Never mind.]"
  5: 0x0019 [0x25] WAIT_DIALOG_SELECT()
  6: 0x001A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002A
  7: 0x0022 [0x03] Work_Zone[2] = 1*
  8: 0x0027 [0x01] GOTO 0x008F
  9: 0x002A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x003A
 10: 0x0032 [0x03] Work_Zone[2] = 2*
 11: 0x0037 [0x01] GOTO 0x008F
 12: 0x003A [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x004A
 13: 0x0042 [0x03] Work_Zone[2] = 3*
 14: 0x0047 [0x01] GOTO 0x008F
 15: 0x004A [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x006F
 16: 0x0052 [0x03] Work_Zone[2] = 4*
 17: 0x0057 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=4*, condition_work_offset=1*)
 18: 0x005E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=5*, condition_work_offset=1*)
 19: 0x0065 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=6*, condition_work_offset=1*)
 20: 0x006C [0x01] GOTO 0x008F
 21: 0x006F [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x007F
 22: 0x0077 [0x03] Work_Zone[2] = 50*
 23: 0x007C [0x01] GOTO 0x008F
 24: 0x007F [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x008F
 25: 0x0087 [0x03] Work_Zone[2] = 0*
 26: 0x008C [0x01] GOTO 0x008F

SUBROUTINE_008F:
 27: 0x008F [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x009A
 28: 0x0097 [0x01] GOTO 0x03E2
 29: 0x009A [0x02] IF !(Work_Zone[2] == 50*) GOTO 0x00A5
 30: 0x00A2 [0x01] GOTO 0x0166
 31: 0x00A5 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[2]
 32: 0x00AA [0x0C] ExtData[1]->WorkLocal[2]--
 33: 0x00AD [0x24] CREATE_DIALOG(message_id=7232*, default_option=0*, option_flags=ExtData[1]->WorkLocal[1])
    → "Enter which floor of the tower? [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Back./Never mind.]"
 34: 0x00B4 [0x25] WAIT_DIALOG_SELECT()
 35: 0x00B5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CA
 36: 0x00BD [0x14] Work_Zone[2] *= 10*
 37: 0x00C2 [0x07] Work_Zone[2] += 1*
 38: 0x00C7 [0x01] GOTO 0x0166
 39: 0x00CA [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00DF
 40: 0x00D2 [0x14] Work_Zone[2] *= 10*
 41: 0x00D7 [0x07] Work_Zone[2] += 2*
 42: 0x00DC [0x01] GOTO 0x0166
 43: 0x00DF [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00F4
 44: 0x00E7 [0x14] Work_Zone[2] *= 10*
 45: 0x00EC [0x07] Work_Zone[2] += 3*
 46: 0x00F1 [0x01] GOTO 0x0166
 47: 0x00F4 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0109
 48: 0x00FC [0x14] Work_Zone[2] *= 10*
 49: 0x0101 [0x07] Work_Zone[2] += 4*
 50: 0x0106 [0x01] GOTO 0x0166
 51: 0x0109 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x011E
 52: 0x0111 [0x14] Work_Zone[2] *= 10*
 53: 0x0116 [0x07] Work_Zone[2] += 5*
 54: 0x011B [0x01] GOTO 0x0166
 55: 0x011E [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0133
 56: 0x0126 [0x14] Work_Zone[2] *= 10*
 57: 0x012B [0x07] Work_Zone[2] += 6*
 58: 0x0130 [0x01] GOTO 0x0166
 59: 0x0133 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0148
 60: 0x013B [0x14] Work_Zone[2] *= 10*
 61: 0x0140 [0x07] Work_Zone[2] += 7*
 62: 0x0145 [0x01] GOTO 0x0166
 63: 0x0148 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0156
 64: 0x0150 [0x01] GOTO 0x000D

SUBROUTINE_0166:
 65: 0x0166 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0171
 66: 0x016E [0x01] GOTO 0x03E2
 67: 0x0171 [0x03] Work_Zone[1] = Work_Zone[2]
 68: 0x0176 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 69: 0x0177 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[1]
 70: 0x017C [0x03] Work_Zone[1] = 100*
 71: 0x0181 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 72: 0x0183 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 73: 0x0185 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[3]
 74: 0x018A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 75: 0x0191 [0x02] IF !(Work_Zone[1] == 11*) GOTO 0x01A8
 76: 0x0199 [0x47] UPDATE_PLAYER_POS(380.000*, 376.000*, 71.620*, yaw=270.0°*)
 77: 0x01A3 [0x47] WAIT_PLAYER_POS_UPDATE
 78: 0x01A5 [0x01] GOTO 0x03DB
 79: 0x01A8 [0x02] IF !(Work_Zone[1] == 12*) GOTO 0x01BF
 80: 0x01B0 [0x47] UPDATE_PLAYER_POS(180.000*, 376.000*, -82.380*, yaw=270.0°*)
 81: 0x01BA [0x47] WAIT_PLAYER_POS_UPDATE
 82: 0x01BC [0x01] GOTO 0x03DB
 83: 0x01BF [0x02] IF !(Work_Zone[1] == 13*) GOTO 0x01D6
 84: 0x01C7 [0x47] UPDATE_PLAYER_POS(60.000*, 376.000*, 71.620*, yaw=270.0°*)
 85: 0x01D1 [0x47] WAIT_PLAYER_POS_UPDATE
 86: 0x01D3 [0x01] GOTO 0x03DB
 87: 0x01D6 [0x02] IF !(Work_Zone[1] == 14*) GOTO 0x01ED
 88: 0x01DE [0x47] UPDATE_PLAYER_POS(-140.000*, 376.000*, -82.380*, yaw=270.0°*)
 89: 0x01E8 [0x47] WAIT_PLAYER_POS_UPDATE
 90: 0x01EA [0x01] GOTO 0x03DB
 91: 0x01ED [0x02] IF !(Work_Zone[1] == 15*) GOTO 0x0204
 92: 0x01F5 [0x47] UPDATE_PLAYER_POS(-260.000*, 376.000*, 77.620*, yaw=270.0°*)
 93: 0x01FF [0x47] WAIT_PLAYER_POS_UPDATE
 94: 0x0201 [0x01] GOTO 0x03DB
 95: 0x0204 [0x02] IF !(Work_Zone[1] == 16*) GOTO 0x021B
 96: 0x020C [0x47] UPDATE_PLAYER_POS(-460.000*, 376.000*, -82.380*, yaw=270.0°*)
 97: 0x0216 [0x47] WAIT_PLAYER_POS_UPDATE
 98: 0x0218 [0x01] GOTO 0x03DB
 99: 0x021B [0x02] IF !(Work_Zone[1] == 17*) GOTO 0x0232
100: 0x0223 [0x47] UPDATE_PLAYER_POS(-580.000*, 376.000*, 77.620*, yaw=270.0°*)
101: 0x022D [0x47] WAIT_PLAYER_POS_UPDATE
102: 0x022F [0x01] GOTO 0x03DB
103: 0x0232 [0x02] IF !(Work_Zone[1] == 21*) GOTO 0x0249
104: 0x023A [0x47] UPDATE_PLAYER_POS(380.000*, 96.000*, -2.380*, yaw=270.0°*)
105: 0x0244 [0x47] WAIT_PLAYER_POS_UPDATE
106: 0x0246 [0x01] GOTO 0x03DB
107: 0x0249 [0x02] IF !(Work_Zone[1] == 22*) GOTO 0x0260
108: 0x0251 [0x47] UPDATE_PLAYER_POS(180.000*, 96.000*, -162.380*, yaw=270.0°*)
109: 0x025B [0x47] WAIT_PLAYER_POS_UPDATE
110: 0x025D [0x01] GOTO 0x03DB
111: 0x0260 [0x02] IF !(Work_Zone[1] == 23*) GOTO 0x0277
112: 0x0268 [0x47] UPDATE_PLAYER_POS(60.000*, 96.000*, -2.380*, yaw=270.0°*)
113: 0x0272 [0x47] WAIT_PLAYER_POS_UPDATE
114: 0x0274 [0x01] GOTO 0x03DB
115: 0x0277 [0x02] IF !(Work_Zone[1] == 24*) GOTO 0x028E
116: 0x027F [0x47] UPDATE_PLAYER_POS(-140.000*, 96.000*, -162.380*, yaw=270.0°*)
117: 0x0289 [0x47] WAIT_PLAYER_POS_UPDATE
118: 0x028B [0x01] GOTO 0x03DB
119: 0x028E [0x02] IF !(Work_Zone[1] == 25*) GOTO 0x02A5
120: 0x0296 [0x47] UPDATE_PLAYER_POS(-260.000*, 96.000*, -2.380*, yaw=270.0°*)
121: 0x02A0 [0x47] WAIT_PLAYER_POS_UPDATE
122: 0x02A2 [0x01] GOTO 0x03DB
123: 0x02A5 [0x02] IF !(Work_Zone[1] == 26*) GOTO 0x02BC
124: 0x02AD [0x47] UPDATE_PLAYER_POS(-460.000*, 96.000*, -162.380*, yaw=270.0°*)
125: 0x02B7 [0x47] WAIT_PLAYER_POS_UPDATE
126: 0x02B9 [0x01] GOTO 0x03DB
127: 0x02BC [0x02] IF !(Work_Zone[1] == 27*) GOTO 0x02D3
128: 0x02C4 [0x47] UPDATE_PLAYER_POS(-580.000*, 96.000*, -2.380*, yaw=270.0°*)
129: 0x02CE [0x47] WAIT_PLAYER_POS_UPDATE
130: 0x02D0 [0x01] GOTO 0x03DB
131: 0x02D3 [0x02] IF !(Work_Zone[1] == 31*) GOTO 0x02EA
132: 0x02DB [0x47] UPDATE_PLAYER_POS(380.000*, -184.000*, 71.620*, yaw=270.0°*)
133: 0x02E5 [0x47] WAIT_PLAYER_POS_UPDATE
134: 0x02E7 [0x01] GOTO 0x03DB
135: 0x02EA [0x02] IF !(Work_Zone[1] == 32*) GOTO 0x0301
136: 0x02F2 [0x47] UPDATE_PLAYER_POS(180.000*, -184.000*, -82.380*, yaw=270.0°*)
137: 0x02FC [0x47] WAIT_PLAYER_POS_UPDATE
138: 0x02FE [0x01] GOTO 0x03DB
139: 0x0301 [0x02] IF !(Work_Zone[1] == 33*) GOTO 0x0318
140: 0x0309 [0x47] UPDATE_PLAYER_POS(60.000*, -184.000*, 71.620*, yaw=270.0°*)
141: 0x0313 [0x47] WAIT_PLAYER_POS_UPDATE
142: 0x0315 [0x01] GOTO 0x03DB
143: 0x0318 [0x02] IF !(Work_Zone[1] == 34*) GOTO 0x032F
144: 0x0320 [0x47] UPDATE_PLAYER_POS(-140.000*, -184.000*, -82.380*, yaw=270.0°*)
145: 0x032A [0x47] WAIT_PLAYER_POS_UPDATE
146: 0x032C [0x01] GOTO 0x03DB
147: 0x032F [0x02] IF !(Work_Zone[1] == 35*) GOTO 0x0346
148: 0x0337 [0x47] UPDATE_PLAYER_POS(-260.000*, -184.000*, 77.620*, yaw=270.0°*)
149: 0x0341 [0x47] WAIT_PLAYER_POS_UPDATE
150: 0x0343 [0x01] GOTO 0x03DB
151: 0x0346 [0x02] IF !(Work_Zone[1] == 36*) GOTO 0x035D
152: 0x034E [0x47] UPDATE_PLAYER_POS(-460.000*, -184.000*, -82.380*, yaw=270.0°*)
153: 0x0358 [0x47] WAIT_PLAYER_POS_UPDATE
154: 0x035A [0x01] GOTO 0x03DB
155: 0x035D [0x02] IF !(Work_Zone[1] == 37*) GOTO 0x0374
156: 0x0365 [0x47] UPDATE_PLAYER_POS(-580.000*, -184.000*, 77.620*, yaw=270.0°*)
157: 0x036F [0x47] WAIT_PLAYER_POS_UPDATE
158: 0x0371 [0x01] GOTO 0x03DB
159: 0x0374 [0x02] IF !(Work_Zone[1] == 41*) GOTO 0x038B
160: 0x037C [0x47] UPDATE_PLAYER_POS(580.000*, -544.000*, -2.380*, yaw=270.0°*)
161: 0x0386 [0x47] WAIT_PLAYER_POS_UPDATE
162: 0x0388 [0x01] GOTO 0x03DB
163: 0x038B [0x02] IF !(Work_Zone[1] == 42*) GOTO 0x03A2
164: 0x0393 [0x47] UPDATE_PLAYER_POS(260.000*, -504.000*, -162.380*, yaw=270.0°*)
165: 0x039D [0x47] WAIT_PLAYER_POS_UPDATE
166: 0x039F [0x01] GOTO 0x03DB
167: 0x03A2 [0x02] IF !(Work_Zone[1] == 43*) GOTO 0x03B9
168: 0x03AA [0x47] UPDATE_PLAYER_POS(20.000*, -544.000*, -2.380*, yaw=270.0°*)
169: 0x03B4 [0x47] WAIT_PLAYER_POS_UPDATE
170: 0x03B6 [0x01] GOTO 0x03DB
171: 0x03B9 [0x02] IF !(Work_Zone[1] == 44*) GOTO 0x03D0
172: 0x03C1 [0x47] UPDATE_PLAYER_POS(-296.000*, -500.000*, -162.380*, yaw=180.0°*)
173: 0x03CB [0x47] WAIT_PLAYER_POS_UPDATE
174: 0x03CD [0x01] GOTO 0x03DB
175: 0x03D0 [0x02] IF !(Work_Zone[1] == 50*) GOTO 0x03DB
176: 0x03D8 [0x01] GOTO 0x03DB

SUBROUTINE_03DB:
177: 0x03DB [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_03E2:
178: 0x03E2 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
179: 0x03E4 [0x21] END_EVENT
180: 0x03E5 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0153 [0x01] GOTO 0x0166
# Dead code (unreachable instructions):
     0x03E6 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[75*, 0*]
     0x03F7 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[1]
     0x03FC [0x03] Work_Zone[1] = 100*
     0x0401 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0403 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0405 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[3]
     0x040A [0x1C] WAIT(180* ticks)
     0x040D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x041E [0x1C] WAIT(60* ticks)
     0x0421 [0x46] CAMERA_CONTROL: Disable user control
     0x0423 [0x1B] RETURN
     0x0424 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0435 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[76*, 0*]
     0x0446 [0x1C] WAIT(170* ticks)
     0x0449 [0x46] CAMERA_CONTROL: Restore default settings
     0x044B [0x1B] RETURN
```
