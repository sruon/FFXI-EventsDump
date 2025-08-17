# 17637617 - Debug_MonsterPlay

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 636 bytes         |
| Total Events     | 2                 |
| References Count | 26                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [168](#event-168)     | 0x0001       |    506 |             93 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x237C      |        9084 |
|       2 | 0x0064      |         100 |
|       3 | 0x0065      |         101 |
|       4 | 0x006A      |         106 |
|       5 | 0x006B      |         107 |
|       6 | 0x0073      |         115 |
|       7 | 0x0074      |         116 |
|       8 | 0x237D      |        9085 |
|       9 | 0x0001      |           1 |
|      10 | 0x0002      |           2 |
|      11 | 0x0003      |           3 |
|      12 | 0x0004      |           4 |
|      13 | 0x0005      |           5 |
|      14 | 0x0006      |           6 |
|      15 | 0x0007      |           7 |
|      16 | 0x237E      |        9086 |
|      17 | 0x237F      |        9087 |
|      18 | 0x2382      |        9090 |
|      19 | 0x000F      |          15 |
|      20 | 0x0010      |          16 |
|      21 | 0x001F      |          31 |
|      22 | 0x0078      |         120 |
|      23 | 0x00C8      |         200 |
|      24 | 0x2380      |        9088 |
|      25 | 0x2381      |        9089 |

## String References

- **9084**: Vague images of worlds beyond coalesce and diffuse within.
- **9085**: Where to, intrepid pioneer? [$8./$8./$8./$8./$8./$8./Away from Monstrosity./Away from this menu!]
- **9086**: You dare trek to $8?
- **9087**: Well, do you? [Oh, I do./Nope. Cold feet.]
- **9088**: You truly wish to end your relationsip with this content, despite all the fun times you've had together?
- **9089**: Truly end it all? [Yes, I must!/No, not yet!]
- **9090**: Where in $8? [Point 1./Point 2./Point 3./Point 4./Point 5./Nowhere.]

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

### Event 168

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 506 bytes |
| Instructions | 93        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 01 10 00 80 48 01  80 23 05 00 00 03 02 00   .....H..#......
0010: 02 10 02 00 00 00 80 02  F9 01 03 02 10 02 80 03  ................
0020: 03 10 03 80 03 04 10 04  80 03 05 10 05 80 03 06  ................
0030: 10 06 80 03 07 10 07 80  24 08 80 00 80 00 80 25  ........$......%
0040: 02 00 10 00 80 00 50 00  03 01 00 02 80 01 BE 00  ......P.........
0050: 02 00 10 09 80 00 60 00  03 01 00 03 80 01 BE 00  ......`.........
0060: 02 00 10 0A 80 00 70 00  03 01 00 04 80 01 BE 00  ......p.........
0070: 02 00 10 0B 80 00 80 00  03 01 00 05 80 01 BE 00  ................
0080: 02 00 10 0C 80 00 90 00  03 01 00 06 80 01 BE 00  ................
0090: 02 00 10 0D 80 00 A0 00  03 01 00 07 80 01 BE 00  ................
00A0: 02 00 10 0E 80 00 B0 00  03 01 00 00 80 01 BE 00  ................
00B0: 02 00 10 0F 80 00 BE 00  06 00 00 01 BE 00 02 00  ................
00C0: 00 00 80 01 F6 01 02 01  00 00 80 01 B6 01 03 02  ................
00D0: 10 01 00 48 10 80 23 24  11 80 00 80 00 80 25 02  ...H..#$......%.
00E0: 00 10 00 80 00 A8 01 03  03 00 00 80 02 02 00 00  ................
00F0: 80 01 4B 01 03 02 10 01  00 24 12 80 00 80 00 80  ..K......$......
0100: 25 02 00 10 00 80 00 0C  01 01 43 01 02 00 10 09  %.........C.....
0110: 80 00 17 01 01 43 01 02  00 10 0A 80 00 22 01 01  .....C......."..
0120: 43 01 02 00 10 0B 80 00  2D 01 01 43 01 02 00 10  C.......-..C....
0130: 0C 80 00 38 01 01 43 01  02 00 10 0D 80 00 43 01  ...8..C.......C.
0140: 01 43 01 03 03 00 00 10  0B 03 00 02 03 00 0E 80  .C..............
0150: 01 A5 01 40 00 80 0B 80  01 10 09 80 40 0C 80 13  ...@........@...
0160: 80 01 10 01 00 40 14 80  15 80 01 10 03 00 06 00  .....@..........
0170: 00 62 09 80 F0 FF FF 7F  F0 FF FF 7F 6D 61 69 6E  .b..........main
0180: 00 80 1C 16 80 45 17 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0190: 66 64 6F 31 00 80 55 17  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
01A0: 7F 66 64 6F 31 01 B3 01  02 00 10 09 80 00 B3 01  .fdo1...........
01B0: 01 B3 01 01 F6 01 48 18  80 23 24 19 80 00 80 00  ......H..#$.....
01C0: 80 25 02 00 10 00 80 00  EB 01 40 00 80 0B 80 01  .%........@.....
01D0: 10 09 80 40 0C 80 13 80  01 10 01 00 40 14 80 15  ...@........@...
01E0: 80 01 10 03 00 06 00 00  01 F6 01 02 00 10 09 80  ................
01F0: 00 F6 01 01 F6 01 01 12  00 21 00                 .........!.     
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[1] = 0*
  1: 0x0006 [0x48] [System] [9084*]:
    → "Vague images of worlds beyond coalesce and diffuse within."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x05] ExtData[1]->WorkLocal[0] = 1
  4: 0x000D [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[2]
  5: 0x0012 [0x02] IF !(ExtData[1]->WorkLocal[0] <= 0*) GOTO 0x01F9
  6: 0x001A [0x03] Work_Zone[2] = 100*
  7: 0x001F [0x03] Work_Zone[3] = 101*
  8: 0x0024 [0x03] Work_Zone[4] = 106*
  9: 0x0029 [0x03] Work_Zone[5] = 107*
 10: 0x002E [0x03] Work_Zone[6] = 115*
 11: 0x0033 [0x03] Work_Zone[7] = 116*
 12: 0x0038 [0x24] CREATE_DIALOG(message_id=9085*, default_option=0*, option_flags=0*)
    → "Where to, intrepid pioneer? [$8./$8./$8./$8./$8./$8./Away from Monstrosity./Away from this menu!]"
 13: 0x003F [0x25] WAIT_DIALOG_SELECT()
 14: 0x0040 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0050
 15: 0x0048 [0x03] ExtData[1]->WorkLocal[1] = 100*
 16: 0x004D [0x01] GOTO 0x00BE
 17: 0x0050 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0060
 18: 0x0058 [0x03] ExtData[1]->WorkLocal[1] = 101*
 19: 0x005D [0x01] GOTO 0x00BE
 20: 0x0060 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0070
 21: 0x0068 [0x03] ExtData[1]->WorkLocal[1] = 106*
 22: 0x006D [0x01] GOTO 0x00BE
 23: 0x0070 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0080
 24: 0x0078 [0x03] ExtData[1]->WorkLocal[1] = 107*
 25: 0x007D [0x01] GOTO 0x00BE
 26: 0x0080 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0090
 27: 0x0088 [0x03] ExtData[1]->WorkLocal[1] = 115*
 28: 0x008D [0x01] GOTO 0x00BE
 29: 0x0090 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x00A0
 30: 0x0098 [0x03] ExtData[1]->WorkLocal[1] = 116*
 31: 0x009D [0x01] GOTO 0x00BE
 32: 0x00A0 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x00B0
 33: 0x00A8 [0x03] ExtData[1]->WorkLocal[1] = 0*
 34: 0x00AD [0x01] GOTO 0x00BE
 35: 0x00B0 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00BE
 36: 0x00B8 [0x06] ExtData[1]->WorkLocal[0] = 0
 37: 0x00BB [0x01] GOTO 0x00BE

SUBROUTINE_00BE:
 38: 0x00BE [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x01F6
 39: 0x00C6 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x01B6
 40: 0x00CE [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 41: 0x00D3 [0x48] [System] [9086*]:
    → "You dare trek to $8?"
 42: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x00D7 [0x24] CREATE_DIALOG(message_id=9087*, default_option=0*, option_flags=0*)
    → "Well, do you? [Oh, I do./Nope. Cold feet.]"
 44: 0x00DE [0x25] WAIT_DIALOG_SELECT()
 45: 0x00DF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01A8
 46: 0x00E7 [0x03] ExtData[1]->WorkLocal[3] = 0*
 47: 0x00EC [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x014B
 48: 0x00F4 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 49: 0x00F9 [0x24] CREATE_DIALOG(message_id=9090*, default_option=0*, option_flags=0*)
    → "Where in $8? [Point 1./Point 2./Point 3./Point 4./Point 5./Nowhere.]"
 50: 0x0100 [0x25] WAIT_DIALOG_SELECT()
 51: 0x0101 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x010C
 52: 0x0109 [0x01] GOTO 0x0143
 53: 0x010C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0117
 54: 0x0114 [0x01] GOTO 0x0143
 55: 0x0117 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0122
 56: 0x011F [0x01] GOTO 0x0143
 57: 0x0122 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x012D
 58: 0x012A [0x01] GOTO 0x0143
 59: 0x012D [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0138
 60: 0x0135 [0x01] GOTO 0x0143
 61: 0x0138 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0143
 62: 0x0140 [0x01] GOTO 0x0143

SUBROUTINE_0143:
 63: 0x0143 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[0]
 64: 0x0148 [0x0B] ExtData[1]->WorkLocal[3]++
 65: 0x014B [0x02] IF !(ExtData[1]->WorkLocal[3] == 6*) GOTO 0x01A5
 66: 0x0153 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=1*)
 67: 0x015C [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 68: 0x0165 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[3])
 69: 0x016E [0x06] ExtData[1]->WorkLocal[0] = 0
 70: 0x0171 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
 71: 0x0182 [0x1C] WAIT(120* ticks)
 72: 0x0185 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 73: 0x0196 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 74: 0x01A5 [0x01] GOTO 0x01B3
 75: 0x01A8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01B3
 76: 0x01B0 [0x01] GOTO 0x01B3

SUBROUTINE_01B3:
 77: 0x01B3 [0x01] GOTO 0x01F6
 78: 0x01B6 [0x48] [System] [9088*]:
    → "You truly wish to end your relationsip with this content, despite all the fun times you've had together?"
 79: 0x01B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 80: 0x01BA [0x24] CREATE_DIALOG(message_id=9089*, default_option=0*, option_flags=0*)
    → "Truly end it all? [Yes, I must!/No, not yet!]"
 81: 0x01C1 [0x25] WAIT_DIALOG_SELECT()
 82: 0x01C2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01EB
 83: 0x01CA [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=1*)
 84: 0x01D3 [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 85: 0x01DC [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[3])
 86: 0x01E5 [0x06] ExtData[1]->WorkLocal[0] = 0
 87: 0x01E8 [0x01] GOTO 0x01F6
 88: 0x01EB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01F6
 89: 0x01F3 [0x01] GOTO 0x01F6

SUBROUTINE_01F6:
 90: 0x01F6 [0x01] GOTO 0x0012
 91: 0x01F9 [0x21] END_EVENT
 92: 0x01FA [0x00] END_REQSTACK()
```
