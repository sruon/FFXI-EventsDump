# 17756500 - Enigmatic Footprints 2

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 688 bytes                |
| Total Events     | 2                        |
| References Count | 31                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [581](#event-581)     | 0x0001       |    537 |            119 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0004      |           4 |
|       1 | 0x2AB2      |       10930 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x000E      |          14 |
|       5 | 0x0002      |           2 |
|       6 | 0x000F      |          15 |
|       7 | 0x0003      |           3 |
|       8 | 0x40000000  |  1073741824 |
|       9 | 0x2A8D      |       10893 |
|      10 | 0x2ABB      |       10939 |
|      11 | 0x2A7E      |       10878 |
|      12 | 0x0010      |          16 |
|      13 | 0x2ABC      |       10940 |
|      14 | 0x2ABD      |       10941 |
|      15 | 0x0708      |        1800 |
|      16 | 0x0E10      |        3600 |
|      17 | 0x1518      |        5400 |
|      18 | 0x0C54      |        3156 |
|      19 | 0x003C      |          60 |
|      20 | 0x2AB3      |       10931 |
|      21 | 0x2AB4      |       10932 |
|      22 | 0x2AB5      |       10933 |
|      23 | 0x2AB6      |       10934 |
|      24 | 0x2AB7      |       10935 |
|      25 | 0x2AB8      |       10936 |
|      26 | 0x2AB9      |       10937 |
|      27 | 0x005A      |          90 |
|      28 | 0x00C9      |         201 |
|      29 | 0x002D      |          45 |
|      30 | 0x00C8      |         200 |

## String References

- **10878**: [Apply to proceed/Proceed]? [Definitely!/Not yet.]
- **10893**: Treasure chest bonuses are now active!
- **10930**: Enter [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] (Shared)? [No thanks./Enter. (CL: $1)/Check area status./About sharing.]
- **10931**: Shared is a status where solo adventurers all join the same instance.
- **10932**: Players can enter once per day (Earth time), and this applies to all Dynamis - Divergence shared areas.
- **10933**: This does not apply to non-shared Dynamis - Divergence instances.
- **10934**: Shared [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] instaces are open for two hours starting at : (JST) and have a time limit of $11 minutes. Unlike non-shared instances, this time cannot be extended.
- **10935**: If the instance is late to open, the time limit will be extended by a similar amount.
- **10936**: The instane will close when the time limit is reached or the Wave 2 boss monster is defeated.
- **10937**: You can check wave and monster status from the Check Area Status dialog selection.
- **10939**: Entering [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] (Shared). Proceed?
- **10940**: You have chosen not to enter [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] (Shared).
- **10941**: Entering [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] (Shared).

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

### Event 581

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 537 bytes |
| Instructions | 105       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 07 00 02 10 03  04 00 03 10 03 13 00 04   B..............
0010: 10 03 14 00 05 10 03 0E  00 06 10 03 10 00 08 10  ................
0020: 03 12 00 09 10 05 08 00  03 02 10 10 00 3E 0E 00  .............>..
0030: 00 80 3A 00 05 15 00 01  3D 00 06 15 00 03 03 10  ..:.....=.......
0040: 04 00 24 01 80 02 80 07  00 25 02 00 10 03 80 00  ..$......%......
0050: 73 00 02 15 00 02 80 00  70 00 1A 28 01 03 01 10  s.......p..(....
0060: 02 80 3C 01 10 04 80 03  80 43 00 43 01 05 15 00  ..<......C.C....
0070: 01 C4 00 02 00 10 05 80  00 91 00 03 01 10 02 80  ................
0080: 3C 01 10 06 80 03 80 43  00 43 01 01 28 00 01 C4  <......C.C..(...
0090: 00 02 00 10 07 80 00 BD  00 1A 28 01 02 15 00 02  ..........(.....
00A0: 80 00 B7 00 03 01 10 02  80 3C 01 10 04 80 03 80  .........<......
00B0: 43 00 43 01 05 15 00 01  28 00 01 C4 00 03 01 10  C.C.....(.......
00C0: 08 80 21 00 02 12 00 02  80 01 CF 00 48 09 80 03  ..!.........H...
00D0: 02 10 10 00 48 0A 80 23  24 0B 80 02 80 02 80 25  ....H..#$......%
00E0: 02 00 10 02 80 00 06 01  03 01 10 02 80 3C 01 10  .............<..
00F0: 0C 80 03 80 43 00 43 01  02 09 10 02 80 01 03 01  ....C.C.........
0100: 01 28 00 01 15 01 03 02  10 10 00 48 0D 80 03 01  .(.........H....
0110: 10 08 80 21 00 03 02 10  10 00 48 0E 80 23 1A AD  ...!......H..#..
0120: 01 03 01 10 05 80 21 00  02 10 00 02 80 80 3D 01  ......!.......=.
0130: 03 02 10 02 80 03 02 17  02 80 01 86 01 02 10 00  ................
0140: 03 80 80 52 01 03 02 10  03 80 03 02 17 0F 80 01  ...R............
0150: 86 01 02 10 00 05 80 80  67 01 03 02 10 05 80 03  ........g.......
0160: 02 17 10 80 01 86 01 02  10 00 07 80 80 7C 01 03  .............|..
0170: 02 10 07 80 03 02 17 11  80 01 86 01 03 02 10 02  ................
0180: 80 03 02 17 02 80 03 04  10 12 80 03 03 17 13 80  ................
0190: 48 14 80 23 48 15 80 23  48 16 80 23 48 17 80 23  H..#H..#H..#H..#
01A0: 48 18 80 23 48 19 80 23  48 1A 80 23 1B 62 03 80  H..#H..#H..#.b..
01B0: F0 FF FF 7F F0 FF FF 7F  6D 61 69 6E 02 80 1C 1B  ........main....
01C0: 80 45 1C 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 31  .E..........who1
01D0: 02 80 55 1C 80 F0 FF FF  7F F0 FF FF 7F 77 68 6F  ..U..........who
01E0: 31 1C 1D 80 45 1E 80 F0  FF FF 7F F0 FF FF 7F 66  1...E..........f
01F0: 64 6F 31 02 80 55 1E 80  F0 FF FF 7F F0 FF FF 7F  do1..U..........
0200: 66 64 6F 31 45 1C 80 F0  FF FF 7F F0 FF FF 7F 77  fdo1E..........w
0210: 68 69 31 02 80 1C 06 80  30 1B                    hi1.....0.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[2]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[3]
  3: 0x000C [0x03] ExtData[1]->WorkLocal[19] = Work_Zone[4]
  4: 0x0011 [0x03] ExtData[1]->WorkLocal[20] = Work_Zone[5]
  5: 0x0016 [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[6]
  6: 0x001B [0x03] ExtData[1]->WorkLocal[16] = Work_Zone[8]
  7: 0x0020 [0x03] ExtData[1]->WorkLocal[18] = Work_Zone[9]
  8: 0x0025 [0x05] ExtData[1]->WorkLocal[8] = 1
  9: 0x0028 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[16]
 10: 0x002D [0x3E] IF !(ExtData[1]->WorkLocal[14] bit 4*) GOTO 0x003A
 11: 0x0034 [0x05] ExtData[1]->WorkLocal[21] = 1
 12: 0x0037 [0x01] GOTO 0x003D
 13: 0x003A [0x06] ExtData[1]->WorkLocal[21] = 0

SUBROUTINE_003D:
 14: 0x003D [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[4]
 15: 0x0042 [0x24] CREATE_DIALOG(message_id=10930*, default_option=0*, option_flags=ExtData[1]->WorkLocal[7])
    → "Enter [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] (Shared)? [No thanks./Enter. (CL: $1)/Check area status./About sharing.]"
 16: 0x0049 [0x25] WAIT_DIALOG_SELECT()
 17: 0x004A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0073
 18: 0x0052 [0x02] IF !(ExtData[1]->WorkLocal[21] == 0*) GOTO 0x0070
 19: 0x005A [0x1A] CALL_SUBROUTINE(address=0x0128)
 20: 0x005D [0x03] Work_Zone[1] = 0*
 21: 0x0062 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[1], bit_index_work_offset=14*, condition_work_offset=1*)
 22: 0x0069 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 23: 0x006B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 24: 0x006D [0x05] ExtData[1]->WorkLocal[21] = 1
 25: 0x0070 [0x01] GOTO 0x00C4
 26: 0x0073 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0091
 27: 0x007B [0x03] Work_Zone[1] = 0*
 28: 0x0080 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[1], bit_index_work_offset=15*, condition_work_offset=1*)
 29: 0x0087 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 30: 0x0089 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 31: 0x008B [0x01] GOTO 0x0028

SUBROUTINE_00C4:
 32: 0x00C4 [0x02] IF !(ExtData[1]->WorkLocal[18] == 0*) GOTO 0x00CF
 33: 0x00CC [0x48] [System] [10893*]:
    → "Treasure chest bonuses are now active!"
 34: 0x00CF [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[16]
 35: 0x00D4 [0x48] [System] [10939*]:
    → "Entering [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] (Shared). Proceed?"
 36: 0x00D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x00D8 [0x24] CREATE_DIALOG(message_id=10878*, default_option=0*, option_flags=0*)
    → "[Apply to proceed/Proceed]? [Definitely!/Not yet.]"
 38: 0x00DF [0x25] WAIT_DIALOG_SELECT()
 39: 0x00E0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0106
 40: 0x00E8 [0x03] Work_Zone[1] = 0*
 41: 0x00ED [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[1], bit_index_work_offset=16*, condition_work_offset=1*)
 42: 0x00F4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 43: 0x00F6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 44: 0x00F8 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x0103
 45: 0x0100 [0x01] GOTO 0x0028
 46: 0x0103 [0x01] GOTO 0x0115
 47: 0x0106 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[16]
 48: 0x010B [0x48] [System] [10940*]:
    → "You have chosen not to enter [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] (Shared)."
 49: 0x010E [0x03] Work_Zone[1] = 1073741824*
 50: 0x0113 [0x21] END_EVENT
 51: 0x0114 [0x00] END_REQSTACK()

SUBROUTINE_0115:
 52: 0x0115 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[16]
 53: 0x011A [0x48] [System] [10941*]:
    → "Entering [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] (Shared)."
 54: 0x011D [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x011E [0x1A] CALL_SUBROUTINE(address=0x01AD)
 56: 0x0121 [0x03] Work_Zone[1] = 2*
 57: 0x0126 [0x21] END_EVENT
 58: 0x0127 [0x00] END_REQSTACK()

SUBROUTINE_0128:
 59: 0x0128 [0x02] IF !(ExtData[1]->WorkLocal[16] == 0*) GOTO 0x013D
 60: 0x0130 [0x03] Work_Zone[2] = 0*
 61: 0x0135 [0x03] Work_Zone_1700[2] = 0*
 62: 0x013A [0x01] GOTO 0x0186
 63: 0x013D [0x02] IF !(ExtData[1]->WorkLocal[16] == 1*) GOTO 0x0152
 64: 0x0145 [0x03] Work_Zone[2] = 1*
 65: 0x014A [0x03] Work_Zone_1700[2] = 1800*
 66: 0x014F [0x01] GOTO 0x0186
 67: 0x0152 [0x02] IF !(ExtData[1]->WorkLocal[16] == 2*) GOTO 0x0167
 68: 0x015A [0x03] Work_Zone[2] = 2*
 69: 0x015F [0x03] Work_Zone_1700[2] = 3600*
 70: 0x0164 [0x01] GOTO 0x0186
 71: 0x0167 [0x02] IF !(ExtData[1]->WorkLocal[16] == 3*) GOTO 0x017C
 72: 0x016F [0x03] Work_Zone[2] = 3*
 73: 0x0174 [0x03] Work_Zone_1700[2] = 5400*
 74: 0x0179 [0x01] GOTO 0x0186
 75: 0x017C [0x03] Work_Zone[2] = 0*
 76: 0x0181 [0x03] Work_Zone_1700[2] = 0*

SUBROUTINE_0186:
 77: 0x0186 [0x03] Work_Zone[4] = 3156*
 78: 0x018B [0x03] Work_Zone_1700[3] = 60*
 79: 0x0190 [0x48] [System] [10931*]:
    → "Shared is a status where solo adventurers all join the same instance."
 80: 0x0193 [0x23] WAIT_FOR_DIALOG_INTERACTION
 81: 0x0194 [0x48] [System] [10932*]:
    → "Players can enter once per day (Earth time), and this applies to all Dynamis - Divergence shared areas."
 82: 0x0197 [0x23] WAIT_FOR_DIALOG_INTERACTION
 83: 0x0198 [0x48] [System] [10933*]:
    → "This does not apply to non-shared Dynamis - Divergence instances."
 84: 0x019B [0x23] WAIT_FOR_DIALOG_INTERACTION
 85: 0x019C [0x48] [System] [10934*]:
    → "Shared [D. San d'Oria/D. Bastok/D. Windurst/D. Jeuno] instaces are open for two hours starting at : (JST) and have a time limit of $11 minutes. Unlike non-shared instances, this time cannot be extended."
 86: 0x019F [0x23] WAIT_FOR_DIALOG_INTERACTION
 87: 0x01A0 [0x48] [System] [10935*]:
    → "If the instance is late to open, the time limit will be extended by a similar amount."
 88: 0x01A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 89: 0x01A4 [0x48] [System] [10936*]:
    → "The instane will close when the time limit is reached or the Wave 2 boss monster is defeated."
 90: 0x01A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 91: 0x01A8 [0x48] [System] [10937*]:
    → "You can check wave and monster status from the Check Area Status dialog selection."
 92: 0x01AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 93: 0x01AC [0x1B] RETURN

SUBROUTINE_01AD:
 94: 0x01AD [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
 95: 0x01BE [0x1C] WAIT(90* ticks)
 96: 0x01C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 97: 0x01D2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
 98: 0x01E1 [0x1C] WAIT(45* ticks)
 99: 0x01E4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
100: 0x01F5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
101: 0x0204 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
102: 0x0215 [0x1C] WAIT(15* ticks)
103: 0x0218 [0x30] SET_UCOFF_CONTINUE_ZERO()
104: 0x0219 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x008E [0x01] GOTO 0x00C4
     0x00BA [0x01] GOTO 0x00C4
```
