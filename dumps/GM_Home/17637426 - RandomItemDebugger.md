# 17637426 - RandomItemDebugger

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 564 bytes         |
| Total Events     | 2                 |
| References Count | 19                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [86](#event-86)       | 0x0001       |    460 |            102 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x0003      |           3 |
|       4 | 0x20002     |      131074 |
|       5 | 0x40003     |      262147 |
|       6 | 0x60005     |      393221 |
|       7 | 0x3001      |       12289 |
|       8 | 0x0010      |          16 |
|       9 | 0x0017      |          23 |
|      10 | 0x0018      |          24 |
|      11 | 0x001F      |          31 |
|      12 | 0x0004      |           4 |
|      13 | 0x0005      |           5 |
|      14 | 0x0006      |           6 |
|      15 | 0x0007      |           7 |
|      16 | 0x1DC4      |        7620 |
|      17 | 0x1DC5      |        7621 |
|      18 | 0x1DC6      |        7622 |

## String References

- **7620**: [First/Second] bonus! Get yer freshly baked [first/second] bonus! [Don't do me no favors./Accuracy +10/Attack +10/Ranged Accuracy +10/Ranged Attack +10/Evasion +10/"Magic Accuracy Bonus"+4/"Magic Attack Bonus"+4/Double Attack rate +2%/Critical hit rate +3%/"Store TP"+4 "Subtle Blow"+4/Enmity+5/Enimity-5/Enhances "Fast Casting" effect (+5%)/"Call Beast" ability delay -15/"Snap Shot"+5%/Enhances "Dual Wield" effect (+3%)/"Blood Pact" ability delay -4/Avatar perpetuation cost -2/"Quick Draw" ability delay -5/Pet: Accuracy+15 Ranged Accuracy+15/Pet: Attack+15 Ranged Attack+15/Pet: Magic Accuracy+7 Magic Attack+7/Pet: "Double Attack"+2% Critical hit rate+2%]
- **7621**: [First/Second] bonus! Get yer freshly baked [first/second] bonus! [Don't do me no favors./@Regen./@Refresh./@Double Attack +2%/@Haste +2%/@Beefed-up Dual Wield (3%)/@Store TP +5/@Subtle Blow +5/@@@"Blood Pact" ability delay -5/@Avatar perpetuation cost -1/@Charm +5/@Song spellcasting time -10%/@Beefed-up Fast Cast (5%)/@Critical hit rate +3%/@Magic Accuracy Bonus +5/@Magic Attack Bonus +5/@Is dat all ya got?]
- **7622**: [First/Second] bonus! Get yer freshly baked [first/second] bonus! [Don't do me no favors./@Pet: Accuracy +10/@Pet: Attack +10/@Pet: Magic Accuracy Bonus +10/@Pet: Magic Attack Bonus +5/@Pet: Critical hit rate +3%/@I sez, what else ya got?]

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

### Event 86

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 460 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 05 00 02 10 02 05  00 00 80 80 14 00 1A 45   ..............E
0010: 00 01 3E 00 02 05 00 01  80 80 22 00 1A 46 00 01  ..>......."..F..
0020: 3E 00 02 05 00 02 80 80  30 00 1A 47 00 01 3E 00  >.......0..G..>.
0030: 02 05 00 03 80 80 3E 00  1A 48 00 01 3E 00 03 01  ......>..H..>...
0040: 10 01 00 21 00 1B 1B 1B  1B 1A 4C 00 03 02 00 04  ...!......L.....
0050: 80 03 03 00 05 80 03 04  00 06 80 CC 01 07 80 02  ................
0060: 00 03 00 04 00 1B 03 06  00 01 80 02 06 00 00 80  ................
0070: 01 13 01 02 06 00 01 80  80 9E 00 06 01 00 1A 14  ................
0080: 01 02 00 00 00 80 01 96  00 03 01 00 00 00 03 06  ................
0090: 00 02 80 01 9B 00 03 06  00 00 80 01 10 01 02 06  ................
00A0: 00 02 80 80 CF 00 03 00  17 00 80 1A 1A 01 02 00  ................
00B0: 00 00 80 01 C7 00 40 08  80 09 80 01 00 00 00 03  ......@.........
00C0: 06 00 03 80 01 CC 00 03  06 00 01 80 01 10 01 02  ................
00D0: 06 00 03 80 80 00 01 03  00 17 01 80 1A 1A 01 02  ................
00E0: 00 00 00 80 01 F8 00 40  0A 80 0B 80 01 00 00 00  .......@........
00F0: 03 06 00 0C 80 01 FD 00  03 06 00 02 80 01 10 01  ................
0100: 02 06 00 0C 80 80 10 01  03 06 00 00 80 01 10 01  ................
0110: 01 6B 00 1B 03 00 00 07  80 1B 03 08 00 00 80 06  .k..............
0120: 07 00 02 07 00 00 80 00  57 01 02 08 00 00 80 80  ........W.......
0130: 38 01 1A 6A 01 01 54 01  02 08 00 01 80 80 46 01  8..j..T.......F.
0140: 1A 8B 01 01 54 01 02 08  00 02 80 80 54 01 1A AC  ....T.......T...
0150: 01 01 54 01 01 22 01 40  00 80 0D 80 00 00 09 00  ..T..".@........
0160: 40 0E 80 0F 80 00 00 08  00 1B 24 10 80 00 80 00  @.........$.....
0170: 80 25 02 00 10 0B 80 00  82 01 03 08 00 01 80 01  .%..............
0180: 8A 01 03 09 00 00 10 05  07 00 1B 24 11 80 00 80  ...........$....
0190: 00 80 25 02 00 10 08 80  00 A3 01 03 08 00 02 80  ..%.............
01A0: 01 AB 01 03 09 00 00 10  05 07 00 1B 24 12 80 00  ............$...
01B0: 80 00 80 25 02 00 10 0E  80 00 C4 01 03 08 00 00  ...%............
01C0: 80 01 CC 01 03 09 00 00  10 05 07 00 1B           .............   
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[2]
  1: 0x0006 [0x02] IF !(ExtData[1]->WorkLocal[5] == 0*) GOTO 0x0014
  2: 0x000E [0x1A] CALL_SUBROUTINE(address=0x0045)
  3: 0x0011 [0x01] GOTO 0x003E
  4: 0x0014 [0x02] IF !(ExtData[1]->WorkLocal[5] == 1*) GOTO 0x0022
  5: 0x001C [0x1A] CALL_SUBROUTINE(address=0x0046)
  6: 0x001F [0x01] GOTO 0x003E
  7: 0x0022 [0x02] IF !(ExtData[1]->WorkLocal[5] == 2*) GOTO 0x0030
  8: 0x002A [0x1A] CALL_SUBROUTINE(address=0x0047)
  9: 0x002D [0x01] GOTO 0x003E
 10: 0x0030 [0x02] IF !(ExtData[1]->WorkLocal[5] == 3*) GOTO 0x003E
 11: 0x0038 [0x1A] CALL_SUBROUTINE(address=0x0048)
 12: 0x003B [0x01] GOTO 0x003E

SUBROUTINE_003E:
 13: 0x003E [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[1]
 14: 0x0043 [0x21] END_EVENT
 15: 0x0044 [0x00] END_REQSTACK()

SUBROUTINE_0045:
 16: 0x0045 [0x1B] RETURN

SUBROUTINE_0046:
 17: 0x0046 [0x1B] RETURN

SUBROUTINE_0047:
 18: 0x0047 [0x1B] RETURN

SUBROUTINE_0048:
 19: 0x0048 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0049 [0x1A] CALL_SUBROUTINE(address=0x004C)
     0x004C [0x03] ExtData[1]->WorkLocal[2] = 131074*
     0x0051 [0x03] ExtData[1]->WorkLocal[3] = 262147*
     0x0056 [0x03] ExtData[1]->WorkLocal[4] = 393221*
     0x005B [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=12289*, buffer1=ExtData[1]->WorkLocal[2], buffer2=ExtData[1]->WorkLocal[3], buffer3=ExtData[1]->WorkLocal[4])
     0x0065 [0x1B] RETURN
     0x0066 [0x03] ExtData[1]->WorkLocal[6] = 1*
     0x006B [0x02] IF !(ExtData[1]->WorkLocal[6] == 0*) GOTO 0x0113
     0x0073 [0x02] IF !(ExtData[1]->WorkLocal[6] == 1*) GOTO 0x009E
     0x007B [0x06] ExtData[1]->WorkLocal[1] = 0
     0x007E [0x1A] CALL_SUBROUTINE(address=0x0114)
     0x0081 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0096
     0x0089 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x008E [0x03] ExtData[1]->WorkLocal[6] = 2*
     0x0093 [0x01] GOTO 0x009B
     0x0096 [0x03] ExtData[1]->WorkLocal[6] = 0*
     0x009B [0x01] GOTO 0x0110
     0x009E [0x02] IF !(ExtData[1]->WorkLocal[6] == 2*) GOTO 0x00CF
     0x00A6 [0x03] Work_Zone_1700[0] = 0*
     0x00AB [0x1A] CALL_SUBROUTINE(address=0x011A)
     0x00AE [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x00C7
     0x00B6 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=23*, target=ExtData[1]->WorkLocal[1], source=ExtData[1]->WorkLocal[0])
     0x00BF [0x03] ExtData[1]->WorkLocal[6] = 3*
     0x00C4 [0x01] GOTO 0x00CC
     0x00C7 [0x03] ExtData[1]->WorkLocal[6] = 1*
     0x00CC [0x01] GOTO 0x0110
     0x00CF [0x02] IF !(ExtData[1]->WorkLocal[6] == 3*) GOTO 0x0100
     0x00D7 [0x03] Work_Zone_1700[0] = 1*
     0x00DC [0x1A] CALL_SUBROUTINE(address=0x011A)
     0x00DF [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x00F8
     0x00E7 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=ExtData[1]->WorkLocal[1], source=ExtData[1]->WorkLocal[0])
     0x00F0 [0x03] ExtData[1]->WorkLocal[6] = 4*
     0x00F5 [0x01] GOTO 0x00FD
     0x00F8 [0x03] ExtData[1]->WorkLocal[6] = 2*
     0x00FD [0x01] GOTO 0x0110
     0x0100 [0x02] IF !(ExtData[1]->WorkLocal[6] == 4*) GOTO 0x0110
     0x0108 [0x03] ExtData[1]->WorkLocal[6] = 0*
     0x010D [0x01] GOTO 0x0110
     0x0110 [0x01] GOTO 0x006B
     0x0113 [0x1B] RETURN
     0x0114 [0x03] ExtData[1]->WorkLocal[0] = 12289*
     0x0119 [0x1B] RETURN
     0x011A [0x03] ExtData[1]->WorkLocal[8] = 0*
     0x011F [0x06] ExtData[1]->WorkLocal[7] = 0
     0x0122 [0x02] IF !(ExtData[1]->WorkLocal[7] == 0*) GOTO 0x0157
     0x012A [0x02] IF !(ExtData[1]->WorkLocal[8] == 0*) GOTO 0x0138
     0x0132 [0x1A] CALL_SUBROUTINE(address=0x016A)
     0x0135 [0x01] GOTO 0x0154
     0x0138 [0x02] IF !(ExtData[1]->WorkLocal[8] == 1*) GOTO 0x0146
     0x0140 [0x1A] CALL_SUBROUTINE(address=0x018B)
     0x0143 [0x01] GOTO 0x0154
     0x0146 [0x02] IF !(ExtData[1]->WorkLocal[8] == 2*) GOTO 0x0154
     0x014E [0x1A] CALL_SUBROUTINE(address=0x01AC)
     0x0151 [0x01] GOTO 0x0154
     0x0154 [0x01] GOTO 0x0122
     0x0157 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=5*, target=ExtData[1]->WorkLocal[0], source=ExtData[1]->WorkLocal[9])
     0x0160 [0x40] SET_BIT_WORK_RANGE(start_bit=6*, end_bit=7*, target=ExtData[1]->WorkLocal[0], source=ExtData[1]->WorkLocal[8])
     0x0169 [0x1B] RETURN
     0x016A [0x24] CREATE_DIALOG(message_id=7620*, default_option=0*, option_flags=0*)
    → "[First/Second] bonus! Get yer freshly baked [first/second] bonus! [Don't do me no favors./Accuracy +10/Attack +10/Ranged Accuracy +10/Ranged Attack +10/Evasion +10/"Magic Accuracy Bonus"+4/"Magic Attack Bonus"+4/Double Attack rate +2%/Critical hit rate +3%/"Store TP"+4 "Subtle Blow"+4/Enmity+5/Enimity-5/Enhances "Fast Casting" effect (+5%)/"Call Beast" ability delay -15/"Snap Shot"+5%/Enhances "Dual Wield" effect (+3%)/"Blood Pact" ability delay -4/Avatar perpetuation cost -2/"Quick Draw" ability delay -5/Pet: Accuracy+15 Ranged Accuracy+15/Pet: Attack+15 Ranged Attack+15/Pet: Magic Accuracy+7 Magic Attack+7/Pet: "Double Attack"+2% Critical hit rate+2%]"
     0x0171 [0x25] WAIT_DIALOG_SELECT()
     0x0172 [0x02] IF !(Work_Zone[0] == 31*) GOTO 0x0182
     0x017A [0x03] ExtData[1]->WorkLocal[8] = 1*
     0x017F [0x01] GOTO 0x018A
     0x0182 [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
     0x0187 [0x05] ExtData[1]->WorkLocal[7] = 1
     0x018A [0x1B] RETURN
     0x018B [0x24] CREATE_DIALOG(message_id=7621*, default_option=0*, option_flags=0*)
    → "[First/Second] bonus! Get yer freshly baked [first/second] bonus! [Don't do me no favors./@Regen./@Refresh./@Double Attack +2%/@Haste +2%/@Beefed-up Dual Wield (3%)/@Store TP +5/@Subtle Blow +5/@@@"Blood Pact" ability delay -5/@Avatar perpetuation cost -1/@Charm +5/@Song spellcasting time -10%/@Beefed-up Fast Cast (5%)/@Critical hit rate +3%/@Magic Accuracy Bonus +5/@Magic Attack Bonus +5/@Is dat all ya got?]"
     0x0192 [0x25] WAIT_DIALOG_SELECT()
     0x0193 [0x02] IF !(Work_Zone[0] == 16*) GOTO 0x01A3
     0x019B [0x03] ExtData[1]->WorkLocal[8] = 2*
     0x01A0 [0x01] GOTO 0x01AB
     0x01A3 [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
     0x01A8 [0x05] ExtData[1]->WorkLocal[7] = 1
     0x01AB [0x1B] RETURN
     0x01AC [0x24] CREATE_DIALOG(message_id=7622*, default_option=0*, option_flags=0*)
    → "[First/Second] bonus! Get yer freshly baked [first/second] bonus! [Don't do me no favors./@Pet: Accuracy +10/@Pet: Attack +10/@Pet: Magic Accuracy Bonus +10/@Pet: Magic Attack Bonus +5/@Pet: Critical hit rate +3%/@I sez, what else ya got?]"
     0x01B3 [0x25] WAIT_DIALOG_SELECT()
     0x01B4 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x01C4
     0x01BC [0x03] ExtData[1]->WorkLocal[8] = 0*
     0x01C1 [0x01] GOTO 0x01CC
     0x01C4 [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
     0x01C9 [0x05] ExtData[1]->WorkLocal[7] = 1
     0x01CC [0x1B] RETURN
```
