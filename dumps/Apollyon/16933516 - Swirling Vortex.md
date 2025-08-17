# 16933516 - Swirling Vortex

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 1376 bytes        |
| Total Events     | 2                 |
| References Count | 76                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [103](#event-103)     | 0x0001       |   1046 |            190 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0006      |           6 |
|       2 | 0x0001      |           1 |
|       3 | 0x0004      |           4 |
|       4 | 0x0005      |           5 |
|       5 | 0x1C47      |        7239 |
|       6 | 0x000A      |          10 |
|       7 | 0x0014      |          20 |
|       8 | 0x0002      |           2 |
|       9 | 0x001E      |          30 |
|      10 | 0x0003      |           3 |
|      11 | 0x0028      |          40 |
|      12 | 0x0033      |          51 |
|      13 | 0x0034      |          52 |
|      14 | 0x0007      |           7 |
|      15 | 0x0008      |           8 |
|      16 | 0x1C48      |        7240 |
|      17 | 0x0064      |         100 |
|      18 | 0xFFF6B900  |  4294359296 |
|      19 | 0xFFF6D840  |  4294367296 |
|      20 | 0x07E8      |        2024 |
|      21 | 0x94700     |      608000 |
|      22 | 0x000B      |          11 |
|      23 | 0xFFF94940  |  4294527296 |
|      24 | 0xFFFEA840  |  4294879296 |
|      25 | 0x0C00      |        3072 |
|      26 | 0x000C      |          12 |
|      27 | 0xFFF7DA10  |  4294433296 |
|      28 | 0x29BF8     |      171000 |
|      29 | 0x0A00      |        2560 |
|      30 | 0x000D      |          13 |
|      31 | 0xFFFB8390  |  4294673296 |
|      32 | 0x000E      |          14 |
|      33 | 0xFFF66AE0  |  4294339296 |
|      34 | 0x79568     |      497000 |
|      35 | 0x0E00      |        3584 |
|      36 | 0x000F      |          15 |
|      37 | 0xFFFA1460  |  4294579296 |
|      38 | 0x79950     |      498000 |
|      39 | 0x0015      |          21 |
|      40 | 0xFFF8DBE0  |  4294499296 |
|      41 | 0xFFF67698  |  4294342296 |
|      42 | 0x0016      |          22 |
|      43 | 0xFFF73600  |  4294391296 |
|      44 | 0xFFF97820  |  4294539296 |
|      45 | 0x0017      |          23 |
|      46 | 0xFFFA2018  |  4294582296 |
|      47 | 0x0018      |          24 |
|      48 | 0xFFFD5080  |  4294791296 |
|      49 | 0x001F      |          31 |
|      50 | 0x6B6C0     |      440000 |
|      51 | 0x0020      |          32 |
|      52 | 0x825F0     |      534000 |
|      53 | 0x0021      |          33 |
|      54 | 0x47C70     |      294000 |
|      55 | 0x0022      |          34 |
|      56 | 0x99520     |      628000 |
|      57 | 0x0023      |          35 |
|      58 | 0x5EBA0     |      388000 |
|      59 | 0x0029      |          41 |
|      60 | 0x72420     |      468000 |
|      61 | 0x002A      |          42 |
|      62 | 0x8CA00     |      576000 |
|      63 | 0x002B      |          43 |
|      64 | 0x687E0     |      428000 |
|      65 | 0x002C      |          44 |
|      66 | 0x2AF80     |      176000 |
|      67 | 0x30D40     |      200000 |
|      68 | 0x0400      |        1024 |
|      69 | 0xFFFCF2C0  |  4294767296 |
|      70 | 0x0049      |          73 |
|      71 | 0x008C      |         140 |
|      72 | 0x00C8      |         200 |
|      73 | 0x003C      |          60 |
|      74 | 0x004A      |          74 |
|      75 | 0x00AA      |         170 |

## String References

- **7239**: Select a destination. [NW./SW./NE./SE./CN./CS./Entrance #1./Entrance #2./Never mind.]
- **7240**: Select a destination. [[/NW/SW/NE/SE] #1./[/NW/SW/NE/SE] #2./[/NW/SW/NE/SE] #3./[/NW/SW/NE/SE] #4./[/NW//NE] #5./Back./Never mind.]

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

### Event 103

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 1046 bytes |
| Instructions | 170        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 00 00 00 80  03 02 00 00 80 03 00 00    ..............
0010: 03 10 07 00 00 01 80 3C  02 00 00 00 02 80 3C 02  .......<......<.
0020: 00 03 80 02 80 3C 02 00  04 80 02 80 03 01 00 00  .....<..........
0030: 80 24 05 80 00 80 02 00  25 02 00 10 00 80 00 4E  .$......%......N
0040: 00 03 01 00 06 80 03 02  10 02 80 01 DD 00 02 00  ................
0050: 10 02 80 00 63 00 03 01  00 07 80 03 02 10 08 80  ....c...........
0060: 01 DD 00 02 00 10 08 80  00 78 00 03 01 00 09 80  .........x......
0070: 03 02 10 0A 80 01 DD 00  02 00 10 0A 80 00 8D 00  ................
0080: 03 01 00 0B 80 03 02 10  03 80 01 DD 00 02 00 10  ................
0090: 03 80 00 9D 00 03 01 10  0C 80 01 DD 00 02 00 10  ................
00A0: 04 80 00 AD 00 03 01 10  0D 80 01 DD 00 02 00 10  ................
00B0: 01 80 00 BD 00 03 01 10  02 80 01 DD 00 02 00 10  ................
00C0: 0E 80 00 CD 00 03 01 10  08 80 01 DD 00 02 00 10  ................
00D0: 0F 80 00 DD 00 03 01 10  00 80 01 DD 00 02 01 00  ................
00E0: 00 80 00 E8 00 01 86 01  03 03 00 00 80 02 01 00  ................
00F0: 07 80 00 FC 00 3C 03 00  03 80 02 80 02 01 00 0B  .....<..........
0100: 80 00 0B 01 3C 03 00 03  80 02 80 03 01 10 01 00  ....<...........
0110: 24 10 80 00 80 03 00 25  02 00 10 00 80 00 28 01  $......%......(.
0120: 07 01 10 02 80 01 86 01  02 00 10 02 80 00 38 01  ..............8.
0130: 07 01 10 08 80 01 86 01  02 00 10 08 80 00 48 01  ..............H.
0140: 07 01 10 0A 80 01 86 01  02 00 10 0A 80 00 58 01  ..............X.
0150: 07 01 10 03 80 01 86 01  02 00 10 03 80 00 68 01  ..............h.
0160: 07 01 10 04 80 01 86 01  02 00 10 04 80 00 76 01  ..............v.
0170: 01 2C 00 01 86 01 02 00  10 01 80 00 86 01 03 01  .,..............
0180: 10 00 80 01 86 01 02 01  10 00 80 00 91 01 01 AD  ................
0190: 03 42 03 04 00 01 10 03  01 10 11 80 43 00 43 01  .B..........C.C.
01A0: 03 01 10 04 00 29 01 F0  FF FF 7F 02 02 01 10 02  .....)..........
01B0: 80 80 C3 01 47 00 12 80  13 80 00 80 14 80 47 01  ....G.........G.
01C0: 01 A6 03 02 01 10 08 80  80 DA 01 47 00 15 80 13  ...........G....
01D0: 80 00 80 00 80 47 01 01  A6 03 02 01 10 16 80 80  .....G..........
01E0: F1 01 47 00 17 80 18 80  00 80 19 80 47 01 01 A6  ..G.........G...
01F0: 03 02 01 10 1A 80 80 08  02 47 00 1B 80 1C 80 00  .........G......
0200: 80 1D 80 47 01 01 A6 03  02 01 10 1E 80 80 1F 02  ...G............
0210: 47 00 1F 80 1C 80 00 80  1D 80 47 01 01 A6 03 02  G.........G.....
0220: 01 10 20 80 80 36 02 47  00 21 80 22 80 00 80 23  .. ..6.G.!."...#
0230: 80 47 01 01 A6 03 02 01  10 24 80 80 4D 02 47 00  .G.......$..M.G.
0240: 25 80 26 80 00 80 23 80  47 01 01 A6 03 02 01 10  %.&...#.G.......
0250: 27 80 80 64 02 47 00 28  80 29 80 00 80 23 80 47  '..d.G.(.)...#.G
0260: 01 01 A6 03 02 01 10 2A  80 80 7B 02 47 00 2B 80  .......*..{.G.+.
0270: 2C 80 00 80 1D 80 47 01  01 A6 03 02 01 10 2D 80  ,.....G.......-.
0280: 80 92 02 47 00 2C 80 2E  80 00 80 23 80 47 01 01  ...G.,.....#.G..
0290: A6 03 02 01 10 2F 80 80  A9 02 47 00 30 80 21 80  ...../....G.0.!.
02A0: 00 80 1D 80 47 01 01 A6  03 02 01 10 31 80 80 C0  ....G.......1...
02B0: 02 47 00 32 80 18 80 00  80 19 80 47 01 01 A6 03  .G.2.......G....
02C0: 02 01 10 33 80 80 D7 02  47 00 34 80 1C 80 00 80  ...3....G.4.....
02D0: 23 80 47 01 01 A6 03 02  01 10 35 80 80 EE 02 47  #.G.......5....G
02E0: 00 36 80 1C 80 00 80 23  80 47 01 01 A6 03 02 01  .6.....#.G......
02F0: 10 37 80 80 05 03 47 00  38 80 22 80 00 80 1D 80  .7....G.8.".....
0300: 47 01 01 A6 03 02 01 10  39 80 80 1C 03 47 00 3A  G.......9....G.:
0310: 80 26 80 00 80 1D 80 47  01 01 A6 03 02 01 10 3B  .&.....G.......;
0320: 80 80 33 03 47 00 3C 80  29 80 00 80 1D 80 47 01  ..3.G.<.).....G.
0330: 01 A6 03 02 01 10 3D 80  80 4A 03 47 00 3E 80 2C  ......=..J.G.>.,
0340: 80 00 80 23 80 47 01 01  A6 03 02 01 10 3F 80 80  ...#.G.......?..
0350: 61 03 47 00 40 80 2E 80  00 80 1D 80 47 01 01 A6  a.G.@.......G...
0360: 03 02 01 10 41 80 80 78  03 47 00 42 80 21 80 00  ....A..x.G.B.!..
0370: 80 23 80 47 01 01 A6 03  02 01 10 0C 80 80 8F 03  .#.G............
0380: 47 00 00 80 43 80 00 80  44 80 47 01 01 A6 03 02  G...C...D.G.....
0390: 01 10 0D 80 80 A6 03 47  00 00 80 45 80 00 80 19  .......G...E....
03A0: 80 47 01 01 A6 03 29 01  F0 FF FF 7F 03 20 00 21  .G....)...... .!
03B0: 00 9F 46 80 F0 FF FF 7F  F0 FF FF 7F 6D 61 69 6E  ..F.........main
03C0: 00 80 03 04 00 01 10 03  01 10 11 80 43 00 43 01  ............C.C.
03D0: 03 01 10 04 00 1C 47 80  45 48 80 F0 FF FF 7F F0  ......G.EH......
03E0: FF FF 7F 66 64 6F 31 00  80 1C 49 80 46 01 1B 45  ...fdo1...I.F..E
03F0: 48 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 00 80  H.........fdi1..
0400: 9F 4A 80 F0 FF FF 7F F0  FF FF 7F 6D 61 69 6E 00  .J.........main.
0410: 80 1C 4B 80 46 00 1B                              ..K.F..         
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[0] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[2] = 0*
  3: 0x000D [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  4: 0x0012 [0x07] ExtData[1]->WorkLocal[0] += 6*
  5: 0x0017 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=ExtData[1]->WorkLocal[0], condition_work_offset=1*)
  6: 0x001E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=4*, condition_work_offset=1*)
  7: 0x0025 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=5*, condition_work_offset=1*)
  8: 0x002C [0x03] ExtData[1]->WorkLocal[1] = 0*
  9: 0x0031 [0x24] CREATE_DIALOG(message_id=7239*, default_option=0*, option_flags=ExtData[1]->WorkLocal[2])
    → "Select a destination. [NW./SW./NE./SE./CN./CS./Entrance #1./Entrance #2./Never mind.]"
 10: 0x0038 [0x25] WAIT_DIALOG_SELECT()
 11: 0x0039 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004E
 12: 0x0041 [0x03] ExtData[1]->WorkLocal[1] = 10*
 13: 0x0046 [0x03] Work_Zone[2] = 1*
 14: 0x004B [0x01] GOTO 0x00DD
 15: 0x004E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0063
 16: 0x0056 [0x03] ExtData[1]->WorkLocal[1] = 20*
 17: 0x005B [0x03] Work_Zone[2] = 2*
 18: 0x0060 [0x01] GOTO 0x00DD
 19: 0x0063 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0078
 20: 0x006B [0x03] ExtData[1]->WorkLocal[1] = 30*
 21: 0x0070 [0x03] Work_Zone[2] = 3*
 22: 0x0075 [0x01] GOTO 0x00DD
 23: 0x0078 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x008D
 24: 0x0080 [0x03] ExtData[1]->WorkLocal[1] = 40*
 25: 0x0085 [0x03] Work_Zone[2] = 4*
 26: 0x008A [0x01] GOTO 0x00DD
 27: 0x008D [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x009D
 28: 0x0095 [0x03] Work_Zone[1] = 51*
 29: 0x009A [0x01] GOTO 0x00DD
 30: 0x009D [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x00AD
 31: 0x00A5 [0x03] Work_Zone[1] = 52*
 32: 0x00AA [0x01] GOTO 0x00DD
 33: 0x00AD [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x00BD
 34: 0x00B5 [0x03] Work_Zone[1] = 1*
 35: 0x00BA [0x01] GOTO 0x00DD
 36: 0x00BD [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00CD
 37: 0x00C5 [0x03] Work_Zone[1] = 2*
 38: 0x00CA [0x01] GOTO 0x00DD
 39: 0x00CD [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x00DD
 40: 0x00D5 [0x03] Work_Zone[1] = 0*
 41: 0x00DA [0x01] GOTO 0x00DD

SUBROUTINE_00DD:
 42: 0x00DD [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00E8
 43: 0x00E5 [0x01] GOTO 0x0186
 44: 0x00E8 [0x03] ExtData[1]->WorkLocal[3] = 0*
 45: 0x00ED [0x02] IF !(ExtData[1]->WorkLocal[1] == 20*) GOTO 0x00FC
 46: 0x00F5 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=4*, condition_work_offset=1*)
 47: 0x00FC [0x02] IF !(ExtData[1]->WorkLocal[1] == 40*) GOTO 0x010B
 48: 0x0104 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=4*, condition_work_offset=1*)
 49: 0x010B [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[1]
 50: 0x0110 [0x24] CREATE_DIALOG(message_id=7240*, default_option=0*, option_flags=ExtData[1]->WorkLocal[3])
    → "Select a destination. [[/NW/SW/NE/SE] #1./[/NW/SW/NE/SE] #2./[/NW/SW/NE/SE] #3./[/NW/SW/NE/SE] #4./[/NW//NE] #5./Back./Never mind.]"
 51: 0x0117 [0x25] WAIT_DIALOG_SELECT()
 52: 0x0118 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0128
 53: 0x0120 [0x07] Work_Zone[1] += 1*
 54: 0x0125 [0x01] GOTO 0x0186
 55: 0x0128 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0138
 56: 0x0130 [0x07] Work_Zone[1] += 2*
 57: 0x0135 [0x01] GOTO 0x0186
 58: 0x0138 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0148
 59: 0x0140 [0x07] Work_Zone[1] += 3*
 60: 0x0145 [0x01] GOTO 0x0186
 61: 0x0148 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0158
 62: 0x0150 [0x07] Work_Zone[1] += 4*
 63: 0x0155 [0x01] GOTO 0x0186
 64: 0x0158 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0168
 65: 0x0160 [0x07] Work_Zone[1] += 5*
 66: 0x0165 [0x01] GOTO 0x0186
 67: 0x0168 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0176
 68: 0x0170 [0x01] GOTO 0x002C

SUBROUTINE_0186:
 69: 0x0186 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0191
 70: 0x018E [0x01] GOTO 0x03AD
 71: 0x0191 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 72: 0x0192 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[1]
 73: 0x0197 [0x03] Work_Zone[1] = 100*
 74: 0x019C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 75: 0x019E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 76: 0x01A0 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[4]
 77: 0x01A5 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 78: 0x01AC [0x02] IF !(Work_Zone[1] == 1*) GOTO 0x01C3
 79: 0x01B4 [0x47] UPDATE_PLAYER_POS(-608.000*, -600.000*, 0.000*, yaw=177.9°*)
 80: 0x01BE [0x47] WAIT_PLAYER_POS_UPDATE
 81: 0x01C0 [0x01] GOTO 0x03A6
 82: 0x01C3 [0x02] IF !(Work_Zone[1] == 2*) GOTO 0x01DA
 83: 0x01CB [0x47] UPDATE_PLAYER_POS(608.000*, -600.000*, 0.000*, yaw=0.0°*)
 84: 0x01D5 [0x47] WAIT_PLAYER_POS_UPDATE
 85: 0x01D7 [0x01] GOTO 0x03A6
 86: 0x01DA [0x02] IF !(Work_Zone[1] == 11*) GOTO 0x01F1
 87: 0x01E2 [0x47] UPDATE_PLAYER_POS(-440.000*, -88.000*, 0.000*, yaw=270.0°*)
 88: 0x01EC [0x47] WAIT_PLAYER_POS_UPDATE
 89: 0x01EE [0x01] GOTO 0x03A6
 90: 0x01F1 [0x02] IF !(Work_Zone[1] == 12*) GOTO 0x0208
 91: 0x01F9 [0x47] UPDATE_PLAYER_POS(-534.000*, 171.000*, 0.000*, yaw=225.0°*)
 92: 0x0203 [0x47] WAIT_PLAYER_POS_UPDATE
 93: 0x0205 [0x01] GOTO 0x03A6
 94: 0x0208 [0x02] IF !(Work_Zone[1] == 13*) GOTO 0x021F
 95: 0x0210 [0x47] UPDATE_PLAYER_POS(-294.000*, 171.000*, 0.000*, yaw=225.0°*)
 96: 0x021A [0x47] WAIT_PLAYER_POS_UPDATE
 97: 0x021C [0x01] GOTO 0x03A6
 98: 0x021F [0x02] IF !(Work_Zone[1] == 14*) GOTO 0x0236
 99: 0x0227 [0x47] UPDATE_PLAYER_POS(-628.000*, 497.000*, 0.000*, yaw=315.0°*)
100: 0x0231 [0x47] WAIT_PLAYER_POS_UPDATE
101: 0x0233 [0x01] GOTO 0x03A6
102: 0x0236 [0x02] IF !(Work_Zone[1] == 15*) GOTO 0x024D
103: 0x023E [0x47] UPDATE_PLAYER_POS(-388.000*, 498.000*, 0.000*, yaw=315.0°*)
104: 0x0248 [0x47] WAIT_PLAYER_POS_UPDATE
105: 0x024A [0x01] GOTO 0x03A6
106: 0x024D [0x02] IF !(Work_Zone[1] == 21*) GOTO 0x0264
107: 0x0255 [0x47] UPDATE_PLAYER_POS(-468.000*, -625.000*, 0.000*, yaw=315.0°*)
108: 0x025F [0x47] WAIT_PLAYER_POS_UPDATE
109: 0x0261 [0x01] GOTO 0x03A6
110: 0x0264 [0x02] IF !(Work_Zone[1] == 22*) GOTO 0x027B
111: 0x026C [0x47] UPDATE_PLAYER_POS(-576.000*, -428.000*, 0.000*, yaw=225.0°*)
112: 0x0276 [0x47] WAIT_PLAYER_POS_UPDATE
113: 0x0278 [0x01] GOTO 0x03A6
114: 0x027B [0x02] IF !(Work_Zone[1] == 23*) GOTO 0x0292
115: 0x0283 [0x47] UPDATE_PLAYER_POS(-428.000*, -385.000*, 0.000*, yaw=315.0°*)
116: 0x028D [0x47] WAIT_PLAYER_POS_UPDATE
117: 0x028F [0x01] GOTO 0x03A6
118: 0x0292 [0x02] IF !(Work_Zone[1] == 24*) GOTO 0x02A9
119: 0x029A [0x47] UPDATE_PLAYER_POS(-176.000*, -628.000*, 0.000*, yaw=225.0°*)
120: 0x02A4 [0x47] WAIT_PLAYER_POS_UPDATE
121: 0x02A6 [0x01] GOTO 0x03A6
122: 0x02A9 [0x02] IF !(Work_Zone[1] == 31*) GOTO 0x02C0
123: 0x02B1 [0x47] UPDATE_PLAYER_POS(440.000*, -88.000*, 0.000*, yaw=270.0°*)
124: 0x02BB [0x47] WAIT_PLAYER_POS_UPDATE
125: 0x02BD [0x01] GOTO 0x03A6
126: 0x02C0 [0x02] IF !(Work_Zone[1] == 32*) GOTO 0x02D7
127: 0x02C8 [0x47] UPDATE_PLAYER_POS(534.000*, 171.000*, 0.000*, yaw=315.0°*)
128: 0x02D2 [0x47] WAIT_PLAYER_POS_UPDATE
129: 0x02D4 [0x01] GOTO 0x03A6
130: 0x02D7 [0x02] IF !(Work_Zone[1] == 33*) GOTO 0x02EE
131: 0x02DF [0x47] UPDATE_PLAYER_POS(294.000*, 171.000*, 0.000*, yaw=315.0°*)
132: 0x02E9 [0x47] WAIT_PLAYER_POS_UPDATE
133: 0x02EB [0x01] GOTO 0x03A6
134: 0x02EE [0x02] IF !(Work_Zone[1] == 34*) GOTO 0x0305
135: 0x02F6 [0x47] UPDATE_PLAYER_POS(628.000*, 497.000*, 0.000*, yaw=225.0°*)
136: 0x0300 [0x47] WAIT_PLAYER_POS_UPDATE
137: 0x0302 [0x01] GOTO 0x03A6
138: 0x0305 [0x02] IF !(Work_Zone[1] == 35*) GOTO 0x031C
139: 0x030D [0x47] UPDATE_PLAYER_POS(388.000*, 498.000*, 0.000*, yaw=225.0°*)
140: 0x0317 [0x47] WAIT_PLAYER_POS_UPDATE
141: 0x0319 [0x01] GOTO 0x03A6
142: 0x031C [0x02] IF !(Work_Zone[1] == 41*) GOTO 0x0333
143: 0x0324 [0x47] UPDATE_PLAYER_POS(468.000*, -625.000*, 0.000*, yaw=225.0°*)
144: 0x032E [0x47] WAIT_PLAYER_POS_UPDATE
145: 0x0330 [0x01] GOTO 0x03A6
146: 0x0333 [0x02] IF !(Work_Zone[1] == 42*) GOTO 0x034A
147: 0x033B [0x47] UPDATE_PLAYER_POS(576.000*, -428.000*, 0.000*, yaw=315.0°*)
148: 0x0345 [0x47] WAIT_PLAYER_POS_UPDATE
149: 0x0347 [0x01] GOTO 0x03A6
150: 0x034A [0x02] IF !(Work_Zone[1] == 43*) GOTO 0x0361
151: 0x0352 [0x47] UPDATE_PLAYER_POS(428.000*, -385.000*, 0.000*, yaw=225.0°*)
152: 0x035C [0x47] WAIT_PLAYER_POS_UPDATE
153: 0x035E [0x01] GOTO 0x03A6
154: 0x0361 [0x02] IF !(Work_Zone[1] == 44*) GOTO 0x0378
155: 0x0369 [0x47] UPDATE_PLAYER_POS(176.000*, -628.000*, 0.000*, yaw=315.0°*)
156: 0x0373 [0x47] WAIT_PLAYER_POS_UPDATE
157: 0x0375 [0x01] GOTO 0x03A6
158: 0x0378 [0x02] IF !(Work_Zone[1] == 51*) GOTO 0x038F
159: 0x0380 [0x47] UPDATE_PLAYER_POS(0.000*, 200.000*, 0.000*, yaw=90.0°*)
160: 0x038A [0x47] WAIT_PLAYER_POS_UPDATE
161: 0x038C [0x01] GOTO 0x03A6
162: 0x038F [0x02] IF !(Work_Zone[1] == 52*) GOTO 0x03A6
163: 0x0397 [0x47] UPDATE_PLAYER_POS(0.000*, -200.000*, 0.000*, yaw=270.0°*)
164: 0x03A1 [0x47] WAIT_PLAYER_POS_UPDATE
165: 0x03A3 [0x01] GOTO 0x03A6

SUBROUTINE_03A6:
166: 0x03A6 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_03AD:
167: 0x03AD [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
168: 0x03AF [0x21] END_EVENT
169: 0x03B0 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0173 [0x01] GOTO 0x0186
# Dead code (unreachable instructions):
     0x03B1 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[73*, 0*]
     0x03C2 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[1]
     0x03C7 [0x03] Work_Zone[1] = 100*
     0x03CC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x03CE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x03D0 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[4]
     0x03D5 [0x1C] WAIT(140* ticks)
     0x03D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03E9 [0x1C] WAIT(60* ticks)
     0x03EC [0x46] CAMERA_CONTROL: Disable user control
     0x03EE [0x1B] RETURN
     0x03EF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0400 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[74*, 0*]
     0x0411 [0x1C] WAIT(170* ticks)
     0x0414 [0x46] CAMERA_CONTROL: Restore default settings
     0x0416 [0x1B] RETURN
```
