# 16929278 - Matter Diffusion Module

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 1076 bytes       |
| Total Events     | 2                |
| References Count | 56               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1000](#event-1000)   | 0x0001       |    825 |            152 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0004      |           4 |
|       2 | 0x0001      |           1 |
|       3 | 0x0005      |           5 |
|       4 | 0x0006      |           6 |
|       5 | 0x1C43      |        7235 |
|       6 | 0x0002      |           2 |
|       7 | 0x0003      |           3 |
|       8 | 0x0033      |          51 |
|       9 | 0x1C44      |        7236 |
|      10 | 0x000A      |          10 |
|      11 | 0x0007      |           7 |
|      12 | 0x0008      |           8 |
|      13 | 0x0064      |         100 |
|      14 | 0x000B      |          11 |
|      15 | 0xFFFDDD20  |  4294827296 |
|      16 | 0x5BCC0     |      376000 |
|      17 | 0xFFFEBE34  |  4294884916 |
|      18 | 0x0C00      |        3072 |
|      19 | 0x000C      |          12 |
|      20 | 0xFFFC0860  |  4294707296 |
|      21 | 0x12F34     |       77620 |
|      22 | 0x000D      |          13 |
|      23 | 0xFFF8FB20  |  4294507296 |
|      24 | 0x000E      |          14 |
|      25 | 0xFFF72660  |  4294387296 |
|      26 | 0x0015      |          21 |
|      27 | 0x17700     |       96000 |
|      28 | 0xFFFD85B4  |  4294804916 |
|      29 | 0x0016      |          22 |
|      30 | 0xFFFFF6B4  |  4294964916 |
|      31 | 0x0017      |          23 |
|      32 | 0x0018      |          24 |
|      33 | 0x001F      |          31 |
|      34 | 0xFFFD3140  |  4294783296 |
|      35 | 0x0020      |          32 |
|      36 | 0x0021      |          33 |
|      37 | 0x0022      |          34 |
|      38 | 0x0029      |          41 |
|      39 | 0x3F7A0     |      260000 |
|      40 | 0xFFF84F40  |  4294463296 |
|      41 | 0x002A      |          42 |
|      42 | 0x4E20      |       20000 |
|      43 | 0xFFF7B300  |  4294423296 |
|      44 | 0x002B      |          43 |
|      45 | 0xFFFB7BC0  |  4294671296 |
|      46 | 0xFFF85EE0  |  4294467296 |
|      47 | 0x0800      |        2048 |
|      48 | 0xFFF7C2A0  |  4294427296 |
|      49 | 0xFFF716C0  |  4294383296 |
|      50 | 0x004B      |          75 |
|      51 | 0x00B4      |         180 |
|      52 | 0x00C8      |         200 |
|      53 | 0x003C      |          60 |
|      54 | 0x004C      |          76 |
|      55 | 0x00AA      |         170 |

## String References

- **7235**: Enter which tower? [Northern Tower./Western Tower./Eastern Tower./Central Tower./Central Tower B1./Never mind.]
- **7236**: Select a destination. [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Back./Never mind.]

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

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 825 bytes |
| Instructions | 132       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 02 00 00 80  03 00 00 02 10 03 01 00    ..............
0010: 00 80 3C 01 00 01 80 02  80 3C 01 00 03 80 02 80  ..<......<......
0020: 3C 01 00 04 80 02 80 24  05 80 02 00 00 00 25 02  <......$......%.
0030: 00 10 00 80 00 3F 00 03  02 10 02 80 01 96 00 02  .....?..........
0040: 00 10 02 80 00 4F 00 03  02 10 06 80 01 96 00 02  .....O..........
0050: 00 10 06 80 00 5F 00 03  02 10 07 80 01 96 00 02  ....._..........
0060: 00 10 07 80 00 76 00 03  02 10 01 80 3C 01 00 07  .....v......<...
0070: 80 02 80 01 96 00 02 00  10 01 80 00 86 00 03 02  ................
0080: 10 08 80 01 96 00 02 00  10 03 80 00 96 00 03 02  ................
0090: 10 00 80 01 96 00 02 02  10 00 80 00 A1 00 01 D0  ................
00A0: 02 02 02 10 08 80 00 AC  00 01 2E 01 03 02 00 02  ................
00B0: 10 0C 02 00 24 09 80 00  80 01 00 25 02 00 10 00  ....$......%....
00C0: 80 00 D1 00 14 02 10 0A  80 07 02 10 02 80 01 2E  ................
00D0: 01 02 00 10 02 80 00 E6  00 14 02 10 0A 80 07 02  ................
00E0: 10 06 80 01 2E 01 02 00  10 06 80 00 FB 00 14 02  ................
00F0: 10 0A 80 07 02 10 07 80  01 2E 01 02 00 10 07 80  ................
0100: 00 10 01 14 02 10 0A 80  07 02 10 01 80 01 2E 01  ................
0110: 02 00 10 0B 80 00 1E 01  01 0D 00 01 2E 01 02 00  ................
0120: 10 0C 80 00 2E 01 03 02  10 00 80 01 2E 01 02 02  ................
0130: 10 00 80 00 39 01 01 D0  02 03 01 10 02 10 42 03  ....9.........B.
0140: 03 00 01 10 03 01 10 0D  80 43 00 43 01 03 01 10  .........C.C....
0150: 03 00 29 01 F0 FF FF 7F  02 02 01 10 0E 80 80 70  ..)............p
0160: 01 47 00 0F 80 10 80 11  80 12 80 47 01 01 C9 02  .G.........G....
0170: 02 01 10 13 80 80 87 01  47 00 14 80 10 80 15 80  ........G.......
0180: 12 80 47 01 01 C9 02 02  01 10 16 80 80 9E 01 47  ..G............G
0190: 00 17 80 10 80 11 80 12  80 47 01 01 C9 02 02 01  .........G......
01A0: 10 18 80 80 B5 01 47 00  19 80 10 80 15 80 12 80  ......G.........
01B0: 47 01 01 C9 02 02 01 10  1A 80 80 CC 01 47 00 0F  G............G..
01C0: 80 1B 80 1C 80 12 80 47  01 01 C9 02 02 01 10 1D  .......G........
01D0: 80 80 E3 01 47 00 14 80  1B 80 1E 80 12 80 47 01  ....G.........G.
01E0: 01 C9 02 02 01 10 1F 80  80 FA 01 47 00 17 80 1B  ...........G....
01F0: 80 1C 80 12 80 47 01 01  C9 02 02 01 10 20 80 80  .....G....... ..
0200: 11 02 47 00 19 80 1B 80  1E 80 12 80 47 01 01 C9  ..G.........G...
0210: 02 02 01 10 21 80 80 28  02 47 00 0F 80 22 80 11  ....!..(.G..."..
0220: 80 12 80 47 01 01 C9 02  02 01 10 23 80 80 3F 02  ...G.......#..?.
0230: 47 00 14 80 22 80 15 80  12 80 47 01 01 C9 02 02  G...".....G.....
0240: 01 10 24 80 80 56 02 47  00 17 80 22 80 11 80 12  ..$..V.G..."....
0250: 80 47 01 01 C9 02 02 01  10 25 80 80 6D 02 47 00  .G.......%..m.G.
0260: 19 80 22 80 15 80 12 80  47 01 01 C9 02 02 01 10  ..".....G.......
0270: 26 80 80 84 02 47 00 27  80 28 80 1C 80 12 80 47  &....G.'.(.....G
0280: 01 01 C9 02 02 01 10 29  80 80 9B 02 47 00 2A 80  .......)....G.*.
0290: 2B 80 1E 80 12 80 47 01  01 C9 02 02 01 10 2C 80  +.....G.......,.
02A0: 80 B2 02 47 00 2D 80 2E  80 1C 80 2F 80 47 01 01  ...G.-...../.G..
02B0: C9 02 02 01 10 08 80 80  C9 02 47 00 30 80 31 80  ..........G.0.1.
02C0: 1E 80 12 80 47 01 01 C9  02 29 01 F0 FF FF 7F 03  ....G....)......
02D0: 20 00 21 00 9F 32 80 F0  FF FF 7F F0 FF FF 7F 6D   .!..2.........m
02E0: 61 69 6E 00 80 03 03 00  01 10 03 01 10 0D 80 43  ain............C
02F0: 00 43 01 03 01 10 03 00  1C 33 80 45 34 80 F0 FF  .C.......3.E4...
0300: FF 7F F0 FF FF 7F 66 64  6F 31 00 80 1C 35 80 46  ......fdo1...5.F
0310: 01 1B 45 34 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E4.........fdi
0320: 31 00 80 9F 36 80 F0 FF  FF 7F F0 FF FF 7F 6D 61  1...6.........ma
0330: 69 6E 00 80 1C 37 80 46  00 1B                    in...7.F..      
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[2] = 0*
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x000D [0x03] ExtData[1]->WorkLocal[1] = 0*
  4: 0x0012 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=4*, condition_work_offset=1*)
  5: 0x0019 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=5*, condition_work_offset=1*)
  6: 0x0020 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=6*, condition_work_offset=1*)
  7: 0x0027 [0x24] CREATE_DIALOG(message_id=7235*, default_option=ExtData[1]->WorkLocal[2], option_flags=ExtData[1]->WorkLocal[0])
    → "Enter which tower? [Northern Tower./Western Tower./Eastern Tower./Central Tower./Central Tower B1./Never mind.]"
  8: 0x002E [0x25] WAIT_DIALOG_SELECT()
  9: 0x002F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003F
 10: 0x0037 [0x03] Work_Zone[2] = 1*
 11: 0x003C [0x01] GOTO 0x0096
 12: 0x003F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004F
 13: 0x0047 [0x03] Work_Zone[2] = 2*
 14: 0x004C [0x01] GOTO 0x0096
 15: 0x004F [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x005F
 16: 0x0057 [0x03] Work_Zone[2] = 3*
 17: 0x005C [0x01] GOTO 0x0096
 18: 0x005F [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0076
 19: 0x0067 [0x03] Work_Zone[2] = 4*
 20: 0x006C [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=3*, condition_work_offset=1*)
 21: 0x0073 [0x01] GOTO 0x0096
 22: 0x0076 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0086
 23: 0x007E [0x03] Work_Zone[2] = 51*
 24: 0x0083 [0x01] GOTO 0x0096
 25: 0x0086 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0096
 26: 0x008E [0x03] Work_Zone[2] = 0*
 27: 0x0093 [0x01] GOTO 0x0096

SUBROUTINE_0096:
 28: 0x0096 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00A1
 29: 0x009E [0x01] GOTO 0x02D0
 30: 0x00A1 [0x02] IF !(Work_Zone[2] == 51*) GOTO 0x00AC
 31: 0x00A9 [0x01] GOTO 0x012E
 32: 0x00AC [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[2]
 33: 0x00B1 [0x0C] ExtData[1]->WorkLocal[2]--
 34: 0x00B4 [0x24] CREATE_DIALOG(message_id=7236*, default_option=0*, option_flags=ExtData[1]->WorkLocal[1])
    → "Select a destination. [[/Northern/Western/Eastern/Central] Tower - 1st Floor./[/Northern/Western/Eastern/Central] Tower - 2nd Floor./[/Northern/Western/Eastern/Central] Tower - 3rd Floor./[/Northern/Western/Eastern/Central] Tower - 4th Floor./[/Northern/Western/Eastern] Tower - 5th Floor./[/Northern/Western/Eastern] Tower - 6th Floor./[/Northern/Western/Eastern] Tower - 7th Floor./Back./Never mind.]"
 35: 0x00BB [0x25] WAIT_DIALOG_SELECT()
 36: 0x00BC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00D1
 37: 0x00C4 [0x14] Work_Zone[2] *= 10*
 38: 0x00C9 [0x07] Work_Zone[2] += 1*
 39: 0x00CE [0x01] GOTO 0x012E
 40: 0x00D1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00E6
 41: 0x00D9 [0x14] Work_Zone[2] *= 10*
 42: 0x00DE [0x07] Work_Zone[2] += 2*
 43: 0x00E3 [0x01] GOTO 0x012E
 44: 0x00E6 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00FB
 45: 0x00EE [0x14] Work_Zone[2] *= 10*
 46: 0x00F3 [0x07] Work_Zone[2] += 3*
 47: 0x00F8 [0x01] GOTO 0x012E
 48: 0x00FB [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0110
 49: 0x0103 [0x14] Work_Zone[2] *= 10*
 50: 0x0108 [0x07] Work_Zone[2] += 4*
 51: 0x010D [0x01] GOTO 0x012E
 52: 0x0110 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x011E
 53: 0x0118 [0x01] GOTO 0x000D

SUBROUTINE_012E:
 54: 0x012E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0139
 55: 0x0136 [0x01] GOTO 0x02D0
 56: 0x0139 [0x03] Work_Zone[1] = Work_Zone[2]
 57: 0x013E [0x42] SET_CLI_EVENT_CANCEL_DATA()
 58: 0x013F [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[1]
 59: 0x0144 [0x03] Work_Zone[1] = 100*
 60: 0x0149 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 61: 0x014B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 62: 0x014D [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[3]
 63: 0x0152 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 64: 0x0159 [0x02] IF !(Work_Zone[1] == 11*) GOTO 0x0170
 65: 0x0161 [0x47] UPDATE_PLAYER_POS(-140.000*, 376.000*, -82.380*, yaw=270.0°*)
 66: 0x016B [0x47] WAIT_PLAYER_POS_UPDATE
 67: 0x016D [0x01] GOTO 0x02C9
 68: 0x0170 [0x02] IF !(Work_Zone[1] == 12*) GOTO 0x0187
 69: 0x0178 [0x47] UPDATE_PLAYER_POS(-260.000*, 376.000*, 77.620*, yaw=270.0°*)
 70: 0x0182 [0x47] WAIT_PLAYER_POS_UPDATE
 71: 0x0184 [0x01] GOTO 0x02C9
 72: 0x0187 [0x02] IF !(Work_Zone[1] == 13*) GOTO 0x019E
 73: 0x018F [0x47] UPDATE_PLAYER_POS(-460.000*, 376.000*, -82.380*, yaw=270.0°*)
 74: 0x0199 [0x47] WAIT_PLAYER_POS_UPDATE
 75: 0x019B [0x01] GOTO 0x02C9
 76: 0x019E [0x02] IF !(Work_Zone[1] == 14*) GOTO 0x01B5
 77: 0x01A6 [0x47] UPDATE_PLAYER_POS(-580.000*, 376.000*, 77.620*, yaw=270.0°*)
 78: 0x01B0 [0x47] WAIT_PLAYER_POS_UPDATE
 79: 0x01B2 [0x01] GOTO 0x02C9
 80: 0x01B5 [0x02] IF !(Work_Zone[1] == 21*) GOTO 0x01CC
 81: 0x01BD [0x47] UPDATE_PLAYER_POS(-140.000*, 96.000*, -162.380*, yaw=270.0°*)
 82: 0x01C7 [0x47] WAIT_PLAYER_POS_UPDATE
 83: 0x01C9 [0x01] GOTO 0x02C9
 84: 0x01CC [0x02] IF !(Work_Zone[1] == 22*) GOTO 0x01E3
 85: 0x01D4 [0x47] UPDATE_PLAYER_POS(-260.000*, 96.000*, -2.380*, yaw=270.0°*)
 86: 0x01DE [0x47] WAIT_PLAYER_POS_UPDATE
 87: 0x01E0 [0x01] GOTO 0x02C9
 88: 0x01E3 [0x02] IF !(Work_Zone[1] == 23*) GOTO 0x01FA
 89: 0x01EB [0x47] UPDATE_PLAYER_POS(-460.000*, 96.000*, -162.380*, yaw=270.0°*)
 90: 0x01F5 [0x47] WAIT_PLAYER_POS_UPDATE
 91: 0x01F7 [0x01] GOTO 0x02C9
 92: 0x01FA [0x02] IF !(Work_Zone[1] == 24*) GOTO 0x0211
 93: 0x0202 [0x47] UPDATE_PLAYER_POS(-580.000*, 96.000*, -2.380*, yaw=270.0°*)
 94: 0x020C [0x47] WAIT_PLAYER_POS_UPDATE
 95: 0x020E [0x01] GOTO 0x02C9
 96: 0x0211 [0x02] IF !(Work_Zone[1] == 31*) GOTO 0x0228
 97: 0x0219 [0x47] UPDATE_PLAYER_POS(-140.000*, -184.000*, -82.380*, yaw=270.0°*)
 98: 0x0223 [0x47] WAIT_PLAYER_POS_UPDATE
 99: 0x0225 [0x01] GOTO 0x02C9
100: 0x0228 [0x02] IF !(Work_Zone[1] == 32*) GOTO 0x023F
101: 0x0230 [0x47] UPDATE_PLAYER_POS(-260.000*, -184.000*, 77.620*, yaw=270.0°*)
102: 0x023A [0x47] WAIT_PLAYER_POS_UPDATE
103: 0x023C [0x01] GOTO 0x02C9
104: 0x023F [0x02] IF !(Work_Zone[1] == 33*) GOTO 0x0256
105: 0x0247 [0x47] UPDATE_PLAYER_POS(-460.000*, -184.000*, -82.380*, yaw=270.0°*)
106: 0x0251 [0x47] WAIT_PLAYER_POS_UPDATE
107: 0x0253 [0x01] GOTO 0x02C9
108: 0x0256 [0x02] IF !(Work_Zone[1] == 34*) GOTO 0x026D
109: 0x025E [0x47] UPDATE_PLAYER_POS(-580.000*, -184.000*, 77.620*, yaw=270.0°*)
110: 0x0268 [0x47] WAIT_PLAYER_POS_UPDATE
111: 0x026A [0x01] GOTO 0x02C9
112: 0x026D [0x02] IF !(Work_Zone[1] == 41*) GOTO 0x0284
113: 0x0275 [0x47] UPDATE_PLAYER_POS(260.000*, -504.000*, -162.380*, yaw=270.0°*)
114: 0x027F [0x47] WAIT_PLAYER_POS_UPDATE
115: 0x0281 [0x01] GOTO 0x02C9
116: 0x0284 [0x02] IF !(Work_Zone[1] == 42*) GOTO 0x029B
117: 0x028C [0x47] UPDATE_PLAYER_POS(20.000*, -544.000*, -2.380*, yaw=270.0°*)
118: 0x0296 [0x47] WAIT_PLAYER_POS_UPDATE
119: 0x0298 [0x01] GOTO 0x02C9
120: 0x029B [0x02] IF !(Work_Zone[1] == 43*) GOTO 0x02B2
121: 0x02A3 [0x47] UPDATE_PLAYER_POS(-296.000*, -500.000*, -162.380*, yaw=180.0°*)
122: 0x02AD [0x47] WAIT_PLAYER_POS_UPDATE
123: 0x02AF [0x01] GOTO 0x02C9
124: 0x02B2 [0x02] IF !(Work_Zone[1] == 51*) GOTO 0x02C9
125: 0x02BA [0x47] UPDATE_PLAYER_POS(-540.000*, -584.000*, -2.380*, yaw=270.0°*)
126: 0x02C4 [0x47] WAIT_PLAYER_POS_UPDATE
127: 0x02C6 [0x01] GOTO 0x02C9

SUBROUTINE_02C9:
128: 0x02C9 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_02D0:
129: 0x02D0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
130: 0x02D2 [0x21] END_EVENT
131: 0x02D3 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x011B [0x01] GOTO 0x012E
# Dead code (unreachable instructions):
     0x02D4 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[75*, 0*]
     0x02E5 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[1]
     0x02EA [0x03] Work_Zone[1] = 100*
     0x02EF [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x02F1 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x02F3 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[3]
     0x02F8 [0x1C] WAIT(180* ticks)
     0x02FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x030C [0x1C] WAIT(60* ticks)
     0x030F [0x46] CAMERA_CONTROL: Disable user control
     0x0311 [0x1B] RETURN
     0x0312 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0323 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[76*, 0*]
     0x0334 [0x1C] WAIT(170* ticks)
     0x0337 [0x46] CAMERA_CONTROL: Restore default settings
     0x0339 [0x1B] RETURN
```
