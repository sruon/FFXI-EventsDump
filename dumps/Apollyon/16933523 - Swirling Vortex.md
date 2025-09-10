# 16933523 - Swirling Vortex

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 1364 bytes        |
| Total Events     | 2                 |
| References Count | 76                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [102](#event-102)     | 0x0001       |   1032 |            188 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0006      |           6 |
|       2 | 0x0001      |           1 |
|       3 | 0x1C47      |        7239 |
|       4 | 0x000A      |          10 |
|       5 | 0x0014      |          20 |
|       6 | 0x0002      |           2 |
|       7 | 0x001E      |          30 |
|       8 | 0x0003      |           3 |
|       9 | 0x0028      |          40 |
|      10 | 0x0004      |           4 |
|      11 | 0x0033      |          51 |
|      12 | 0x0005      |           5 |
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
|      67 | 0x2FDA0     |      196000 |
|      68 | 0x0400      |        1024 |
|      69 | 0xFFFD0260  |  4294771296 |
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

### Event 102

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 1032 bytes |
| Instructions | 168        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 00 00 00 80  03 02 00 02 10 03 00 00    ..............
0010: 03 10 07 00 00 01 80 3C  02 00 00 00 02 80 03 01  .......<........
0020: 00 00 80 24 03 80 00 80  02 00 25 02 00 10 00 80  ...$......%.....
0030: 00 40 00 03 01 00 04 80  03 02 10 02 80 01 CF 00  .@..............
0040: 02 00 10 02 80 00 55 00  03 01 00 05 80 03 02 10  ......U.........
0050: 06 80 01 CF 00 02 00 10  06 80 00 6A 00 03 01 00  ...........j....
0060: 07 80 03 02 10 08 80 01  CF 00 02 00 10 08 80 00  ................
0070: 7F 00 03 01 00 09 80 03  02 10 0A 80 01 CF 00 02  ................
0080: 00 10 0A 80 00 8F 00 03  01 10 0B 80 01 CF 00 02  ................
0090: 00 10 0C 80 00 9F 00 03  01 10 0D 80 01 CF 00 02  ................
00A0: 00 10 01 80 00 AF 00 03  01 10 02 80 01 CF 00 02  ................
00B0: 00 10 0E 80 00 BF 00 03  01 10 06 80 01 CF 00 02  ................
00C0: 00 10 0F 80 00 CF 00 03  01 10 00 80 01 CF 00 02  ................
00D0: 01 00 00 80 00 DA 00 01  78 01 03 03 00 00 80 02  ........x.......
00E0: 01 00 05 80 00 EE 00 3C  03 00 0A 80 02 80 02 01  .......<........
00F0: 00 09 80 00 FD 00 3C 03  00 0A 80 02 80 03 01 10  ......<.........
0100: 01 00 24 10 80 00 80 03  00 25 02 00 10 00 80 00  ..$......%......
0110: 1A 01 07 01 10 02 80 01  78 01 02 00 10 02 80 00  ........x.......
0120: 2A 01 07 01 10 06 80 01  78 01 02 00 10 06 80 00  *.......x.......
0130: 3A 01 07 01 10 08 80 01  78 01 02 00 10 08 80 00  :.......x.......
0140: 4A 01 07 01 10 0A 80 01  78 01 02 00 10 0A 80 00  J.......x.......
0150: 5A 01 07 01 10 0C 80 01  78 01 02 00 10 0C 80 00  Z.......x.......
0160: 68 01 01 1E 00 01 78 01  02 00 10 01 80 00 78 01  h.....x.......x.
0170: 03 01 10 00 80 01 78 01  02 01 10 00 80 00 83 01  ......x.........
0180: 01 9F 03 42 03 04 00 01  10 03 01 10 11 80 43 00  ...B..........C.
0190: 43 01 03 01 10 04 00 29  01 F0 FF FF 7F 02 02 01  C......)........
01A0: 10 02 80 80 B5 01 47 00  12 80 13 80 00 80 14 80  ......G.........
01B0: 47 01 01 98 03 02 01 10  06 80 80 CC 01 47 00 15  G............G..
01C0: 80 13 80 00 80 00 80 47  01 01 98 03 02 01 10 16  .......G........
01D0: 80 80 E3 01 47 00 17 80  18 80 00 80 19 80 47 01  ....G.........G.
01E0: 01 98 03 02 01 10 1A 80  80 FA 01 47 00 1B 80 1C  ...........G....
01F0: 80 00 80 1D 80 47 01 01  98 03 02 01 10 1E 80 80  .....G..........
0200: 11 02 47 00 1F 80 1C 80  00 80 1D 80 47 01 01 98  ..G.........G...
0210: 03 02 01 10 20 80 80 28  02 47 00 21 80 22 80 00  .... ..(.G.!."..
0220: 80 23 80 47 01 01 98 03  02 01 10 24 80 80 3F 02  .#.G.......$..?.
0230: 47 00 25 80 26 80 00 80  23 80 47 01 01 98 03 02  G.%.&...#.G.....
0240: 01 10 27 80 80 56 02 47  00 28 80 29 80 00 80 23  ..'..V.G.(.)...#
0250: 80 47 01 01 98 03 02 01  10 2A 80 80 6D 02 47 00  .G.......*..m.G.
0260: 2B 80 2C 80 00 80 1D 80  47 01 01 98 03 02 01 10  +.,.....G.......
0270: 2D 80 80 84 02 47 00 2C  80 2E 80 00 80 23 80 47  -....G.,.....#.G
0280: 01 01 98 03 02 01 10 2F  80 80 9B 02 47 00 30 80  ......./....G.0.
0290: 21 80 00 80 1D 80 47 01  01 98 03 02 01 10 31 80  !.....G.......1.
02A0: 80 B2 02 47 00 32 80 18  80 00 80 19 80 47 01 01  ...G.2.......G..
02B0: 98 03 02 01 10 33 80 80  C9 02 47 00 34 80 1C 80  .....3....G.4...
02C0: 00 80 23 80 47 01 01 98  03 02 01 10 35 80 80 E0  ..#.G.......5...
02D0: 02 47 00 36 80 1C 80 00  80 23 80 47 01 01 98 03  .G.6.....#.G....
02E0: 02 01 10 37 80 80 F7 02  47 00 38 80 22 80 00 80  ...7....G.8."...
02F0: 1D 80 47 01 01 98 03 02  01 10 39 80 80 0E 03 47  ..G.......9....G
0300: 00 3A 80 26 80 00 80 1D  80 47 01 01 98 03 02 01  .:.&.....G......
0310: 10 3B 80 80 25 03 47 00  3C 80 29 80 00 80 1D 80  .;..%.G.<.).....
0320: 47 01 01 98 03 02 01 10  3D 80 80 3C 03 47 00 3E  G.......=..<.G.>
0330: 80 2C 80 00 80 23 80 47  01 01 98 03 02 01 10 3F  .,...#.G.......?
0340: 80 80 53 03 47 00 40 80  2E 80 00 80 1D 80 47 01  ..S.G.@.......G.
0350: 01 98 03 02 01 10 41 80  80 6A 03 47 00 42 80 21  ......A..j.G.B.!
0360: 80 00 80 23 80 47 01 01  98 03 02 01 10 0B 80 80  ...#.G..........
0370: 81 03 47 00 00 80 43 80  00 80 44 80 47 01 01 98  ..G...C...D.G...
0380: 03 02 01 10 0D 80 80 98  03 47 00 00 80 45 80 00  .........G...E..
0390: 80 19 80 47 01 01 98 03  29 01 F0 FF FF 7F 03 20  ...G....)...... 
03A0: 00 21 00 9F 46 80 F0 FF  FF 7F F0 FF FF 7F 6D 61  .!..F.........ma
03B0: 69 6E 00 80 03 04 00 01  10 03 01 10 11 80 43 00  in............C.
03C0: 43 01 03 01 10 04 00 1C  47 80 45 48 80 F0 FF FF  C.......G.EH....
03D0: 7F F0 FF FF 7F 66 64 6F  31 00 80 1C 49 80 46 01  .....fdo1...I.F.
03E0: 1B 45 48 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .EH.........fdi1
03F0: 00 80 9F 4A 80 F0 FF FF  7F F0 FF FF 7F 6D 61 69  ...J.........mai
0400: 6E 00 80 1C 4B 80 46 00  1B                       n...K.F..       
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[0] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[2]
  3: 0x000D [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  4: 0x0012 [0x07] ExtData[1]->WorkLocal[0] += 6*
  5: 0x0017 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=ExtData[1]->WorkLocal[0], condition_work_offset=1*)
  6: 0x001E [0x03] ExtData[1]->WorkLocal[1] = 0*
  7: 0x0023 [0x24] CREATE_DIALOG(message_id=7239*, default_option=0*, option_flags=ExtData[1]->WorkLocal[2])
    → "Select a destination. [NW./SW./NE./SE./CN./CS./Entrance #1./Entrance #2./Never mind.]"
  8: 0x002A [0x25] WAIT_DIALOG_SELECT()
  9: 0x002B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0040
 10: 0x0033 [0x03] ExtData[1]->WorkLocal[1] = 10*
 11: 0x0038 [0x03] Work_Zone[2] = 1*
 12: 0x003D [0x01] GOTO 0x00CF
 13: 0x0040 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0055
 14: 0x0048 [0x03] ExtData[1]->WorkLocal[1] = 20*
 15: 0x004D [0x03] Work_Zone[2] = 2*
 16: 0x0052 [0x01] GOTO 0x00CF
 17: 0x0055 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x006A
 18: 0x005D [0x03] ExtData[1]->WorkLocal[1] = 30*
 19: 0x0062 [0x03] Work_Zone[2] = 3*
 20: 0x0067 [0x01] GOTO 0x00CF
 21: 0x006A [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x007F
 22: 0x0072 [0x03] ExtData[1]->WorkLocal[1] = 40*
 23: 0x0077 [0x03] Work_Zone[2] = 4*
 24: 0x007C [0x01] GOTO 0x00CF
 25: 0x007F [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x008F
 26: 0x0087 [0x03] Work_Zone[1] = 51*
 27: 0x008C [0x01] GOTO 0x00CF
 28: 0x008F [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x009F
 29: 0x0097 [0x03] Work_Zone[1] = 52*
 30: 0x009C [0x01] GOTO 0x00CF
 31: 0x009F [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x00AF
 32: 0x00A7 [0x03] Work_Zone[1] = 1*
 33: 0x00AC [0x01] GOTO 0x00CF
 34: 0x00AF [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00BF
 35: 0x00B7 [0x03] Work_Zone[1] = 2*
 36: 0x00BC [0x01] GOTO 0x00CF
 37: 0x00BF [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x00CF
 38: 0x00C7 [0x03] Work_Zone[1] = 0*
 39: 0x00CC [0x01] GOTO 0x00CF

SUBROUTINE_00CF:
 40: 0x00CF [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00DA
 41: 0x00D7 [0x01] GOTO 0x0178
 42: 0x00DA [0x03] ExtData[1]->WorkLocal[3] = 0*
 43: 0x00DF [0x02] IF !(ExtData[1]->WorkLocal[1] == 20*) GOTO 0x00EE
 44: 0x00E7 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=4*, condition_work_offset=1*)
 45: 0x00EE [0x02] IF !(ExtData[1]->WorkLocal[1] == 40*) GOTO 0x00FD
 46: 0x00F6 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[3], bit_index_work_offset=4*, condition_work_offset=1*)
 47: 0x00FD [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[1]
 48: 0x0102 [0x24] CREATE_DIALOG(message_id=7240*, default_option=0*, option_flags=ExtData[1]->WorkLocal[3])
    → "Select a destination. [[/NW/SW/NE/SE] #1./[/NW/SW/NE/SE] #2./[/NW/SW/NE/SE] #3./[/NW/SW/NE/SE] #4./[/NW//NE] #5./Back./Never mind.]"
 49: 0x0109 [0x25] WAIT_DIALOG_SELECT()
 50: 0x010A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x011A
 51: 0x0112 [0x07] Work_Zone[1] += 1*
 52: 0x0117 [0x01] GOTO 0x0178
 53: 0x011A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x012A
 54: 0x0122 [0x07] Work_Zone[1] += 2*
 55: 0x0127 [0x01] GOTO 0x0178
 56: 0x012A [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x013A
 57: 0x0132 [0x07] Work_Zone[1] += 3*
 58: 0x0137 [0x01] GOTO 0x0178
 59: 0x013A [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x014A
 60: 0x0142 [0x07] Work_Zone[1] += 4*
 61: 0x0147 [0x01] GOTO 0x0178
 62: 0x014A [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x015A
 63: 0x0152 [0x07] Work_Zone[1] += 5*
 64: 0x0157 [0x01] GOTO 0x0178
 65: 0x015A [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0168
 66: 0x0162 [0x01] GOTO 0x001E

SUBROUTINE_0178:
 67: 0x0178 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0183
 68: 0x0180 [0x01] GOTO 0x039F
 69: 0x0183 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 70: 0x0184 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[1]
 71: 0x0189 [0x03] Work_Zone[1] = 100*
 72: 0x018E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 73: 0x0190 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 74: 0x0192 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[4]
 75: 0x0197 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 76: 0x019E [0x02] IF !(Work_Zone[1] == 1*) GOTO 0x01B5
 77: 0x01A6 [0x47] UPDATE_PLAYER_POS(-608.000*, -600.000*, 0.000*, yaw=177.9°*)
 78: 0x01B0 [0x47] WAIT_PLAYER_POS_UPDATE
 79: 0x01B2 [0x01] GOTO 0x0398
 80: 0x01B5 [0x02] IF !(Work_Zone[1] == 2*) GOTO 0x01CC
 81: 0x01BD [0x47] UPDATE_PLAYER_POS(608.000*, -600.000*, 0.000*, yaw=0.0°*)
 82: 0x01C7 [0x47] WAIT_PLAYER_POS_UPDATE
 83: 0x01C9 [0x01] GOTO 0x0398
 84: 0x01CC [0x02] IF !(Work_Zone[1] == 11*) GOTO 0x01E3
 85: 0x01D4 [0x47] UPDATE_PLAYER_POS(-440.000*, -88.000*, 0.000*, yaw=270.0°*)
 86: 0x01DE [0x47] WAIT_PLAYER_POS_UPDATE
 87: 0x01E0 [0x01] GOTO 0x0398
 88: 0x01E3 [0x02] IF !(Work_Zone[1] == 12*) GOTO 0x01FA
 89: 0x01EB [0x47] UPDATE_PLAYER_POS(-534.000*, 171.000*, 0.000*, yaw=225.0°*)
 90: 0x01F5 [0x47] WAIT_PLAYER_POS_UPDATE
 91: 0x01F7 [0x01] GOTO 0x0398
 92: 0x01FA [0x02] IF !(Work_Zone[1] == 13*) GOTO 0x0211
 93: 0x0202 [0x47] UPDATE_PLAYER_POS(-294.000*, 171.000*, 0.000*, yaw=225.0°*)
 94: 0x020C [0x47] WAIT_PLAYER_POS_UPDATE
 95: 0x020E [0x01] GOTO 0x0398
 96: 0x0211 [0x02] IF !(Work_Zone[1] == 14*) GOTO 0x0228
 97: 0x0219 [0x47] UPDATE_PLAYER_POS(-628.000*, 497.000*, 0.000*, yaw=315.0°*)
 98: 0x0223 [0x47] WAIT_PLAYER_POS_UPDATE
 99: 0x0225 [0x01] GOTO 0x0398
100: 0x0228 [0x02] IF !(Work_Zone[1] == 15*) GOTO 0x023F
101: 0x0230 [0x47] UPDATE_PLAYER_POS(-388.000*, 498.000*, 0.000*, yaw=315.0°*)
102: 0x023A [0x47] WAIT_PLAYER_POS_UPDATE
103: 0x023C [0x01] GOTO 0x0398
104: 0x023F [0x02] IF !(Work_Zone[1] == 21*) GOTO 0x0256
105: 0x0247 [0x47] UPDATE_PLAYER_POS(-468.000*, -625.000*, 0.000*, yaw=315.0°*)
106: 0x0251 [0x47] WAIT_PLAYER_POS_UPDATE
107: 0x0253 [0x01] GOTO 0x0398
108: 0x0256 [0x02] IF !(Work_Zone[1] == 22*) GOTO 0x026D
109: 0x025E [0x47] UPDATE_PLAYER_POS(-576.000*, -428.000*, 0.000*, yaw=225.0°*)
110: 0x0268 [0x47] WAIT_PLAYER_POS_UPDATE
111: 0x026A [0x01] GOTO 0x0398
112: 0x026D [0x02] IF !(Work_Zone[1] == 23*) GOTO 0x0284
113: 0x0275 [0x47] UPDATE_PLAYER_POS(-428.000*, -385.000*, 0.000*, yaw=315.0°*)
114: 0x027F [0x47] WAIT_PLAYER_POS_UPDATE
115: 0x0281 [0x01] GOTO 0x0398
116: 0x0284 [0x02] IF !(Work_Zone[1] == 24*) GOTO 0x029B
117: 0x028C [0x47] UPDATE_PLAYER_POS(-176.000*, -628.000*, 0.000*, yaw=225.0°*)
118: 0x0296 [0x47] WAIT_PLAYER_POS_UPDATE
119: 0x0298 [0x01] GOTO 0x0398
120: 0x029B [0x02] IF !(Work_Zone[1] == 31*) GOTO 0x02B2
121: 0x02A3 [0x47] UPDATE_PLAYER_POS(440.000*, -88.000*, 0.000*, yaw=270.0°*)
122: 0x02AD [0x47] WAIT_PLAYER_POS_UPDATE
123: 0x02AF [0x01] GOTO 0x0398
124: 0x02B2 [0x02] IF !(Work_Zone[1] == 32*) GOTO 0x02C9
125: 0x02BA [0x47] UPDATE_PLAYER_POS(534.000*, 171.000*, 0.000*, yaw=315.0°*)
126: 0x02C4 [0x47] WAIT_PLAYER_POS_UPDATE
127: 0x02C6 [0x01] GOTO 0x0398
128: 0x02C9 [0x02] IF !(Work_Zone[1] == 33*) GOTO 0x02E0
129: 0x02D1 [0x47] UPDATE_PLAYER_POS(294.000*, 171.000*, 0.000*, yaw=315.0°*)
130: 0x02DB [0x47] WAIT_PLAYER_POS_UPDATE
131: 0x02DD [0x01] GOTO 0x0398
132: 0x02E0 [0x02] IF !(Work_Zone[1] == 34*) GOTO 0x02F7
133: 0x02E8 [0x47] UPDATE_PLAYER_POS(628.000*, 497.000*, 0.000*, yaw=225.0°*)
134: 0x02F2 [0x47] WAIT_PLAYER_POS_UPDATE
135: 0x02F4 [0x01] GOTO 0x0398
136: 0x02F7 [0x02] IF !(Work_Zone[1] == 35*) GOTO 0x030E
137: 0x02FF [0x47] UPDATE_PLAYER_POS(388.000*, 498.000*, 0.000*, yaw=225.0°*)
138: 0x0309 [0x47] WAIT_PLAYER_POS_UPDATE
139: 0x030B [0x01] GOTO 0x0398
140: 0x030E [0x02] IF !(Work_Zone[1] == 41*) GOTO 0x0325
141: 0x0316 [0x47] UPDATE_PLAYER_POS(468.000*, -625.000*, 0.000*, yaw=225.0°*)
142: 0x0320 [0x47] WAIT_PLAYER_POS_UPDATE
143: 0x0322 [0x01] GOTO 0x0398
144: 0x0325 [0x02] IF !(Work_Zone[1] == 42*) GOTO 0x033C
145: 0x032D [0x47] UPDATE_PLAYER_POS(576.000*, -428.000*, 0.000*, yaw=315.0°*)
146: 0x0337 [0x47] WAIT_PLAYER_POS_UPDATE
147: 0x0339 [0x01] GOTO 0x0398
148: 0x033C [0x02] IF !(Work_Zone[1] == 43*) GOTO 0x0353
149: 0x0344 [0x47] UPDATE_PLAYER_POS(428.000*, -385.000*, 0.000*, yaw=225.0°*)
150: 0x034E [0x47] WAIT_PLAYER_POS_UPDATE
151: 0x0350 [0x01] GOTO 0x0398
152: 0x0353 [0x02] IF !(Work_Zone[1] == 44*) GOTO 0x036A
153: 0x035B [0x47] UPDATE_PLAYER_POS(176.000*, -628.000*, 0.000*, yaw=315.0°*)
154: 0x0365 [0x47] WAIT_PLAYER_POS_UPDATE
155: 0x0367 [0x01] GOTO 0x0398
156: 0x036A [0x02] IF !(Work_Zone[1] == 51*) GOTO 0x0381
157: 0x0372 [0x47] UPDATE_PLAYER_POS(0.000*, 196.000*, 0.000*, yaw=90.0°*)
158: 0x037C [0x47] WAIT_PLAYER_POS_UPDATE
159: 0x037E [0x01] GOTO 0x0398
160: 0x0381 [0x02] IF !(Work_Zone[1] == 52*) GOTO 0x0398
161: 0x0389 [0x47] UPDATE_PLAYER_POS(0.000*, -196.000*, 0.000*, yaw=270.0°*)
162: 0x0393 [0x47] WAIT_PLAYER_POS_UPDATE
163: 0x0395 [0x01] GOTO 0x0398

SUBROUTINE_0398:
164: 0x0398 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_039F:
165: 0x039F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
166: 0x03A1 [0x21] END_EVENT
167: 0x03A2 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0165 [0x01] GOTO 0x0178
# Dead code (unreachable instructions):
     0x03A3 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[73*, 0*]
     0x03B4 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[1]
     0x03B9 [0x03] Work_Zone[1] = 100*
     0x03BE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x03C0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x03C2 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[4]
     0x03C7 [0x1C] WAIT(140* ticks)
     0x03CA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03DB [0x1C] WAIT(60* ticks)
     0x03DE [0x46] CAMERA_CONTROL: Disable user control
     0x03E0 [0x1B] RETURN
     0x03E1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03F2 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[74*, 0*]
     0x0403 [0x1C] WAIT(170* ticks)
     0x0406 [0x46] CAMERA_CONTROL: Restore default settings
     0x0408 [0x1B] RETURN
```
