# 16839111 - Time Master Debug

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Konschtat (ID: 15) |
| Block Size       | 1328 bytes                   |
| Total Events     | 2                            |
| References Count | 35                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2000](#event-2000)   | 0x0001       |   1161 |            181 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x1E3F      |        7743 |
|       4 | 0x003C      |          60 |
|       5 | 0x0078      |         120 |
|       6 | 0x0003      |           3 |
|       7 | 0x0004      |           4 |
|       8 | 0x0006      |           6 |
|       9 | 0x0005      |           5 |
|      10 | 0x04F7      |        1271 |
|      11 | 0x1E40      |        7744 |
|      12 | 0x40000000  |  1073741824 |
|      13 | 0x1E41      |        7745 |
|      14 | 0x000F      |          15 |
|      15 | 0x0010      |          16 |
|      16 | 0x001F      |          31 |
|      17 | 0x00B4      |         180 |
|      18 | 0x012C      |         300 |
|      19 | 0x0258      |         600 |
|      20 | 0x0007      |           7 |
|      21 | 0x0384      |         900 |
|      22 | 0x0008      |           8 |
|      23 | 0x0708      |        1800 |
|      24 | 0x0009      |           9 |
|      25 | 0x0A8C      |        2700 |
|      26 | 0x000A      |          10 |
|      27 | 0x0E10      |        3600 |
|      28 | 0x000B      |          11 |
|      29 | 0x1194      |        4500 |
|      30 | 0x000C      |          12 |
|      31 | 0x1518      |        5400 |
|      32 | 0x000D      |          13 |
|      33 | 0x1C20      |        7200 |
|      34 | 0x1E42      |        7746 |

## String References

- **7743**: Time debug: Time limit: $0 [sec./min.] Time debug: Search flag: [OFF/ON] Time debug: Search flag switched ON flag: [OFF/ON] Time debug: Forced exit flag: [OFF/ON]
- **7744**: Time debug: Do what? [Nuttin'./Increase time limit./Reduce time limit./Switch OFF "Search flag switched ON flag."/Forced exit flag OFF./Receive one $3.]
- **7745**: Time debug: Increase by how much? [Return./+0 minute./+1 minute./+2 minutes./+3 minutes./+5 minutes./+10 minutes./+15 minutes./+30 minutes./+45 minutes./+60 minutes./+75 minutes./+90 minutes./+120 minutes.]
- **7746**: Time debug: Reduce by how much? [\`Gi/-0 minute./-1 minute./-2 minutes./-3 minutes./-5 minutes./-10 minutes./-15 minutes./-30 minutes./-45 minutes./-60 minutes./-75 minutes./-90 minutes./-120 minutes.]

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

### Event 2000

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 1161 bytes |
| Instructions | 181        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 00 00 02 10  03 01 00 03 10 03 02 00    ..............
0010: 04 10 03 03 00 05 10 03  02 10 00 80 03 03 10 00  ................
0020: 80 03 04 10 00 80 03 05  10 00 80 03 06 10 00 80  ................
0030: 03 02 10 01 00 03 03 10  00 80 3E 00 00 00 80 49  ..........>....I
0040: 00 03 04 10 01 80 01 4E  00 03 04 10 00 80 3E 00  .......N......>.
0050: 00 01 80 5D 00 03 05 10  01 80 01 62 00 03 05 10  ...].......b....
0060: 00 80 3E 00 00 02 80 71  00 03 06 10 01 80 01 76  ..>....q.......v
0070: 00 03 06 10 00 80 48 03  80 23 03 04 00 00 80 03  ......H..#......
0080: 05 00 01 00 15 05 00 04  80 02 05 00 00 80 05 9B  ................
0090: 00 3C 04 00 02 80 01 80  01 AA 00 02 05 00 05 80  .<..............
00A0: 04 AA 00 3C 04 00 01 80  01 80 3E 00 00 01 80 B4  ...<......>.....
00B0: 00 01 BB 00 3C 04 00 06  80 01 80 3E 00 00 02 80  ....<......>....
00C0: C5 00 01 CC 00 3C 04 00  07 80 01 80 02 03 00 08  .....<..........
00D0: 80 04 DB 00 3C 04 00 09  80 01 80 03 02 10 0A 80  ....<...........
00E0: 24 0B 80 00 80 04 00 25  02 00 10 00 80 00 F8 00  $......%........
00F0: 03 01 10 0C 80 01 87 04  02 00 10 01 80 00 94 02  ................
0100: 24 0D 80 00 80 00 80 25  02 00 10 00 80 00 18 01  $......%........
0110: 03 01 10 0C 80 01 91 02  02 00 10 01 80 00 35 01  ..............5.
0120: 40 00 80 0E 80 01 10 01  80 40 0F 80 10 80 01 10  @........@......
0130: 00 80 01 91 02 02 00 10  02 80 00 52 01 40 00 80  ...........R.@..
0140: 0E 80 01 10 01 80 40 0F  80 10 80 01 10 04 80 01  ......@.........
0150: 91 02 02 00 10 06 80 00  6F 01 40 00 80 0E 80 01  ........o.@.....
0160: 10 01 80 40 0F 80 10 80  01 10 05 80 01 91 02 02  ...@............
0170: 00 10 07 80 00 8C 01 40  00 80 0E 80 01 10 01 80  .......@........
0180: 40 0F 80 10 80 01 10 11  80 01 91 02 02 00 10 09  @...............
0190: 80 00 A9 01 40 00 80 0E  80 01 10 01 80 40 0F 80  ....@........@..
01A0: 10 80 01 10 12 80 01 91  02 02 00 10 08 80 00 C6  ................
01B0: 01 40 00 80 0E 80 01 10  01 80 40 0F 80 10 80 01  .@........@.....
01C0: 10 13 80 01 91 02 02 00  10 14 80 00 E3 01 40 00  ..............@.
01D0: 80 0E 80 01 10 01 80 40  0F 80 10 80 01 10 15 80  .......@........
01E0: 01 91 02 02 00 10 16 80  00 00 02 40 00 80 0E 80  ...........@....
01F0: 01 10 01 80 40 0F 80 10  80 01 10 17 80 01 91 02  ....@...........
0200: 02 00 10 18 80 00 1D 02  40 00 80 0E 80 01 10 01  ........@.......
0210: 80 40 0F 80 10 80 01 10  19 80 01 91 02 02 00 10  .@..............
0220: 1A 80 00 3A 02 40 00 80  0E 80 01 10 01 80 40 0F  ...:.@........@.
0230: 80 10 80 01 10 1B 80 01  91 02 02 00 10 1C 80 00  ................
0240: 57 02 40 00 80 0E 80 01  10 01 80 40 0F 80 10 80  W.@........@....
0250: 01 10 1D 80 01 91 02 02  00 10 1E 80 00 74 02 40  .............t.@
0260: 00 80 0E 80 01 10 01 80  40 0F 80 10 80 01 10 1F  ........@.......
0270: 80 01 91 02 02 00 10 20  80 00 91 02 40 00 80 0E  ....... ....@...
0280: 80 01 10 01 80 40 0F 80  10 80 01 10 21 80 01 91  .....@......!...
0290: 02 01 87 04 02 00 10 02  80 00 30 04 24 22 80 00  ..........0.$"..
02A0: 80 00 80 25 02 00 10 00  80 00 B4 02 03 01 10 0C  ...%............
02B0: 80 01 2D 04 02 00 10 01  80 00 D1 02 40 00 80 0E  ..-.........@...
02C0: 80 01 10 02 80 40 0F 80  10 80 01 10 00 80 01 2D  .....@.........-
02D0: 04 02 00 10 02 80 00 EE  02 40 00 80 0E 80 01 10  .........@......
02E0: 02 80 40 0F 80 10 80 01  10 04 80 01 2D 04 02 00  ..@.........-...
02F0: 10 06 80 00 0B 03 40 00  80 0E 80 01 10 02 80 40  ......@........@
0300: 0F 80 10 80 01 10 05 80  01 2D 04 02 00 10 07 80  .........-......
0310: 00 28 03 40 00 80 0E 80  01 10 02 80 40 0F 80 10  .(.@........@...
0320: 80 01 10 11 80 01 2D 04  02 00 10 09 80 00 45 03  ......-.......E.
0330: 40 00 80 0E 80 01 10 02  80 40 0F 80 10 80 01 10  @........@......
0340: 12 80 01 2D 04 02 00 10  08 80 00 62 03 40 00 80  ...-.......b.@..
0350: 0E 80 01 10 02 80 40 0F  80 10 80 01 10 13 80 01  ......@.........
0360: 2D 04 02 00 10 14 80 00  7F 03 40 00 80 0E 80 01  -.........@.....
0370: 10 02 80 40 0F 80 10 80  01 10 15 80 01 2D 04 02  ...@.........-..
0380: 00 10 16 80 00 9C 03 40  00 80 0E 80 01 10 02 80  .......@........
0390: 40 0F 80 10 80 01 10 17  80 01 2D 04 02 00 10 18  @.........-.....
03A0: 80 00 B9 03 40 00 80 0E  80 01 10 02 80 40 0F 80  ....@........@..
03B0: 10 80 01 10 19 80 01 2D  04 02 00 10 1A 80 00 D6  .......-........
03C0: 03 40 00 80 0E 80 01 10  02 80 40 0F 80 10 80 01  .@........@.....
03D0: 10 1B 80 01 2D 04 02 00  10 1C 80 00 F3 03 40 00  ....-.........@.
03E0: 80 0E 80 01 10 02 80 40  0F 80 10 80 01 10 1D 80  .......@........
03F0: 01 2D 04 02 00 10 1E 80  00 10 04 40 00 80 0E 80  .-.........@....
0400: 01 10 02 80 40 0F 80 10  80 01 10 1F 80 01 2D 04  ....@.........-.
0410: 02 00 10 20 80 00 2D 04  40 00 80 0E 80 01 10 02  ... ..-.@.......
0420: 80 40 0F 80 10 80 01 10  21 80 01 2D 04 01 87 04  .@......!..-....
0430: 02 00 10 06 80 00 4D 04  40 00 80 0E 80 01 10 06  ......M.@.......
0440: 80 40 0F 80 10 80 01 10  00 80 01 87 04 02 00 10  .@..............
0450: 07 80 00 6A 04 40 00 80  0E 80 01 10 07 80 40 0F  ...j.@........@.
0460: 80 10 80 01 10 00 80 01  87 04 02 00 10 09 80 00  ................
0470: 87 04 40 00 80 0E 80 01  10 09 80 40 0F 80 10 80  ..@........@....
0480: 01 10 00 80 01 87 04 42  21 00                    .......B!.      
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  3: 0x000D [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  4: 0x0012 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  5: 0x0017 [0x03] Work_Zone[2] = 0*
  6: 0x001C [0x03] Work_Zone[3] = 0*
  7: 0x0021 [0x03] Work_Zone[4] = 0*
  8: 0x0026 [0x03] Work_Zone[5] = 0*
  9: 0x002B [0x03] Work_Zone[6] = 0*
 10: 0x0030 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 11: 0x0035 [0x03] Work_Zone[3] = 0*
 12: 0x003A [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 0*) GOTO 0x0049
 13: 0x0041 [0x03] Work_Zone[4] = 1*
 14: 0x0046 [0x01] GOTO 0x004E
 15: 0x0049 [0x03] Work_Zone[4] = 0*

SUBROUTINE_004E:
 16: 0x004E [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 1*) GOTO 0x005D
 17: 0x0055 [0x03] Work_Zone[5] = 1*
 18: 0x005A [0x01] GOTO 0x0062
 19: 0x005D [0x03] Work_Zone[5] = 0*

SUBROUTINE_0062:
 20: 0x0062 [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 2*) GOTO 0x0071
 21: 0x0069 [0x03] Work_Zone[6] = 1*
 22: 0x006E [0x01] GOTO 0x0076
 23: 0x0071 [0x03] Work_Zone[6] = 0*

SUBROUTINE_0076:
 24: 0x0076 [0x48] [System] [7743*]:
    → "Time debug: Time limit: $0 [sec./min.] Time debug: Search flag: [OFF/ON] Time debug: Search flag switched ON flag: [OFF/ON] Time debug: Forced exit flag: [OFF/ON]"
 25: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x007A [0x03] ExtData[1]->WorkLocal[4] = 0*
 27: 0x007F [0x03] ExtData[1]->WorkLocal[5] = ExtData[1]->WorkLocal[1]
 28: 0x0084 [0x15] ExtData[1]->WorkLocal[5] /= 60*
 29: 0x0089 [0x02] IF !(ExtData[1]->WorkLocal[5] > 0*) GOTO 0x009B
 30: 0x0091 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[4], bit_index_work_offset=2*, condition_work_offset=1*)
 31: 0x0098 [0x01] GOTO 0x00AA
 32: 0x009B [0x02] IF !(ExtData[1]->WorkLocal[5] < 120*) GOTO 0x00AA
 33: 0x00A3 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[4], bit_index_work_offset=1*, condition_work_offset=1*)

SUBROUTINE_00AA:
 34: 0x00AA [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 1*) GOTO 0x00B4
 35: 0x00B1 [0x01] GOTO 0x00BB
 36: 0x00B4 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[4], bit_index_work_offset=3*, condition_work_offset=1*)

SUBROUTINE_00BB:
 37: 0x00BB [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 2*) GOTO 0x00C5
 38: 0x00C2 [0x01] GOTO 0x00CC
 39: 0x00C5 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[4], bit_index_work_offset=4*, condition_work_offset=1*)

SUBROUTINE_00CC:
 40: 0x00CC [0x02] IF !(ExtData[1]->WorkLocal[3] < 6*) GOTO 0x00DB
 41: 0x00D4 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[4], bit_index_work_offset=5*, condition_work_offset=1*)
 42: 0x00DB [0x03] Work_Zone[2] = 1271*
 43: 0x00E0 [0x24] CREATE_DIALOG(message_id=7744*, default_option=0*, option_flags=ExtData[1]->WorkLocal[4])
    → "Time debug: Do what? [Nuttin'./Increase time limit./Reduce time limit./Switch OFF "Search flag switched ON flag."/Forced exit flag OFF./Receive one $3.]"
 44: 0x00E7 [0x25] WAIT_DIALOG_SELECT()
 45: 0x00E8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F8
 46: 0x00F0 [0x03] Work_Zone[1] = 1073741824*
 47: 0x00F5 [0x01] GOTO 0x0487
 48: 0x00F8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0294
 49: 0x0100 [0x24] CREATE_DIALOG(message_id=7745*, default_option=0*, option_flags=0*)
    → "Time debug: Increase by how much? [Return./+0 minute./+1 minute./+2 minutes./+3 minutes./+5 minutes./+10 minutes./+15 minutes./+30 minutes./+45 minutes./+60 minutes./+75 minutes./+90 minutes./+120 minutes.]"
 50: 0x0107 [0x25] WAIT_DIALOG_SELECT()
 51: 0x0108 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0118
 52: 0x0110 [0x03] Work_Zone[1] = 1073741824*
 53: 0x0115 [0x01] GOTO 0x0291
 54: 0x0118 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0135
 55: 0x0120 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 56: 0x0129 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=0*)
 57: 0x0132 [0x01] GOTO 0x0291
 58: 0x0135 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0152
 59: 0x013D [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 60: 0x0146 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=60*)
 61: 0x014F [0x01] GOTO 0x0291
 62: 0x0152 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x016F
 63: 0x015A [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 64: 0x0163 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=120*)
 65: 0x016C [0x01] GOTO 0x0291
 66: 0x016F [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x018C
 67: 0x0177 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 68: 0x0180 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=180*)
 69: 0x0189 [0x01] GOTO 0x0291
 70: 0x018C [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x01A9
 71: 0x0194 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 72: 0x019D [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=300*)
 73: 0x01A6 [0x01] GOTO 0x0291
 74: 0x01A9 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x01C6
 75: 0x01B1 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 76: 0x01BA [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=600*)
 77: 0x01C3 [0x01] GOTO 0x0291
 78: 0x01C6 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x01E3
 79: 0x01CE [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 80: 0x01D7 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=900*)
 81: 0x01E0 [0x01] GOTO 0x0291
 82: 0x01E3 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x0200
 83: 0x01EB [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 84: 0x01F4 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=1800*)
 85: 0x01FD [0x01] GOTO 0x0291
 86: 0x0200 [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x021D
 87: 0x0208 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 88: 0x0211 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=2700*)
 89: 0x021A [0x01] GOTO 0x0291
 90: 0x021D [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x023A
 91: 0x0225 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 92: 0x022E [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=3600*)
 93: 0x0237 [0x01] GOTO 0x0291
 94: 0x023A [0x02] IF !(Work_Zone[0] == 11*) GOTO 0x0257
 95: 0x0242 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
 96: 0x024B [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=4500*)
 97: 0x0254 [0x01] GOTO 0x0291
 98: 0x0257 [0x02] IF !(Work_Zone[0] == 12*) GOTO 0x0274
 99: 0x025F [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
100: 0x0268 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=5400*)
101: 0x0271 [0x01] GOTO 0x0291
102: 0x0274 [0x02] IF !(Work_Zone[0] == 13*) GOTO 0x0291
103: 0x027C [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=1*)
104: 0x0285 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=7200*)
105: 0x028E [0x01] GOTO 0x0291

SUBROUTINE_0291:
106: 0x0291 [0x01] GOTO 0x0487
107: 0x0294 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0430
108: 0x029C [0x24] CREATE_DIALOG(message_id=7746*, default_option=0*, option_flags=0*)
    → "Time debug: Reduce by how much? [`Gi/-0 minute./-1 minute./-2 minutes./-3 minutes./-5 minutes./-10 minutes./-15 minutes./-30 minutes./-45 minutes./-60 minutes./-75 minutes./-90 minutes./-120 minutes.]"
109: 0x02A3 [0x25] WAIT_DIALOG_SELECT()
110: 0x02A4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02B4
111: 0x02AC [0x03] Work_Zone[1] = 1073741824*
112: 0x02B1 [0x01] GOTO 0x042D
113: 0x02B4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02D1
114: 0x02BC [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
115: 0x02C5 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=0*)
116: 0x02CE [0x01] GOTO 0x042D
117: 0x02D1 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x02EE
118: 0x02D9 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
119: 0x02E2 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=60*)
120: 0x02EB [0x01] GOTO 0x042D
121: 0x02EE [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x030B
122: 0x02F6 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
123: 0x02FF [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=120*)
124: 0x0308 [0x01] GOTO 0x042D
125: 0x030B [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0328
126: 0x0313 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
127: 0x031C [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=180*)
128: 0x0325 [0x01] GOTO 0x042D
129: 0x0328 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0345
130: 0x0330 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
131: 0x0339 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=300*)
132: 0x0342 [0x01] GOTO 0x042D
133: 0x0345 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0362
134: 0x034D [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
135: 0x0356 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=600*)
136: 0x035F [0x01] GOTO 0x042D
137: 0x0362 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x037F
138: 0x036A [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
139: 0x0373 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=900*)
140: 0x037C [0x01] GOTO 0x042D
141: 0x037F [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x039C
142: 0x0387 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
143: 0x0390 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=1800*)
144: 0x0399 [0x01] GOTO 0x042D
145: 0x039C [0x02] IF !(Work_Zone[0] == 9*) GOTO 0x03B9
146: 0x03A4 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
147: 0x03AD [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=2700*)
148: 0x03B6 [0x01] GOTO 0x042D
149: 0x03B9 [0x02] IF !(Work_Zone[0] == 10*) GOTO 0x03D6
150: 0x03C1 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
151: 0x03CA [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=3600*)
152: 0x03D3 [0x01] GOTO 0x042D
153: 0x03D6 [0x02] IF !(Work_Zone[0] == 11*) GOTO 0x03F3
154: 0x03DE [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
155: 0x03E7 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=4500*)
156: 0x03F0 [0x01] GOTO 0x042D
157: 0x03F3 [0x02] IF !(Work_Zone[0] == 12*) GOTO 0x0410
158: 0x03FB [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
159: 0x0404 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=5400*)
160: 0x040D [0x01] GOTO 0x042D
161: 0x0410 [0x02] IF !(Work_Zone[0] == 13*) GOTO 0x042D
162: 0x0418 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2*)
163: 0x0421 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=7200*)
164: 0x042A [0x01] GOTO 0x042D

SUBROUTINE_042D:
165: 0x042D [0x01] GOTO 0x0487
166: 0x0430 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x044D
167: 0x0438 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=3*)
168: 0x0441 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=0*)
169: 0x044A [0x01] GOTO 0x0487
170: 0x044D [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x046A
171: 0x0455 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=4*)
172: 0x045E [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=0*)
173: 0x0467 [0x01] GOTO 0x0487
174: 0x046A [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0487
175: 0x0472 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=5*)
176: 0x047B [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=0*)
177: 0x0484 [0x01] GOTO 0x0487

SUBROUTINE_0487:
178: 0x0487 [0x42] SET_CLI_EVENT_CANCEL_DATA()
179: 0x0488 [0x21] END_EVENT
180: 0x0489 [0x00] END_REQSTACK()
```
